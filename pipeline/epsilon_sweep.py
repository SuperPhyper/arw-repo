"""
pipeline/epsilon_sweep.py — Admissible ε-Interval Finder

Given existing sweep results, re-runs partition extraction across a range
of ε values and records the partition invariant signature σ(ε) = (N(ε), G_S(ε))
at each step.

Identifies:
  - Admissible ε-intervals (plateaus where σ is constant)
  - Critical ε-values (where σ jumps)
  - Plateau width w = log(ε_max / ε_min) as a scope robustness measure

This implements the ε-sweep protocol from
docs/advanced/epsilon_and_scope_resolution.md § 4.

Output: results/partition/EpsilonSweep.json

Usage:
    python -m pipeline.epsilon_sweep --case cases/CASE-... [--eps-min 0.001] [--eps-max 1.0] [--eps-steps 50]
"""

import argparse
import json
import math
import sys
from pathlib import Path

try:
    import yaml
    import numpy as np
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

# Import observable extractors from extract_partition
from pipeline.extract_partition import OBSERVABLE_MAP, extract_observable_stub


# ── ε-dependent regime assignment ────────────────────────────────────────────

def assign_regimes_at_epsilon(sweep_results: list, system: str, epsilon: float) -> list:
    """
    Re-assign regimes for the given ε value.

    For systems with analytically defined regime boundaries (Kuramoto, Pendulum),
    the regime thresholds are functions of ε.
    For ε-clustering systems (continuous observables), ε directly controls
    the indistinguishability relation.
    """
    extractor = OBSERVABLE_MAP.get(system, extract_observable_stub)
    observables = []

    for r in sweep_results:
        obs = extractor(r)
        observables.append({
            "sweep_point": r.get("_sweep_point", {}),
            "sweep_index": r.get("_sweep_index"),
            "observable":  obs.get("observable"),
            "observable_name": obs.get("observable_name"),
        })

    # Extract raw observable values
    obs_values = [o["observable"] for o in observables if o["observable"] is not None]
    if not obs_values:
        return []

    # ε-clustering: group observable values into regimes using ε as the
    # indistinguishability threshold.
    # Sort by observable value, then assign regime IDs by detecting gaps > ε.
    indexed = [(i, o["observable"], o) for i, o in enumerate(observables)
               if o["observable"] is not None]
    indexed.sort(key=lambda x: x[1])

    regime_id = 0
    regime_assignments = {}
    prev_val = indexed[0][1]
    regime_assignments[indexed[0][0]] = regime_id

    for idx, val, _ in indexed[1:]:
        if val - prev_val > epsilon:
            regime_id += 1
        regime_assignments[idx] = regime_id
        prev_val = val

    # Build annotated results
    annotated = []
    for i, o in enumerate(observables):
        if i in regime_assignments:
            annotated.append({
                **o,
                "regime_id": regime_assignments[i],
                "epsilon": epsilon,
            })

    return annotated


def compute_invariant_signature(annotated: list, sweep_param: str) -> dict:
    """
    Compute the partition invariant signature σ(ε) = (N, G_S).

    N:   number of distinct regime classes
    G_S: adjacency graph (which regimes are adjacent in parameter space)
    """
    if not annotated:
        return {"regime_count": 0, "adjacency_edges": [], "regime_ids": []}

    # Regime count
    regime_ids = sorted(set(a["regime_id"] for a in annotated))
    N = len(regime_ids)

    # Adjacency: sort by sweep parameter, find where regime changes
    pts = []
    for a in annotated:
        sp = a.get("sweep_point", {})
        param_val = sp.get(sweep_param)
        if param_val is not None:
            pts.append((param_val, a["regime_id"]))
    pts.sort(key=lambda x: x[0])

    edges = []
    seen_edges = set()
    for i in range(1, len(pts)):
        if pts[i][1] != pts[i-1][1]:
            edge = (min(pts[i-1][1], pts[i][1]), max(pts[i-1][1], pts[i][1]))
            if edge not in seen_edges:
                edges.append({
                    "from": pts[i-1][1],
                    "to": pts[i][1],
                    "param_midpoint": (pts[i-1][0] + pts[i][0]) / 2,
                })
                seen_edges.add(edge)

    return {
        "regime_count": N,
        "regime_ids": regime_ids,
        "adjacency_edges": edges,
        "adjacency_edge_count": len(edges),
    }


