---
status: working-definition
layer: docs/cognitive_architecture/
---

# Modal Cognition

## Definition

Modal cognition is the hypothesis that cognitive processing is organized
into a small set of discrete **modes** — each mode being a **regime in S_global**,
i.e. a stable partition cell that is admissible under a specific class of
environmental boundary conditions.

**Revision note (see `docs/context_navigation/mode_scope_regime_audit.md` §1.3):**
Modes are *not* independent scope tuples (B_mode, Π_mode, Δ_mode, ε_mode).
They are regime cells in the partition of S_global. The observables Π_m and
resolution threshold ε_m that characterize a mode are properties of the
regime R_m as a sub-scope grounded in S_global's partition — not components
of a separately constituted scope. A mode exists only as long as the partition
in S_global supports it.

Rather than a single continuous processing strategy, the agent maintains
a mode ecology: a structured regime partition of S_global, each regime
dominant in a different region of parameter space.

---

## Modes as Regimes in S_global

A mode is not simply a policy or a strategy.
In ARW terms, each mode is a **regime (stable partition cell) in S_global**:

```
mode mᵢ ≡ R_mᵢ  ∈  partition(S_global)
```

Each regime R_mᵢ is characterized by the subset Π_mᵢ ⊆ Π of observables
that remain within their observable range R(π) at parameter points inside R_mᵢ,
and by the dominant BC class of the boundary conditions active in that region.
These are *properties of the regime*, not independent scope components.

| Mode | Regime label | Dominant BC class | Active observables Π_m |
|---|---|---|---|
| Exploration (R_B1) | R_explore | Low restriction | Local map, coverage, novelty |
| Deliberative (R_B2) | R_deliberate | High restriction | Full trajectory, error cost, depth |
| Anchor retrieval (R_B3) | R_anchor | Coupling (memory) | Context embedding, stored anchors |
| Reactive (R_B4) | R_react | Restriction (low visibility) | Immediate local observation only |

Each mode corresponds to a region in S_global's partition where certain observables
are admissible (within R(π)) and others are not. The deliberative mode is the
partition cell where novelty and coverage signals have exited their valid range.
The reactive mode is the cell where trajectory-level observables lie outside Π_m.

---

## Mode Identity

Two behavioral trajectories belong to the same mode if:

1. They were generated within the same regime cell R_mᵢ of S_global's partition
2. Their policy embeddings are within ε_mᵢ of each other in the observable space of Π_mᵢ
3. They are stable under the same perturbations Δ (the global perturbation class)

Mode identity is therefore defined by **regime-cell membership in S_global**,
not by surface behavioral similarity and not by an independent scope comparison.

**Consequence:** Two trajectories that look different (different paths through the maze)
can belong to the same mode if they are indistinguishable at the level of Π_mᵢ within R_mᵢ.
Two trajectories that look similar can belong to different modes if they are
in different partition cells of S_global.

---

## Why Discrete Modes

A single-regime agent (monolithic policy) cannot remain admissible
across BC configurations that require structurally incompatible observables.

Exploration requires: high-coverage signals, novelty-seeking, loose error tolerance.
Deliberation requires: tight error tolerance, planning depth, coverage suppressed.

These are not continuously interpolatable — they correspond to different partition
cells in S_global, each with a different active observable set Π_m and resolution
scale ε_m. A monolithic policy that tries to remain valid in both regions will
have observables that violate R(π) in one region, entering the exclusion zone Z(π).

Modal cognition solves this by constituting S_global such that its partition
contains these structurally distinct regime cells, with a selection mechanism
(salience + gating) that identifies the current cell.

---

## Mode Ecology

The full set of modes forms an **ecology** in the sense that:

- modes are mutually exclusive (only one regime cell is active at a time)
- modes are complementary (together they tile the relevant region of parameter space)
- modes compete at regime boundaries (salience reflects this competition)
- the set of modes can evolve through consolidation (new partition cells emerge; unused ones decay)

The mode ecology *is* the regime partition of S_global at the agent-behavior level:

```
mode ecology ≅ partition(S_global)
each mode    ≅ one regime cell Rᵢ ∈ partition(S_global)
```

---

## Mode Switching as Regime Transition

When the agent's parameter point p moves across a partition boundary in S_global
(e.g., from Zone A to Zone B), the currently active regime cell R_mᵢ is no longer
the cell p occupies. The agent must identify the new cell R_mⱼ.

This is formally a **regime transition within S_global** (not a scope transition):

```
R_mᵢ → R_mⱼ    within partition(S_global)
```

**Distinction from scope transition:** A scope transition would mean S_global
itself becomes invalid — all observables in Π enter their exclusion zone Z(π),
and the descriptive framework breaks down entirely. Mode switching does not
involve S_global failure. See `docs/context_navigation/mode_scope_regime_audit.md` §2.3.

Salience is the signal that the current parameter point p is approaching
the boundary between regime cells — where admissibility of the active mode's
observables begins to degrade (p approaching Z(π_mᵢ)).

Mode switching is not a smooth interpolation — it is a discrete
transition that reorganizes which observables are active and valid
at the agent's current parameter point.

---

## Related Concepts

- [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md)
- [salience_mode_ecology.md](salience_mode_ecology.md)
- [anchor_memory.md](anchor_memory.md)
- [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md)
