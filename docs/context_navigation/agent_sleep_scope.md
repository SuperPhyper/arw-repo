---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
---

# Agent Sleep Scope — Archetype Revision and Effectiveness Evaluation

## Purpose

This document defines the **sleep scope** of the context navigation agent —
the offline evaluation and consolidation phase that runs between active
labyrinth traversal runs. It is the second of three scope-level documents
in the multi-scope architecture of the Emergent Modes Experiment.

| Document | Scope | Operates |
|----------|-------|----------|
| `agent_online_scope.md` | S_online | At each timestep during a run |
| `agent_sleep_scope.md` (this document) | S_sleep | Between runs |
| `arw_observer_scope.md` | S_observer | Across runs (ARW external measurement) |

S_sleep is structurally **distinct from S_online**: it operates on accumulated
encounter protocols, not on perceptual observations. Its output is an updated
archetype library, which feeds back into S_online on the next run.

S_sleep is also distinct from S_observer: S_sleep is agent-internal
(the agent evaluates its own protocols); S_observer is external (ARW measures
the agent's behavioral output without access to internal state).

---

## 1 Scope Definition

```
S_sleep = (B_sleep, Π_evaluation, Δ_archetype, ε_eff)
```

### B_sleep — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_sl1 | S_sleep operates on the encounter protocol buffer accumulated during the preceding run. The buffer is read-only during sleep. | Restriction |
| B_sl2 | S_sleep has read and write access to the archetype library A. The library is frozen during S_online. | Coupling |
| B_sl3 | The archetype library has a bounded capacity: |A| ≤ A_max. If capacity is reached, the least-effective archetype is evicted before a new one is added. | Restriction |
| B_sl4 | The sleep phase is non-interactive: no new perceptual input is received during sleep. | Restriction |
| B_sl5 | The output of S_sleep is a revised archetype library A'. S_online on the next run reads A'. | Coupling |

The primary BC class of S_sleep is **Restriction** (bounded memory, frozen
buffer) coupled with **Coupling** (bidirectional connection to S_online via
archetype library A).

---

## 2 Evaluation Observables — Π_evaluation

The evaluation observables operate on the encounter protocol buffer, not on
individual timesteps. They project each protocol record onto scalar or vector
quantities that can be compared against archetype profiles.

| Key | Definition | BC Signature |
|-----|-----------|--------------|
| `eff_norm` | Normalized progress efficiency per encounter (defined in `agent_online_scope.md` §4.4) | R·S (ratio, normalized) |
| `weight_stability` | `1 − σ(w_i) / mean(w_i)` over the encounter — consistency of the weight profile during the encounter | A·S (aggregation over timesteps, scaled) |
| `encounter_duration` | `t_end − t_start` in steps — length of the encounter | R (direct measurement) |
| `archetype_coherence` | `cos(w_encounter, w(A_nearest))` — cosine similarity between the encounter weight profile and the weight profile of the nearest archetype | R·A (projection onto archetype space) |

**Primary evaluation observable: `eff_norm`**

Progress efficiency is the primary criterion for archetype revision. It is
directly task-relevant, interpretable without external labels, and computable
entirely from Π_perception quantities recorded in the protocol.

`weight_stability`, `encounter_duration`, and `archetype_coherence` are
secondary evaluation observables. They provide additional discriminating
information for the archetype revision decision and prevent revision based
on single high-efficiency encounters that may not be structurally robust.

### Pre-Scopal Substrate — eff_norm

| ID | Assumption | Violated when |
|----|-----------|---------------|
| A_buf | The protocol buffer contains a representative sample of the preceding run's encounters. | When the run is very short and the buffer contains fewer than min_protocols records. |
| A_conv | The encounter effectiveness is approximately stationary within the encounter window. | During encounters that span two environmental contexts (saliency event missed). |
| A_res | `resource_spent(e) > ε_stab`. | When the agent is nearly depleted (r_resource → 0) and encounters are resource-trivial. |

**Observable range R(eff_norm):**
Valid when A_buf, A_conv, and A_res hold. Violated when the buffer is
underpopulated or when encounters span multiple environmental contexts.
At minimum: `min_protocols = 5` (hyperparameter) required for meaningful
evaluation. Below this threshold, S_sleep should apply a **null revision**
(archetype library unchanged) rather than risk spurious updates.

---

## 3 Archetype Library

An **archetype** is a compressed representation of a family of similar
encounter contexts with historically effective weight profiles.

### 3.1 Archetype Record

```
archetype(A_i) = {
    signature:     sig(A_i)     // representative encounter signature (mean of family)
    weight:        w(A_i)       // weight profile associated with this archetype
    effectiveness: eff(A_i)     // running estimate of effectiveness (EMA)
    support:       n(A_i)       // number of encounters that contributed to this archetype
    last_updated:  run_id       // run index when this archetype was last revised
}
```

The archetype signature `sig(A_i)` lives in the encounter signature space
(the same space as `s(e)` in S_online). The archetype weight `w(A_i)` is the
weight profile that the archetype recommends for encounters matching its signature.

### 3.2 Archetype Initialization

The archetype library is initialized as empty: `A = {}`. The first run produces
encounter protocols that seed the library at the end of the first sleep phase.

If no archetypes exist, S_online falls back to exploratory updates:
```
w_target = w(t) + δ(e)
```
as specified in `agent_online_scope.md` §3.

---

## 4 Archetype Revision Protocol

The revision protocol runs once per sleep phase. It processes the encounter
protocol buffer and updates the archetype library A.

### 4.1 Protocol Filtering

Before revision, exclude protocols with:
- `encounter_duration` < min_duration (too short for reliable effectiveness estimation)
- `resource_spent` < ε_stab (resource-trivial encounters; eff_norm undefined)
- Any A_buf or A_conv violation flagged during the run

Remaining protocols form the **evaluation set** E for this sleep phase.

### 4.2 Signature Clustering

Group the evaluation set by encounter signature similarity:

```
For each e in E:
    A_nearest = argmin_{A_i ∈ A} dist(s(e), sig(A_i))
    If dist(s(e), sig(A_nearest)) < θ_match:
        assign e to archetype group G(A_nearest)
    Else:
        create candidate new archetype from e
```

This produces:
- **Matched groups**: encounter protocols assigned to existing archetypes
- **Candidate archetypes**: novel encounter signatures without an archetype match

### 4.3 Effectiveness Comparison — Matched Groups

For each matched group G(A_i), compute the group's mean effectiveness:

```
eff_group(A_i) = mean(eff_norm(e) for e in G(A_i))
```

Compare against the stored archetype effectiveness using an exponential moving
average update:

```
eff_updated(A_i) = α · eff_group(A_i) + (1 − α) · eff(A_i)
```

Where α ∈ (0, 1] is the learning rate (hyperparameter; default: 0.3).

**Weight revision decision:**

```
If eff_group(A_i) > eff(A_i) + θ_improve:
    w(A_i) ← mean(w(e) for e in G(A_i))   // update weight profile
    sig(A_i) ← mean(s(e) for e in G(A_i)) // update signature (online mean)
    eff(A_i) ← eff_updated(A_i)
    n(A_i) ← n(A_i) + |G(A_i)|
Else:
    eff(A_i) ← eff_updated(A_i)            // update effectiveness estimate only
    n(A_i) ← n(A_i) + |G(A_i)|             // increment support count
```

Where `θ_improve` is the minimum effectiveness improvement threshold
(hyperparameter; default: 0.05). This prevents revision on marginal improvements.

**Structural interpretation:** This revision rule has a **selective Dissipation
signature (S4)**: the archetype weight profile contracts toward the empirically
better-performing weight profile. The threshold `θ_improve` prevents contraction
toward marginally better attractors, ensuring only structurally significant
improvements drive revision.

### 4.4 Candidate Archetype Promotion

A candidate archetype (novel signature without an archetype match) is promoted
to the library if:

```
eff_norm(e_candidate) > θ_promote    AND
weight_stability(e_candidate) > θ_stability
```

Where:
- `θ_promote` is the minimum effectiveness for promotion (hyperparameter; default: 0.4)
- `θ_stability` is the minimum weight consistency required (hyperparameter; default: 0.5)

A single encounter with high effectiveness and stable weights is sufficient for
initial promotion. The promoted archetype has `n = 1` and will be consolidated
or evicted in future sleep phases depending on future encounter evidence.

### 4.5 Archetype Eviction

If `|A| = A_max` and a new archetype is to be promoted, evict the archetype
with the lowest effectiveness and lowest support:

```
A_evict = argmin_{A_i ∈ A} [eff(A_i) · log(1 + n(A_i))]
```

The product `eff · log(1 + n)` balances effectiveness against evidence count.
A low-effectiveness archetype with little support is evicted before a
low-effectiveness archetype that is well-supported — the latter may be
well-supported for structural reasons (e.g., an unavoidable low-efficiency zone).

---

## 5 Δ_archetype — Admissible Perturbations

The archetype revision must produce stable library updates under:

| ID | Perturbation |
|----|-------------|
| δ_sl1 | Variation in encounter ordering within the protocol buffer (order independence). |
| δ_sl2 | Different run lengths (more or fewer encounter protocols; bounded by min_protocols). |
| δ_sl3 | Noise in `eff_norm` within measurement uncertainty (numerical stability). |
| δ_sl4 | Different values of α (learning rate) within a reasonable range. |

A revision that produces qualitatively different archetype updates under
δ_sl1 (order dependence) is a structural failure of the revision protocol.

---

## 6 Connection to ARW Framework

S_sleep is the agent-internal analog of a **regime stabilization process**.
From the ARW perspective:

- The archetype library A is a compressed representation of the agent's
  experienced regime partition in encounter-signature space.
- The archetype revision protocol is a **discrete selection event** that
  determines which behavioral regimes (weight profiles) persist.
- This mirrors the ARW principle that regimes become identifiable when a
  stable partition is established under admissible perturbations.

S_sleep is not directly observable by S_observer (the ARW measurement scope).
S_observer sees the behavioral output of S_online (which is shaped by A),
not A itself. Whether the archetype library A corresponds to the emergent
behavioral partition detected by S_observer is an empirical question —
it is not guaranteed by construction.

This correspondence is the content of **H2** in
`context_navigation_emergent_modes_experiment.md`: if the archetypes cluster
by zone BC class, then the agent-internal representation and the ARW-observed
partition are in structural correspondence.

---

## 7 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-SL-01 | Should `eff_norm` be supplemented by a consistency-across-runs term? A weight profile that is effective but unstable across runs should be penalized relative to one that is reliably effective. | open |
| Q-SL-02 | Is the EMA update rate α appropriate, or should α decay over time (less revision as archetypes mature)? A decaying α would implement a stability-over-novelty bias in mature archetypes. | open |
| Q-SL-03 | What is the right `A_max`? If A_max equals the number of zone types, the library is constrained to match the zone structure. A larger A_max allows finer-grained archetypes; a smaller one forces coarse-graining. This is a scope decision, not an optimization problem. | open |
| Q-SL-04 | Can the archetype library serve as the ARW observer's indirect access to the agent's internal regime partition? If sig(A_i) clusters by zone type, this would confirm H2 from the agent-internal side without requiring behavioral trajectory analysis. | open |
| Q-SL-05 | At what point does the archetype library stabilize? The number of archetype revisions per sleep phase may serve as a convergence indicator — analogous to χ = ∂r_ss/∂κ in the Kuramoto case. | open |
