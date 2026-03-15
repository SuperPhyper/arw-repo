---
status: hypothesis
layer: docs/overview/
---

# Minimal Example: The Two-Link Pendulum

This document walks through a single concrete example of ARW in action.
No prior knowledge of the framework is required.

---

## The System

A two-link planar pendulum — two rigid rods connected in series, free to swing.

The system has two degrees of freedom: the angle of the first link (θ₁)
and the angle of the second link (θ₂).

Depending on how it is driven, it can exhibit very different behaviors:
regular oscillation, quasi-periodic motion, or chaos.

---

## Step 1 — Define a Scope

In ARW, before analyzing a system we must specify a **scope**:

```
S = (B, Π, Δ, ε)
```

For this example:

| Parameter | Choice | Meaning |
|---|---|---|
| **B** | bounded energy, fixed pivot | only physically realizable motions |
| **Π** | {θ₁, θ₂} | we observe both joint angles |
| **Δ** | small perturbations to initial conditions | robustness under noise |
| **ε** | 0.05 rad | differences smaller than this are indistinguishable |

This scope says: *we describe the pendulum by watching both angles, under small perturbations, at moderate resolution.*

---

## Step 2 — Extract the Regime Partition

The ARW operator applies this scope to the system's state space
and groups states that behave indistinguishably under S:

```
A(S) = R_S
```

With scope S = ({θ₁, θ₂}, ...), three regime classes emerge:

| Regime | Behavior |
|---|---|
| R₁ | Periodic — both links oscillate regularly |
| R₂ | Quasi-periodic — incommensurable frequencies, no chaos |
| R₃ | Chaotic — sensitive dependence, trajectory divergence |

These regimes are separated by **transition boundaries** in the
parameter space (e.g., driving frequency, coupling strength).

---

## Step 3 — Change the Scope

Now suppose the joint coupling becomes very stiff: θ₁ ≈ θ₂ at all times.
Under this condition, the relative angle carries no useful information.

A reduced scope becomes admissible:

```
S' = (B', Π', Δ', ε')
```

| Parameter | New choice |
|---|---|
| **Π'** | {θ_mode} — a single collective angle |
| **B'** | stiff-coupling constraint added |

The ARW operator now produces a coarser partition:

```
A(S') = R_S'
```

R₁ and R₂ merge into a single "ordered motion" class.
R₃ may persist or also collapse, depending on coupling strength.

---

## Step 4 — Apply the Admissibility Criterion

Is S → S' an **admissible reduction**?

ARW's partition compatibility criterion requires:

```
for every x: [x]_S ⊆ [x]_S'
```

Each regime class under S must be fully contained within
a regime class under S'.

**If the coupling is strong enough:** R₁ ⊆ R_ordered and R₂ ⊆ R_ordered.
The reduction is admissible — the reduced scope captures the same structure.

**If the coupling is too weak:** Trajectories from R₁ and R₃ mix in S'.
The reduction is inadmissible — the reduced scope destroys structural information.

---

## What ARW Makes Visible

Without ARW, one might simply say: *"the reduced model works when coupling is strong."*

ARW makes this precise:

- **When** a reduction is valid = when partition compatibility holds
- **What is lost** = which regime distinctions are collapsed
- **How to measure failure** = degree of partition mismatch between R_S and R_S'

This is the core analytical contribution: a structural criterion for
when a simpler description remains faithful to the original.

---

## Summary

```
Full scope S         →   3 regimes {R₁, R₂, R₃}
Reduced scope S'     →   2 regimes {R_ordered, R_chaotic}
Admissibility check  →   R₁ ⊆ R_ordered ✓   R₂ ⊆ R_ordered ✓
Reduction verdict    →   admissible under strong coupling
```

The pendulum example demonstrates ARW in its minimal operational form:
scope definition, regime extraction, scope transition, and admissibility check.

---

*For the full formal treatment, see [docs/core/arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md).*
*For the experimental design based on this system, see [experiments/multi_link_pendulum.md](../../experiments/multi_link_pendulum.md).*
