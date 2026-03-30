---
status: experiment-proposal
layer: experiments/
depends_on:
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/context_navigation_scope_spec_emergent.md
  - experiments/labyrinth_experiment_agenda.md
  - cases/CASE-20260330-0012/ScopeSpec.yaml
---

# ART Instantiation: Labyrinth Agent — Emergent Modes Experiment

This document is the **execution-oriented experiment record** for the Emergent Modes
Experiment. It describes what to build, how to run it, and what to measure.

For the full theoretical treatment and formal scope specification, see:
- [context_navigation_emergent_modes_experiment.md](../docs/context_navigation/context_navigation_emergent_modes_experiment.md)
- [context_navigation_scope_spec_emergent.md](../docs/context_navigation/context_navigation_scope_spec_emergent.md)

For the Designed Modes Experiment (agent with prescribed mode library), see:
- [labyrinth_experiment_agenda.md](labyrinth_experiment_agenda.md)

The pipeline artifacts for this experiment are in:
- [cases/CASE-20260330-0012/](../cases/CASE-20260330-0012/)

---

## 1 Scientific Question

> Can behavioral regime structure — interpretable as distinct cognitive modes —
> emerge from training in a structured environment, **without being architecturally
> prescribed**?

This is an ARW **observation experiment**, not an architecture design exercise.
The agent has no mode library, no explicit switching mechanism, no mode-labeled
training signal. ARW is applied as a post-hoc measurement instrument.

This experiment is the empirical complement to the Designed Modes Experiment:
- **Designed Modes** (CASE-20260329-0011): architecture prescribes modes; experiment
  tests navigation between them.
- **Emergent Modes** (CASE-20260330-0012): no prescribed modes; experiment tests
  whether regime structure arises from training alone.

---

## 2 System Setup

### 2.1 Environment

The multi-zone labyrinth from [labyrinth_experiment_agenda.md](labyrinth_experiment_agenda.md)
and [labyrinth_experiment_extended_design.md](labyrinth_experiment_extended_design.md).
**No change to the environment.** Its zone structure is the BC ground truth.

Zone types:
| Zone | BC Class | Active constraint |
|------|----------|------------------|
| R (Restriction) | Restriction | Tight resource/action constraints |
| C (Coupling) | Coupling | Coordination with local environmental features |
| F (Forcing) | Forcing | Directional reward signal |

Zone boundaries are discontinuous. Crossing one changes the active constraint set.

### 2.2 Agent

A **single unstructured policy** — feedforward or recurrent neural network trained
by standard RL (PPO or A2C).

**Must NOT have:**
- A mode library M
- An explicit mode selector
- Mode-labeled reward component
- Modular subnetwork architecture (no separate per-zone networks)

**Receives the same perceptual input as the Designed Modes agent:**
local zone features within visibility radius r = 5 (wall layout, zone-type
indicators, resource state). Produces discrete actions.

### 2.3 Training

Standard RL training on the full multi-zone labyrinth. No curriculum that
explicitly separates zone types. No mode-specific reward shaping.

Training procedure is an experimental degree of freedom — what matters is
that no mode structure is injected. Record: optimizer, learning rate,
discount factor, entropy coefficient, number of steps.

---

## 3 ARW Observation Protocol

After training, do not modify the agent. Collect behavioral data and apply
the ARW partition extraction pipeline.

### 3.1 Data Collection

Collect N_episodes (≥ 100) episodes from the trained agent across the
full labyrinth. For each step t, record:

```
(episode_id, step_t, grid_position, zone_membership, action_taken)
```

Segment each episode into **zone windows**: consecutive steps within a single
zone type. Exclude transition steps (zone boundary crossings) from all
downstream analysis — these fall in Z(action_dist) and violate the A4
stationarity assumption.

Minimum window size: 20 steps (required for reliable action_dist estimation).

### 3.2 Compute action_dist

For each zone window W:

```
action_dist(W) = empirical distribution of actions in W
action_dist_i  = count(a = i in W) / |W|
```

This is the primary observable for the ε-sweep. Observable key: `action_dist`.
Distance metric: L1 (sum of absolute differences over action probabilities).

### 3.3 ε-Sweep

Run `pipeline/epsilon_sweep.py` on the action_dist data.

**Note:** The pipeline currently operates on numerical time-series from physical
simulations. A **behavioral adapter** is required to convert zone-window
action_dist vectors into the pipeline's expected input format. See Section 5.

ε-sweep range: log-spaced over [0.01, 1.0] (50 points, adjustable).
Output: N(ε) — number of distinguishable behavioral regime clusters as a function of ε.

### 3.4 Plateau Analysis

From the ε-sweep output, identify:

