#!/usr/bin/env python3
"""
audit.py — ARW Repository Structural Audit (L2)
Schema-aware version: supports both v0.2 (legacy) and v0.3+ (new) formats.

Usage:
    python pipeline/audit.py [--repo-root PATH] [--output PATH] [--strict]

Exit codes:  0 = all pass | 1 = errors found | 2 = strict mode + violations
"""

import os, sys, json, re
from pathlib import Path
from datetime import date
from dataclasses import dataclass, field
from typing import Optional

try:
    import yaml
except ImportError:
    print("pyyaml required: pip install pyyaml")
    sys.exit(2)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

VALID_STATUS = {
    "definition", "working-definition", "claim", "hypothesis",
    "interpretation", "experiment-proposal", "open-question", "note"
}

# Legacy v0.2 status values — warn but don't error
LEGACY_STATUS = {"draft", "active", "redirect", "reference",
                 "conceptual-outlook", "concept"}

VALID_GO_NOGO = {"go", "pending", "no_go"}
VALID_ADMISSIBILITY = {"highly_admissible", "partially_admissible", "inadmissible"}
VALID_CASE_STATUS = {"open", "in_progress", "complete", "failed", "archived"}
VALID_SEVERITY = {"scope_rejection", "sweep_refinement"}

SCHEMA_DIRS = {"schemas"}   # skip schema template files for YAML checks

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Violation:
    file: str
    rule_id: str
    message: str
    severity: str = "error"

