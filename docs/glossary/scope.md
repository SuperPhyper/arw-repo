
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

Two states become indistinguishable when

d_Π(x, y) ≤ ε

Resolution therefore determines:

- which state differences are detectable
- which observables remain admissible
- how regime partitions are formed.

---

# Role of Scope in ARW

A scope provides the input to the ARW operator.

Given a scope

S = (B, Π, Δ, ε)

the ARW operator produces a **regime partition** of admissible states.

This partition groups states that remain indistinguishable under the
descriptions Π and perturbations Δ within resolution ε.

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
