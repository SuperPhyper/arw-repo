---
status: working-definition
---

# ART Instantiation: Context-Navigation Agent
## Labyrinth Experiment — Scope Definition and Core Hypotheses

This document defines the ART scope for the context-navigation agent experiment.
It is the primary **cognitive architecture test case** of Phase 2 and the
face of the OSV fellowship application.

The experiment tests whether an agent architecture with mode selection,
anchor memory, and consolidation produces emergent behavioral regime structure —
and whether that structure is measurable using ARW partition tools.

For the extended environment design with constraint zones, see
[labyrinth_experiment_extended_design.md](labyrinth_experiment_extended_design.md).

---

## 1 System Description

**Domain:** Reinforcement learning — context-driven navigation in structured environments

**Why this system:**
The labyrinth agent is the ARW framework's first *endogenous* test case:
unlike the physical calibration systems, the agent's regime structure is not
given by the environment but *emerges* from the interaction between
environmental boundary conditions and the agent's internal architecture.

This makes it the critical test of the claim that BC-induced regime structure
generalizes beyond physics and dynamical systems.

**State space X:**
A state x ∈ X is a full system snapshot:

```
x = (grid_position, local_observation, active_mode, context_embedding,
     anchor_memory_state, salience_vector, episode_step)
```

The state space is partially observable — the agent sees only within
its visibility radius, not the full maze.

**Key distinction from calibration systems:**
In Kuramoto and the pendulum, scope and regime structure are analytically
derived from the equations of motion. Here, regime structure must be
*measured from agent behavior* — the ARW partition extraction pipeline
operates on behavioral trajectories, not on differential equations.

---

## 2 Scope Definition

### Behavioral Scope S_B

The primary scope tracks the agent's behavioral regime —
which strategy dominates at each point in the environment.

```
S_B = (B_B, Π_B, Δ_B, ε_B)
```

**B_B — Boundary Conditions**

Environmental constraints that structure the admissible behavioral regime space:

| Constraint | Value | Effect on regime space |
|---|---|---|
| Planning budget | lookahead depth d ∈ {1, 3, 5, ∞} | Suppresses deliberative modes at d=1 |
| Visibility radius | r ∈ {1, 3, full} | Suppresses global-map modes at r=1 |
| Action cost | c ∈ {low, medium, high} | Suppresses exploration mode at high c |
| Memory capacity | m ∈ {0, 5, unlimited} | Suppresses anchor-retrieval mode at m=0 |
| Error tolerance | τ ∈ {strict, lenient} | Suppresses reactive mode at strict τ |

These are the **experimentally manipulated boundary conditions**.
Each configuration of (d, r, c, m, τ) defines a distinct BC tuple
and is predicted to induce a characteristic regime partition.

**Π_B — Observables**

```
Π_B = { mode_activation(t), policy_embedding(t), action_distribution(t),
         salience_vector(t), anchor_retrieval_event(t) }
```

- mode_activation: which of the k learned modes is active at step t
- policy_embedding: continuous representation of current policy in latent space
- action_distribution: probability distribution over actions
- salience_vector: competition signal between candidate modes
- anchor_retrieval_event: binary — did the agent retrieve a stored context anchor?

**Δ_B — Admissible Perturbations**

- Small perturbations to maze layout (wall repositioning < 10% of cells)
- Noise in initial position within the same structural zone
- Single-step action noise (ε-greedy with ε < 0.05)

Perturbations outside Δ_B (full maze restructuring, BC changes) are
scope-transition triggers, not noise.

**ε_B — Resolution Threshold**

```
ε_B: policy embeddings with cosine distance < 0.1 are indistinguishable
```

Behavioral differences below this threshold are treated as within-regime
variation, not regime transitions.

---

## 3 Regime Partition under S_B

```
A(S_B) = R_B
```

The predicted regime partition contains four behavioral regime classes,
each corresponding to a dominant cognitive strategy:

| Regime | Strategy | Dominant BC conditions | Signature in Π_B |
|---|---|---|---|
| R_B1 — Exploration | Builds internal map, high coverage | Low action cost, large visibility, low memory | High action entropy, no anchor retrieval |
| R_B2 — Deliberative | Plans ahead, minimizes errors | High action cost, large planning budget | Low action entropy, no anchor retrieval, high salience at junctions |
| R_B3 — Anchor retrieval | Matches current context to stored patterns | High memory, familiar structure | Anchor retrieval events, fast mode activation |
| R_B4 — Reactive | Local sensing, immediate response | Low visibility, low planning budget | High action entropy, short policy embedding variance |

**Structural prediction:**
Under uniform BC (single constraint regime), the agent converges to
a single dominant mode — only one regime class dominates.
Under mixed BC (constraint zones), all four regimes are active
within a single episode, switching at zone boundaries.

The partition R_B must be empirically extracted from behavioral trajectories —
not assumed. The ARW claim is that it *will* be discrete, not continuous.

---

## 4 The Architecture as Scope Machinery

