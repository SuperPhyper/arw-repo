---
status: experiment-proposal
layer: experiments/
depends_on:
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/agent_sleep_scope.md
  - docs/context_navigation/arw_observer_scope.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/context_navigation_scope_spec_emergent.md
  - cases/CASE-20260330-0012/ScopeSpec.yaml
---

# Minimal Experiment Setup — Three-Scope Architecture
## Emergent Modes Experiment: S_online / S_sleep / S_observer

This document defines the **minimal runnable configuration** of the Emergent
Modes Experiment as specified in the three-scope architecture:

- `agent_online_scope.md` — S_online: perception, weight dynamics, encounter protocol
- `agent_sleep_scope.md`  — S_sleep: archetype revision, effectiveness evaluation
- `arw_observer_scope.md` — S_observer: ARW-side behavioral regime detection

The goal of the minimal setup is to produce the first empirical data as quickly
as possible with the fewest moving parts. Every component that is not strictly
necessary to test H1 is deferred.

This document is **execution-oriented**. For theoretical grounding and scope
formalization, see the documents listed above and
`context_navigation_emergent_modes_experiment.md`.

---

## 1 What "Minimal" Means Here

A minimal experiment answers one question:

> Does a stable behavioral regime partition emerge from the three-scope
> architecture — detectable by S_observer — without prescribing modes?

Everything else (transfer generalization H3, consolidation ablation H4,
BC-class correspondence H2) is deferred to subsequent phases.

**Minimal means:**
- Smallest labyrinth that produces structurally distinct zones
- Simplest possible agent architecture
- Only the observables strictly required for the ε-sweep
- Only the sleep-phase machinery strictly required to produce archetype-guided behavior
- One training seed first; reproducibility testing comes later

**Not minimal means (deferred):**
- Multi-seed reproducibility (δ_ob1)
- Cross-labyrinth transfer (δ_ob2, H3)
- Consolidation ablation (H4)
- Layer-2 observer observables (salience_freq, action_switching_rate, etc.)
- Full archetype library tuning

---

## 2 Environment — Minimal Labyrinth

### 2.1 Grid

A 9×9 discrete grid with three zone types arranged in distinct spatial regions:

```
+--Zone R--+--Zone C--+--Zone F--+
|          |          |          |
| (3x9)    | (3x9)    | (3x9)    |
|          |          |          |
+----------+----------+----------+
```

- **Zone R (Restriction):** Left third of the grid. High movement cost
  (`c = 0.5` per step). Tight action constraints: only 2 of 4 directional
  actions are permitted per cell (determined by wall layout). No traps.

- **Zone C (Coupling):** Center third. Low movement cost (`c = 0.1`).
  Navigation targets (coupling anchors) are visible within radius r.
  Reward shaping: small positive reward for moving toward visible targets.

- **Zone F (Forcing):** Right third. Medium movement cost (`c = 0.3`).
  Directional forcing field: one action direction receives a reward bonus
  at each cell (the direction of the forcing field, constant within Zone F).

**Exit:** Fixed at the rightmost column of Zone F. The agent's primary task
is to reach the exit.

**Zone boundaries:** Discrete — crossing from column 3 to column 4
(R→C boundary) or column 6 to column 7 (C→F boundary) triggers the
zone-membership change.

### 2.2 Why This Layout

Three zones correspond to the three BC classes in the existing scope
specification (R, C, F). The spatial separation is sharp — no blended
transition regions in the minimal setup. This maximizes the probability
that behavioral differentiation, if it occurs, aligns with zone boundaries.

The asymmetry (Zone R is hardest, Zone F leads to exit) creates a natural
resource gradient that gives `p_progress` and `eff_norm` meaningful signal
across zones.

### 2.3 Implementation Notes

- Grid size: 9×9 cells
- Discrete action space: A = {up, down, left, right}, |A| = 4
- Per-step reward: `-c(zone)` (movement cost) + task reward at exit
- Exit reward: +10
- Episode termination: exit reached OR step limit T_max = 200 steps
- Zone-membership: determined by grid column (columns 0–2: R, 3–5: C, 6–8: F)

---

## 3 Agent Architecture — Minimal Policy

### 3.1 Network

A **two-layer feedforward neural network** (no recurrence in the minimal
setup):

