"""
pipeline/transfer_v2.py — Rigorous Cross-Scope Transfer Analyst (v2)

This module is a non-destructive replacement for `pipeline/transfer.py` (v1).
v1 is intentionally left untouched so historical Phi values remain reproducible.

------------------------------------------------------------------------------
Why v2 exists — defects found in v1 (transfer.py)
------------------------------------------------------------------------------
D1  PCI was a *structural proxy* computed only from `regime_count` and the
    adjacency edge count (transfer.py:96-135). It never read the per-point
    regime labels that already exist in PartitionResult.json
    ("annotated_results"). Consequently PCI was collinear with RCD and SDI:
    three of the four metrics were functions of (N_A, N_B, |E_A|, |E_B|).
    With Phi weights PCI=0.4, RCD=0.3, SDI=0.2, TBS=0.1, this meant ~90% of
    the Phi weight tracked the regime count N alone.
    -> v2 computes a REAL overlap-based PCI from annotated_results, aligned on
       a common normalised BC axis. PCI now carries independent information.

D2  SDI's node term is |N_A - N_B|, i.e. it *contains* RCD. So a regime-count
    difference was counted three times (RCD, SDI-node-part, PCI-proxy).
    -> v2 folds regime-count + adjacency agreement into ONE topology term,
       counted once, and reports every component separately. It raises an
       explicit N-confound flag when RCD=0 and a disagreement flag when the
       real-overlap PCI and the topology term diverge.

D3  TBS_norm = |theta*_A/range_A - theta*_B/range_B| is sweep-WINDOW dependent:
    widening a sweep range halves theta*_norm. The near-zero TBS values that
    drove "boundary_preserved" verdicts were partly artefacts of experimenter-
    chosen windows (e.g. 0.34 == 0.34 across unrelated systems).
    -> v2 reports a window-sensitivity band for TBS_norm and an alternative
       observable-intrinsic locator, so window fragility is visible.

D4  Controls were markdown checkboxes. A TransferMetrics.json with Phi=1.0
    could be (and was) written for cases whose pipeline never ran
    (annotated_results empty).
    -> v2 has a mechanical input validator. If annotated_results are empty,
       sweep_range is missing, or epsilon is unmatched without documentation,
       it returns VOID and refuses to emit a Phi.

Reference: docs/bc_taxonomy/transfer_distortion_metrics.md
"""

import argparse
import json
import sys
from itertools import permutations
from pathlib import Path
from datetime import date

try:
    import numpy as np
    import yaml
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
GRID_N = 1000  # resolution of the common normalised BC axis


# ── Loading & normalisation ──────────────────────────────────────────────────

def _normalised_sequence(part: dict, inv: dict):
    """
    Return (x_norm, regime_id, observable) arrays from annotated_results,
    with x_norm = (theta - range_min) / (range_max - range_min) in [0,1].

    Raises ValueError if annotated_results is empty or sweep_range invalid —
    this is the core VOID condition for D4.
    """
    ann = part.get("annotated_results", [])
    if not ann:
        raise ValueError("annotated_results is empty (pipeline never produced a partition)")

    sweep_param = part.get("sweep_param") or inv.get("sweep_param")
    rng = inv.get("sweep_range")
    if not rng or (rng[1] - rng[0]) <= 0:
        raise ValueError("sweep_range missing or non-positive in Invariants.json")
    lo, span = rng[0], (rng[1] - rng[0])

    xs, regs, obs = [], [], []
    for a in ann:
        theta = a["sweep_point"][sweep_param]
        xs.append((theta - lo) / span)
        regs.append(int(a["regime_id"]))
        obs.append(float(a.get("observable", np.nan)))
    order = np.argsort(xs)
    return np.array(xs)[order], np.array(regs)[order], np.array(obs)[order]


def _resample_to_grid(x_norm, regime_id, grid):
    """Nearest-neighbour resample of the regime label onto a common grid in [0,1]."""
    idx = np.searchsorted(x_norm, grid)
    idx = np.clip(idx, 0, len(x_norm) - 1)
    left = np.clip(idx - 1, 0, len(x_norm) - 1)
    take_left = np.abs(grid - x_norm[left]) <= np.abs(grid - x_norm[idx])
    chosen = np.where(take_left, left, idx)
    return regime_id[chosen]


