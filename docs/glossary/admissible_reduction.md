---
status: working-definition
---

# Admissible Reduction

## Definition

A scope transition S → S' is an admissible reduction if the induced
partition R_S' is a compatible coarsening of R_S:

```
∀x ∈ X_B: [x]_S ⊆ [x]_S'
```

Every regime class under S must be fully contained within a regime class under S'.
No class in R_S may straddle a boundary in R_S'.

## Intuition

An admissible reduction is a scope transition that loses resolution
without distorting structure. The coarser scope S' sees less detail,
but what it sees is consistent with what S sees.

An inadmissible reduction distorts — it merges states from different
regime classes into the same coarse class, destroying structural information.

## Formal Criterion

S → S' is admissible iff the function f: R_S → R_S' defined by

```
f(Rᵢ) = R'ⱼ   where Rᵢ ⊆ R'ⱼ
```

is well-defined (each fine class maps to exactly one coarse class).

If this function is not well-defined — some Rᵢ intersects multiple R'ⱼ —
the reduction is inadmissible.

## Degree of Admissibility

Admissibility is not binary in practice. The distortion metrics
(RCD, TBS, PCI, SDI) quantify the degree to which a reduction
deviates from perfect admissibility.

## Not Identical To

- **Approximation:** An approximation accepts error. An admissible reduction
  makes no error within its resolution — it simply sees less.
- **Simplification:** A simplification is a modeling choice. An admissible
  reduction is a structurally verified scope transition.
- **Coarse-graining (statistical physics):** Coarse-graining is a specific
  technical operation. Admissible reduction is the general ARW condition
  that coarse-graining must satisfy to preserve regime structure.

## Related Concepts

- [regime_partition.md](regime_partition.md)
- [scope_transition.md](scope_transition.md)
- [admissibility.md](admissibility.md)

## Full Treatment

[docs/core/arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md)
