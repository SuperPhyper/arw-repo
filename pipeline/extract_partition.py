"""
pipeline/extract_partition.py — Partition Extractor

Converts raw sweep output (sweep_results.json) into a regime partition
using the robust indistinguishability relation ~_S.

For each sweep point x, extracts the observable value Π(x) and groups
points into equivalence classes under d_Π(x,y) ≤ ε.

CLUSTERING MODEL (BC-coupled):
    Regime assignment is done along the BC axis, not by global observable
    sorting. Two adjacent BC points i, i+1 (in sweep order) trigger a
    regime boundary iff |Π(x_{i+1}) - Π(x_i)| > ε.

    This means ε is a perturbation threshold *on the BC*: it asks
    "does this step along the BC axis produce a distinguishable change
    in the observable?" — which is the correct framing for a partition
    over BC space, not over observable space.

    Consequence: the partition lives in BC-space. Two κ-values that happen
    to produce the same r_ss but are separated by a large region of
    different r_ss values will correctly end up in different regimes.

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
    """Kuramoto: observables are r_ss. Default primary: r_ss."""
    r = result.get("r_ss", None)
    if r is None:
        return {"observables": {}}
    return {
        "observables": {"r_ss": r},
        "default_primary": "r_ss",
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
        "default_primary": "var_rel",
    }


def extract_observables_double_pendulum(result: dict) -> dict:
    """Classical double pendulum: lambda_proxy, var_rel, E_mean.

    Default primary is var_rel — it has larger span and is monotone in E.
    Can be overridden by ScopeSpec Pi[*].primary = true on any observable.
    """
    if result.get("status") != "ok":
        return {"observables": {}}
    return {
        "observables": {
            "lambda_proxy": result.get("lambda_proxy"),
            "var_rel":      result.get("var_rel"),
            "E_mean":       result.get("E_mean"),
        },
        "default_primary": "var_rel",
    }


def extract_observables_stuart_landau_coupled(result: dict) -> dict:
    """Coupled Stuart-Landau oscillators: PLV (primary), amp_asym, freq_gap.

    PLV (phase-locking value) is the relational observable — measures inter-oscillator
    phase coherence. amp_asym is the local emergence precursor (collapses below ε
    before PLV transition — CASE-20260318-0004 emergence window). Default primary: plv.
    """
    return {
        "observables": {
            "plv":      result.get("plv"),
            "amp_asym": result.get("amp_asym"),
            "freq_gap": result.get("freq_gap"),
        },
        "default_primary": "plv",
    }


def extract_observables_stub(result: dict) -> dict:
    return {"observables": {},
            "note": "Implement observable extractor for this system"}


OBSERVABLE_MAP = {
    "kuramoto":               extract_observables_kuramoto,
    "pendulum":               extract_observables_pendulum,
    "double_pendulum":        extract_observables_double_pendulum,
    "stuart_landau_coupled":  extract_observables_stuart_landau_coupled,
    "consensus":              extract_observables_stub,
    "meanfield":              extract_observables_stub,
    "labyrinth":              extract_observables_stub,
}


def resolve_primary_observable(extractor_result: dict, scope_pi: list) -> str | None:
    """
    Determine the primary observable for clustering.

    Priority order:
      1. ScopeSpec Pi entry with `primary: true`
         — must name an observable that exists in extractor_result["observables"]
      2. extractor default_primary (system-level fallback)
      3. First observable in the observables dict

    This ensures the ScopeSpec is the authoritative source for which
    observable drives the partition. The extractor only supplies values.
    """
    available = extractor_result.get("observables", {})

    # 1. ScopeSpec override
    for pi_entry in scope_pi:
        if isinstance(pi_entry, dict) and pi_entry.get("primary") is True:
            # Map pi id to observable name via the 'name' field or id convention
            # Convention: pi_02 → var_rel via the 'map.definition' or explicit 'observable_key'
            obs_key = pi_entry.get("observable_key")
            if obs_key and obs_key in available:
                return obs_key
            # Fallback: try to infer from pi name text
            name = pi_entry.get("name", "").lower()
            for obs_name in available:
                if obs_name.lower() in name or name in obs_name.lower():
                    return obs_name

    # 2. Extractor default
    default = extractor_result.get("default_primary")
    if default and default in available:
        return default

    # 3. First available
    return next(iter(available), None)


# ── BC-coupled ε-clustering ──────────────────────────────────────────────────

def eps_cluster_bc(bc_ordered_values: list, epsilon: float) -> list:
    """
    BC-coupled ε-clustering.

    Input:
        bc_ordered_values: list of (index, bc_param_value, observable_value)
                           sorted by bc_param_value (sweep order along BC axis).
        epsilon:           indistinguishability threshold in observable units.

    Clustering rule:
        Walk along the BC axis in sweep order. Open a new regime whenever
        |Π(x_{i+1}) - Π(x_i)| > ε.

    This couples ε to the BC: the threshold is applied to *consecutive BC
    steps*, not to globally sorted observable values. A regime boundary
    requires that a single step along the BC produces a distinguishable
    observable change.

    Returns list of (original_index, regime_id).

    Note on directionality: if the observable is non-monotone along the BC
    (e.g. the system re-enters a previously visited observable range after
    a transition), those re-entries will be assigned new regime IDs — which
    is the correct behavior for a BC-partition. Use hysteresis_width in
    invariants.py to detect and quantify such cases.
    """
    if not bc_ordered_values:
        return []

    regime_id = 0
    result = [(bc_ordered_values[0][0], 0)]
    prev_obs = bc_ordered_values[0][2]

    for orig_idx, _bc_val, obs_val in bc_ordered_values[1:]:
        if abs(obs_val - prev_obs) > epsilon:
            regime_id += 1
        result.append((orig_idx, regime_id))
        prev_obs = obs_val

    return result


def eps_cluster(values: list, epsilon: float) -> list:
    """
    Legacy observable-space ε-clustering. Kept for reference only.

    DEPRECATED: Use eps_cluster_bc() for all new partition work.
    This function sorts by observable value (not BC order) and therefore
    produces a partition over observable space, not BC space.
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
            obs_min  = min(values)
            obs_max  = max(values)
            obs_mean = sum(values) / len(values)
        else:
            obs_min = obs_max = obs_mean = None

        labels[rid] = {
            "label":     f"R{rid}",
            "count":     len(indices),
            "obs_mean":  round(obs_mean, 6) if obs_mean is not None else None,
            "obs_range": (round(obs_min, 6), round(obs_max, 6)) if obs_min is not None else None,
        }

    return labels


