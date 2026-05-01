---
status: working-definition
layer: docs/glossary/
title: "Scope — Extended Definition"
created: 2026-05-01
extends: docs/glossary/scope.md
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
  - docs/core/cover_stability_criterion.md
---

# Scope — Extended Definition

This document extends the base scope definition in `docs/glossary/scope.md`
with three foundational clarifications that emerged from the multi-scale
observable analysis and the spring-mass chain case development. These
clarifications do not change the formal components S = (B, Π, Δ, ε) but
sharpen the epistemological commitments behind them.

---

## 1. A Scope Is a Stable Descriptive Regime, Not a Truth Claim

A scope S = (B, Π, Δ, ε) does not assert that a system *has* certain regimes.
It asserts that, relative to the chosen observables and resolution, stable
non-trivial distinctions can be made within B.

**Scope validity is a precondition for description, not a claim about
the system independently of description.**

The criterion for scope validity — that the cover C_ε is non-trivial and
Δ-stable — is a criterion about descriptive adequacy. A scope that fails
this criterion does not reveal that "no regimes exist"; it reveals that the
chosen (Π, Δ, ε) cannot sustain stable distinctions in B. The system is
not wrong; the description is inadequate.

This has a direct practical consequence: when a scope fails (F0–F3), the
correct response is to revise the description, not to conclude anything about
the system. Observable replacement, scope refinement, and sweep extension are
all descriptive revisions.

**Corollary:** Two scopes S and S' over the same B but with different Π, Δ, ε
may produce incompatible partition structures. Neither is more correct than the
other. They are answers to different descriptive questions.

---

## 2. Observable Admissibility Is Stability-Grounded, Not Ontologically Fixed

An observable π ∈ Π is admissible in scope S if and only if:

1. The cover C_ε(π, B) is non-trivial within B
2. The cover is Δ-stable: σ_Δ(x) < ε for all x in each cover element

This criterion is the same for all observables regardless of their physical
interpretation, temporal structure, or measurement modality.

**In particular: whether an observable is time-averaged, instantaneous,
structural, or configurational does not determine its admissibility.**
Admissibility is determined entirely by whether a stable non-trivial cover
exists at some ε in the admissible resolution regime.

The classification of observables by aggregation level (micro, meso, macro,
configurational) is a descriptive convenience, not a formal distinction within
the scope framework. What matters is whether the observable produces a stable
cover — everything else is substrate analysis (A0–A6) that establishes
*when* this condition is satisfiable.

**Consequence for scope design:** Any variable that can be evaluated over B
and produces a stable non-trivial cover is a legitimate member of Π. The
question "is this a valid observable?" reduces entirely to: does it produce
observable information in the sense of Definition 6 (Felder 2026)?

---

## 3. Time Is One Observable Among Many

The standard ARW pipeline uses time-averaged observables: Var_t[π(x(t))],
r_ss, and similar quantities. This is not a formal requirement of the
scope framework — it is a substrate choice.

Time enters ARW observables through the stationarity assumption A6: the
observable is assumed to produce consistent values once transients have
decayed. Under A6, the time average is a well-defined scalar over B. But
A6 is a substrate assumption, not a definition of what an observable can be.

**The formal status of time in ARW:**

Time is an ordering structure that we impose on the trajectory x(t) through
B-space. It is useful — and often necessary — for systems whose stable
existence is itself constituted by temporal trajectories (dissipative systems,
driven systems, biological systems). For such systems, time-averaging is not
merely convenient; it is the natural way to extract stable scalars from
inherently dynamic substrates.

However, time is not the only admissible ordering structure, and it is not
privileged within the scope framework. A configurational observable like
π_κ = {k_1,...,k_N} does not require time averaging — its substrate
satisfies A6 trivially because no temporal variation is assumed. This does
not make it less admissible; it makes A6 vacuously satisfied.

**More precisely:** The choice to use time as the primary ordering dimension
reflects a constraint on the observer, not a constraint on the scope
framework. Systems that require temporal trajectories for stable existence
impose time-structured observables on their observers. Systems that do not
have no such requirement.

