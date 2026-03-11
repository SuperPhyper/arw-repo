# Pipeline

Python implementation of the ARW/ART partition extraction pipeline.
Implements the full workflow from scope specification to cross-scope transfer analysis.

For the methodological design document, see [PartitionPipeline.md](PartitionPipeline.md).

---

## Architecture

```
ScopeSpec.yaml + BCManifest.yaml
        │
        ▼
    validate          ← structural completeness check
        │
        ▼
    sweep             ← BC parameter sweep → results/raw/sweep_results.json
        │
        ▼
    extract_partition ← observable extraction + ε-regime assignment
        │               → results/partition/PartitionResult.json
        ▼
    invariants        ← regime count, adjacency graph, persistence, θ*
        │               → results/partition/Invariants.json
        ▼
    transfer          ← RCD, TBS, PCI, SDI across two cases
        │               → transfer/TransferReport.md + TransferMetrics.json
        ▼
    audit_helpers     ← A5 failure audit
                        → audits/FailureAudit_Phase{N}.md
```

---

## Modules

| Module | Purpose |
|---|---|
| [validate.py](validate.py) | Structural completeness check on ScopeSpec + BCManifest |
| [sweep.py](sweep.py) | BC parameter sweep; simulation kernels (Kuramoto implemented, others stubbed) |
| [extract_partition.py](extract_partition.py) | Observable extraction + ε-threshold regime assignment |
| [invariants.py](invariants.py) | Partition invariants: regime count, adjacency graph, persistence, hysteresis, θ* |
| [transfer.py](transfer.py) | Cross-scope distortion metrics (RCD, TBS, PCI, SDI, Φ) |
| [audit_helpers.py](audit_helpers.py) | A5 failure audit: scope leakage, ε robustness, partition match, falsification |
| [new_case.py](new_case.py) | Case directory scaffolding generator |

---

## CLI Reference

```bash
# Create a new case
python -m pipeline.new_case --id CASE-YYYYMMDD-#### --system kuramoto --phase 1
python -m pipeline.new_case --list-systems

# Validate scope + manifest
python -m pipeline.validate --case cases/CASE-...
python -m pipeline.validate --case cases/CASE-... --strict

# Run BC sweep
python -m pipeline.sweep --case cases/CASE-... --out results/raw
python -m pipeline.sweep --case cases/CASE-... --dry-run

# Extract partition
python -m pipeline.extract_partition --case cases/CASE-... --in results/raw --out results/partition

# Compute invariants
python -m pipeline.invariants --case cases/CASE-... --in results/partition --out results/partition

# Cross-scope transfer (requires two completed cases)
python -m pipeline.transfer --caseA cases/CASE-A --caseB cases/CASE-B --out transfer

# Failure audit
python -m pipeline.audit_helpers --case cases/CASE-... --phase 1 --out audits
```

---

## Simulation Kernels

| System | Status | Key observable | Analytical ground truth |
|---|---|---|---|
| `kuramoto` | implemented | r_ss (order parameter) | K_c = 2/(π·g(0)) ≈ 0.6366 |
| `pendulum` | stub | Lyapunov indicators | none |
| `consensus` | stub | cluster count, opinion variance | none |
| `meanfield` | stub | distribution peak count | from agent-level |
| `labyrinth` | stub | policy embedding cluster count | none |

To add a system: implement `run_<s>(params, sweep_point, rng) -> dict`
in `sweep.py`, register in `KERNEL_MAP`, add observable extractor
in `extract_partition.py`, and register in `OBSERVABLE_MAP`.

---

## Schemas

All schemas are defined in [`schemas/`](../schemas/). Each new case gets its own
copies, stamped with case ID and date by `new_case`.

---

## Current Status

End-to-end validated on Kuramoto Phase 1 (`CASE-20260311-0001`).
See [PartitionPipeline.md](PartitionPipeline.md) § Phase 1 Status for details.
