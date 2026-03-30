---
status: experiment-proposal
layer: docs/context_navigation/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/advanced/observable_decomposition.md
  - docs/context_navigation/mode_scope_regime_audit.md
---

# Context Navigation — Emergent Modes Experiment

## Purpose

This document defines the **Emergent Modes Experiment** for the context-navigation
research strand of the ARW/ART repository.

The experiment addresses the following question directly:

> Can behavioral regime structure — interpretable as distinct cognitive modes —
> emerge from training in a structured environment, without being architecturally
> prescribed?

This is an ARW observation experiment, not an architecture design exercise.
The agent has no mode library, no explicit switching mechanism, and no
mode-labeled training signal. ARW is applied as a post-hoc observation
instrument to determine whether the trained policy's behavior partitions
into stable, distinguishable regimes.

---

## Relation to the Existing Context Navigation Experiment

This experiment is distinct from the **Designed Modes Experiment** documented in:

- `docs/context_navigation/context_navigation_model_spec.md`
- `docs/context_navigation/context_navigation_scope_spec.md`

In the Designed Modes Experiment, the agent is built with an explicit mode
library M = {m₁, ..., m_k} as architectural boundary condition B1. Modes are
prescribed; the experiment tests how well the agent navigates between them.

In this experiment, the agent has no prescribed modes. The experimental question
is whether ARW regime analysis reveals mode-like structure in the resulting
behavior — and whether that structure corresponds to the zone topology of
the environment.

The two experiments are complementary: the Designed Modes Experiment tests
navigation under known regime structure; the Emergent Modes Experiment tests
whether regime structure arises without design.

---

## 1 Experimental Setup

### 1.1 Environment

The labyrinth environment is retained from the Designed Modes Experiment.
It consists of a structured maze with structurally distinct zone types, each
enforcing different resource constraints, navigation rules, or reward signals.
Zone boundaries are discontinuous: crossing a boundary changes the active
constraint set.

The environment is unchanged. Its zone structure constitutes the BC-class
ground truth against which emergent regime structure will be compared.

See `docs/context_navigation/context_navigation_scope_spec.md` §1 for the
full zone type specification (zone types R, C, F).

### 1.2 Agent

The agent is a **single, unstructured policy** — for example a feedforward
or recurrent neural network trained by reinforcement learning.

**The agent has no:**
- mode library M
- explicit mode selector
- mode-labeled training signal
- modular subnetwork architecture
- consolidation phase (in the base variant)

The agent receives the same perceptual input as in the Designed Modes
Experiment: local zone features, resource state, available actions.
It produces actions. It is trained to maximize cumulative reward over
the labyrinth.

### 1.3 Training

Standard RL training (e.g., PPO or A2C) on the labyrinth environment.
No mode-specific reward shaping. No curriculum that explicitly introduces
zone types in sequence.

The training procedure is not prescribed in detail here; it is an
experimental degree of freedom. What matters is that no mode structure
is injected during training.

---

## 2 ARW Observation Protocol

After training, the agent's behavior is analyzed using ARW regime analysis.
The pipeline used is the same as for physical system cases (Kuramoto, Doppelpendel,
Stuart-Landau): ε-sweep, regime count extraction, partition stability analysis.

### 2.1 Behavioral Observable

The primary observable is derived from the agent's action distribution within
a context window:

```
π_action: (trajectory segment in zone z) → action_distribution_vector
```

This projects a behavioral trajectory onto a distributional representation.
It is an Aggregation-dominated observable (class A·R) — analogous to `var_rel`
in the physical cases, not to `r_ss`.

The sweep parameter is **context load** or **zone type index** — a parameter
that varies systematically across the trajectory.

**Observable range R(π_action):**
- Valid within zones where the agent's policy has converged.
- Violated during zone transitions (A4 stationarity assumption fails during
  boundary crossings).
- F0 condition expected at every zone boundary crossing, by the same argument
  as for `salience_mean` in `context_navigation_scope_spec.md` §5.

### 2.2 ε-Sweep

The ε-sweep is run over behavioral trajectory data collected from the trained
agent across many episodes.

The sweep produces:
- N(ε): number of distinguishable behavioral regimes as a function of ε
- Plateau structure: intervals of ε over which N is stable
- Regime boundaries θ*: the context parameter values at which N changes

The working hypothesis is that the plateau at the most robust N matches
the number of structurally distinct zone types in the labyrinth.

### 2.3 Partition Comparison

The emergent regime partition (from the ε-sweep) is compared against the
zone topology of the environment:

- Does N_stable match the number of zone types?
- Do regime boundaries θ* align with zone boundaries?
- Are the emergent regimes spatially coherent (each regime concentrated
  in a specific zone type)?

This comparison is the core empirical result of the experiment.

---

## 3 Formal Scope Specification

```
S_emergent = (B_emergent, Π_emergent, Δ_emergent, ε_emergent)
```

### B_emergent — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_e1 | The labyrinth is finite and fully connected. Agent position x(t) ∈ L. | Restriction |
| B_e2 | Zone membership determines active resource constraints. | Restriction |
| B_e3 | The agent is a single unstructured policy. No mode architecture. | Restriction |
| B_e4 | Agent perceives local zone features only (no global map). | Coupling |
| B_e5 | Reward signal is task-performance only; no mode-label signal. | Restriction |

The primary BC class of S_emergent is **Restriction** — the key boundary
condition is what the agent is *not* given (no mode structure), rather than
an active coupling or forcing term.

