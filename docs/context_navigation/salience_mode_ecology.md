---
status: hypothesis
layer: docs/context_navigation/
---


# Salience as an Emergent Property of Mode Ecology

## Overview

This document summarizes the conceptual development of **salience** within a context‑adaptive cognitive architecture.

Instead of defining salience purely as a property of sensory stimuli, this framework treats salience as an **emergent property of the performance landscape of processing modes across contexts**.

The idea arises from combining:

- context navigation
- mode‑based cognition
- anchor/prototype memory
- offline consolidation
- ecological competition between modes

---

# 1 Classical Interpretation of Salience

In many cognitive and AI models, salience is treated as a direct function of the input stimulus.

Examples:

- visual contrast
- novelty
- attention weights
- feature activation

Formally:

S(c)

where **S** is a salience function applied to the current context **c**.

In these models:

stimulus → salience → attention → processing

---

# 2 Limitations of Stimulus-Based Salience

Stimulus-based salience assumes that important features exist independently of the cognitive strategy applied to interpret them.

However, in adaptive cognition:

- different strategies focus on different features
- what matters depends on the interpretive regime
- relevance emerges from learned performance

Thus salience should not depend only on the stimulus, but also on the **available processing modes and their historical success**.

---

# 3 Modes and Context Space

Let

c ∈ C

represent a context within a context space **C**.

Let

M = {m₁, m₂, ..., m_k}

represent the set of processing modes.

Each mode has a contextual performance function:

Fₘ(c)

which measures how effective mode **m** is in context **c**.

This value can be estimated using stored anchor prototypes.

---

# 4 Mode Ecology

Processing modes form an ecological structure over context space.

Each mode has a **niche** defined by contexts where it performs well:

Nₘ = { c ∈ C | Fₘ(c) high }

Learning reshapes these niches over time through experience and consolidation.

---

# 5 Emergent Salience

In this framework, salience emerges from **competition between modes**.

A context becomes salient when:

- multiple modes have comparable fitness
- or when the system approaches a boundary between niches.

One simple definition:

S(c) = Varₘ(Fₘ(c))

Where salience corresponds to the variance of mode fitness values across the set of modes.

Interpretation:

- low variance → one mode clearly dominates → low salience
- high variance → competition between modes → high salience

---

# 6 Interpretation

Salience therefore indicates:

"How important it is to resolve which processing mode should be active."

Salience is highest when the system must decide between competing interpretations of the situation.

---

# 7 Relationship to Mode Selection

Mode selection follows:

m* = argmaxₘ Fₘ(c)

Salience does not determine the selected mode directly.

Instead it indicates:

- whether a mode transition is likely
- how sensitive the system should be to contextual cues.

---

# 8 Role of Anchors

Anchor prototypes store historically successful context–mode configurations.

Anchors allow the system to estimate Fₘ(c) by comparing the current context to past experiences.

Anchors therefore indirectly shape the salience landscape.

---

# 9 Offline Consolidation

During sleep or consolidation phases the system:

- reorganizes anchors
- updates performance estimates
- reshapes mode niches

This process continuously refines the ecological structure of modes in context space.

---

# 10 Conceptual Summary

In this framework:

Salience is not a direct property of stimuli.

Instead, salience emerges from the **learned performance landscape of processing modes across context space**.

Key principles:

- contexts form a landscape
- modes form ecological niches
- anchors store prototypes of stable niches
- salience appears at niche boundaries
- cognition navigates this landscape by activating the mode with maximal contextual fitness

---

# Core Principle

Salience emerges from the competition and learned performance of processing modes across contexts, indicating where the system must resolve which interpretive regime is most admissible.
