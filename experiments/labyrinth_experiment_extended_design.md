
# Labyrinth Experiment – Extended Design
## Regime‑Forcing Environment for Mode Ecology and Context Navigation

This document extends the basic labyrinth experiment to **force the emergence
of multiple behavioral regimes (modes)** within the same environment. The goal
is to make **mode switching observable and measurable**, rather than allowing
a single smooth policy to dominate.

The design introduces **local constraint zones**, **dynamic resource shifts**,
and **structural transfer tests** to provoke regime competition.

---

# Core Principle

The environment is structured so that **different regions reward different
strategies**. This prevents the agent from solving the entire task with a
single policy.

Instead, optimal behavior requires:

context → mode selection → policy execution

---

# Environment Structure

The base environment remains a **grid‑based labyrinth**, but it now contains
multiple **constraint zones** that impose different resource conditions.

Example base sizes:

- 10×10 grid (initial experiments)
- 15×15 grid (expanded tests)

Zones are distributed across the maze so that the agent must traverse
multiple constraint regimes within a single episode.

---

# Constraint Zones

## Zone A — Exploration Zone

Properties:

- low action cost
- large visibility radius
- minimal penalty for errors

Optimal behavior:

exploration / mapping mode

Purpose:

Encourages building internal structure representations.

---

## Zone B — High‑Cost Zone

Properties:

- high penalty for wrong turns
- narrow corridors
- possible traps

Optimal behavior:

deliberative / cautious mode

Purpose:

Tests careful planning strategies.

---

## Zone C — Landmark Zone

Properties:

- repeated structural motifs
- identifiable landmarks
- recurring substructures

Optimal behavior:

anchor retrieval / heuristic navigation

Purpose:

Tests whether anchor memory enables reuse of structural knowledge.

---

## Zone D — Low‑Visibility Zone

Properties:

- restricted observation radius
- partial observability
- ambiguous intersections

Optimal behavior:

reactive / local sensing mode

Purpose:

Forces the agent to rely on local information rather than planning.

---

# Dynamic Constraint Shifts

To further provoke regime transitions, certain constraints may change
*during the episode*.

Examples:

- visibility radius suddenly decreases
- action cost increases
- memory capacity temporarily reduced
- time pressure activated

Expected pattern:

constraint shift → salience spike → mode switch

---

# Ambiguous Decision Nodes

Certain junctions are deliberately designed to produce **strategy conflict**.

Examples:

- short risky path vs long safe path
- path requiring planning vs path requiring exploration

Prediction:

Salience peaks at these nodes due to competing mode activation.

---

# Agent Architecture (Recap)

Minimal prototype components:

- shared perception network
- 3–5 learnable modes
- gating mechanism
- context representation layer
- anchor memory
- salience estimator
- periodic sleep / consolidation phase

---

# Observables

## Mode–Zone Alignment

Test whether specific modes dominate in appropriate zones.

zone type ↔ mode identity

Strong alignment suggests successful regime selection.

---

## Salience Dynamics

Measure:

- salience spikes at decision nodes
- correlation between salience and mode switches
- salience reduction after correct regime activation

---

## Policy Regime Clustering

Embed policy behavior across episodes and perform clustering.

Expected result:

policy space → discrete clusters

These clusters correspond to emergent modes.

---

# Transfer Experiments

After training on several mazes, introduce **structurally similar but visually
different labyrinths**.

Prediction:

The agent retrieves anchors and activates corresponding modes quickly.

Expected sequence:

context similarity → anchor retrieval → mode activation

---

# Experimental Phases

## Phase 1 – Mode Emergence

Single constraint regime.

Goal:

Verify whether multiple behavioral modes emerge.

---

## Phase 2 – Local Regime Switching

Single maze containing multiple constraint zones.

Goal:

Observe intra‑episode mode switching.

---

## Phase 3 – Structural Transfer

Introduce new but structurally similar mazes.

Goal:

Measure anchor‑based transfer and regime reuse.

---

# Success Criteria

The architecture succeeds if the agent develops a **mode ecology**
with the following properties:

- small number of stable modes
- reliable switching triggered by salience
- clear zone‑mode alignment
- anchor reuse across new environments

---

# Conceptual Summary

maze
↓
local constraint zones
↓
mode competition
↓
salience‑triggered switching
↓
sleep consolidation
↓
anchor‑based transfer

This design transforms the labyrinth task from a simple navigation
problem into a **regime‑selection problem**, directly testing the
context‑navigation hypothesis.