### Π_emergent — Admissible Observables

| Observable key | Description | Observable BC notation |
|---------------|-------------|----------------------|
| action_dist | Distribution over actions within a zone-episode window | A·R |
| trajectory_entropy | Entropy of the action sequence within a zone | A·R |
| zone_return | Cumulative reward per zone type | R·A |

Primary observable: **action_dist**
Secondary observable: **trajectory_entropy**

### Δ_emergent — Admissible Perturbations

| ID | Perturbation |
|----|-------------|
| δ₁ | Random noise in perceptual input (up to magnitude η) |
| δ₂ | Different labyrinth instances with same zone topology (different geometry) |
| δ₃ | Different random seeds for training |
| δ₄ | Different RL hyperparameters within a reasonable range |

δ₂ and δ₃ are the critical robustness tests: the emergent partition must be
stable across training runs and across unseen labyrinth geometries.

### ε_emergent — Resolution Threshold

To be determined empirically via ε-sweep on action_dist data.

Working hypothesis: a robust plateau exists at N matching the number of
zone types. ε_emergent is chosen as the center of that plateau.

---

## 4 Hypotheses

### H1 — Regime Emergence (primary hypothesis)

> Training in a structured multi-zone labyrinth produces a behavioral
> partition with N stable regimes, where N matches the number of structurally
> distinct zone types, even without architectural mode prescription.

**Falsification condition:** No robust ε-plateau exists, or the plateau N
does not match the zone count. → F3 condition: no stable behavioral regime
structure.

### H2 — BC-Class Correspondence

> The emergent regimes, when characterized by their dominant observable
> signatures, correspond to the BC classes of the zones in which they
> predominantly occur.

**Falsification condition:** Regime signatures do not correspond to the
predicted BC classes. → The regime structure is emergent but not BC-structured.
This would be a partial result: emergence confirmed, BC correspondence not.

### H3 — Transfer Generalization

> The emergent behavioral partition generalizes to unseen labyrinth
> instances with the same zone topology (Φ ≥ 0.75 under S_training → S_transfer).

**Falsification condition:** Φ < 0.5. → The emergent partition is
environment-specific; the agent has not learned generalizable behavioral regimes.

### H4 — Consolidation Ablation (secondary)

> Adding a consolidation phase to the unstructured agent produces a sharper
> regime partition (higher SDI, narrower transition windows) compared to
> the base variant without consolidation.

This hypothesis tests whether consolidation contributes to regime sharpening
independently of the mode architecture.
See Q-CNS-03 (revised interpretation: consolidation effects are asymptotic,
not step-like; expected signature is monotone approach to stable N over cycles).

---

## 5 Failure Mode Table

| ID | Condition | Severity | Interpretation |
|----|-----------|----------|---------------|
| F0 | action_dist observed during zone-transition window (A4 violated) | observable_replacement | Exclude transition steps from partition computation |
| F1 | span(action_dist) < 2ε across all zones | observable_replacement | Agent has not differentiated behavior across zones; try trajectory_entropy |
| F1_BC | span(ALL observables) < ε | scope_rejection | Agent behavior is undifferentiated; zone structure has not induced behavioral differentiation |
| F2 | Partition unstable under δ₃ (different training seeds) | scope_rejection | Emergent partition is not robust; training dynamics produce different regime structures |
| F3 | No robust ε-plateau | scope_rejection | No stable behavioral regime structure; H1 falsified |
| F4 | Regime boundary θ* at episode boundary | sweep_refinement | Extend episode length; rerun |

---

## 6 Connection to Open Questions

| Question ID | Connection |
|-------------|-----------|
| Q-CNS-03 | H4 directly tests whether consolidation produces asymptotic partition sharpening |
| Q-CNS-05 | H2 tests whether BC classes of zones produce the mode types predicted by bc_taxonomy_cognitive_modes — but now as an emergent result, not by design |
| Q-CNS-06 | If H1 is confirmed, Q-CNS-06 asks what the minimal fluctuation observable is for the emergent mode transitions |
| Q-CNS-08 | H1 falsification condition (F1_BC) is the empirical signature of scope failure vs. regime transition |

---

## 7 Relationship to Physical System Cases

The Emergent Modes Experiment is the cognitive-architecture analog of the
physical system cases in the ARW/ART case portfolio.

| Physical case | Cognitive analog |
|--------------|-----------------|
| CASE-20260311-0001 (Kuramoto) | Agent in coupling zone; action_dist ≅ r_ss as order parameter |
| CASE-20260311-0003 (Doppelpendel) | Agent in restriction zone; trajectory_entropy ≅ var_rel |
| CASE-20260318-0004 (Stuart-Landau) | Emergence condition: consolidation phase as K → K_c |

The primary distinction: in the physical cases, the observable is applied
to a physical system whose structure is independent of the observation.
In this experiment, the agent is *trained* — its behavior is shaped by the
training process. The ARW scope analysis is applied to a system that
co-evolved with its environment. This is a new experimental regime for
the framework.

---

## 8 Case Registration

When the experiment is run, results should be registered as a new case:

```
cases/CASE-YYYYMMDD-####/
```

The ScopeSpec.yaml should reference this document as the pre-pipeline
experiment definition. The primary observable key is `action_dist`.

The go_nogo verdict depends on H1: a stable ε-plateau at N matching the
zone count constitutes a `go` result. Absence of plateau is `no_go`.
