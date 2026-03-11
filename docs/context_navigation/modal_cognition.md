---
status: working-definition
---

# Modal Cognition

## Definition

Modal cognition is the hypothesis that cognitive processing is organized
into a small set of discrete **modes** — each mode being a reduced scope
S_mode = (B_mode, Π_mode, Δ_mode, ε_mode) that is admissible under a specific
class of environmental boundary conditions.

Rather than a single continuous processing strategy, the agent maintains
a mode ecology: a structured set of scopes, each dominant in a different
context region.

---

## Modes as Reduced Scopes

A mode is not simply a policy or a strategy.
In ARW terms, each mode instantiates a distinct scope:

```
mode mᵢ ≡ S_mᵢ = (B_mᵢ, Π_mᵢ, Δ_mᵢ, ε_mᵢ)
```

| Mode | Dominant scope | Key BC | Observables |
|---|---|---|---|
| Exploration (R_B1) | S_explore | Low cost, high visibility | Local map, coverage, novelty |
| Deliberative (R_B2) | S_deliberate | High cost, planning budget | Full trajectory, error cost, depth |
| Anchor retrieval (R_B3) | S_anchor | Familiar structure, memory | Context embedding, stored anchors |
| Reactive (R_B4) | S_react | Low visibility, no planning | Immediate local observation only |

Each mode suppresses observables that are not relevant under its BC class.
The deliberative mode suppresses novelty and coverage signals — they are below ε_deliberate.
The reactive mode suppresses trajectory-level information — it is outside Π_react.

---

## Mode Identity

Two behavioral trajectories belong to the same mode if:

1. They were generated under the same active scope S_mᵢ
2. Their policy embeddings are within ε_B of each other in latent space
3. They are stable under the same perturbations Δ_mᵢ

Mode identity is therefore defined by partition membership under S_mᵢ,
not by surface behavioral similarity.

**Consequence:** Two trajectories that look different (different paths through the maze)
can belong to the same mode if they are indistinguishable at the level of S_mᵢ.
Two trajectories that look similar can belong to different modes if they are
in different regions of the S_mᵢ partition.

---

## Why Discrete Modes

A single-scope agent (monolithic policy) cannot remain admissible
across BC configurations that require structurally incompatible observables.

Exploration requires: high-coverage signals, novelty-seeking, loose error tolerance.
Deliberation requires: tight error tolerance, planning depth, coverage suppressed.

These are not continuously interpolatable — they require different Π and different ε.
A single scope that tries to track both will lose admissibility in both regions.

Modal cognition solves this by maintaining multiple scopes,
each admissible in its own region, with a selection mechanism (salience + gating)
that activates the appropriate scope for the current context.

---

## Mode Ecology

The full set of modes forms an **ecology** in the sense that:

- modes are mutually exclusive (only one is active at a time)
- modes are complementary (together they cover the full BC space)
- modes compete at scope boundaries (salience reflects this competition)
- the set of modes can evolve through consolidation (new modes emerge; unused modes decay)

The mode ecology is the agent-level instantiation of a regime partition:

```
mode ecology ≅ regime partition R_B
each mode ≅ one regime class Rᵢ ∈ R_B
```

---

## Mode Switching as Scope Transition

When the agent crosses a BC boundary (e.g., from Zone A to Zone B),
the currently active scope S_mᵢ loses admissibility.
The agent must transition to a new scope S_mⱼ.

This is formally a scope transition:

```
S_mᵢ → S_mⱼ
```

Salience is the admissibility-loss signal that detects when S_mᵢ
is failing and competing modes are becoming appropriate.

Mode switching is not a smooth interpolation — it is a discrete
scope transition that reorganizes which observables are tracked
and which perturbations are admitted.

---

## Related Concepts

- [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md)
- [salience_mode_ecology.md](salience_mode_ecology.md)
- [anchor_memory.md](anchor_memory.md)
- [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md)
