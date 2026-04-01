---
status: experiment-proposal
layer: experiments/
depends_on:
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/agent_sleep_scope.md
  - docs/context_navigation/arw_observer_scope.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - cases/CASE-20260330-0012/ScopeSpec.yaml
---

# Minimal Experiment Setup — Three-Scope Architecture
## Emergent Modes Experiment: S_online / S_sleep / S_observer

This document defines the **minimal runnable configuration** of the Emergent
Modes Experiment under the three-scope architecture. Its purpose is to produce
the first empirical data with the fewest moving parts sufficient to test H1:

> Does a stable behavioral regime partition emerge — detectable by S_observer —
> from an agent operating under the three-scope architecture, without prescribed modes?

Everything not strictly necessary for H1 is deferred.

For theoretical grounding see `context_navigation_emergent_modes_experiment.md`
and the three scope documents listed above.

---

## 1 What "Minimal" Means

**Minimal means:**
- Simplest environment that produces structurally distinct encounter contexts
- Smallest possible agent network
- Only the three saliency triggers specified in `agent_online_scope.md` §3.1
- Single contingency variable (`r_resource`)
- Sleep revision without EMA, support counts, or promotion thresholds
- One training seed; reproducibility testing deferred
- Zone structure as scaffold only — not the object of the first claim

**Deferred:**
- Multi-seed reproducibility (δ_ob1) — Phase 2
- Cross-labyrinth transfer (δ_ob2, H3) — Phase 3
- Consolidation ablation (H4) — Phase 2
- Layer-2 observer observables — post H1 confirmation
- Archetype library capacity management — Phase 2
- `contact_onset` saliency trigger — Phase 2

---

## 2 Environment

### 2.1 Grid

A 9×9 discrete grid with three zone types:

```
columns 0–2: Zone R (Restriction)   — high movement cost, tight action constraints
columns 3–5: Zone C (Coupling)      — low cost, visible coupling targets
columns 6–8: Zone F (Forcing)       — medium cost, directional reward field
```

Zone boundaries are at column transitions (2→3 and 5→6). Crossing a boundary
is instantaneous — zone membership changes at the first step in the new column.

Exit: fixed at a cell in the rightmost column of Zone F.
Primary task: reach the exit.

**Design note:** Zone structure is scaffold, not the object of study. The
zones create structurally different encounter contexts (different cost profiles,
different saliency trigger distributions) without prescribing what the agent
should do. If subscopes emerge, they may or may not align with zones — both
outcomes are informative.

### 2.2 Zone Parameters

| Zone | Movement cost c | Visibility radius r | Notes |
|------|----------------|---------------------|-------|
| R | 0.5 | 3 | High cost makes progress drop salient |
| C | 0.1 | 5 | Low cost; coupling targets visible at r=5 |
| F | 0.3 | 3 | Directional reward bonus on one action per cell |

### 2.3 Episode Parameters

- Grid size: 9×9
- Action space: A = {up, down, left, right}, |A| = 4
- Per-step reward: −c(zone)
- Exit reward: +10
- Episode termination: exit reached OR T_max = 200 steps
- Starting position: random cell in Zone R (left third), randomized per episode

---

## 3 Agent Architecture

### 3.1 Policy Network

A two-layer feedforward network:

```
Input:  o_weighted(t) = w(t) ⊙ o(t)     [7-dimensional]
Hidden: Linear(7 → 32) → ReLU
Output: Linear(32 → 4) → Softmax        [action probabilities]
```

The input is the **weighted perception vector** from S_online. The PPO
optimizer sees only `w(t) ⊙ o(t)` — it does not receive `w(t)` or `o(t)`
separately. This means:

- The optimizer learns a policy conditioned on whatever weighted input it receives
- Weight changes (from S_online) appear to the optimizer as input distribution shifts
- The optimizer does not know that weights are non-stationary

This implicit conditioning is a deliberate design choice: if the policy learns
to exploit weight profiles without being told they exist, that is a stronger
emergence result than explicit conditioning.

### 3.2 Training

- Algorithm: PPO (standard implementation, e.g. Stable-Baselines3)
- Training steps: 500,000
- γ = 0.99, entropy coefficient = 0.01, learning rate = 3 × 10⁻⁴
- No curriculum; all zones present from the first episode
- No mode-specific reward shaping

