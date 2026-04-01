---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/agent_sleep_scope.md
  - docs/context_navigation/context_navigation_scope_spec_emergent.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
---

# ARW Observer Scope — Behavioral Observables and Regime Detection

## Purpose

This document defines the **ARW observation scope** for the Emergent Modes
Experiment — the external measurement scope through which the ARW framework
observes the agent's behavioral output across runs.

It is the third of three scope-level documents in the multi-scope architecture:

| Document | Scope | What it covers |
|----------|-------|----------------|
| `agent_online_scope.md` | S_online | Agent perception and weight dynamics |
| `agent_sleep_scope.md` | S_sleep | Archetype revision and effectiveness evaluation |
| `arw_observer_scope.md` (this document) | S_observer | ARW-side observables on behavioral output |

**Critical distinction:** S_observer operates on the agent's *behavioral output*
(actions, trajectories, observable patterns across runs) — not on the agent's
internal state (w(t), archetype library A, protocol buffer). The agent's
internal state is opaque to S_observer. Any correspondence between internal
structure and observed behavioral regime structure is an empirical finding.

**Primary scientific question:** Do stable behavioral regimes emerge — detectable
by standard ARW regime analysis — from an agent operating under the three-scope
architecture? The answer does not presuppose alignment with any particular
environmental structure.

---

## 1 Scope Definition

```
S_observer = (B_observer, Π_behavior, Δ_run, ε_cluster)
```

### B_observer — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_ob1 | S_observer has access only to externally observable behavioral data: trajectories, actions, positions, saliency event timestamps. Internal state is not accessible. | Restriction |
| B_ob2 | Observation windows are saliency-bounded: observables are computed within encounter windows, not zone windows. | Restriction |
| B_ob3 | Observations are aggregated across multiple runs. Run-level statistics are the primary unit of analysis. | Aggregation |
| B_ob4 | The zone topology of the labyrinth is available as ground-truth metadata for secondary analysis only. | Coupling |

**B_ob2 is the key difference from S_emergent** (`context_navigation_scope_spec_emergent.md`):
S_emergent segments by zone membership; S_observer segments by saliency-bounded
encounter windows. The encounter window is the natural unit of the three-scope
architecture. Zone alignment is a secondary analysis, not a primary segmentation
criterion.

---

## 2 Behavioral Observable Set — Π_behavior

### Layer 1 — Primary Observables (ε-sweep input)

| Key | Definition | Observable BC notation | Primary? |
|-----|-----------|----------------------|---------|
| `action_dist` | Distribution over actions within a saliency-bounded encounter window | A·R | yes |
| `trajectory_entropy` | Entropy of the action sequence within an encounter window | A·R | no |

`action_dist` is the primary observable for the ε-sweep, as in S_emergent.
The segmentation unit changes (encounter window instead of zone window) but
the observable definition and distance metric (L1) are unchanged.

### Layer 2 — Regime Dynamics Observables (post-partition characterization)

These observables are computed after the ε-sweep produces a partition.
They characterize identified regimes and test correspondences. They are
**not** fed into the ε-sweep pipeline.

| Key | Definition |
|-----|-----------|
| `saliency_type_dist` | Distribution over saliency types within each regime cluster |
| `saliency_strength_dist` | Distribution over saliency strength classes within each regime cluster |
| `progress_rate_obs` | Externally computed progress efficiency per encounter window: `Δd_exit / window_length` |
| `regime_persistence` | Conditional probability that the next encounter window falls in the same regime cluster |
| `archetype_library_size` | Number of archetypes per saliency-type partition, logged per run (debug / correspondence) |

**`archetype_library_size`** is logged for correspondence analysis only. It is
an indirect probe of S_sleep activity, not a behavioral observable in the
strict sense. It must be clearly marked as debug data, not as primary evidence.

**`progress_rate_obs`** uses step count as the denominator (externally
observable). This differs from S_sleep's `progress_rate` which uses
`steps + ε_stab`. The two quantities are related but not identical.

### Observable Range — Layer 2

| Observable | Z(π) — failure conditions |
|-----------|--------------------------|
| `saliency_type_dist` | Encounter windows with ambiguous or missed saliency detection |
| `progress_rate_obs` | Encounter windows where d_exit gradient is flat (agent near equidistant position) |
| `regime_persistence` | At regime boundaries; requires partition as prerequisite |

**Z_shared for S_observer:**

All Layer 2 observables that assume stationary within-encounter behavior share
a universal exclusion zone at encounter boundaries — the behavioral analog of
Z_shared in the physical cases:

```
Z_shared(S_observer) = { timesteps at saliency events }

∀ π ∈ Π_behavior_L2:  Z(π) ⊇ Z_shared(S_observer)
```

At saliency events, the agent's weight vector is in transition. All
stationary-expectation observables fail there. A behavioral fluctuation
observable would be needed to characterize the transition itself (Q-OB-03).

---

## 3 Regime Detection Protocol

### 3.1 Segmentation

Segment behavioral trajectories into **encounter windows** using logged
saliency event timestamps. Each encounter window spans from one saliency
event to the next. Exclude the timestep of the saliency event itself
from both the closing and opening window.

