---
status: note
layer: cases/
---

# Cases

Each subdirectory contains all artifacts for a single experiment instance.
A case bundles the full pipeline output for one system under one scope:
ScopeSpec → BCManifest → sweep → partition → invariants → transfer → audit.

---

## Case Structure

```
CASE-YYYYMMDD-####/
├── ScopeSpec.yaml              ← ART scope instantiation
├── BCManifest.yaml             ← BC classification + sweep program
├── CaseRecord.yaml             ← Case envelope (status, artifact registry)
├── results/
│   ├── raw/
│   │   └── sweep_results.json  ← Raw sweep output
│   └── partition/
│       ├── PartitionResult.json
│       └── Invariants.json
├── transfer/
│   └── <comparison_name>/
│       ├── TransferMetrics.json
│       └── TransferReport.md
└── audits/
    └── FailureAudit_Phase{N}.md
```

---

## Current Cases

| Case ID | System | BC Class | Domain | Status |
|---|---|---|---|---|
| [CASE-20260311-0001](CASE-20260311-0001/) | Kuramoto oscillators (κ-sweep) | Coupling | DS | pending (sweep_refinement) |
| [CASE-20260311-0002](CASE-20260311-0002/) | Multi-Link-Pendel (κ-sweep) | Coupling | DS | go |
| [CASE-20260311-0003](CASE-20260311-0003/) | Doppelpendel (E-sweep) | Restriction | DS | go |
| [CASE-20260315-0004_stuart_landau](CASE-20260315-0004_stuart_landau/) | Stuart-Landau oscillator (μ-sweep) | Dissipation | DS | pending |
| [CASE-20260315-0005](CASE-20260315-0005/) | Multi-Pendel with damping (γ-sweep) | Dissipation | DS | pending |
| [CASE-20260315-0006](CASE-20260315-0006/) | Multi-Pendel with forcing (Ω-sweep) | Forcing | DS | pending |
| [CASE-20260315-0007](CASE-20260315-0007/) | SIR epidemic model (β-sweep) | Aggregation | EPI | pending |
| [CASE-20260315-0008](CASE-20260315-0008/) | Pitchfork bifurcation (μ-sweep) | Symmetry_Breaking | DS | pending |
| [CASE-20260315-0009](CASE-20260315-0009/) | Stochastic Kuramoto (σ-sweep) | Stochastic_BC | DS | pending |
| [CASE-20260315-SOC1](CASE-20260315-SOC1/) | Shame interaction regime | Restriction | SOC | no_go (Pre-Screening blocked) |

**BC coverage:** All 7 classes covered — Coupling, Restriction, Dissipation, Forcing, Aggregation, Symmetry_Breaking, Stochastic_BC

**Transfer computed:** CASE-0001↔0002 (Φ=0.675) · CASE-0001↔0003 (Φ=0.40/0.95*)
All other pairs pending pipeline runs.

---

## Creating a New Case

```bash
python -m pipeline.new_case --id CASE-YYYYMMDD-#### --system <system> --phase <N>
```

This scaffolds the directory structure and stamps schema copies with the case ID.
See [pipeline/README.md](../pipeline/README.md) for full CLI reference.

---

## Design Principle

No agent retains state between sessions.
All progress lives in artifacts. Any agent can be replaced or re-run
from the artifact state alone.
