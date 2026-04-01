---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
---

# Agent Online Scope — Perception, Encounter Protocol, and Weight Dynamics

## Purpose

This document defines the **online operational scope** of the context navigation
agent during active labyrinth traversal. It is one of three scope-level documents
constituting the multi-scope architecture of the Emergent Modes Experiment:

| Document | Scope | What it covers |
|----------|-------|----------------|
| `agent_online_scope.md` (this document) | S_online | Agent perception, weight dynamics, encounter protocol |
| `agent_sleep_scope.md` | S_sleep | Archetype revision, effectiveness evaluation |
| `arw_observer_scope.md` | S_observer | ARW-side observables on agent behavior across runs |

The three scopes are structurally distinct and must not be conflated.
S_online operates at each timestep during a run. S_sleep operates between
runs. S_observer is the external ARW measurement scope.

---

## 1 Scope Definition

```
S_online = (B_online, Π_perception, Δ_encounter, ε_w)
```

### B_online — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_ol1 | Agent operates within the finite labyrinth. Position x(t) ∈ L. | Restriction |
| B_ol2 | Agent perceives only local features within visibility radius r. No global map. | Restriction |
| B_ol3 | Weight vector w(t) is updated only at encounter events. Between events w(t) is constant. | Restriction |
| B_ol4 | Total weight is conserved: sum(w_i(t)) = 1 at all times. | Restriction |
| B_ol5 | Agent accumulates encounter protocols in a bounded buffer. Oldest protocol evicted when full. | Restriction |
| B_ol6 | Agent has read-only access to the archetype library A maintained by S_sleep. | Coupling |

---

## 2 Perception Observable Set — Π_perception

Seven normalized observables constitute the agent's perceptual space.
These are **inputs to the agent**, not observables over agent behavior.
Π_perception belongs to S_online. The ARW observer's Π_behavior
(defined in `arw_observer_scope.md`) operates on the agent's response
to these inputs — not on the inputs themselves.

All observables are normalized to [0, 1].

| Key | Name | Type | BC Signature |
|-----|------|------|--------------|
| `d_exit` | Distance to exit | scalar | R |
| `v_sight` | Visible free space | scalar | R·A |
| `e_edge` | Structure indicator | binary | R |
| `c_contact` | Contact indicator | binary | R |
| `m_cost` | Movement cost | scalar | R·S |
| `r_resource` | Remaining resource — **sole contingency variable** | scalar | R·S |
| `p_progress` | Progress rate | scalar | R·A |

**Single contingency variable:** `r_resource` is the sole ordering contingency
in the minimal experiment. It is the only observable that drives encounter
structure in a resource-relative sense. Additional contingency variables
are deferred to later phases.

**`p_progress` dependency:** `p_progress` is a function of `d_exit` over
a look-back window and is therefore not independent of other observables.
It is retained because it captures temporally integrated efficiency that
neither `d_exit` nor `r_resource` alone provides. It is not used as a
matching key in the archetype comparison.

**`ε_stab`:** The small stability constant in the `p_progress` denominator
is written `ε_stab` throughout to avoid collision with the ARW scope
resolution threshold ε.

### Observable vector

```
o(t) = [d_exit, v_sight, e_edge, c_contact, m_cost, r_resource, p_progress]
```

---

## 3 Saliency Events — Encounter Boundaries

A saliency event marks a suspected discontinuity in the functionally relevant
perceptual structure. It closes the current encounter and opens a new one,
triggering a weight update.

### 3.1 Minimal Saliency Triggers

Three triggers constitute the minimal saliency set:

| ID | Trigger | Signal | Type |
|----|---------|--------|------|
| `structure_loss` | `e_edge` transitions 1 → 0 | binary | binary |
| `resource_threshold` | `r_resource` crosses `θ_resource` downward | scalar | scalar |
| `progress_drop` | `p_progress` drops below `θ_progress` | scalar | scalar |

`contact_onset` is explicitly deferred from the minimal set.

When multiple triggers fire simultaneously, the highest-strength signal takes
precedence. If strength is tied (or both binary), the order of precedence is:
`structure_loss` > `resource_threshold` > `progress_drop`.

### 3.2 Saliency Strength

Saliency strength is defined only for **scalar triggers**. It is computed
as the encounter-relative gradient of the triggering observable: how much
did the observable change per unit of contingency variable consumed?

```
gradient_pct = |Δo_trigger / Δr_resource| × 100     [percentage]
```

where `Δo_trigger` is the change in the triggering observable over the last
k steps and `Δr_resource` is the corresponding change in `r_resource` over
the same window. This normalizes the observable's change against resource
consumption — a fast drop with little resource spent is stronger than the
same drop spread over a long, resource-heavy segment.

| gradient_pct | Strength class |
|-------------|----------------|
| 0 – 15% | weak |
| 15 – 45% | medium |
| > 45% | strong |

For **binary triggers** (`structure_loss`), strength is not defined.
Binary signals are recorded with `strength = None`.

### 3.3 Saliency Record

