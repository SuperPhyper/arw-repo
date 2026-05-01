#!/usr/bin/env python3
"""
spring_mass_cover.py
====================
Cover analysis for the vertical spring-mass chain sweep.

Reads sweep_raw.npz produced by spring_mass_sweep.py and applies
the adjacency-preserving cover pipeline from cover_pipeline_v2.py
(Felder 2026) to all three observable fields simultaneously.

Outputs per observable (in results/N{N}/{obs_name}/):
    observable_field.png      — O(A, Omega/omega_1)
    grad_magnitude.png        — |∇O|
    perturbation_spread.png   — σ_Δ (from sigma_delta.npz if available,
                                     else gradient proxy)
    stable_mask.png           — binary mask σ_Δ < ε
    cover_height.png          — adjacency-preserving cover height h(b)
    cover_count_curve.png     — N(ε) cover collapse curve
    cover_overlay.png         — observable field + cover height contours
    admissible_window.png     — directional admissible window
    metadata.json             — all scalar summary statistics

Multi-observable comparison (in results/N{N}/):
    comparison_cover_height.png    — h side-by-side for all three
    comparison_stable_mask.png     — masks side-by-side at common ε
    comparison_nstar.png           — N* vs ε per observable (collapse ordering)
    nesting_check.json             — P1 cover ordering test result

Usage
-----
# After running spring_mass_sweep.py --N 3 ...
python spring_mass_cover.py --N 3
python spring_mass_cover.py --N 3 --epsilon-micro 0.005 --epsilon-meso 0.01 --epsilon-macro 0.02
python spring_mass_cover.py --N 1  # baseline P6 check

Dependencies
------------
Requires cover_pipeline_v2.py in the same directory (or PYTHONPATH).
"""

from __future__ import annotations
import argparse
import json
import sys
from collections import deque
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Import cover backend from cover_pipeline_v2
# ---------------------------------------------------------------------------

try:
    sys.path.insert(0, str(Path(__file__).parent))
    from cover_pipeline_v2 import (
        cover_components,
        compute_cover_height_adjacency,
        compute_directional_cover_heights,
        compute_admissible_window,
        compute_gradients,
        compute_perturbation_spread,
        compute_stable_mask,
        run_analysis,
        plot_heatmap,
        plot_two_heatmaps,
        plot_overlay,
        plot_curve,
        save_csv,
    )
    print("  [OK] cover_pipeline_v2 loaded")
