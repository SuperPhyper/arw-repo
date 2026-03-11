"""
pipeline/audit_helpers.py — Failure Auditor (Agent A5)

Reads all artifacts for a case and produces a FailureAudit.md that checks:
    1. Scope leakage: ARW-forbidden constructs in ScopeSpec (dynamics, norms, targets)
    2. Robustness: is ε tied to Δ? Is the stability window non-trivial?
    3. Partition integrity: does observed partition match predicted?
    4. Transfer integrity: are distortion metrics within expected bounds?
    5. Falsification: are falsification conditions defined and checkable?
    6. Open failure modes from BCManifest

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

# ARW-forbidden constructs in ScopeSpec (belong only in ART, not in formal ARW level)
# Reference: docs/core (ARW makes no empirical claims)
ARW_FORBIDDEN_KEYWORDS = [
    "lyapunov", "hamiltonian", "energy", "objective", "reward",
    "policy", "regulation_error", "desired_state", "goal", "utility",
    "optimal", "loss_function",
]


def check_scope_leakage(scope: dict) -> list:
    """Check for ARW-forbidden constructs accidentally placed in scope-level fields."""
    issues = []
    scope_str = yaml.dump(scope).lower()
    for kw in ARW_FORBIDDEN_KEYWORDS:
        if kw in scope_str:
            issues.append(f"Possible scope leakage: '{kw}' found in ScopeSpec "
                          f"(dynamics/goal constructs belong in ART simulation code, not schema)")
    return issues


def check_epsilon_robustness(scope: dict) -> list:
    issues = []
    eps = scope.get("epsilon", {})
    if not eps.get("tie_to_perturbations"):
        issues.append("ε not tied to Δ: epsilon.tie_to_perturbations is empty. "
                      "Risk: partition may be ε-artifact, not robust structure.")
    window = eps.get("stability_window_plan", {})
    vary_e = window.get("vary_epsilon", [])
    if len(vary_e) < 2:
        issues.append("Stability window plan has fewer than 2 ε values. "
                      "Cannot confirm robustness across ε without at least a 3-level sweep.")
    return issues


def check_partition_match(scope: dict, invariants: dict | None) -> list:
    issues = []
    if invariants is None:
        issues.append("Invariants.json not found — partition not yet extracted.")
        return issues

    predicted_count = scope.get("expected_partition", {}).get("regime_count_predicted")
    observed_count  = invariants.get("regime_count")
    predicted_type  = scope.get("expected_partition", {}).get("partition_type")

    if predicted_count and observed_count and predicted_count != observed_count:
        issues.append(f"Regime count mismatch: predicted={predicted_count}, observed={observed_count}. "
                      f"Possible failure mode: BC class does not produce expected partition type '{predicted_type}'.")
    elif not predicted_count:
        issues.append("expected_partition.regime_count_predicted not set — no baseline for comparison.")

    persistence = invariants.get("persistence")
    if persistence is not None and persistence < 0.6:
        issues.append(f"Low persistence score ({persistence:.2f}): partition is unstable across sweep. "
                      f"Possible failure mode F1 (no stable window).")

    return issues


def check_falsification(scope: dict, bcm: dict) -> list:
    issues = []
    scope_falss = scope.get("falsification", [])
    bcm_falss   = []
    for bc in bcm.get("bc_components", []):
        bcm_falss += bc.get("falsification_criteria", [])

    if len(scope_falss) == 0 and len(bcm_falss) == 0:
        issues.append("No falsification conditions defined in ScopeSpec or BCManifest. "
                      "Result cannot be refuted — not a valid ART instantiation.")
    for f in scope_falss + bcm_falss:
        if isinstance(f, dict):
            if not f.get("measurable_test"):
                issues.append(f"Falsification criterion '{f.get('id')}' has no measurable_test.")

    return issues


def check_transfer(transfer_metrics: dict | None, bcm: dict) -> list:
    issues = []
    if transfer_metrics is None:
        targets = bcm.get("transfer_targets", [])
        if targets:
            issues.append("Transfer targets defined in BCManifest but TransferMetrics.json not found. "
                          "Run pipeline.transfer before auditing transfer results.")
        return issues

    phi = transfer_metrics.get("metrics", {}).get("Phi", {}).get("value")
    if phi is not None and phi < 0.6:
        issues.append(f"Φ = {phi} < 0.6: transfer is inadmissible. "
                      "Identify which BC component drives the distortion (check RCD, SDI).")

    pci = transfer_metrics.get("metrics", {}).get("PCI", {}).get("value")
    if pci is not None and pci < 0.5:
        issues.append(f"PCI = {pci} < 0.5: more than half of equivalence classes straddle "
                      "partition boundaries — core compatibility assumption fails.")

    return issues


def collect_failure_modes(bcm: dict) -> list:
    """Collect all declared failure signatures from BCManifest."""
    modes = []
    for bc in bcm.get("bc_components", []):
        sigs = bc.get("failure_signatures", [])
        for s in sigs:
            if s:
                modes.append(f"[bc={bc.get('id', '?')}] {s}")
    return modes


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
    ]

    sections = [
        ("Scope Leakage",           issues.get("scope_leakage", [])),
        ("ε Robustness",            issues.get("epsilon_robustness", [])),
        ("Partition Match",         issues.get("partition_match", [])),
        ("Falsification Integrity", issues.get("falsification", [])),
        ("Transfer Integrity",      issues.get("transfer", [])),
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


def run_audit(case_dir: Path, phase: str, out_subdir: str):
    scope_path    = case_dir / "ScopeSpec.yaml"
    bcm_path      = case_dir / "BCManifest.yaml"
    inv_path      = case_dir / "results" / "partition" / "Invariants.json"
    transfer_path = case_dir / "transfer" / "TransferMetrics.json"
    record_path   = case_dir / "CaseRecord.yaml"

    scope    = yaml.safe_load(scope_path.read_text()) if scope_path.exists() else {}
    bcm      = yaml.safe_load(bcm_path.read_text())   if bcm_path.exists()   else {}
    record   = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}
    inv      = json.loads(inv_path.read_text())         if inv_path.exists()   else None
    transfer = json.loads(transfer_path.read_text())    if transfer_path.exists() else None

    case_id = record.get("id", case_dir.name)
    print(f"\nAudit: {case_id}  |  phase={phase}")
    print("─" * 50)

    issues = {
        "scope_leakage":    check_scope_leakage(scope),
        "epsilon_robustness": check_epsilon_robustness(scope),
        "partition_match":  check_partition_match(scope, inv),
        "falsification":    check_falsification(scope, bcm),
        "transfer":         check_transfer(transfer, bcm),
    }
    failure_modes = collect_failure_modes(bcm)

    total = sum(len(v) for v in issues.values())
    for section, items in issues.items():
        status = f"✓" if not items else f"⚠ {len(items)}"
        print(f"  {status:5s}  {section.replace('_',' ').title()}")

    print(f"\n  Total issues: {total}")

    out_dir = case_dir / out_subdir
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