# ── Metric 1: RCD (unchanged definition) ─────────────────────────────────────

def compute_rcd(inv_a, inv_b):
    n_a, n_b = inv_a.get("regime_count", 0), inv_b.get("regime_count", 0)
    rcd = abs(n_a - n_b)
    return {"value": rcd, "N_A": n_a, "N_B": n_b,
            "interpretation": "perfect_match" if rcd == 0 else
            ("minor_mismatch" if rcd == 1 else "significant_mismatch")}


# ── Metric 3 (the important fix): REAL overlap-based PCI ──────────────────────

def _adjusted_rand_index(a, b):
    """Label-agnostic partition agreement via pair counting (Hubert & Arabie 1985)."""
    a_labels = {v: i for i, v in enumerate(np.unique(a))}
    b_labels = {v: i for i, v in enumerate(np.unique(b))}
    cont = np.zeros((len(a_labels), len(b_labels)), dtype=float)
    for ai, bi in zip(a, b):
        cont[a_labels[ai], b_labels[bi]] += 1
    n = cont.sum()
    if n < 2:
        return 1.0
    def comb2(x):
        return x * (x - 1) / 2.0
    sum_ij = comb2(cont).sum()
    sum_a = comb2(cont.sum(axis=1)).sum()
    sum_b = comb2(cont.sum(axis=0)).sum()
    expected = sum_a * sum_b / comb2(n)
    maxi = 0.5 * (sum_a + sum_b)
    if maxi - expected == 0:
        return 1.0
    return float((sum_ij - expected) / (maxi - expected))


def compute_pci_real(part_a, inv_a, part_b, inv_b):
    """
    REAL Partition Compatibility Index — the canonical containment definition
    PCI = (1/N) Σ_i |R_i| · max_j |R_i ∩ R'_j| / |R_i|
    computed on a common normalised BC grid, plus a symmetric ARI companion.

    Unlike v1, this reads the per-point regime labels (annotated_results) and
    is NOT a function of regime_count alone. Two partitions with equal N but
    different boundary placement score PCI < 1 here (they scored 1.0 in v1).
    """
    xa, ra, _ = _normalised_sequence(part_a, inv_a)
    xb, rb, _ = _normalised_sequence(part_b, inv_b)
    grid = (np.arange(GRID_N) + 0.5) / GRID_N
    ga = _resample_to_grid(xa, ra, grid)
    gb = _resample_to_grid(xb, rb, grid)

    def containment(src, dst):
        total, acc = 0, 0.0
        for c in np.unique(src):
            mask = src == c
            size = mask.sum()
            # largest share of this src-class that lands in a single dst-class
            best = max((dst[mask] == d).sum() for d in np.unique(dst[mask]))
            acc += best
            total += size
        return acc / total

    pci_ab = containment(ga, gb)   # canonical directional S_A -> S_B
    pci_ba = containment(gb, ga)
    ari = _adjusted_rand_index(ga, gb)

    return {
        "value": round(min(pci_ab, pci_ba), 4),    # strict (worst-direction) PCI
        "pci_A_to_B": round(pci_ab, 4),
        "pci_B_to_A": round(pci_ba, 4),
        "ari": round(ari, 4),
        "method": "overlap_on_normalised_grid",
        "grid_n": GRID_N,
        "interpretation": (
            "full_compatibility" if min(pci_ab, pci_ba) >= 0.95 else
            "high_compatibility" if min(pci_ab, pci_ba) >= 0.8 else
            "partial_compatibility" if min(pci_ab, pci_ba) >= 0.5 else
            "low_compatibility"),
        "note": "Real overlap PCI from annotated_results; independent of regime count.",
    }


# ── Metric 2: TBS with window-sensitivity + intrinsic locator (D3) ────────────

def _theta_star_norm(inv):
    t = inv.get("theta_star")
    rng = inv.get("sweep_range")
    if t is None or not rng or (rng[1] - rng[0]) <= 0:
        return None
    return (t - rng[0]) / (rng[1] - rng[0])