```
Input:  o_weighted(t) = w(t) ⊙ o(t)     [7-dimensional weighted observation]
Hidden: Linear(7 → 32) → ReLU
Output: Linear(32 → 4) → Softmax        [action probability distribution]
```

The input is the **weighted perception vector** from S_online, not the raw
observation vector. This is the minimal integration point between S_online
and the policy network.

The raw observation vector `o(t) = [d_exit, v_sight, e_edge, c_contact, m_cost,
r_resource, p_progress]` is computed from the environment state at each step.
The weight vector `w(t)` is maintained by S_online and updated at encounter
events (see Section 5).

### 3.2 Training

- Algorithm: **PPO** (Proximal Policy Optimization), standard implementation
- Training steps: 500,000 (adjustable; stop early if policy converges)
- Discount factor: γ = 0.99
- Entropy coefficient: 0.01 (prevents premature determinism)
- Learning rate: 3 × 10⁻⁴
- Batch size: 2048 steps
- No curriculum; all three zones present from the first training episode

**Critical:** Standard PPO operates on the policy output (action probabilities).
The weight vector w(t) is maintained by S_online, not learned by the RL
optimizer. This separation is constitutive: the optimizer shapes the policy
given whatever weighted input it receives; S_online shapes the weighting
given encounter history and archetypes.

---

## 4 Observable Vector — Π_perception (S_online)

The seven observables from `agent_online_scope.md` §2, computed at each step:

| Key | Computation | Notes |
|-----|------------|-------|
| `d_exit` | `manhattan_dist(x_t, x_exit) / D_max` | D_max = 16 (9×9 grid diagonal) |
| `v_sight` | `count(free cells within r=3) / V_max` | V_max = 28 (max free cells at r=3) |
| `e_edge` | `1 if any wall within r=1, else 0` | Detects structural boundaries |
| `c_contact` | `1 if last action resulted in no movement, else 0` | Detects blockage |
| `m_cost` | `c(zone_membership(x_t)) / M_max` | M_max = 0.5 (Zone R cost) |
| `r_resource` | `steps_remaining / T_max` | Proxy for resource; decreases monotonically |
| `p_progress` | `(d_exit(t−5) − d_exit(t)) / (5 + ε_stab)` | Window k=5 steps; ε_stab = 0.01 |

**Note on `r_resource`:** In the minimal setup, resource is operationalized as
remaining step budget (steps_remaining / T_max), not an explicit consumable.
This avoids implementing a separate resource system while preserving the
structural role of `r_resource` as a dissipating quantity.

**Note on `p_progress`:** Window k=5 is the minimal window that produces a
meaningful signal. At k=5, `p_progress` measures progress over the last 5
steps relative to the maximum possible progress. Negative values are clipped
to 0 as specified in `agent_online_scope.md` §4.4.

---

## 5 S_online: Weight Dynamics and Encounter Protocol

### 5.1 Initial Weights

```
w(0) = [1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7]    [uniform initialization]
```

### 5.2 Saliency Detection

At each step, evaluate the following saliency signals (from `agent_online_scope.md` §4.1):

```python
def detect_saliency(o_prev, o_curr):
    signals = []
    if o_prev['e_edge'] == 1 and o_curr['e_edge'] == 0:
        signals.append(('structure_loss', 'strong'))
    if o_prev['r_resource'] >= theta_resource and o_curr['r_resource'] < theta_resource:
        signals.append(('resource_threshold', 'medium'))
    if o_curr['p_progress'] < theta_progress:
        signals.append(('progress_drop', 'weak'))
    if o_prev['c_contact'] == 0 and o_curr['c_contact'] == 1:
        signals.append(('contact_onset', 'medium'))
    return signals   # empty list = no saliency event
```

Minimal parameters: `theta_resource = 0.25`, `theta_progress = 0.1`

If `signals` is non-empty, a saliency event is triggered and the current
encounter is closed.

### 5.3 Weight Update at Encounter Event

