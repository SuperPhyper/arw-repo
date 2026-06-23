---
status: working-definition
layer: docs/glossary/
last_updated: 2026-06-10
---


# Scope

## Overview

In the ARW framework, a **scope** defines the descriptive conditions under which
a system is analyzed. It specifies the admissible states, the descriptive
projections, the admissible perturbations, and the resolution threshold that
determines distinguishability.

A scope therefore determines **how a system can be described**, rather than
what the system intrinsically is.

---

# Formal Definition

A scope is defined as the tuple

S = (B, Π, Δ, ε)

where

- **B** : boundary constraints selecting admissible states
- **Π** : admissible descriptions or projections (observables)
- **Δ** : admissible perturbations
- **ε** : resolution threshold

Together, these parameters define the descriptive regime under which
system states are compared and organized.

---

# The Structured State Space X (Meta-Assumption)

The tuple S presupposes a state space X with enough structure — topology,
a metric on the observable image, smoothness of the dynamics where an
observable requires it — for the projections in Π to be well-defined.
This structure is **not** part of the scope tuple, and it is **not**
declared by B: B selects X_B ⊆ X; it does not define the structure of X.

By architectural decision (2026-06-10; Q_NEW_1 in
[open_questions.md](../notes/open_questions.md)), the structure of X
belongs to the **ART layer**: each domain instantiation (ScopeSpec /
signature-first document) declares the state-space structure its
observables require, as part of the pre-scopal substrate conditions
(A0–A6; see [observable_decomposition.md](../advanced/observable_decomposition.md)).
ARW-core statements are therefore conditional on a well-defined X, and
that conditionality is made explicit at the ART level rather than
absorbed into the tuple.

---

# Components of a Scope

## B — Boundary Constraints

Boundary constraints define which states of the underlying state space
are considered admissible.

Formally, they select a subset

X_B ⊆ X

of the structured state space.

Examples include:

- physical constraints
- environmental conditions
- modeling assumptions
- domain-specific restrictions

Boundary conditions therefore determine the **domain of the scope**.

---

## Π — Descriptions / Projections

Π defines the family of admissible **descriptions** or **observables**
used to analyze the system.

Each projection

π ∈ Π

maps system states to a descriptive space.

These projections determine which aspects of the system are visible
within the scope.

Different choices of Π correspond to different descriptive regimes.

---

## Δ — Admissible Perturbations

Δ defines the set of perturbations that are considered admissible
within the scope.

These perturbations determine the robustness conditions under which
descriptive distinctions must remain stable.

Perturbations may represent:

- measurement noise
- environmental variation
- bounded interventions
- modeling uncertainty

Robust partitions must remain stable under these perturbations.

---

## ε — Resolution Threshold

ε defines the **resolution of the scope**.

It determines the smallest distinguishable difference between system
states under the admissible descriptions.

Two states are pairwise indistinguishable when

d_Π(x, y) ≤ ε

Pairwise indistinguishability alone, however, does not define a partition:
the relation is not transitive — a chain of sub-ε steps can connect states
that are arbitrarily far apart (the sorites problem in measurement form).
The canonical construction (INC-01 upgrade, 2026-06-10; Felder 2026) is
therefore the **observable cover**: regimes are the path-connected components
of the cover C_ε of the observable image — maximal regions whose states are
mutually reachable through sub-ε steps. Distinct regimes exist exactly where
the observable image has gaps or jumps larger than ε. Regime membership must
additionally be stable under Δ (cover stability; see
[cover_stability_criterion.md](../core/cover_stability_criterion.md)).
The pairwise relation d_Π(x, y) ≤ ε defines adjacency *within* the cover;
it is not itself the equivalence that yields regimes.

Resolution therefore determines:

- which state differences are detectable
- which observables remain admissible
- how regime partitions are formed.

For a fixed scope skeleton (B, Π, Δ), ε is not a single correct value
but admits an **admissible ε-interval** I_ε = [ε_min, ε_max] — the range
of resolution values under which the partition structure (regime count,
adjacency graph) remains invariant. The width of this interval measures
scope robustness. See [epsilon_and_scope_resolution.md](../advanced/epsilon_and_scope_resolution.md) § 4.

---

# Role of Scope in ARW

A scope provides the input to the ARW operator.

Given a scope

S = (B, Π, Δ, ε)

the ARW operator produces a **regime partition** of admissible states.

This partition groups states into the connected components of the
observable cover at resolution ε — states mutually reachable through
sub-ε steps under the descriptions Π, with membership stable under the
perturbations Δ.

---

# Conceptual Role

A scope represents a **descriptive regime** rather than an intrinsic
property of a system.

Different scopes applied to the same underlying system may produce:

- different regime structures
- different observable relations
- different stability properties.

The ARW framework therefore studies how **scope choices shape the
structures that appear stable within a description**.
