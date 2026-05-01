---
status: hypothesis
layer: docs/advanced/
title: "Multi-Scale Observables and Latent Regime Formation"
created: 2026-04-30
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/observable_decomposition.md
  - docs/advanced/arw_emergence_bc_relative.md
  - docs/glossary/observable_range.md
related_cases:
  - CASE-20260318-0004
  - CASE-20260315-0007
open_questions:
  - Q-MULTI-01
  - Q-MULTI-02
---

# Multi-Scale Observables and Latent Regime Formation

This document develops the ARW treatment of observables that operate across distinct
aggregation levels — micro, meso, and macro — and the structural consequences for
regime visibility, scope validity, and bifurcation interpretation.

It extends the emergence analysis framework (see [Emergence Analysis](../advanced/arw_emergence_bc_relative.md))
from the two-level local/relational distinction to a general multi-scale case.

---

## 1. The Core Problem: Aggregation as Information Loss

A macro-observable π_macro is typically constructed as a spatial or ensemble
average over micro-states:

```
π_macro(x) = E[f(x_i) | i ∈ population]
```

This construction belongs to the **Aggregation BC class** (operator E[·|G]).
It is formally valid — it satisfies substrate assumptions A0–A6 across most of
the BC domain B — and therefore has a wide R(π_macro). However, its Z_cover
(the region where σ_Δ ≥ ε) is large with respect to **inter-group variation**.

**The key structural fact:** An aggregation-class observable compresses
high-dimensional micro-structure into a scalar. Variation *between* subgroups
is explicitly averaged out. The observable is within R(π) for the aggregate
quantity, but has Z_cover = ∅ only if inter-group variation is itself negligible.

**Consequence for scope design:** A scope that relies on π_macro alone to describe
a system with structural inter-group variation will exhibit a *cover that is stable
for the wrong question*. The partition structure produced is real, but it answers
only the question the observable can ask — which excludes sub-group dynamics.

This is not an F0 failure (the substrate is sound) and not F1 (the span may be
adequate). It is a **scope mismatch**: the scope is admissible for its stated
observables, but the stated observables are inadmissible for the scientific
question being posed.

---

## 2. The Three-Level Observable Architecture

ARW formalizes three structural levels of observable:

| Level | Observable type | Aggregation operator | BC class signature | Preserves sub-structure? |
|---|---|---|---|---|
| Micro (Π_micro) | Individual-state observables | None (direct measurement) | Restriction, Dissipation | Yes — by construction |
| Meso (Π_meso) | Structure-preserving group aggregations | E[·\|G] with group membership G fixed | Aggregation with Coupling | Partially — group structure retained |
| Macro (Π_macro) | Full-population aggregations | E[·\|all] | Aggregation | No — inter-group variation lost |

**Π_micro** resolves the finest level of structure. Its Z_cover is smallest
relative to micro-level variation, but it requires micro-level measurement access.

**Π_macro** has the widest R(π) but loses inter-group variation by construction.
Its Z_cover for sub-group regime questions is structurally determined and
cannot be reduced by any choice of ε or Δ.

**Π_meso** is the critical intermediate layer. A meso-observable *conditions*
the aggregation on a group structure G — it computes averages *within* subgroups
and retains the *distribution* of those averages across groups. This preserves
inter-group variation while still reducing micro-level noise.

**The central claim of this document (status: hypothesis):**

> Π_meso observables are the minimal observable class that simultaneously
> satisfies the substrate requirements of Π_macro (convergent, finite-variance,
> computable) and retains inter-group variation in R(π).

This makes Π_meso the structure-preserving aggregation layer that enables
regime detection at the meso-scale without requiring micro-level access.

---

## 3. Latent Regime Formation

A *latent regime* is a regime that is Δ-stable and non-trivial in BC space
but invisible to the observable family Π of the current scope.

Formally: a regime R is latent with respect to scope S = (B, Π, Δ, ε) if:

1. There exists an observable π' ∉ Π such that R is a component of C_ε(π', B)
2. For all π ∈ Π: R is not a component of C_ε(π, B) — it is not resolved
3. π' ∉ Z(π') in the region of B where R exists — the substrate is valid for π'

Condition 3 distinguishes a latent regime from a structurally inaccessible one.
A latent regime is *in principle observable* — it is invisible only because the
current Π does not contain a suitable observable.

