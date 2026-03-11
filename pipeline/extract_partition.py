"""
pipeline/extract_partition.py — Partition Extractor

Converts raw sweep output (sweep_results.json) into a regime partition
using the robust indistinguishability relation ~_S.

For each sweep point x, extracts the observable value Π(x) and groups
points into equivalence classes under d_Π(x,y) ≤ ε.

Regime assignment is purely ε-based: no hardcoded thresholds. Observable
extractors return raw values only. Labels are assigned post-hoc based on
the observable range each cluster covers.

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


# ── Observable extractors ────────────────────────────────────────────────────
# Each extractor returns raw observable values — NO regime labels, NO IDs.
# The partition is determined by ε-clustering, not by thresholds.

def extract_observables_kuramoto(result: dict) -> dict:
    """Kuramoto: primary observable is r_ss (steady-state order parameter)."""
    r = result.get("r_ss", None)
    if r is None:
        return {"observables": {}}
    return {
        "observables": {
            "r_ss": r,
        },
        "primary_observable": "r_ss",
    }


def extract_observables_pendulum(result: dict) -> dict:
    """Old pendulum (with kappa): lambda_proxy and var_rel."""
    if result.get("status") != "ok":
        return {"observables": {}}
    return {
        "observables": {
            "lambda_proxy": result.get("lambda_proxy"),
            "var_rel":      result.get("var_rel"),
        },
        "primary_observable": "lambda_proxy",
    }


def extract_observables_double_pendulum(result: dict) -> dict:
    """Classical double pendulum: lambda_proxy, var_rel, E_mean."""
    if result.get("status") != "ok":
        return {"observables": {}}
    return {
        "observables": {
            "lambda_proxy": result.get("lambda_proxy"),
            "var_rel":      result.get("var_rel"),
            "E_mean":       result.get("E_mean"),
        },
        "primary_observable": "lambda_proxy",
    }


def extract_observables_stub(result: dict) -> dict:
    return {"observables": {},
            "note": "Implement observable extractor for this system"}


OBSERVABLE_MAP = {
    "kuramoto":        extract_observables_kuramoto,
    "pendulum":        extract_observables_pendulum,
    "double_pendulum": extract_observables_double_pendulum,
    "consensus":       extract_observables_stub,
    "meanfield":       extract_observables_stub,
    "labyrinth":       extract_observables_stub,
}


# ── ε-clustering ─────────────────────────────────────────────────────────────

def eps_cluster(values: list, epsilon: float) -> list:
    """
    ε-cluster a list of (index, value) pairs by the indistinguishability
    relation: x ~_S y iff |Π(x) - Π(y)| ≤ ε.

    Implementation: sort by value, assign same regime ID to consecutive
    points with gap ≤ ε, increment ID at gaps > ε.

    Returns list of (index, regime_id).
    """
    if not values:
        return []
    sorted_vals = sorted(values, key=lambda x: x[1])
    regime_id = 0
    result = [(sorted_vals[0][0], 0)]
    prev_val = sorted_vals[0][1]
    for idx, val in sorted_vals[1:]:
        if val - prev_val > epsilon:
            regime_id += 1
        result.append((idx, regime_id))
        prev_val = val
    return result


def label_clusters(assignments: list, obs_values: dict,
                   primary_obs: str) -> dict:
    """
    Assign descriptive labels to clusters based on the observable range
    they cover. Labels are post-hoc descriptions, not inputs to the
    partitioning.

    Returns {regime_id: {"label": str, "obs_range": (min, max), "count": int}}
    """
    # Group by regime_id
    clusters = {}
    for idx, rid in assignments:
        if rid not in clusters:
            clusters[rid] = []
        clusters[rid].append(idx)

    labels = {}
    for rid in sorted(clusters.keys()):
        indices = clusters[rid]
        values = [obs_values[primary_obs][i] for i in indices
                  if i in obs_values.get(primary_obs, {})]
        if values:
            obs_min = min(values)
            obs_max = max(values)
            obs_mean = sum(values) / len(values)
        else:
            obs_min = obs_max = obs_mean = None

        labels[rid] = {
            "label": f"R{rid}",
            "count": len(indices),
            "obs_mean": round(obs_mean, 6) if obs_mean is not None else None,
            "obs_range": (round(obs_min, 6), round(obs_max, 6)) if obs_min is not None else None,
        }

    return labels


# ── Main partition extraction ────────────────────────────────────────────────

def assign_regimes(sweep_results: list, extractor, epsilon: float) -> list:
    """
    Extract observables from each sweep point, then assign regimes via
    ε-clustering on the primary observable.

    Returns annotated results with regime_id and all observable values.
    """
    # Phase 1: extract raw observables
    extracted = []
    for r in sweep_results:
        obs_data = extractor(r)
        extracted.append({
            "sweep_result": r,
            "observables": obs_data.get("observables", {}),
            "primary_observable": obs_data.get("primary_observable"),
        })

    # Phase 2: ε-clustering on primary observable
    primary_obs = None
    indexed_values = []
    for i, e in enumerate(extracted):
        obs = e["observables"]
        prim = e["primary_observable"]
        if prim and prim in obs and obs[prim] is not None:
            primary_obs = prim
            indexed_values.append((i, float(obs[prim])))

    if not indexed_values:
        # No valid observables — return unassigned
        return [{**r, "regime_id": -1, "regime_label": "no_data",
                 "observables": {}} for r in sweep_results]

    assignments = eps_cluster(indexed_values, epsilon)
    idx_to_regime = dict(assignments)

    # Phase 3: build per-index observable lookup for labeling
    obs_by_name = {}
    for i, e in enumerate(extracted):
        for name, val in e["observables"].items():
            if name not in obs_by_name:
                obs_by_name[name] = {}
            if val is not None:
                obs_by_name[name][i] = float(val)

    # Phase 4: label clusters
    cluster_labels = label_clusters(assignments, obs_by_name, primary_obs)

    # Phase 5: annotate results
    annotated = []
    for i, r in enumerate(sweep_results):
        rid = idx_to_regime.get(i, -1)
        cl = cluster_labels.get(rid, {})
        obs = extracted[i]["observables"]
        annotated.append({
            **r,
            "regime_id":       rid,
            "regime_label":    cl.get("label", "unassigned"),
            "observable":      obs.get(primary_obs),
            "observable_name": primary_obs,
            # Include all observables for downstream analysis
            "all_observables": {k: v for k, v in obs.items() if v is not None},
        })

    return annotated


def compute_transition_boundary(annotated: list, param: str) -> dict:
    """
    Locate transition boundaries θ* in parameter space:
    parameter values where the regime assignment changes.
    """
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
    extractor = OBSERVABLE_MAP.get(system, extract_observables_stub)

    print(f"\nPartition Extraction: {case_dir.name}  |  system={system}  |  ε={epsilon}")
    print("─" * 50)

    results   = sweep_data.get("results", [])
    annotated = assign_regimes(results, extractor, epsilon)

    # Count regimes
    regime_ids     = [r.get("regime_id", -1) for r in annotated if r.get("regime_id", -1) >= 0]
    unique_regimes = sorted(set(regime_ids))
    regime_counts  = {rid: regime_ids.count(rid) for rid in unique_regimes}

    print(f"  Regime count N = {len(unique_regimes)}  (ε-clustered, no hardcoded thresholds)")
    for rid, cnt in regime_counts.items():
        # Show observable range for each cluster
        obs_vals = [r["observable"] for r in annotated
                    if r.get("regime_id") == rid and r.get("observable") is not None]
        if obs_vals:
            obs_name = annotated[0].get("observable_name", "?")
            print(f"    R{rid}:  {obs_name} ∈ [{min(obs_vals):.4f}, {max(obs_vals):.4f}]  ({cnt} points)")
        else:
            print(f"    R{rid}:  ({cnt} points)")

    # Locate transition boundary
    bc_components = yaml.safe_load((case_dir / "BCManifest.yaml").read_text()).get("bc_components", [])
    sweeps        = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    param         = sweeps[0].get("param") if sweeps else None
    transition    = compute_transition_boundary(annotated, param) if param else {}

    if transition.get("transitions"):
        for t in transition["transitions"]:
            print(f"  Transition: R{t['from_regime']} → R{t['to_regime']}  "
                  f"at {param} ≈ {t['theta_star']:.4f}")
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
        "method":        "eps_clustering",
        "regime_count":  len(unique_regimes),
        "regime_labels": {str(rid): f"R{rid}" for rid in unique_regimes},
        "regime_counts": {str(k): v for k, v in regime_counts.items()},
        "regime_observable_ranges": {
            str(rid): {
                "min": round(min(v for r in annotated if r.get("regime_id") == rid
                                 and r.get("observable") is not None
                                 for v in [r["observable"]]), 6),
                "max": round(max(v for r in annotated if r.get("regime_id") == rid
                                 and r.get("observable") is not None
                                 for v in [r["observable"]]), 6),
            }
            for rid in unique_regimes
            if any(r.get("regime_id") == rid and r.get("observable") is not None for r in annotated)
        },
        "transition_boundary": transition,
        "annotated_results": [
            {
                "sweep_index":     r.get("_sweep_index"),
                "sweep_point":     r.get("_sweep_point"),
                "observable":      r.get("observable"),
                "observable_name": r.get("observable_name"),
                "all_observables": r.get("all_observables", {}),
                "regime_id":       r.get("regime_id"),
                "regime_label":    r.get("regime_label"),
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
