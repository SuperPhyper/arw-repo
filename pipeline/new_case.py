"""
pipeline/new_case.py — Case Initializer

Creates a new case directory from schema templates.

Usage:
    python -m pipeline.new_case --id CASE-20260311-0001 --system kuramoto --phase 1
    python -m pipeline.new_case --id CASE-20260311-0002 --system pendulum  --phase 1
    python -m pipeline.new_case --list-systems
"""

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCHEMAS   = REPO_ROOT / "schemas"
CASES     = REPO_ROOT / "cases"

# Map system names to their experiment docs and default phase
SYSTEM_REGISTRY = {
    "kuramoto": {
        "experiment_doc": "experiments/kuramoto_oscillators.md",
        "default_phase": "1",
        "description": "Kuramoto oscillator synchronization — Phase 1 calibration system",
        "bc_classes": ["coupling"],
        "partition_type_prediction": "sequential",
    },
    "pendulum": {
        "experiment_doc": "experiments/multi_link_pendulum.md",
        "default_phase": "1",
        "description": "Multi-link pendulum — scope reduction admissibility testing",
        "bc_classes": ["coupling", "dissipation"],
        "partition_type_prediction": "clustered",
    },
    "double_pendulum": {
        "experiment_doc": "experiments/multi_link_pendulum.md",
        "default_phase": "1",
        "description": "Classical double pendulum — multi-BC-class regime analysis",
        "bc_classes": ["restriction", "coupling", "dissipation", "forcing"],
        "partition_type_prediction": "sequential",
    },
    "consensus": {
        "experiment_doc": "experiments/agent_consensus_models.md",
        "default_phase": "2a",
        "description": "Opinion dynamics agent-based model — BC-induced regime generation",
        "bc_classes": ["coupling", "restriction"],
        "partition_type_prediction": "multi_stable",
    },
    "meanfield": {
        "experiment_doc": "experiments/aggregation_meanfield.md",
        "default_phase": "2c",
        "description": "Mean-field aggregation — cross-scope distortion metrics",
        "bc_classes": ["aggregation"],
        "partition_type_prediction": "binary",
    },
    "labyrinth": {
        "experiment_doc": "experiments/labyrinth_experiment_agenda.md",
        "default_phase": "2b",
        "description": "Context-navigation agent — mode ecology and scope transitions",
        "bc_classes": ["restriction", "forcing"],
        "partition_type_prediction": "hierarchical",
    },
    "custom": {
        "experiment_doc": "",
        "default_phase": "0",
        "description": "Custom system — fill in manually",
        "bc_classes": [],
        "partition_type_prediction": "",
    },
}


def create_case(case_id: str, system: str, phase: str) -> Path:
    today = date.today().isoformat()
    sys_info = SYSTEM_REGISTRY[system]

    case_dir = CASES / case_id
    if case_dir.exists():
        print(f"ERROR: Case directory already exists: {case_dir}")
        sys.exit(1)

    # Create subdirectories
    for subdir in ["results", "transfer", "audits"]:
        (case_dir / subdir).mkdir(parents=True)

    # Copy and stamp CaseRecord
    case_record_src = SCHEMAS / "CaseRecord.yaml"
    case_record_dst = case_dir / "CaseRecord.yaml"
    content = case_record_src.read_text()
    content = content.replace("CASE-YYYYMMDD-####", case_id)
    content = content.replace('phase: ""', f'phase: "{phase}"')
    content = content.replace('system: ""', f'system: "{system}"')
    content = content.replace('created_at: "YYYY-MM-DD"', f'created_at: "{today}"')
    content = content.replace('updated_at: "YYYY-MM-DD"', f'updated_at: "{today}"')
    content = content.replace('description: ""', f'description: "{sys_info["description"]}"')
    content = content.replace('experiment_doc: ""', f'experiment_doc: "{sys_info["experiment_doc"]}"')
    case_record_dst.write_text(content)

    # Copy and stamp ScopeSpec
    scope_id = case_id.replace("CASE", "SCOPE")
    scope_src = SCHEMAS / "ScopeSpec.yaml"
    scope_dst = case_dir / "ScopeSpec.yaml"
    content = scope_src.read_text()
    content = content.replace("SCOPE-YYYYMMDD-####", scope_id)
    content = content.replace('created_at: "YYYY-MM-DD"', f'created_at: "{today}"')
    content = content.replace('updated_at: "YYYY-MM-DD"', f'updated_at: "{today}"')
    content = content.replace('experiment_doc: ""', f'experiment_doc: "{sys_info["experiment_doc"]}"')
    if sys_info["partition_type_prediction"]:
        content = content.replace(
            'partition_type: ""',
            f'partition_type: "{sys_info["partition_type_prediction"]}"'
        )
    scope_dst.write_text(content)

    # Copy and stamp BCManifest
    bcm_id = case_id.replace("CASE", "BCM")
    bcm_src = SCHEMAS / "BCManifest.yaml"
    bcm_dst = case_dir / "BCManifest.yaml"
    content = bcm_src.read_text()
    content = content.replace("BCM-YYYYMMDD-####", bcm_id)
    content = content.replace("SCOPE-YYYYMMDD-####", scope_id)
    content = content.replace('created_at: "YYYY-MM-DD"', f'created_at: "{today}"')
    content = content.replace('updated_at: "YYYY-MM-DD"', f'updated_at: "{today}"')
    content = content.replace('experiment_doc: ""', f'experiment_doc: "{sys_info["experiment_doc"]}"')
    bcm_dst.write_text(content)

    # Update CaseRecord artifact ids
    cr = case_record_dst.read_text()
    cr = cr.replace('id: ""                          # SCOPE', f'id: "{scope_id}"                  # SCOPE')
    cr = cr.replace('id: ""                          # BCM',   f'id: "{bcm_id}"                    # BCM')
    case_record_dst.write_text(cr)

    return case_dir


def main():
    parser = argparse.ArgumentParser(description="Initialize a new ARW/ART case.")
    parser.add_argument("--id",      required=False, help="Case ID (CASE-YYYYMMDD-####)")
    parser.add_argument("--system",  default="custom", choices=list(SYSTEM_REGISTRY.keys()))
    parser.add_argument("--phase",   default=None)
    parser.add_argument("--list-systems", action="store_true")
    args = parser.parse_args()

    if args.list_systems:
        print("Available systems:")
        for name, info in SYSTEM_REGISTRY.items():
            print(f"  {name:12s}  phase={info['default_phase']}  —  {info['description']}")
        return

    if not args.id:
        today_compact = date.today().strftime("%Y%m%d")
        args.id = f"CASE-{today_compact}-0001"
        print(f"No --id given; using: {args.id}")

    phase = args.phase or SYSTEM_REGISTRY[args.system]["default_phase"]
    case_dir = create_case(args.id, args.system, phase)

    print(f"Case created: {case_dir}")
    print(f"  ScopeSpec : {case_dir}/ScopeSpec.yaml")
    print(f"  BCManifest: {case_dir}/BCManifest.yaml")
    print(f"  CaseRecord: {case_dir}/CaseRecord.yaml")
    print(f"\nNext step: fill in ScopeSpec.yaml and BCManifest.yaml, then run:")
    print(f"  python -m pipeline.validate --case cases/{args.id}")


if __name__ == "__main__":
    main()