def compute_tbs(inv_a, inv_b, part_a=None, part_b=None):
    na, nb = _theta_star_norm(inv_a), _theta_star_norm(inv_b)
    if na is None or nb is None:
        return {"value": None, "note": "TBS undefined: theta_star or sweep_range missing"}

    tbs_norm = abs(na - nb)

    # D3a — window sensitivity: how much TBS_norm moves if either sweep window
    # had been cropped. Recompute theta*_norm inside cropped sub-windows.
    def renorm(inv, crop):
        t, rng = inv.get("theta_star"), inv.get("sweep_range")
        lo = rng[0] + crop * (rng[1] - rng[0])
        hi = rng[1] - crop * (rng[1] - rng[0])
        if not (lo < t < hi):
            return None
        return (t - lo) / (hi - lo)

    band = []
    for ca in (0.0, 0.1, 0.2):
        for cb in (0.0, 0.1, 0.2):
            xa, xb = renorm(inv_a, ca), renorm(inv_b, cb)
            if xa is not None and xb is not None:
                band.append(abs(xa - xb))
    band_min, band_max = (min(band), max(band)) if band else (tbs_norm, tbs_norm)

    # D3b — observable-intrinsic locator: position where the observable reaches
    # 50% of its own span. Window-robust because it uses the observable range,
    # not the (arbitrary) parameter window.
    tbs_obs = None
    if part_a is not None and part_b is not None:
        try:
            xa_, _, oa = _normalised_sequence(part_a, inv_a)
            xb_, _, ob = _normalised_sequence(part_b, inv_b)
            def half_span_pos(x, o):
                o = np.asarray(o, float)
                lo, hi = np.nanmin(o), np.nanmax(o)
                if hi - lo == 0:
                    return None
                half = lo + 0.5 * (hi - lo)
                k = int(np.argmin(np.abs(o - half)))
                return x[k]
            pa, pb = half_span_pos(xa_, oa), half_span_pos(xb_, ob)
            if pa is not None and pb is not None:
                tbs_obs = round(abs(pa - pb), 4)
        except Exception:
            tbs_obs = None

    window_fragile = (band_max - band_min) > 0.1
    return {
        "value": round(tbs_norm, 6),
        "theta_star_norm_A": round(na, 4),
        "theta_star_norm_B": round(nb, 4),
        "window_band": [round(band_min, 4), round(band_max, 4)],
        "window_fragile": window_fragile,
        "tbs_observable_intrinsic": tbs_obs,
        "interpretation": ("boundary_preserved" if tbs_norm < 0.05 else
                           "moderate_shift" if tbs_norm < 0.2 else "large_shift"),
        "note": ("TBS_norm is sweep-window dependent; window_band shows its range "
                 "under +/-10-20% window cropping. tbs_observable_intrinsic is the "
                 "window-robust companion (0.5-span crossing position)."),
    }


# ── Topology term: RCD + adjacency, counted ONCE (D2) ─────────────────────────

def compute_topology(inv_a, inv_b):
    n_a, n_b = inv_a.get("regime_count", 0), inv_b.get("regime_count", 0)
    e_a = len(inv_a.get("adjacency_graph", {}).get("edges", []))
    e_b = len(inv_b.get("adjacency_graph", {}).get("edges", []))
    norm = max(n_a, n_b, 1)
    count_score = max(0.0, 1 - abs(n_a - n_b) / norm)
    edge_score = max(0.0, 1 - abs(e_a - e_b) / max(e_a, e_b, 1))
    topo = round(0.5 * count_score + 0.5 * edge_score, 4)
    return {"value": topo, "count_score": round(count_score, 4),
            "edge_score": round(edge_score, 4), "N_A": n_a, "N_B": n_b,
            "edges_A": e_a, "edges_B": e_b,
            "note": "Regime-count + adjacency agreement, counted once (replaces "
                    "collinear RCD+SDI of v1)."}


# ── Composite Phi v2 ──────────────────────────────────────────────────────────

# Provisional weights (calibratable). Majority weight on the real-overlap PCI;
# topology and TBS are secondary. Documented as provisional in the report.
W_PCI, W_TOPO, W_TBS = 0.55, 0.25, 0.20


