---
status: working-definition
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/glossary/scope.md
---

# Agent Sleep Scope — Archetype Revision and Effectiveness Evaluation

## Purpose

This document defines the **sleep scope** of the context navigation agent —
the offline evaluation and consolidation phase that runs between active
labyrinth runs. It is the second of three scope-level documents in the
multi-scope architecture of the Emergent Modes Experiment.

| Document | Scope | Operates |
|----------|-------|----------|
| `agent_online_scope.md` | S_online | At each timestep during a run |
| `agent_sleep_scope.md` (this document) | S_sleep | Between runs |
| `arw_observer_scope.md` | S_observer | Across runs (external ARW measurement) |

S_sleep is agent-internal. Its output is an updated archetype library A',
which feeds back into S_online on the next run. S_observer does not have
access to A or to the protocol buffer — it observes only behavioral output.

---

## 1 Scope Definition

```
S_sleep = (B_sleep, Π_evaluation, Δ_archetype, ε_eff)
```

### B_sleep — Boundary Constraints

| ID | Constraint | BC Class |
|----|-----------|----------|
| B_sl1 | S_sleep operates on the encounter protocol buffer from the preceding run. Buffer is read-only during sleep. | Restriction |
| B_sl2 | S_sleep has read and write access to the archetype library A. A is frozen during S_online. | Coupling |
| B_sl3 | The archetype library is partitioned by saliency type. Revision operates within each partition independently. | Restriction |
| B_sl4 | No new perceptual input is received during sleep. | Restriction |
| B_sl5 | Output of S_sleep is a revised library A'. S_online reads A' on the next run. | Coupling |

---

## 2 Evaluation Observable — Π_evaluation

The single primary evaluation observable in the minimal sleep scope is:

**`progress_rate`** — as recorded in the encounter protocol
(see `agent_online_scope.md` §5.1):

```
progress_rate(e) = clip((d_exit(t_start) - d_exit(t_end)) / (steps + ε_stab), 0, 1)
```

This is the sole effectiveness criterion for archetype revision in the
minimal experiment. It is directly task-relevant, requires no external
labels, and is computable entirely from within Π_perception.

No secondary evaluation observables (weight stability, support counts,
promotion thresholds) are used in the minimal version. These are deferred
to later phases.

### Observable Range R(progress_rate)

Valid when:
- `steps > 0` (non-trivial encounter)
- `r_resource > ε_stab` at encounter onset (not resource-depleted at entry)
- encounter duration ≥ `min_duration` (sufficient length for meaningful estimation)

Encounters violating these conditions are excluded from revision.

---

## 3 Archetype Library

### 3.1 Structure

The archetype library is partitioned by saliency type:

```
A = {
    'structure_loss':      [ A_0, A_1, ... ],
    'resource_threshold':  [ A_0, A_1, ... ],
    'progress_drop':       [ A_0, A_1, ... ]
}
```

Each archetype record:

```
archetype = {
    saliency_type:     'structure_loss' | 'resource_threshold' | 'progress_drop'
    saliency_strength: 'weak' | 'medium' | 'strong' | None
    w_in:              weight vector at encounter onset (matching key)
    w_out:             weight vector at encounter close (recommended exit weight)
    effectiveness:     progress_rate estimate for this archetype
    last_updated:      run index of last revision
}
```

### 3.2 Initialization

The archetype library is initialized empty: `A = {}` (all partitions empty).
The first run produces encounter protocols that seed the library at the
end of the first sleep phase. During the first run, all weight updates
are exploratory (no match possible).

---

## 4 Revision Protocol

The revision protocol runs once per sleep phase. It processes the encounter
protocol buffer partition by partition.

### 4.1 Protocol Filtering

Before revision, exclude protocols where:
- `steps < min_duration` (too short)
- `C_in < ε_stab` (resource-depleted at encounter entry)

Remaining protocols form the **evaluation set** E.

If `|E| < min_protocols`, apply **null revision**: archetype library unchanged.
This prevents spurious updates from underpopulated runs.

### 4.2 Matching Within Partition

For each protocol `p` in E:

```
partition = A[p.saliency_type]

find A_match in partition where:
  A_match.saliency_strength == p.saliency_strength
  AND |p.w_in - A_match.w_in|_inf <= θ_tolerance
```

Same matching rule as in S_online (Section 4.1 of `agent_online_scope.md`).

### 4.3 Revision Decision

The revision rule is a **single comparison with winner-takes-place**. No
averaging, no merging, no smoothing. One encounter, one decision:

**Case 1 — Match found:**

```
if proto.progress_rate > A_match.effectiveness:
    replace A_match entirely with proto's w_out and progress_rate
    update A_match.last_updated = current_run

elif proto.progress_rate == A_match.effectiveness:
    replace A_match.w_out with proto.w_out          ← recency tie-break
    update A_match.last_updated = current_run

else:  # proto.progress_rate < A_match.effectiveness
    discard proto — no change to archetype
```

**Why winner-takes-place, not averaging:** The archetype stores a specific
weight profile that produced a specific effectiveness. Averaging two profiles
would produce a profile that was never actually tested. The goal is to retain
the best-performing observed configuration, not to estimate a mean behavior.

**Case 2 — No match:**

Promote unconditionally to a new archetype. No threshold, no stability check:

```
new_archetype = {
    saliency_type:     proto.saliency_type,
    saliency_strength: proto.saliency_strength,
    w_in:              proto.w_in,
    w_out:             proto.w_out,
    effectiveness:     proto.progress_rate,
    last_updated:      current_run
}
A[proto.saliency_type].append(new_archetype)
```

Every unmatched valid encounter with a distinct weight profile becomes its
own archetype. Whether two archetypes represent the same latent subscope is
not decided here — that is S_observer's analysis after experiment end.

### 4.4 Library Size

No hard capacity limit in the minimal version. The library grows as new
encounter patterns are observed. Library size is logged as an observable
for S_observer. Capacity management (eviction) is deferred to later phases.

---

## 5 Connection to ARW Framework

S_sleep implements a **discrete selection event** between runs: only
encounter patterns with higher effectiveness than the stored archetype
replace it; equal patterns trigger recency-based replacement; weaker
patterns are silently discarded. This selective retention is the mechanism
by which stable behavioral patterns persist across runs.

From the ARW perspective, the archetype library is the agent's internal
compressed representation of experienced encounter contexts. Whether the
archetypes cluster by zone BC class — and whether that clustering corresponds
to the regime partition detected by S_observer — is an empirical question,
not a design guarantee. This correspondence is the content of H2 in
`context_navigation_emergent_modes_experiment.md`.

---

## 6 Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q-SL-01 | Should progress_rate be supplemented by a cross-run consistency term in later phases? A weight profile that is effective but unstable across runs should eventually be penalized. | open |
| Q-SL-02 | At what library size does S_observer begin to see meaningful clustering? Is there a minimum archetype count required for regime detection? | open |
| Q-SL-03 | Should capacity management (eviction) be based on effectiveness, recency, or both? | open |
| Q-SL-04 | Can the archetype library serve as indirect access to the agent's internal regime partition for S_observer correspondence analysis? | open |