# ── Main partition extraction ────────────────────────────────────────────────

def assign_regimes(sweep_results: list, extractor, epsilon: float,
                   sweep_param: str | None = None,
                   scope_pi: list | None = None) -> list:
    """
    Extract observables from each sweep point, then assign regimes via
    BC-coupled ε-clustering on the primary observable.

    The primary observable is resolved via resolve_primary_observable():
      1. ScopeSpec Pi entry with primary: true  (requires observable_key field)
      2. Extractor default_primary
      3. First available observable

    The sweep_param is used to sort points along the BC axis before
    clustering. If sweep_param is None, the original list order is used.

    Returns annotated results with regime_id and all observable values.
    """
    scope_pi = scope_pi or []

    # Phase 1: extract raw observables
    extracted = []
    for r in sweep_results:
        obs_data = extractor(r)
        prim = resolve_primary_observable(obs_data, scope_pi)
        extracted.append({
            "sweep_result":       r,
            "observables":        obs_data.get("observables", {}),
            "primary_observable": prim,
        })

    # Phase 2: build BC-ordered (index, bc_value, obs_value) triples
    primary_obs = None
    bc_ordered = []

    for i, e in enumerate(extracted):
        obs  = e["observables"]
        prim = e["primary_observable"]
        if prim and prim in obs and obs[prim] is not None:
            primary_obs = prim
            sp = e["sweep_result"].get("_sweep_point", {})
            bc_val = sp.get(sweep_param, i) if sweep_param else i
            # Fall back to index if bc_val is not numeric
            try:
                bc_val = float(bc_val)
            except (TypeError, ValueError):
                bc_val = float(i)
            bc_ordered.append((i, bc_val, float(obs[prim])))

    if not bc_ordered:
        return [{**r, "regime_id": -1, "regime_label": "no_data",
                 "observables": {}} for r in sweep_results]

    # Sort by BC parameter value (sweep axis)
    bc_ordered.sort(key=lambda x: x[1])

    # Phase 3: BC-coupled clustering
    assignments = eps_cluster_bc(bc_ordered, epsilon)
    idx_to_regime = dict(assignments)

    # Phase 4: build per-index observable lookup for labeling
    obs_by_name = {}
    for i, e in enumerate(extracted):
        for name, val in e["observables"].items():
            if name not in obs_by_name:
                obs_by_name[name] = {}
            if val is not None:
                obs_by_name[name][i] = float(val)

    # Phase 5: label clusters
    cluster_labels = label_clusters(assignments, obs_by_name, primary_obs)

    # Phase 6: annotate results
    annotated = []
    for i, r in enumerate(sweep_results):
        rid = idx_to_regime.get(i, -1)
        cl  = cluster_labels.get(rid, {})
        obs = extracted[i]["observables"]
        annotated.append({
            **r,
            "regime_id":       rid,
            "regime_label":    cl.get("label", "unassigned"),
            "observable":      obs.get(primary_obs),
            "observable_name": primary_obs,
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
                "from_regime":  pts[i-1][1],
                "to_regime":    pts[i][1],
                "param_before": pts[i-1][0],
                "param_after":  pts[i][0],
                "theta_star":   (pts[i-1][0] + pts[i][0]) / 2,
            })
    return {
        "param":      param,
        "transitions": transitions,
        "theta_star": transitions[0]["theta_star"] if transitions else None,
    }


