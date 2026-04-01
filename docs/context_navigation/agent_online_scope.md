---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/context_navigation_scope_spec_emergent.md
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
---

# Agent Online Scope — Perception, Encounter Protocol, and Weight Dynamics

## Purpose

This document defines the **online operational scope** of the context navigation
agent during active labyrinth traversal. It is one of three scope-level documents
constituting the multi-scope architecture of the Emergent Modes Experiment:

| Document | Scope | What it covers |
|----------|-------|---------------|
| `agent_online_scope.md` (this document) | S_online | Agent perception, weight dynamics, encounter protocol |
| `agent_sleep_scope.md` | S_sleep | Archetype revision, effectiveness evaluation |
| `arw_observer_scope.md` | S_observer | ARW-side observables on agent behavior across runs |

The three scopes are structurally distinct and must not be conflated:
S_online is agent-side and operates at each timestep; S_sleep is agent-side
and operates between runs; S_observer is the external ARW measurement scope.

This document is **not** a replacement for `context_navigation_scope_spec_emergent.md`.
That document defines S_emergent — the ARW observation scope over the trained
agent's behavioral distribution. S_online is the agent's internal perceptual and
computational scope during execution.

---

## 1 Scope Definition

```
S_online = (B_online, Π_perception, Δ_encounter, ε_w)
```

### B_online — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_ol1 | Agent operates within the finite labyrinth environment. Position x(t) ∈ L. | Restriction |
| B_ol2 | Agent perceives only local features within visibility radius r. No global map. | Restriction |
| B_ol3 | Agent maintains a weight vector w(t) over Π_perception. w(t) is updated only at encounter events. | Restriction |
| B_ol4 | Total weight is conserved: sum(w_i(t)) = 1 at all times. | Restriction |
| B_ol5 | Agent accumulates encounter protocols under a resource budget R(t). When R(t) → 0, no new protocols are stored. | Restriction |
| B_ol6 | Agent has read access to the archetype library A (maintained by S_sleep). Archetypes are read-only during online operation. | Coupling |

The primary BC class of S_online is **Restriction**: the central structural
conditions are what the agent cannot access (global map, prescribed modes,
unlimited memory) and what it must conserve (total weight).

---

## 2 Perception Observable Set — Π_perception

The agent's perceptual space is a fixed vector of seven normalized observables.
These are **inputs to the agent**, not observables over the agent's behavior.
This distinction is critical: Π_perception belongs to S_online; the ARW
observer's Π_behavior (defined in `arw_observer_scope.md`) operates on the
agent's response to Π_perception, not on Π_perception itself.

All observables are normalized to [0, 1].

| Key | Name | Definition | BC Signature |
|-----|------|-----------|--------------|
| `d_exit` | Distance to exit | `dist(x_t, x_exit) / D_max` | R (selection from spatial field) |
| `v_sight` | Visible free space | `visible_free_cells(t) / V_max` | R·A (aggregation over visible cells) |
| `e_edge` | Structure indicator | Binary: 1 if navigable structure present within radius r, 0 otherwise | R (projection) |
| `c_contact` | Contact indicator | Binary: 1 if blockage or forced contact detected, 0 otherwise | R (projection) |
| `m_cost` | Movement cost | `cost(x_t) / M_max` | R·S (scaling of local cost field) |
| `r_resource` | Remaining resource | `R(t) / R_0` — 1 = full, 0 = depleted | R·S (ratio, dissipative) |
| `p_progress` | Progress rate | `(d_exit(t−k) − d_exit(t)) / (resource_used_in_window + ε_stab)` normalized to [0,1] | R·A (derived, see note below) |

**Note on `p_progress`:** This observable is a function of `d_exit` and `r_resource`
over a window of length k. It is therefore **dependent** in the sense that it
is not independent of other Π_perception elements. It is retained because it
captures a temporally integrated quantity (efficiency) that neither `d_exit`
nor `r_resource` alone provides. It must not be used redundantly as a weight
selector alongside the observables it depends on.

**Note on `ε_stab`:** The `ε_stab` parameter in the `p_progress` denominator
is a numerical stability constant, not the ARW scope resolution threshold ε.
To avoid notational collision with the ARW framework, this constant is labeled
`ε_stab` throughout this document and must not be written as bare `ε`.

**Observable vector:**

```
o(t) = [d_exit, v_sight, e_edge, c_contact, m_cost, r_resource, p_progress]
```

### Observable Range and Exclusion Zones

| Observable | Z(π) — known failure condition |
|-----------|-------------------------------|
| `d_exit` | undefined if labyrinth is not fully connected (B_ol1 violation) |
| `v_sight` | degenerates to 0 when agent is fully enclosed (blind spot zones) |
| `p_progress` | F0 condition when `r_resource` → 0; denominator collapses; exclude from weighting when `r_resource < ε_stab` |
| `r_resource` | monotonically decreasing; not a stationary observable; valid only as directional signal |

---

## 3 Weight Dynamics

The agent maintains a weight vector w(t) = [w_1, ..., w_7] with sum(w_i) = 1.
Weights determine the **salience** of each observable in driving action selection:

```
o_weighted(t) = w(t) ⊙ o(t)
```

Weights are updated **only at encounter events** (see Section 4). Between
encounters, w(t) is held constant.

### Weight Update Rule

At encounter event e, the agent selects a target weight vector w_target using
the following priority rule:

```
1. Compute encounter signature s(e) from o(t) at encounter onset (see Section 4.2).
2. Find nearest archetype: A_nearest = argmin_{A_i ∈ A} dist(s(e), sig(A_i))
3. If dist(s(e), sig(A_nearest)) < θ_match:
     w_target = w(A_nearest) + δ(e)        [archetype-guided update]
   Else:
     w_target = w(t) + δ(e)                [exploratory update]
4. Normalize: w_target ← w_target / sum(w_target)
5. Apply: w(t) ← w_target
```

