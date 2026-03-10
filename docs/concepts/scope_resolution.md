# Scope Resolution

## Overview

Scope resolution describes the minimal distinguishable scale within a
given scope.

In the ARW framework, each scope S includes a resolution threshold ε
that determines which differences between states are considered
distinguishable.

This parameter directly limits which observables can contribute to the
ordering of a system description.

---

# Resolution in the Scope Definition

A scope is defined as

S = (B, Π, Δ, ε)

where

- B defines admissible states
- Π defines admissible descriptions or projections
- Δ defines admissible perturbations
- ε defines the **resolution threshold**

The resolution ε determines the smallest distinguishable difference
between system states under the admissible descriptions.

---

# Distinguishability

For two states x and y, distinguishability is defined through the
combined descriptive family Π.

d_Π(x, y)

represents the maximal distinguishability across admissible
descriptions.

Two states become indistinguishable when

d_Π(x, y) ≤ ε

In that case they belong to the same regime class of the scope.

---

# Role in Partition Formation

Scope resolution directly determines the induced partition of the
state space.

States that remain indistinguishable under resolution ε are grouped
into the same regime class.

The ARW operator therefore produces a regime partition

R_S = X_B / ~_S

where the indistinguishability relation depends explicitly on ε.

Changing ε changes the partition structure.

---

# Resolution and Observable Admissibility

The resolution of a scope determines which observables remain
admissible.

An observable is admissible when its relevant dynamical effects remain
distinguishable above the resolution threshold.

If the effects of an observable fall below ε:

- it becomes indistinguishable within the scope
- it cannot contribute to the ordering of the description
- it becomes effectively latent.

---

# Resolution and Scope Stability

A scope remains useful only as long as the observables required to
stabilize the description operate above the resolution threshold.

If critical observables fall below the scope resolution:

- regime structure becomes unstable
- partitions collapse or fragment
- a different scope may become necessary.

---

# Conceptual Summary

Scope resolution ε determines:

- which state differences are distinguishable
- which observables are admissible
- how regime partitions are formed.

It therefore acts as the structural boundary between:

observable structure

and

latent dynamics.
