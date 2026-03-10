
# ε as Resolution Window

## Purpose

This note clarifies the interpretation of **ε** in the ARW scope definition

S = (B, Π, Δ, ε)

Rather than treating ε strictly as a single scalar tolerance value, it is often
more accurate to interpret ε as a **resolution window** describing the range of
variations under which behavior remains indistinguishable within the scope.

This clarification preserves the original ARW operator while making its use in
real systems more explicit.

---

# Original Role of ε

In the minimal ARW formulation, ε defines the **resolution of observation**.

Two states x and y are considered equivalent within scope S if their observable
differences remain below ε.

Informally:

|Π(x) − Π(y)| < ε

This captures the idea that a scope cannot distinguish arbitrarily small
differences.

---

# Motivation for the Resolution Window Interpretation

In many real systems, regime stability is not defined by a single threshold but
by a **robust interval**.

Examples include:

- stable laser operation windows
- control parameter ranges
- stability domains in dynamical systems
- tolerance ranges in engineering systems

Within such regions, behavior remains qualitatively unchanged despite parameter
variation.

This motivates interpreting ε as a **region of admissible variation** rather
than a single tolerance value.

---

# Extended Interpretation

Instead of

ε ∈ ℝ⁺

we can interpret

ε = admissible resolution window

or more generally

ε ⊂ parameter / observable space

Under this interpretation, two states are equivalent if their observable
differences remain within this window.

---

# Relation to Perturbations Δ

Within ARW:

Δ describes the **set of admissible perturbations**.

ε describes the **magnitude range** under which those perturbations do not
change the qualitative behavior of the system.

Together they define the robustness condition:

Perturbations δ ∈ Δ whose effect lies within ε preserve behavioral equivalence.

---

# Connection to Regime Stability

A behavioral regime can be interpreted as a region in which

system behavior remains invariant under perturbations within ε.

Transitions between regimes occur when system parameters move outside the
admissible ε-window.

---

# Example: ECDL Laser Modes

In an external cavity diode laser (ECDL), stable single-mode operation occurs
within a finite region of parameter space.

For example:

- injection current window
- temperature window
- cavity length tuning range

Within these ranges the system remains single-mode. Outside them the system
transitions to multi-mode operation or experiences mode hops.

These regions correspond naturally to **ε-resolution windows** within the ARW
scope.

---

# Relation to Emergence

Variables become **inadmissible** when their effects fall below the resolution
defined by ε.

When this occurs, different microstates become indistinguishable within the
scope and collapse into a single behavioral equivalence class.

This mechanism contributes to the emergence of higher-level regimes.

---

# Summary

Interpreting ε as a **resolution window** rather than a strict scalar threshold

- preserves the minimal ARW formalism
- better reflects real experimental systems
- aligns with regime stability concepts in dynamical systems
- clarifies the relationship between admissibility and emergence

The ARW operator therefore remains unchanged while its practical interpretation
is strengthened.