**Latency is a cover-geometric property, not a dynamical one.**

Observable π_m is latent with respect to π_ℓ in region R ⊂ B if
C_ε(π_ℓ, R) is non-trivial while C_ε(π_m, R) is trivial. This is a
structural relationship between the two covers over B — it carries no
implication about temporal ordering, causal precedence, or physical mechanism.
The latency exists whether or not a trajectory visits R, and whether or not
time is the ordering dimension of the substrate.

**Latent regime formation** is the process by which a latent regime becomes
observable. In cover-geometric terms: it is the extension of C_ε(π', B) into
a region R where C_ε(π, B) for all π ∈ Π was previously trivial. This occurs
when σ_Δ(π', b) < ε for b ∈ R — i.e., when the perturbation spread of the
candidate observable falls below the resolution threshold in that region.

**Dynamical language as shorthand:**

Phrases like "a micro-level mode propagates to the macro level" are shorthand
for a cover-geometric statement: the cover of π_micro is non-trivial in a
region R where π_macro is still trivial, and the loading L_macro,micro(R) > 0
(see `docs/glossary/scope_extended_definition.md`, Section 4). The
"propagation" is the geometry of the cover structure in B-space. No temporal
ordering is implied by the latency itself.

---

## 4. The Cover Collapse Sequence

In a multi-scale system with latent regime structure, the cover collapse sequence
under increasing ε proceeds characteristically:

```
Low ε:
  Π_micro: non-trivial cover — resolves individual variation
  Π_meso:  non-trivial cover — resolves group-level variation
  Π_macro: non-trivial cover — resolves population-level variation

Intermediate ε (micro collapse):
  Π_micro: trivial (F1) — individual variation falls below ε
  Π_meso:  non-trivial — group structure still resolved
  Π_macro: non-trivial — population structure still resolved

High ε (meso collapse):
  Π_micro: trivial
  Π_meso:  trivial (F1) — group variation falls below ε
  Π_macro: non-trivial (if population-level variation exceeds ε)

Very high ε (macro collapse):
  All: trivial — ε*(O,X) reached for all observables
```

The regime windows at each scale form a nested structure:

```
I_ε(Π_macro) ⊆ I_ε(Π_meso) ⊆ I_ε(Π_micro)   [admissible intervals, generally nested]
```

Note: this nesting order holds for the admissible *upper* bounds (ε* values).
The lower bounds (determined by σ_Δ) are independent and may not preserve
this ordering.

---

## 5. Formal Implication: Bifurcation Reinterpretation

**ARW cover-geometric reinterpretation:**

A macroscopically abrupt transition at BC value θ* is the value at which
C_ε(π_macro, B) first resolves a boundary that C_ε(π_meso, B) or
C_ε(π_micro, B) already contained at lower BC values. The transition is
"abrupt" in π_macro because π_macro's cover structure has a narrow
emergence window there — not because the system changed suddenly.

This reinterpretation has three consequences:

1. **θ* is an observable property, not a system property.** A different
   π_macro (with different gradient profile) yields a different θ*.

2. **"Abruptness" is a cover-height property.** The transition appears
   abrupt when the cover height drops sharply near θ* in π_macro. A wide
   meso-level emergence window can precede a narrow macro-level transition.

3. **Prediction shifts from timing to structure.** The question is not
   "when will the transition occur?" but "which latent cover structure has
   already stabilised in π_meso or π_micro?" Detection of prior cover
   stabilisation in finer observables is the leading indicator — not
   because finer observables are causally prior, but because their cover
   geometry in B already resolves what π_macro cannot yet see.

---

## 6. The Meso-Observable Design Criterion

For Π_meso to serve as a structure-preserving aggregation, the following
conditions must be satisfied:

**Substrate validity (necessary):**
- A0–A6 must hold for π_meso within B, as for any observable.

**Structure preservation (necessary for meso function):**
- The group structure G must be empirically well-defined and Δ-stable:
  group membership must be persistent under admissible perturbations.
- π_meso must be sensitive to *between-group* variation, not only
  *within-group* means.

**Operational criterion:** A candidate meso-observable π' satisfies the
structure-preservation condition if:

```
Var_G[π'(x)] >> E_G[Var_within(π'(x))]
```

i.e., the variance *across* group means is large relative to the average
within-group variance. This ensures that π' carries inter-group information.

**Counter-example (scope design error):** An observable that computes the
average across the entire population without conditioning on G violates the
structure-preservation criterion and reduces to π_macro. Such an observable
will have Z_cover for inter-group variation regardless of how it is labeled.

---

## 7. Scope Design Implications

For a system suspected to contain latent meso-level regime structure, a
valid multi-scale scope must include at least one element of Π_meso.

**Minimal multi-scale scope:**

```
S_multi = (B, {π_macro, π_meso}, Δ, ε_vector)
```

where ε_vector = (ε_macro, ε_meso) and each component lies in the
admissible interval of the corresponding observable (see
[Multi-Observable Scopes](../advanced/multi_observable_scopes.md)).

**Scope diagnostic for latent regime failure:**

If a scope S = (B, {π_macro}, Δ, ε) produces:
- A stable macro-level partition at θ*
- No pre-transition signal in the macro observable
- A post-transition macro collapse (R1→R4-type jump)

Then the scope should be diagnosed as:
1. **Admissible for its stated scope** — π_macro had a valid plateau
2. **Inadmissible for the question** — the question required meso-level resolution
3. **Latent regime present** — a meso-observable with structure-preserving
   aggregation would have revealed R2/R3-type intermediate regimes

The correct response is not to redesign the scope's ε or Δ, but to extend Π
with a meso-observable. This is a **Π-extension**, not a resolution refinement.

---

## 8. Connection to Existing ARW Framework

**Cover height:** The cover-height function h(b_i) (see [Cover Height](../advanced/cover_height.md))
provides a multi-scale depth map for a *single* observable. In the multi-scale
case, a joint cover height over Π_meso would capture the ε-range over which
meso-level structure persists. A latent regime's meso-level cover height drops
to zero at the macro-observable's θ*, consistent with the bifurcation
reinterpretation in Section 5.

**Emergence analysis:** The micro/local vs. relational/collective distinction
in [Emergence Analysis](../advanced/arw_emergence_bc_relative.md) is a special
case of the three-level structure here. The "local observable" in CASE-0004
(amp_asym) corresponds to Π_micro; the "relational observable" (PLV) corresponds
to Π_meso (it aggregates phase relationships across the ensemble while preserving
their pairwise structure).

**BC class:** Aggregation-class observables (E[·|G] operator) are the canonical
Π_macro observables. Meso-observables with structure-preserving aggregation
combine Aggregation and Coupling operators — they aggregate within groups (E[·|G])
while preserving inter-group coupling structure.

---

## 9. Open Questions

**Q-MULTI-01 (open):** What is the formal condition under which a latent meso-level
regime becomes Δ-stable? The current hypothesis (σ_Δ < ε for π_meso) is
necessary but the dynamics by which this condition is approached are not
characterized. Is there an analogue of the cover-height persistence measure
for the transition into Δ-stability?

**Q-MULTI-02 (open):** Can the structure-preservation criterion (Var_G >> E_G[Var_within])
be operationalized as a pre-scopal substrate condition A7 for meso-observables?
This would allow substrate analysis to flag candidate meso-observables that
fail to preserve inter-group variation before they are committed to a scope.

---

## 10. Illustrative Application: Institutional System Scopes

The ART instantiation of this framework is documented in
`docs/art_instantiations/ariba_adoption_scope.md` (ART level; see that document
for concrete observable assignments). The current document provides only the
ARW-level formal structure.

The general pattern: in strongly institutionalized systems, macro-observables
(citywide readiness, aggregate throughput) satisfy substrate conditions
throughout B but have Z_cover for bureau- or unit-level variation. A scope
built on macro-observables alone is formally valid but scientifically
inadequate for detecting sub-institutional regime variation.

The transition from a pre-intervention "stable" state to a post-intervention
collapse is structurally analogous to an R1→R4 macro-cover collapse, with
R2/R3 latent regimes present throughout. Early detection requires Π_meso
observables conditioned on the relevant institutional grouping structure G.

---

## Status Note

This document is `hypothesis`. Promotion to `working-definition` requires:
- At least one ART case that operationalizes Π_meso observables and confirms
  the latent regime structure (Q-MULTI-01 partially answered)
- Formal treatment of the structure-preservation criterion as a substrate
  condition (Q-MULTI-02)
