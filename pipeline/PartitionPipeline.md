---
status: working-definition
---

# Partition Extraction Pipeline

This document is the Phase 0 methodological deliverable described in
`docs/overview/roadmap.md`. It specifies the full workflow from
scope specification to cross-scope transfer analysis.

**Implemented:** `pipeline/` Python modules (validated end-to-end on Kuramoto Phase 1).  
**Schemas:** `schemas/` (ScopeSpec.yaml, BCManifest.yaml, CaseRecord.yaml).  
**Cases:** `cases/` (one directory per experiment instance).

---

## Pipeline Overview

```
ScopeSpec.yaml + BCManifest.yaml
        │
        ▼
pipeline.validate          ← structural completeness check
        │
        ▼
pipeline.sweep             ← BC parameter sweep, writes results/raw/sweep_results.json
        │
        ▼
pipeline.extract_partition ← observable extraction + ε-regime assignment
        │                    writes results/partition/PartitionResult.json
        ▼
pipeline.epsilon_sweep     ← ε-sweep: admissible ε-interval, plateaus, critical ε-values
        │                    writes results/partition/EpsilonSweep.json
        ▼
pipeline.invariants        ← regime_count, adjacency_graph, persistence,
        │                    hysteresis_width, θ*
        │                    writes results/partition/Invariants.json
        ▼
pipeline.transfer          ← RCD, TBS, PCI, SDI, Φ across two cases
        │                    writes transfer/TransferReport.md + TransferMetrics.json
        ▼
pipeline.audit_helpers     ← A5 failure audit: scope leakage, ε robustness,
                             partition match, falsification integrity, transfer
                             writes audits/FailureAudit_Phase{N}.md
```

---

## CLI Reference

```bash
# 1. Create a new case
python -m pipeline.new_case --id CASE-YYYYMMDD-#### --system kuramoto --phase 1
python -m pipeline.new_case --list-systems

# 2. Fill in ScopeSpec.yaml and BCManifest.yaml, then validate
python -m pipeline.validate --case cases/CASE-...
python -m pipeline.validate --case cases/CASE-... --strict

# 3. Run BC sweep
python -m pipeline.sweep --case cases/CASE-... --out results/raw
python -m pipeline.sweep --case cases/CASE-... --dry-run      # preview sweep points

# 4. Extract partition
python -m pipeline.extract_partition --case cases/CASE-... --in results/raw --out results/partition

# 4b. ε-sweep (find admissible ε-interval)
python -m pipeline.epsilon_sweep --case cases/CASE-... --eps-min 0.001 --eps-max 1.0 --eps-steps 80

# 5. Compute invariants
python -m pipeline.invariants --case cases/CASE-... --in results/partition --out results/partition

# 6. Cross-scope transfer analysis (requires two completed cases)
python -m pipeline.transfer --caseA cases/CASE-A --caseB cases/CASE-B --out transfer

# 7. Failure audit
python -m pipeline.audit_helpers --case cases/CASE-... --phase 1 --out audits
```

---

## Artifact Schemas

All schemas are in `schemas/`. Each new case gets its own copies, stamped
with the case ID and date by `pipeline.new_case`.

| Schema | Purpose |
|---|---|
| `ScopeSpec.yaml` | ART scope instantiation: X, B, Π, Δ, ε, expected partition |
| `BCManifest.yaml` | BC classification, sweep program, distortion metrics plan |
| `CaseRecord.yaml` | Case envelope: artifact registry, go/no-go criteria, agent assignments |

---

## Partition Invariants

Computed by `pipeline.invariants`. These are the transferable quantities
used in cross-scope comparison (see `docs/bc_taxonomy/transfer_distortion_metrics.md`).

| Invariant | Symbol | Definition |
|---|---|---|
| Regime count | N | \|R_S\| — number of equivalence classes |
| Adjacency graph | G_S | Which regimes are adjacent in parameter space |
| Persistence | P | Fraction of sweep interval with stable regime assignment |
| Hysteresis width | H | Width of bistable parameter window (if any) |
| Transition boundary | θ* | Parameter value at regime transition |

---

## Distortion Metrics

Computed by `pipeline.transfer`. Reference: `docs/bc_taxonomy/transfer_distortion_metrics.md`.

