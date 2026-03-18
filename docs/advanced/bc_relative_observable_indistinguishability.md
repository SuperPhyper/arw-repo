---
status: working-definition
layer: docs/advanced/
related_docs:
  - docs/advanced/mathematical_scope_boundary.md
  - docs/advanced/minimal_operator_basis_arw.md
---

# BC-Relative Observable Indistinguishability

## Overview

This document introduces a **boundary-condition-relative notion of observable indistinguishability**.

The central idea is:

> Observables are not globally indistinguishable under a single ε,
> but become indistinguishable **relative to specific boundary conditions (BCs)**.

This allows different BC directions to collapse local observable structure
while preserving relational or coupled structure.

---

# 1. Setup

Let

B = B₁ × ... × B_m

be the boundary condition space, and

O : B → 𝒪

an observable.

Let b ∈ B be a reference point.

---

# 2. BC-Relative Neighborhood

For a BC component α, define the neighborhood:

N_α^δ(b) = {
  b' ∈ B |
  b'^(β) = b^(β) for β ≠ α,
  d_α(b'^(α), b^(α)) ≤ δ
}

This isolates variation along a single BC.

---

# 3. BC-Induced Observable Variation

Define the local observable variation:

Δ_α O(b; δ) =
  sup_{b' ∈ N_α^δ(b)} d_𝒪(O(b'), O(b))

Interpretation:

- Measures how strongly BC α influences O locally
- Independent of parametrization order
- Intrinsic to BC geometry

---

# 4. BC-Relative Indistinguishability

Given a resolution function τ_α(b; δ), define:

b ~_α^δ b'
iff

1. b' ∈ N_α^δ(b)
2. d_𝒪(O(b), O(b')) ≤ τ_α(b; δ)

This defines a **BC-relative equivalence relation**.

---

# 5. Interpretation

This construction implies:

- Indistinguishability is **direction-dependent in BC space**
- Different BCs induce different observable collapse regimes
- Observable structure is not absolute but **BC-relative**

This forms the basis for ARW emergence.
