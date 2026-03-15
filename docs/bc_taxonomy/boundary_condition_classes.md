---
status: working-definition
layer: docs/bc_taxonomy/
---

# Boundary Condition Classes

This document defines the ARW boundary condition (BC) taxonomy.
Each BC class is defined formally, its characteristic regime structure
is described, and instantiations across the experimental systems are given.

The central hypothesis of the ARW research program:

> Similar BC classes generate similar regime partition structures
> across domains.

This taxonomy is the operational form of that hypothesis.

For the full theoretical treatment, see
[docs/core/bc_classes_and_regime_generation.md](../core/bc_classes_and_regime_generation.md).

---

## Formal Role of Boundary Conditions

In the scope tuple S = (B, Π, Δ, ε), B specifies the set of constraints
that determine which states x ∈ X are admissible:

```
X_B = { x ∈ X | B(x) holds }
```

Different B configurations — even over the same underlying system —
induce different admissible state spaces and therefore different
regime partitions under A(S).

BC classes are equivalence classes of constraints that produce
structurally similar regime partitions across different systems.

---

## Class 1 — Restriction

**Definition:**
Constraints that bound a resource, capacity, or degree of freedom
to a finite range or maximum value.

```
B_restriction: f(x) ≤ C   for some resource function f and bound C
```

**Mechanism:**
As f(x) approaches C, certain strategies or trajectories become inadmissible.
The system is forced into a reduced action space. Distinct behavioral modes
emerge at different levels of resource saturation.

**Characteristic regime structure:**
- Stratified regimes along the resource dimension
- Sharp transitions at saturation boundaries
- Asymmetric partition: high-resource and low-resource regimes are structurally different

**Instantiations:**

| System | Restriction BC | Induced regime |
|---|---|---|
| Labyrinth Zone B | High action cost c | Deliberative mode dominates (R_B2); exploration inadmissible |
| Labyrinth Zone D | Visibility radius r = 1 | Reactive mode dominates (R_B4); planning inadmissible |
| Pendulum | Bounded energy E < E_max | Restricts to physical trajectories; chaos suppressed at low E |
| Opinion dynamics | Opinion space xᵢ ∈ [0,1] | Boundary effects create cluster-attracting behavior near extremes |

**Signature in partition:**
Regime boundaries align with resource saturation levels.
Near the restriction boundary, partition becomes coarser — fewer
distinguishable states survive the constraint.

---

## Class 2 — Coupling

**Definition:**
Constraints that impose mutual influence between components,
requiring their states to co-evolve within a bounded difference.

```
B_coupling: |xᵢ - xⱼ| < κ   or   xᵢ is dynamically influenced by xⱼ
```

**Mechanism:**
Coupling introduces coherence requirements. When coupling is strong enough,
independent trajectories synchronize into collective modes.
Regime transitions correspond to synchronization thresholds.

**Characteristic regime structure:**
- Incoherent → partially coherent → fully coherent transition sequence
- Partition cardinality decreases with coupling strength (modes merge)
- Cluster regimes under partial coupling (components synchronize locally)

**Instantiations:**

| System | Coupling BC | Induced regimes |
|---|---|---|
| Kuramoto (uniform) | All-to-all coupling K | R_K1 (incoherent) → R_K2 (partial) → R_K3 (synchronized) |
| Kuramoto (network) | Sparse coupling | Additional cluster-sync regimes; R_K2 splits |
| Pendulum | Joint stiffness κ | R_P4 (locked) emerges at high κ; reduction S_P → S_P' becomes admissible |
| Opinion dynamics | Confidence bound ε_bc | R_Op1 (consensus) ← coupling strong; R_Op3 (fragmented) ← coupling weak |

**Signature in partition:**
Critical coupling value K_c marks a partition boundary.
Below K_c: fine partition (many distinguishable regimes).
Above K_c: coarse partition (collective modes suppress individual variation).

---

## Class 3 — Symmetry Breaking

**Definition:**
Constraints that distinguish previously equivalent states or trajectories,
selecting among otherwise symmetric outcomes.

```
B_sym: h(x) ≠ 0   where h = 0 describes the symmetric case
```

**Mechanism:**
In the absence of symmetry breaking, a system has multiple equivalent
regime attractors. B_sym lifts this degeneracy — one attractor becomes
preferred, or the symmetric partition splits into asymmetric classes.

**Characteristic regime structure:**
- Bifurcated partition: symmetric solution replaced by two asymmetric regimes
- One regime becomes dominant; others become metastable or suppressed
- Partition is sensitive to the magnitude of symmetry breaking

**Instantiations:**

| System | Symmetry-breaking BC | Effect |
|---|---|---|
| Opinion dynamics | External media bias, asymmetric initial conditions | R_Op2 (polarization) splits: one cluster grows, other shrinks |
| Kuramoto | Bimodal frequency distribution g(ω) | Cluster-sync regimes form around frequency peaks |
| Labyrinth (ambiguous junctions) | Path cost asymmetry | Salience-driven selection among equivalent strategies |
| Geopolitical system | Asymmetric actor boundary conditions | US/Israel vs. Iran operate in structurally different regime spaces |

**Signature in partition:**
Symmetric partition → asymmetric partition under B_sym.
The number of regime classes may remain the same, but their
stability and accessibility change asymmetrically.

---

## Class 4 — Dissipation

**Definition:**
Constraints that continuously remove energy, information, or resources
from the system, driving it toward a contracted subset of state space.

```
B_dissipation: d/dt f(x) < 0   for some Lyapunov-like function f
```

**Mechanism:**
Dissipation contracts the effective state space over time.
Without dissipation, trajectories may fill state space ergodically.
With dissipation, they converge to lower-dimensional attracting structures.
Regime partitions under dissipative BCs correspond to attractor basins.

