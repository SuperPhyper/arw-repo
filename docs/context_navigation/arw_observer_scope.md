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
  - docs/advanced/observable_decomposition.md
---

# ARW Observer Scope — Behavioral Observables and Regime Detection

## Purpose

This document defines the **ARW observation scope** for the Emergent Modes
Experiment — the external measurement scope through which the ARW framework
observes the agent's behavioral output across runs.

It is the third of three scope-level documents in the multi-scope architecture:

| Document | Scope | What it covers |
|----------|-------|---------------|
| `agent_online_scope.md` | S_online | Agent perception and weight dynamics |
| `agent_sleep_scope.md` | S_sleep | Archetype revision and effectiveness evaluation |
| `arw_observer_scope.md` (this document) | S_observer | ARW-side observables on behavioral output |

**Critical distinction:** S_observer operates on the agent's *behavioral output*
(actions, trajectories, observable weight signatures) — not on the agent's
internal state (weight vector w(t), archetype library A, protocol buffer).
The agent's internal state is opaque to S_observer. Any correspondence between
internal state and observed behavioral regime structure is an empirical finding,
not a definitional truth.

S_observer **refines and extends** `context_navigation_scope_spec_emergent.md`.
That document defines S_emergent — the coarser ARW scope over the trained
agent's behavioral distribution (primary observable: `action_dist`). S_observer
adds a second observational layer: behavioral metrics that capture the weight
dynamics and archetype effects on the agent's behavior, observed externally.

---

## 1 Scope Definition

```
S_observer = (B_observer, Π_behavior, Δ_run, ε_cluster)
```

### B_observer — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_ob1 | S_observer has access only to externally observable behavioral data: trajectories, actions taken, labyrinth positions, zone membership at each step. Internal state (w, A, protocols) is not accessible. | Restriction |
| B_ob2 | Observation windows are bounded by zone membership: observables are computed within-zone (excluding transition steps, per F0 condition in S_emergent). | Restriction |
| B_ob3 | Observations are aggregated across multiple runs (different training seeds, different labyrinth instances). Run-level statistics are the primary unit of analysis. | Aggregation |
| B_ob4 | The zone topology of the labyrinth is known to S_observer. Zone-membership labels are available as ground-truth tags. | Coupling |

The primary BC class of S_observer is **Restriction** (limited access to
internal state) combined with **Aggregation** (run-level statistics).

---

## 2 Behavioral Observable Set — Π_behavior

The observables in Π_behavior are defined over behavioral trajectories of
the trained agent, observed externally. They project trajectory segments
onto measurable quantities without access to the agent's internal state.

Π_behavior is structured in two layers:

**Layer 1 — Primary behavioral distributions** (direct analogs of physical
system observables; feed into ε-sweep pipeline):

| Key | Definition | Observable BC notation | Primary? |
|-----|-----------|----------------------|---------|
| `action_dist` | Distribution over actions within a zone-episode window. `action_dist_i = count(a=i in W) / |W|` | A·R | yes |
| `trajectory_entropy` | Entropy of the action sequence within a zone window: `H = −sum(p_i · log p_i)` | A·R | no |
| `zone_return` | Cumulative reward per zone type per episode | R·A | no |

These are identical to the observables defined in S_emergent
(`context_navigation_scope_spec_emergent.md` §2). They are the primary
input to the ε-sweep pipeline.

**Layer 2 — Regime dynamics observables** (derived from behavioral patterns
across runs; not directly fed into ε-sweep but used for regime characterization
and correspondence analysis):

| Key | Definition | Observable BC notation |
|-----|-----------|----------------------|
| `salience_freq` | Frequency of saliency events per zone-episode window (events per step). Externally observable analog of internal encounter detection. | R·A |
| `action_switching_rate` | Rate of action-class transitions per step within a zone window: `trans_count / |W|` | R·A (Coupling signature) |
| `progress_efficiency_obs` | Externally computed progress efficiency per zone window: `Δd_exit(W) / steps(W)`. Analogous to `eff_norm` in S_sleep but computed from trajectory data without resource information. | R·S |
| `zone_dwell_time` | Mean number of steps per zone-episode visit, aggregated across runs | A·R |
| `regime_persistence` | Conditional probability that the behavioral regime at step t+1 is in the same cluster as at step t (estimated from action_dist cluster labels) | A·R (depends on partition result) |

### Observable Dependencies

`regime_persistence` depends on the partition result (cluster labels from the
ε-sweep). It is a **post-partition observable**: it can only be computed after
the ε-sweep has identified the regime partition. It is not a primary input to
the pipeline; it is a characterization metric for confirmed regimes.

