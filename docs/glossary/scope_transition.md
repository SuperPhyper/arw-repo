---
status: working-definition
layer: docs/glossary/
---

# Scope Transition

## Definition

A scope transition is a shift from one scope S to a new scope S' that occurs
when S loses admissibility — when the degrees of freedom it suppresses become
dynamically relevant and the current partition R_S no longer stably describes the system.

```
scope transition: S → S'
condition: S loses admissibility in region D ⊆ X_B
result: A(S') = R_S' replaces A(S) = R_S as the operative description
```

## Formal Condition

S undergoes a scope transition when, for some state x:

```
∃ π ∈ Π: |π(x_t) - π(x_{t+δ})| > ε   under perturbations within Δ
```

The observable distinction that should be stable under Δ is no longer stable.
The current scope cannot maintain its partition — [x]_S becomes unstable.

## Relation to Admissible Reduction

A scope transition is **not** the same as an admissible reduction.

- Admissible reduction: S → S' where R_S' is a compatible coarsening of R_S.
  The transition preserves structural information.
- Scope transition (general): S → S' where R_S' may reorganize R_S entirely.
  The new partition is not necessarily a coarsening — it may be a **reorganization**.

Emergence corresponds to a scope transition that is a reorganization, not a coarsening.

## Not Identical To

- **Phase transition:** A phase transition is a domain event (change in physical state).
  A scope transition is a descriptive event (change in which description is valid).
  They may coincide but are conceptually distinct.
- **Model change:** Changing a model is a deliberate choice. A scope transition is
  structurally forced — it is detected by admissibility loss, not chosen.
- **Regime change:** A regime change is a transition *within* a scope (R₁ → R₂ under S).
  A scope transition changes the scope itself (S → S').

## Related Concepts

- [admissibility.md](admissibility.md)
- [scope_dominance.md](scope_dominance.md)
- [emergence.md](emergence.md)

## Full Treatment

[docs/core/scope_transition.md](../core/scope_transition.md)
