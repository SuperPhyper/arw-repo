---
status: proposal
layer: experiments/
title: "Patch: Operator–Modulator Weight Split for S_online"
parent: labyrinth_three_scope_minimal_setup.md
inspiration: kht_architecture_layer4.md (§3, Design Constraints C1–C2)
created: 2026-05-14
scope: S_online internals only — no changes to Policy Network, S_sleep, or S_observer
---

# Patch: Operator–Modulator Weight Split for S_online

## Motivation

KHT Layer 4 distinguishes two structurally different kinds of cognitive parameters:

- **Operators**: determine *what* is processed — the content of attention
- **Modulators**: determine *how* it is evaluated — the processing context

In the current setup, all 7 observables are weighted by a single vector `w` and
treated as structurally equivalent. This conflates two functionally distinct
roles: some observables describe the *content* of the agent's situation
(what is out there), others describe the *processing context* (how constrained
is the agent right now).

Separating these roles in S_online gives the archetype library a cleaner
structure: archetypes encode *content attention profiles* (`w_op`) rather than
a mixture of content and context. The context observables (`w_mod`) are handled
by a separate, simpler update mechanism driven directly by the saliency trigger type.

**Scope of this patch:** S_online internals only. The Policy Network receives
the same 7-dimensional `o_weighted(t)` as before. S_sleep, S_observer, and
the ε-sweep are unchanged.

---

## 1 Observable Classification

The 7 observables are split into two groups by structural role:

### Operator observables — `w_op` (5-dimensional)
Content of the situation; what the agent is attending to:

| Index | Key | Role |
|-------|-----|------|
| 0 | `d_exit` | Distance to goal — primary navigation content |
| 1 | `v_sight` | Spatial openness — structural content of current position |
| 2 | `e_edge` | Wall proximity — discontinuity / constraint content |
| 3 | `c_contact` | Movement blocked — action-outcome content |
| 4 | `p_progress` | Recent progress rate — trajectory content |

### Modulator observables — `w_mod` (2-dimensional)
Processing context; how constrained / costly is the current situation:

| Index | Key | Role |
|-------|-----|------|
| 0 | `r_resource` | Time remaining — resource/urgency context |
| 1 | `m_cost` | Movement cost — effort context |

**Rationale for this split:**
`r_resource` and `m_cost` do not describe what the agent sees — they describe
the conditions under which it operates. They are the closest labyrinth-analogs
to KHT's modulator axes (τ ≈ `r_resource`; zone-cost ≈ `m_cost`). Critically,
the saliency triggers are already defined over these two observables
(`resource_threshold` fires on `r_resource`; zone transitions drive `m_cost`
changes). This makes them natural modulators: they *trigger* context-mode
changes rather than being objects of attention themselves.

---

## 2 Modified Initialization

Replace the single `w` vector with two sub-vectors. The combined weighted
observation is reconstructed for the Policy Network at each step.

```python
# Operator weights (over content observables)
w_op  = np.ones(5) / 5          # uniform initial weights, sum to 1

# Modulator weights (over context observables)
w_mod = np.ones(2) / 2          # uniform initial weights, sum to 1

# Index maps (consistent with Π_perception ordering)
IDX_OP  = [0, 1, 2, 3, 6]      # d_exit, v_sight, e_edge, c_contact, p_progress
IDX_MOD = [4, 5]                # m_cost, r_resource

def build_o_weighted(o, w_op, w_mod):
    """Reconstruct the 7-dim weighted observation for the Policy Network."""
    w_full = np.empty(7)
    w_full[IDX_OP]  = w_op
    w_full[IDX_MOD] = w_mod
    # Renormalize so full vector sums to 1 (preserves existing policy input scale)
    w_full /= w_full.sum()
    return w_full * o   # element-wise, same as before

# Archetype library — unchanged structure, but w_in / w_out now refer to w_op only
archetype_library = {
    'structure_loss':      [],
    'resource_threshold':  [],
    'progress_drop':       []
}

protocol_buffer = []

encounter_start = {
    't':            0,
    'w_op_in':      w_op.copy(),   # was: 'w_in'
    'C_in':         1.0,
    'd_exit_start': initial_d_exit
}
```

**Note:** `w_mod` is not stored in `encounter_start` or the archetype library.
It is updated by a separate mechanism (§4) and is not the object of consolidation.

---

## 3 Modified Weight Update Logic

### 3.1 w_op update (content attention — via archetype library)

`w_op` is updated exactly as `w` was in the original design, but operates
only over the 5 operator observables. The archetype library stores and
retrieves `w_op` profiles (not the full 7-dim vector).