```python
def update_weights(w_current, o_onset, archetype_library, delta_max=0.05):
    s_encounter = o_onset                          # encounter signature = observation at onset
    A_nearest, dist_nearest = find_nearest_archetype(s_encounter, archetype_library)

    if A_nearest is not None and dist_nearest < theta_match:
        w_target = A_nearest['weight'].copy()      # archetype-guided
    else:
        w_target = w_current.copy()                # exploratory

    # small stochastic perturbation
    delta = np.random.uniform(-delta_max, delta_max, size=7)
    w_target = w_target + delta
    w_target = np.clip(w_target, 0.01, None)       # no zero or negative weights
    w_target = w_target / w_target.sum()           # normalize
    return w_target
```

Minimal parameters: `delta_max = 0.05`, `theta_match = 0.3` (L2 distance in
7-dimensional observation space).

### 5.4 Encounter Protocol Recording

At encounter close (saliency event), record:

```python
protocol = {
    'signature':       o_onset,                    # observation at encounter start
    'weight_profile':  w_encounter,                # weight used during encounter
    'effectiveness':   compute_eff(d_exit_start, d_exit_end, steps_used),
    'duration':        steps_in_encounter,
    'resource_spent':  r_resource_start - r_resource_end
}
buffer.append(protocol)
```

Buffer capacity: `max_protocols = 50` per run.

```python
def compute_eff(d_start, d_end, steps, eps_stab=0.01):
    delta_d = d_start - d_end              # progress toward exit (positive = good)
    eff = delta_d / (steps + eps_stab)
    return max(0.0, eff)                   # clip negative values to 0
```

---

## 6 S_sleep: Archetype Revision (Minimal)

The minimal sleep phase runs once per run (after episode termination or step
limit). It processes the protocol buffer and updates the archetype library.

### 6.1 Minimal Revision Loop

```python
def sleep_phase(buffer, archetype_library, alpha=0.3,
                theta_improve=0.05, theta_promote=0.4,
                theta_stability=0.5, min_protocols=5):

    if len(buffer) < min_protocols:
        return archetype_library              # null revision — insufficient data

    # Filter protocols (minimum duration)
    valid = [p for p in buffer if p['duration'] >= 5 and p['resource_spent'] > 0.01]

    for proto in valid:
        A_nearest, dist = find_nearest_archetype(proto['signature'], archetype_library)

        if A_nearest is not None and dist < theta_match:
            # --- Matched: update existing archetype ---
            eff_group = proto['effectiveness']
            eff_prev  = A_nearest['effectiveness']
            eff_new   = alpha * eff_group + (1 - alpha) * eff_prev

            if eff_group > eff_prev + theta_improve:
                # Revision: update weight and signature
                A_nearest['weight']        = proto['weight_profile'].copy()
                A_nearest['signature']     = proto['signature'].copy()
            A_nearest['effectiveness'] = eff_new
            A_nearest['support']      += 1

        else:
            # --- Unmatched: candidate for promotion ---
            stability = compute_weight_stability(proto['weight_profile'])
            if (proto['effectiveness'] > theta_promote and
                    stability > theta_stability):
                new_archetype = {
                    'signature':     proto['signature'].copy(),
                    'weight':        proto['weight_profile'].copy(),
                    'effectiveness': proto['effectiveness'],
                    'support':       1
                }
                archetype_library = add_archetype(archetype_library, new_archetype,
                                                  A_max=10)

    return archetype_library


def compute_weight_stability(weight_profile):
    # In the minimal setup, weight stability is approximated by
    # the inverse of the weight vector's normalized entropy.
    # A highly concentrated weight vector is stable (low entropy).
    p = weight_profile / weight_profile.sum()
    H = -np.sum(p * np.log(p + 1e-8))
    H_max = np.log(len(p))
    return 1.0 - H / H_max    # 1 = fully concentrated, 0 = uniform
```

`A_max = 10` (upper bound on archetype library size; 3× the expected zone count,
leaving room for sub-zone archetypes without forcing over-compression).

### 6.2 Effectiveness Normalization Across Runs

After the sleep phase, normalize `eff_norm` across all protocols in the buffer
for logging purposes:

```python
eff_values = [p['effectiveness'] for p in valid]
eff_max = max(eff_values) if eff_values else 1.0
for p in valid:
    p['eff_norm'] = p['effectiveness'] / (eff_max + 1e-8)
```

This normalized value is what is compared in the archetype revision decision
when multi-run statistics are available (later phases).

---

