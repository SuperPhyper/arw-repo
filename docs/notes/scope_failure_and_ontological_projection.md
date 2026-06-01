---
status: note
layer: docs/notes/
title: "Scope Failure and Ontological Projection"
created: 2026-05-09
last_updated: 2026-05-29
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/admissibility.md
  - docs/advanced/epistemic_ceilings_as_scope_saturation.md
  - docs/art_instantiations/epistemic_context_and_functional_admissibility.md
  - docs/advanced/causality_as_directed_observable_structure.md
  - docs/bc_taxonomy/bc_failure_signatures.md
open_questions:
  - Q-PROJ-01 (partially addressed in §9)
update_notes: >
  2026-05-29: Added §7 (BC failure signatures and projection error structure),
  §8 (philosophical contexts beyond physics — consciousness, species, social scopes),
  §9 (self-application of ARW, partial answer to Q-PROJ-01 via bc_failure_signatures).
  Core argument (§1–6) unchanged.
---

# Scope Failure and Ontological Projection

## 1. The Core Observation

F-type failures (F0–F4) are description-relative. They are properties
of a scope S = (B, Π, Δ, ε) at its admissibility boundary — not
properties of the system beyond that boundary.

When a scope fails at its boundary, the failure has a pattern: a
specific failure mode (range collapse, partition instability, plateau
absence) at a specific region of B. This pattern is informative about
the scope. It is not informative about what the system is, does, or
requires beyond the boundary.

**The projection error** is treating the failure pattern as an
ontological claim about what lies beyond the admissibility boundary.
The scope is silent beyond its boundary. The failure marks where silence
begins — not what the silence contains.

---

## 2. Structure of the Error

A scope S reaches its admissibility boundary at some region R ⊆ B.
Within R, one or more of the following holds:

- **F0:** Observable Π lies outside R(π) — the pre-scopal substrate
  collapses. The observable is structurally invalid here.
- **F2:** The partition is not Δ-stable — the scope cannot reproduce
  its own distinctions under admissible perturbations.
- **F3:** No ε produces a non-trivial, Δ-stable cover — no partition
  is robust at any resolution.

Each failure mode characterises a different way in which the description
breaks down in R. None of them characterise what is in R from a more
complete parametrisation's perspective. They characterise the scope's
inability to describe R, not R's structure.

**The projection mechanism:** The failure has a shape. It arrives from
a direction — the scope was describing something coherent, and then it
stopped. The pattern of approach looks like it is pointing at something.
The error is to follow that pointing and conclude that the shape of the
failure reveals the structure of what lies beyond.

---

## 3. The Enabling Condition: Implicit Admissibility Boundaries

The projection error is structurally enabled when admissibility
boundaries are not explicit.

Without an explicit boundary marker — without the scope declaring "I
fail here, for this reason, in this mode" — the failure is invisible
as a failure. It appears as a finding. The description seems to continue
beyond its valid range, and claims accumulate that the scope cannot
support.

This is the mechanism by which models become larger than they are.
Not through deliberate overreach, but through the absence of structural
resistance at the boundary. If the boundary is unmarked, there is no
signal to stop. The description extends into the region of its own
failure and reports the failure pattern as a result.

**Formal statement:** A scope S makes claims over B implicitly bounded
by its admissibility region A(S). If A(S) is not explicitly delimited
— if the F-type failures at ∂A(S) are not identified and named — then
claims derived from S in the region R ∩ ∂A(S) carry no declared scope
restriction. They appear as results over all of B.

---

## 4. Bell Inequalities as Primary Example

The violation of Bell inequalities by quantum systems is an F2-type
finding about the LHV scope:

```
S_LHV = (B_bipartite, Π_outcomes, Δ_LOCC, ε)
```

Under this scope, the joint partition R_AB is not Δ-stable as a product
partition R_A × R_B. No local hidden variable assignment stabilises the
bipartite partition under the perturbation class Δ_LOCC.

This is a failure of S_LHV at its admissibility boundary. It is a
statement about S_LHV.

The standard interpretation — "locality is disproven" — is the
projection error. The F2 failure of S_LHV tells us that no scope of
the form S_LHV can produce a stable product partition here. It does
not tell us whether a more complete parametrisation of B would restore
a locally-causal structure, reveal a non-local one, or dissolve the
distinction entirely.

The admissibility boundary of S_LHV is where S_LHV is silent. The
projection error mistakes that silence for a positive claim about the
system's non-locality.

---

## 5. Distinction from Epistemic Ceilings

This note addresses a different failure mode than the one documented
in `docs/advanced/epistemic_ceilings_as_scope_saturation.md`.

| | Epistemic ceiling | Ontological projection |
|---|---|---|
| **Location** | Inside the scope's admissibility region | At or beyond the admissibility boundary |
| **Mechanism** | Cover exhausted — (Π, Δ, ε) produces no new distinctions | Failure pattern misread as external claim |
| **Error type** | Methodological: more effort of the same kind won't help | Categorical: scope claims are extended beyond their range |
| **Resolution** | Scope change: extend Π, decompose Δ, calibrate ε | Boundary identification: mark where the scope fails and declare silence |

Both errors result in descriptions that are larger than their actual
admissibility warrants. But the mechanism differs: the ceiling error
is about exhausting capacity; the projection error is about crossing
the boundary without marking it.

---

## 6. ARW as a Projection Filter

ARW's primary contribution in this context is not a deeper picture of
what lies beyond admissibility boundaries. It is the systematic
identification of where those boundaries are and what kind of failure
occurs at them.

