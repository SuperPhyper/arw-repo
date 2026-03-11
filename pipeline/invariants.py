"""
pipeline/invariants.py — Partition Invariant Calculator

Computes the four partition invariants used across all ART scopes:
    1. regime_count       — |R_S|
    2. adjacency_graph    — which regimes are adjacent in parameter space
    3. persistence        — fraction of sweep interval with stable partition
    4. hysteresis_width   — width of bistable region (if any)

These invariants feed directly into the transfer distortion metrics (RCD, TBS, SDI).

Output: results/partition/Invariants.json

Usage:
    python -m pipeline.invariants --case cases/CASE-... --in results/partition --out results/partition
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy not installed. Run: pip install numpy --break-system-packages")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent


def build_adjacency_graph(annotated: list, param: str) -> dict:
    """
    Two regimes R_i and R_j are adjacent if they appear at consecutive sweep points
    when sorted by parameter value.
    Returns: { "nodes": [regime_ids], "edges": [[i,j,param_midpoint], ...] }
    """
    pts = sorted(
        [(r.get("sweep_point", {}).get(param), r.get("regime_id", -1))
         for r in annotated if r.get("sweep_point", {}).get(param) is not None],
        key=lambda x: x[0]
    )

    edges   = []
    seen    = set()
    for i in range(1, len(pts)):
        ri, rj = pts[i-1][1], pts[i][1]
        if ri != rj:
            key = tuple(sorted([ri, rj]))
            mid = (pts[i-1][0] + pts[i][0]) / 2
            if key not in seen:
                edges.append({"from": ri, "to": rj, "param_midpoint": mid})
                seen.add(key)

    nodes = sorted({p[1] for p in pts if p[1] >= 0})
    return {"nodes": nodes, "edges": edges}


def compute_persistence(annotated: list, param: str, n_epsilon_levels: int = 3) -> float:
    """
    Persistence score: fraction of the sweep interval for which the regime
    assignment is stable (same regime for at least 2 consecutive points).
    Proxy for: does partition survive admissible perturbations?
    Range: [0, 1]  where 1 = fully stable across sweep.
    """
    pts = sorted(
        [(r.get("sweep_point", {}).get(param), r.get("regime_id", -1))
         for r in annotated if r.get("sweep_point", {}).get(param) is not None],
        key=lambda x: x[0]
    )
    if len(pts) < 2:
        return 1.0

    stable_count = sum(
        1 for i in range(1, len(pts)) if pts[i][1] == pts[i-1][1]
    )
    return round(stable_count / (len(pts) - 1), 4)


def compute_hysteresis_width(annotated: list, param: str) -> float | None:
    """
    Hysteresis width: if multiple transitions occur at different param values
    between the same pair of regimes (indicating bistability), return the
    width of the bistable window. Returns None if no bistability detected.
    """
    pts = sorted(
        [(r.get("sweep_point", {}).get(param), r.get("regime_id", -1))
         for r in annotated if r.get("sweep_point", {}).get(param) is not None],
        key=lambda x: x[0]
    )

    # Find all transitions between each regime pair
    transition_params = defaultdict(list)
    for i in range(1, len(pts)):
        ri, rj = pts[i-1][1], pts[i][1]
        if ri != rj:
            key = tuple(sorted([ri, rj]))
            mid = (pts[i-1][0] + pts[i][0]) / 2
            transition_params[key].append(mid)

    # Hysteresis: same pair appears more than once
    widths = []
    for key, vals in transition_params.items():
        if len(vals) > 1:
            widths.append(max(vals) - min(vals))

    return round(float(max(widths)), 6) if widths else None


def compute_invariants(case_dir: Path, in_subdir: str, out_subdir: str):
    partition_path = case_dir / in_subdir / "PartitionResult.json"
    if not partition_path.exists():
        print(f"ERROR: PartitionResult.json not found at {partition_path}")
        sys.exit(1)

    import yaml
    record = yaml.safe_load((case_dir / "CaseRecord.yaml").read_text()) \
             if (case_dir / "CaseRecord.yaml").exists() else {}
    bcm    = yaml.safe_load((case_dir / "BCManifest.yaml").read_text()) \
             if (case_dir / "BCManifest.yaml").exists() else {}

    partition = json.loads(partition_path.read_text())
    annotated = partition.get("annotated_results", [])

    # Determine sweep parameter from BCManifest
    bc_components = bcm.get("bc_components", [])
    sweeps        = bc_components[0].get("perturbation_program", {}).get("sweeps", []) if bc_components else []
    param         = sweeps[0].get("param") if sweeps else None

    print(f"\nInvariants: {case_dir.name}  |  param={param}")
    print("─" * 50)

    # 1. Regime count
    regime_count = partition.get("regime_count", 0)
    print(f"  regime_count      = {regime_count}")

    # 2. Adjacency graph
    adj = build_adjacency_graph(annotated, param) if param else {"nodes": [], "edges": []}
    print(f"  adjacency_graph   = {len(adj['nodes'])} nodes, {len(adj['edges'])} edges")
    for e in adj["edges"]:
        label_from = partition.get("regime_labels", {}).get(str(e["from"]), f"R{e['from']}")
        label_to   = partition.get("regime_labels", {}).get(str(e["to"]),   f"R{e['to']}")
        print(f"    {label_from} ↔ {label_to}  (at {param} ≈ {e['param_midpoint']:.4f})")

    # 3. Persistence
    persistence = compute_persistence(annotated, param) if param else None
    print(f"  persistence       = {persistence}")

    # 4. Hysteresis width
    hysteresis = compute_hysteresis_width(annotated, param) if param else None
    print(f"  hysteresis_width  = {hysteresis}")

    # Transition boundary (from partition result)
    theta_star = partition.get("transition_boundary", {}).get("theta_star")
    print(f"  theta_star (θ*)   = {theta_star}")

    # Compare with predicted partition type
    import yaml as _yaml
    scope = _yaml.safe_load((case_dir / "ScopeSpec.yaml").read_text()) \
            if (case_dir / "ScopeSpec.yaml").exists() else {}
    predicted_count = scope.get("expected_partition", {}).get("regime_count_predicted")
    predicted_type  = scope.get("expected_partition", {}).get("partition_type")

    match_count = (predicted_count == regime_count) if predicted_count else None
    print(f"\n  Predicted:   type={predicted_type}  count={predicted_count}")
    print(f"  Observed:    count={regime_count}")
    if match_count is not None:
        print(f"  Count match: {'✓' if match_count else '✗'}")

    # Write output
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "Invariants.json"

    invariants = {
        "case_id":           record.get("id", case_dir.name),
        "system":            record.get("system", ""),
        "sweep_param":       param,
        "regime_count":      regime_count,
        "adjacency_graph":   adj,
        "persistence":       persistence,
        "hysteresis_width":  hysteresis,
        "theta_star":        theta_star,
        "predicted_count":   predicted_count,
        "predicted_type":    predicted_type,
        "count_match":       match_count,
    }

    out_path.write_text(json.dumps(invariants, indent=2))
    print(f"\n  Output: {out_path}")
    print(f"\nNext step: python -m pipeline.transfer --caseA {case_dir} --caseB <counterpart>")


def main():
    parser = argparse.ArgumentParser(description="Compute partition invariants.")
    parser.add_argument("--case", required=True)
    parser.add_argument("--in",   dest="in_dir",  default="results/partition")
    parser.add_argument("--out",  dest="out_dir", default="results/partition")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    compute_invariants(case_dir, args.in_dir, args.out_dir)


if __name__ == "__main__":
    main()