## 7 S_observer: Data Collection and ε-Sweep

### 7.1 Data Collection

After training, collect behavioral data from the **trained, frozen policy**
(no further training):

- N_episodes = 100 evaluation episodes
- For each episode, record: `(step_t, grid_position, zone_membership, action_taken)`
- Segment into zone windows: consecutive steps within a single zone type
- Exclude transition steps: the 2 steps before and after each zone-boundary crossing
- Minimum window size: 20 steps (discard shorter windows)

```python
def compute_action_dist(window_actions, n_actions=4):
    counts = np.zeros(n_actions)
    for a in window_actions:
        counts[a] += 1
    return counts / counts.sum()
```

### 7.2 ε-Sweep Input

The ε-sweep operates on the set of `action_dist` vectors from all valid
zone windows. Each window is treated as a data point; the sweep clusters
these data points at each ε value.

Format for the pipeline adapter:

```python
# One row per zone window
records = [
    {
        'window_id': i,
        'zone_type': zone,           # 'R', 'C', or 'F'
        'action_dist': dist_vector,  # numpy array, shape (4,)
        'episode_id': ep,
        'step_start': t0,
        'step_end':   t1
    }
    for i, (zone, dist_vector, ep, t0, t1) in enumerate(windows)
]
```

Distance metric: L1 (sum of absolute differences over action probabilities).

### 7.3 Clustering and Plateau Detection

Apply the existing ε-sweep pipeline (`pipeline/epsilon_sweep.py`) with the
behavioral adapter. For each ε value in the sweep range [0.01, 1.0] (50
log-spaced points):

1. Compute pairwise L1 distances between all `action_dist` vectors
2. Apply threshold clustering: two windows are in the same cluster if
   L1 distance ≤ ε
3. Record N(ε) = number of clusters

**go/no-go criterion for H1:**
- Stable plateau at N = 3 (matching zone count)
- Plateau width w ≥ 0.5 (log-scale)
- Reproducible in the single-seed minimal run (multi-seed test deferred)

### 7.4 Minimal Logging

For each evaluation episode and each zone window, log:

| Field | Description |
|-------|-------------|
| `zone_type` | R, C, or F |
| `action_dist` | action distribution vector |
| `progress_efficiency_obs` | `Δd_exit / window_length` (external proxy for eff_norm) |
| `saliency_events` | count of saliency events in window |
| `w_at_window_start` | weight vector at start of window (logged for correspondence analysis) |

`w_at_window_start` is the only internal-state quantity logged by S_observer.
It is logged for post-hoc correspondence analysis (Section 8), not as input
to the ε-sweep.

---

## 8 Correspondence Analysis (Post-Partition)

After the ε-sweep produces a partition, run the following minimal correspondence
checks:

### 8.1 Zone-Regime Alignment

For each identified regime cluster, compute:

```
alignment_score = max_{z ∈ {R,C,F}} P(zone_type = z | regime = R_i)
```

If the partition aligns with zone structure, each regime cluster should be
dominated by one zone type (alignment_score > 0.8 for all clusters).

### 8.2 Effectiveness Correspondence

Compare `progress_efficiency_obs` across regime clusters:

```
eff_per_regime = {R_i: mean(progress_efficiency_obs for windows in R_i)}
```

If regime clusters correspond to zone types and zone types differ in efficiency,
`eff_per_regime` should differ across clusters. This is the minimal test of H2.

### 8.3 Weight-Behavior Correspondence

Using the logged `w_at_window_start` values, check whether weight profiles
cluster by zone type:

```
weight_variance_within_zone  = mean(var(w_i | zone_type = z)) for z in {R,C,F}
weight_variance_between_zones = var(mean(w_i | zone_type = z)) for z in {R,C,F}
```

If archetype-guided weight updates produce zone-specific weight profiles,
`weight_variance_between_zones > weight_variance_within_zone`.

This is the minimal external test of whether S_sleep is producing
zone-differentiated archetypes (Q-OB-04).

---

## 9 Hyperparameter Summary

All hyperparameters in one place for reproducibility:

