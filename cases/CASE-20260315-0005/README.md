---
status: note
layer: cases/CASE-20260315-0005/
---

# CASE-20260315-0005 — Multi-Pendel + damping (γ-sweep)

**System:** Multi-Pendel + damping (γ-sweep)
**BC class:** Dissipation
**go_nogo:** open — signature-first only, pipeline not yet run

---

## Status

Pre-pipeline stage. A `ScopeSpec_signature_first.md` has been created formalizing
the BC inference from system operators before simulation.

**Next step:** Run pipeline sweep → extract partition → compute invariants.

---

## Artifacts

```
CASE-20260315-0005/
├── CASE-20260315-0005_ScopeSpec_signature_first.md   ← pre-pipeline BC inference
├── ScopeSpec.yaml (or CASE_ScopeSpec.yaml)
├── BCManifest.yaml
└── CaseRecord.yaml
```

---

*See [cases/README.md](../README.md) for the full case registry.*
