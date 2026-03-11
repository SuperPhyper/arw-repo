"""
pipeline/epsilon_multi_observable.py — Multi-Observable ε-Sweep

For systems with multiple observables (Π = {π₁, π₂, ...}), runs
independent ε-sweeps per observable and a joint ε-sweep to test:

1. Do different observables produce the same plateau structure?
2. Does a single ε suffice, or does each observable need its own εᵢ?
3. What is the joint admissible region in (ε₁, ε₂) space?

First test case: Pendulum with λ_proxy and Var_rel.

Output: results/partition/EpsilonMultiObservable.json

Usage:
    python -m pipeline.epsilon_multi_observable --case cases/CASE-... \
        [--eps-min 0.0001] [--eps-max 1.0] [--eps-steps 60]
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


def eps_cluster_1d(values: list, epsilon: float) -> list:
    """
    ε-cluster a list of (index, value) pairs.
    Returns list of (index, regime_id).
    """
    if not values:
        return []
    sorted_vals = sorted(values, key=lambda x: x[1])
    regime_id = 0
    result = [(sorted_vals[0][0], 0)]
    prev = sorted_vals[0][1]
    for idx, val in sorted_vals[1:]:
        if val - prev > epsilon:
            regime_id += 1
        result.append((idx, regime_id))
        prev = val
    return result


def partition_signature(assignments: list, kappa_order: list) -> dict:
    """Compute N and edge count from regime assignments in κ-order."""
    if not assignments:
        return {"N": 0, "edges": 0}

    idx_to_regime = dict(assignments)
    regime_seq = [idx_to_regime[i] for i in kappa_order if i in idx_to_regime]
    N = len(set(regime_seq))

    edges = set()
    for j in range(1, len(regime_seq)):
        if regime_seq[j] != regime_seq[j-1]:
            e = (min(regime_seq[j-1], regime_seq[j]), max(regime_seq[j-1], regime_seq[j]))
            edges.add(e)

    return {"N": N, "edges": len(edges)}


def find_plateaus(trace: list) -> list:
    """Find plateaus in a σ(ε) trace."""
    if not trace:
        return []
    plateaus = []
    current = {"N": trace[0]["N"], "eps_start": trace[0]["epsilon"],
               "eps_end": trace[0]["epsilon"], "n_points": 1}
    for entry in trace[1:]:
        if entry["N"] == current["N"]:
            current["eps_end"] = entry["epsilon"]
            current["n_points"] += 1
        else:
            plateaus.append(current)
            current = {"N": entry["N"], "eps_start": entry["epsilon"],
                       "eps_end": entry["epsilon"], "n_points": 1}
    plateaus.append(current)

    for p in plateaus:
        if p["eps_end"] > p["eps_start"] > 0:
            p["width_log"] = round(math.log(p["eps_end"] / p["eps_start"]), 4)
        else:
            p["width_log"] = 0.0
    return plateaus


def run_multi_observable_sweep(case_dir: Path, eps_min: float, eps_max: float,
                               eps_steps: int, out_subdir: str):
    sweep_path  = case_dir / "results/raw/sweep_results.json"
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"
    bcm_path    = case_dir / "BCManifest.yaml"

    for p in [sweep_path, scope_path]:
        if not p.exists():
            print(f"ERROR: {p} not found")
            sys.exit(1)

    sweep_data = json.loads(sweep_path.read_text())
    record = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}
    bcm = yaml.safe_load(bcm_path.read_text()) if bcm_path.exists() else {}

    system = record.get("system", "custom")
    results = sweep_data.get("results", [])

    # Determine sweep parameter
    bc_components = bcm.get("bc_components", [])
    sweeps_spec = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    sweep_param = sweeps_spec[0].get("param", "kappa") if sweeps_spec else "kappa"

    # Extract observables per system
    if system == "pendulum":
        observables = {
            "lambda_proxy": [],
            "var_rel": [],
        }
        kappa_order = []  # indices sorted by kappa
        for i, r in enumerate(results):
            if r.get("status") == "ok":
                lp = r.get("lambda_proxy")
                vr = r.get("var_rel")
                if lp is not None:
                    observables["lambda_proxy"].append((i, float(lp)))
                if vr is not None:
                    observables["var_rel"].append((i, float(vr)))
                kappa_order.append((i, float(r["_sweep_point"].get("kappa", 0))))

        kappa_order.sort(key=lambda x: x[1])
        kappa_idx_order = [x[0] for x in kappa_order]
    else:
        print(f"WARNING: Multi-observable sweep not configured for system '{system}'.")
        print(f"  Falling back to single-observable mode.")
        return

    eps_values = np.logspace(math.log10(eps_min), math.log10(eps_max), eps_steps).tolist()

    print(f"\nMulti-Observable ε-Sweep: {case_dir.name}  |  system={system}")
    print(f"  Observables: {list(observables.keys())}")
    print(f"  ε range: [{eps_min}, {eps_max}]  |  {eps_steps} steps")
    print(f"  Data points: {len(results)} (valid: {len(kappa_idx_order)})")
    print("─" * 60)

    # Observable ranges
    for obs_name, obs_vals in observables.items():
        vals = [v for _, v in obs_vals]
        if vals:
            print(f"  {obs_name}: range [{min(vals):.6f}, {max(vals):.6f}]  "
                  f"span={max(vals)-min(vals):.6f}")

    # Phase 1: Independent ε-sweep per observable
    print(f"\n  Phase 1: Independent ε-sweeps per observable")
    per_observable = {}

    for obs_name, obs_vals in observables.items():
        trace = []
        for eps in eps_values:
            assignments = eps_cluster_1d(obs_vals, eps)
            sig = partition_signature(assignments, kappa_idx_order)
            trace.append({"epsilon": round(eps, 6), "N": sig["N"], "edges": sig["edges"]})

        plateaus = find_plateaus(trace)
        per_observable[obs_name] = {
            "trace": trace,
            "plateaus": plateaus,
        }

        print(f"\n    {obs_name}:")
        for p in plateaus:
            if p["n_points"] >= 2:
                print(f"      N={p['N']:2d}  ε ∈ [{p['eps_start']:.6f}, {p['eps_end']:.6f}]  "
                      f"w={p['width_log']:.3f}")

    # Phase 2: Joint ε-sweep (same ε for both observables, intersection of regimes)
    print(f"\n  Phase 2: Joint ε-sweep (same ε, regime = intersection)")
    joint_trace = []

    for eps in eps_values:
        # Assign regimes independently per observable
        all_assignments = {}
        for obs_name, obs_vals in observables.items():
            asgn = eps_cluster_1d(obs_vals, eps)
            all_assignments[obs_name] = dict(asgn)

        # Joint regime: two points are in the same regime iff they agree on ALL observables
        obs_names = list(observables.keys())
        valid_indices = set(kappa_idx_order)
        for a in all_assignments.values():
            valid_indices &= set(a.keys())

        # Create composite regime ID
        composite = {}
        for idx in valid_indices:
            key = tuple(all_assignments[obs][idx] for obs in obs_names)
            composite[idx] = key

        # Map composite keys to integer IDs
        unique_keys = sorted(set(composite.values()))
        key_to_id = {k: i for i, k in enumerate(unique_keys)}
        joint_assignments = [(idx, key_to_id[composite[idx]]) for idx in composite]

        sig = partition_signature(joint_assignments, kappa_idx_order)
        joint_trace.append({"epsilon": round(eps, 6), "N": sig["N"], "edges": sig["edges"]})

    joint_plateaus = find_plateaus(joint_trace)

    print(f"    Joint plateaus:")
    for p in joint_plateaus:
        if p["n_points"] >= 2:
            print(f"      N={p['N']:2d}  ε ∈ [{p['eps_start']:.6f}, {p['eps_end']:.6f}]  "
                  f"w={p['width_log']:.3f}")

    # Phase 3: Cross-observable comparison
    print(f"\n  Phase 3: Cross-observable plateau comparison")

    # For each ε, compare regime counts across observables
    comparison = []
    for i, eps in enumerate(eps_values):
        entry = {"epsilon": round(eps, 6)}
        for obs_name in observables:
            entry[f"N_{obs_name}"] = per_observable[obs_name]["trace"][i]["N"]
        entry["N_joint"] = joint_trace[i]["N"]
        entry["observables_agree"] = len(set(entry[f"N_{obs_name}"] for obs_name in observables)) == 1
        comparison.append(entry)

    # Find ε ranges where observables agree vs disagree
    agree_ranges = []
    disagree_ranges = []
    current_agree = comparison[0]["observables_agree"]
    current_start = comparison[0]["epsilon"]

    for c in comparison[1:]:
        if c["observables_agree"] != current_agree:
            (agree_ranges if current_agree else disagree_ranges).append(
                (current_start, comparison[comparison.index(c) - 1]["epsilon"] if comparison.index(c) > 0 else current_start))
            current_agree = c["observables_agree"]
            current_start = c["epsilon"]
    (agree_ranges if current_agree else disagree_ranges).append(
        (current_start, comparison[-1]["epsilon"]))

    n_agree = sum(1 for c in comparison if c["observables_agree"])
    n_disagree = sum(1 for c in comparison if not c["observables_agree"])
    print(f"    Observables agree on N: {n_agree}/{len(comparison)} ε-values "
          f"({100*n_agree/len(comparison):.0f}%)")

    # Show disagreement zone
    print(f"\n    Disagreement zones (where observables give different N):")
    for c in comparison:
        if not c["observables_agree"]:
            obs_ns = {obs: c[f"N_{obs}"] for obs in observables}
            print(f"      ε={c['epsilon']:.6f}  {obs_ns}  joint={c['N_joint']}")

    # Write output
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "EpsilonMultiObservable.json"

    output = {
        "case_id": record.get("id", case_dir.name),
        "system": system,
        "observables": list(observables.keys()),
        "observable_ranges": {
            obs: {"min": min(v for _, v in vals), "max": max(v for _, v in vals),
                  "span": max(v for _, v in vals) - min(v for _, v in vals)}
            for obs, vals in observables.items() if vals
        },
        "eps_range": [eps_min, eps_max],
        "eps_steps": eps_steps,
        "per_observable": {
            obs: {"plateaus": data["plateaus"]}
            for obs, data in per_observable.items()
        },
        "joint": {
            "plateaus": joint_plateaus,
        },
        "comparison": comparison,
        "agreement_rate": round(n_agree / len(comparison), 3) if comparison else 0,
    }

    out_path.write_text(json.dumps(output, indent=2))
    print(f"\n  Output: {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-observable ε-sweep.")
    parser.add_argument("--case",      required=True)
    parser.add_argument("--eps-min",   type=float, default=0.0001)
    parser.add_argument("--eps-max",   type=float, default=1.0)
    parser.add_argument("--eps-steps", type=int,   default=60)
    parser.add_argument("--out",       dest="out_dir", default="results/partition")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    run_multi_observable_sweep(case_dir, args.eps_min, args.eps_max,
                               args.eps_steps, args.out_dir)


if __name__ == "__main__":
    main()
