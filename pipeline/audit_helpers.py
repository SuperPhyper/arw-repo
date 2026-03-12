"""
pipeline/audit_helpers.py — Failure Auditor (Agent A5)

Reads all artifacts for a case and produces a FailureAudit.md that checks:
    1. Scope leakage: ARW-forbidden constructs in ScopeSpec
    2. Observable sufficiency: span(Π_i) vs ε — instrument check, not scope check
    3. ε robustness: is ε tied to Δ? Is the stability window non-trivial?
    4. Partition integrity: does observed partition match predicted?
    5. Falsification: are BC-level falsification conditions defined and checkable?
       (F1: BC wirkungslos, F2: Partition nicht BC-reproduzierbar,
        F3: kein robustes Plateau für gesamtes Π, F4: θ* nicht auflösbar)
    6. Transfer integrity: distortion metrics within expected bounds?
    7. Open failure modes from BCManifest

DESIGN PRINCIPLE — Observable insufficiency vs Scope falsification:
    Observable insufficiency (small span, no plateau for a single π) is an
    instrument problem. It triggers observable replacement, not scope rejection.
    Scope falsification requires that the BC itself is shown to be structureless
    (F1, F3) or that the partition is demonstrably not produced by the BC (F2).
    This distinction is enforced throughout this module.

Usage:
    python -m pipeline.audit_helpers --case cases/CASE-... --phase 1 --out audits
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed.")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

ARW_FORBIDDEN_KEYWORDS = [
    "hamiltonian", "objective", "reward",
    "policy", "regulation_error", "desired_state", "goal", "utility",
    "optimal", "loss_function", "ground_truth", "true_model",
]


# ── Check 1: Scope leakage ───────────────────────────────────────────────────

def check_scope_leakage(scope: dict) -> list:
    """Check for ARW-forbidden constructs in ScopeSpec."""
    issues = []
    scope_str = yaml.dump(scope).lower()
    for kw in ARW_FORBIDDEN_KEYWORDS:
        if kw in scope_str:
            issues.append(
                f"Possible scope leakage: '{kw}' found in ScopeSpec "
                f"(dynamics/goal constructs belong in ART simulation code, not schema)"
            )
    return issues


# ── Check 2: Observable sufficiency ─────────────────────────────────────────

def check_observable_sufficiency(scope: dict, partition: dict | None) -> list:
    """
    Check whether each observable has sufficient span relative to ε_working.

    This is an INSTRUMENT check, not a scope falsification check.
    Issues here mean: replace or supplement the observable.
    They do NOT mean the scope is inadmissible.
    """
    issues = []
    eps_working = scope.get("epsilon", {}).get("value")
    if eps_working is None:
        return issues

    threshold = 2 * eps_working

    # Check against declared spans in observable_sufficiency block (if present)
    obs_suff = scope.get("observable_sufficiency", {})
    per_obs  = obs_suff.get("per_observable", [])

    for obs in per_obs:
        span = obs.get("span_observed")
        oid  = obs.get("id", "?")
        if span is not None and span < threshold:
            issues.append(
                f"[Observable insufficiency — not scope falsification] "
                f"{oid}: span={span:.4f} < 2·ε={threshold:.4f}. "
                f"Observable cannot resolve more than one regime at ε_working. "
                f"Action: demote {oid} to non-primary and promote a wider-span observable."
            )

    # If partition results available, cross-check primary observable span
    if partition is not None:
        ranges = partition.get("regime_observable_ranges", {})
        if ranges:
            all_mins = [v["min"] for v in ranges.values() if "min" in v]
            all_maxs = [v["max"] for v in ranges.values() if "max" in v]
            if all_mins and all_maxs:
                observed_span = max(all_maxs) - min(all_mins)
                if observed_span < threshold:
                    obs_name = partition.get("annotated_results", [{}])[0].get(
                        "observable_name", "primary observable")
                    issues.append(
                        f"[Observable insufficiency — not scope falsification] "
                        f"Primary observable '{obs_name}' has observed span={observed_span:.4f} "
                        f"< 2·ε={threshold:.4f} in partition results. "
                        f"Demote and replace; do not reject scope."
                    )

    return issues


# ── Check 3: ε robustness ────────────────────────────────────────────────────

def check_epsilon_robustness(scope: dict, eps_sweep: dict | None) -> list:
    """
    Check whether ε is tied to Δ and whether a stability window exists.

    Also checks EpsilonSweep results if available: is the working ε
    inside an admissible plateau?
    """
    issues = []
    eps_block = scope.get("epsilon", {})

    if not eps_block.get("tie_to_perturbations"):
        issues.append(
            "ε not tied to Δ: epsilon.tie_to_perturbations is empty. "
            "Risk: partition may be ε-artifact. "
            "Verify sup_{δ∈Δ} E[d_Pi(δ(x), x)] << ε_working for bulk states."
        )

    window   = eps_block.get("stability_window_plan", {})
    vary_eps = window.get("vary_epsilon", [])
    if len(vary_eps) < 3:
        issues.append(
            "stability_window_plan has fewer than 3 ε values. "
            "A minimum 3-level sweep is needed to confirm plateau existence."
        )

    if eps_sweep is not None:
        working_eps = eps_sweep.get("working_epsilon")
        admissible  = eps_sweep.get("admissible_interval")
        if admissible is None:
            issues.append(
                f"Working ε={working_eps} lies on or near a critical ε-boundary "
                f"(no containing plateau found in EpsilonSweep). "
                f"Partition at this ε is structurally fragile. "
                f"Move ε into an admissible plateau interior."
            )
        else:
            w = admissible.get("width_log", 0)
            N = admissible.get("regime_count", 0)
            if w < 0.3:
                issues.append(
                    f"Admissible plateau containing working ε is narrow (w={w:.3f} < 0.3). "
                    f"Partition is marginally robust. Consider moving to a wider plateau."
                )
            if N == 1:
                issues.append(
                    f"Working ε falls in a N=1 plateau: all sweep points are in one regime. "
                    f"ε is too large to resolve any structure. Reduce ε_working."
                )

    return issues


# ── Check 4: Partition integrity ─────────────────────────────────────────────

def check_partition_match(scope: dict, invariants: dict | None) -> list:
    """
    Check whether the observed partition matches the predicted one.

    A mismatch is a finding, not necessarily a falsification trigger.
    It prompts investigation of which BC component drives the discrepancy.
    """
    issues = []
    if invariants is None:
        issues.append("Invariants.json not found — partition not yet extracted.")
        return issues

    predicted_count = scope.get("expected_partition", {}).get("regime_count_predicted")
    observed_count  = invariants.get("regime_count")
    predicted_type  = scope.get("expected_partition", {}).get("partition_type")

    if predicted_count and observed_count and predicted_count != observed_count:
        issues.append(
            f"Regime count mismatch: predicted={predicted_count}, observed={observed_count}. "
            f"Investigate: does the BC produce the expected partition type '{predicted_type}'? "
            f"Check which BC component drives the discrepancy before concluding scope failure."
        )
    elif not predicted_count:
        issues.append(
            "expected_partition.regime_count_predicted not set — no baseline for comparison."
        )

    persistence = invariants.get("persistence")
    if persistence is not None and persistence < 0.6:
        issues.append(
            f"Low persistence score ({persistence:.2f}): regime assignments are unstable "
            f"across the sweep. Check whether sweep density is sufficient near θ* before "
            f"concluding partition failure."
        )

    return issues


# ── Check 5: Falsification integrity ─────────────────────────────────────────

def check_falsification(scope: dict, bcm: dict,
                        partition: dict | None,
                        invariants: dict | None,
                        eps_sweep: dict | None) -> list:
    """
    Evaluate the BC-level falsification conditions defined in ScopeSpec.

    CRITICAL DISTINCTION:
        - Observable insufficiency (small span, single plateau) → check_observable_sufficiency
        - BC structurelessness → here (F1, F3)
        - Partition not BC-reproducible → here (F2), requires repeated runs
        - θ* not resolvable → here (F4), triggers sweep refinement

    A scope is falsified only by F1, F2, or F3.
    F4 triggers a methodological action (sweep extension), not rejection.
    """
    issues = []
    scope_falss = scope.get("falsification", [])
    bcm_falss   = []
    for bc in bcm.get("bc_components", []):
        bcm_falss += bc.get("falsification_criteria", [])

    # Structural check: are falsification conditions defined at all?
    if len(scope_falss) == 0 and len(bcm_falss) == 0:
        issues.append(
            "No falsification conditions defined. "
            "The scope cannot be refuted — not a valid ART instantiation. "
            "Add at minimum F1 (BC wirkungslos) and F2 (Partition nicht reproduzierbar)."
        )
        return issues

    # Check that each condition has a measurable_test field
    for f in scope_falss + bcm_falss:
        if isinstance(f, dict):
            fid = f.get("id", f.get("condition", "unnamed"))
            if not f.get("measurable_test"):
                issues.append(
                    f"Falsification condition '{fid}' has no measurable_test. "
                    f"Without a concrete test the condition cannot be evaluated."
                )

    # Evaluate F1 if partition is available:
    # BC wirkungslos iff span of ALL observables < ε_working
    if partition is not None:
        eps_working = scope.get("epsilon", {}).get("value", 0.05)
        ranges      = partition.get("regime_observable_ranges", {})
        if ranges:
            all_vals  = [(v["min"], v["max"]) for v in ranges.values()
                         if "min" in v and "max" in v]
            if all_vals:
                span = max(mx for _, mx in all_vals) - min(mn for mn, _ in all_vals)
                if span < eps_working:
                    issues.append(
                        f"⚠ F1 TRIGGERED — BC wirkungslos: "
                        f"Observable span={span:.4f} < ε_working={eps_working}. "
                        f"The BC produces no measurable effect on any observable. "
                        f"Scope is inadmissible."
                    )

    # Evaluate F3 if ε-sweep is available:
    # No robust plateau for any observable
    if eps_sweep is not None:
        plateaus = eps_sweep.get("plateaus", [])
        robust   = [p for p in plateaus
                    if p.get("regime_count", 0) >= 2 and p.get("width_log", 0) >= 0.3]
        if not robust:
            # Only raise as falsification if this was the ONLY observable swept
            # (multi-observable case requires checking all π_i separately)
            issues.append(
                f"⚠ F3 candidate — No ε-plateau with N≥2 and w≥0.3 found for this observable. "
                f"If this holds for ALL observables in Π, F3 is triggered and the scope is "
                f"inadmissible. If other observables have robust plateaus, this is observable "
                f"insufficiency only — demote this observable and keep the scope."
            )

    # Evaluate F4 if invariants available:
    # θ* at boundary of sweep range
    if invariants is not None:
        theta_star = invariants.get("theta_star")
        # Get sweep range from BCManifest
        bc_components = bcm.get("bc_components", [])
        sweep_values  = []
        if bc_components:
            sweeps = bc_components[0].get("perturbation_program", {}).get("sweeps", [])
            if sweeps:
                sweep_values = sweeps[0].get("values", [])
        if theta_star is None and invariants.get("regime_count", 0) >= 2:
            issues.append(
                "F4: θ* not detected despite N≥2 regimes. "
                "Transition boundary may lie outside the sweep range. "
                "Action: extend sweep range and re-run."
            )
        elif theta_star is not None and sweep_values:
            sweep_min, sweep_max = min(sweep_values), max(sweep_values)
            margin = (sweep_max - sweep_min) * 0.05
            if theta_star < sweep_min + margin or theta_star > sweep_max - margin:
                issues.append(
                    f"F4: θ*={theta_star:.3f} is at the boundary of the sweep range "
                    f"[{sweep_min}, {sweep_max}]. "
                    f"The transition is not bracketed. Extend sweep range."
                )

    return issues


# ── Check 6: Transfer integrity ──────────────────────────────────────────────

def check_transfer(transfer_metrics: dict | None, bcm: dict) -> list:
    issues = []
    if transfer_metrics is None:
        targets = bcm.get("transfer_targets", [])
        if targets:
            issues.append(
                "Transfer targets defined in BCManifest but TransferMetrics.json not found. "
                "Run pipeline.transfer before auditing transfer results."
            )
        return issues

    phi = transfer_metrics.get("metrics", {}).get("Phi", {}).get("value")
    if phi is not None and phi < 0.6:
        issues.append(
            f"Φ = {phi} < 0.6: transfer is inadmissible. "
            "Identify which BC component drives the distortion (check RCD, SDI)."
        )

    pci = transfer_metrics.get("metrics", {}).get("PCI", {}).get("value")
    if pci is not None and pci < 0.5:
        issues.append(
            f"PCI = {pci} < 0.5: more than half of equivalence classes straddle "
            "partition boundaries — core compatibility assumption fails."
        )

    return issues


# ── Collect declared failure modes ───────────────────────────────────────────

def collect_failure_modes(bcm: dict) -> list:
    modes = []
    for bc in bcm.get("bc_components", []):
        for s in bc.get("failure_signatures", []):
            if s:
                modes.append(f"[bc={bc.get('id', '?')}] {s}")
    return modes


# ── Report writer ─────────────────────────────────────────────────────────────

def write_audit(out_path: Path, case_id: str, phase: str,
                issues: dict, failure_modes: list):
    today = date.today().isoformat()
    lines = [
        f"# Failure Audit: {case_id}",
        f"",
        f"**Phase:** {phase}  ",
        f"**Date:** {today}  ",
        f"**Auditor:** pipeline.audit_helpers (A5)",
        f"",
        f"---",
        f"",
        f"## Design note",
        f"",
        f"Observable insufficiency (small span, single-observable plateau collapse) is",
        f"reported under *Observable Sufficiency* and triggers observable replacement —",
        f"not scope rejection. Scope falsification (F1–F3) requires BC-level evidence.",
        f"",
        f"---",
        f"",
    ]

    sections = [
        ("Scope Leakage",          issues.get("scope_leakage", [])),
        ("Observable Sufficiency", issues.get("observable_sufficiency", [])),
        ("ε Robustness",           issues.get("epsilon_robustness", [])),
        ("Partition Match",        issues.get("partition_match", [])),
        ("Falsification (BC-level)", issues.get("falsification", [])),
        ("Transfer Integrity",     issues.get("transfer", [])),
    ]

    total_issues = sum(len(v) for v in issues.values())

    for section, items in sections:
        lines.append(f"## {section}")
        lines.append("")
        if items:
            for item in items:
                lines.append(f"- ⚠ {item}")
        else:
            lines.append("- ✓ No issues.")
        lines.append("")

    lines += [
        "## Declared Failure Modes (from BCManifest)",
        "",
    ]
    if failure_modes:
        for m in failure_modes:
            lines.append(f"- {m}")
    else:
        lines.append("- None declared.")

    lines += [
        "",
        "---",
        "",
        f"## Summary",
        "",
        f"Total issues: **{total_issues}**",
        "",
        ("✓ Case is audit-clean for this phase." if total_issues == 0
         else "⚠ Address issues before advancing to next phase."),
        "",
        "*Generated by pipeline.audit_helpers*",
    ]

    out_path.write_text("\n".join(lines))


# ── Main ─────────────────────────────────────────────────────────────────────

def run_audit(case_dir: Path, phase: str, out_subdir: str):
    scope_path     = case_dir / "ScopeSpec.yaml"
    bcm_path       = case_dir / "BCManifest.yaml"
    inv_path       = case_dir / "results" / "partition" / "Invariants.json"
    partition_path = case_dir / "results" / "partition" / "PartitionResult.json"
    eps_sweep_path = case_dir / "results" / "partition" / "EpsilonSweep.json"
    transfer_path  = case_dir / "transfer" / "TransferMetrics.json"
    record_path    = case_dir / "CaseRecord.yaml"

    scope     = yaml.safe_load(scope_path.read_text())    if scope_path.exists()     else {}
    bcm       = yaml.safe_load(bcm_path.read_text())      if bcm_path.exists()       else {}
    record    = yaml.safe_load(record_path.read_text())   if record_path.exists()    else {}
    inv       = json.loads(inv_path.read_text())          if inv_path.exists()       else None
    partition = json.loads(partition_path.read_text())    if partition_path.exists() else None
    eps_sweep = json.loads(eps_sweep_path.read_text())    if eps_sweep_path.exists() else None
    transfer  = json.loads(transfer_path.read_text())     if transfer_path.exists()  else None

    case_id = record.get("id", case_dir.name)
    print(f"\nAudit: {case_id}  |  phase={phase}")
    print("─" * 50)

    issues = {
        "scope_leakage":          check_scope_leakage(scope),
        "observable_sufficiency": check_observable_sufficiency(scope, partition),
        "epsilon_robustness":     check_epsilon_robustness(scope, eps_sweep),
        "partition_match":        check_partition_match(scope, inv),
        "falsification":          check_falsification(scope, bcm, partition, inv, eps_sweep),
        "transfer":               check_transfer(transfer, bcm),
    }
    failure_modes = collect_failure_modes(bcm)

    section_labels = {
        "scope_leakage":          "Scope Leakage",
        "observable_sufficiency": "Observable Sufficiency",
        "epsilon_robustness":     "ε Robustness",
        "partition_match":        "Partition Match",
        "falsification":          "Falsification (BC-level)",
        "transfer":               "Transfer Integrity",
    }

    total = sum(len(v) for v in issues.values())
    for key, items in issues.items():
        status = "✓" if not items else f"⚠ {len(items)}"
        print(f"  {status:6s}  {section_labels[key]}")

    print(f"\n  Total issues: {total}")

    out_dir  = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"FailureAudit_Phase{phase}.md"
    write_audit(out_path, case_id, phase, issues, failure_modes)
    print(f"  Report: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Run failure audit on a case.")
    parser.add_argument("--case",  required=True)
    parser.add_argument("--phase", default="0")
    parser.add_argument("--out",   default="audits")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    run_audit(case_dir, args.phase, args.out)


if __name__ == "__main__":
    main()
