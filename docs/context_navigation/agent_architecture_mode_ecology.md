
# Agent Architecture – Mode Ecology and Context Navigation

## Overview

This document describes a conceptual agent architecture designed to support
**context-driven mode selection**, **anchor-based memory**, and **periodic
consolidation ("sleep")**.

The goal of the architecture is not only task performance, but the emergence of
a **mode ecology**: a small set of stable behavioral regimes that can be
activated depending on context.

The architecture is inspired by ideas from:

- dynamical systems (regimes / attractors)
- reinforcement learning (policy learning)
- cognitive science (task sets and strategy switching)
- ARW-style scope selection (context → regime partition)

---

# High-Level Structure

The agent consists of six interacting subsystems:

1. Perception Layer
2. Context Representation
3. Mode Library
4. Mode Gating / Selection
5. Anchor Memory
6. Sleep / Consolidation

Flow:

perception → context representation → mode selection → policy execution

---

# 1. Perception Layer

The perception layer processes the raw observations of the environment.

Possible implementations:

- convolutional network
- transformer encoder
- simple feature extractor for grid worlds

Output:

state embedding

This embedding feeds into the **context representation system**.

---

# 2. Context Representation

The context representation transforms raw perception into a representation that
captures the **structural properties of the current situation**.

Examples of context features:

- local maze topology
- resource constraints
- uncertainty level
- visibility radius
- proximity to decision nodes

The context vector serves as the **input for mode selection**.

---

# 3. Mode Library

The agent maintains a set of possible behavioral regimes (modes).

Example size:

3–5 modes in early experiments.

Each mode corresponds to a **policy specialization**, such as:

- exploration
- cautious planning
- heuristic navigation
- reactive movement

Modes share perception but have different policy heads.

---

# 4. Mode Gating / Selection

The gating mechanism determines which mode is active at a given moment.

Input:

context representation.

Output:

mode probability distribution.

Possible implementations:

- softmax gating
- winner-take-all gating
- mixture-of-experts controller

Mode switching may occur when:

- salience spikes
- context similarity changes
- constraints shift.

---

# 5. Anchor Memory

Anchor memory stores associations between **context classes and modes**.

Conceptually:

context cluster → preferred mode

Anchors are created when a particular mode repeatedly succeeds in a
recognizable context.

Functions:

- fast mode retrieval
- transfer to structurally similar problems
- stabilization of regime structure

---

# 6. Salience Estimator

Salience measures the **uncertainty or competition between candidate modes**.

High salience occurs when:

- multiple modes appear plausible
- the environment changes unexpectedly
- decision points are encountered

Role:

salience spike → trigger potential mode switch.

---

# 7. Sleep / Consolidation

Every N episodes the agent enters an offline consolidation phase.

During this phase:

- experiences are replayed
- context clusters are identified
- anchor associations are updated
- mode boundaries become clearer

This process strengthens stable regime structure.

---

# 8. Mode Ecology

Over time the system should develop a **mode ecology**:

a small number of stable behavioral regimes that dominate under specific
context conditions.

Expected characteristics:

- clear regime clusters in policy space
- reliable switching between regimes
- reuse of modes in new environments
- reduced exploration after consolidation

---

# Conceptual Summary

perception
↓
context representation
↓
mode competition
↓
salience detection
↓
mode activation
↓
policy execution
↓
experience storage
↓
sleep consolidation
↓
anchor stabilization
