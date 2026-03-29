---
status: working-definition
layer: docs/context_navigation/
---

# Context Navigation — ARW Scope Specification

## Purpose

This document provides the formal ARW scope specification for the
context-navigation labyrinth system.

It serves as the bridge between the ARW/ART framework and the
Context Navigation Agent architecture:

- It defines the **system-level scope** S = (B, Π, Δ, ε) for the
  labyrinth environment and the agent operating within it.
- It shows how **labyrinth constraint zones** instantiate as **scope
  transitions S → S'** in the ARW sense.
- It maps each architectural component of the agent to its ARW role.

This is an ART-level document. The formal ARW definitions it uses
are sourced from `docs/glossary/scope.md` and
`docs/bc_taxonomy/boundary_condition_classes.md`.

---

## 1 System Description

The system consists of two coupled components:

**The labyrinth environment** — a structured maze with distinct
constraint zones. Each zone enforces a different set of resource
limits, navigation rules, or salience signals. Zone boundaries
are discontinuous: crossing a boundary changes which strategies
are viable.

**The context navigation agent** — an agent with a mode library
M = {m₁, m₂, ..., m_k}, anchor-based memory, a salience estimator,
and a periodic consolidation phase. The agent must learn to select
the admissible processing mode for each zone and to switch modes
at zone boundaries.

The scientific question is whether a stable **regime partition**
emerges over the agent's behavioral space — a partition that
corresponds to the zone structure of the environment.

---

## 2 Global Scope S_global

The global scope describes the full labyrinth system as observable
from outside.

```
S_global = (B_global, Π_global, Δ_global, ε_global)
```

### B_global — Boundary Constraints

The global boundary conditions select the admissible state space
of the joint system (environment + agent).

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_g1 | The labyrinth is finite and fully connected. The agent's position x(t) ∈ L where L is the discrete zone graph. | Restriction |
| B_g2 | Zone membership determines which resource constraints are active. Crossing a zone boundary changes the active constraint set. | Restriction |
| B_g3 | The agent's mode library M is fixed in size throughout an experiment. | Restriction |
| B_g4 | Agent and environment interact through shared perception channel: agent observes local zone features, not global map. | Coupling |
| B_g5 | Consolidation phases occur periodically at fixed episode intervals. | Forcing |
| B_g6 | Anchor memory decays if not reinforced across consolidation cycles. | Dissipation |

The primary BC class of S_global is **Coupling** (agent–environment)
with **Restriction** (zone constraints) as structural co-driver.

### Π_global — Admissible Observables

Admissible observables project the joint state (agent position,
active mode, anchor activation, salience level) onto measurable
quantities.

| Observable key | Description | Observable range R(π) |
|---------------|-------------|----------------------|
| mode_dist | Distribution over active modes across time steps within a zone. Measures regime occupancy. | [0, 1]^k, sums to 1 |
| switch_rate | Mode-switch events per episode. Measures transition frequency. | [0, max_steps] |
| salience_mean | Mean salience S(c) = Var_m(F_m(c)) within a zone. Measures boundary proximity. | [0, σ²_max] |
| anchor_stability | Fraction of anchors retained across successive consolidation cycles. Measures partition stability. | [0, 1] |
| task_success | Episode success rate per zone, per mode. Measures regime fitness. | [0, 1] |

Primary observable: **mode_dist** (sufficient for regime partition;
measures which behavioral regime dominates each zone).

Secondary observable: **salience_mean** (measures admissibility
competition at zone boundaries; structurally analogous to χ =
∂r_ss/∂κ at K_c in CASE-20260311-0001).

### Δ_global — Admissible Perturbations

Perturbations that the regime partition must remain stable under:

| ID | Perturbation |
|----|-------------|
| δ₁ | Random noise in the agent's perception of local zone features (up to magnitude η). |
| δ₂ | Paraphrased or shuffled instruction sequences within a zone type. |
| δ₃ | Small structural variations of the labyrinth (equivalent zone graph, different geometry). |
| δ₄ | Different random seeds for initial agent state and anchor initialization. |

Perturbations δ₃ and δ₄ are the transfer-test perturbations:
they define when a learned mode partition **generalizes** to unseen
environments.

### ε_global — Resolution Threshold

Two behavioral states x, y are indistinguishable under S_global if:

```
d_Π(x, y) ≤ ε_global
```

where d_Π is the L¹ distance over the mode_dist observable.

ε_global is to be determined empirically via the ε-sweep pipeline
(analogous to the Kuramoto ε-sweep in CASE-20260311-0001).
The working hypothesis is that a robust plateau exists at a regime
count N matching the number of structurally distinct zone types
in the labyrinth.

