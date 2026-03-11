---
status: working-definition
---


# Scope Transition and Admissible Reduction
## ARW Concept Note (Consistent with S = (B, Π, Δ, ε))

## Overview

In many modeling contexts, reduction is treated as a technical operation: variables are removed or compressed to simplify a description.

Within the ARW framework, reduction should instead be interpreted as a **scope transition**. A reduction is admissible only when the regime structure induced by the reduced scope remains structurally compatible with the regime structure of the original scope.

This formulation aligns reduction directly with the ARW operator, which maps scope specifications to regime partitions.

---

# 1. Scope Definition in ARW

In ARW, a scope is defined as the tuple

S = (B, Π, Δ, ε)

where

- B — constraints selecting admissible states X_B ⊆ X
- Π — admissible descriptions or projections
- Δ — admissible perturbations
- ε — resolution threshold for distinguishability

The ARW operator maps a scope to its induced regime partition:

A(S) = R_S

Thus every scope specification induces a specific equivalence structure over admissible states.

---

# 2. Reduction as Scope Transition

A reduction is therefore not simply

(O₁, O₂, O₃) → O_eff

but a transformation between scopes

S → S'

with

S = (B, Π, Δ, ε)
S' = (B', Π', Δ', ε')

The transformation changes the description structure, perturbation admissibility, constraints, or resolution threshold.

Reduction becomes a **change in distinguishability structure**, not merely a loss of variables.

---

# 3. Partition-Based Reduction Criterion

Let

R_S = A(S)
R_{S'} = A(S')

be the regime partitions induced by the two scopes.

A scope transition S → S' constitutes an **admissible reduction** if the partition induced by S' is compatible with the partition induced by S on the relevant admissible domain.

Typically this means that

R_{S'} is a controlled coarsening of R_S.

Informally:

The reduced scope may merge distinctions, but it must not cut across existing regime classes in a way that destroys the structural organization of the system.

---

# 4. Formal Compatibility Condition

Let D be the relevant admissible domain:

D ⊆ X_B ∩ X_{B'}

The reduction S → S' is admissible if

for every x in D

[x]_S ⊆ [x]_{S'}

That is, each regime class in the original partition is contained within a regime class of the reduced partition.

This guarantees that the reduced scope merges regimes but does not fragment them inconsistently.

---

# 5. Interpretation

Under this criterion:

Reduction means that the new scope recognizes fewer distinctions between states, but those distinctions remain aligned with the regime structure discovered in the original scope.

Thus:

Reduction = compatible partition coarsening.

---

# 6. Example: Coupled Pendulum

Consider a two-link planar pendulum.

Initial scope:

Π = {θ₁, θ₂}

The regime structure depends on the motion of both angles.

Under very strong joint stiffness:

θ₁ ≈ θ₂

A collective observable becomes admissible:

Π' = {θ_mode}

The reduced scope becomes

S' = (B', Π', Δ', ε')

If the regime partition produced by S' corresponds to a coarsening of the regime partition produced by S, the reduction is admissible.

If distinctions defined by relative motion remain regime-relevant, the reduction fails.

---

# 7. Reduction vs Scope Reframing

Not every scope transition is a reduction.

Two possibilities exist:

1. Compatible coarsening  
   The reduced scope merges regimes but preserves their structure.

2. Partition mismatch  
   The new scope reorganizes the regime structure entirely.

Only the first case represents admissible reduction.

---

# 8. ARW Reduction Principle

A concise statement:

Reduction should be treated as a scope transition.  
It is admissible when the regime partition induced by the reduced scope remains a compatible coarsening of the regime partition induced by the original scope on the relevant admissible domain.

---

# 9. Consequence for Modeling

This interpretation provides a principled way to evaluate reductions:

Instead of asking whether variables were removed, we ask whether the regime structure remains compatible across scopes.

This aligns reduction directly with the structural comparison of partitions that ARW enables.
