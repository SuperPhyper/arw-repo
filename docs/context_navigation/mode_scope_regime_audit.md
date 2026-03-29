---
status: note
layer: docs/context_navigation/
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/observable_decomposition.md
  - docs/bc_taxonomy/boundary_condition_classes.md
supersedes_claims_in:
  - docs/context_navigation/context_navigation_model_spec.md
  - docs/context_navigation/admissibility_and_mode_selection.md
  - docs/context_navigation/modal_cognition.md
---

# Conceptual Audit: Mode, Scope, and Regime in the Cognitive Architecture

## Purpose

This document corrects a structural ambiguity in the cognitive architecture layer
of the ARW/ART repository. It establishes the precise relation between the terms
**system**, **scope**, **regime**, and **mode**, and identifies where existing
documents require revision.

This document does not replace those documents. It serves as the reference
for how they should be revised.

---

## 1. The Core Clarification

### 1.1 System = Scope

In ARW, a **system** is not an independent object prior to description.
A system is always already a scope: a stabilized descriptive regime
constituted by the tuple

```
S = (B, Π, Δ, ε)
```

There is no "system" apart from the scope that makes it describable.
The phrase "the system and its scope" is therefore redundant at best
and misleading at worst — it implies a substrate that exists independently
of the scope relation. This is not the ARW position.

**Consequence:** When the cognitive architecture refers to "the agent system,"
it refers to S_global — the scope within which the agent's behavior
is described. The agent does not *have* a scope; the agent *is* a scope
from the perspective of the observer.

---

### 1.2 Regimes Are Sub-Scopes — But Conditionally

A **regime** is a stable, distinguishable region of the parameter space P
within a given scope S. It is a sub-scope in the following precise sense:

A regime R_i is a sub-scope of S_global if and only if:

1. R_i is a stable partition cell in the partition induced by S_global
2. The boundary conditions active in R_i are a restriction or
   specialization of those in S_global
3. The observables Π_i ⊆ Π active in R_i produce stable descriptions
   within R_i (i.e. R_i ⊆ R(π_i) for all π_i ∈ Π_i)

This is the critical point: **a regime exists as a sub-scope only
by virtue of the partition in S_global.** It is not independently defined.
If the partition collapses — as at a phase transition or salience event —
the sub-scope loses its basis. There is no regime; there is only S_global
in an unresolved state.

```
S_global = (B, Π, Δ, ε)
  ├── R_1  (stable partition cell → sub-scope)
  ├── R_2  (stable partition cell → sub-scope)
  ├── ...
  └── [transition zone: no stable sub-scope; S_global only]
```

---

### 1.3 Modes Are Regimes — Not Independent Scopes

A **processing mode** in the cognitive architecture is a regime in S_global.
It is a sub-scope whose existence is grounded in the stability of
the global partition.

Modes are not:
- independently defined scopes with their own (B, Π, Δ, ε)
- competing agents with separate descriptive frameworks
- persistent structures that survive the collapse of their partition cell

Modes are:
- stable, distinguishable regions in the global partition of agent behavior
- characterized by which observables π_m ∈ Π are active and stable
- differentiated by their BC class structure (which boundary conditions
  dominate within that regime)
- temporary: they exist only as long as the partition in S_global supports them

**The single most important sentence:**

> A mode is a regime in S_global — a sub-scope whose existence depends
> on the stability of the global partition, not on an independent
> scope definition.

---

## 2. Consequences for Key Concepts

### 2.1 Mode Admissibility

Previous formulation (admissibility_and_mode_selection.md):

> A(m|c) = degree to which mode m remains structurally compatible
> with context c

This is a valid intuition but not grounded in the ARW apparatus.

**Revised formulation:**

A mode m is admissible at parameter point p if and only if:

```
p ∈ R(π_m)   for all π_m ∈ Π_m
```

That is: all observables active in mode m are within their observable
range at p. This is the standard ARW admissibility condition applied
to the sub-scope R_m.

Mode inadmissibility is therefore not a property of the mode relative
to a context in some informal sense — it is a structural condition:
the observables of the mode have left their valid range.

Loss of mode admissibility = F0 condition for the sub-scope R_m.

---

### 2.2 Salience

Previous formulation (admissibility_and_mode_selection.md):

> S(c) = Var_m(A(m|c))

This is a class-E observable: it requires stationary, ergodic measurement
of admissibility across modes. It fails structurally at the transition
point — which is precisely where salience is most relevant.

**Revised formulation:**

Salience is the signal that the current parameter point p is approaching
or entering Z_shared — the universal exclusion zone where no class-E
observable (no stationary-expectation observable) in Π_m remains valid.

Formally:

```
Salience(p) ~ distance(p, Z_shared)^{-1}
```

More precisely: salience is a fluctuation observable, not a class-E
observable. It is maximal at the transition point, not computable
from a mean across modes. The appropriate observable class is
analogous to χ = ∂r_ss/∂κ in CASE-20260311-0001:

```
χ_mode = ∂(mode_distribution)/∂(context_load)
```

This observable belongs to the fluctuation class, lives outside class E,
and has R(χ_mode) ∋ transition points — precisely where class-E
observables fail.

**Open question Q-CNS-06** (new):
What is the minimal fluctuation observable for cognitive mode transitions,
and does it show the Z_shared peak predicted by the ARW framework?

---

### 2.3 Mode Switching

Previous formulation: mode switching = scope transition.

**Revised formulation:**

Mode switching is a **regime transition** within S_global.
It is not a scope transition in the sense of leaving S_global.
The observer's scope (S_global) remains constant; what changes is
which partition cell the system occupies.