**Integration point:** At each step during training, S_online computes
`o_weighted(t) = w(t) ⊙ o(t)` before passing input to the policy network.
At each saliency event, S_online updates w(t) before the next step.
At run end (episode termination or T_max), S_sleep runs on the accumulated
protocol buffer and updates the archetype library before the next run begins.

---

## 4 Observable Vector — Π_perception

Computed at each step from environment state:

| Key | Computation | Range |
|-----|------------|-------|
| `d_exit` | `manhattan_dist(x_t, x_exit) / D_max`, D_max = 16 | [0, 1] |
| `v_sight` | `free_cells_in_radius(r) / V_max`, V_max = zone-dependent | [0, 1] |
| `e_edge` | `1 if wall within r=1 else 0` | {0, 1} |
| `c_contact` | `1 if last action produced no movement else 0` | {0, 1} |
| `m_cost` | `c(zone) / 0.5` (normalized by max cost) | [0, 1] |
| `r_resource` | `steps_remaining / T_max` | [0, 1] — monotone decreasing |
| `p_progress` | `clip((d_exit(t−k) − d_exit(t)) / (k + ε_stab), 0, 1)`, k=5, ε_stab=0.01 | [0, 1] |

---

## 5 S_online Implementation

### 5.1 Initialization

```python
w = np.ones(7) / 7          # uniform initial weights
archetype_library = {
    'structure_loss': [],
    'resource_threshold': [],
    'progress_drop': []
}
protocol_buffer = []
encounter_start = {
    't': 0,
    'w_in': w.copy(),
    'C_in': 1.0,
    'd_exit_start': initial_d_exit
}
```

### 5.2 Saliency Detection (each step)

```python
def detect_saliency(o_prev, o_curr, r_resource_curr, k_window, obs_history):
    # Binary trigger: structure loss
    if o_prev['e_edge'] == 1 and o_curr['e_edge'] == 0:
        return {'type': 'structure_loss', 'strength': None}

    # Scalar trigger: resource threshold
    if o_prev['r_resource'] >= THETA_RESOURCE > o_curr['r_resource']:
        grad_pct = compute_gradient_pct('r_resource', obs_history, k_window)
        return {'type': 'resource_threshold', 'strength': classify_strength(grad_pct)}

    # Scalar trigger: progress drop
    if o_curr['p_progress'] < THETA_PROGRESS:
        grad_pct = compute_gradient_pct('p_progress', obs_history, k_window)
        return {'type': 'progress_drop', 'strength': classify_strength(grad_pct)}

    return None   # no saliency event

def classify_strength(grad_pct):
    if grad_pct <= 15: return 'weak'
    if grad_pct <= 45: return 'medium'
    return 'strong'

def compute_gradient_pct(key, obs_history, k):
    # gradient of observable w.r.t. r_resource over last k steps
    delta_obs      = abs(obs_history[-1][key] - obs_history[-k][key])
    delta_resource = abs(obs_history[-1]['r_resource'] - obs_history[-k]['r_resource'])
    if delta_resource < 1e-6:
        return 0.0
    return (delta_obs / delta_resource) * 100
```

Parameters: `THETA_RESOURCE = 0.25`, `THETA_PROGRESS = 0.1`, gradient window `k = 5`.

### 5.3 Encounter Close and Weight Update

```python
def close_encounter_and_update(saliency, encounter_start, o_curr, w_curr,
                                archetype_library, protocol_buffer, step):
    # 1. Record completed encounter protocol
    progress_rate = clip(
        (encounter_start['d_exit_start'] - o_curr['d_exit']) /
        (step - encounter_start['t'] + EPS_STAB), 0, 1
    )
    protocol = {
        'saliency_type':     saliency['type'],
        'saliency_strength': saliency['strength'],
        'C_in':              encounter_start['C_in'],
        'C_out':             o_curr['r_resource'],
        'w_in':              encounter_start['w_in'].copy(),
        'w_out':             w_curr.copy(),
        'progress_rate':     progress_rate
    }
    if len(protocol_buffer) >= MAX_PROTOCOLS:
        protocol_buffer.pop(0)   # FIFO eviction
    protocol_buffer.append(protocol)

    # 2. Find archetype match for new encounter
    partition = archetype_library[saliency['type']]
    match = find_match(saliency['strength'], w_curr, partition, THETA_TOLERANCE)

    # 3. Compute new weight vector
    if match is not None:
        w_target = match['w_out'].copy()
    else:
        w_target = w_curr.copy()

    delta = np.random.uniform(-DELTA_MAX, DELTA_MAX, size=7)
    w_target = np.clip(w_target + delta, 0.01, None)
    w_target /= w_target.sum()

    return w_target, protocol

def find_match(strength, w_in, partition, tolerance):
    candidates = [
        a for a in partition
        if a['saliency_strength'] == strength
        and np.max(np.abs(w_in - a['w_in'])) <= tolerance
    ]
    if not candidates:
        return None
    # Recency tie-break: most recently updated archetype
    return max(candidates, key=lambda a: a['last_updated'])
```

