---
status: working-definition
---

# Scope Dominance

## Definition

A scope S is dominant over a system when it successfully orders
the system's relevant degrees of freedom — when its observables Π
produce a stable partition R_S under the admissible perturbations Δ.

```
S is dominant: A(S) = R_S is stable under all δx ∈ Δ
```

## Loss of Dominance

Scope dominance is lost when suppressed degrees of freedom
become dynamically relevant — when they begin to influence
the observables in Π in ways that cross the resolution threshold ε.

Signals of dominance loss:
- Sensitivity to initial conditions within the same regime class
- Apparent chaos under S (trajectories that should be equivalent diverge)
- Partition instability: [x]_S changes under perturbations within Δ

## Not Identical To

- **Predictive accuracy:** A scope can dominate without being maximally predictive.
  Dominance is about structural stability of the partition, not prediction error.
- **Correctness:** A dominant scope is not necessarily "true" —
  it is structurally stable for the current BC configuration.
- **Coverage:** A scope can dominate over a subset of the state space
  while losing dominance in other regions.

## Related Concepts

- [admissibility.md](admissibility.md)
- [scope_transition.md](scope_transition.md)

## Full Treatment

[docs/core/scope_dominance.md](../core/scope_dominance.md)