---

## 3 Zone-Level Scopes (Sub-Scope Transitions within S_global)

Each labyrinth zone enforces a reduced scope S_zone ⊂ S_global.

**Terminological precision (see `mode_scope_regime_audit.md` §2.3):**
Zone boundary crossings are **sub-scope transitions S_z → S_z'** within S_global —
the global scope remains valid throughout. They are not scope transitions in the
strong ARW sense (which would require S_global itself to become invalid, i.e.
all π ∈ Π entering Z(π)). The *modes* the agent employs within a zone are
regime cells in S_global's partition; zone-level sub-scopes differ in their
active B_z ⊆ B_global.

A **sub-scope transition** occurs when the agent crosses a zone boundary:
the active boundary constraints change, the admissible observable
range shifts, and the admissible mode set contracts to the subset
that remains valid under the new constraints.

### Zone Scope Template

Each zone z instantiates a scope:

```
S_z = (B_z, Π_z, Δ_z, ε_z)
```

where B_z ⊂ B_global restricts to the constraints active in zone z,
and Π_z ⊆ Π_global retains only observables with non-degenerate
range under B_z.

### Example Zone Scopes

The labyrinth design specifies at minimum three structurally distinct
zone types, corresponding to three BC-class instantiations:

**Zone type R — Resource-restricted zone (BC class: Restriction)**

```
B_R:  Agent's action set is reduced to a strict subset of L.
      Navigation paths with high resource cost are inadmissible.
Π_R:  Primary observable: task_success (measures survival under
      resource constraint). switch_rate is secondary.
ε_R:  Smaller than ε_global: finer resolution needed because
      strategy differences have large outcome consequences.
Admissible mode: cautious planning mode.
```

**Zone type C — Coupling zone (BC class: Coupling)**

```
B_C:  Agent must coordinate with environmental signals
      (e.g., timing-dependent doors, token-passing constraints).
      Agent state and environment state are coupled.
Π_C:  Primary observable: mode_dist (measures which coordination
      strategy dominates). salience_mean secondary.
ε_C:  Working value from calibration experiments.
Admissible mode: reactive / coordination mode.
```

**Zone type F — Forcing zone (BC class: Forcing)**

```
B_F:  External periodic signal (time pressure, pulsed reward)
      drives agent behavior. The temporal structure of the
      forcing is an explicit boundary condition X → X × T.
Π_F:  Primary observable: switch_rate (measures responsiveness
      to forcing rhythm). task_success secondary.
ε_F:  Working value from calibration experiments.
Admissible mode: exploration or heuristic mode (depending on
      forcing frequency relative to consolidation period).
```

### Scope Transition Formalization

The transition from zone type A to zone type B is a scope
transition S_A → S_B characterized by:

- **ΔB**: the change in active boundary constraints.
  Measured as the set difference ΔB = B_B \ B_A ∪ B_A \ B_B.
- **ΔΠ**: the shift in primary observable.
  If primary observables differ across zones, the transition
  involves observable replacement — not scope failure.
- **Δε**: if the resolution threshold changes across zones,
  partition compatibility at the boundary requires the
  matched-ε transfer protocol (see Transfer Metrics).

The agent must detect this transition via its salience estimator
and switch to the admissible mode for the new scope.

**Salience at scope transitions** corresponds structurally to the
fluctuation observable χ = ∂r_ss/∂κ at K_c in CASE-20260311-0001:
it is highest precisely where admissibility is most contested.

---

## 4 Agent Architecture — ARW Role Mapping

| Agent component | ARW role | Formal correspondence |
|----------------|----------|-----------------------|
| Perception layer | Observable projection | π: X → D_π (where π ∈ Π_global) |
| Context representation | Scope-relative state | x_Π = π(x), the projected state |
| Mode library M | Regime partition | Each m_i corresponds to a regime R_i in the partition of X_B |
| Mode gating / selection | Scope admissibility check | m* = argmax_m A(m|c) ≅ selecting the admissible regime |
| Salience estimator | Sub-scope-boundary detector | Fluctuation observable; maximal near Z_shared at zone boundaries. Class-E formula S(c) = Var_m(F_m(c)) valid only within zones (away from Z_shared). See `mode_scope_regime_audit.md` §2.2. |
| Anchor memory | Stored scope–partition associations | aᵢ = (context_class, mode, stability_score) ≅ partition membership record |
| Consolidation phase | Partition boundary sharpening | Refines the equivalence classes x ~_S y; reduces ε-instability |
| Transfer test | Cross-scope partition compatibility | Δ-perturbation test on unseen labyrinth; measures Φ (partition compatibility) |

