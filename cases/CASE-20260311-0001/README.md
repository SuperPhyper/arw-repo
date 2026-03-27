---
status: note
layer: cases/CASE-20260311-0001/
---

# CASE-20260311-0001 — Kuramoto Oscillators (κ-sweep)

**System:** Kuramoto oscillators, N=500, κ ∈ [0, 3], 36 sweep points
**BC class:** Coupling
**Domain:** Dynamical systems (DS)
**go_nogo:** pending — F1: sweep_refinement (θ* at sweep boundary)

---

## Key Results

| Parameter | Value |
|---|---|
| Working ε | 0.09 |
| Regime count N | 4 |
| θ* (transition boundary) | 1.475 |
| Primary observable | r_ss (order parameter) |
| Analytical ground truth | K_c = 2/(π·g(0)) ≈ 0.6366 |

**Important:** θ* ≈ 1.475 lies in Z(r_ss) — the exclusion zone where r_ss violates
pre-scope substrate assumptions simultaneously. This is a **scope transition**, not a
regime boundary. See `docs/glossary/observable_range.md` and `docs/advanced/observable_consequences.md` K3.

---

## Transfer

| Comparison | Φ | Admissibility | Notes |
|---|---|---|---|
| CASE-0001 ↔ CASE-0002 | 0.675 | partially_admissible | TBS_norm=0.167, RCD=1 |
| CASE-0001 ↔ CASE-0003 | 0.40 raw / ≈0.95 matched-ε | partially / highly | Coupling vs Restriction; matched at N=4 |
| CASE-0001 ↔ CASE-20260318-0004 | planned | — | First same-BC cross-system comparison |

---

## Artifacts

```
CASE-20260311-0001/
├── ScopeSpec.yaml              ← S = (B, Π={r_ss}, Δ, ε=0.09)
├── BCManifest.yaml             ← BC class: Coupling; κ-sweep program
├── CaseRecord.yaml             ← status: complete; go_nogo: pending (sweep_refinement)
├── kuramoto_case_notes.md      ← Case-specific working notes
├── results/
│   ├── raw/                    ← sweep_results.json
│   └── partition/              ← PartitionResult.json, Invariants.json
├── transfer/
│   └── kuramoto_vs_pendulum/   ← TransferMetrics.json, TransferReport.md (Φ=0.675)
└── audits/
    └── FailureAudit_Phase1.md
```

---

## Open Issues

- F4: θ* at sweep boundary — sweep refinement needed around κ ∈ [1.3, 1.7]
- Q_NEW_12: χ = ∂r_ss/∂κ as fluctuation observable (R(χ) ∋ κ_c) — high priority extension

**Reference:** `docs/notes/research_journal.md` — Session 2026-03-18
