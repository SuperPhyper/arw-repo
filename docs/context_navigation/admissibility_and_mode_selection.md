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

Mode switching therefore corresponds to a **regime transition within S_global** — the system moves from one stable partition cell to another. This is not a scope transition: a scope transition would require S_global itself to become invalid (all π ∈ Π entering Z(π)). See `mode_scope_regime_audit.md` §2.3.

---

# 5 Relationship to Salience

Salience emerges from differences in admissibility between competing modes.

Contexts become salient when multiple modes show similar admissibility levels
or when admissibility changes rapidly.

One possible operational definition:

S(c) = Var_m(A(m|c))

Salience therefore indicates contexts where mode choice becomes structurally relevant.

---

# 6 Observable Range of the Salience Estimator

## 6.1 Pre-Scopal Substrates of S(c)

The salience estimator S(c) = Var_m(A(m|c)) is itself an observable — a projection
of the joint agent-context state onto a scalar fitness-variance measure.

Like all ARW observables, it carries **pre-scopal substrate assumptions** that
define where it is valid:

| ID | Assumption | Violated when |
|----|-----------|---------------|
| A4 | The admissibility function A(m|c) is approximately stationary within the current context region. | The agent is crossing a zone boundary: the constraint structure is changing, so A(m|c) is non-stationary. |
| A_conv | The fitness estimates F_m(c) from anchor comparison have converged for the current context. | The agent is in a novel context with no nearby anchors; estimates are unstable. |
| A_sep | The modes are sufficiently distinct that Var_m(A(m|c)) has a stable non-degenerate value. | All modes have collapsed to identical admissibility (full scope failure) or one mode dominates completely (trivial partition). |

The **observable range** of S(c) is:

R(S) = { c | A4 holds, A_conv holds, A_sep holds }

## 6.2 Exclusion Zone Z(S) — The Scope Transition Window

The exclusion zone Z(S) is the set of contexts where S(c) cannot be interpreted
as a mode-competition signal:

Z(S) ⊇ { c | zone boundary crossing is in progress }

This is the structural analog to Z(r_ss) at κ_c in CASE-20260311-0001:
r_ss violates its stationarity assumption at the Kuramoto phase transition,
just as S(c) violates A4 during a zone boundary crossing.

**Key implication:** A high salience reading at a zone boundary does not
unambiguously indicate mode competition. It may instead indicate that the
salience observable itself has entered its exclusion zone — an
**F0 condition** (observable outside R(π)), not an admissibility signal.

## 6.3 F0 Condition for Salience

The ARW falsification category F0 applies when an observable is used outside
its observable range:

```
F0: R(S) ∩ B_active ≠ B_active
Severity: observable_replacement
```

For the salience estimator, F0 is expected to occur at every zone boundary
crossing — by design. This is not a failure of the agent architecture; it is
a structural property of the salience observable.

**The correct interpretation is therefore:**

- Salience spike **inside** a zone (within R(S)): genuine mode competition;
  admissibility is contested; a scope transition may be imminent.
- Salience spike **at** a zone boundary (S(c) ∈ Z(S)): observable in F0
  condition; the spike reflects substrate violation, not mode competition.
  The agent has already entered the new scope; mode selection should use
  anchor comparison rather than the live salience signal.

## 6.4 Discriminating F0 from Genuine Competition

The agent cannot observe zone boundaries directly (it does not have a
global map). A practical discrimination heuristic:

1. **Anchor availability:** If no anchor exists near the current context,
   the agent is likely in a transition or novel zone. Weight live salience
   less; rely on exploratory mode.

2. **Salience persistence:** Genuine mode competition produces sustained
   elevated salience. Zone-crossing F0 events are transient — salience
   returns to a stable level once the new zone's constraint structure is
   established and A4 is restored.

3. **Post-consolidation sharpening:** After a consolidation phase, the
   agent has updated admissibility estimates for recently visited contexts.
   Salience readings that were ambiguous online may be classified retrospectively
   as F0 events (boundary crossings) vs. genuine competition events. This is
   one structural function of the consolidation phase in ARW terms:
   **retrospective F0 classification**.

---

# 7 Anchor Memory and Admissibility Estimation

Anchor memory stores prototypical experiences where a mode was successful.

Anchors therefore approximate the admissibility function by providing empirical
examples of contexts where a given mode remained stable.

Admissibility estimation may be approximated by comparing the current context to
stored anchors.

Anchors accumulated within a zone's interior (away from boundary crossing events)
are more reliable estimates of A(m|c) than anchors formed during transition episodes.
The stability_score field of each anchor should reflect this: anchors formed during
high-salience transient events (candidate F0) should carry lower stability scores
and be subject to replacement first during consolidation.

---

# 8 Offline Consolidation

During consolidation phases the agent:

- reorganizes anchor prototypes
- re-evaluates admissibility regions
- identifies contexts where scope mismatch occurred
- **retrospectively classifies salience events as F0 (boundary crossing)
  vs. genuine admissibility competition** (see §6.4)

This process refines the structural map between contexts and admissible modes.

---

# 9 Conceptual Summary

Admissibility provides the structural principle linking ARW scope theory to the
agent's cognitive architecture.

Key correspondences:

| ARW concept | Agent component |
|-------------|----------------|
| Scope | Processing mode |
| Latent degrees of freedom | Suppressed observables |
| Loss of scope dominance | Mode inadmissibility |
| Regime transition within S_global | Mode switching |
| Chaos / instability | Signal of scope mismatch |
| Observable range R(π) | Valid operating region of the salience estimator |
| Exclusion zone Z(π) | Zone boundary crossing window |
| F0 failure | Salience spike at boundary (substrate violation, not mode competition) |
| Consolidation | Retrospective F0 classification + partition sharpening |

This interpretation grounds mode selection in structural compatibility rather
than heuristic switching rules, and grounds the salience estimator's limitations
in the ARW observable range formalism rather than treating them as engineering
edge cases.