Parameters: `THETA_TOLERANCE = 0.05`, `DELTA_MAX = 0.05`, `MAX_PROTOCOLS = 50`.

---

## 6 S_sleep Implementation

Runs once per run (after episode termination), before the next run begins.

```python
def sleep_phase(protocol_buffer, archetype_library, run_id,
                min_duration=5, min_protocols=5):

    valid = [p for p in protocol_buffer
             if p['C_in'] > EPS_STAB
             and (p['C_in'] - p['C_out']) * T_MAX > min_duration]

    if len(valid) < min_protocols:
        return archetype_library   # null revision — insufficient data

    for proto in valid:
        partition = archetype_library[proto['saliency_type']]
        match = find_match(proto['saliency_strength'], proto['w_in'],
                           partition, THETA_TOLERANCE)

        if match is not None:
            # Single comparison — winner takes place, no averaging
            if proto['progress_rate'] > match['effectiveness']:
                match['w_out']         = proto['w_out'].copy()
                match['effectiveness'] = proto['progress_rate']
                match['last_updated']  = run_id
            elif proto['progress_rate'] == match['effectiveness']:
                match['w_out']        = proto['w_out'].copy()   # recency tie-break
                match['last_updated'] = run_id
            # else: discard — existing archetype was more effective, no change

        else:
            # No match → unconditional promotion, no threshold
            new_arch = {
                'saliency_type':     proto['saliency_type'],
                'saliency_strength': proto['saliency_strength'],
                'w_in':              proto['w_in'].copy(),
                'w_out':             proto['w_out'].copy(),
                'effectiveness':     proto['progress_rate'],
                'last_updated':      run_id
            }
            partition.append(new_arch)

    return archetype_library
```

---

## 7 S_observer: Data Collection and ε-Sweep

### 7.1 Data Collection

After training, evaluate the frozen policy for N_episodes = 100 episodes.
For each step, record:

```python
record = {
    'episode_id':     ep,
    'step_t':         t,
    'grid_position':  x_t,
    'zone_type':      zone_membership(x_t),
    'action_taken':   a_t,
    'saliency_event': saliency or None,   # logged for segmentation
    'w_at_step':      w_t                 # debug/correspondence only — not primary evidence
}
```

**`w_at_step`** is marked debug/correspondence-only. It is not used in the
ε-sweep or regime detection. It is available for post-hoc correspondence
analysis (Section 7.3) but does not constitute external observation of
behavioral output.

### 7.2 Segmentation and ε-Sweep

Segment trajectories into encounter windows using logged saliency event
timestamps. Exclude the saliency event timestep from both adjacent windows.
Discard windows shorter than 10 steps.

For each valid window, compute:

```python
action_dist = np.bincount(actions_in_window, minlength=4) / len(actions_in_window)
```

Run `pipeline/epsilon_sweep.py` on the set of `action_dist` vectors.
Distance metric: L1. Sweep range: [0.01, 1.0], 50 log-spaced points.

**go/no-go criterion for H1:**
Stable ε-plateau at N ≥ 2, reproducible in the single-seed run.
N is a finding — not a target.

### 7.3 Correspondence Analysis (post-partition)

If H1 is confirmed, run the following analyses in order:

**1. Saliency type distribution per cluster:**
```python
for regime_cluster in partition:
    windows = [w for w in all_windows if w.cluster == regime_cluster]
    sal_dist = Counter(w.saliency_type for w in windows)
```

