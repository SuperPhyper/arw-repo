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

## Pipeline-Run Cases

Cases with sweep data and pipeline artifacts.

| Case ID | System | BC Class | θ* | go_nogo | Notes |
|---|---|---|---|---|---|
| [CASE-20260311-0001](CASE-20260311-0001/) | Kuramoto oscillators (κ-sweep, 36 pts) | Coupling | 1.475 | pending | F1: sweep_refinement; θ* in Z(r_ss) — scope transition, not regime boundary |
| [CASE-20260311-0002](CASE-20260311-0002/) | Multi-Link-Pendel (κ-sweep, 25 pts) | Coupling | 3.25 | go (2026-03-12) | var_rel primary; lambda_proxy structurally insufficient |
| [CASE-20260311-0003](CASE-20260311-0003/) | Doppelpendel (E-sweep, 12 pts) | Restriction | 8.5 J | go (2026-03-12) | var_rel primary; lambda_proxy structurally insufficient |
| [CASE-20260318-0004](CASE-20260318-0004/) | Two coupled Stuart-Landau (K-sweep, 12 pts) | Coupling | K*≈0.055 | pending | First ARW emergence case; PLV primary; amp_asym insufficient by design |

**Transfer computed:**
- CASE-0001 ↔ CASE-0002: Φ=0.675 (partially_admissible), RCD=1, TBS_norm=0.167
- CASE-0001 ↔ CASE-0003: Φ=0.40 raw / Φ≈0.95 at matched ε
- CASE-0004 ↔ CASE-0001: planned (first same-BC cross-system comparison)

---

## Signature-First Cases

Cases with `ScopeSpec_signature_first.md` pre-pipeline artifact. Pipeline not yet run.

| Case ID | System | BC Class | Domain |
|---|---|---|---|
| [CASE-20260315-0004_stuart_landau](CASE-20260315-0004_stuart_landau/) | Stuart-Landau oscillator (μ-sweep) | Dissipation | DS |
| [CASE-20260315-0005](CASE-20260315-0005/) | Multi-Pendel + damping (γ-sweep) | Dissipation | DS |
| [CASE-20260315-0006](CASE-20260315-0006/) | Multi-Pendel + forcing (Ω-sweep) | Forcing | DS |
| [CASE-20260315-0007](CASE-20260315-0007/) | SIR epidemic model (β-sweep) | Aggregation | EPI |
| [CASE-20260315-0008](CASE-20260315-0008/) | Pitchfork normal form (μ-sweep) | Symmetry Breaking | DS |
| [CASE-20260315-0009](CASE-20260315-0009/) | Stochastic Kuramoto (σ-sweep) | Coupling + Noise | DS |
| [CASE-20260315-SOC1](CASE-20260315-SOC1/) | Shame interaction regime | Restriction (social) | SOC |

**BC coverage:** All 6 canonical classes represented — Coupling (0001/0002/0318-0004/0009), Restriction (0003/SOC1), Dissipation (0004_sl/0005), Forcing (0006), Aggregation (0007), Symmetry Breaking (0008).

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
