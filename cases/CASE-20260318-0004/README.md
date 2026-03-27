---
status: note
layer: cases/CASE-20260318-0004/
---

# CASE-20260318-0004 — Coupled Stuart-Landau Oscillators (K-sweep)

**System:** Two coupled Stuart-Landau oscillators (Hopf normal form), K ∈ [0.01, 0.12], 12 sweep points
**BC class:** Coupling
**Domain:** Dynamical systems (DS)
**go_nogo:** pending — pipeline artifacts pending

**Special status:** First empirical ARW emergence case.

---

## Key Results

| Parameter | Value |
|---|---|
| Working ε | 0.09 |
| Regime count N | 2 |
| θ* / K* | K* ≈ 0.055 |
| Primary observable | PLV (phase-locking value) — sufficient |
| Insufficient observable | amp_asym — insufficient by design (emergence condition) |

**Emergence window:** ε ∈ [0.082, 0.805], width = 0.723
- amp_asym collapse (local) precedes PLV collapse (relational) → relational emergence
- Lambda-robustness: Δ-stable for λ ∈ [0.4, 1.3]; breaks at λ > 1.3 for weak K

**Observable design:** amp_asym insufficiency is by design, not a failure. It confirms
the relational emergence: the local property collapses before the relational one.
See `docs/advanced/arw_emergence_bc_relative.md`.

---

## Transfer

| Comparison | Φ | Status |
|---|---|---|
| CASE-0004 ↔ CASE-0001 | planned | First same-BC cross-system comparison (both Coupling) |

---

## Artifacts

```
CASE-20260318-0004/
├── ScopeSpec.yaml              ← S = (B, Π={PLV, amp_asym}, Δ, ε=0.09)
├── BCManifest.yaml             ← BC class: Coupling; K-sweep
├── CaseRecord.yaml             ← status: in_progress; go_nogo: pending
├── ScopeSpec_signature_first.md ← pre-pipeline BC inference document
├── results/                    ← pipeline artifacts pending
├── transfer/                   ← planned: CASE-0004 ↔ CASE-0001
└── audits/
```

---

## Open Questions

- Q_NEW_9: Is BC class a system property or scope property? (PLV is relational; amp_asym is local)
- Planned: compare PLV-scope and amp_asym-scope as first Φ_obs × Φ_sys decomposition test

**References:**
- `docs/advanced/arw_emergence_bc_relative.md` — formal emergence framework
- `docs/advanced/observable_consequences.md` — K4 (Φ decomposition)
- `docs/notes/research_journal.md` — session 2026-03-18