**Characteristic regime structure:**
- Contracted partition: fewer effective regimes than the full state space supports
- Attractor-basin structure: each regime class is the basin of an attractor
- Stability depth: regimes are robust to perturbations (dissipation absorbs them)

**Instantiations:**

| System | Dissipation BC | Effect |
|---|---|---|
| Pendulum (damped) | Damping coefficient γ > 0 | Chaotic regime R_P3 suppressed; periodic regimes stabilized |
| Labyrinth agent | Policy gradient descent | Policy space contracts toward attractor regimes (modes) |
| Geopolitical attractors | Institutional inertia, cost of regime change | Contained conflict (A1) is deep attractor; war (R_A5) has high entry cost |

**Signature in partition:**
Dissipation makes regime boundaries more stable (harder to cross via Δ).
High dissipation → fewer, deeper, more robust regimes.
Low dissipation → more regimes, shallower, more sensitive to perturbation.

---

## Class 5 — Forcing

**Definition:**
Constraints that inject external energy or information into the system
at a specified frequency or rate, preventing relaxation to equilibrium.

```
B_forcing: x receives external input F(t) with characteristic timescale τ_F
```

**Mechanism:**
Forcing drives the system away from its natural resting state.
Regime structure is determined by the relationship between forcing
frequency and natural system frequencies (resonance / entrainment).
Different forcing regimes (sub-resonant, resonant, supra-resonant)
produce qualitatively different partition structures.

**Characteristic regime structure:**
- Entrainment regimes: system locks to forcing frequency
- Quasiperiodic regimes: near-resonant but not locked
- Chaotic regimes: forcing breaks all stable orbits
- The partition maps the (amplitude, frequency) parameter space

**Instantiations:**

| System | Forcing BC | Effect |
|---|---|---|
| Pendulum (driven) | Driving amplitude A, frequency Ω | R_P1/R_P2/R_P3 partition in (A, Ω) space |
| Kuramoto (external field) | Global phase forcing | Entrainment regime appears; R_K1 suppressed above forcing threshold |
| Labyrinth (dynamic shifts) | Mid-episode BC changes | Forces unscheduled scope transitions; tests admissibility-loss detection |
| Geopolitical | External crisis events | Scope-transition triggers — disrupts current regime stability |

**Signature in partition:**
Resonance creates sharp partition boundaries in forcing parameter space.
Forcing frequency is a primary BC parameter: the partition topology
changes qualitatively as Ω crosses natural system frequencies.

---

## Class 6 — Aggregation

**Definition:**
Constraints that suppress individual-level information by replacing it
with aggregate statistics, reducing the observable space by design.

```
B_aggregation: Π_agg = { summary statistics of Π_full }
```

**Mechanism:**
Aggregation is a scope operation, not a system property.
It corresponds to choosing Π such that individual-level distinctions
fall below ε. The characteristic effect is partition coarsening:
fine-grained regime classes merge in the aggregated scope.

**Characteristic regime structure:**
- Coarser partition than the individual-level scope
- Loss of boundary-region classes (states near regime transitions are misclassified)
- Mean-field regimes are always a subset of agent-level regimes
- Specific distortion: boundary-straddling states are absorbed into the nearest bulk class

**Instantiations:**

| System | Aggregation BC | Effect |
|---|---|---|
| Opinion dynamics → mean-field | Π_MF = { ρ(x,t) } | R_Op4 (frozen disorder) becomes invisible; transition boundaries shift |
| Kuramoto → order parameter | Π_MF = { r(t) } | Individual oscillator regimes suppressed; only global sync visible |
| Labyrinth → episode scope | Π_ep = { outcome } | Intra-episode mode structure invisible; only success/failure survives |
| Geopolitical → system level | Π_G = { conflict_intensity } | Actor-level distinctions (R_A4, R_A6) become ambiguous |

**Signature in partition:**
Aggregation always reduces partition cardinality or shifts boundaries.
The distortion metrics TBS, RCD, PCI, SDI quantify the degree of this reduction.
See [transfer_distortion_metrics.md](transfer_distortion_metrics.md).

---

## BC Class Combinations

BC classes can combine. Combined classes produce compound regime structures.

| Combination | Effect |
|---|---|
| Coupling + Restriction | Synchronization suppressed by resource limits; cluster regimes at intermediate coupling |
| Dissipation + Forcing | Driven-dissipative system; regime structure in forcing parameter space with attractor basins |
| Coupling + Symmetry breaking | Asymmetric synchronization; one cluster dominates |
| Aggregation + any class | The aggregated scope may fail to detect the characteristic regimes of the other class |

The labyrinth experiment combines **restriction** (resource constraints per zone),
**coupling** (anchor memory links context to mode), and **aggregation** (episode-level
scope suppresses intra-episode switching). This compound structure is why it is the
most complex test case in the research program.

---

## Summary Table

| BC class | Formal form | Characteristic partition | Key parameter |
|---|---|---|---|
| Restriction | f(x) ≤ C | Stratified by resource level | Saturation bound C |
| Coupling | \|xᵢ - xⱼ\| < κ | Incoherent → clustered → synchronized | Coupling strength κ |
| Symmetry breaking | h(x) ≠ 0 | Bifurcated / asymmetric | Symmetry-breaking magnitude |
| Dissipation | df/dt < 0 | Contracted, attractor-basin | Dissipation rate γ |
| Forcing | F(t) external | Resonance / quasiperiodic / chaotic | Forcing frequency Ω |
| Aggregation | Π_agg ⊂ Π_full | Coarsened, boundary-shifted | Resolution loss |
