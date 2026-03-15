---
status: working-definition
layer: docs/context_navigation/
---


# Admissibility in Context-Navigating Cognitive Architectures

## Overview

This document translates the ARW concept of **admissibility** into the context-navigation
cognitive architecture used in this repository.

The concept originates from the ARW interpretation of chaos as a **scope mismatch** between
a stabilized descriptive regime and the degrees of freedom that remain dynamically active.

In the cognitive architecture, this idea becomes a principle governing **mode validity and
mode selection**.

---

# 1 ARW Definition of Admissibility

Within ARW, a **scope** is a stabilized descriptive regime.

A scope remains ordnend dominant as long as the degrees of freedom it suppresses remain
compatible with the boundary conditions active in the system.

Admissibility therefore describes the compatibility between:

- the freedoms stabilized (suppressed or aggregated) by a scope
- and the freedoms that remain dynamically active.

Admissibility is not binary. It degrades gradually as suppressed degrees of freedom begin
to influence system behavior.

Loss of admissibility manifests as:

- sensitivity to initial conditions
- path divergence
- breakdown of predictive stability

Chaos can therefore be interpreted as a signal that a scope has lost its ordering dominance.

---

# 2 Translation to Cognitive Architecture

In the cognitive architecture:

Global scope:
the full set of observables available to the agent.

Processing modes:
structured projections or subnetworks that reduce or prioritize observables.

Each mode therefore defines a **reduced descriptive scope**.

The central question becomes:

Can this reduced scope still stabilize the currently active degrees of freedom?

---

# 3 Definition of Mode Admissibility

For a processing mode m and context c:

A(m|c)

represents the degree to which the mode remains structurally compatible with the
current context.

A mode is admissible if the degrees of freedom it suppresses remain dynamically irrelevant
under the boundary conditions of the current context.

When suppressed variables become relevant, admissibility degrades.

---

# 4 Mode Selection

Mode selection follows the principle of **scope dominance**:

m* = argmax_m A(m|c)

The agent activates the processing mode whose scope remains most admissible in the
current context.

Mode switching therefore corresponds to **scope transition**.

---

# 5 Relationship to Salience

Salience emerges from differences in admissibility between competing modes.

Contexts become salient when multiple modes show similar admissibility levels
or when admissibility changes rapidly.

One possible operational definition:

S(c) = Var_m(A(m|c))

Salience therefore indicates contexts where mode choice becomes structurally relevant.

---

# 6 Anchor Memory and Admissibility Estimation

Anchor memory stores prototypical experiences where a mode was successful.

Anchors therefore approximate the admissibility function by providing empirical
examples of contexts where a given mode remained stable.

Admissibility estimation may be approximated by comparing the current context to
stored anchors.

---

# 7 Offline Consolidation

During consolidation phases the agent:

- reorganizes anchor prototypes
- re-evaluates admissibility regions
- identifies contexts where scope mismatch occurred

This process refines the structural map between contexts and admissible modes.

---

# 8 Conceptual Summary

Admissibility provides the structural principle linking ARW scope theory to the
agent's cognitive architecture.

Key correspondences:

Scope (ARW) -> Processing mode

Latent degrees of freedom -> Suppressed observables

Loss of scope dominance -> Mode inadmissibility

Scope transition -> Mode switching

Chaos / instability -> Signal of scope mismatch

This interpretation grounds mode selection in structural compatibility rather
than heuristic switching rules.