```python
def close_encounter_and_update(saliency, encounter_start, o_curr,
                                w_op_curr, w_mod_curr,
                                archetype_library, protocol_buffer, step):
    # 1. Record protocol — w_op only
    progress_rate = clip(
        (encounter_start['d_exit_start'] - o_curr['d_exit']) /
        (step - encounter_start['t'] + EPS_STAB), 0, 1
    )
    protocol = {
        'saliency_type':     saliency['type'],
        'saliency_strength': saliency['strength'],
        'C_in':              encounter_start['C_in'],
        'C_out':             o_curr['r_resource'],
        'w_op_in':           encounter_start['w_op_in'].copy(),  # 5-dim
        'w_op_out':          w_op_curr.copy(),                   # 5-dim
        'progress_rate':     progress_rate
    }
    if len(protocol_buffer) >= MAX_PROTOCOLS:
        protocol_buffer.pop(0)
    protocol_buffer.append(protocol)

    # 2. Find archetype match on w_op
    partition = archetype_library[saliency['type']]
    match = find_match(saliency['strength'], w_op_curr, partition, THETA_TOLERANCE)

    # 3. Compute new w_op
    if match is not None:
        w_op_target = match['w_op_out'].copy()
    else:
        w_op_target = w_op_curr.copy()

    delta = np.random.uniform(-DELTA_MAX, DELTA_MAX, size=5)   # 5-dim now
    w_op_target = np.clip(w_op_target + delta, 0.01, None)
    w_op_target /= w_op_target.sum()

    return w_op_target, protocol


def find_match(strength, w_op_in, partition, tolerance):
    """Unchanged logic — operates on 5-dim w_op instead of 7-dim w."""
    candidates = [
        a for a in partition
        if a['saliency_strength'] == strength
        and np.max(np.abs(w_op_in - a['w_op_in'])) <= tolerance
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda a: a['last_updated'])
```

### 3.2 w_mod update (context — direct saliency mapping)

`w_mod` is not routed through the archetype library. It is updated directly
based on saliency trigger type, reflecting the KHT insight that modulator
state is driven by context conditions, not by learned content profiles.

```python
# w_mod index: 0 = m_cost weight, 1 = r_resource weight
W_MOD_PROFILES = {
    'resource_threshold': np.array([0.2, 0.8]),  # urgency context: emphasize r_resource
    'progress_drop':      np.array([0.5, 0.5]),  # mixed context: balanced
    'structure_loss':     np.array([0.7, 0.3]),  # cost context: emphasize m_cost
}

def update_w_mod(saliency_type, w_mod_curr, alpha=0.3):
    """
    Soft update toward the context profile for the triggered saliency type.
    alpha controls update speed — lower = more inertia (hysteresis-like).
    """
    target = W_MOD_PROFILES[saliency_type]
    w_mod_new = (1 - alpha) * w_mod_curr + alpha * target
    w_mod_new /= w_mod_new.sum()
    return w_mod_new
```

**Design notes:**
- `W_MOD_PROFILES` are fixed priors, not learned. This is intentional: the
  modulator update encodes a structural assumption (resource_threshold → urgency
  context) rather than an empirical finding. It can be ablated in Phase 2
  by replacing with uniform targets.
- `alpha = 0.3` provides moderate inertia. The agent does not snap
  immediately to the new context profile — it drifts toward it. This is
  the hysteresis analog from Layer 4 §3.3.
- `w_mod` is updated at every saliency event, including `structure_loss`
  (which has `strength: None`). For `structure_loss`, strength-based
  matching is not used for `w_op` either — this is unchanged.

---

## 4 Modified Per-Step Integration

```python
# At each step t:

# 1. Compute observables
o_curr = compute_observables(env_state, obs_history)

# 2. Build weighted input for Policy Network
o_weighted = build_o_weighted(o_curr, w_op, w_mod)

# 3. Policy Network step (unchanged)
action = policy.predict(o_weighted)
obs_history.append(o_curr)

# 4. Detect saliency
saliency = detect_saliency(o_prev, o_curr, o_curr['r_resource'],
                           k_window, obs_history)

# 5. If saliency event: update both sub-vectors
if saliency is not None:
    # 5a. Update w_mod (direct, fast)
    w_mod = update_w_mod(saliency['type'], w_mod, alpha=0.3)

    # 5b. Close encounter, update w_op (via archetype library)
    w_op, protocol = close_encounter_and_update(
        saliency, encounter_start, o_curr,
        w_op, w_mod,
        archetype_library, protocol_buffer, t
    )

    # 5c. Open new encounter
    encounter_start = {
        't':            t,
        'w_op_in':      w_op.copy(),
        'C_in':         o_curr['r_resource'],
        'd_exit_start': o_curr['d_exit']
    }

o_prev = o_curr
```

---

## 5 Modified S_sleep

S_sleep operates on `w_op_in` / `w_op_out` (5-dim) instead of `w_in` / `w_out`
(7-dim). Logic is otherwise unchanged.