def find_plateaus(sigma_trace: list) -> list:
    """
    Identify plateaus in the σ(ε) trace: contiguous ε-ranges where
    the partition signature is constant.
    """
    if not sigma_trace:
        return []

    plateaus = []
    current = {
        "regime_count": sigma_trace[0]["regime_count"],
        "edge_count":   sigma_trace[0]["adjacency_edge_count"],
        "eps_start":    sigma_trace[0]["epsilon"],
        "eps_end":      sigma_trace[0]["epsilon"],
        "n_points":     1,
    }

    for entry in sigma_trace[1:]:
        same = (entry["regime_count"] == current["regime_count"] and
                entry["adjacency_edge_count"] == current["edge_count"])
        if same:
            current["eps_end"] = entry["epsilon"]
            current["n_points"] += 1
        else:
            plateaus.append(current)
            current = {
                "regime_count": entry["regime_count"],
                "edge_count":   entry["adjacency_edge_count"],
                "eps_start":    entry["epsilon"],
                "eps_end":      entry["epsilon"],
                "n_points":     1,
            }

    plateaus.append(current)

    # Compute plateau widths
    for p in plateaus:
        if p["eps_start"] > 0 and p["eps_end"] > 0 and p["eps_end"] > p["eps_start"]:
            p["width_log"] = round(math.log(p["eps_end"] / p["eps_start"]), 4)
        else:
            p["width_log"] = 0.0
        p["eps_start"] = round(p["eps_start"], 6)
        p["eps_end"]   = round(p["eps_end"], 6)

    return plateaus


def find_critical_epsilon_values(sigma_trace: list) -> list:
    """
    Find ε values where the partition signature jumps.
    """
    criticals = []
    for i in range(1, len(sigma_trace)):
        prev = sigma_trace[i-1]
        curr = sigma_trace[i]
        if (curr["regime_count"] != prev["regime_count"] or
                curr["adjacency_edge_count"] != prev["adjacency_edge_count"]):
            criticals.append({
                "epsilon_before": round(prev["epsilon"], 6),
                "epsilon_after":  round(curr["epsilon"], 6),
                "epsilon_midpoint": round((prev["epsilon"] + curr["epsilon"]) / 2, 6),
                "N_before": prev["regime_count"],
                "N_after":  curr["regime_count"],
                "edges_before": prev["adjacency_edge_count"],
                "edges_after":  curr["adjacency_edge_count"],
            })
    return criticals


# ── Main ─────────────────────────────────────────────────────────────────────