| Parameter | Value | Scope | Source |
|-----------|-------|-------|--------|
| Grid size | 9×9 | Environment | §2.1 |
| Zone layout | 3 columns per zone | Environment | §2.1 |
| T_max | 200 steps | Environment | §2.1 |
| Exit reward | +10 | Environment | §2.1 |
| Movement cost Zone R | 0.5 | Environment | §2.1 |
| Movement cost Zone C | 0.1 | Environment | §2.1 |
| Movement cost Zone F | 0.3 | Environment | §2.1 |
| Visibility radius r | 3 | S_online | §4 |
| p_progress window k | 5 steps | S_online | §4 |
| ε_stab | 0.01 | S_online | §4 |
| theta_resource | 0.25 | S_online | §5.2 |
| theta_progress | 0.1 | S_online | §5.2 |
| delta_max | 0.05 | S_online | §5.3 |
| theta_match | 0.3 | S_online / S_sleep | §5.3 |
| max_protocols | 50 | S_online | §5.4 |
| alpha (EMA rate) | 0.3 | S_sleep | §6.1 |
| theta_improve | 0.05 | S_sleep | §6.1 |
| theta_promote | 0.4 | S_sleep | §6.1 |
| theta_stability | 0.5 | S_sleep | §6.1 |
| min_protocols | 5 | S_sleep | §6.1 |
| A_max | 10 | S_sleep | §6.1 |
| PPO training steps | 500,000 | Training | §3.2 |
| gamma | 0.99 | Training | §3.2 |
| entropy coefficient | 0.01 | Training | §3.2 |
| learning rate | 3e-4 | Training | §3.2 |
| N_eval_episodes | 100 | S_observer | §7.1 |
| Transition exclusion | 2 steps | S_observer | §7.1 |
| Min window size | 20 steps | S_observer | §7.1 |
| ε-sweep range | [0.01, 1.0], 50 pts | S_observer | §7.2 |

---

## 10 Execution Checklist

```
Phase 0 — Implementation
[ ] 9×9 labyrinth environment with three zones implemented and unit-tested
[ ] Observable vector o(t) computation verified (all 7 observables, correct ranges)
[ ] Saliency detection function verified on synthetic trajectories
[ ] Weight update function verified (sum-to-1 constraint maintained)
[ ] Encounter protocol buffer implemented (max_protocols eviction)
[ ] Sleep phase revision loop implemented and unit-tested
[ ] PPO training loop integrated with S_online weight updates
[ ] Behavioral data collection and zone-window segmentation verified
[ ] ε-sweep pipeline adapter implemented and tested on synthetic action_dist data

Phase 1 — Single-Seed Run
[ ] Agent trains for 500,000 steps
[ ] Training reward curve plotted (verify convergence)
[ ] Archetype library logged at end of training (how many archetypes? what signatures?)
[ ] 100 evaluation episodes collected
[ ] Zone-window segmentation: min window size satisfied in most episodes
[ ] action_dist computed for all valid windows
[ ] ε-sweep executed on action_dist data
[ ] N(ε) plot reviewed for plateau structure
[ ] go/no-go verdict for H1 recorded

Phase 2 — Correspondence Analysis (if H1 go)
[ ] Zone-regime alignment score computed
[ ] Effectiveness correspondence computed (eff_per_regime)
[ ] Weight-behavior correspondence computed (within vs. between zone weight variance)
[ ] Results recorded in FailureAudit and CaseRecord for CASE-20260330-0012
```

---

## 11 What This Setup Does Not Test (Deferred)

| Deferred item | Reason | Next phase |
|--------------|--------|-----------|
| Multi-seed reproducibility (δ_ob1) | Single seed sufficient for minimal H1 test | Phase 2 |
| Cross-labyrinth transfer (δ_ob2, H3) | Requires second labyrinth instance | Phase 3 |
| Consolidation ablation (H4) | Requires baseline without sleep phase | Phase 2 |
| Layer-2 observer observables | Require partition result as prerequisite | Post-Phase 1 |
| Archetype library ablation | Requires run without S_sleep | Phase 2 |
| BC-class correspondence (H2 full) | Requires multi-zone signature analysis | Post-Phase 1 |

The minimal setup is designed so that **Phase 1 failure is informative**:
if no plateau emerges, the failure mode (F1, F1_BC, F3) points directly
to which component to investigate next (observable insufficiency, agent
undifferentiation, or partition instability).
