"""
pipeline/validate.py — Schema Validator

Checks that ScopeSpec.yaml and BCManifest.yaml are sufficiently complete
before simulation begins. Does not run any simulation — pure structural check.

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

# Fields that must be non-empty for a case to be considered ready for simulation
SCOPE_REQUIRED = [
    ("X.name",),
    ("X.type",),
    ("X.state_coordinates",),          # must be non-empty list
    ("B.description",),
    ("B.constraints",),                 # must be non-empty list
    ("B.admissible_set.membership_test",),
    ("B.boundary_condition_classes",),  # must be non-empty list
    ("Pi",),                            # must be non-empty list
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


def get_nested(d, path):
    """Navigate a nested dict/list by dot-path, handling integer indices."""
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
    errors = []
    warnings = []
    for path_tuple in required_paths:
        path = path_tuple[0]
        val = get_nested(doc, path)
        if is_empty(val):
            errors.append(f"  MISSING: {label}.{path}")
    return errors, warnings


def validate_scope_spec(path: Path):
    errors, warnings = [], []
    doc = yaml.safe_load(path.read_text())

    errs, warns = check_required(doc, SCOPE_REQUIRED, "ScopeSpec")
    errors += errs
    warnings += warns

    # Check BC classes are valid
    bc_classes = get_nested(doc, "B.boundary_condition_classes") or []
    for i, bc in enumerate(bc_classes):
        cls = bc.get("class", "") if isinstance(bc, dict) else ""
        if cls and cls not in BC_VALID_CLASSES:
            errors.append(f"  INVALID BC class at B.boundary_condition_classes[{i}]: '{cls}'")

    # Check partition type is valid
    pt = get_nested(doc, "expected_partition.partition_type")
    if pt and pt not in PARTITION_TYPES and not is_empty(pt):
        errors.append(f"  INVALID partition_type: '{pt}' (valid: {sorted(PARTITION_TYPES)})")

    # Warn if epsilon not tied to perturbations
    tie = get_nested(doc, "epsilon.tie_to_perturbations")
    if is_empty(tie):
        warnings.append("  WARN: epsilon.tie_to_perturbations not set (recommended)")

    # Warn if no falsification conditions
    falss = get_nested(doc, "falsification") or []
    if len(falss) == 0:
        warnings.append("  WARN: no falsification conditions defined")

    return errors, warnings


def validate_bc_manifest(path: Path):
    errors, warnings = [], []
    doc = yaml.safe_load(path.read_text())

    errs, warns = check_required(doc, BCM_REQUIRED, "BCManifest")
    errors += errs
    warnings += warns

    # Check BC classes
    bcs = get_nested(doc, "bc_components") or []
    for i, bc in enumerate(bcs):
        cls = bc.get("class", "") if isinstance(bc, dict) else ""
        if cls and cls not in BC_VALID_CLASSES:
            errors.append(f"  INVALID BC class at bc_components[{i}]: '{cls}'")

        # Warn if sweep values empty
        sweeps = get_nested(bc, "perturbation_program.sweeps") if isinstance(bc, dict) else []
        if not sweeps or len(sweeps) == 0:
            warnings.append(f"  WARN: bc_components[{i}] has no sweep values")

    # Check transfer targets have distortion metrics planned
    targets = get_nested(doc, "transfer_targets") or []
    for i, t in enumerate(targets):
        if isinstance(t, dict):
            metrics = t.get("distortion_metrics_planned") or []
            if len(metrics) == 0:
                warnings.append(f"  WARN: transfer_targets[{i}] has no distortion_metrics_planned")

    return errors, warnings


def validate_case(case_dir: Path, strict: bool = False):
    print(f"\nValidating: {case_dir.name}")
    print("─" * 50)

    all_errors = []
    all_warnings = []

    scope_path = case_dir / "ScopeSpec.yaml"
    bcm_path   = case_dir / "BCManifest.yaml"

    for label, path, validator in [
        ("ScopeSpec",    scope_path, validate_scope_spec),
        ("BCManifest",   bcm_path,   validate_bc_manifest),
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

    if not all_errors:
        print(f"\n  ✓  Validation passed ({len(all_warnings)} warning(s))")
        return True
    else:
        if strict:
            print("\n  STRICT MODE: treating warnings as errors")
            return False
        return False


def main():
    parser = argparse.ArgumentParser(description="Validate ARW/ART case artifacts.")
    parser.add_argument("--case",   required=True, help="Path to case directory")
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
