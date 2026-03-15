---
status: working-definition
layer: docs/core/
---

# Basins as Scope Partitions

## Overview

Within ARW, basins of attraction are not intrinsic dynamical objects.
They are **scope-relative structures** — they appear, merge, split, or disappear
depending on which observables are tracked and at what resolution.

This document makes precise the relationship between dynamical basins
and ARW regime classes: when they coincide, when they diverge,
and what the divergence reveals.

---

## 1 The Standard Account and Its Limit

In classical dynamical systems theory, a basin of attraction is the set of
initial conditions that converge to a given attractor under the system's dynamics.

```
Basin(A) = { x₀ ∈ X | φ_t(x₀) → A as t → ∞ }
```

This definition is intrinsic — it depends only on the dynamics, not on
how the system is observed.

**The ARW challenge:** Two systems with identical basin structure can produce
different observable regime structures depending on which observables are tracked.
And conversely, a scope change can make a basin appear, disappear, or split —
without changing the underlying dynamics at all.

Basins are not simply "given" by the system. They are visible or invisible
depending on the scope.

---

## 2 When a Basin Is an ARW Regime Class

A dynamical basin Basin(A) coincides with an ARW regime class [x]_S when:

**Condition 1 — Observable resolution:**
The observables Π contain at least one function that distinguishes
the attractor A from all other attractors:

```
∃ π ∈ Π, ∃ A' ≠ A: |π(A) - π(A')| > ε
```

If no observable resolves the distinction, all basins collapse into one regime class.

**Condition 2 — Perturbation stability:**
The basin boundary is robust under Δ — small perturbations do not move
initial conditions across basin boundaries:

```
∀ x ∈ Basin(A), ∀ δ ∈ Δ: x + δ ∈ Basin(A)   (for bulk states)
```

If perturbations in Δ routinely cross basin boundaries, basin identity
is not stable under the scope's noise model — the scope is too coarse
to resolve the basin structure.

**When both conditions hold:**
```
Basin(A) = [x]_S   for all x ∈ Basin(A) (away from basin boundary)
```

The ARW regime class and the dynamical basin are the same object,
described from two different angles.

---

## 3 When They Diverge: Four Cases

### Case 1 — Observable below resolution

The attractor A exists dynamically, but the observable difference between
A and A' is below ε:

```
|π(A) - π(A')| < ε   for all π ∈ Π
```

