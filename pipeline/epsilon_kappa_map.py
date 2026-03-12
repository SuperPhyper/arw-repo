"""
pipeline/epsilon_kappa_map.py — 2D (κ, ε) Scope Robustness Map

For each BC parameter value κ, determines the local admissible ε-interval
by running a sliding-window ε-sweep over the observable landscape.

This answers the question: does the admissible ε-interval narrow
near the phase transition boundary θ*?

Implements the "Plateau stability under BC variation" question from
docs/advanced/epsilon_and_scope_resolution.md § 8.

Output: results/partition/EpsilonKappaMap.json

Usage:
    python -m pipeline.epsilon_kappa_map --case cases/CASE-... \
        --kappa-points 80 --eps-min 0.001 --eps-max 1.0 --eps-steps 60
"""

import argparse
import json
import math
import sys
import time
from pathlib import Path

try:
    import yaml
    import numpy as np
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent


def run_kuramoto_single(kappa: float, N: int = 500, T: float = 200.0,
                        dt: float = 0.05, seed: int = 42) -> float:
    """Run one Kuramoto simulation, return r_ss."""
    rng = np.random.default_rng(seed)
    omega = rng.standard_normal(N)
    theta = rng.uniform(0, 2 * np.pi, N)
    n_steps = int(T / dt)
    r_series = np.zeros(n_steps)

    for t in range(n_steps):
        psi = np.angle(np.mean(np.exp(1j * theta)))
        r = np.abs(np.mean(np.exp(1j * theta)))
        dtheta = omega + kappa * r * np.sin(psi - theta)
        theta = theta + dt * dtheta
        r_series[t] = r

    return float(np.mean(r_series[int(0.8 * n_steps):]))


def epsilon_partition_count(r_values: list, epsilon: float) -> dict:
    """
    Given a sorted list of (kappa, r_ss) pairs, assign regimes using ε-clustering
    and return partition signature.
    """
    if not r_values:
        return {"N": 0, "edges": 0}

    # Sort by observable value for ε-clustering
    sorted_by_obs = sorted(r_values, key=lambda x: x[1])

    regime_id = 0
    assignments = {}  # index -> regime_id
    prev_r = sorted_by_obs[0][1]
    assignments[0] = 0

    for i in range(1, len(sorted_by_obs)):
        if sorted_by_obs[i][1] - prev_r > epsilon:
            regime_id += 1
        assignments[i] = regime_id
        prev_r = sorted_by_obs[i][1]

    N = regime_id + 1

    # Map back to parameter order for adjacency
    # Create (kappa, regime_id) pairs in kappa-order
    kappa_regime = []
    obs_to_idx = {id(v): i for i, v in enumerate(sorted_by_obs)}
    # Rebuild in original kappa order
    sorted_by_kappa = sorted(r_values, key=lambda x: x[0])
    for kr in sorted_by_kappa:
        # Find this point in sorted_by_obs
        for j, so in enumerate(sorted_by_obs):
            if so[0] == kr[0] and so[1] == kr[1] and j in assignments:
                kappa_regime.append((kr[0], assignments[j]))
                break

    # Count adjacency edges
    edges = set()
    for i in range(1, len(kappa_regime)):
        if kappa_regime[i][1] != kappa_regime[i-1][1]:
            e = (min(kappa_regime[i-1][1], kappa_regime[i][1]),
                 max(kappa_regime[i-1][1], kappa_regime[i][1]))
            edges.add(e)

    return {"N": N, "edges": len(edges)}


def compute_local_plateau_width(r_values: list, kappa_center: float,
                                kappa_window: float,
                                eps_values: list) -> dict:
    """
    For a window of κ around kappa_center, compute the ε-plateau structure.
    Returns the plateau containing the "natural" ε for this window.
    """
    # Select points within the window
    local = [(k, r) for k, r in r_values if abs(k - kappa_center) <= kappa_window]
    if len(local) < 2:
        return {"kappa": kappa_center, "n_local": len(local),
                "plateaus": [], "max_plateau_width": 0.0}

    # ε-sweep on this local window
    sigma_trace = []
    for eps in eps_values:
        sig = epsilon_partition_count(local, eps)
        sigma_trace.append({"epsilon": eps, "N": sig["N"], "edges": sig["edges"]})

    # Find plateaus
    plateaus = []
    current = {"N": sigma_trace[0]["N"], "eps_start": sigma_trace[0]["epsilon"],
               "eps_end": sigma_trace[0]["epsilon"]}
    for s in sigma_trace[1:]:
        if s["N"] == current["N"]:
            current["eps_end"] = s["epsilon"]
        else:
            plateaus.append(current)
            current = {"N": s["N"], "eps_start": s["epsilon"], "eps_end": s["epsilon"]}
    plateaus.append(current)

    for p in plateaus:
        if p["eps_end"] > p["eps_start"] > 0:
            p["width_log"] = round(math.log(p["eps_end"] / p["eps_start"]), 4)
        else:
            p["width_log"] = 0.0

    max_w = max((p["width_log"] for p in plateaus), default=0.0)

    return {
        "kappa": round(kappa_center, 4),
        "n_local": len(local),
        "plateaus": plateaus,
        "max_plateau_width": round(max_w, 4),
    }


