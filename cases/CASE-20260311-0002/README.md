---
status: note
layer: cases/CASE-20260311-0002/
---

# CASE-20260311-0002 — Multi-Link Pendulum (κ-sweep)

**System:** 4-link pendulum, κ ∈ [0, 10], 25 sweep points, fixed γ=0.1
**BC class:** Coupling
**Domain:** Dynamical systems (DS)
**go_nogo:** go (2026-03-12)

---

## Key Results

| Parameter | Value |
|---|---|
| Working ε | 0.023 |
| Regime count N | 3 |
| θ* | 3.25 |
| Primary observable | var_rel (relative variance) |
| Insufficient observable | lambda_proxy — structurally insufficient by construction |

**Observable note:** lambda_proxy is insufficient because A6.1 and A6.2 (finite T,
finite δθ(0)) are violated by construction — not a measurement quality issue.
See `docs/advanced/observable_decomposition.md`.

---

## Transfer

| Comparison | Φ | Admissibility | Notes |
|---|---|---|---|
| CASE-0002 ↔ CASE-0001 | 0.675 | partially_admissible | TBS_norm=0.167, RCD=1; same BC class |

---

## Artifacts

```
CASE-20260311-0002/
├── ScopeSpec.yaml              ← S = (B, Π={var_rel}, Δ, ε=0.023)
├── BCManifest.yaml             ← BC class: Coupling; κ-sweep; fixed_params: {gamma: 0.1}
├── CaseRecord.yaml             ← status: complete; go_nogo: go (2026-03-12)
├── results/
│   ├── raw/
│   └── partition/              ← PartitionResult.json, Invariants.json
├── transfer/
│   └── pendulum_vs_kuramoto/   ← TransferMetrics.json, TransferReport.md (Φ=0.675)
└── audits/
    └── FailureAudit_Phase1.md
```