Where:
- `w(A_nearest)` is the weight profile stored with the nearest archetype
- `δ(e)` is a small stochastic perturbation vector, `|δ_i| ≤ δ_max`
- `δ_max` is a hyperparameter controlling exploration magnitude
- `θ_match` is the archetype similarity threshold
- `dist(·,·)` is L2 distance in the encounter signature space

**Structural interpretation:** This update rule has a **Dissipation signature
(S4)**: the agent contracts toward the archetype weight profile (the attractor),
with δ(e) as an exploration perturbation. In the absence of a matching
archetype, the current weight profile serves as the local attractor.

The archetype library A is managed by S_sleep and is read-only during S_online.
The agent does not create or modify archetypes during online operation.

---

## 4 Encounter Protocol

An **encounter** is a delimited episode of navigation within a single
encounter context, bounded by saliency events.

### 4.1 Saliency Events — Encounter Boundaries

A saliency event marks a suspected discontinuity in the functionally relevant
perceptual structure. Saliency events trigger:
1. Closure of the current encounter protocol
2. Onset of a new encounter (weight update as per Section 3)

Saliency events are detected by threshold-crossing of the following signals:

| Signal | Trigger condition | BC class of trigger |
|--------|-----------------|---------------------|
| Structure loss | `e_edge` transitions 1 → 0 | Restriction (loss of navigable structure) |
| Resource threshold | `r_resource` crosses `θ_resource` (default: 0.25) | Restriction (resource constraint onset) |
| Progress drop | `p_progress` drops below `θ_progress` (default: 0.1) | Restriction + Dissipation (efficiency collapse) |
| Contact onset | `c_contact` transitions 0 → 1 | Restriction (hard blockage) |

Saliency signals are classified by gradient magnitude of the triggering
observable: S ∈ {weak, medium, strong}. Strong signals take precedence when
multiple signals co-occur.

**Note:** Saliency events are detectible by both the agent (as encounter
boundaries) and by S_observer (as candidate regime-transition markers). This
dual role is intentional: saliency events are the shared vocabulary between
agent-internal structure and ARW observation.

### 4.2 Encounter Signature

At the onset of each encounter (immediately after a saliency event), the agent
records an encounter signature:

```
s(e) = o(t_onset)    [raw observation vector at encounter onset]
```

The encounter signature is the basis for archetype matching (Section 3).
It characterizes the environmental context at the moment the encounter begins,
not the agent's response to it.

### 4.3 Encounter Protocol Record

For each completed encounter e, the agent records:

```
protocol(e) = {
    signature:        s(e)              // observation vector at onset
    weight_profile:   w(e)              // weight vector used during encounter
    effectiveness:    eff(e)            // scalar effectiveness measure (see below)
    duration:         t_end - t_start   // encounter length in steps
    resource_spent:   R(t_start) - R(t_end)
}
```

Encounter protocols are accumulated in a **temporary buffer** during the run.
The buffer capacity is bounded (hyperparameter: `max_protocols`). When the
buffer is full, the oldest protocol is evicted. The buffer is consumed by
S_sleep at the end of the run.

### 4.4 Effectiveness Measure

The effectiveness of an encounter is measured by **progress efficiency** —
the ratio of exit-distance reduction to resource consumed:

```
eff(e) = Δd_exit(e) / resource_spent(e)
       = (d_exit(t_start) − d_exit(t_end)) / (R(t_start) − R(t_end) + ε_stab)
```

Normalized to [0, 1] using the maximum observed effectiveness across the
current run:

```
eff_norm(e) = clip(eff(e) / eff_max_run, 0, 1)
```

**Design rationale:** Progress efficiency was selected as the primary effectiveness
measure because it is directly task-relevant (progress toward the exit) and
resource-aware (penalizes costly navigation). It avoids binary outcome measures
(reached exit / did not reach exit) that would discard structural information
about partial success. It is computed entirely from within Π_perception
without requiring external labels.

**Known limitation:** eff(e) can be negative if the agent moves away from the
exit. Negative values are clipped to 0. This discards information about
counterproductive encounters; the agent does not penalize itself, it merely
records zero effectiveness. Whether this is appropriate is noted as
open question Q-OL-01 (see Section 6).

---

## 5 Δ_encounter — Admissible Perturbations

The weight dynamics and encounter protocol must remain functionally stable under:

| ID | Perturbation |
|----|-------------|
| δ_ol1 | Random noise in perceptual input `o(t)` up to magnitude η (sensor noise). |
| δ_ol2 | Variation in `δ_max` within a reasonable range (exploration robustness). |
| δ_ol3 | Different initial weight vectors w(0) (initialization independence). |
| δ_ol4 | Different random seeds for δ(e) perturbations (stochasticity robustness). |

A weight profile that is stable under δ_ol3 and δ_ol4 is a candidate for
archetype formation (evaluated by S_sleep).

---

## 6 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-OL-01 | Should negative effectiveness (agent moves away from exit) be penalized rather than clipped to 0? A penalty would create a directional signal discouraging exploration-by-regression. | open |
| Q-OL-02 | What is the right window length k for `p_progress` estimation? Too short: noisy; too long: misses encounter-scale dynamics. | open |
| Q-OL-03 | Can a saliency event be triggered internally (e.g., by weight instability or effectiveness drop) in addition to external triggers? Internal saliency would close the encounter before environmental change occurs. | open |
| Q-OL-04 | Does the archetype similarity threshold `θ_match` need to be adaptive? A fixed threshold may miss archetypes in early training (few encounters) or admit too many spurious matches later. | open |
