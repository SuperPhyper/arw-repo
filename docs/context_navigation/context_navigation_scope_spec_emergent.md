---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/mode_scope_regime_audit.md
---

# Context Navigation — ARW Scope Specification (Emergent Modes)

## Purpose

This document provides the formal ARW scope specification for the
**Emergent Modes Experiment** defined in
`context_navigation_emergent_modes_experiment.md`.

It is the scope-level companion to that experiment document, following the
same structure as other ARW scope specifications in the repository.

This document is **not** a revision of `context_navigation_scope_spec.md`.
That document formalizes the Designed Modes Experiment (agent with prescribed
mode library M). This document formalizes the Emergent Modes Experiment
(unstructured policy; ARW as observation instrument).

---

## 1 System Description

The system consists of two coupled components:

**The labyrinth environment** — a structured maze with distinct zone types.
Each zone enforces a different set of resource constraints, navigation rules,
or reward signals (zone types R, C, F as in `context_navigation_scope_spec.md` §1).
Zone boundaries are discontinuous.

**The context navigation agent** — a single unstructured policy (e.g. a
feedforward or recurrent neural network) trained by reinforcement learning
on the labyrinth. The agent has no mode library, no explicit mode selector,
and no mode-labeled training signal.

The scientific question:

> Does a stable regime partition emerge over the agent's behavioral space
> after training — a partition that was not architecturally prescribed but
> that corresponds to the zone structure of the environment?

---

## 2 Global Scope S_emergent

```
S_emergent = (B_emergent, Π_emergent, Δ_emergent, ε_emergent)
```

### B_emergent — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_e1 | The labyrinth is finite and fully connected. Agent position x(t) ∈ L (discrete zone graph). | Restriction |
| B_e2 | Zone membership determines active resource constraints. Crossing a zone boundary changes the active constraint set. | Restriction |
| B_e3 | The agent is a single unstructured policy. No mode architecture is prescribed. | Restriction |
| B_e4 | Agent perceives local zone features only; no global map is available. | Coupling |
| B_e5 | Reward signal is task-performance only. No mode-label signal is provided during training. | Restriction |

The primary BC class of S_emergent is **Restriction**.
The dominant structural condition is what the agent is *not given*:
no mode structure, no mode labels, no modular architecture.
This distinguishes S_emergent from S_global in `context_navigation_scope_spec.md`,
where B_g3 (fixed mode library) is itself a prescriptive Restriction.

### Π_emergent — Admissible Observables

Observables are defined over behavioral trajectories of the trained agent.
They project trajectory segments — not architectural states — onto
measurable quantities.

| Observable key | Description | Observable BC notation | Primary? |
|---------------|-------------|----------------------|---------|
| action_dist | Distribution over actions within a zone-episode window. Measures behavioral regime occupancy. | A·R | yes |
| trajectory_entropy | Entropy of the action sequence within a zone. Measures behavioral diversity. | A·R | no |
| zone_return | Cumulative reward per zone type. Measures regime fitness. | R·A | no |

**Primary observable: action_dist**

action_dist is the behavioral analog of r_ss (Kuramoto) and var_rel
(Doppelpendel): a distributional summary statistic over a trajectory window
that aggregates behavioral variation into a single representational vector.

**Key difference from the Designed Modes Experiment:**
In the Designed Modes Experiment, the primary observable is `mode_dist` —
the distribution over the agent's *prescribed* mode activations.
In this experiment, there are no prescribed modes. The observable is
`action_dist` — the distribution over *actions* — because actions are
the only behavioral signal available from an unstructured policy.
If regime structure is present, it will manifest as systematic differences
in action_dist across zone types.

### Pre-Scopal Substrate Analysis — action_dist

| ID | Assumption | Violated when |
|----|-----------|---------------|
| A4 | The action distribution is approximately stationary within the current zone-episode window. | During zone transitions (boundary-crossing episodes). |
| A2 | Consecutive action samples within a window are sufficiently decorrelated. | In highly repetitive or stuck trajectories. |
| A_conv | The agent's policy has converged for the current zone type. | In early training or in novel zones far from training distribution. |

**Observable range R(action_dist):**
Valid within zones after convergence. Violated at zone boundaries (F0
condition, same argument as for `mode_dist` in `context_navigation_scope_spec.md` §5).
Transition windows must be excluded from partition computation.

**Observable BC notation: A·R**
action_dist is Aggregation-dominated: it projects the full action sequence
onto a probability vector. The Restriction component reflects the finite
action space (R restricts the domain).

### Δ_emergent — Admissible Perturbations

The regime partition must remain stable under:

| ID | Perturbation |
|----|-------------|
| δ₁ | Random noise in the agent's perception of local zone features (up to magnitude η). |
| δ₂ | Different labyrinth instances with the same zone topology but different geometry. |
| δ₃ | Different random seeds for training. |
| δ₄ | Different RL hyperparameters within a reasonable range. |

δ₂ and δ₃ are the critical tests. A partition that depends on specific
training seeds or specific geometric arrangements of the maze is
environment-specific, not generalizable. Stability under δ₂ and δ₃ is
required for an admissible emergent partition.

