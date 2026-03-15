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
| TBS | \|θ\*_A/range_A − θ\*_B/range_B\| | Normalised transition boundary shift (incommensurable axes safe) |
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

## Phase 1 Status

### CASE-0001 — Kuramoto (κ-Sweep, Coupling BC)

```
validate      ✓  0 errors, 0 warnings
sweep         ✓  36 κ points in [0, 3], N=500, T=200s
extract       ✓  4 regimes recovered (Incoherent / Onset / Partial / Synchronized)
invariants    ✓  count=4 | adjacency: 3 edges | persistence=0.914 | θ*=1.475
epsilon_sweep ✓  80 ε values in [0.001, 1.0] — working ε=0.09 (N=4 plateau, w=0.700)
              ℹ  Most robust partition: N=5, I_ε=[0.009, 0.047], w=1.66
              ℹ  Expected 3-regime partition: I_ε=[0.146, 0.294], w=0.70
epsilon_kappa ✓  2D (κ,ε) robustness map — scope fragile near κ≈K_c
transfer      ✓  CASE-0001 ↔ CASE-0002: Φ=0.675 (partially_admissible)
              ✓  CASE-0001 ↔ CASE-0003: Φ=0.40 (inadmissible at ε-mismatch)
audit         ✓  all checks clean
```

**Note on θ\*:** θ\*=1.475 is above K_c≈0.64 (go/no-go criterion not yet met).
Denser κ sweep in [0.5, 0.9] needed to recover K_c within 5%. This is
`severity: sweep_refinement` (F1 in ScopeSpec), not a scope_rejection.

### CASE-0002 — Multi-Link-Pendel (κ-Sweep, Coupling BC)

```
validate      ✓  0 errors, 0 warnings
sweep         ✓  25 κ points in [0, 10], fixed γ=0.1
extract       ✓  3 regimes (Decoupled/Chaotic / Transitional / Low-var/Locked)
invariants    ✓  count=3 | adjacency: 2 edges | persistence=0.917 | θ*=3.25
epsilon_sweep ✓  N=3 at ε=0.023 (single-point plateau — fragil, dokumentiert)
              ℹ  Robusterer N=2-Plateau: I_ε=[0.025, 0.044], w=0.551
              ⚠  ε=0.023 liegt auf Plateau-Grenze; epsilon_choice_note in ScopeSpec
transfer      ✓  CASE-0002 ↔ CASE-0001: Φ=0.675 (partially_admissible), RCD=1
audit         ✓  1 verbleibende Warning (ε-Fragilität, akzeptiert)
```

**Primary observable:** var_rel (span=0.274, Faktor 7× gegenüber lambda_proxy=0.037).
**γ-Fix:** bc_02 nutzt `sweeps: []` + `fixed_params: {gamma: 0.1}` — kein γ-Kontaminant mehr.

### CASE-0003 — Doppelpendel (E-Sweep, Restriction BC)

```
validate      ✓  0 errors, 0 warnings
sweep         ✓  12 E_target points in [0.5, 30 J]
extract       ✓  9 regimes at ε=0.015 (primary: var_rel)
invariants    ✓  count=9 | adjacency: 8 edges | persistence=0.727 | θ*=8.5 J
              ⚠  persistence=0.727 — sweep zu dünn (12 Punkte). Kein Blocker.
epsilon_sweep ✓  ε=0.015 interior of N=9 plateau
transfer      ✓  CASE-0003 ↔ CASE-0001: Φ=0.40 (inadmissible at ε-mismatch)
              ℹ  At matched ε (ε_A=0.034, N=4): Φ≈0.95 (highly_admissible)
audit         pending
```

**Multi-Observable:** lambda_proxy (span=0.069) vs. var_rel (span=0.297 — 4.3×).
var_rel ist primary. Nur 37% ε-Übereinstimmung zwischen Observablen — Q3 empirisch untermauert.

---

## BC-coupled Clustering — Observable-Auswahl

`pipeline.extract_partition` löst das primäre Observable in dieser Reihenfolge auf:

1. ScopeSpec `Pi[*].observable_key` wo `primary: true` — maschinenlesbarer Vorrang
2. `extract_observables_<system>()` `default_primary` — systemspezifischer Fallback
3. Laufzeit-Parameter `--primary-observable` — optionaler Override

Jedes Observable braucht ein eigenes εᵢ kalibriert auf seinen Wertebereich (Q3).
Observable-Insuffizienz (`span < 2ε`) ist keine Scope-Rejection — das Observable wird
ersetzt, nicht der Scope. Scope-Rejection (`severity: scope_rejection` in ScopeSpec)
gilt nur wenn *alle* Observablen unzureichend sind.

---

## Nächste Schritte

1. CASE-0001: Dichterer Sweep κ ∈ [0.5, 0.9] um K_c-go/no-go zu erfüllen
2. CASE-0002: Dichterer Sweep κ ∈ [3.0, 5.5] für breiteres N=3-Plateau
3. CASE-0003: Sweep-Verdichtung E ∈ [2, 8 J]; Transfer mit ε_A=0.034 (matched N=4)
4. CASE-0004: Dissipation-BC (fehlt noch — dritte BC-Klasse für Taxonomie)
