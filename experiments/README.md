---
status: note
layer: experiments/
---

# Experiments

Concrete ART instantiations and experimental designs.

Each document in this folder follows the ART scope template:
it defines S = (B, Π, Δ, ε) explicitly, derives the expected regime partition,
and specifies falsification conditions.

---

## Research Logic

The experiments are organized in three phases:

**Phase 1 — Calibration**
Systems with analytically known regime structure.
Purpose: validate the ARW partition extraction pipeline before applying it
to systems where ground truth is unknown.

**Phase 2 — Core Investigation**
Systems where regime structure must be empirically extracted.
Purpose: test BC taxonomy hypotheses and cross-scope admissibility.

**Phase 3 — Transfer**
Cross-maze and cross-scope transfer in the context-navigation agent.
Purpose: test whether regime partitions are portable across structurally
similar environments.

---

## Calibration Systems

| Document | System | ARW role |
|---|---|---|
| [kuramoto_oscillators.md](kuramoto_oscillators.md) | Coupled oscillators | Validate pipeline against known K_c; calibrate distortion metrics |
| [multi_link_pendulum.md](multi_link_pendulum.md) | Two/three-link pendulum | Test admissible reduction under tunable coupling κ |

---

## Core Investigation

| Document | System | ARW role |
|---|---|---|
| [agent_consensus_models.md](agent_consensus_models.md) | Opinion dynamics (N agents) | BC-induced regime generation; network topology variation |
| [aggregation_meanfield.md](aggregation_meanfield.md) | Agent ↔ mean-field comparison | Develop and validate cross-scope distortion metrics (TBS, RCD, PCI, SDI) |

---

## Context Navigation Agent

| Document | Content |
|---|---|
| [labyrinth_experiment_agenda.md](labyrinth_experiment_agenda.md) | Full ART scope, regime partition, hypotheses in ARW terms, distortion metrics |
| [labyrinth_experiment_extended_design.md](labyrinth_experiment_extended_design.md) | Zone scopes as explicit BC classes, intra-episode scope transitions, experimental phases |

---

## Cross-Experiment Dependencies

The experiments are designed to build on each other:

```
Kuramoto + Pendulum
  → validate partition extraction pipeline
  → calibrate distortion metrics (TBS, PCI)

Consensus models + Mean-field
  → develop cross-scope comparison methodology
  → first social-domain BC taxonomy test

Context-navigation agent
  → applies all of the above to emergent regime structure
  → tests transfer admissibility across maze instances
```

The distortion metrics developed in the mean-field experiment
are reused in the labyrinth transfer phases.
The admissibility criterion validated in the pendulum
is applied to zone-scope transitions in the labyrinth.