### ε_emergent — Resolution Threshold

Two behavioral states x, y are indistinguishable under S_emergent if:

```
d_Π(x, y) ≤ ε_emergent
```

where d_Π is the L¹ distance over the action_dist observable.

ε_emergent is to be determined empirically via the ε-sweep pipeline,
following the same procedure as CASE-20260311-0001 (Kuramoto ε-sweep).

Working hypothesis: a robust ε-plateau exists at a regime count N matching
the number of structurally distinct zone types in the labyrinth.

---

## 3 Observable Range and Exclusion Zone

### R(action_dist) — Valid Region

action_dist is valid while:
- The agent is within a single zone type (A4 holds)
- The policy has converged for the current zone type (A_conv holds)
- The trajectory window is long enough for distributional estimation (A2 holds)

### Z(action_dist) — Exclusion Zone

Z(action_dist) ⊇ { trajectory windows spanning zone boundary crossings }

This is the behavioral analog of Z(r_ss) at κ_c in CASE-20260311-0001:
action_dist violates its stationarity assumption during zone transitions,
just as r_ss violates stationarity at the Kuramoto phase transition.

**F0 condition:** action_dist observed during zone-transition windows is
outside R(action_dist). These windows should be excluded from partition
computation. This is not a failure of the experiment; it is a structural
property of the observable.

---

## 4 Regime Partition Prediction

If H1 holds (regime emergence), the partition of S_emergent is expected to
have the following structure:

```
S_emergent
  ├── R_r   behavioral regime in zone type R (Restriction zones)
  ├── R_c   behavioral regime in zone type C (Coupling zones)
  ├── R_f   behavioral regime in zone type F (Forcing zones)
  └── [transition windows: no stable regime; F0 condition]
```

Each R_i is characterized by a distinct action_dist signature, reflecting
the behavioral strategy the agent has converged to within that zone type.

The BC class of each emergent regime R_i is a property of R_i as a
sub-scope of S_emergent — not a property of the agent. Per
`mode_scope_regime_audit.md` §2.5: BC classes are sub-scope properties
grounded in the S_emergent partition. Whether the BC class of R_i corresponds
to the BC class of the zone type it occupies is the content of H2.

---

## 5 Transfer Specification

Transfer experiments for the Emergent Modes Experiment follow the protocol
in `transfer_semantics_context_navigation.md`.

The relevant transfer type is **2.1 (transfer across labyrinth instances,
same observable)**:

```
S_training = (B_L_A, {action_dist}, Δ_emergent, ε_emergent)
S_transfer  = (B_L_B, {action_dist}, Δ_emergent, ε_emergent)
```

where L_A is the training labyrinth and L_B is an unseen labyrinth with
the same zone topology but different geometry.

Because both scopes use the same observable, Φ here measures primarily
**Φ_sys** — whether the behavioral partition generalizes across environments.

Admissibility verdict thresholds (from `transfer_semantics_context_navigation.md` §2.1):
- Φ ≥ 0.75: highly_admissible — the emergent behavioral partition generalizes
- Φ < 0.5: inadmissible — the partition is environment-specific

---

## 6 Comparison with S_global (Designed Modes Experiment)

| Feature | S_global (Designed Modes) | S_emergent (Emergent Modes) |
|---------|--------------------------|----------------------------|
| Agent architecture | Mode library M = {m₁,...,m_k} prescribed | Single unstructured policy |
| B: mode structure | B_g3: fixed mode library (Restriction) | B_e3: no mode library (Restriction on absence) |
| Primary observable | mode_dist: distribution over *prescribed* modes | action_dist: distribution over *actions* |
| Regime interpretation | Regime = partition cell corresponding to a prescribed mode | Regime = partition cell emerging from behavioral differentiation |
| Scientific question | How does the agent navigate between prescribed modes? | Does regime structure emerge without prescription? |
| ARW role | ARW as architecture design principle | ARW as observation instrument |

Both experiments use the same labyrinth environment and the same ARW
scope analysis pipeline. They are complementary, not competitive.

---

## 7 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-CNS-01 | What is ε_emergent? Requires ε-sweep on action_dist data. | open |
| Q-CNS-03 | Does consolidation produce asymptotic partition sharpening in the unstructured agent? (H4 ablation test) | open |
| Q-CNS-05 | Do the emergent regimes correspond to the BC classes predicted by bc_taxonomy_cognitive_modes? (H2) | open |
| Q-CNS-06 | What is the minimal fluctuation observable for emergent mode transitions? Does it show a Z_shared peak? | open |
| Q-CNS-08 | What is the empirical signature of scope failure (F1_BC) vs. regime transition in behavioral data? | open |
| Q-EMG-01 | Does the emergent partition arise gradually during training (asymptotic) or abruptly (phase-transition-like)? | open |
| Q-EMG-02 | Is the emergent partition richer than N = zone count? Could sub-zones produce finer-grained behavioral regimes? | open |