Minimum window size: 10 steps (discard shorter windows as unreliable).

### 3.2 ε-Sweep on action_dist

Apply the existing ε-sweep pipeline to the `action_dist` vectors from
all valid encounter windows, following the standard ARW procedure:

- Distance metric: L1
- Sweep range: [0.01, 1.0], 50 log-spaced points
- Output: N(ε), plateau structure, regime boundaries θ*

**go/no-go criterion for H1:**
A stable ε-plateau at N ≥ 2, reproducible across ≥ 80% of training seeds,
constitutes a `go` verdict. The specific value of N is not prescribed — what
matters is that a stable partition exists at all.

N = 3 (matching zone count) is one possible outcome and would support H2,
but it is not a requirement for H1. A plateau at N = 2 or N = 5 would still
confirm H1 if reproducible. The regime count is a finding, not a target.

### 3.3 Post-Partition Characterization (if H1 confirmed)

For each identified regime cluster R_i, compute:

**Saliency correspondence:**
```
P(saliency_type = s | regime = R_i)   for s in {structure_loss, resource_threshold, progress_drop}
```
If regimes are structured by encounter type, each cluster should be dominated
by one saliency type. This is a finding — not a requirement.

**Effectiveness correspondence:**
```
mean(progress_rate_obs | regime = R_i)
```
If regimes correspond to structurally different encounter contexts, effectiveness
should differ systematically across clusters.

**Zone correspondence (secondary — labeled explicitly as such):**
```
P(zone_type = z | regime = R_i)   for z in {R, C, F}
```
Zone alignment is one possible explanation for regime structure. It is not the
primary hypothesis. Regimes that do not align with zones are equally valid
findings — they indicate that the agent's subscope structure diverges from the
environmental scaffold.

### 3.4 Subscope Reconstruction (post-partition, separate analysis)

After the regime partition is established, reconstruct the observable subscope
associated with each archetype in the library using the threshold rule:

```
subscope(A_i) = { o_j | w_j(A_i) > θ_w }
```

where `w_j(A_i)` is the j-th component of the archetype's `w_in` vector
and `θ_w` is the subscope threshold (default: `θ_w = 0.15`).

This reconstruction is applied to **each archetype individually** — it does
not require the ε-sweep partition as a prerequisite. It runs on the archetype
library directly.

The result is a set of observable subsets, one per archetype. These are the
candidate emergent subscopes. Whether archetypes that produce the same subscope
(same dominant observables) correspond to the same regime cluster is then
compared against the ε-sweep partition — that comparison is the empirical
content of H2.

**Why this order matters:** Subscope reconstruction from archetypes is
agent-internal structure made visible. Regime detection from action_dist is
behavioral structure observed externally. The correspondence between the two
is the finding — not an assumption.

---

## 4 Failure Mode Table

| ID | Condition | Severity | Interpretation |
|----|-----------|----------|---------------|
| F0 | Any observable computed at saliency event timesteps (Z_shared violation) | observable_replacement | Exclude saliency timesteps from window computation |
| F0-L2 | `regime_persistence` computed before partition exists | observable_replacement | Layer 2 observables require partition as prerequisite |
| F1 | `span(action_dist) < 2ε` across all encounter windows | observable_replacement | Agent behavior undifferentiated at encounter level; try trajectory_entropy |
| F1_BC | All observables in Π_behavior show span < ε | scope_rejection | No stable behavioral differentiation; H1 falsified |
| F2 | Partition unstable under δ_ob1 (different training seeds) | scope_rejection | Emergent partition not robust; run-specific |
| F3 | No robust ε-plateau in N(ε) | scope_rejection | No stable behavioral regime structure; H1 falsified |

---

## 5 Relation to S_emergent

S_observer refines S_emergent (`context_navigation_scope_spec_emergent.md`)
in one key structural dimension:

| Feature | S_emergent | S_observer |
|---------|-----------|-----------|
| Segmentation unit | Zone-membership window | Saliency-bounded encounter window |
| Primary success criterion | Plateau at N = zone count | Plateau at N ≥ 2 (count is a finding) |
| Zone alignment | Primary analysis | Secondary analysis |
| Architecture | General emergent modes experiment | Three-scope architecture specifically |

S_emergent remains valid as the scope for the general Emergent Modes Experiment.
S_observer is the specific observation scope for the three-scope architecture
variant where S_online and S_sleep are active components.

---

## 6 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-OB-01 | How closely does progress_rate_obs (step-denominator) correspond to S_sleep's progress_rate (ε_stab-denominator) across encounter types? | open |
| Q-OB-02 | Can saliency_type_dist per regime cluster serve as an indirect verification of S_online's encounter structure without accessing internal state? | open |
| Q-OB-03 | What is the minimal behavioral fluctuation observable at saliency events — the analog of χ = ∂r_ss/∂κ for the cognitive case? | open |
| Q-OB-04 | Does archetype_library_size per partition correspond to the regime cluster count per saliency type in the ε-sweep? | open |