The agent architecture is not just an implementation detail —
each component maps directly onto ARW scope machinery:

| Architecture component | ARW role |
|---|---|
| Constraint zones (B) | Boundary conditions defining admissible strategies |
| Learnable modes (k policies) | Candidate regime representatives |
| Gating mechanism | Mode selection = regime activation |
| Salience estimator | Admissibility loss signal — detects scope boundary |
| Context embedding | State projection Π_B |
| Anchor memory | Stored scope-partition associations from prior episodes |
| Sleep / consolidation | Post-episode regime stabilization — strengthens partition boundaries |

**Key ARW interpretation of sleep:**
Consolidation is not primarily about improving performance weights.
It is about *sharpening the regime partition* — making [x]_B boundaries
more stable under Δ_B perturbations.
A sleep phase that improves task performance but does not increase
partition stability is not supporting the ARW account.

---

## 5 Scope Transitions within the Agent

The agent undergoes internal scope transitions when it moves between
constraint zones or encounters a BC shift.

**Example transition: Zone A → Zone B**

```
S_B(Zone A) = (B_low-cost, Π_B, Δ_B, ε_B)   →   R_B(A) dominated by R_B1
S_B(Zone B) = (B_high-cost, Π_B, Δ_B, ε_B)  →   R_B(B) dominated by R_B2
```

At the zone boundary, S_B(A) loses admissibility for the new BC:
exploration is no longer a valid strategy under high action cost.
This triggers a scope transition — salience spikes as candidate modes compete.

**ARW prediction:**
Salience spikes are the observable signature of scope transitions.
They are not simply uncertainty signals — they are admissibility loss events
in which the current scope's regime assignment becomes unstable.

---

## 6 Cross-Scope Comparison: Behavioral S_B → Structural S_S

A second scope describes the *environment structure* rather than the agent behavior:

```
S_S = (B_S, Π_S, Δ_S, ε_S)
```

where Π_S = {zone_type, structural_motif, local_topology} — observable properties
of the maze independent of the agent.

**Admissibility prediction S_B → S_S:**

The behavioral regime partition R_B should be compatible with the
structural partition R_S induced by zone boundaries:

```
zone boundary in R_S  ↔  mode switch in R_B
```

If behavioral modes align with structural zones, the reduction S_B → S_S
is admissible: zone type predicts behavioral mode.

If modes do not align with zones — the agent uses a different strategy
than the zone "intends" — the reduction is inadmissible.
This is a direct test of whether the environment's BC structure
is driving the agent's regime structure.

---

## 7 Core Hypotheses in ARW Terms

| Hypothesis | ARW formulation |
|---|---|
| H1: Resource constraints select modes | BC tuple (d, r, c, m, τ) determines which R_Bᵢ are admissible |
| H2: Sleep stabilizes context–mode anchors | Consolidation increases partition stability: ε_B widens post-sleep |
| H3: Salience enables mode switching | Salience spike = admissibility loss at scope transition boundary |
| H4: Transfer via anchor reuse | Prior R_B partition compatible with new maze's R_S → fast reactivation |

---

## 8 Distortion Metrics for the Agent Experiment

| Metric | Definition |
|---|---|
| Mode stability index | Variance of mode_activation within a zone across episodes |
| Zone–mode alignment score | Mutual information between zone_type and active_mode |
| Salience–transition correlation | Pearson correlation of salience spikes with mode switch events |
| Transfer PCI | Fraction of anchor retrievals correctly predicting active mode in new maze |
| Sleep sharpening index | Change in policy embedding cluster separation before/after consolidation |

---

## 9 Baseline Comparisons

| Baseline | Missing component | ARW prediction |
|---|---|---|
| Standard RL (single policy) | No modes, no anchors, no sleep | No discrete partition emerges |
| Mixture-of-experts, no salience | No admissibility signal | Modes emerge but switching is sluggish |
| Multi-mode, no sleep | No consolidation | Modes emerge but anchors are unstable across mazes |
| Full architecture | All components | Discrete partition + stable anchors + fast transfer |

The baselines are designed to isolate each ARW mechanism independently.

---

## 10 Falsification Conditions

The ARW account is **weakened** if:

- Policy embeddings form a continuous manifold, not discrete clusters — no partition emerges
- Sleep improves task performance but does not increase cluster separation — consolidation is not partition sharpening
- Salience spikes are uncorrelated with mode switches — salience is not an admissibility signal
- Transfer requires full relearning — prior partition is incompatible with new maze's structure
- Zone–mode alignment is random — environmental BC does not drive behavioral regime structure

---

*For the extended environment design, see [labyrinth_experiment_extended_design.md](labyrinth_experiment_extended_design.md).*
*For the cognitive architecture theory, see [docs/context_navigation/agent_architecture_mode_ecology.md](../docs/context_navigation/agent_architecture_mode_ecology.md).*
*For the ARW account of salience, see [docs/context_navigation/salience_mode_ecology.md](../docs/context_navigation/salience_mode_ecology.md).*
