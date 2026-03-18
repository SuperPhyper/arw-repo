---
status: working-definition
layer: docs/advanced/
related_docs:
  - docs/advanced/bc_relative_observable_indistinguishability.md
  - docs/advanced/mathematical_scope_boundary.md
---

# Epsilon-Induced Scope Families

## Overview

In ARW, scopes are not static objects but arise as **families parameterized by ε**.

This document formalizes BC-relative scope families.

---

# 1. Local Scope Definition

For BC α and scale δ:

S_α(δ; b) =
(
  N_α^δ(b),
  O,
  Δ,
  τ_α
)

This is a **local scope** centered at b.

---

# 2. Scope Family

Define the scope family:

𝒮_α(b) = { S_α(δ; b) | δ ∈ I_α(b) }

where I_α(b) is an admissible ε-interval.

---

# 3. Observable Collapse

A collapse occurs if:

Δ_α O(b; δ) ≤ τ_α(b; δ)

for δ in I_α(b).

Interpretation:

- Observable becomes **indistinguishable along BC α**
- Local structure is removed

---

# 4. Key Insight

Scopes are not single objects but:

> **trajectories through resolution space**

Thus:

- ε does not define a partition alone
- ε defines a **family of partitions**

---

# 5. ARW Interpretation

This formalizes:

- Scope = function of ε
- Structure = persistence across ε

This connects directly to regime stability and persistence.