```
saliency = {
    type:     'structure_loss' | 'resource_threshold' | 'progress_drop',
    strength: 'weak' | 'medium' | 'strong' | None,
    t:        timestep of trigger
}
```

---

## 4 Weight Dynamics

### 4.1 Archetype Matching

The archetype library is **partitioned by saliency type**:

```
A = {
    'structure_loss':      [ archetype_0, archetype_1, ... ],
    'resource_threshold':  [ archetype_0, archetype_1, ... ],
    'progress_drop':       [ archetype_0, archetype_1, ... ]
}
```

At encounter onset, only the partition matching the current saliency type
is searched. Within that partition, matching is a **hard gate** — not a
similarity score, not a nearest-neighbor search:

```
match iff ALL of:
  1. saliency_strength == A_i.saliency_strength   (exact; or both None)
  2. |w_in - A_i.w_in|_inf <= θ_tolerance         (every weight dimension within tolerance)

If criterion 1 or criterion 2 fails for all archetypes in the partition:
    → NO MATCH. There is no fallback. No nearest archetype is used.
```

Default `θ_tolerance = 0.05` (5% of the [0,1] observable range).

**Why no fallback:** The tolerance boundary is the definition of the subscope
boundary. An encounter that falls outside tolerance represents a genuinely
different initial condition — not a noisy version of a known archetype.
Treating it as a match would conflate distinct subscopes. Near-miss archetypes
are candidates for later consolidation in S_observer, not online approximations.

**Tie-break:** If multiple archetypes satisfy both criteria exactly, the most
recently updated archetype wins (`last_updated` run index). Recency takes
priority over effectiveness in the online phase — effectiveness comparison
is S_sleep's responsibility.

### 4.2 Weight Update Rule

```
At encounter onset:

1. Record w_in = w(t)
2. Find match in archetype library (Section 4.1)
3. If match found:
     w_target = A_match.w_out + δ       [archetype-guided: contract toward w_out]
   Else:
     w_target = w(t) + δ               [exploratory: small drift from current]
4. Clip:      w_target_i = max(0.01, w_target_i)
5. Normalize: w_target   = w_target / sum(w_target)
6. Apply:     w(t) ← w_target
```

`δ_i ~ Uniform(-δ_max, δ_max)`, `δ_max = 0.05`.

**Structural interpretation (S4 — Dissipation):** The agent contracts toward
the archetype's `w_out` profile (the attractor). `δ` is the exploration
perturbation. In the absence of a matching archetype, the current weight
profile is the local attractor.

---

## 5 Encounter Protocol

An encounter is a delimited episode of navigation bounded by consecutive
saliency events.

### 5.1 w_in and w_out as First-Class Fields

`w_in` and `w_out` are the two primary structural fields of the encounter
protocol. They are not supplementary metadata — they are the core of what
the protocol records:

- **`w_in`** — the weight vector at encounter onset. This is the initial
  perceptual condition of the encounter. It is the matching key for archetype
  lookup. It defines which subscope the agent entered the encounter with.

- **`w_out`** — the weight vector at encounter close. This is what the agent
  carries into the next encounter. In the minimal setup (weights constant
  between saliency events, per B_ol3), `w_out == w_in`. Both fields are
  recorded separately to support future variants where intra-encounter
  weight drift is permitted.

Matching is based on `w_in` only. Evaluation may optionally consider
`Δw = w_out − w_in` to characterize adaptation within the encounter,
but this is deferred to later phases.

### 5.2 Protocol Record

At encounter close (next saliency event), record:

```
protocol(e) = {
    saliency_type:     type of the opening saliency event
    saliency_strength: strength of the opening saliency event (or None)
    C_in:              r_resource at encounter onset
    C_out:             r_resource at encounter close
    w_in:              weight vector at encounter onset       ← matching key
    w_out:             weight vector at encounter close       ← recommended exit weight
    progress_rate:     clip((d_exit(t_start) - d_exit(t_end)) / (steps + ε_stab), 0, 1)
}
```

Negative `progress_rate` values (agent moved away from exit) are clipped
to 0. No further penalty in the minimal version.

### 5.2 Buffer Management

Protocols accumulate in a buffer of capacity `max_protocols`. When full,
the oldest protocol is evicted (FIFO). The complete buffer is passed to
S_sleep at run end, then cleared.

---

## 6 Δ_encounter — Admissible Perturbations

| ID | Perturbation |
|----|-------------|
| δ_ol1 | Random noise in perceptual input up to magnitude η. |
| δ_ol2 | Variation in δ_max within a reasonable range. |
| δ_ol3 | Different initial weight vectors w(0). |
| δ_ol4 | Different random seeds for δ perturbations. |

---

## 7 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-OL-01 | Should negative progress_rate be penalized rather than clipped to 0? | open |
| Q-OL-02 | What is the right look-back window length for p_progress and gradient computation? | open |
| Q-OL-03 | Can saliency be triggered by internal signals (e.g. weight conflict) in addition to external triggers? | open |
| Q-OL-04 | Does θ_tolerance need to be adaptive as the archetype library matures? | open |
