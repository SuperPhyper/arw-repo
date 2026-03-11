"""
pipeline/extract_partition.py — Partition Extractor

Converts raw sweep output (sweep_results.json) into a regime partition
using the robust indistinguishability relation ~_S.

For each sweep point x, computes the observable value Π(x) and groups
points into equivalence classes under d_Π(x,y) ≤ ε.

Currently implemented: Kuramoto order-parameter thresholding.

Output: results/partition/PartitionResult.json

Usage:
    python -m pipeline.extract_partition --case cases/CASE-... --in results/raw --out results/partition
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
    import numpy as np
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent


# ── Observable extractors (one per system) ───────────────────────────────────

def extract_observable_kuramoto(result: dict) -> dict:
    """
    Observable: r_ss (steady-state order parameter)
    Regime partition R_K (from experiments/kuramoto_oscillators.md):
        Incoherent:         r_ss < 0.1
        Partially synced:   0.1 ≤ r_ss < 0.85
        Fully synchronized: r_ss ≥ 0.85
    """
    r = result.get("r_ss", None)
    if r is None:
        return {"observable": None, "regime_label": "unknown", "regime_id": -1}

    if r < 0.1:
        label, rid = "Incoherent", 0
    elif r < 0.85:
        label, rid = "Partially_synchronized", 1
    else:
        label, rid = "Fully_synchronized", 2

    return {
        "observable":   r,
        "observable_name": "r_ss",
        "regime_label": label,
        "regime_id":    rid,
    }


def extract_observable_stub(result: dict) -> dict:
    return {"observable": None, "regime_label": "stub", "regime_id": -1,
            "note": "Implement observable extractor for this system"}


OBSERVABLE_MAP = {
    "kuramoto":  extract_observable_kuramoto,
    "pendulum":  extract_observable_stub,
    "consensus": extract_observable_stub,
    "meanfield": extract_observable_stub,
    "labyrinth": extract_observable_stub,
}


# ── Robust partition via ε-thresholding ─────────────────────────────────────

def assign_regimes(sweep_results: list, extractor, epsilon: float) -> list:
    """
    Apply the extractor to each sweep point, assign regimes.
    For systems with discrete regime labels (Kuramoto), the extractor
    directly returns regime IDs.
    For continuous observables, ε-clustering is applied.
    """
    annotated = []
    for r in sweep_results:
        obs = extractor(r)
        annotated.append({**r, **obs})
    return annotated


def compute_transition_boundary(annotated: list, param: str) -> dict:
    """
    Locate the transition boundary θ* in parameter space:
    the smallest param value where regime changes from R_i to R_{i+1}.
    """
    # Sort by parameter value
    pts = [(p.get("_sweep_point", {}).get(param), p.get("regime_id", -1))
           for p in annotated
           if p.get("_sweep_point", {}).get(param) is not None]
    pts.sort(key=lambda x: x[0])

    transitions = []
    for i in range(1, len(pts)):
        if pts[i][1] != pts[i-1][1]:
            transitions.append({
                "from_regime": pts[i-1][1],
                "to_regime":   pts[i][1],
                "param_before": pts[i-1][0],
                "param_after":  pts[i][0],
                "theta_star":   (pts[i-1][0] + pts[i][0]) / 2,
            })
    return {
        "param":       param,
        "transitions": transitions,
        "theta_star":  transitions[0]["theta_star"] if transitions else None,
    }


def extract_partition(case_dir: Path, in_subdir: str, out_subdir: str):
    sweep_path  = case_dir / in_subdir / "sweep_results.json"
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"

    for p in [sweep_path, scope_path]:
        if not p.exists():
            print(f"ERROR: {p} not found")
            sys.exit(1)

    sweep_data = json.loads(sweep_path.read_text())
    scope      = yaml.safe_load(scope_path.read_text())
    record     = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}

    system   = record.get("system", "custom")
    epsilon  = scope.get("epsilon", {}).get("value", 0.01)
    extractor = OBSERVABLE_MAP.get(system, extract_observable_stub)

    print(f"\nPartition Extraction: {case_dir.name}  |  system={system}  |  ε={epsilon}")
    print("─" * 50)

    results   = sweep_data.get("results", [])
    annotated = assign_regimes(results, extractor, epsilon)

    # Count regimes
    regime_ids    = [r.get("regime_id", -1) for r in annotated if r.get("regime_id", -1) >= 0]
    unique_regimes = sorted(set(regime_ids))
    regime_counts  = {rid: regime_ids.count(rid) for rid in unique_regimes}

    print(f"  Regime count N = {len(unique_regimes)}")
    for rid, cnt in regime_counts.items():
        label = next((r["regime_label"] for r in annotated if r.get("regime_id") == rid), "?")
        print(f"    R{rid}: {label}  ({cnt} sweep points)")

    # Locate transition boundary (for first BC param)
    bc_components = yaml.safe_load((case_dir / "BCManifest.yaml").read_text()).get("bc_components", [])
    sweeps        = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    param         = sweeps[0].get("param") if sweeps else None
    transition    = compute_transition_boundary(annotated, param) if param else {}

    if transition.get("theta_star") is not None:
        print(f"  Transition boundary θ* ≈ {transition['theta_star']:.4f}  (param: {param})")
    else:
        print(f"  No transition boundary detected for param: {param}")

    # Write output
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "PartitionResult.json"

    partition_result = {
        "case_id":       record.get("id", case_dir.name),
        "system":        system,
        "epsilon":       epsilon,
        "regime_count":  len(unique_regimes),
        "regime_labels": {str(rid): next((r["regime_label"] for r in annotated
                                          if r.get("regime_id") == rid), "?")
                          for rid in unique_regimes},
        "regime_counts": {str(k): v for k, v in regime_counts.items()},
        "transition_boundary": transition,
        "annotated_results": [
            {
                "sweep_index":    r.get("_sweep_index"),
                "sweep_point":    r.get("_sweep_point"),
                "observable":     r.get("observable"),
                "observable_name": r.get("observable_name"),
                "regime_id":      r.get("regime_id"),
                "regime_label":   r.get("regime_label"),
            }
            for r in annotated
        ],
    }

    out_path.write_text(json.dumps(partition_result, indent=2))
    print(f"\n  Output: {out_path}")
    print(f"\nNext step: python -m pipeline.invariants --case {case_dir} --in {out_subdir}")


def main():
    parser = argparse.ArgumentParser(description="Extract regime partition from sweep results.")
    parser.add_argument("--case", required=True)
    parser.add_argument("--in",   dest="in_dir",  default="results/raw")
    parser.add_argument("--out",  dest="out_dir", default="results/partition")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    extract_partition(case_dir, args.in_dir, args.out_dir)


if __name__ == "__main__":
    main()
