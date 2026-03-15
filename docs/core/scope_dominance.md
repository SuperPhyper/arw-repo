---
status: working-definition
layer: docs/core/
---


# Scope Dominance

## Overview

This document formalizes the concept of **scope dominance** as introduced in the ARW
framework and translates it into the cognitive architecture used in this repository.

Scope dominance describes the condition under which a descriptive regime (scope)
successfully orders the behavior of a system.

Loss of scope dominance manifests as instability, unpredictability, or chaotic behavior.
In the cognitive architecture, scope dominance corresponds to the **active processing mode**
that currently organizes the agent's interpretation of context.

---

# 1 ARW Definition

In ARW, a **scope** is a stabilized descriptive regime that selects variables, relations,
and invariants sufficient to describe a system under given conditions.

A scope remains **dominant** when it successfully orders the behavior of the system's
relevant degrees of freedom.

Loss of scope dominance occurs when degrees of freedom that were assumed to be stabilized
or negligible become dynamically relevant and begin influencing system evolution.

Typical signals of dominance loss include:

- sensitivity to initial conditions
- unstable trajectories
- unpredictable behavior
- apparent chaos

Chaos can therefore be interpreted as a structural signal that the chosen scope is no longer
able to maintain ordering authority over the system.

---

# 2 Translation to Cognitive Architecture

In the context-navigation architecture:

Global scope:
the full observable state space of the agent.

Processing modes:
reduced scopes that prioritize and suppress subsets of observables.

Each processing mode attempts to provide a stable description of the current context.

A mode is **dominant** when it successfully organizes the interpretation of the agent's
environment and produces stable predictions or actions.

---

# 3 Mode Dominance

Mode dominance can be expressed as:

m* = argmax_m A(m|c)

Where:

m = processing mode  
c = context  
A(m|c) = admissibility of mode m in context c  

The dominant mode is the mode whose reduced scope remains most compatible with the
currently active degrees of freedom.

---

# 4 Loss of Dominance

Dominance degrades when suppressed observables begin to influence outcomes.

This can occur when:

- environmental conditions change
- previously irrelevant variables become relevant
- new interactions activate latent degrees of freedom

In such situations, the current mode may lose its stabilizing capacity.

---

# 5 Structural Interpretation

From the ARW perspective:

Dominance loss does not imply randomness or failure of determinism.

Instead, it indicates that:

- the current scope is no longer adequate
- additional degrees of freedom must be considered
- a new scope (or processing mode) must take over.

Thus instability becomes a **diagnostic signal** for required scope transition.

---

# 6 Relationship to Other Concepts

Scope dominance interacts with several other concepts in the architecture:

Admissibility
→ measures compatibility between scope assumptions and active degrees of freedom

Salience
→ increases when multiple scopes compete for dominance

Scope Transition
→ occurs when dominance shifts from one scope to another

Latent Degrees of Freedom
→ suppressed variables that may destabilize a scope when activated

---

# 7 Conceptual Summary

Scope dominance describes when a descriptive regime remains capable of organizing
system behavior.

In the cognitive architecture:

Scope dominance = dominant processing mode.

Loss of dominance triggers:

- increased salience
- evaluation of alternative modes
- potential scope transition.

This principle provides the structural foundation for context navigation in the agent.
