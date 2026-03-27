---
status: note
layer: cases/CASE-20260315-0006/
---

# CASE-20260315-0006 — Multi-Pendel + forcing (Ω-sweep)

**System:** Multi-Pendel + forcing (Ω-sweep)
**BC class:** Forcing
**go_nogo:** open — signature-first only, pipeline not yet run

---

## Status

Pre-pipeline stage. A `ScopeSpec_signature_first.md` has been created formalizing
the BC inference from system operators before simulation.

**Next step:** Run pipeline sweep → extract partition → compute invariants.

---

## Artifacts

```
CASE-20260315-0006/
├── CASE-20260315-0006_ScopeSpec_signature_first.md   ← pre-pipeline BC inference
├── ScopeSpec.yaml (or CASE_ScopeSpec.yaml)
├── BCManifest.yaml
└── CaseRecord.yaml
```

---

*See [cases/README.md](../README.md) for the full case registry.*