def extract_partition(case_dir: Path, in_subdir: str, out_subdir: str):
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
    bcm        = yaml.safe_load(bcm_path.read_text())    if bcm_path.exists()    else {}

    system    = record.get("system", "custom")
    epsilon   = scope.get("epsilon", {}).get("value", 0.01)
    extractor = OBSERVABLE_MAP.get(system, extract_observables_stub)
    scope_pi  = scope.get("Pi", [])

    # Determine sweep parameter — needed to sort points along BC axis
    bc_components = bcm.get("bc_components", [])
    sweeps        = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    sweep_param   = sweeps[0].get("param") if sweeps else None

    # Resolve primary observable for logging
    _sample      = extractor({"status": "ok", "r_ss": 0, "lambda_proxy": 0,
                               "var_rel": 0, "E_mean": 0, "kappa": 0})
    primary_name = resolve_primary_observable(_sample, scope_pi) or "?"

    print(f"\nPartition Extraction: {case_dir.name}  |  system={system}  |  ε={epsilon}")
    print(f"  BC sweep param: {sweep_param}  |  primary observable: {primary_name}")
    print(f"  clustering: BC-coupled (along {sweep_param}-axis)")
    print("─" * 50)

    results   = sweep_data.get("results", [])
    annotated = assign_regimes(results, extractor, epsilon,
                                sweep_param=sweep_param, scope_pi=scope_pi)

    # Count regimes
    regime_ids     = [r.get("regime_id", -1) for r in annotated if r.get("regime_id", -1) >= 0]
    unique_regimes = sorted(set(regime_ids))
    regime_counts  = {rid: regime_ids.count(rid) for rid in unique_regimes}

    print(f"  Regime count N = {len(unique_regimes)}  (ε-clustered along BC axis)")
    for rid, cnt in regime_counts.items():
        obs_vals = [r["observable"] for r in annotated
                    if r.get("regime_id") == rid and r.get("observable") is not None]
        if obs_vals:
            obs_name = annotated[0].get("observable_name", "?")
            print(f"    R{rid}:  {obs_name} ∈ [{min(obs_vals):.4f}, {max(obs_vals):.4f}]  ({cnt} points)")
        else:
            print(f"    R{rid}:  ({cnt} points)")

    # Locate transition boundary
    transition = compute_transition_boundary(annotated, sweep_param) if sweep_param else {}

    if transition.get("transitions"):
        for t in transition["transitions"]:
            print(f"  Transition: R{t['from_regime']} → R{t['to_regime']}  "
                  f"at {sweep_param} ≈ {t['theta_star']:.4f}")
    else:
        print(f"  No transition boundary detected for param: {sweep_param}")

    # Write output
    out_dir  = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "PartitionResult.json"

    partition_result = {
        "case_id":       record.get("id", case_dir.name),
        "system":        system,
        "epsilon":       epsilon,
        "method":        "eps_clustering_bc_coupled",
        "sweep_param":   sweep_param,
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