@dataclass
class AuditReport:
    repo_root: str
    run_date: str
    violations: list = field(default_factory=list)
    checked_files: int = 0

    def add(self, file, rule_id, message, severity="error"):
        self.violations.append(Violation(file, rule_id, message, severity))

    @property
    def errors(self): return [v for v in self.violations if v.severity == "error"]
    @property
    def warnings(self): return [v for v in self.violations if v.severity == "warning"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_yaml(path):
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except Exception:
        return None

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None

def extract_frontmatter(path):
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None
        end = text.index("---", 3)
        return yaml.safe_load(text[3:end])
    except Exception:
        return None

GERMAN = [r"\bund\b",r"\boder\b",r"\bfür\b",r"\bist\b",r"\bsind\b",
          r"\bhat\b",r"\bwird\b",r"\bkann\b",r"ß",r"\bÄ\b",r"\bÖ\b",r"\bÜ\b"]

def has_german(text):
    return any(re.search(p, text) for p in GERMAN)

def rel(path, root):
    return str(path.relative_to(root))

def is_schema_file(rpath):
    return rpath.startswith("schemas/")

# ---------------------------------------------------------------------------
# BCManifest — supports v0.2 (bc_components) and v0.3+ (bc_class.primary)
# ---------------------------------------------------------------------------

def check_bcmanifest(path, root, report):
    rpath = rel(path, root)
    if is_schema_file(rpath): return
    report.checked_files += 1
    before = len(report.violations)

    data = load_yaml(path)
    if data is None:
        report.add(rpath, "BM-00", "Could not parse YAML"); return

    version = str(data.get("schema_version", "0.3"))

    if version.startswith("0.2"):
        # Legacy v0.2: uses bc_components list
        if not data.get("bc_components"):
            report.add(rpath, "BM-01", "v0.2: Missing bc_components list")
        # sweep info is nested inside bc_components[].parameterization
        bc = (data.get("bc_components") or [{}])[0]
        if not bc.get("parameterization"):
            report.add(rpath, "BM-04",
                "v0.2: No parameterization in bc_components[0]", severity="warning")
    else:
        # v0.3+: uses bc_class.primary
        bc = data.get("bc_class", {})
        if not bc.get("primary"):
            report.add(rpath, "BM-01", "Missing bc_class.primary")
        if not bc.get("justification"):
            report.add(rpath, "BM-02", "Missing bc_class.justification", severity="warning")
        sig = data.get("operator_signature", {})
        if not sig.get("primary"):
            report.add(rpath, "BM-03", "Missing operator_signature.primary")
        sweep = data.get("sweep_program", {})
        if not sweep:
            report.add(rpath, "BM-04", "Missing sweep_program")
        else:
            for f in ["range", "n_points"]:
                if f not in sweep:
                    report.add(rpath, "BM-04", f"Missing sweep_program.{f}")
        if not data.get("expected_regimes"):
            report.add(rpath, "BM-05", "Missing expected_regimes")

    if len(report.violations) == before:
        pass  # clean


# ---------------------------------------------------------------------------
# CaseRecord — supports v0.2 (status field) and v0.3+ (go_nogo.verdict)
# ---------------------------------------------------------------------------

def check_caserecord(path, root, report):
    rpath = rel(path, root)
    if is_schema_file(rpath): return
    report.checked_files += 1
    before = len(report.violations)

    data = load_yaml(path)
    if data is None:
        report.add(rpath, "CR-00", "Could not parse YAML"); return

    version = str(data.get("schema_version", "0.3"))

    if version.startswith("0.2"):
        # v0.2: uses top-level status
        status = data.get("status")
        if status and status not in VALID_CASE_STATUS:
            report.add(rpath, "CR-03",
                f"v0.2: status '{status}' not in {VALID_CASE_STATUS}", severity="warning")
        # go_nogo may exist nested
        gn = data.get("go_nogo", {})
        if gn and not gn.get("verdict"):
            report.add(rpath, "CR-01", "v0.2: go_nogo block present but verdict missing",
                severity="warning")
    else:
        gn = data.get("go_nogo", {})
        verdict = gn.get("verdict")
        if not verdict:
            report.add(rpath, "CR-01", "Missing go_nogo.verdict")
        elif verdict not in VALID_GO_NOGO:
            report.add(rpath, "CR-01", f"Invalid go_nogo.verdict '{verdict}'")
        else:
            if verdict == "go" and not gn.get("date"):
                report.add(rpath, "CR-01", "go_nogo=go but date missing")
            if verdict == "no_go" and not gn.get("reason"):
                report.add(rpath, "CR-01", "go_nogo=no_go but reason missing")

        if "artifact_registry" not in data:
            report.add(rpath, "CR-02", "Missing artifact_registry", severity="warning")
        if "related_cases" not in data:
            report.add(rpath, "CR-04", "Missing related_cases", severity="warning")


# ---------------------------------------------------------------------------
# ScopeSpec
# ---------------------------------------------------------------------------

def check_scopespec(path, root, report):
    rpath = rel(path, root)
    if is_schema_file(rpath): return
    report.checked_files += 1
    before = len(report.violations)

    data = load_yaml(path)
    if data is None:
        report.add(rpath, "SS-00", "Could not parse YAML"); return

    version = str(data.get("schema_version", "0.3"))

    # Pi block — works for both v0.2 and v0.3+
    pi = (data.get("scope_tuple") or {}).get("Pi") or data.get("Pi") or data.get("observables")
    if not pi:
        report.add(rpath, "SS-01", "Missing Pi / observables block")
    else:
        primaries = [o for o in pi
                     if o.get("primary") is True or o.get("role") == "primary"]
        if len(primaries) == 0:
            report.add(rpath, "SS-02", "No observable marked primary")
        elif len(primaries) > 1:
            report.add(rpath, "SS-02", f"{len(primaries)} observables marked primary")

        for i, obs in enumerate(pi):
            key = obs.get("observable_key") or obs.get("key") or obs.get("name")
            if not key:
                report.add(rpath, "SS-03", f"Observable at index {i} missing key field")
            if "observable_sufficiency" not in obs and "sufficiency" not in obs:
                k = key or f"index_{i}"
                report.add(rpath, "SS-04",
                    f"Observable '{k}' missing observable_sufficiency", severity="warning")

    # Epsilon block
    eps = (data.get("scope_tuple") or {}).get("epsilon") or data.get("epsilon")
    if not eps:
        report.add(rpath, "SS-06", "Missing epsilon block")
    else:
        has_val = ("working_epsilon" in eps or "value" in eps or
                   "vary_epsilon" in eps or "tie_to_perturbations" in eps)
        if not has_val:
            report.add(rpath, "SS-06", "Missing epsilon value/working_epsilon")

    # Falsification block
    false_block = data.get("falsification") or data.get("failure_modes")
    if not false_block:
        report.add(rpath, "SS-07", "Missing falsification/failure_modes block",
            severity="warning")
    else:
        for i, entry in enumerate(false_block):
            if "id" not in entry:
                report.add(rpath, "SS-07",
                    f"Falsification entry {i} missing 'id'", severity="warning")
            if "severity" in entry and entry["severity"] not in VALID_SEVERITY:
                report.add(rpath, "SS-07",
                    f"Entry {i} invalid severity '{entry['severity']}'", severity="warning")


# ---------------------------------------------------------------------------
# Invariants.json
# ---------------------------------------------------------------------------

def check_invariants(path, root, report):
    rpath = rel(path, root)
    report.checked_files += 1
    before = len(report.violations)

    data = load_json(path)
    if data is None:
        report.add(rpath, "INV-00", "Could not parse JSON"); return

    if "sweep_range" not in data:
        report.add(rpath, "INV-01",
            "Missing sweep_range — required for TBS_norm")

    for f in ["theta_star", "regime_count"]:
        k = f if f in data else ("N_regimes" if "N_regimes" in data else None)
        if f not in data and "N_regimes" not in data and f == "regime_count":
            report.add(rpath, "INV-02",
                f"Missing regime_count / N_regimes", severity="warning")
            break
        if f not in data and f != "regime_count":
            report.add(rpath, "INV-02", f"Missing '{f}'", severity="warning")


# ---------------------------------------------------------------------------
# TransferMetrics.json — supports v0.2 (nested metrics{}) and v0.3+ (flat)
# ---------------------------------------------------------------------------

def check_transfermetrics(path, root, report):
    rpath = rel(path, root)
    report.checked_files += 1
    before = len(report.violations)

    data = load_json(path)
    if data is None:
        report.add(rpath, "TM-00", "Could not parse JSON"); return

    # v0.2: fields are nested under "metrics"
    metrics = data.get("metrics", data)

    rcd = metrics.get("RCD") or metrics.get("rcd")
    tbs = metrics.get("TBS_norm") or metrics.get("TBS") or metrics.get("tbs_norm")
    phi = metrics.get("Phi") or metrics.get("admissibility_verdict") or metrics.get("phi")

    if rcd is None:
        report.add(rpath, "TM-01", "Missing RCD / rcd")
    if tbs is None:
        report.add(rpath, "TM-01", "Missing TBS_norm / TBS")

    # v0.2 uses "Phi" dict with "value"; v0.3 uses admissibility_verdict string
    if phi is None:
        report.add(rpath, "TM-01", "Missing Phi / admissibility_verdict")
    elif isinstance(phi, str) and phi not in VALID_ADMISSIBILITY:
        report.add(rpath, "TM-02",
            f"Invalid admissibility_verdict '{phi}'", severity="warning")

    # Check TBS_norm vs raw TBS
    if tbs is not None:
        tbs_val = tbs.get("value") if isinstance(tbs, dict) else tbs
        tbs_norm = metrics.get("TBS_norm")
        if tbs_norm is None and isinstance(tbs, dict) and "norm" not in str(tbs):
            report.add(rpath, "TM-03",
                "TBS present but TBS_norm not explicitly named — verify normalization",
                severity="warning")

    # ε-mismatch check
    n_a = (metrics.get("RCD") or {}).get("N_A") if isinstance(metrics.get("RCD"), dict) else None
    n_b = (metrics.get("RCD") or {}).get("N_B") if isinstance(metrics.get("RCD"), dict) else None
    if n_a and n_b and n_a != n_b:
        has_matched = "phi_matched_epsilon" in metrics or "phi_matched" in metrics
        if not has_matched:
            report.add(rpath, "TM-04",
                f"N_A≠N_B (ε-mismatch): phi_matched_epsilon missing", severity="warning")


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def check_markdown(path, root, report):
    rpath = rel(path, root)
    report.checked_files += 1

    fm = extract_frontmatter(path)
    if fm is None:
        # README files without front-matter are acceptable
        if path.name == "README.md":
            return
        report.add(rpath, "MD-01", "Missing YAML front-matter")
        return

    status = fm.get("status")
    if not status:
        report.add(rpath, "MD-02", "Missing 'status:' in front-matter")
    elif status in LEGACY_STATUS:
        report.add(rpath, "MD-02",
            f"Legacy status '{status}' — migrate to: {sorted(VALID_STATUS)}",
            severity="warning")
    elif status not in VALID_STATUS:
        report.add(rpath, "MD-02",
            f"Invalid status '{status}'. Valid: {sorted(VALID_STATUS)}")

    if not fm.get("layer"):
        report.add(rpath, "MD-03", "Missing 'layer:' in front-matter", severity="warning")

    try:
        text = path.read_text(encoding="utf-8")
        if text.startswith("---"):
            try: text = text[text.index("---", 3)+3:]
            except ValueError: pass
        if has_german(text[:3000]):
            report.add(rpath, "MD-04",
                "German text detected — repo language is English", severity="warning")
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Report writer
# ---------------------------------------------------------------------------

def write_report(report, output_path):
    lines = [
        "---", "status: note", "layer: docs/meta/",
        f"generated: {report.run_date}", "---", "",
        f"# ARW Audit Report — {report.run_date}", "",
        f"**Files checked:** {report.checked_files}  ",
        f"**Errors:** {len(report.errors)}  ",
        f"**Warnings:** {len(report.warnings)}  ", "",
    ]

    if not report.violations:
        lines.append("✅ All checks passed.")
    else:
        # Group by file
        by_file = {}
        for v in report.violations:
            by_file.setdefault(v.file, []).append(v)

        if report.errors:
            lines += ["## Errors", ""]
            for f, vs in sorted(by_file.items()):
                errs = [v for v in vs if v.severity == "error"]
                if errs:
                    lines.append(f"### `{f}`")
                    for v in errs:
                        lines.append(f"- **[{v.rule_id}]** {v.message}")
                    lines.append("")

        if report.warnings:
            lines += ["## Warnings", ""]
            for f, vs in sorted(by_file.items()):
                warns = [v for v in vs if v.severity == "warning"]
                if warns:
                    lines.append(f"### `{f}`")
                    for v in warns:
                        lines.append(f"- [{v.rule_id}] {v.message}")
                    lines.append("")

    # Summary by rule
    rule_counts = {}
    for v in report.violations:
        rule_counts[v.rule_id] = rule_counts.get(v.rule_id, 0) + 1
    if rule_counts:
        lines += ["## Violations by Rule", "", "| Rule | Count | Type |", "|---|---|---|"]
        for rule, count in sorted(rule_counts.items()):
            vtype = "Error" if any(v.rule_id == rule and v.severity == "error"
                                   for v in report.violations) else "Warning"
            lines.append(f"| {rule} | {count} | {vtype} |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to: {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def check_readme_staleness(directory: Path, root: Path, report: AuditReport):
    """
    Check whether a directory's README.md mentions all .md and .yaml files
    in that directory. Files not mentioned in README = stale README.
    """
    readme = directory / "README.md"
    if not readme.exists():
        rpath = rel(directory, root) + "/README.md"
        report.add(rpath, "RM-01", "Missing README.md in directory", severity="warning")
        return

    report.checked_files += 1
    readme_text = readme.read_text(encoding="utf-8").lower()

    # Collect all non-README content files in the directory (non-recursive)
    content_files = [
        f for f in directory.iterdir()
        if f.is_file()
        and f.name != "README.md"
        and f.suffix in {".md", ".yaml", ".json", ".mmd"}
        and not f.name.startswith(".")
        and not f.name.startswith("audit_report")  # auto-generated
    ]

    missing = []
    for f in sorted(content_files):
        # Check if filename (without extension or with) appears in README
        stem = f.stem.lower()
        name = f.name.lower()
        if stem not in readme_text and name not in readme_text:
            missing.append(f.name)

    if missing:
        rpath = rel(readme, root)
        report.add(rpath, "RM-02",
            f"README does not mention {len(missing)} file(s): "
            f"{', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}",
            severity="warning")


def run_audit(repo_root, strict=False):
    report = AuditReport(repo_root=str(repo_root), run_date=date.today().isoformat())

    for path in sorted(repo_root.rglob("*")):
        if not path.is_file(): continue
        parts = path.parts
        if any(p.startswith(".") or p in {"node_modules","__pycache__"} for p in parts):
            continue

        name = path.name
        rpath = rel(path, repo_root)

        if name == "ScopeSpec.yaml":
            check_scopespec(path, repo_root, report)
        elif name == "BCManifest.yaml":
            check_bcmanifest(path, repo_root, report)
        elif name == "CaseRecord.yaml":
            check_caserecord(path, repo_root, report)
        elif name == "Invariants.json":
            check_invariants(path, repo_root, report)
        elif name == "TransferMetrics.json":
            check_transfermetrics(path, repo_root, report)
        elif path.suffix == ".md" and any(
            rpath.startswith(d) for d in ("docs/", "cases/")
        ):
            check_markdown(path, repo_root, report)

    # README staleness checks for key directories
    readme_dirs = [
        repo_root / "cases",
        repo_root / "docs" / "advanced",
        repo_root / "docs" / "art_instantiations",
        repo_root / "docs" / "bc_taxonomy",
        repo_root / "docs" / "core",
        repo_root / "docs" / "glossary",
        repo_root / "docs" / "meta",
        repo_root / "docs" / "notes",
        repo_root / "docs" / "overview",
        repo_root / "docs" / "pipelines",
        repo_root / "pipeline",
        repo_root / "figures",
    ]
    for d in readme_dirs:
        if d.exists():
            check_readme_staleness(d, repo_root, report)

    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="ARW L2 Audit")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", default=None)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    print(f"Auditing: {root}")
    report = run_audit(root, args.strict)

    if not args.quiet:
        for v in report.violations:
            pfx = "ERROR" if v.severity == "error" else "WARN "
            print(f"  [{pfx}] [{v.rule_id}] {v.file}: {v.message}")

    print(f"\nSummary: {report.checked_files} files, "
          f"{len(report.errors)} errors, {len(report.warnings)} warnings")

    out = Path(args.output) if args.output else \
          root / "docs" / "meta" / f"audit_report_{report.run_date}.md"
    write_report(report, out)

    sys.exit(2 if args.strict and report.violations else 1 if report.errors else 0)


if __name__ == "__main__":
    main()
