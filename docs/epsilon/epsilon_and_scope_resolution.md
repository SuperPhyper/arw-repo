
# ε and Scope Resolution

## Purpose

This document clarifies the relationship between **ε (epsilon)** and **scope resolution** in the
ARW framework.

In ARW a scope is defined as:

S = (B, Π, Δ, ε)

Where ε determines the **resolution at which observable differences are considered meaningful**.

---

# ε as Resolution of a Scope

A scope cannot distinguish arbitrarily small differences.

ε therefore represents the **minimum observable distinction** within that scope.

Two states are indistinguishable if:

|Π(x) − Π(y)| < ε

In this case they belong to the same behavioral equivalence class.

---

# Resolution as a Property of the Scope

Scope resolution determines which observables remain admissible.

If a variable produces changes smaller than ε, it becomes **inadmissible within the scope**.

This produces a reduction of effective degrees of freedom.

Formally:

observable effect < ε  
→ observable becomes latent

---

# Connection to Emergence

Emergence occurs when micro-level distinctions fall below scope resolution.

When variables become inadmissible, many microstates collapse into the same equivalence class.

This produces a **higher-level regime description**.

Example:

Microscopic states: many laser cavity configurations

Observable behavior: single-mode output

Within the scope, these microstates collapse into one behavioral regime.

---

# Scope Transitions

Changing ε effectively changes the scope.

Increasing ε:

- reduces the number of distinguishable observables
- merges behavioral classes
- produces higher-level regimes

Decreasing ε:

- reveals finer distinctions
- splits regimes into sub-regimes

Thus ε controls the **granularity of the regime partition**.
