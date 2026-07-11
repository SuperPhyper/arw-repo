---
status: note
layer: docs/context_navigation/
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/observable_decomposition.md
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/core/cover_stability_criterion.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
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

## 2.6 χ_mode — Formal Derivation and Local-Max Correction (Q-CNS-06)

**Definition.** Building on the regime-cell reading of "mode" (§1.3) and the
revised salience formulation (§2.2), the minimal fluctuation observable for
cognitive mode transitions is the derivative of regime-cell occupancy with
respect to context_load. Occupancy is a soft assignment of `action_dist`
(see `context_navigation_emergent_modes_experiment.md` §2.1) to regime
centroids:

```
p_i(c) = softmax_i(-β · d_i(c)),   d_i(c) = dist(action_dist(c), μ_i)
χ_mode(c) := ∂p_i(c) / ∂c
```

This is the cognitive-architecture instance of χ = ∂r_ss/∂κ
(Q_NEW_12, `arw-observable-analysis` skill, consequence K6). Both are
fluctuation observables (class ∉ E) built as the derivative of an
aggregation-class observable with respect to the sweep parameter, and
both are expected to peak at the transition point (θ* / zone boundary)
rather than being computable as a class-E stationary mean. Resolving the
finite-difference bias below for χ_mode directly informs Q_NEW_12 in the
physical case portfolio, and vice versa — this is a signature-level
transfer candidate between the cognitive and physical case lines
(cf. monograph transfer chapter, WP-A5).

**Bottom-up decomposition.**

1. `action_dist`: Aggregation (ensemble mean over window) ∘ Restriction³
   (zone / episode / action-space window)
2. Centroid distance / softmax assignment: Restriction (projection onto
   regime centroids)
3. Simplex normalization: Restriction (scaling)
4. Derivative w.r.t. context_load: **Approximation** (finite difference
   in any pipeline implementation, not an exact continuum operation)

BC structure notation: **R⁴·A·Approx**

This differs from `r_ss` (R³·A·D) and `var_rel` (R³·A²·S) both in being
more Restriction-heavy and, critically, in carrying the same Approximation
component as `lambda_proxy` — the component already known to produce
structural insufficiency near regime boundaries (A6.1/A6.2 violations).

**Local Lipschitz constant.** For a two-class softmax at the decision
boundary (p_i ≈ 0.5):

```
∂p_i/∂c = -β · p_i·(1-p_i) · ∂d_i/∂c
L(c*) ≈ (β/4) · max|∂d_i/∂c|
```

Unlike κ_c or E_sep, this divergence is not enforced by system dynamics
(Z_shared in the K1 sense) — it is governed by β, the softmax temperature
of the regime-assignment procedure itself. β is not currently part of
`B_emergent` in `context_navigation_emergent_modes_experiment.md` and
should be added as an explicit boundary constraint if χ_mode is adopted
as an observable for S_emergent.

**Finite-difference bias (parallel to C1/C2).** For a naive
finite-difference estimator with step h, against a true transition of
width w and total jump Δp:

```
χ_mode^FD(c) = [p_i(c+h) − p_i(c)] / h ≈ Δp/h     when h ≥ w
L(c*)_true / χ_mode^FD ≈ h/w
```

This reproduces the C1 structure (2026-06-02 σ_Δ-proxy correction,
`arw-repo-context` skill §8) exactly: as training sharpens the behavioral
zone boundary (w → 0) at fixed sampling resolution h, the naive estimator
increasingly under-reports the true divergence — a one-sided false
negative at precisely the point where the observable is meant to be
most sensitive.

**Local-max correction.**

```
χ_mode^LM(c) := sup_{h' ≤ r} | p_i(c+h') − p_i(c) | / h'
```

This is the discrete analog of Corollary 1's local-max Lipschitz constant
L(x) = max_{|δ|≤r}|∇O(x+δ)|. It converges toward the true divergence as
data resolution improves, rather than saturating at Δp_max/h.

**Stability condition.**

```
(β/4) · max|∂d_i/∂c| · r < ε
```

The cognitive-specific extension of Corollary 1's L·r < ε: the admissible
resolution region for χ_mode depends jointly on Δ (context_load
perturbation bound r), ε, and β (assignment temperature) — a degree of
freedom absent from the physical cases.

**Pipeline implication.** If χ_mode is estimated from trajectory data, use
the sup-over-secants estimator χ_mode^LM, not the naive finite-difference
form — otherwise the same bias corrected for σ_Δ on 2026-06-02 reappears
one level up, in the mode-assignment observable rather than the raw
system observable.

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
| Q-CNS-06 | What is the minimal fluctuation observable for cognitive mode transitions? Does it show a Z_shared peak at transition points? — **Partially resolved** (§2.6): χ_mode defined and decomposed (R⁴·A·Approx); local-max correction χ_mode^LM derived by analogy with Corollary 1. Two independent candidate operationalizations now exist (2026-03-29 mode-switch-rate proxy; 2026-07-08 χ_mode^LM) — not yet reconciled. Open: empirical validation that either shows the predicted peak in trained-agent trajectory data. Cross-references Q_NEW_12 (physical case) as a shared signature-level transfer problem. | high |
| Q-CNS-06a | Should β (softmax assignment temperature) be added to `B_emergent` as an explicit boundary constraint, given it governs L(c*) independently of system dynamics? | medium |
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
| χ_mode | Fluctuation observable ∂p(R_i\|context_load)/∂c. R⁴·A·Approx. Cognitive instance of Q_NEW_12; requires local-max estimator (§2.6), not naive finite difference. |

---

## Maintenance History

- **2026-07-08 (merged into repo 2026-07-11):** Added §2.6 (χ_mode — formal derivation and
  local-max correction, Q-CNS-06). Decomposed χ_mode bottom-up (R⁴·A·Approx), derived local
  Lipschitz constant L(c*) ≈ (β/4)·max|∂d_i/∂c| for the softmax regime-assignment case, showed
  the finite-difference bias reproduces the C1 structure (2026-06-02 σ_Δ-proxy correction) via
  L(c*)_true/χ_mode^FD ≈ h/w, and derived the local-max estimator χ_mode^LM by analogy with
  Corollary 1. Flagged β as a candidate addition to `B_emergent`. Updated §4 (Q-CNS-06 status,
  new Q-CNS-06a), §6 (summary row), and front-matter `depends_on`. Imported from a session note
  reconstructed offline (no live repo access at drafting time); reconciled against the existing
  Q-CNS-06 entry in `docs/notes/open_questions.md`, which already carried an independent
  2026-03-29 partial answer (mode-switch-rate proxy) — both are recorded as separate candidate
  operationalizations rather than one superseding the other.
