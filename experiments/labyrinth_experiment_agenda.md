
# Labyrinth Experiment Agenda
## Demonstration Scenario for Context-Navigation and Mode Ecology

This experiment is designed to test whether an agent architecture based on
context representation, mode selection, anchor memory, and periodic
consolidation ("sleep") can produce emergent behavioral regimes and
context-driven mode switching.

The goal is not merely improved task performance, but the observation of
structured mode ecology and transfer across structurally similar tasks.

---

# Core Hypotheses

## H1 — Resource Constraints Select Behavioral Modes

Different environmental constraints (planning budget, memory, visibility, etc.)
will favor different strategies.

Prediction:
Under stable constraints, the agent will converge to distinct behavioral
regimes (modes) rather than a single smooth policy.

---

## H2 — Sleep Consolidation Stabilizes Context–Mode Anchors

Periodic offline consolidation phases will transform episodic experience into
stable context–mode anchor associations.

Prediction:
After sleep cycles, the mapping

context → mode

becomes more stable and faster to activate.

---

## H3 — Salience Enables Rapid Mode Switching

Salience is modeled as competition or uncertainty between candidate modes.

Prediction:
At structural decision points in the environment, salience spikes precede
mode transitions.

---

# Environment

The environment consists of a grid-based labyrinth.

Properties:

- Discrete grid world
- Multiple maze instances
- Structural similarities across mazes
- Controlled resource constraints

Example grid sizes:

- 10 × 10 (initial)
- 15 × 15 (later experiments)

---

# Manipulated Resource Constraints

Each experiment condition modifies the available cognitive resources:

- Planning budget (lookahead depth)
- Working memory capacity
- Visibility radius
- Action cost
- Error tolerance

These constraints are intended to induce different dominant strategies.

---

# Agent Architecture (Minimal Prototype)

Components:

- Shared perception model
- 3–5 learnable modes (gated policies)
- Context representation layer
- Anchor memory for context–mode associations
- Salience estimator
- Periodic consolidation phase ("sleep")

---

# Sleep / Consolidation Phase

Occurs every N episodes (e.g., 5).

During sleep:

- Experiences are replayed
- Stable context clusters are identified
- Anchor associations are updated
- Mode boundaries become clearer

Goal:

Strengthen stable regime structure rather than simply improve policy weights.

---

# Observables and Metrics

## Performance Metrics

- Solution time per episode
- Total steps to goal
- Convergence speed after constraint changes

---

## Structural Metrics

- Number of emergent modes
- Stability of mode clusters
- Policy embedding clustering
- Mode-switch frequency

---

## Memory Metrics

- Anchor reuse rate across new mazes
- Anchor formation speed
- Context classification stability

---

## Salience Metrics

- Salience spikes near decision points
- Correlation between salience and mode switching
- Salience decay after successful regime selection

---

# Transfer Tests

After training on several mazes, introduce structurally similar but unseen
labyrinths.

Prediction:

The agent should rapidly activate previously consolidated regimes instead of
learning from scratch.

Expected pattern:

context similarity → anchor retrieval → mode activation

---

# Baseline Comparisons

To validate the mechanism, compare against agents without:

- sleep / consolidation
- anchor memory
- explicit mode selection

Baselines include:

1. Standard RL policy
2. Mixture-of-experts without salience
3. Single-policy agent

---

# Falsification Criteria

The model would be weakened if:

- only a single smooth policy emerges
- sleep improves performance but does not stabilize mode structure
- salience does not correlate with mode switching
- new mazes require full relearning instead of regime reuse

---

# Expected Outcome

If the architecture functions as hypothesized, the system should develop a
mode ecology consisting of a small set of stable behavioral regimes.

These regimes should:

- dominate under specific resource constraints
- become anchored through consolidation
- transfer across structurally similar environments

This would demonstrate context-driven regime selection rather than
pure policy interpolation.