The F-schema (F0–F4) is a boundary-marking instrument. Each category
names a specific failure mode and locates it at a specific level
(observable, partition, scope). The A_f / A_h distinction marks the
boundary between what is functionally operable and what is formally
coherent but epistemically unreachable.

These instruments do not reveal what is beyond the boundary. They make
the boundary visible — and thereby make the projection error visible as
an error.

**The minimal claim:** A description that has identified its F-type
failures is a description that knows where it stops. That knowledge
does not add content beyond the boundary. It prevents content from being
projected beyond the boundary under the appearance of being within it.

---

## 7. BC Failure Signatures and the Structure of the Projection Error

*(Added 2026-05-29 — integrates bc_failure_signatures.md developed in
monograph session.)*

The projection error is not uniformly shaped. Its structure depends on
which BC class is generating the regime being described. This has a
concrete consequence: the specific form of the projection error can be
predicted from the operative BC class.

**Coupling BC:** The instability band at the coupling threshold (Z_shared)
is the admissibility boundary. The projection error characteristic of
coupling scopes is to read the instability as a claim about the system
beyond the threshold — e.g., "the system becomes incoherent" rather than
"the scope loses its ability to make zone assignments here." The failure is
about the description, not the system.

**Restriction BC:** The separatrix is a genuine F0 boundary — the observable
loses its referent. The characteristic projection error is to treat the
observable null (ω = 0 at the separatrix) as a statement about the system
(the system "has no frequency") rather than about the scope (this observable
class cannot be extended through this boundary).

**Dissipation BC:** The failure is gradual (fragility increase). The
projection error is to read increasing fragility as a statement about the
system's "inherent instability" rather than about the attractor depth
decreasing within the current scope's conditions.

The general principle: the failure mode taxonomy (F0, F-gradient, Z_shared)
describes scope properties at the boundary. The BC class determines which
failure mode characteristically appears. Reading either as claims about the
system beyond the boundary is the projection error in its BC-specific form.

*See:* `docs/bc_taxonomy/bc_failure_signatures.md` for the full failure
signature taxonomy by BC class.

---

## 8. Philosophical Contexts Beyond Physics

*(Added 2026-05-29 — extends the worked example range for monograph Part IX.)*

The Bell inequality example (§4) operates in physics, where admissibility
boundaries are relatively well-defined. The projection error is equally
prevalent in philosophical and social-scientific contexts, where
admissibility boundaries are typically unmarked.

**Consciousness and mental causation.** The question "what is consciousness
really?" is frequently a dispute over admissibility conditions, not over the
substrate. Different scopes — neurological, phenomenological, functionalist
— have different Π and different Δ. Each encounters failure at its boundary
and the characteristic projection error is to treat that failure as evidence
about what consciousness "is" beyond the boundary of the failing scope.
The hard problem of consciousness is, in ARW terms, a family of projection
errors from scopes with incompatible admissibility conditions.

**Species and natural kinds.** The species problem in biology — the
proliferation of incompatible species concepts — is not resolved by finding
the "real" species concept. Different species concepts are scopes with
different observables (morphological, genetic, reproductive). Each fails at
its boundary in characteristic ways; the failure patterns generate the
appearance of contradictory facts about the same organisms. The productive
question is not "which concept is correct?" but "what is the admissibility
region of each, and where do they overlap?"

**Social and institutional description.** Questions like "what is the
real cause of organisational failure?" systematically project the failure
signatures of the operative BC class (e.g., dissipation exhaustion
described as "inherent instability," coupling failure described as "lack
of leadership") onto the system beyond the scope's admissibility boundary.
The description stops working; the failure pattern is reported as a finding
about the system.

The structural point across all these cases: making admissibility boundaries
explicit converts apparent ontological disputes into tractable scope
comparisons. The disagreement does not dissolve — different scopes remain
valid in their respective regions — but it becomes the right kind of
disagreement: about scope conditions, not about reality.

---

## 9. Self-Application and Q-PROJ-01 Update

*(Added 2026-05-29 — addresses reflexivity and partial answer to Q-PROJ-01.)*

**Self-application.** ARW itself is a description — a scope that describes
scope structure. As such it has its own admissibility conditions: it requires
that the system being described has enough coherence to have a describable
BC structure at all. Below a certain pre-scopal threshold, the framework has
no purchase. The projection error applies to ARW itself: treating the BC
taxonomy as a view from nowhere — as unconditionally valid rather than
scope-valid — would be the projection error at the meta-level. ARW's
admissibility boundary is the condition under which the taxonomy's answers
become unstable: when the same system admits multiple incompatible BC
characterisations even after careful analysis, the taxonomy is approaching
the edge of its own scope. This is diagnostic, not refutatory.

**Q-PROJ-01: Partial answer.** The question — can failure structure
constrain the form of a successor scope? — is now partially addressable via
`bc_failure_signatures.md`.

An F0 failure in a coupling-BC scope implies that any successor scope
operating across the coupling threshold requires an observable that either:
(a) does not use the collective-mode signal that fails at κ_c, or
(b) explicitly models the instability band as part of its structure rather
than as a measurement artefact.

An F0 failure in a restriction-BC scope (separatrix crossing) implies that
the successor scope requires an observable with a referent on both sides of
the boundary — one that does not have a null point at the transition itself.

The general form of the partial answer: the BC class of the failing scope
constrains the observable class that a successor scope would need to use.
The failure mode narrows the admissibility class of successor observables —
without specifying which member of that class is appropriate. That
specification still requires empirical access to the region beyond the
boundary.

This does not fully resolve Q-PROJ-01, which asks for a systematic
procedure. But it replaces the question's open-ended form with a structured
one: successor scope constraints are BC-class-specific, and the constraint
is on the observable class, not on the boundary conditions.