| Metric | Formula | Interpretation |
|---|---|---|
| RCD | \|N_A − N_B\| | Regime count discrepancy |
| TBS | \|θ\*_A − θ\*_B\| | Transition boundary shift |
| PCI | (1/N) Σ pᵢ | Partition compatibility (0=inadmissible, 1=fully compatible) |
| SDI | graph\_edit\_distance(G_A, G_B) | Structural distortion of adjacency graph |
| Φ | weighted composite | Overall admissibility score ∈ [0,1] |

**Admissibility thresholds:**
- Φ ≥ 0.85 → highly admissible (compatible coarsening)
- Φ ∈ [0.6, 0.85) → partially admissible (distortion localized)
- Φ < 0.6 → inadmissible (informative failure — identify driving BC class)

---

## Simulation Kernels

Located in `pipeline/sweep.py`. Currently implemented:

| System | Status | Key observable | Analytical ground truth |
|---|---|---|---|
| `kuramoto` | ✓ implemented | r_ss (order parameter) | K_c = 2/(π·g(0)) ≈ 0.6366 |
| `pendulum` | stub | Lyapunov indicators | none |
| `consensus` | stub | cluster count, opinion variance | none |
| `meanfield` | stub | distribution peak count | from agent-level |
| `labyrinth` | stub | policy embedding cluster count | none |

To add a system: implement `run_<system>(params, sweep_point, rng) -> dict`
in `pipeline/sweep.py` and register in `KERNEL_MAP`. Add observable extractor
in `pipeline/extract_partition.py` and register in `OBSERVABLE_MAP`.

---

## Agent Role Mapping

From `agents/roles.md` and the Multi-Agent Scaffold (Feb 28, 2026):

| Agent | Role | Pipeline step |
|---|---|---|
| A0 | Orchestrator | `new_case`, registry management |
| A1 | Scope Formalizer | fills `ScopeSpec.yaml` |
| A2 | Boundary Taxonomist | fills `BCManifest.yaml` |
| A3 | Partition Engineer | runs `sweep`, `extract_partition`, `invariants` |
| A4 | Transfer Analyst | runs `transfer` |
| A5 | Skeptic / Failure Auditor | runs `audit_helpers` |

**Key principle:** No agent retains state between sessions.
All progress lives in artifacts. Any agent can be replaced or re-run
from the artifact state alone.

---

## Phase 1 Status (Kuramoto)

Case `CASE-20260311-0001` completed end-to-end:

```
validate      ✓  0 errors, 0 warnings
sweep         ✓  15 κ points, N=500, T=200s
extract       ✓  3 regimes recovered (Incoherent / Partial / Synchronized)
invariants    ✓  count=3 ✓ | adjacency: 2 edges | persistence=0.857
              ⚠  θ* = 1.25 (expected ~0.64 — sweep density too low near transition)
epsilon_sweep ✓  80 ε values in [0.001, 1.0] — 5 structurally distinct plateaus
              ⚠  Working ε=0.05 sits at plateau boundary (N=5→4 at ε*≈0.049)
              ℹ  Most robust partition: N=5, I_ε=[0.009, 0.047], w=1.66
              ℹ  Expected 3-regime partition: I_ε=[0.146, 0.294], w=0.70
audit         ✓  4/5 checks clean | 1 pending: TransferMetrics (awaits pendulum case)
```

**Note on θ\*:** The current sweep resolves the transition coarsely.
Add denser kappa values in [0.5, 0.9] to recover K_c within 5% (go/no-go criterion).

**Note on ε:** The ε-sweep reveals that the working ε=0.05 is at a critical
boundary. Recommend updating to ε=0.03 (N=5 plateau) or ε=0.09 (N=4 plateau)
depending on the desired resolution level. The expected 3-regime partition
requires ε ≈ 0.15–0.29 — coarser than the current working value.

---

## Next Steps

1. Add dense sweep near κ ∈ [0.5, 0.9] to recover K_c within 5%
2. Create `CASE-20260311-0002` (pendulum) and run Phase 1
3. Run `pipeline.transfer --caseA CASE-0001 --caseB CASE-0002`
4. Implement pendulum kernel in `pipeline/sweep.py`
