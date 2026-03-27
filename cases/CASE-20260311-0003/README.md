---
status: note
layer: cases/CASE-20260311-0003/
---

# CASE-20260311-0003 — Classical Double Pendulum (E-sweep)

**System:** Classical double pendulum, E_target ∈ [0.5, 30 J], 12 sweep points
**BC class:** Restriction
**Domain:** Dynamical systems (DS)
**go_nogo:** go (2026-03-12)

---

## Key Results

| Parameter | Value |
|---|---|
| Working ε | 0.015 |
| Regime count N | 9 |
| θ* | 8.5 J |
| Primary observable | var_rel (relative variance) |
| Insufficient observable | lambda_proxy — structurally insufficient by construction |

**Observable note:** Same structural reason as CASE-0002: lambda_proxy assumes A6.1 and A6.2
which are violated by construction. See `docs/advanced/observable_decomposition.md`.

---

## Transfer

| Comparison | Φ | Admissibility | Notes |
|---|---|---|---|
| CASE-0003 ↔ CASE-0001 | 0.40 raw | partially_admissible | Different BC classes, unmatched ε |
| CASE-0003 ↔ CASE-0001 | ≈0.95 | highly_admissible | At matched ε (both N=4); sequential topology universal |

**Key finding from transfer:** At matched ε, Coupling and Restriction produce structurally equivalent
sequential partitions. BC class-specific signal is in θ*/range (position) and plateau width
(robustness), not in partition cardinality.

---

## Artifacts

```
CASE-20260311-0003/
├── ScopeSpec.yaml              ← S = (B, Π={var_rel}, Δ, ε=0.015)
├── BCManifest.yaml             ← BC class: Restriction; E-sweep
├── CaseRecord.yaml             ← status: complete; go_nogo: go (2026-03-12)
├── results/
│   ├── raw/
│   └── partition/              ← PartitionResult.json, Invariants.json
├── transfer/
│   └── doppelpendulum_vs_kuramoto/  ← TransferMetrics.json, TransferReport.md
└── audits/
    └── FailureAudit_Phase1.md
```
