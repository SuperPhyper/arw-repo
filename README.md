# ARW / ART Framework  
*A structural framework for analyzing regime partitions under boundary conditions*

Author: Rico Felder

---

# Regime Scope Analysis

Methods for analyzing how **regime structures transform when the scope of a model changes**.

Modern science and engineering increasingly rely on models to understand complex systems — from climate and infrastructure to financial markets and artificial intelligence. Yet we still lack systematic tools to analyze how the structural patterns revealed by these models depend on the way systems are described.

This repository develops a framework for studying how **regime structures, regime boundaries, and regime transitions change when modeling scopes change**.

The project builds a methodological toolkit for comparing regime structures across different descriptions of the same system.

---

# Core Idea

Complex systems rarely exhibit a single behavior. Instead, they operate in **regimes** — relatively stable patterns of behavior separated by transitions.

However, the regimes observed in a system depend strongly on the **scope of the model**, including:

- chosen observables  
- included couplings  
- boundary conditions  
- resolution of description  

Different scopes can therefore produce different regime structures.

This repository explores methods for analyzing these transformations.

---

# Research Questions

This project investigates several key questions:

- Do **classes of boundary conditions** generate characteristic regime structures?
- How do **regime boundaries shift** when the scope of a model changes?
- When do regime structures remain **stable across modeling levels**?
- When do regime descriptions become **distorted under scope reduction**?
- Can these transformations be measured using **structural distortion metrics**?

---

# Methodological Approach

The project studies regime transformations using multiple complementary systems:

### Mechanical Systems
Controlled dynamical systems such as:

- coupled oscillators
- multi-link pendulum systems

These provide well-understood regime structures for calibration.

### Agent Systems
Minimal agent-based models exhibiting regimes such as:

- consensus
- polarization
- fragmentation

These systems are compared to aggregated mean-field descriptions.

### Cross-Scope Comparison

The framework analyzes how regime structures transform across modeling scopes using tools such as:

- regime partition extraction
- regime graph construction
- regime boundary detection
- structural distortion metrics

---

# Conceptual Framework

The framework focuses on the relationship between:

model scope
->
admissible observables
->
regime partitions
->
regime stability regions
->
regime transition structure

The central object of study is the **transformation of regime structures under scope change**.

---

# Why This Matters

Many failures in complex systems arise not because models are wrong, but because **structural regimes shift when modeling assumptions change**.

Examples include:

- infrastructure instability
- financial regime shifts
- unexpected AI behavior
- engineering systems with hidden couplings

Understanding how regime structures depend on modeling scope could provide new diagnostic tools for complex systems research.

---

# Repository Structure

The repository is organized as a combination of:

- research code
- conceptual documentation
- glossary for ARW / ART concepts
- experimental simulations

See the repository structure below for details.

---

# Status

This repository is an active research workspace.  
Concepts, experiments, and documentation will evolve over time.

---

# License

MIT License
