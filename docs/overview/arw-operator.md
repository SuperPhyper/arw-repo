
# ARW Operator

## Overview

The ARW operator is the formal core of the ARW framework.

It maps a **scope specification** to a **robust regime partition**
of the admissible state space.

Importantly, the operator itself makes **no empirical claims**.
It only provides a structural mapping from descriptive conditions
to a partition of states.

---

# Formal Definition

Given a scope

S = (B, Π, Δ, ε)

the ARW operator is defined as

A(S) = R_S

where R_S is the **regime partition** induced by the scope.

---

# Inputs of the Operator

The operator takes a scope consisting of four elements.

## Boundary Constraints (B)

Boundary constraints define the admissible subset of the
state space.

X_B ⊆ X

Only states within this subset are considered by the operator.

---

## Descriptions / Projections (Π)

Π is a family of admissible descriptive mappings

π ∈ Π

Each projection maps system states to a descriptive space
where differences between states can be evaluated.

---

## Admissible Perturbations (Δ)

Δ specifies perturbations under which distinctions must
remain stable.

These perturbations define the **robustness requirement**
for regime formation.

---

## Resolution Threshold (ε)

ε defines the resolution of the scope.

Differences smaller than ε are considered indistinguishable.

---

# Distinguishability

The distinguishability between two states is defined as

d_Π(x, y)

which aggregates distinguishability across all admissible
descriptions in Π.

---

# Robust Indistinguishability

Two states x and y are considered equivalent under scope S if

d_Π(x, y) ≤ ε

and the same relation holds under all admissible perturbations

δ ∈ Δ

This defines the **robust indistinguishability relation**

x ~_S y

---

# Regime Partition

The regime partition produced by the ARW operator is

R_S = X_B / ~_S

This means that all admissible states are grouped into
equivalence classes according to robust indistinguishability.

Each equivalence class represents a **regime** under the
chosen scope.

---

# Interpretation

The ARW operator therefore performs a structural task:

Scope specification → regime partition.

It shows how the chosen boundary conditions, observables,
perturbations, and resolution determine the regime structure
that appears stable.

---

# Conceptual Role

The operator separates:

• **description structure** (ARW)  
from  
• **domain instantiation** (ART)

ARW provides the formal mapping.

ART provides concrete systems, observables, and measurements
that instantiate a scope.