except ImportError as e:
    print(f"  [ERROR] Could not import cover_pipeline_v2: {e}")
    print("  Place cover_pipeline_v2.py in the same directory as this script.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Observable metadata
# ---------------------------------------------------------------------------

OBS_NAMES   = ["pi_micro", "pi_meso", "pi_macro"]
OBS_LABELS  = {
    "pi_micro": "π_micro  (spring-extension variance)",
    "pi_meso":  "π_meso   (COM variance)",
    "pi_macro": "π_macro  (end-mass variance)",
}
OBS_LEVEL   = {
    "pi_micro": "micro",
    "pi_meso":  "meso",
    "pi_macro": "macro",
}


# ---------------------------------------------------------------------------
# Load sweep results
# ---------------------------------------------------------------------------

def load_sweep(results_dir: Path, N: int):
    sweep_path = results_dir / f"N{N}" / "sweep_raw.npz"
    sigma_path = results_dir / f"N{N}" / "sigma_delta.npz"

    if not sweep_path.exists():
        print(f"  [ERROR] sweep_raw.npz not found: {sweep_path}")
        sys.exit(1)

    data = np.load(sweep_path)
    A_grid          = data["A_grid"]
    Omega_ratio_grid = data["Omega_ratio_grid"]
    omega_1         = float(data["omega_1"])

    fields = {
        "pi_micro": data["pi_micro"],
        "pi_meso":  data["pi_meso"],
        "pi_macro": data["pi_macro"],
    }

    # sigma_delta: empirical perturbation spread if available
    sigma_fields = {}
    if sigma_path.exists():
        sdata = np.load(sigma_path)
        sigma_fields = {
            "pi_micro": sdata["sig_micro"],
            "pi_meso":  sdata["sig_meso"],
            "pi_macro": sdata["sig_macro"],
        }
        print(f"  [OK] sigma_delta.npz loaded (empirical σ_Δ available)")
    else:
        print(f"  [INFO] sigma_delta.npz not found — will use gradient proxy for σ_Δ")

    return A_grid, Omega_ratio_grid, omega_1, fields, sigma_fields


# ---------------------------------------------------------------------------
# Cover count N*(ε) curve
# ---------------------------------------------------------------------------

def compute_nstar_curve(field: np.ndarray, n_eps: int = 80):
    """
    Compute number of cover components N*(ε) over a log-spaced ε sweep.
    Returns (eps_values, nstar_values).
    """
    ny, nx = field.shape
    diffs = []
    for i in range(ny):
        for j in range(nx):
            if j + 1 < nx: diffs.append(abs(field[i, j+1] - field[i, j]))
            if i + 1 < ny: diffs.append(abs(field[i+1, j] - field[i, j]))
    diffs = np.array(diffs)
    pos = diffs[diffs > 0]
    if len(pos) == 0:
        return np.array([1e-6]), np.array([1])

    eps_min = max(float(np.percentile(pos, 1)) / 2.0, 1e-8)
    eps_max = max(float(field.max() - field.min()), eps_min * 10)
    eps_vals = np.geomspace(eps_min, eps_max, num=n_eps)

    nstar = []
    for eps in eps_vals:
        _, _, n_comp = cover_components(field, eps)
        nstar.append(n_comp)

    return eps_vals, np.array(nstar)


# ---------------------------------------------------------------------------
# Single-observable analysis
# ---------------------------------------------------------------------------

def analyse_observable(obs_name: str, field: np.ndarray,
                        sigma_empirical,
                        A_grid: np.ndarray,
                        Omega_ratio_grid: np.ndarray,
                        omega_1: float,
                        epsilon: float,
                        outdir: Path,
                        cover_eps_n: int = 80):
    """
    Run full cover analysis for one observable field.
    If sigma_empirical is provided (not None), use it as σ_Δ.
    Otherwise fall back to gradient proxy (cover_pipeline_v2 default).
    """
    outdir.mkdir(parents=True, exist_ok=True)

    label    = OBS_LABELS[obs_name]
    p1_label = "A [m]"
    p2_label = "Ω/ω₁"

    print(f"\n  [{obs_name}] epsilon={epsilon:.5f}")

    # --- gradients ---
    # field shape: (nA, nOmega). compute_gradients calls np.gradient(field, p2, p1)
    # expecting field(p2-rows, p1-cols). Transpose so rows=Omega, cols=A.
    _gp1, _gp2, _gmag = compute_gradients(field.T, A_grid, Omega_ratio_grid)
    grad_p1  = _gp1.T
    grad_p2  = _gp2.T
    grad_mag = _gmag.T

    # --- σ_Δ ---
    if sigma_empirical is not None and not np.all(np.isnan(sigma_empirical)):
        spread = np.nan_to_num(sigma_empirical, nan=0.0)
        spread_source = "empirical"
    else:
        spread = compute_perturbation_spread(field)
        spread_source = "gradient_proxy"

    stable_mask = compute_stable_mask(spread, epsilon)

    print(f"    σ_Δ source: {spread_source}")
    print(f"    σ_Δ max={spread.max():.4e}  mean={spread.mean():.4e}")
    print(f"    unstable fraction: {(spread >= epsilon).mean()*100:.1f}%")

    # --- cover height ---
    print(f"    cover height...")
    cover_height, eps_vals_h, cover_counts_h = compute_cover_height_adjacency(
        field, n_eps=cover_eps_n)

    # --- directional heights ---
    print(f"    directional cover heights...")
    h_p1, h_p2 = compute_directional_cover_heights(field, n_eps=cover_eps_n)
    window = compute_admissible_window(h_p1, h_p2)

    # --- N*(ε) curve ---
    print(f"    N*(ε) curve...")
    eps_nstar, nstar = compute_nstar_curve(field, n_eps=cover_eps_n)

    # --- save CSVs ---
    save_csv(outdir / "observable_field.csv", field)
    save_csv(outdir / "grad_magnitude.csv", grad_mag)
    save_csv(outdir / "perturbation_spread.csv", spread)
    save_csv(outdir / "stable_mask.csv", stable_mask)
    save_csv(outdir / "cover_height.csv", cover_height)
    save_csv(outdir / "admissible_window.csv", window)
    np.save(outdir / "eps_values.npy", eps_vals_h)
    np.save(outdir / "cover_counts.npy", cover_counts_h)
    np.save(outdir / "eps_nstar.npy", eps_nstar)
    np.save(outdir / "nstar.npy", nstar)
    np.save(outdir / "A_grid.npy", A_grid)
    np.save(outdir / "Omega_ratio_grid.npy", Omega_ratio_grid)

    # --- plots ---
    kw = dict(p1_vals=A_grid, p2_vals=Omega_ratio_grid,
              p1_label=p1_label, p2_label=p2_label)

    plot_heatmap(outdir / "observable_field.png",
                 field, **kw,
                 title=f"{label}  —  observable field  (ω₁={omega_1:.3f})",
                 cbar_label="O(A, Ω/ω₁)")

    plot_heatmap(outdir / "grad_magnitude.png",
                 grad_mag, **kw,
                 title=f"{label}  —  gradient |∇O|",
                 cbar_label="|∇O|")

    plot_heatmap(outdir / "perturbation_spread.png",
                 spread, **kw,
                 title=f"{label}  —  perturbation spread σ_Δ  [{spread_source}]",
                 cbar_label="σ_Δ")

    plot_heatmap(outdir / "stable_mask.png",
                 stable_mask, **kw,
                 title=f"{label}  —  stable mask (ε={epsilon:.4f})",
                 cbar_label="stable (1=yes)", cmap="plasma")

    plot_heatmap(outdir / "cover_height.png",
                 cover_height, **kw,
                 title=f"{label}  —  cover height h(b)",
                 cbar_label="h")

    plot_two_heatmaps(
        outdir / "directional_cover_height.png",
        h_p1, h_p2, A_grid, Omega_ratio_grid,
        title1=f"h_{p1_label} (A-direction)",
        title2=f"h_{p2_label} (Ω/ω₁-direction)",
        label1="h_A", label2="h_Ω",
        p1_label=p1_label, p2_label=p2_label,
    )

    plot_heatmap(outdir / "admissible_window.png",
                 window, **kw,
                 title=f"{label}  —  admissible description window",
                 cbar_label="h_A · h_Ω (norm.)", cmap="plasma")

    plot_overlay(outdir / "cover_overlay.png",
                 field.T, cover_height.T, A_grid, Omega_ratio_grid,
                 title=f"{label}  —  observable field + cover-height contours",
                 cbar_label="O", p1_label=p1_label, p2_label=p2_label)

    # N*(ε) log-scale plot
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(eps_nstar, nstar, "b-", lw=1.5)
    ax.axvline(epsilon, color="r", lw=1.2, linestyle="--",
               label=f"ε={epsilon:.4f}")
    ax.set_xscale("log")
    ax.set_xlabel("ε", fontsize=12)
    ax.set_ylabel("N* (cover elements)", fontsize=12)
    ax.set_title(f"{label}  —  N*(ε) cover collapse", fontsize=10)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(outdir / "nstar_curve.png", dpi=180)
    plt.close()

    # --- metadata ---
    meta = {
        "observable": obs_name,
        "label": label,
        "level": OBS_LEVEL[obs_name],
        "epsilon": epsilon,
        "spread_source": spread_source,
        "observable_span": float(field.max() - field.min()),
        "observable_min": float(np.nanmin(field)),
        "observable_max": float(np.nanmax(field)),
        "spread_max": float(spread.max()),
        "spread_mean": float(spread.mean()),
        "fraction_unstable_pct": float((spread >= epsilon).mean() * 100),
        "cover_height_max": float(cover_height.max()),
        "cover_height_min": float(cover_height.min()),
        "window_fraction_wide_pct": float((window > 0.5).mean() * 100),
        "nstar_at_epsilon": int(np.interp(epsilon, eps_nstar, nstar)),
        "cover_eps_n": cover_eps_n,
        "omega_1": omega_1,
    }
    with open(outdir / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2)

    print(f"    N*(ε={epsilon:.4f}) ≈ {meta['nstar_at_epsilon']}")
    print(f"    cover height max={cover_height.max():.2e}")
    print(f"    Saved → {outdir}")

    return {
        "cover_height": cover_height,
        "stable_mask": stable_mask,
        "spread": spread,
        "eps_nstar": eps_nstar,
        "nstar": nstar,
        "meta": meta,
    }


# ---------------------------------------------------------------------------
# Multi-observable comparison
# ---------------------------------------------------------------------------

def compare_observables(results: dict, fields: dict,
                         A_grid, Omega_ratio_grid,
                         epsilons: dict,
                         outdir: Path,
                         N: int, omega_1: float):
    """
    Generate cross-observable comparison plots and P1/nesting check.
    """
    outdir.mkdir(parents=True, exist_ok=True)

    p1_label = "A [m]"
    p2_label = "Ω/ω₁"
    extent = [A_grid.min(), A_grid.max(),
              Omega_ratio_grid.min(), Omega_ratio_grid.max()]

    # --- (1) Cover height comparison side-by-side ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for ax, obs in zip(axes, OBS_NAMES):
        h = results[obs]["cover_height"]
        im = ax.imshow(h.T, origin="lower", aspect="auto", extent=extent,
                       cmap="viridis")
        ax.set_title(OBS_LABELS[obs], fontsize=9)
        ax.set_xlabel(p1_label, fontsize=9)
        ax.set_ylabel(p2_label, fontsize=9)
        plt.colorbar(im, ax=ax, label="h")
    fig.suptitle(f"Cover height comparison  N={N}", fontsize=11)
    plt.tight_layout()
    plt.savefig(outdir / "comparison_cover_height.png", dpi=180)
    plt.close()

    # --- (2) Stable mask comparison ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for ax, obs in zip(axes, OBS_NAMES):
        mask = results[obs]["stable_mask"]
        eps  = epsilons[obs]
        im = ax.imshow(mask.T, origin="lower", aspect="auto", extent=extent,
                       cmap="plasma", vmin=0, vmax=1)
        ax.set_title(f"{OBS_LEVEL[obs]}  ε={eps:.4f}", fontsize=9)
        ax.set_xlabel(p1_label, fontsize=9)
        ax.set_ylabel(p2_label, fontsize=9)
        plt.colorbar(im, ax=ax, label="stable")
    fig.suptitle(f"Stability mask comparison  N={N}", fontsize=11)
    plt.tight_layout()
    plt.savefig(outdir / "comparison_stable_mask.png", dpi=180)
    plt.close()

    # --- (3) N*(ε) overlay — P1 check ---
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = {"pi_micro": "blue", "pi_meso": "green", "pi_macro": "red"}
    for obs in OBS_NAMES:
        eps_v = results[obs]["eps_nstar"]
        nstar = results[obs]["nstar"]
        ax.plot(eps_v, nstar, color=colors[obs], lw=1.5,
                label=f"{OBS_LEVEL[obs]}  (ε_work={epsilons[obs]:.4f})")
        ax.axvline(epsilons[obs], color=colors[obs], lw=0.8,
                   linestyle=":", alpha=0.7)

    ax.set_xscale("log")
    ax.set_xlabel("ε", fontsize=12)
    ax.set_ylabel("N* (cover elements)", fontsize=12)
    ax.set_title(f"N*(ε) per observable — N={N}\n"
                 f"P1: N*_micro collapses last (farthest right)", fontsize=10)
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(outdir / "comparison_nstar.png", dpi=180)
    plt.close()

    # --- (4) P1 nesting check ---
    # Find ε*(obs) = ε where N* first reaches 1
    def eps_star(eps_v, nstar_v):
        idx = np.argmax(nstar_v <= 1)
        return float(eps_v[idx]) if nstar_v[-1] <= 1 else float(eps_v[-1])

    eps_stars = {obs: eps_star(results[obs]["eps_nstar"],
                               results[obs]["nstar"])
                 for obs in OBS_NAMES}

    p1_check = (eps_stars["pi_micro"] <= eps_stars["pi_meso"] <=
                eps_stars["pi_macro"])

    # P2: latent regime — find A values where micro is non-trivial but macro is trivial
    def nstar_at_eps(obs, eps):
        return int(np.interp(eps, results[obs]["eps_nstar"],
                             results[obs]["nstar"]))

    p2_evidence = []
    for i, A in enumerate(A_grid):
        for j, Or in enumerate(Omega_ratio_grid):
            fm = fields["pi_micro"][i, j]
            fk = fields["pi_macro"][i, j]
            # proxy: micro field varies significantly across Omega slice
            # (real test requires cover labeling per (A,Ω) point — simplified here)
        # simplified P2: check if nstar differs at each working epsilon
    nstar_micro_work = nstar_at_eps("pi_micro", epsilons["pi_micro"])
    nstar_meso_work  = nstar_at_eps("pi_meso",  epsilons["pi_meso"])
    nstar_macro_work = nstar_at_eps("pi_macro", epsilons["pi_macro"])

    p4_check = (nstar_micro_work >= nstar_meso_work >= nstar_macro_work)

    nesting_result = {
        "N": N,
        "omega_1": omega_1,
        "epsilon_star": eps_stars,
        "nstar_at_working_epsilon": {
            "pi_micro": nstar_micro_work,
            "pi_meso":  nstar_meso_work,
            "pi_macro": nstar_macro_work,
        },
        "P1_cover_collapse_ordering": {
            "result": "CONFIRMED" if p1_check else "NOT_CONFIRMED",
            "eps_star_micro": eps_stars["pi_micro"],
            "eps_star_meso":  eps_stars["pi_meso"],
            "eps_star_macro": eps_stars["pi_macro"],
            "ordering": (f"ε*(micro)={eps_stars['pi_micro']:.4e} "
                         f"<= ε*(meso)={eps_stars['pi_meso']:.4e} "
                         f"<= ε*(macro)={eps_stars['pi_macro']:.4e}"),
        },
        "P4_nstar_ordering_at_working_eps": {
            "result": "CONFIRMED" if p4_check else "NOT_CONFIRMED",
            "ordering": (f"N*(micro)={nstar_micro_work} "
                         f">= N*(meso)={nstar_meso_work} "
                         f">= N*(macro)={nstar_macro_work}"),
        },
    }

    with open(outdir / "nesting_check.json", "w") as f:
        json.dump(nesting_result, f, indent=2)

    print(f"\n--- Pre-registration check (N={N}) ---")
    print(f"  P1 (ε* ordering):  {nesting_result['P1_cover_collapse_ordering']['result']}")
    print(f"      {nesting_result['P1_cover_collapse_ordering']['ordering']}")
    print(f"  P4 (N* ordering):  {nesting_result['P4_nstar_ordering_at_working_eps']['result']}")
    print(f"      {nesting_result['P4_nstar_ordering_at_working_eps']['ordering']}")

    return nesting_result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Cover analysis for spring-mass chain sweep")
    p.add_argument("--N",              type=int,   default=3)
    p.add_argument("--results-dir",    type=str,   default="results")
    p.add_argument("--epsilon-micro",  type=float, default=None,
                   help="Working ε for pi_micro (auto if not set)")
    p.add_argument("--epsilon-meso",   type=float, default=None,
                   help="Working ε for pi_meso  (auto if not set)")
    p.add_argument("--epsilon-macro",  type=float, default=None,
                   help="Working ε for pi_macro (auto if not set)")
    p.add_argument("--cover-eps-n",    type=int,   default=80,
                   help="Number of ε levels for cover height sweep")
    return p.parse_args()


def auto_epsilon(field: np.ndarray, percentile: float = 10.0) -> float:
    """
    Auto-select ε as the 10th percentile of neighbour differences.
    This sits safely inside the admissible resolution regime for
    most well-behaved observable fields.
    """
    ny, nx = field.shape
    diffs = []
    for i in range(ny):
        for j in range(nx):
            if j + 1 < nx: diffs.append(abs(field[i, j+1] - field[i, j]))
            if i + 1 < ny: diffs.append(abs(field[i+1, j] - field[i, j]))
    diffs = np.array(diffs)
    pos = diffs[diffs > 0]
    if len(pos) == 0:
        return 0.01
    return float(np.percentile(pos, percentile))


def main():
    args = parse_args()
    N = args.N
    results_dir = Path(args.results_dir)

    print(f"\n=== ARW Spring-Mass Cover Analysis ===")
    print(f"  N={N}   results_dir={results_dir}")

    A_grid, Omega_ratio_grid, omega_1, fields, sigma_fields = \
        load_sweep(results_dir, N)

    print(f"  Grid: {len(A_grid)} x {len(Omega_ratio_grid)}  "
          f"  omega_1={omega_1:.4f}")
    print(f"  A range:      [{A_grid[0]:.3f}, {A_grid[-1]:.3f}]")
    print(f"  Omega/omega_1: [{Omega_ratio_grid[0]:.3f}, {Omega_ratio_grid[-1]:.3f}]")

    # --- determine working epsilons ---
    eps_args = {
        "pi_micro": args.epsilon_micro,
        "pi_meso":  args.epsilon_meso,
        "pi_macro": args.epsilon_macro,
    }
    epsilons = {}
    for obs in OBS_NAMES:
        if eps_args[obs] is not None:
            epsilons[obs] = eps_args[obs]
        else:
            epsilons[obs] = auto_epsilon(fields[obs])
            print(f"  Auto ε({obs}) = {epsilons[obs]:.5f}")

    # --- analyse each observable ---
    ana_results = {}
    for obs in OBS_NAMES:
        obs_outdir = results_dir / f"N{N}" / obs
        sigma_emp  = sigma_fields.get(obs, None)
        ana_results[obs] = analyse_observable(
            obs_name=obs,
            field=fields[obs],
            sigma_empirical=sigma_emp,
            A_grid=A_grid,
            Omega_ratio_grid=Omega_ratio_grid,
            omega_1=omega_1,
            epsilon=epsilons[obs],
            outdir=obs_outdir,
            cover_eps_n=args.cover_eps_n,
        )

    # --- multi-observable comparison ---
    print(f"\n--- Multi-observable comparison ---")
    compare_dir = results_dir / f"N{N}"
    nesting = compare_observables(
        results=ana_results,
        fields=fields,
        A_grid=A_grid,
        Omega_ratio_grid=Omega_ratio_grid,
        epsilons=epsilons,
        outdir=compare_dir,
        N=N,
        omega_1=omega_1,
    )

    print(f"\nDone. All outputs in: {compare_dir.resolve()}")
    print(f"Next: inspect comparison_nstar.png for cover collapse ordering.")


if __name__ == "__main__":
    main()