`progress_efficiency_obs` is the externally observable analog of S_sleep's
`eff_norm`. The two quantities measure related but not identical things:
`eff_norm` uses resource consumption as the denominator (agent-internal);
`progress_efficiency_obs` uses step count (externally observable). Their
correspondence is an open question (Q-OB-01).

### Observable Range — Layer 2

| Observable | R(π) | Z(π) — known failure conditions |
|-----------|------|--------------------------------|
| `salience_freq` | Within-zone windows after policy convergence | At zone boundaries (transition windows); in early training (policy not converged) |
| `action_switching_rate` | Stable policy execution | At zone boundaries; during stuck trajectories (switching rate = 0 but for non-behavioral reasons) |
| `progress_efficiency_obs` | Within-zone windows with non-zero displacement | At zone boundaries; when agent is stationary (zero displacement); when `d_exit` gradient is flat |
| `zone_dwell_time` | Aggregated across ≥ N_min episodes | In early training (insufficient episodes); in novel zones |
| `regime_persistence` | Post-partition (requires cluster labels) | At regime boundaries (Z_shared analog: transitional behavior between regimes) |

**Z_shared for S_observer:**

All Layer 2 observables that assume stationary within-zone behavior share a
universal exclusion zone at zone boundary crossings — the behavioral analog of
Z_shared in the physical cases:

```
Z_shared(S_observer) = { trajectory windows spanning zone boundary crossings }

∀ π ∈ Π_behavior_L2:  Z(π) ⊇ Z_shared(S_observer)
```

This mirrors the Kuramoto result: all stationary-expectation observables fail
at the scope transition (phase transition / zone boundary crossing). A
behavioral fluctuation observable — the analog of χ = ∂r_ss/∂κ — would be
needed to characterize the transition windows themselves. See Q-OB-03.

---

## 3 Regime Detection Protocol

### 3.1 Primary Partition — ε-Sweep on action_dist

The primary regime detection procedure is the ε-sweep on `action_dist`,
as defined in `context_navigation_emergent_modes_experiment.md` §2.2.

This pipeline is shared with the physical system cases (Kuramoto, Doppelpendel,
Stuart-Landau) and produces:
- N(ε): number of distinguishable behavioral regime clusters
- Plateau structure and plateau widths
- Regime boundaries θ*

go/no-go criterion for H1: stable plateau at N ≥ 2, reproducible across
≥ 80% of training seeds.

### 3.2 Weight-Profile Clustering — Indirect Archetype Detection

If the agent's behavioral output is shaped by archetype-guided weight updates
(as specified in `agent_online_scope.md` §3), the weight dynamics should
leave indirect signatures in the behavioral observables — even though
S_observer cannot directly access w(t).

The following secondary analysis detects archetype-like clustering in
behavioral observables:

**Saliency co-occurrence analysis:**
Compute the empirical distribution of behavioral states immediately following
saliency events. If archetypes are operating, the post-saliency state should
cluster more tightly than the general within-zone behavioral distribution.

Metric: `KL(P(action_dist | post_saliency) || P(action_dist | general))`

If this divergence is significantly positive, the agent is behaviorally
differentiating at saliency events — consistent with archetype-guided weight
updates. If it is near zero, saliency events leave no behavioral signature.

**Run-level profile consistency:**
For each zone type, compute the variance of `action_dist` across runs
(different seeds). Low variance indicates a stable behavioral profile
across training runs — consistent with convergent archetype formation.
High variance indicates run-specific behavioral patterns (no stable archetypes).

Metric: `σ²(action_dist | zone_type)` aggregated across runs.

### 3.3 Effectiveness Correspondence Analysis

The externally observable `progress_efficiency_obs` can be compared against
the zone partition structure to assess whether the emergent regimes correspond
to zones with systematically different efficiency profiles.

If the ε-sweep produces N = 3 regimes (one per zone type), and `progress_efficiency_obs`
differs systematically across these three regimes, this provides evidence that:
1. The emergent partition is behaviorally meaningful (not just distributional artifact)
2. The agent's behavior adapts to the task-structure of each zone type

This analysis directly tests H2 from the external observation side.

---

## 4 Correspondence with S_online and S_sleep

S_observer cannot directly verify the agent's internal state. However, the
following structural correspondences can be tested empirically:

| Internal quantity (S_online / S_sleep) | External proxy (S_observer) | Testable correspondence |
|---------------------------------------|---------------------------|------------------------|
| Saliency event rate | `salience_freq` | High saliency_freq ↔ high encounter-event rate |
| Weight stability within encounter | `action_switching_rate` | Low switching ↔ stable weight profile |
| Archetype diversity `|A|` | Regime cluster count N | If N ≈ |A|, regimes ≈ archetypes |
| `eff_norm` per archetype | `progress_efficiency_obs` per regime | High eff archetype ↔ high efficiency regime |
| Sleep revision frequency | Run-to-run variance of `action_dist` | High revision ↔ high behavioral variance between runs |