A scope transition would mean that S_global itself becomes invalid —
that the observables in Π cease to produce stable descriptions of
the agent at all. This is a much stronger condition and corresponds
to a breakdown of the descriptive framework entirely, not merely
a mode change.

Distinction:

```
Regime transition:  agent moves between R_i and R_j within S_global
                    → mode switch
                    → S_global partition updated, not replaced

Scope transition:   S_global loses validity
                    → all π ∈ Π enter Z(π)
                    → descriptive framework fails
                    → requires new scope, not new mode
```

---

### 2.4 Consolidation

Previous formulation (B5): consolidation sharpens regime partition boundaries.

**Revised formulation:**

Consolidation is a dissipation process operating on the space of
anchor representations. By K6 from the observable analysis skill,
dissipation produces projective mapping onto attractors only
asymptotically — not as a finite operation.

Therefore: consolidation does not sharpen partition boundaries by
mechanism. It *tends toward* sharper boundaries as a limit process.
The claim "consolidation stabilizes the context map" is a
limit-hypothesis, not a design principle.

This has an experimental consequence: consolidation effects on
partition stability should be measurable as a monotone approach
to a stable partition over repeated cycles — not as an
immediate post-consolidation sharpening.

This is the content of Q-CNS-03, which should be updated to
reflect that the expected signature is asymptotic, not step-like.

---

### 2.5 BC Classes of Modes

Previous treatment: modes are assigned BC classes (Restriction-mode,
Coupling-mode, etc.) as system properties.

**Revised formulation:**

BC classes characterize the boundary conditions that dominate
within a regime R_m — they are scope properties of R_m as a sub-scope
of S_global. Since S_global = system (from 1.1), and R_m is a
sub-scope grounded in S_global's partition, BC classes of modes
are properties of the sub-scope, not of the agent independently.

This resolves Q_NEW_9 partially for the cognitive architecture case:
BC class is a scope property at the level of R_m, not a property
of the agent substrate.

The remaining open question is whether the BC class of R_m is
stable under changes to Π (i.e. if we observe the agent with
different observables, does the same mode appear to have the same
BC class?). This is Q_NEW_9 in its general form, still open.

---

## 3. Documents Requiring Revision

The following documents contain formulations that conflict with
the clarifications above. Revisions should reference this document.

| Document | Problem | Required change |
|---|---|---|
| context_navigation_model_spec.md | "Processing modes are reduced scopes S_mode = (B_mode, Π_mode, Δ_mode, ε_mode)" | Replace: modes are regimes in S_global; sub-scopes only insofar as the partition supports them |
| context_navigation_model_spec.md | "mode = argmax P(m\|c)" — implies modes are independent from S_global | Reframe: mode selection = identification of current regime cell in S_global partition |
| admissibility_and_mode_selection.md | A(m\|c) defined informally | Replace with: admissibility = R(π_m) condition per observable |
| admissibility_and_mode_selection.md | S(c) = Var_m(A(m\|c)) | Replace with: salience as fluctuation observable; class-E definition fails at transitions |
| admissibility_and_mode_selection.md | "mode switching = scope transition" | Replace with: mode switching = regime transition within S_global |
| context_navigation_model_spec.md B5 | "consolidation sharpens boundaries" | Replace with: consolidation is asymptotic dissipation; sharpening is a limit, not a step |
| bc_taxonomy_cognitive_modes.md | BC classes as system properties | Add: BC classes are sub-scope properties of R_m, grounded in S_global partition |

---

## 4. New Open Questions

These questions arise directly from the clarifications above and
should be added to docs/notes/open_questions.md.

| ID | Question | Priority |
|---|---|---|
| Q-CNS-06 | What is the minimal fluctuation observable for cognitive mode transitions? Does it show a Z_shared peak at transition points? | high |
| Q-CNS-07 | Is the BC class of a mode R_m stable under change of observation set Π? (cognitive instance of Q_NEW_9) | medium |
| Q-CNS-08 | What is the empirical signature of a scope transition (S_global failure) vs. a regime transition (mode switch) in behavioral data? | high |
| Q-CNS-09 | Does consolidation produce asymptotic partition sharpening (as predicted by dissipation analysis), or is there a faster mechanism? | medium |

---

## 5. What Remains Valid

The following claims in the existing documents are consistent with
the revised framework and do not require change:

- The agent architecture has a three-layer memory structure (B3, B4)
- Anchor memory stores prototypical regime experiences
- The labyrinth experiment operationalizes zone transitions as
  regime transitions in S_global
- Φ measures observable transfer, not agent transfer
  (transfer_semantics_context_navigation.md — this formulation is correct)
- The context partition is induced by the equivalence relation
  d(Π(x), Π(y)) ≤ ε ∧ mode(x) = mode(y) — formally correct,
  but "mode" should now be read as "regime cell in S_global partition"

---

## 6. Summary

| Term | Correct ARW reading |
|---|---|
| System | = Scope S_global. No substrate independent of the descriptive relation. |
| Regime | Stable partition cell in S_global. Sub-scope conditional on partition stability. |
| Mode | Regime in S_global. Not an independent scope. Exists only while partition supports it. |
| Mode admissibility | R(π_m) condition: observables of mode m within their valid range at p. |
| Salience | Fluctuation observable. Maximal at Z_shared boundary. Not computable as class-E mean. |
| Mode switching | Regime transition within S_global. Not a scope transition. |
| Consolidation | Asymptotic dissipation toward stable partition. Limit process, not mechanism. |
| BC class of mode | Sub-scope property of R_m. Grounded in S_global partition. |
