---
status: working-definition
---

# Regime Partition

## Definition

The regime partition R_S is the equivalence structure over the admissible
state space X_B induced by the ARW operator under scope S:

```
A(S) = R_S
```

Two states x, y ∈ X_B belong to the same regime class [x]_S if and only if
they are robustly indistinguishable under S:

```
x ~_S y  iff  |Π(x) - Π(y)| < ε   for all perturbations within Δ
```

## Structure

R_S is a partition of X_B into disjoint, exhaustive equivalence classes:

```
X_B = R₁ ∪ R₂ ∪ ... ∪ Rₙ,   Rᵢ ∩ Rⱼ = ∅ for i ≠ j
```

Each class Rᵢ is a behavioral regime — a set of states that behave
indistinguishably under the chosen scope.

## Dependence on Scope

The same underlying system produces different regime partitions under different scopes.
This is the central claim of ARW: partition structure is scope-relative,
not an intrinsic property of the system.

```
A(S)  = R_S   (one partition)
A(S') = R_S'  (different partition, same system)
```

## Not Identical To

- **Phase diagram:** A phase diagram is domain-specific and represents
  intrinsic system properties. A regime partition is scope-relative and
  formally derived from S = (B, Π, Δ, ε).
- **Attractor set:** Attractors are intrinsic dynamical objects.
  A regime class may correspond to a basin of attraction, but only
  when the scope observables are chosen to resolve basin structure.
- **Cluster:** Clustering is a data analysis operation.
  A regime partition is derived from the formal scope specification,
  not from data similarity alone.

## Related Concepts

- [scope.md](scope.md)
- [admissibility.md](admissibility.md)
- [partition.md](partition.md)

## Full Treatment

[docs/core/arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md)