def compute_phi_v2(pci, tbs, topo, rcd):
    pci_val = pci.get("value")
    if pci_val is None:
        return {"value": None, "note": "Phi undefined: PCI unavailable (VOID input)"}
    tbs_val = tbs.get("value")
    tbs_score = max(0.0, 1 - tbs_val / 0.5) if tbs_val is not None else 0.5
    topo_val = topo["value"]

    phi = round(W_PCI * pci_val + W_TOPO * topo_val + W_TBS * tbs_score, 4)

    flags = []
    if rcd.get("value") == 0:
        flags.append("N_CONFOUND: regime counts equal — legacy v1 Phi was inflated "
                     "by count match; trust PCI_real for true overlap.")
    if abs(pci_val - topo_val) > 0.3:
        flags.append("COMPONENT_DISAGREEMENT: real-overlap PCI and topology term "
                     "diverge by >0.3 — single Phi is not a faithful summary.")
    if tbs.get("window_fragile"):
        flags.append("TBS_WINDOW_FRAGILE: TBS_norm moves >0.1 under window cropping "
                     "— boundary-shift verdict is sweep-window dependent.")

    if any(f.startswith("COMPONENT_DISAGREEMENT") for f in flags):
        verdict = "ambiguous_requires_inspection"
    else:
        verdict = ("highly_admissible" if phi >= 0.85 else
                   "partially_admissible" if phi >= 0.6 else "inadmissible")

    return {"value": phi, "verdict": verdict,
            "components": {"PCI_real": pci_val, "topology": topo_val,
                           "TBS_score": round(tbs_score, 4)},
            "weights": {"PCI": W_PCI, "topology": W_TOPO, "TBS": W_TBS},
            "flags": flags}


# ── Mechanical input validator (D4) ───────────────────────────────────────────

def validate_inputs(part_a, inv_a, part_b, inv_b, eps_a, eps_b, eps_matched_doc):
    """Returns a list of VOID reasons. Empty list = inputs admissible."""
    void = []
    for tag, part, inv in (("A", part_a, inv_a), ("B", part_b, inv_b)):
        if not part.get("annotated_results"):
            void.append(f"VOID[{tag}]: annotated_results empty — pipeline never ran.")
        if not inv.get("sweep_range"):
            void.append(f"VOID[{tag}]: sweep_range missing in Invariants.json.")
        if inv.get("regime_count", 0) < 1:
            void.append(f"VOID[{tag}]: regime_count < 1.")
    if eps_a is not None and eps_b is not None and eps_a != eps_b and not eps_matched_doc:
        void.append(f"VOID: epsilon mismatch ({eps_a} vs {eps_b}) without a documented "
                    f"matching method (pass --eps-matched-doc).")
    return void


# ── Report ────────────────────────────────────────────────────────────────────