def run_epsilon_kappa_map(case_dir: Path, kappa_points: int,
                          eps_min: float, eps_max: float, eps_steps: int,
                          out_subdir: str):
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"

    scope  = yaml.safe_load(scope_path.read_text()) if scope_path.exists() else {}
    record = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}

    system = record.get("system", "kuramoto")
    if system != "kuramoto":
        print(f"ERROR: epsilon_kappa_map currently only supports kuramoto, got '{system}'")
        sys.exit(1)

    # Resolve primary observable from ScopeSpec Pi block (observable_key + primary: true).
    # Falls back to r_ss for kuramoto if not specified.
    scope_pi_entries = scope.get("Pi", [])
    scope_pi = next(
        (p.get("observable_key") for p in scope_pi_entries if p.get("primary") is True),
        "r_ss"
    )
    print(f"  scope_pi (primary observable): {scope_pi}")

    sim_params = scope.get("simulation_parameters", {})
    N_osc = sim_params.get("N", 500)
    T_sim = sim_params.get("T", 200)

    # Dense κ sweep
    kappa_values = np.linspace(0.0, 3.5, kappa_points).tolist()
    eps_values = np.logspace(math.log10(eps_min), math.log10(eps_max), eps_steps).tolist()

    print(f"\n2D (κ, ε) Map: {case_dir.name}")
    print(f"  κ: {kappa_points} points in [0.0, 3.5]")
    print(f"  ε: {eps_steps} points in [{eps_min}, {eps_max}] (log-spaced)")
    print(f"  Kuramoto: N={N_osc}, T={T_sim}")
    print("─" * 60)

    # Phase 1: Dense simulation sweep
    print(f"\n  Phase 1: Running {kappa_points} Kuramoto simulations...")
    t0 = time.time()
    r_values = []  # (kappa, r_ss)
    for i, k in enumerate(kappa_values):
        r_ss = run_kuramoto_single(k, N=N_osc, T=T_sim, seed=42)
        r_values.append((k, r_ss))
        if (i + 1) % 20 == 0:
            print(f"    [{i+1}/{kappa_points}] κ={k:.3f} r_ss={r_ss:.4f}  "
                  f"({time.time()-t0:.1f}s)")

    t_sim = time.time() - t0
    print(f"  Simulations complete: {t_sim:.1f}s")

    # Phase 2: Global 2D map — for each ε, partition all points
    print(f"\n  Phase 2: Computing global σ(κ, ε) map...")
    global_map = []  # [{epsilon, N, edges, regime_boundaries: [κ values]}]

    for eps in eps_values:
        sig = epsilon_partition_count(r_values, eps)

        # Find regime boundaries in κ-space
        sorted_by_kappa = sorted(r_values, key=lambda x: x[0])
        # Re-run clustering to get per-point assignments
        sorted_by_obs = sorted(enumerate(sorted_by_kappa), key=lambda x: x[1][1])
        rid = 0
        asgn = {}
        prev_r = sorted_by_obs[0][1][1]
        asgn[sorted_by_obs[0][0]] = 0
        for j in range(1, len(sorted_by_obs)):
            if sorted_by_obs[j][1][1] - prev_r > eps:
                rid += 1
            asgn[sorted_by_obs[j][0]] = rid
            prev_r = sorted_by_obs[j][1][1]

        # Find κ-boundaries
        kappa_order = [(sorted_by_kappa[i][0], asgn.get(i, -1)) for i in range(len(sorted_by_kappa))]
        boundaries = []
        for j in range(1, len(kappa_order)):
            if kappa_order[j][1] != kappa_order[j-1][1]:
                boundaries.append(round((kappa_order[j-1][0] + kappa_order[j][0]) / 2, 4))

        global_map.append({
            "epsilon": round(eps, 6),
            "N": sig["N"],
            "edges": sig["edges"],
            "regime_boundaries_kappa": boundaries,
        })

    # Phase 3: Local plateau analysis — sliding window along κ
    print(f"\n  Phase 3: Local plateau analysis (sliding window)...")
    kappa_window = (kappa_values[-1] - kappa_values[0]) / 8  # ~1/8 of total range
    local_analysis = []

    sample_kappas = np.linspace(kappa_values[0] + kappa_window,
                                kappa_values[-1] - kappa_window, 30).tolist()
    for k_center in sample_kappas:
        local = compute_local_plateau_width(r_values, k_center, kappa_window, eps_values)
        local_analysis.append(local)

    # Phase 4: Find where scope is most/least robust
    print(f"\n  Phase 4: Robustness analysis...")

    # Observable gradient: dr_ss/dκ
    r_sorted = sorted(r_values, key=lambda x: x[0])
    gradients = []
    for i in range(1, len(r_sorted)):
        dk = r_sorted[i][0] - r_sorted[i-1][0]
        dr = r_sorted[i][1] - r_sorted[i-1][1]
        if dk > 0:
            grad = dr / dk
            k_mid = (r_sorted[i][0] + r_sorted[i-1][0]) / 2
            gradients.append({"kappa": round(k_mid, 4), "dr_dkappa": round(grad, 6)})

    # Find the transition region (max gradient)
    if gradients:
        max_grad = max(gradients, key=lambda g: abs(g["dr_dkappa"]))
        print(f"    Max |dr/dκ| = {abs(max_grad['dr_dkappa']):.4f} at κ ≈ {max_grad['kappa']:.3f}")
    else:
        max_grad = None

    # Correlate local plateau width with gradient
    robustness_profile = []
    for la in local_analysis:
        k = la["kappa"]
        # Find nearest gradient
        nearest_grad = min(gradients, key=lambda g: abs(g["kappa"] - k)) if gradients else None
        robustness_profile.append({
            "kappa": k,
            "max_plateau_width": la["max_plateau_width"],
            "n_local_points": la["n_local"],
            "dr_dkappa": nearest_grad["dr_dkappa"] if nearest_grad else None,
        })

    # Summary
    print(f"\n{'─' * 60}")
    print(f"  Robustness profile (κ → max plateau width w):")
    for rp in robustness_profile[::3]:  # every 3rd for readability
        bar = "█" * int(rp["max_plateau_width"] * 5) if rp["max_plateau_width"] else ""
        grad_str = f"  |dr/dκ|={abs(rp['dr_dkappa']):.4f}" if rp["dr_dkappa"] is not None else ""
        print(f"    κ={rp['kappa']:.2f}  w={rp['max_plateau_width']:.3f}  {bar}{grad_str}")

    # Write output
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "EpsilonKappaMap.json"

    output = {
        "case_id": record.get("id", case_dir.name),
        "system": system,
        "scope_pi": scope_pi,
        "kappa_points": kappa_points,
        "kappa_range": [round(kappa_values[0], 4), round(kappa_values[-1], 4)],
        "eps_range": [eps_min, eps_max],
        "eps_steps": eps_steps,
        "simulation_time_s": round(t_sim, 1),
        "r_values": [{"kappa": round(k, 4), "r_ss": round(r, 6), "observable_key": scope_pi} for k, r in r_values],
        "global_map": global_map,
        "local_analysis": local_analysis,
        "observable_gradient": gradients,
        "robustness_profile": robustness_profile,
        "max_gradient": max_grad,
    }

    out_path.write_text(json.dumps(output, indent=2))
    print(f"\n  Output: {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="2D (κ, ε) scope robustness map.")
    parser.add_argument("--case",         required=True)
    parser.add_argument("--kappa-points", type=int,   default=80)
    parser.add_argument("--eps-min",      type=float, default=0.001)
    parser.add_argument("--eps-max",      type=float, default=1.0)
    parser.add_argument("--eps-steps",    type=int,   default=60)
    parser.add_argument("--out",          dest="out_dir", default="results/partition")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    run_epsilon_kappa_map(case_dir, args.kappa_points,
                          args.eps_min, args.eps_max, args.eps_steps, args.out_dir)


if __name__ == "__main__":
    main()