def run_epsilon_sweep(case_dir: Path, eps_min: float, eps_max: float,
                      eps_steps: int, in_subdir: str, out_subdir: str):
    sweep_path  = case_dir / in_subdir / "sweep_results.json"
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"
    bcm_path    = case_dir / "BCManifest.yaml"

    for p in [sweep_path, scope_path]:
        if not p.exists():
            print(f"ERROR: {p} not found")
            sys.exit(1)

    sweep_data = json.loads(sweep_path.read_text())
    scope      = yaml.safe_load(scope_path.read_text())
    record     = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}
    bcm        = yaml.safe_load(bcm_path.read_text()) if bcm_path.exists() else {}

    system      = record.get("system", "custom")
    working_eps = scope.get("epsilon", {}).get("value", 0.05)
    results     = sweep_data.get("results", [])

    # Determine sweep parameter name
    bc_components = bcm.get("bc_components", [])
    sweeps = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    sweep_param = sweeps[0].get("param", "kappa") if sweeps else "kappa"

    # Generate ε values (logarithmic spacing)
    eps_values = np.logspace(math.log10(eps_min), math.log10(eps_max), eps_steps).tolist()

    print(f"\nε-Sweep: {case_dir.name}  |  system={system}")
    print(f"  ε range: [{eps_min}, {eps_max}]  |  {eps_steps} steps (log-spaced)")
    print(f"  Working ε: {working_eps}")
    print(f"  Sweep param: {sweep_param}")
    print(f"  Sweep points: {len(results)}")
    print("─" * 60)

    # Run ε-sweep
    sigma_trace = []
    for i, eps in enumerate(eps_values):
        annotated = assign_regimes_at_epsilon(results, system, eps)
        sigma = compute_invariant_signature(annotated, sweep_param)
        sigma["epsilon"] = eps

        sigma_trace.append(sigma)

        if (i + 1) % 10 == 0 or i == 0 or i == len(eps_values) - 1:
            print(f"  ε={eps:.6f}  →  N={sigma['regime_count']:2d}  |  edges={sigma['adjacency_edge_count']}")

    # Analyze plateaus
    plateaus = find_plateaus(sigma_trace)
    criticals = find_critical_epsilon_values(sigma_trace)

    print(f"\n{'─' * 60}")
    print(f"  Plateaus found: {len(plateaus)}")
    for j, p in enumerate(plateaus):
        marker = "  ◀ working ε" if p["eps_start"] <= working_eps <= p["eps_end"] else ""
        print(f"    [{j+1}] N={p['regime_count']}  edges={p['edge_count']}  "
              f"ε ∈ [{p['eps_start']:.6f}, {p['eps_end']:.6f}]  "
              f"w={p['width_log']:.3f}{marker}")

    if criticals:
        print(f"\n  Critical ε-values: {len(criticals)}")
        for c in criticals:
            print(f"    ε* ≈ {c['epsilon_midpoint']:.6f}  "
                  f"(N: {c['N_before']} → {c['N_after']}, "
                  f"edges: {c['edges_before']} → {c['edges_after']})")

    # Find the admissible interval containing the working ε
    admissible_interval = None
    for p in plateaus:
        if p["eps_start"] <= working_eps <= p["eps_end"]:
            admissible_interval = p
            break

    if admissible_interval:
        print(f"\n  ✓ Admissible ε-interval for working ε={working_eps}:")
        print(f"    I_ε = [{admissible_interval['eps_start']:.6f}, "
              f"{admissible_interval['eps_end']:.6f}]")
        print(f"    w(I_ε) = {admissible_interval['width_log']:.3f}")
        print(f"    N = {admissible_interval['regime_count']}, "
              f"edges = {admissible_interval['edge_count']}")
    else:
        print(f"\n  ⚠ Working ε={working_eps} falls on or near a critical boundary")

    # Write output
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "EpsilonSweep.json"

    output = {
        "case_id":              record.get("id", case_dir.name),
        "system":               system,
        "working_epsilon":      working_eps,
        "sweep_param":          sweep_param,
        "eps_range":            [eps_min, eps_max],
        "eps_steps":            eps_steps,
        "sigma_trace": [
            {
                "epsilon":       round(s["epsilon"], 6),
                "regime_count":  s["regime_count"],
                "regime_ids":    s["regime_ids"],
                "adjacency_edge_count": s["adjacency_edge_count"],
                "adjacency_edges": s["adjacency_edges"],
            }
            for s in sigma_trace
        ],
        "plateaus":             plateaus,
        "critical_epsilon_values": criticals,
        "admissible_interval":  admissible_interval,
    }

    out_path.write_text(json.dumps(output, indent=2))
    print(f"\n  Output: {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="ε-sweep: find the admissible ε-interval for a case.")
    parser.add_argument("--case",      required=True)
    parser.add_argument("--eps-min",   type=float, default=0.001)
    parser.add_argument("--eps-max",   type=float, default=1.0)
    parser.add_argument("--eps-steps", type=int,   default=50)
    parser.add_argument("--in",        dest="in_dir",  default="results/raw")
    parser.add_argument("--out",       dest="out_dir", default="results/partition")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    run_epsilon_sweep(case_dir, args.eps_min, args.eps_max,
                      args.eps_steps, args.in_dir, args.out_dir)


if __name__ == "__main__":
    main()
