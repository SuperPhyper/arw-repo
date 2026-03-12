"""
pipeline/validate.py — Schema Validator

Checks that ScopeSpec.yaml and BCManifest.yaml are sufficiently complete
before simulation begins. Does not run any simulation — pure structural check.

FALSIFICATION SCHEMA REQUIREMENTS:
    Each falsification condition in ScopeSpec must have:
      - id:               unique identifier (F1, F2, ...)
      - label:            short human-readable name
      - condition:        formal statement of what triggers falsification
      - measurable_test:  concrete, computable test against pipeline outputs
      - severity:         "scope_rejection" | "sweep_refinement"

    Conditions that target observable span or plateau width alone are
    NOT valid falsification conditions — they belong in observable_sufficiency.
    validate.py warns if falsification conditions appear to conflate
    observable instrument quality with BC structural claims.

Usage:
    python -m pipeline.validate --case cases/CASE-20260311-0001
    python -m pipeline.validate --case cases/CASE-... --strict
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml --break-system-packages")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

SCOPE_REQUIRED = [
    ("X.name",),
    ("X.type",),
    ("X.state_coordinates",),
    ("B.description",),
    ("B.constraints",),
    ("B.admissible_set.membership_test",),
    ("B.boundary_condition_classes",),
    ("Pi",),
    ("Pi.0.map.definition",),
    ("Pi.0.distinguishability.d_pi",),
    ("Delta",),
    ("Delta.0.bounds.magnitude",),
    ("epsilon.value",),
    ("epsilon.interpretation",),
    ("expected_partition.partition_type",),
    ("expected_partition.regime_count_predicted",),
]

BCM_REQUIRED = [
    ("bc_components",),
    ("bc_components.0.class",),
    ("bc_components.0.parameterization",),
    ("bc_components.0.perturbation_program.sweeps",),
    ("bc_components.0.resolution_plan.epsilons",),
    ("bc_components.0.predicted_partition_effects.partition_type_prediction",),
    ("bc_components.0.falsification_criteria",),
]

BC_VALID_CLASSES = {
    "restriction", "coupling", "symmetry_breaking",
    "dissipation", "forcing", "aggregation"
}

PARTITION_TYPES = {
    "binary", "sequential", "clustered", "multi_stable", "hierarchical"
}

FALSIFICATION_SEVERITY_VALUES = {"scope_rejection", "sweep_refinement"}

# Keywords that suggest a falsification condition is actually about
# observable quality rather than BC structure
OBSERVABLE_INSTRUMENT_KEYWORDS = [
    "plateau", "span", "observable cannot", "not informative",
    "no eps-plateau", "no ε-plateau",
]


def get_nested(d, path):
    parts = path.split(".")
    cur = d
    for p in parts:
        if cur is None:
            return None
        if isinstance(cur, list):
            try:
                cur = cur[int(p)]
            except (IndexError, ValueError):
                return None
        elif isinstance(cur, dict):
            cur = cur.get(p)
        else:
            return None
    return cur


def is_empty(val):
    if val is None:
        return True
    if isinstance(val, str) and (val.strip() == "" or val.startswith("YYYY") or "####" in val):
        return True
    if isinstance(val, list) and len(val) == 0:
        return True
    return False


def check_required(doc, required_paths, label):
    errors, warnings = [], []
    for path_tuple in required_paths:
        path = path_tuple[0]
        val  = get_nested(doc, path)
        if is_empty(val):
            errors.append(f"  MISSING: {label}.{path}")
    return errors, warnings


def validate_falsification_conditions(falss: list, source: str) -> tuple[list, list]:
    """
    Validate the structure and content of falsification conditions.

    Required fields: id, condition, measurable_test, severity
    Warns if condition text suggests it is about observable quality rather
    than BC structure (conflation error).
    """
    errors, warnings = [], []

    for i, f in enumerate(falss):
        if not isinstance(f, dict):
            # Legacy string format — still valid but warn about upgrade
            warnings.append(
                f"  WARN: {source}.falsification[{i}] is a plain string, not a structured dict. "
                f"Upgrade to dict with id/condition/measurable_test/severity for full audit support."
            )
            # Check for observable-instrument conflation in string form
            f_lower = str(f).lower()
            if any(kw in f_lower for kw in OBSERVABLE_INSTRUMENT_KEYWORDS):
                warnings.append(
                    f"  WARN: {source}.falsification[{i}] appears to target observable quality "
                    f"(plateau/span), not BC structure. "
                    f"Observable insufficiency belongs in observable_sufficiency, not falsification."
                )
            continue

        fid = f.get("id", f"[{i}]")

        if not f.get("measurable_test"):
            errors.append(
                f"  MISSING: {source}.falsification[{fid}].measurable_test — "
                f"condition cannot be evaluated without a concrete test."
            )

        severity = f.get("severity")
        if severity and severity not in FALSIFICATION_SEVERITY_VALUES:
            warnings.append(
                f"  WARN: {source}.falsification[{fid}].severity='{severity}' "
                f"not in {sorted(FALSIFICATION_SEVERITY_VALUES)}"
            )

        if not f.get("severity"):
            warnings.append(
                f"  WARN: {source}.falsification[{fid}] has no severity field. "
                f"Add 'severity: scope_rejection' or 'severity: sweep_refinement'."
            )

        # Check for observable-instrument conflation
        condition_text = str(f.get("condition", "")).lower()
        interp_text    = str(f.get("interpretation", "")).lower()
        combined       = condition_text + " " + interp_text
        if any(kw in combined for kw in OBSERVABLE_INSTRUMENT_KEYWORDS):
            # Only warn if it's the sole condition — single-observable plateau
            # failure is never a scope falsification on its own
            warnings.append(
                f"  WARN: {source}.falsification[{fid}] references observable quality "
                f"(plateau/span). Ensure this is a collective condition over ALL observables "
                f"(F3 pattern), not a single-observable instrument check. "
                f"Single-observable insufficiency belongs in observable_sufficiency."
            )

    return errors, warnings


def validate_scope_spec(path: Path) -> tuple[list, list]:
    errors, warnings = [], []
    doc = yaml.safe_load(path.read_text())

    errs, warns = check_required(doc, SCOPE_REQUIRED, "ScopeSpec")
    errors   += errs
    warnings += warns

    # BC classes
    bc_classes = get_nested(doc, "B.boundary_condition_classes") or []
    for i, bc in enumerate(bc_classes):
        cls = bc.get("class", "") if isinstance(bc, dict) else ""
        if cls and cls not in BC_VALID_CLASSES:
            errors.append(
                f"  INVALID BC class at B.boundary_condition_classes[{i}]: '{cls}'"
            )

    # Partition type
    pt = get_nested(doc, "expected_partition.partition_type")
    if pt and pt not in PARTITION_TYPES and not is_empty(pt):
        errors.append(
            f"  INVALID partition_type: '{pt}' (valid: {sorted(PARTITION_TYPES)})"
        )

    # ε tie to perturbations
    tie = get_nested(doc, "epsilon.tie_to_perturbations")
    if is_empty(tie):
        warnings.append(
            "  WARN: epsilon.tie_to_perturbations not set. "
            "Verify sup_{δ∈Δ} E[d_Pi(δ(x), x)] << ε_working for bulk states."
        )

    # At least one observable marked primary
    pi_list = get_nested(doc, "Pi") or []
    primary_obs = [p for p in pi_list if isinstance(p, dict) and p.get("primary") is True]
    if len(primary_obs) == 0:
        warnings.append(
            "  WARN: No observable marked 'primary: true' in Pi. "
            "The partition extractor needs a primary observable for clustering."
        )

    # observable_sufficiency block recommended for multi-observable scopes
    if len(pi_list) > 1:
        obs_suff = get_nested(doc, "observable_sufficiency")
        if is_empty(obs_suff):
            warnings.append(
                "  WARN: Multiple observables defined but no observable_sufficiency block. "
                "Add observable_sufficiency.per_observable to document span checks "
                "and distinguish instrument limitations from scope falsification."
            )

    # Falsification conditions
    falss = get_nested(doc, "falsification") or []
    if len(falss) == 0:
        warnings.append(
            "  WARN: No falsification conditions defined. "
            "Add at minimum F1 (BC wirkungslos) and F2 (Partition nicht reproduzierbar)."
        )
    else:
        errs, warns = validate_falsification_conditions(falss, "ScopeSpec")
        errors   += errs
        warnings += warns

    return errors, warnings


def validate_bc_manifest(path: Path) -> tuple[list, list]:
    errors, warnings = [], []
    doc = yaml.safe_load(path.read_text())

    errs, warns = check_required(doc, BCM_REQUIRED, "BCManifest")
    errors   += errs
    warnings += warns

    bcs = get_nested(doc, "bc_components") or []
    for i, bc in enumerate(bcs):
        cls = bc.get("class", "") if isinstance(bc, dict) else ""
        if cls and cls not in BC_VALID_CLASSES:
            errors.append(
                f"  INVALID BC class at bc_components[{i}]: '{cls}'"
            )

        sweeps = get_nested(bc, "perturbation_program.sweeps") if isinstance(bc, dict) else []
        if not sweeps:
            warnings.append(
                f"  WARN: bc_components[{i}] has no sweep values"
            )

        # Validate BCManifest-level falsification criteria
        bcm_falss = bc.get("falsification_criteria", []) if isinstance(bc, dict) else []
        if bcm_falss:
            errs, warns = validate_falsification_conditions(
                bcm_falss, f"BCManifest.bc_components[{i}]")
            errors   += errs
            warnings += warns

    # Transfer targets
    targets = get_nested(doc, "transfer_targets") or []
    for i, t in enumerate(targets):
        if isinstance(t, dict):
            metrics = t.get("distortion_metrics_planned") or []
            if len(metrics) == 0:
                warnings.append(
                    f"  WARN: transfer_targets[{i}] has no distortion_metrics_planned"
                )

    return errors, warnings


def validate_case(case_dir: Path, strict: bool = False) -> bool:
    print(f"\nValidating: {case_dir.name}")
    print("─" * 50)

    all_errors   = []
    all_warnings = []

    scope_path = case_dir / "ScopeSpec.yaml"
    bcm_path   = case_dir / "BCManifest.yaml"

    for label, path, validator in [
        ("ScopeSpec",  scope_path, validate_scope_spec),
        ("BCManifest", bcm_path,   validate_bc_manifest),
    ]:
        if not path.exists():
            all_errors.append(f"  FILE MISSING: {path.name}")
            continue
        print(f"  Checking {label}...")
        errs, warns = validator(path)
        all_errors   += errs
        all_warnings += warns

    if all_errors:
        print(f"\n  ✗  {len(all_errors)} error(s):")
        for e in all_errors:
            print(e)
    if all_warnings:
        print(f"\n  ⚠  {len(all_warnings)} warning(s):")
        for w in all_warnings:
            print(w)

    if not all_errors and not (strict and all_warnings):
        print(f"\n  ✓  Validation passed ({len(all_warnings)} warning(s))")
        return True
    else:
        if strict and all_warnings:
            print("\n  STRICT MODE: warnings treated as errors")
        return False


def main():
    parser = argparse.ArgumentParser(description="Validate ARW/ART case artifacts.")
    parser.add_argument("--case",   required=True)
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case directory not found: {case_dir}")
        sys.exit(1)

    ok = validate_case(case_dir, strict=args.strict)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