1. **Plateau(s)**: intervals of ε over which N is stable (≥ 3 consecutive values).
2. **Primary plateau N**: the N value at the most robust plateau.
3. **Transition boundaries θ\***: ε values at which N changes.

**go/no-go criterion:**
A stable plateau with N ≥ 2, reproducible in ≥ 80% of independent training
runs (different seeds), constitutes a `go` verdict for H1.

Primary prediction: N = 3 (one cluster per zone type R, C, F).

### 3.5 Regime Characterization

For each identified regime cluster, compute:
- Mean action_dist (the cluster centroid)
- Dominant actions within each cluster
- Spatial distribution: which grid positions / zone types are overrepresented?
- Correspondence with zone types (H2 test)

---

## 4 Hypotheses and Falsification

| Hypothesis | Prediction | Falsification condition |
|-----------|-----------|------------------------|
| H1 — Regime Emergence | Stable ε-plateau at N = zone count | No plateau (F3) or plateau not reproducible (F2) |
| H2 — BC-Class Correspondence | Each regime cluster corresponds to the BC class of its dominant zone type | Regime signatures do not match predicted BC classes |
| H3 — Transfer Generalization | Partition generalizes to unseen labyrinth (same topology, different geometry); Φ ≥ 0.75 | Φ < 0.5 (environment-specific partition) |
| H4 — Consolidation Ablation | Adding consolidation sharpens regime partition (higher SDI, narrower transition windows) | No measurable change in partition quality with consolidation |

Full failure mode table: see
[cases/CASE-20260330-0012/ScopeSpec.yaml](../cases/CASE-20260330-0012/ScopeSpec.yaml)
(falsification block, F0–F4).

---

## 5 Prerequisites for Execution

The case artifacts (ScopeSpec.yaml, BCManifest.yaml, CaseRecord.yaml) are complete.
The following implementation work is still required before the experiment can be run:

### 5.1 Labyrinth Environment

The multi-zone labyrinth environment must be implemented. It is already designed
(see [labyrinth_experiment_extended_design.md](labyrinth_experiment_extended_design.md)).
Required: a runnable Python environment with configurable zone types (R, C, F),
zone boundaries, and reward structure. The same environment is used for both
the Designed Modes and Emergent Modes experiments.

### 5.2 Unstructured RL Agent

A minimal feedforward or recurrent neural network trained by PPO or A2C on the
labyrinth. Standard implementation (e.g., Stable-Baselines3). No mode library.

### 5.3 Behavioral Pipeline Adapter

The existing ARW pipeline (`epsilon_sweep.py`, `extract_partition.py`,
`invariants.py`) operates on numerical time-series from ODE/stochastic system
simulations. A behavioral adapter is needed that:

1. Takes recorded trajectory data `(episode_id, step_t, zone_membership, action_taken)`
2. Segments into zone windows (excluding transition steps)
3. Computes `action_dist` per window
4. Outputs the data in the format expected by `epsilon_sweep.py`
5. Writes `Invariants.json` with `sweep_range: [epsilon_min, epsilon_max]`

This adapter is the primary implementation bottleneck for running both the
Designed Modes and Emergent Modes experiments.

---

## 6 Execution Checklist

```
[ ] Labyrinth environment implemented and unit-tested
[ ] Unstructured RL agent trains successfully on single-zone environment (CASE-0011 Phase 1 check)
[ ] Agent trains successfully on multi-zone labyrinth
[ ] Behavioral data collection: N_episodes >= 100, zone window segmentation correct
[ ] action_dist computed and verified (distributions sum to 1, windows >= 20 steps)
[ ] Behavioral adapter producing epsilon_sweep-compatible input
[ ] epsilon_sweep runs on action_dist data
[ ] N(epsilon) plot reviewed for plateau structure
[ ] Plateau reproducibility checked across >= 5 training seeds
[ ] go_nogo verdict written to CaseRecord.yaml
[ ] FailureAudit_Emergent.md completed
[ ] Invariants.json written (with sweep_range: [epsilon_min, epsilon_max])
```

---

## 7 Cross-Experiment Dependencies

```
CASE-20260329-0011 (Designed Modes, Phase 1)
  → same environment, same labyrinth
  → behavioral adapter is shared
  → go verdict from CASE-0011 is prerequisite for interpreting CASE-0012 results
    (if designed modes produce N=k regimes, emergent modes should too — or explain why not)

Physical calibration cases (CASE-0001, 0002, 0003)
  → ε-sweep procedure is identical; pipeline reused
  → TBS_norm comparison with physical cases is NOT defined
    (sweep parameter is ε, not a BC parameter; see research_journal.md 2026-03-30)

CASE-20260318-0004 (Stuart-Landau emergence)
  → first empirical ARW emergence case; this experiment is its cognitive analog
  → emergence window analysis may be relevant if H1 confirms a sharp partition boundary
```