**Effect:** Basin(A) and Basin(A') merge into a single regime class.
The scope cannot distinguish them — they appear as one regime.

**Example:** In the Kuramoto model under the mean-field scope (Π = {r(t)}),
individual oscillator attractors are below resolution.
All partially synchronized states with the same r value are one regime class,
even though individual oscillator configurations are dynamically distinct.

**ARW interpretation:** This is admissible aggregation — the scope is
deliberately coarser than the basin structure. Not a flaw; a design choice.

---

### Case 2 — Perturbation crosses basin boundary

Basin boundaries are fractal or highly convoluted, such that
typical perturbations δ ∈ Δ can move states across boundaries:

```
∃ x ∈ Basin(A), ∃ δ ∈ Δ: x + δ ∈ Basin(A')
```

**Effect:** Basin identity is unstable under the scope's noise model.
States near the basin boundary cannot be assigned a stable regime class.
The partition is well-defined in the bulk but diffuse at boundaries.

**Example:** Near the chaotic regime in the driven pendulum, basin boundaries
become fractal. Small perturbations (within Δ) can lead to qualitatively
different long-term behavior. The ARW regime class for these states is
structurally ambiguous — [x]_S is not well-defined.

**ARW interpretation:** This is the formal signal that the scope S is losing
admissibility in the boundary region. Chaos in ARW terms is not a property
of the system — it is a property of the scope-system relationship:
the scope's Δ is too large relative to the basin boundary width.

---

### Case 3 — Scope observable reorganizes the partition

A new observable π' is added to Π that cuts across basin boundaries —
it distinguishes states within the same basin that are dynamically equivalent.

```
∃ x, y ∈ Basin(A): |π'(x) - π'(y)| > ε
```

**Effect:** A single dynamical basin splits into multiple regime classes.

**Example:** In the labyrinth agent, two trajectories may converge to the
same policy attractor (same mode) but have different anchor memory states.
Adding anchor_state to Π splits the basin: two regime classes emerge
within what was previously one.

**ARW interpretation:** This is partition refinement — the new scope
reveals structure that was latent under the coarser Π.
It is admissible as long as the refinement is compatible in the other direction:
the old regime class is fully contained in the union of the new classes.

---

### Case 4 — No attractor, but stable regime class exists

A regime class [x]_S is stable under Δ, but there is no corresponding
dynamical attractor — the system does not converge to a fixed point or limit cycle,
but the observable pattern is stable.

**Example:** The quasi-periodic regime R_P2 in the pendulum has no attractor
in the classical sense (the trajectory fills a torus). But under scope S_P,
the observable signature (incommensurate frequencies, no chaos) is stable
under small perturbations. It is a regime class without a point attractor.

**ARW interpretation:** Regime classes are more general than basins.
A regime class requires only observable stability under Δ, not dynamical
convergence to a fixed set. The ARW framework subsumes the basin concept
as a special case.

---

## 4 The Formal Relationship

Summarizing the four cases:

```
Basin(A) ≡ [x]_S        when Conditions 1 and 2 hold (standard case)
Basin(A) = ∅ in R_S      when attractor is below ε (Case 1)
[x]_S diffuse at ∂Basin  when Δ crosses boundary (Case 2)
Basin(A) splits in R_S   when new π cuts across basin (Case 3)
[x]_S exists, no basin   when regime is quasi-periodic or non-attracting (Case 4)
```

The general statement:

> Basins are a sufficient but not necessary condition for ARW regime classes.
> Every basin (where Conditions 1 and 2 hold) generates a regime class.
> But not every regime class corresponds to a basin.

---

## 5 Consequence for the Experimental Program

This analysis has direct consequences for how the partition extraction
pipeline handles each experimental system:

| System | Basin structure | Scope condition | Expected relationship |
|---|---|---|---|
| Kuramoto (large N) | Well-defined basins in θ-space | Π = {r(t)} suppresses individual θᵢ | Case 1: basins merge under mean-field scope |
| Pendulum (driven) | Fractal boundaries near chaos | Δ = small perturbations | Case 2: boundary states are scope-ambiguous |
| Pendulum (quasi-periodic) | No attractor (torus) | Π = {θ₁, θ₂} resolves frequencies | Case 4: regime class without basin |
| Labyrinth (anchor memory) | Policy attractors in latent space | Anchor state added to Π | Case 3: single basin splits by memory state |

---

## 6 Connection to the Admissibility Criterion

The basin-scope relationship clarifies when the admissibility criterion
[x]_S ⊆ [x]_S' is guaranteed vs. requires checking:

- **Case 1** (basins below resolution): admissibility holds automatically —
  the coarser scope merges basins but does not fragment them.
- **Case 2** (fractal boundaries): admissibility may fail at boundary states —
  these are the primary source of PCI < 1 near regime transitions.
- **Case 3** (partition refinement): admissibility holds in the direction
  fine → coarse, but not coarse → fine by definition.
- **Case 4** (regime without basin): admissibility must be checked directly —
  no dynamical shortcut is available.

---

*For the admissibility criterion, see [arw_scope_reduction_partition_criterion.md](arw_scope_reduction_partition_criterion.md).*
*For distortion metrics at basin boundaries, see [docs/bc_taxonomy/transfer_distortion_metrics.md](../bc_taxonomy/transfer_distortion_metrics.md).*
*For the pendulum instantiation (Cases 2 and 4), see [experiments/multi_link_pendulum.md](../../experiments/multi_link_pendulum.md).*