---

## 5 Observables — Pre-Scopal Substrate Analysis

### mode_dist

**Pre-scopal substrates required:**
- A4 (stationarity): the mode distribution must be stationary
  within a zone for the observable to be meaningful.
  Violated at zone transitions → mode_dist enters Z(π) at
  boundary-crossing events.
- A2 (independence of measurements): consecutive mode activations
  must be sufficiently decorrelated.

**Observable range R(mode_dist):**
- Valid while agent is within a single zone type.
- Violates A4 during zone transitions → F0 condition applies;
  transition windows should be excluded from partition computation.

**BC class of the observable itself:**
- mode_dist is Aggregation-dominated: it projects the full
  sequence of mode activations onto a probability vector.
  Observable BC notation: A·R.

### salience_mean

**Pre-scopal substrates required:**
- A1 (differentiability of fitness landscape): F_m(c) must be
  smooth enough in context space for Var_m(F_m(c)) to be
  well-defined.
- A4 (stationarity): within a zone, the fitness landscape
  should be approximately stationary.

**Observable range R(salience_mean):**
- Valid within zones.
- At zone transitions: salience_mean peaks and potentially
  violates A4 → enters Z(π).
  This is the desired behavior: salience_mean IS the scope
  transition detector. Its Z(π) is the scope boundary itself.

**BC class of the observable:**
- salience_mean is Restriction-dominated: it projects the
  mode-fitness distribution onto its variance.
  Observable BC notation: R·A.

---

## 6 Failure Modes

| ID | Condition | Severity | Action |
|----|-----------|----------|--------|
| F0 | mode_dist observed during zone-transition window (A4 violated) | observable_replacement | Exclude transition steps; use salience_mean for boundary detection |
| F1 | span(mode_dist) < 2ε across all zones | observable_replacement | Increase zone contrast or reduce ε_global |
| F1_BC | span(ALL observables) < ε | scope_rejection | Zone types not structurally distinct enough; redesign labyrinth |
| F2 | Regime partition unstable under δ₃ (structural maze variation) | scope_rejection | Mode ecology does not generalize; transfer test fails |
| F3 | No robust ε plateau across all observables | scope_rejection | Review zone design; check BC class assignment |
| F4 | Transition boundary θ* at episode boundary | sweep_refinement | Extend consolidation interval; rerun |

---

## 7 Connection to Transfer Protocol

The agent's transfer test (run on unseen labyrinth instances) is
an ARW transfer experiment:

- Source scope: S_training (labyrinth A)
- Target scope: S_transfer (labyrinth B, unseen geometry)
- Transfer metric: Φ(S_training, S_transfer)

Admissibility verdict thresholds follow the standard protocol:
- Φ ≥ 0.75: highly_admissible (strong regime generalization)
- 0.5 ≤ Φ < 0.75: partially_admissible
- Φ < 0.5: inadmissible (mode ecology is environment-specific)

The transfer result directly answers the OSV research question:
do the learned behavioral regimes constitute a **generalizable
partition** or an environment-specific one?

---

## 8 Relation to Pending Cases

| Case | System | Relation to this scope |
|------|--------|----------------------|
| CASE-20260315-0005 | Dissipation (Multi-Pendel + γ) | Anchor decay (B_g6) instantiates same BC class |
| CASE-20260315-0006 | Forcing (Multi-Pendel + Ω) | Zone type F (Forcing) shares S3 operator signature |
| CASE-20260315-0007 | SIR (β-sweep) | Zone type R (Restriction) shares S1 operator signature |
| CASE-20260318-0004 | Stuart-Landau emergence | Consolidation phase as emergence condition — same ARW structure |

---

## 9 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-CNS-01 | What is the empirically optimal ε_global for the labyrinth partition? Requires ε-sweep on mode_dist data. | open |
| Q-CNS-02 | Does the salience_mean observable show a Z(π) peak at zone transitions that is structurally analogous to χ at K_c? | open |
| Q-CNS-03 | Is the consolidation phase necessary for regime partition stability, or does it emerge without it? (Testable by ablation.) | open |
| Q-CNS-04 | What is Φ(S_training, S_transfer) for structurally similar vs. dissimilar labyrinths? | open |
| Q-CNS-05 | Do the BC classes of the zone types (R, C, F) produce the mode types predicted by bc_taxonomy_cognitive_modes? | open |