def write_report(out_dir, meta, metrics, void):
    today = date.today().isoformat()
    L = [f"# Transfer Report v2: {meta['case_A']} -> {meta['case_B']}", "",
         f"**Date:** {today}  ", f"**System A:** {meta['system_A']}  ",
         f"**System B:** {meta['system_B']}  ",
         f"**Engine:** pipeline/transfer_v2.py (overlap-based PCI)", "", "---", ""]

    if void:
        L += ["## RESULT: VOID", "",
              "The transfer metrics were NOT computed. The following mandatory "
              "input conditions failed:", ""]
        L += [f"- {r}" for r in void]
        L += ["", "No Phi is reported. Fix the inputs (run the pipeline so "
              "annotated_results are non-empty, add sweep_range, document "
              "epsilon matching) and re-run.", ""]
        (out_dir / "TransferReport_v2.md").write_text("\n".join(L))
        return

    m = metrics
    phi = m["Phi"]
    L += ["## Composite Phi (v2)", "",
          f"**Phi = {phi['value']} -> {phi['verdict']}**", "",
          "| Component | Value | Weight |", "|---|---|---|",
          f"| PCI_real (overlap) | {phi['components']['PCI_real']} | {phi['weights']['PCI']} |",
          f"| topology (count+adjacency) | {phi['components']['topology']} | {phi['weights']['topology']} |",
          f"| TBS_score | {phi['components']['TBS_score']} | {phi['weights']['TBS']} |", ""]
    if phi["flags"]:
        L += ["### Flags", ""] + [f"- **{f}**" for f in phi["flags"]] + [""]

    L += ["---", "", "## Real Partition Compatibility (the v1 fix)", "",
          f"- PCI (strict, worst direction): **{m['PCI']['value']}** ({m['PCI']['interpretation']})",
          f"- PCI A->B: {m['PCI']['pci_A_to_B']}  |  PCI B->A: {m['PCI']['pci_B_to_A']}",
          f"- Adjusted Rand Index: {m['PCI']['ari']}",
          f"- Method: {m['PCI']['method']} (grid N={m['PCI']['grid_n']})", "",
          "PCI is computed from per-point regime labels on a common normalised BC "
          "axis. It is independent of regime count, unlike the v1 structural proxy.", "",
          "---", "", "## Transition Boundary Shift (window-aware)", "",
          f"- TBS_norm: {m['TBS']['value']} ({m['TBS']['interpretation']})",
          f"- theta*_norm A / B: {m['TBS']['theta_star_norm_A']} / {m['TBS']['theta_star_norm_B']}",
          f"- Window-sensitivity band: {m['TBS']['window_band']}  (fragile={m['TBS']['window_fragile']})",
          f"- Observable-intrinsic TBS (0.5-span): {m['TBS']['tbs_observable_intrinsic']}", "",
          "---", "", "## Topology (RCD + adjacency, counted once)", "",
          f"- topology score: {m['topology']['value']} "
          f"(count={m['topology']['count_score']}, edge={m['topology']['edge_score']})",
          f"- N_A={m['topology']['N_A']}, N_B={m['topology']['N_B']}, "
          f"edges_A={m['topology']['edges_A']}, edges_B={m['topology']['edges_B']}",
          f"- RCD (reported separately): {m['RCD']['value']} ({m['RCD']['interpretation']})", "",
          "---", "", "## Notes", "",
          "- Phi v2 weights are provisional (PCI 0.55 / topology 0.25 / TBS 0.20) and "
          "calibratable; report every component, not just Phi.",
          "- v1 collinearity removed: PCI is now real overlap; RCD and adjacency are a "
          "single topology term (v1 double-counted N via RCD + SDI-node + PCI-proxy).",
          "- GUARD-6: this auto-report does not include the observable BC structures of "
          "both scopes (not present in Invariants/PartitionResult). Supplement the report "
          "with each observable's BC notation (e.g. r_ss = R^3.A.D) before recording an "
          "outcome — Phi measures observable transfer, not system transfer.",
          "", "*Generated by pipeline.transfer_v2*"]
    (out_dir / "TransferReport_v2.md").write_text("\n".join(L))


# ── Driver ────────────────────────────────────────────────────────────────────

