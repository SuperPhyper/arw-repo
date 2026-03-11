---
status: working-definition
---

# BC Class to Regime Type Map

This document provides the explicit mapping from boundary condition classes
to the partition types they characteristically generate.

It is the operational core of the ARW research hypothesis:

> Similar BC classes generate similar regime partition structures
> across different systems and domains.

---

## The Mapping

| BC class | Primary partition type | Secondary (under combination) | Signature parameter |
|---|---|---|---|
| Restriction | Sequential | Binary (at extreme saturation) | Resource bound C |
| Coupling | Sequential → Binary | Clustered (network topology) | Coupling strength κ |
| Symmetry breaking | Binary (bifurcated) | Clustered (multiple broken symmetries) | Asymmetry magnitude h |
| Dissipation | Multi-stable (basin structure) | Binary (high dissipation) | Dissipation rate γ |
| Forcing | Sequential (resonance ladder) | Multi-stable (bistable forcing) | Forcing frequency Ω |
| Aggregation | Hierarchical (coarsened) | Binary (strong aggregation) | Resolution loss ε_agg |

---

## Cross-System Verification Table

The hypothesis predicts that the same BC class produces the same
partition type across different domains. This table maps each prediction
to the experimental system that tests it.

### Coupling → Sequential partition

| System | Coupling BC | Sequential partition | Predicted sequence |
|---|---|---|---|
| Kuramoto (uniform) | All-to-all K | ✓ (3 classes) | Incoherent → Partial → Synchronized |
| Pendulum (joint) | Stiffness κ | ✓ (4 classes) | Periodic → Quasi → Chaotic → Locked |
| Opinion dynamics | Confidence ε_bc | ✓ (4 classes) | Consensus → Polar → Fragmented → Frozen |

**Cross-system prediction:** All three systems should show the same
sequential structure (multi-class, ordered, single-parameter-driven).
The specific class labels differ, but the partition type is identical.

---

### Restriction → Sequential partition (resource-stratified)

| System | Restriction BC | Sequential partition | Predicted sequence |
|---|---|---|---|
| Labyrinth Zone B | Action cost c | ✓ (2 classes) | Exploration → Deliberative |
| Labyrinth Zone D | Visibility r | ✓ (2 classes) | Planning → Reactive |
| Pendulum | Energy bound E_max | ✓ (bounded chaos) | Regular → bounded irregular |

**Cross-system prediction:** Resource restriction produces stratified
partitions with clear thresholds. The saturation point C maps directly
to the regime transition boundary.

---

### Symmetry breaking → Binary (bifurcated) partition

| System | Symmetry-breaking BC | Binary partition | Notes |
|---|---|---|---|
| Opinion dynamics (biased) | External media bias | ✓ (asymmetric polarization) | Symmetric R_Op2 → asymmetric split |
| Geopolitical (actor asymmetry) | Different BC tuples per actor | ✓ (structurally different action spaces) | US/Iran asymmetry |
| Kuramoto (bimodal g(ω)) | Two frequency peaks | ✓ (two sync clusters) | Symmetry broken by frequency distribution |

---

### Dissipation → Multi-stable partition

| System | Dissipation BC | Multi-stable partition | Notes |
|---|---|---|---|
| Pendulum (damped + driven) | Damping γ + driving A | ✓ (bistable for certain (A,Ω)) | Two stable orbits coexist |
| Labyrinth agent (policy gradient) | Gradient descent | ✓ (mode ecology) | Multiple policy attractors |
| Geopolitical (institutional inertia) | Transition cost | ✓ (containment vs. escalation) | Both attractors stable simultaneously |

---

### Aggregation → Hierarchical partition (with information loss)

| Scope transition | Aggregation | Partition type change | Information loss |
|---|---|---|---|
| Kuramoto: individual → order parameter | r(t) suppresses θᵢ | Sequential preserved (3 classes) | Cluster substructure lost |
| Consensus: agent → mean-field | ρ(x,t) suppresses xᵢ | Sequential compressed (R_Op4 lost) | 1 class lost |
| Labyrinth: zone → episode | Outcome suppresses trajectory | Sequential → Binary or worse | 2–3 classes lost |
| Geopolitical: actor → system | Conflict index suppresses actor identity | Sequential compressed | R_A4, R_A6 ambiguous |

---

## Failure Cases (Predicted Mismatches)

Not every BC combination produces the predicted partition type.
These are the known failure cases — important as controls and for
boundary conditions of the hypothesis.

| BC class | Condition | Expected type | Actual type | Reason |
|---|---|---|---|---|
| Coupling | Network topology sparse | Sequential | Clustered | Sub-communities form their own sequences |
| Restriction | Multiple simultaneous resources | Sequential | Clustered | Each resource produces its own sequence; they interleave |
| Forcing | Near resonance | Sequential | Multi-stable | Bistability near resonance disrupts sequential ordering |
| Aggregation | Over-aggregation | Hierarchical | Binary | Too much resolution loss collapses hierarchy |

These failure cases define the **boundaries of the hypothesis**:
BC class → partition type is a strong claim in the bulk,
but at BC class combinations and boundary regions it may break down.

---

## Regime Graph Topology by BC Class

Beyond partition type, the transition topology also has characteristic form:

| BC class | Characteristic regime graph topology |
|---|---|
| Coupling | Linear chain: R₁ → R₂ → R₃ (one path through parameter space) |
| Restriction | Linear chain with asymmetric barriers (forward/reverse transition costs differ) |
| Symmetry breaking | Fork: symmetric regime splits into two asymmetric branches |
| Dissipation | Star: attractor at center, multiple basins radiating outward |
| Forcing | Loop: resonant regimes can cycle under varying Ω |
| Aggregation | Contraction: n-node graph → m-node graph (m < n) via node merging |

---

*See [boundary_condition_classes.md](boundary_condition_classes.md) for full BC class definitions.*
*See [partition_types.md](partition_types.md) for full partition type definitions.*
*See [transfer_distortion_metrics.md](transfer_distortion_metrics.md) for quantifying mapping failures.*
