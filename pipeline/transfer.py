"""
pipeline/transfer.py — Cross-Scope Transfer Analyst

Computes the four ARW distortion metrics between two cases (scopes):
    RCD  = |N_A - N_B|           Regime Count Discrepancy
    TBS  = |θ*_A - θ*_B|        Transition Boundary Shift
    PCI  = (1/N) Σ pᵢ           Partition Compatibility Index
    SDI  = graph_edit_distance   Structural Distortion Index
    Φ    = composite score       Admissibility score ∈ [0,1]

Reference: docs/bc_taxonomy/transfer_distortion_metrics.md

Output: transfer/TransferReport.md  and  transfer/TransferMetrics.json

Usage:
    python -m pipeline.transfer --caseA cases/CASE-A --caseB cases/CASE-B --out transfer/CASE-A_vs_CASE-B
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import date

try:
    import numpy as np
    import yaml
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent


# ── Metric Implementations ───────────────────────────────────────────────────

def compute_rcd(inv_a: dict, inv_b: dict) -> dict:
    """RCD = |N_A - N_B|"""
    n_a = inv_a.get("regime_count", 0)
    n_b = inv_b.get("regime_count", 0)
    rcd = abs(n_a - n_b)
    return {
        "value":         rcd,
        "N_A":           n_a,
        "N_B":           n_b,
        "interpretation": "perfect_match" if rcd == 0 else (
                          "minor_mismatch" if rcd == 1 else "significant_mismatch"),
    }


def compute_tbs(inv_a: dict, inv_b: dict) -> dict:
    """
    TBS_norm = |θ*_A / range_A  −  θ*_B / range_B|

    Normalises θ* by each case's sweep range before comparing, making the
    metric meaningful for cross-system-type transfers where control parameter
    axes are incommensurable (e.g. κ ∈ [0,3] vs. E ∈ [0.5,30 J]).

    Falls back to raw TBS = |θ*_A − θ*_B| and labels method as 'raw_only'
    when sweep_range is unavailable in one or both Invariants.json files.
    """
    t_a = inv_a.get("theta_star")
    t_b = inv_b.get("theta_star")
    if t_a is None or t_b is None:
        return {"value": None, "theta_star_A": t_a, "theta_star_B": t_b,
                "note": "TBS undefined: one or both scopes lack a transition boundary"}

    r_a = inv_a.get("sweep_range")
    r_b = inv_b.get("sweep_range")
    tbs_raw = abs(t_a - t_b)

    if r_a and r_b and (r_a[1] - r_a[0]) > 0 and (r_b[1] - r_b[0]) > 0:
        range_a = r_a[1] - r_a[0]
        range_b = r_b[1] - r_b[0]
        tbs_norm = abs(t_a / range_a - t_b / range_b)
        method = "normalised"
    else:
        tbs_norm = tbs_raw
        method = "raw_only"

    interp = ("boundary_preserved" if tbs_norm < 0.05 else
              "moderate_shift"     if tbs_norm < 0.2  else "large_shift")

    return {
        "value":         round(tbs_norm, 6),
        "tbs_raw":       round(tbs_raw, 6),
        "method":        method,
        "theta_star_A":  t_a,
        "theta_star_B":  t_b,
        "sweep_range_A": r_a,
        "sweep_range_B": r_b,
        "interpretation": interp,
    }


def compute_pci(inv_a: dict, inv_b: dict) -> dict:
    """
    PCI = (1/N) Σ pᵢ   where pᵢ = 1 if class Rᵢ in R_A is contained in some class R_B,
                                    0 otherwise.
    Approximated here from regime labels if available, otherwise from adjacency graph structure.
    Full PCI requires aligned annotated_results from both cases.
    """
    n_a = inv_a.get("regime_count", 0)
    if n_a == 0:
        return {"value": None, "note": "PCI undefined: zero regimes in scope A"}

    # Simple structural PCI: fraction of A's regimes that have a structural correspondent in B
    # A regime in A "matches" a regime in B if:
    #   - the regime count is equal (perfect case: PCI = 1)
    #   - or: each adjacency in A has a counterpart in B
    n_b = inv_b.get("regime_count", 0)
    edges_a = inv_a.get("adjacency_graph", {}).get("edges", [])
    edges_b = inv_b.get("adjacency_graph", {}).get("edges", [])

    if n_a == n_b and len(edges_a) == len(edges_b):
        pci = 1.0
        interpretation = "full_compatibility"
    elif n_a == n_b:
        pci = 0.8
        interpretation = "count_match_structure_differs"
    elif n_b == 0:
        pci = 0.0
        interpretation = "no_regimes_in_B"
    else:
        # Partial compatibility: fraction of regimes in A that find any match in B
        pci = round(min(n_a, n_b) / max(n_a, n_b), 4)
        interpretation = "partial_compatibility"

    return {
        "value":          pci,
        "N_A":            n_a,
        "N_B":            n_b,
        "interpretation": interpretation,
        "note":           "Structural PCI approximation. Full PCI requires aligned annotated results.",
    }


def graph_edit_distance(edges_a: list, edges_b: list, n_a: int, n_b: int) -> int:
    """
    SDI = graph_edit_distance(G_A, G_B)
    Simplified: node insertions/deletions + edge insertions/deletions.
    Each node difference costs 1, each edge difference costs 1.
    """
    node_cost = abs(n_a - n_b)
    edge_cost = abs(len(edges_a) - len(edges_b))
    return node_cost + edge_cost


def compute_sdi(inv_a: dict, inv_b: dict) -> dict:
    """SDI = graph_edit_distance(G_A, G_B)"""
    edges_a = inv_a.get("adjacency_graph", {}).get("edges", [])
    edges_b = inv_b.get("adjacency_graph", {}).get("edges", [])
    n_a     = inv_a.get("regime_count", 0)
    n_b     = inv_b.get("regime_count", 0)
    sdi     = graph_edit_distance(edges_a, edges_b, n_a, n_b)
    return {
        "value":          sdi,
        "nodes_A":        n_a,
        "nodes_B":        n_b,
        "edges_A":        len(edges_a),
        "edges_B":        len(edges_b),
        "interpretation": "identical_structure" if sdi == 0 else (
                          "minor_distortion" if sdi <= 2 else "significant_distortion"),
    }


def compute_phi(rcd: dict, tbs: dict, pci: dict, sdi: dict) -> dict:
    """
    Φ = composite admissibility score ∈ [0, 1]
    Higher = more admissible transfer.
    Components: PCI (weight 0.4), normalized RCD (0.3), normalized SDI (0.2), normalized TBS (0.1)
    """
    pci_val = pci.get("value")
    rcd_val = rcd.get("value", 0)
    sdi_val = sdi.get("value", 0)
    tbs_val = tbs.get("value")

    if pci_val is None:
        return {"value": None, "note": "Φ undefined: PCI unavailable"}

    # Normalize components to [0,1] (lower distortion = higher score)
    max_regime_count = max(rcd.get("N_A", 1), rcd.get("N_B", 1), 1)
    rcd_score = max(0, 1 - rcd_val / max_regime_count)
    sdi_score = max(0, 1 - sdi_val / (max_regime_count * 2))
    # tbs_val is already TBS_norm (normalised to [0,1] range); cap at 0.5 for scoring.
    # method="raw_only" means sweep_range was missing — treat as moderate penalty.
    tbs_method = tbs.get("method", "raw_only")
    if tbs_val is not None:
        tbs_score = max(0, 1 - (tbs_val / 0.5))
    else:
        tbs_score = 0.5  # undefined boundary: neutral score

    phi = round(0.4 * pci_val + 0.3 * rcd_score + 0.2 * sdi_score + 0.1 * tbs_score, 4)
    interpretation = (
        "highly_admissible"   if phi >= 0.85 else
        "partially_admissible" if phi >= 0.6  else
        "inadmissible"
    )

    return {
        "value":          phi,
        "components":     {"PCI": pci_val, "RCD_score": rcd_score,
                           "SDI_score": sdi_score, "TBS_score": tbs_score},
        "interpretation": interpretation,
    }


# ── Report Generator ─────────────────────────────────────────────────────────

def write_transfer_report(out_dir: Path, meta: dict, metrics: dict):
    today = date.today().isoformat()
    m = metrics

    lines = [
        f"# Transfer Report: {meta['case_A']} → {meta['case_B']}",
        f"",
        f"**Date:** {today}  ",
        f"**System A:** {meta['system_A']}  ",
        f"**System B:** {meta['system_B']}  ",
        f"**Direction:** {meta.get('direction', 'A → B')}",
        f"",
        f"---",
        f"",
        f"## Distortion Metrics",
        f"",
        f"| Metric | Value | Interpretation |",
        f"|--------|-------|----------------|",
        f"| RCD    | {m['RCD']['value']} | {m['RCD']['interpretation']} |",
        f"| TBS    | {m['TBS'].get('value', 'N/A')} | {m['TBS'].get('interpretation', m['TBS'].get('note', ''))} |",
        f"| PCI    | {m['PCI']['value']} | {m['PCI']['interpretation']} |",
        f"| SDI    | {m['SDI']['value']} | {m['SDI']['interpretation']} |",
        f"| **Φ**  | **{m['Phi'].get('value', 'N/A')}** | **{m['Phi'].get('interpretation', '')}** |",
        f"",
        f"---",
        f"",
        f"## Regime Structure Comparison",
        f"",
        f"| | Scope A ({meta['system_A']}) | Scope B ({meta['system_B']}) |",
        f"|---|---|---|",
        f"| Regime count | {m['RCD']['N_A']} | {m['RCD']['N_B']} |",
        f"| Adjacency edges | {m['SDI']['edges_A']} | {m['SDI']['edges_B']} |",
        f"| θ* (transition) | {m['TBS'].get('theta_star_A', 'N/A')} | {m['TBS'].get('theta_star_B', 'N/A')} |",
        f"",
        f"---",
        f"",
        f"## Admissibility Assessment",
        f"",
        f"Φ = {m['Phi'].get('value', 'N/A')} → **{m['Phi'].get('interpretation', 'unknown')}**",
        f"",
    ]

    # Admissibility criterion from docs/core/arw_scope_reduction_partition_criterion.md
    phi_val = m["Phi"].get("value")
    if phi_val is not None:
        if phi_val >= 0.85:
            lines.append("The scope transition A → B satisfies the ARW admissibility criterion: "
                         "the partition of scope B is a compatible coarsening of scope A "
                         "(∀x: [x]_A ⊆ [x]_B holds approximately).")
        elif phi_val >= 0.6:
            lines.append("The scope transition A → B is partially admissible. "
                         "Some equivalence classes straddle partition boundaries — "
                         "distortion is present but localized. See RCD and SDI for locus.")
        else:
            lines.append("The scope transition A → B is inadmissible under current metrics. "
                         "Regime structure does not transfer. This is an informative failure: "
                         "document which BC class drives the mismatch.")
    lines += [
        f"",
        f"---",
        f"",
        f"## Notes",
        f"",
        f"- PCI approximation used (structural); full PCI requires aligned annotated results.",
        f"- SDI uses simplified graph edit distance (node + edge count differences).",
        f"- Φ weights: PCI=0.4, RCD=0.3, SDI=0.2, TBS=0.1.",
        f"",
        f"*Generated by pipeline.transfer*",
    ]

    report_path = out_dir / "TransferReport.md"
    report_path.write_text("\n".join(lines))
    return report_path


def run_transfer(case_dir_a: Path, case_dir_b: Path, out_subdir: str):
    def load_invariants(case_dir):
        p = case_dir / "results" / "partition" / "Invariants.json"
        if not p.exists():
            print(f"ERROR: Invariants.json not found at {p}")
            sys.exit(1)
        return json.loads(p.read_text())

    def load_record(case_dir):
        p = case_dir / "CaseRecord.yaml"
        return yaml.safe_load(p.read_text()) if p.exists() else {}

    inv_a   = load_invariants(case_dir_a)
    inv_b   = load_invariants(case_dir_b)
    rec_a   = load_record(case_dir_a)
    rec_b   = load_record(case_dir_b)

    print(f"\nTransfer Analysis: {case_dir_a.name} → {case_dir_b.name}")
    print("─" * 50)

    rcd = compute_rcd(inv_a, inv_b)
    tbs = compute_tbs(inv_a, inv_b)
    pci = compute_pci(inv_a, inv_b)
    sdi = compute_sdi(inv_a, inv_b)
    phi = compute_phi(rcd, tbs, pci, sdi)

    print(f"  RCD = {rcd['value']}   ({rcd['interpretation']})")
    print(f"  TBS = {tbs.get('value', 'N/A')}   ({tbs.get('interpretation', tbs.get('note',''))})")
    print(f"  PCI = {pci['value']}   ({pci['interpretation']})")
    print(f"  SDI = {sdi['value']}   ({sdi['interpretation']})")
    print(f"  Φ   = {phi.get('value', 'N/A')}   ({phi.get('interpretation', '')})")

    metrics = {"RCD": rcd, "TBS": tbs, "PCI": pci, "SDI": sdi, "Phi": phi}
    meta    = {
        "case_A":   rec_a.get("id", case_dir_a.name),
        "case_B":   rec_b.get("id", case_dir_b.name),
        "system_A": rec_a.get("system", ""),
        "system_B": rec_b.get("system", ""),
    }

    # Output
    out_dir = case_dir_a / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path   = out_dir / "TransferMetrics.json"
    json_path.write_text(json.dumps({"meta": meta, "metrics": metrics}, indent=2))

    report_path = write_transfer_report(out_dir, meta, metrics)
    print(f"\n  Metrics : {json_path}")
    print(f"  Report  : {report_path}")


def main():
    parser = argparse.ArgumentParser(description="Compute cross-scope transfer distortion metrics.")
    parser.add_argument("--caseA", required=True)
    parser.add_argument("--caseB", required=True)
    parser.add_argument("--out",   default="transfer")
    args = parser.parse_args()

    def resolve(p):
        pp = Path(p)
        return REPO_ROOT / pp if not pp.is_absolute() else pp

    run_transfer(resolve(args.caseA), resolve(args.caseB), args.out)


if __name__ == "__main__":
    main()