def run(case_a, case_b, out_subdir, eps_matched_doc=None):
    def load(case, name):
        p = case / "results" / "partition" / name
        if not p.exists():
            print(f"ERROR: {name} not found at {p}")
            sys.exit(1)
        return json.loads(p.read_text())

    def rec(case):
        p = case / "CaseRecord.yaml"
        return yaml.safe_load(p.read_text()) if p.exists() else {}

    inv_a, inv_b = load(case_a, "Invariants.json"), load(case_b, "Invariants.json")
    part_a, part_b = load(case_a, "PartitionResult.json"), load(case_b, "PartitionResult.json")
    rec_a, rec_b = rec(case_a), rec(case_b)
    eps_a, eps_b = part_a.get("epsilon"), part_b.get("epsilon")

    void = validate_inputs(part_a, inv_a, part_b, inv_b, eps_a, eps_b, bool(eps_matched_doc))

    # Trivial-partition guard: a single-regime partition (N<=1) has no transition,
    # so PCI is degenerately 1.0 and TBS is undefined. Such a comparison is NOT an
    # admissible transfer — it usually signals observable insufficiency (F1: span < eps).
    n_a_chk = inv_a.get("regime_count", 0)
    n_b_chk = inv_b.get("regime_count", 0)
    trivial = [f"TRIVIAL[{tag}]: regime_count={n} (<=1) at this eps — no transition to "
               f"transfer; likely F1 observable insufficiency (span < eps)."
               for tag, n in (("A", n_a_chk), ("B", n_b_chk)) if n <= 1]
    meta = {"case_A": rec_a.get("id", case_a.name), "case_B": rec_b.get("id", case_b.name),
            "system_A": rec_a.get("system", part_a.get("system", "")),
            "system_B": rec_b.get("system", part_b.get("system", "")),
            "epsilon_A": eps_a, "epsilon_B": eps_b,
            "eps_matched_doc": eps_matched_doc}

    out_dir = case_a / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)

    if void:
        print("\nTRANSFER v2: VOID")
        for r in void:
            print("  " + r)
        (out_dir / "TransferMetrics_v2.json").write_text(
            json.dumps({"meta": meta, "result": "VOID", "void_reasons": void}, indent=2))
        write_report(out_dir, meta, None, void)
        print(f"  -> {out_dir/'TransferReport_v2.md'}")
        return

    if trivial:
        print("\nTRANSFER v2: TRIVIAL PARTITION (no transfer computed)")
        for r in trivial:
            print("  " + r)
        note = ("A single-regime partition has no transition to transfer. This is not an "
                "admissible result and not a VOID input error — it signals that at least one "
                "observable does not resolve a transition at the chosen eps (F1: span < eps). "
                "Lower eps with a sigma_Delta-justified value, or replace the observable.")
        (out_dir / "TransferMetrics_v2.json").write_text(json.dumps(
            {"meta": meta, "result": "TRIVIAL_PARTITION",
             "regime_count_A": n_a_chk, "regime_count_B": n_b_chk,
             "trivial_reasons": trivial, "note": note}, indent=2))
        lines = [f"# Transfer Report v2: {meta['case_A']} -> {meta['case_B']}", "",
                 "## RESULT: TRIVIAL PARTITION — no transfer computed", "",
                 f"- N_A = {n_a_chk}, N_B = {n_b_chk}", ""]
        lines += [f"- {r}" for r in trivial] + ["", note, ""]
        (out_dir / "TransferReport_v2.md").write_text("\n".join(lines))
        print(f"  -> {out_dir/'TransferReport_v2.md'}")
        return

    rcd = compute_rcd(inv_a, inv_b)
    pci = compute_pci_real(part_a, inv_a, part_b, inv_b)
    tbs = compute_tbs(inv_a, inv_b, part_a, part_b)
    topo = compute_topology(inv_a, inv_b)
    phi = compute_phi_v2(pci, tbs, topo, rcd)
    metrics = {"RCD": rcd, "PCI": pci, "TBS": tbs, "topology": topo, "Phi": phi}

    print(f"\nTRANSFER v2: {meta['case_A']} -> {meta['case_B']}")
    print("-" * 56)
    print(f"  PCI_real = {pci['value']}  (ARI={pci['ari']})  [{pci['interpretation']}]")
    print(f"  TBS_norm = {tbs['value']}  band={tbs['window_band']} fragile={tbs['window_fragile']}")
    print(f"  topology = {topo['value']}   RCD = {rcd['value']}")
    print(f"  Phi      = {phi['value']}   -> {phi['verdict']}")
    for f in phi["flags"]:
        print(f"  FLAG: {f}")

    (out_dir / "TransferMetrics_v2.json").write_text(
        json.dumps({"meta": meta, "metrics": metrics}, indent=2))
    write_report(out_dir, meta, metrics, [])
    print(f"  -> {out_dir/'TransferMetrics_v2.json'}")
    print(f"  -> {out_dir/'TransferReport_v2.md'}")


def main():
    ap = argparse.ArgumentParser(description="Rigorous cross-scope transfer metrics (v2).")
    ap.add_argument("--caseA", required=True)
    ap.add_argument("--caseB", required=True)
    ap.add_argument("--out", default="transfer_v2")
    ap.add_argument("--eps-matched-doc", default=None,
                    help="String documenting the epsilon-matching method; required "
                         "when epsilon_A != epsilon_B, else result is VOID.")
    args = ap.parse_args()

    def resolve(p):
        pp = Path(p)
        return REPO_ROOT / pp if not pp.is_absolute() else pp

    run(resolve(args.caseA), resolve(args.caseB), args.out, args.eps_matched_doc)


if __name__ == "__main__":
    main()