**2. Effectiveness per cluster:**
```python
    eff_mean = mean(w.progress_rate_obs for w in windows)
```

**3. Subscope reconstruction from archetype library (separate — does not require partition):**
```python
THETA_W = 0.15
for archetype in all_archetypes():
    subscope = [i for i, w_i in enumerate(archetype['w_in']) if w_i > THETA_W]
    archetype['subscope'] = subscope
```

Compare subscopes across archetypes: archetypes sharing the same dominant
observable subset are candidates for the same latent subscope. Then cross-reference
against the ε-sweep partition to see whether archetypes with identical subscopes
also fall in the same regime cluster. This cross-reference is the empirical
content of H2 — it is not presupposed.

**4. Zone correspondence (labeled secondary):**
```python
    zone_dist = Counter(w.zone_type for w in windows)
```
Zone alignment is one possible explanation for the observed regime structure.
It is not the primary success criterion.

**5. Weight profile correspondence (debug — uses internal state log):**
```python
    w_mean = np.mean([w.w_at_step for w in windows], axis=0)
```
`w_at_step` is debug/correspondence-only. It is not behavioral output.

---

## 8 Hyperparameter Summary

| Parameter | Value | Scope |
|-----------|-------|-------|
| Grid size | 9×9 | Environment |
| T_max | 200 | Environment |
| Exit reward | +10 | Environment |
| c(Zone R/C/F) | 0.5 / 0.1 / 0.3 | Environment |
| r (visibility) | 3 / 5 / 3 | Environment |
| k (gradient window) | 5 steps | S_online |
| ε_stab | 0.01 | S_online |
| THETA_RESOURCE | 0.25 | S_online |
| THETA_PROGRESS | 0.10 | S_online |
| THETA_TOLERANCE | 0.05 | S_online / S_sleep |
| DELTA_MAX | 0.05 | S_online |
| MAX_PROTOCOLS | 50 | S_online |
| min_duration | 5 steps | S_sleep |
| min_protocols | 5 | S_sleep |
| PPO steps | 500,000 | Training |
| γ | 0.99 | Training |
| entropy coeff | 0.01 | Training |
| learning rate | 3×10⁻⁴ | Training |
| N_eval_episodes | 100 | S_observer |
| min window size | 10 steps | S_observer |
| ε-sweep range | [0.01, 1.0], 50 pts | S_observer |

---

## 9 Execution Checklist

```
Phase 0 — Implementation
[ ] 9×9 labyrinth environment implemented and unit-tested
[ ] All 7 observables computed correctly (check normalization)
[ ] Saliency detection verified on synthetic trajectories
    [ ] Binary trigger fires correctly on e_edge transition
    [ ] Scalar triggers compute gradient correctly
    [ ] Strength classification produces expected classes
[ ] Weight update verified: sum-to-1 maintained, no zero weights
[ ] Encounter protocol buffer: FIFO eviction working
[ ] S_sleep: null revision fires when buffer < min_protocols
[ ] S_sleep: recency tie-break correctly resolves equal effectiveness
[ ] S_sleep: new archetypes promoted unconditionally on no-match
[ ] PPO training integrated with S_online weight updates
[ ] Behavioral data collection: saliency timestamps logged correctly
[ ] Encounter window segmentation: saliency timesteps excluded
[ ] action_dist computed and verified (sums to 1, windows ≥ 10 steps)
[ ] ε-sweep pipeline adapter: encounter windows as input

Phase 1 — Single-Seed Run
[ ] Agent trains for 500,000 steps
[ ] Training reward curve plotted — verify convergence
[ ] Archetype library logged at run end (size per partition? saliency type distribution?)
[ ] 100 evaluation episodes collected
[ ] N(ε) plot reviewed for plateau structure
[ ] go/no-go verdict for H1 recorded in CaseRecord for CASE-20260330-0012

Phase 2 — Correspondence Analysis (if H1 go)
[ ] Saliency type distribution per regime cluster computed
[ ] Effectiveness correspondence computed
[ ] Zone correspondence computed (secondary)
[ ] Weight-profile correspondence computed (debug — uses w_at_step log)
[ ] Results recorded in FailureAudit_Emergent.md
```