**Consequence for multi-observable scopes:** A scope Π = {π_micro, π_meso,
π_macro, π_κ} where π_κ is a configurational observable and the others are
time-averaged is formally coherent. Each observable has its own substrate
(A0–A6 analysis), its own admissible resolution regime, and its own cover
structure over B. The fact that they operate on different temporal structures
does not prevent them from forming a joint cover over the same B.

---

## 4. Observable Latency and Cover Overlap

When a multi-observable scope Π = {π_1,...,π_k} is evaluated over B, the
covers C_ε(π_ℓ, B) for different observables may overlap, coincide, or
be mutually coarser/finer.

**Cover overlap as latency signature:**

If C_ε(π_ℓ, R) is non-trivial in region R ⊂ B while C_ε(π_m, R) is
trivial, observable π_m is *latent* with respect to π_ℓ in R: the
distinction that π_ℓ resolves is not yet visible in π_m at this ε.

This is not a deficiency of π_m — it is a structural property of their
relationship over B. The latency is defined entirely by the cover structure,
without reference to causality, temporal ordering, or physical mechanism.

**Directionality without time:**

The asymmetry between C_ε(π_ℓ, R) being non-trivial while C_ε(π_m, R)
is trivial defines a *direction* in the observable space: π_ℓ resolves
structure that π_m cannot. This direction — the loading of one observable's
cover structure onto another's — constitutes a form of directionality in the
observable space that does not require a temporal ordering.

Formally, the loading matrix

```
L_ℓm(b) = |∂π_ℓ / ∂π_m|   evaluated over B
```

measures how strongly π_ℓ co-varies with π_m across B. An asymmetric
loading matrix (L_ℓm >> L_mℓ) defines a directed structure in Π — not
because one observable precedes the other in time, but because one
observable's variation in B is more strongly coupled to the other's than
vice versa.

**Dynamical language as shorthand:**

When we say "a micro-level mode *propagates* to the macro level", this is
shorthand for: the cover structure of π_micro resolves a region R where
π_macro is still trivial, and L_macro,micro(R) > 0, meaning that as B
moves through R, π_macro will eventually resolve the same structure.
The "propagation" is not a temporal process — it is the geometry of the
cover structure in B-space.

---

## 5. Scope Choice Is Descriptive Intent, Not Privileged Access

The choice of S = (B, Π, Δ, ε) is a choice of descriptive intent. Different
scopes over the same system are not competing for the correct description —
they are providing answers to different questions.

This has two immediate consequences:

**5.1 No scope is more fundamental than another.** A scope using
configurational observables (π_κ) is not more fundamental than one using
dynamic observables (Var_t[d_i]), nor vice versa. Both are admissible if
their covers are stable. The question "which scope is right?" does not arise.
The question "which scope is appropriate for this descriptive purpose?" does.

**5.2 The admissibility criterion is the only universal constraint.** The
single formal constraint that applies to every scope equally is: observable
information must exist for each π ∈ Π at the working ε. This criterion
(Definition 6, Felder 2026) is scope-relative, observable-relative, and
resolution-relative. It makes no claim about the system beyond the conditions
under which a stable description is available.

---

## 6. Relation to the Base Scope Definition

This document does not modify the formal components B, Π, Δ, ε as defined
in `docs/glossary/scope.md`. It clarifies the epistemological commitments
that justify those definitions:

| Component | Formal role (base definition) | Epistemological commitment (this document) |
|---|---|---|
| B | Selects admissible states X_B ⊆ X | Defines the domain of the descriptive question |
| Π | Observable family | Each π is a descriptive commitment; admissibility is cover-stability |
| Δ | Admissible perturbations | Defines what the description must be robust against |
| ε | Resolution threshold | Sets the granularity of the description |
| S valid | Non-trivial Δ-stable cover exists | A well-posed descriptive question has been asked |
| S invalid | Cover trivial or unstable | The descriptive question cannot be answered at this level |

The scope framework is a **theory of descriptive adequacy**, not a theory
of what systems are. Regime structure is always relative to a scope. The
scope is always a choice.
