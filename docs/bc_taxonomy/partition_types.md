---
status: working-definition
---

# Partition Types

This document defines the ARW typology of regime partition structures.
Each partition type is a characteristic structural form that recurs
across systems with similar BC classes.

The typology is the other half of the BC taxonomy:

```
BC class  →  generates  →  partition type
```

See [boundary_condition_classes.md](boundary_condition_classes.md) for the BC side
and [bc_class_to_regime_type_map.md](bc_class_to_regime_type_map.md) for the
explicit mapping between the two.

---

## Formal Setup

Given A(S) = R_S, a partition type characterizes the *structural form* of R_S:

- How many regime classes does it contain?
- How are they arranged relative to each other?
- What is the topology of transitions between them?
- How do boundaries behave under perturbation?

Two systems have the same partition type if their regime graphs are isomorphic
under the ARW operator — regardless of the physical domain.

---

## Type 1 — Binary Partition

**Structure:** Two regime classes, one transition boundary.

```
R = { R₁, R₂ }
```

**Regime graph:**
```
R₁ ←→ R₂
```

Bidirectional transition is possible (forward and reverse as parameter varies).

**Characteristic properties:**
- Single control parameter drives the transition
- Transition boundary is a codimension-1 surface in parameter space
- Partitions are symmetric or asymmetric depending on BC class

**Generating BC classes:** Coupling (below/above K_c), Restriction (below/above saturation)

**Instantiations:**

| System | Binary partition | Control parameter |
|---|---|---|
| Kuramoto (large N) | Incoherent / Synchronized | Coupling K across K_c |
| Pendulum (stiff coupling) | Ordered / Chaotic | Driving amplitude A |
| Opinion dynamics (large ε_bc) | Consensus / Polarized | Confidence bound ε_bc |

**Distortion under aggregation:**
Binary partitions are the most stable under aggregation — both classes
are typically large enough to survive coarse-graining.
Boundary-straddling states are the only distortion zone.

---

## Type 2 — Sequential (Ordered) Partition

**Structure:** Multiple regime classes arranged in a linear sequence,
each accessible from its neighbors but not by direct jumps.

```
R = { R₁, R₂, R₃, ... }
```

**Regime graph:**
```
R₁ → R₂ → R₃ → ...
```

Directed or bidirectional, depending on reversibility.

**Characteristic properties:**
- Ordered along a single control dimension (coupling strength, resource level)
- Intermediate regimes exist that are not simple combinations of extremes
- Transition sequence is predictable from BC structure

**Generating BC classes:** Coupling (incoherent → partial → full), Forcing (sub- → resonant → chaotic)

**Instantiations:**

| System | Sequential partition | Sequence |
|---|---|---|
| Kuramoto | Three-regime | Incoherent → Partial sync → Full sync |
| Pendulum | Three-regime | Periodic → Quasi-periodic → Chaotic |
| Opinion dynamics | Four-regime | Consensus → Polarized → Fragmented → Frozen |
| Escalation ladder (geopolitics) | Six-regime | R_A1 → R_A2 → R_A3 → ... → R_A6 |

**Distortion under aggregation:**
Intermediate regimes (R₂, R₃) are most vulnerable.
Aggregation tends to merge them into the nearest extreme,
producing apparent binary or tertiary partitions.

---

## Type 3 — Clustered Partition

**Structure:** Multiple regime classes that form groups — clusters of regimes
with dense internal transitions and sparse inter-cluster transitions.

```
R = { {R₁₁, R₁₂, ...}, {R₂₁, R₂₂, ...}, ... }
```

**Regime graph:**
```
Cluster A: R₁₁ ↔ R₁₂ ↔ R₁₃
                              ↕ (rare)
Cluster B: R₂₁ ↔ R₂₂
```

**Characteristic properties:**
- Intra-cluster transitions are frequent and low-cost
- Inter-cluster transitions require large perturbations or BC changes
- Cluster identity is more stable than individual regime identity
- The number of clusters is determined by BC class; the intra-cluster structure by ε

**Generating BC classes:** Coupling (network topology → sub-communities),
Symmetry breaking (multiple equivalent attractors), Restriction (multiple saturation levels)

**Instantiations:**

| System | Clustered partition | Clusters |
|---|---|---|
| Kuramoto (network coupling) | Two-level | Individual oscillator regimes within global sync clusters |
| Opinion dynamics (modular network) | Community clusters | Each network community forms an opinion cluster |
| Labyrinth agent | Mode ecology | {Exploration, Reactive} (low-planning cluster) vs. {Deliberative, Anchor-retrieval} (high-planning cluster) |

