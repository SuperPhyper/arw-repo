---
status: note
layer: docs/notes/
title: "Scope Failure and Ontological Projection"
created: 2026-05-09
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/admissibility.md
  - docs/advanced/epistemic_ceilings_as_scope_saturation.md
  - docs/art_instantiations/epistemic_context_and_functional_admissibility.md
  - docs/advanced/causality_as_directed_observable_structure.md
open_questions:
  - Q-PROJ-01
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

## 7. Open Question

**Q-PROJ-01:** The failure structure at an admissibility boundary (the
specific F-type mode, the region of B where it occurs, the direction
of approach) may carry partial information about what a more complete
parametrisation would need to provide. For example: an F0 failure
(observable outside R(π)) identifies a structural class of observable
that fails here — which implies a structural requirement on any
observable that would succeed here. Can ARW generate such structural
requirements systematically from the failure mode? That is, can the
description of where and how a scope fails constrain the form of a
successor scope — without projecting the current scope's content beyond
its boundary?

This is distinct from the projection error: it asks not what the system
is beyond the boundary, but what a valid description beyond the boundary
would need to look like, given the failure structure.