None of these correspondences are guaranteed by design. They are empirical
predictions that can be tested once the experiment is run. Confirmation of
multiple correspondences would provide strong evidence that S_online, S_sleep,
and S_observer are detecting the same underlying regime structure from
different vantage points.

---

## 5 Δ_run — Admissible Perturbations

The behavioral regime partition detected by S_observer must remain stable under:

| ID | Perturbation |
|----|-------------|
| δ_ob1 | Different training seeds (same architecture, same environment) |
| δ_ob2 | Different labyrinth instances with same zone topology (different geometry) |
| δ_ob3 | Different RL hyperparameters within a reasonable range |
| δ_ob4 | Random noise in perceptual input to the agent (η-noise on Π_perception) |

δ_ob1 and δ_ob2 are the critical tests, identical to Δ_emergent in S_emergent.
A behavioral partition that does not survive different training seeds (δ_ob1)
is not an emergent property of the zone structure — it is a property of a
specific training trajectory.

---

## 6 Failure Mode Table

| ID | Condition | Severity | Interpretation |
|----|-----------|----------|---------------|
| F0 | Any observable computed during zone-transition windows (Z_shared violation) | observable_replacement | Exclude transition steps; this is expected, not a failure |
| F0-L2 | `regime_persistence` computed before partition exists | observable_replacement | Layer 2 observables require partition as prerequisite |
| F1 | `span(action_dist) < 2ε` across all zones | observable_replacement | Agent has not behaviorally differentiated; try `trajectory_entropy` |
| F1_BC | All observables in Π_behavior show span < ε | scope_rejection | Agent behavior is undifferentiated; zone structure has not induced behavioral differentiation; H1 falsified |
| F2 | Partition unstable under δ_ob1 (different training seeds) | scope_rejection | Emergent partition not robust; run-specific effect |
| F3 | No robust ε-plateau in N(ε) | scope_rejection | No stable behavioral regime structure; H1 falsified |
| F_corr | `progress_efficiency_obs` does not differ across regime clusters | interpretation | Regimes may be distributional artifact without task-structure grounding; H2 weakened |

---

## 7 Relation to Physical System Cases

S_observer is the cognitive-architecture analog of the ARW measurement scope
applied to physical systems. The structural parallels:

| Physical case | S_observer analog |
|--------------|------------------|
| r_ss in CASE-0001 (Kuramoto) | `action_dist` as order parameter for behavioral coherence |
| var_rel in CASE-0003 (Doppelpendel) | `trajectory_entropy` as variance-based behavioral diversity measure |
| χ = ∂r_ss/∂κ (fluctuation observable at κ_c) | Behavioral fluctuation observable at zone boundaries (to be defined; Q-OB-03) |
| ε-plateau width w in CASE-0001 | `zone_dwell_time` stability as behavioral regime robustness indicator |

The primary structural difference: in the physical cases, the system is
independent of the measurement. In the cognitive case, the agent is trained —
its behavior was shaped by a learning process. S_observer therefore measures
a system that has co-adapted to its environment, not a system with fixed dynamics.

This distinction does not undermine the ARW analysis but it changes its
interpretation: a confirmed regime partition in S_observer is evidence that
the training process produced generalizable behavioral structure, not merely
that a fixed physical system exhibits stable regimes.

---

## 8 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-OB-01 | How closely does `progress_efficiency_obs` (step-denominator) correspond to `eff_norm` (resource-denominator) in practice? If they diverge systematically across zone types, they carry structurally different information. | open |
| Q-OB-02 | Can saliency co-occurrence analysis (Section 3.2) detect archetype-guided weight updates from purely behavioral data? If yes, this provides an external consistency check on S_online without requiring access to internal state. | open |
| Q-OB-03 | What is the minimal behavioral fluctuation observable at zone boundaries — the analog of χ = ∂r_ss/∂κ for the cognitive case? Candidates: gradient of `action_dist` L1-distance across consecutive windows; variance of `action_switching_rate` near zone boundaries. | open |
| Q-OB-04 | Does the number of stable archetypes `|A|` (S_sleep) correspond to the number of regime clusters N (S_observer)? If N < |A|, the ARW partition is coarser than the agent's internal differentiation. If N > |A|, the agent has fewer archetypes than observable behavioral regimes. | open |
| Q-OB-05 | Is run-to-run variance of `action_dist` a valid proxy for sleep-phase revision activity? High variance between runs could reflect either ongoing archetype revision (healthy exploration) or archetype instability (pathological). Distinguishing these requires additional metrics. | open |