**Distortion under aggregation:**
Aggregation collapses intra-cluster structure — the cluster appears as a single regime.
This is the primary source of RCD (regime count discrepancy) in cross-scope comparison.

---

## Type 4 — Multi-stable Partition

**Structure:** Multiple coexisting stable regime classes for identical BC parameters.
Which regime is active depends on history (initial conditions or prior trajectory).

```
R = { R₁, R₂, R₃ }   all stable at same BC parameter values
```

**Regime graph:**
```
R₁   R₂   R₃   (no transitions under small perturbations)
```

**Characteristic properties:**
- Hysteresis: the system's current regime depends on its history
- Transitions require large perturbations (exceeding Δ)
- Basin of attraction structure determines accessibility
- Parameter change can eliminate regimes (basin merging)

**Generating BC classes:** Dissipation + Forcing (driven-dissipative multi-stability),
Coupling below K_c (multiple equivalent fixed points)

**Instantiations:**

| System | Multi-stable partition | Stable regimes |
|---|---|---|
| Pendulum (bistable driving) | Two coexisting stable orbits | Period-1 and Period-2 orbits at same (A, Ω) |
| Geopolitical system | Containment vs. escalation | Both A1 and A2 stable; trajectory-dependent |
| Agent anchor memory | Multiple valid context-mode mappings | Different anchor configurations for same environment |

**Distortion under aggregation:**
Multi-stable partitions are severely distorted by aggregation —
the population-level average obscures which regime individual
trajectories are in. The mean-field description sees a "mixed" state
rather than distinct coexisting regimes.

---

## Type 5 — Hierarchical Partition

**Structure:** A partition with levels — coarse classes at the top,
each containing a finer sub-partition.

```
R_coarse = { C₁, C₂ }
R_fine   = { C₁: {R₁₁, R₁₂}, C₂: {R₂₁, R₂₂, R₂₃} }
```

**Regime graph:**
```
Coarse level: C₁ ←→ C₂
Fine level:   R₁₁ ↔ R₁₂   (within C₁)
              R₂₁ ↔ R₂₂ ↔ R₂₃   (within C₂)
```

**Characteristic properties:**
- Coarse structure is stable under large perturbations
- Fine structure is visible only under high-resolution scope
- The hierarchy is generated by ε: low ε reveals fine structure, high ε collapses it
- Scope transitions correspond to moving between levels

**Generating BC classes:** Any combination + ε variation;
Aggregation applied hierarchically

**Instantiations:**

| System | Hierarchical partition | Levels |
|---|---|---|
| Labyrinth (cell/zone/episode) | Three-level | Cell-level moves → zone-level strategies → episode-level outcome |
| Geopolitical (actor/system) | Two-level | Actor regimes (R_A1–R_A6) within system regimes (R_G1–R_G3) |
| Kuramoto (oscillator/cluster) | Two-level | Individual phase regimes within global sync classes |

**Distortion under aggregation:**
Moving from fine to coarse level is admissible when partition compatibility holds.
The hierarchical type makes the admissibility condition most transparent:
each coarse class must contain complete fine classes, not split them.

---

## Partition Type Properties Summary

| Type | Classes | Regime graph | Multi-stable? | Key BC class |
|---|---|---|---|---|
| Binary | 2 | Linear | No | Coupling, Restriction |
| Sequential | ≥ 3, ordered | Linear chain | No | Coupling, Forcing |
| Clustered | ≥ 4, grouped | Two-level graph | Rare | Network coupling, Sym. breaking |
| Multi-stable | ≥ 2, coexisting | Disconnected | Yes | Dissipation + Forcing |
| Hierarchical | Multi-level | Nested | Possible | ε variation, Aggregation |

---

## Partition Type Under Scope Transition

When a scope transition S → S' occurs, the partition type may change:

| Transition | Type change | Condition |
|---|---|---|
| ε increases (coarser resolution) | Fine → coarser type | Sequential may become Binary |
| ε decreases (finer resolution) | Coarse → finer type | Binary may reveal Clustered structure |
| Aggregation applied | Any → coarser type | Clustered → Binary; Hierarchical → Binary |
| Coupling BC added | Binary → Sequential | New intermediate regimes appear |
| Multi-stable → forcing removed | Multi-stable → Binary | One attractor eliminated |

These transitions are directly testable in the experimental systems.