```python
def sleep_phase(protocol_buffer, archetype_library, run_id,
                min_duration=5, min_protocols=5):

    valid = [p for p in protocol_buffer
             if p['C_in'] > EPS_STAB
             and (p['C_in'] - p['C_out']) * T_MAX > min_duration]

    if len(valid) < min_protocols:
        return archetype_library

    for proto in valid:
        partition = archetype_library[proto['saliency_type']]
        match = find_match(proto['saliency_strength'], proto['w_op_in'],  # 5-dim
                           partition, THETA_TOLERANCE)

        if match is not None:
            if proto['progress_rate'] > match['effectiveness']:
                match['w_op_out']      = proto['w_op_out'].copy()  # 5-dim
                match['effectiveness'] = proto['progress_rate']
                match['last_updated']  = run_id
            elif proto['progress_rate'] == match['effectiveness']:
                match['w_op_out']    = proto['w_op_out'].copy()
                match['last_updated'] = run_id
        else:
            new_arch = {
                'saliency_type':     proto['saliency_type'],
                'saliency_strength': proto['saliency_strength'],
                'w_op_in':           proto['w_op_in'].copy(),   # 5-dim
                'w_op_out':          proto['w_op_out'].copy(),  # 5-dim
                'effectiveness':     proto['progress_rate'],
                'last_updated':      run_id
            }
            partition.append(new_arch)

    return archetype_library
```

---

## 6 Modified S_observer Data Collection

Add `w_op_at_step` and `w_mod_at_step` as separate debug fields.
The primary observable for S_observer (action distributions, ε-sweep) is unchanged.

```python
record = {
    'episode_id':      ep,
    'step_t':          t,
    'grid_position':   x_t,
    'zone_type':       zone_membership(x_t),
    'action_taken':    a_t,
    'saliency_event':  saliency or None,
    'w_op_at_step':    w_op.copy(),   # debug — replaces w_at_step
    'w_mod_at_step':   w_mod.copy(),  # debug — new
}
```

**Correspondence analysis addition (§7.3 of parent doc):**
In the subscope reconstruction step, use `w_op_at_step` instead of `w_at_step`:

```python
THETA_W = 0.15
for archetype in all_archetypes():
    subscope = [IDX_OP[i] for i, v in enumerate(archetype['w_op_in'])
                if v > THETA_W]
    archetype['subscope'] = subscope
```

Subscopes are now defined over the 5 operator observables only, which is
the correct structural claim: a subscope is a content attention profile,
not a combined content+context profile.

---

## 7 Summary of Changes

| Component | Change | Unchanged |
|---|---|---|
| `w` initialization | Split into `w_op` (5-dim) + `w_mod` (2-dim) | Sum-to-1 normalization |
| `o_weighted` construction | `build_o_weighted()` reconstructs 7-dim from sub-vectors | Policy Network input shape (7-dim) |
| Saliency detection | Unchanged | — |
| `close_encounter_and_update` | Operates on `w_op` (5-dim); `w_mod` not passed to archetype | Protocol buffer structure |
| `find_match` | Operates on `w_op_in` (5-dim) | Matching logic, THETA_TOLERANCE |
| `update_w_mod` | New function; direct saliency-type mapping with inertia α | — |
| Per-step integration | `w_mod` updated first; then `w_op` via encounter close | Encounter open/close timing |
| `encounter_start` | Stores `w_op_in` instead of `w_in` | `C_in`, `d_exit_start`, `t` |
| Protocol buffer | Stores `w_op_in`, `w_op_out` (5-dim) instead of `w_in`, `w_out` | All other fields |
| S_sleep | Operates on `w_op_*` fields (5-dim) | All logic unchanged |
| S_observer data | `w_op_at_step` + `w_mod_at_step` replace `w_at_step` | ε-sweep, action_dist, all primary observables |
| Archetype structure | `w_op_in`, `w_op_out` (5-dim) | `saliency_type`, `saliency_strength`, `effectiveness`, `last_updated` |

---

## 8 Hyperparameter Additions

| Parameter | Value | Scope | Note |
|---|---|---|---|
| `alpha` (w_mod inertia) | 0.3 | S_online | Soft-update speed for context weights |
| `W_MOD_PROFILES` | see §3.2 | S_online | Fixed context priors per saliency type; ablatable |
| `IDX_OP` | [0,1,2,3,6] | S_online | Observable indices for w_op |
| `IDX_MOD` | [4,5] | S_online | Observable indices for w_mod |

`DELTA_MAX` and `THETA_TOLERANCE` apply to `w_op` (5-dim) unchanged in
absolute terms. Because the vector is now 5-dim instead of 7-dim, the
relative perturbation per dimension is slightly larger — consider reducing
`DELTA_MAX` to `0.04` if early runs show excessive w_op volatility.

---

## 9 What This Patch Does Not Change

- **H1 and the go/no-go criterion**: the ε-sweep runs on action distributions,
  which are downstream of `o_weighted`. The structural split of `w` does not
  alter the action distribution directly — it only changes which weight profiles
  the agent develops. H1 is still testable with identical S_observer logic.

- **The falsification structure**: if H1 fails with this patch, the interpretation
  is the same as without it: no stable behavioral regime partition emerged.
  The patch does not make H1 easier to confirm — it changes *what* the
  emergent regimes encode if they do emerge (content profiles rather than
  mixed content+context profiles).

- **Phase 2 deferral list**: multi-seed reproducibility, cross-labyrinth transfer,
  and consolidation ablation remain deferred. This patch adds one new
  Phase 2 ablation candidate: fix `W_MOD_PROFILES` to uniform (α = 0 effectively)
  and test whether the regime partition still emerges without context-weight
  differentiation.
