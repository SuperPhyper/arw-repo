---
status: working-definition
layer: docs/advanced/
title: "Causality as Directed Observable Structure"
created: 2026-05-01
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/scope_extended_definition.md
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
related_cases: []
open_questions:
  - Q-CAUSAL-01
  - Q-CAUSAL-02
---

# Causality as Directed Observable Structure

This document develops the ARW treatment of causality as a scope-relative
property of the observable space. It does not propose a theory of causality
as a fundamental feature of systems. It specifies the conditions under which
a causal description is admissible within a scope, and the conditions under
which it breaks down.

This document is a direct extension of
`docs/glossary/scope_extended_definition.md`. The core commitments —
that descriptions are relative, that admissibility is stability-grounded,
and that time is one observable among many — are presupposed here.

---

## 1. The Claim

Causality is not a primitive property of a system. It is a stable,
directed structure in observable space that is admissible within a
scope when the following conditions hold:

1. A directed coupling exists between two observables π_A and π_B
   over B: variation in π_A induces structured variation in π_B.
2. This coupling is asymmetric: the induction is stronger in one
   direction than the other.
3. The coupling structure is Δ-stable: it persists under admissible
   perturbations at the working ε.

When these conditions hold, the scope admits the statement:
*"π_A is causally relevant for π_B within scope S."*

When any condition fails, the causal description is inadmissible — not
because causality has "disappeared", but because the descriptive
preconditions for a stable causal statement are not met.

---

## 2. Formal Definition

### 2.1 Observable Coupling

Let Π = {π_1,...,π_k} be the observable family of scope S = (B, Π, Δ, ε).
The **observable coupling** between π_A and π_B over B is:

```
L_{B,A}(b) = |∂π_B / ∂π_A|   evaluated at b ∈ B
```

This is the local sensitivity of π_B to variation in π_A across the
parameter domain. It is a scalar field over B.

**Note:** L_{B,A} is defined over B, not over time. It does not require
a trajectory or a temporal ordering. It is a property of the joint
cover structure of π_A and π_B over B.

### 2.2 Directed Coupling

The coupling is **directed** if:

```
L_{B,A}(b) >> L_{A,B}(b)   for b in some region R ⊆ B
```

Direction arises from asymmetry in the loading matrix, not from temporal
precedence. The statement "π_A influences π_B" means that variation in
π_A co-varies strongly with variation in π_B, while the converse is weak.

### 2.3 Causal Admissibility

A causal relation π_A → π_B is **admissible** in scope S in region R if:

```
(i)   L_{B,A}(b) >> 0                          for b ∈ R    [coupling exists]
(ii)  L_{B,A}(b) >> L_{A,B}(b)                 for b ∈ R    [asymmetric]
(iii) σ_Δ(L_{B,A})(b) < ε_coupling             for b ∈ R    [Δ-stable]
```

where ε_coupling is an appropriate resolution threshold for the coupling
field itself. Condition (iii) is the stability condition: the directed
coupling must be robust under admissible perturbations.

---

## 3. Relation to Cover Structure

The loading matrix L_{B,A} is directly related to the cover structure
of the observable family over B.

If C_ε(π_A, R) is non-trivial and C_ε(π_B, R) tracks the boundaries
of C_ε(π_A, R) — that is, π_B's cover boundaries coincide with or
follow π_A's cover boundaries in R — then L_{B,A} is large in R.

Conversely, if the covers of π_A and π_B are independent in R (their
boundaries do not align), L_{B,A} ≈ 0 in R and no causal admissibility
claim can be made.

**Observable latency and causal direction:**

If C_ε(π_A, R) is non-trivial while C_ε(π_B, R) is trivial in R, then
π_B is latent with respect to π_A in R (see
`docs/advanced/multi_scale_observables_and_latent_regime_formation.md`,
Section 3). In cover-geometric terms this means: the structure resolved
by π_A has not yet been resolved by π_B. The loading L_{B,A} is positive
but the cover of π_B has not yet responded.

This is the cover-geometric signature of causal precedence — without
requiring time as the ordering dimension. The "precedence" is a property
of the cover geometry in B, not a temporal statement.

---

## 4. When Causal Admissibility Fails

Causal admissibility fails under four structural conditions, each
corresponding to a different descriptive failure mode.

### 4.1 Aggregation-induced coupling loss

When π_B is a macro-level aggregation observable (E[·|all]), it loses
inter-group variation by construction. The loading L_{B,A} may vanish
in regions where π_A (a finer observable) is sensitive — not because
the coupling has disappeared in the system, but because π_B compresses
the dimension in which the coupling operates.

**Diagnosis:** C_ε(π_A, R) non-trivial, C_ε(π_B, R) trivial — observable
latency. Causal admissibility is not established for π_B. Extending Π
with a meso-observable that preserves the relevant dimension can restore
admissibility.

### 4.2 Instability under high-dimensional coupling

When many modes are simultaneously active (complex or chaotic regimes),
the coupling field L_{B,A} may fluctuate rapidly across B. σ_Δ(L_{B,A})
exceeds ε_coupling — condition (iii) fails. No stable causal assignment
can be made. This is not a fundamental absence of causal structure; it
is a failure of the chosen observable pair to sustain a stable causal
description in this region of B.

**Diagnosis:** σ_Δ(L_{B,A}) ≥ ε_coupling in R. Causal admissibility is
inadmissible at this resolution. Reducing Δ, increasing ε, or extending
Π with observables that decorrelate the active modes may restore it.

### 4.3 Inadmissible observable choice

If the observable family Π does not contain an observable that resolves
the causally relevant dimension of B, L_{B,A} appears to vanish even
though the underlying structure exists. This is a scope mismatch — the
same failure mode as in Section 4.1 but arising from omission rather
than aggregation.

**Diagnosis:** Adding a new observable π' to Π that resolves the relevant
dimension restores L_{B,π'} > 0. The original absence of loading was a
property of the scope, not of the system.

### 4.4 Inadmissibility of time as ordering dimension

When the system does not have a stable temporal trajectory — or when the
chosen time-averaged observables lose their substrate validity (A6 fails)
— classical cause-effect assignment in the temporal sense breaks down.

Within the ARW framework, this is not a special case. It is simply the
condition under which time-as-observable fails its admissibility criterion:
the time-ordered cover C_ε(π_time, B) collapses or becomes trivial.
When this happens, causal descriptions that rely on temporal ordering
become inadmissible — and must be replaced by descriptions based on the
remaining stable cover structure over B.

---

## 5. Causality Without Time

The standard formulation of causality — A causes B because A precedes B
in time and A's occurrence raises the probability of B — requires time
as a primitive ordering structure.

Within ARW, time is one observable among many (see
`docs/glossary/scope_extended_definition.md`, Section 3). For systems
where temporal trajectories are the natural substrate, time-ordered
causal descriptions are admissible and useful. For systems where they
are not — or where time-averaged observables are inadmissible — the
ARW formulation replaces temporal ordering with cover-geometric ordering:

> A is causally relevant for B in scope S if the cover structure of
> π_A over B is directed toward the cover structure of π_B —
> that is, if L_{B,A} >> L_{A,B} and both are Δ-stable.

This is not a generalisation of causality to "something broader". It
is a restriction of the concept to the conditions under which a stable
causal description actually exists — and a recognition that those
conditions do not necessarily include time.

---

## 6. Scope-Relativity of Causality

The causal admissibility conditions in Section 2.3 are all scope-relative:

- L_{B,A} depends on which observables are in Π
- σ_Δ(L_{B,A}) depends on which perturbations are in Δ
- The threshold ε_coupling depends on the working ε

**Consequence:** Two scopes S and S' over the same system and the same B
but with different (Π, Δ, ε) may disagree on causal admissibility. This
is not a contradiction — it is the expected behaviour of a description-
relative concept. The question "does A cause B?" without specifying a
scope is underspecified in the same way that "does this regime exist?"
is underspecified without a scope.

**This is not relativism about causality.** Within a given scope, the
causal admissibility conditions are precise and empirically testable:
L_{B,A} can be measured, σ_Δ(L_{B,A}) can be computed, and the
asymmetry condition can be checked. The scope-relativity is a feature
of the description framework, not a claim that causality is arbitrary.

---

## 7. Summary Table

| Concept | Classical formulation | ARW formulation |
|---|---|---|
| Causal relation | A precedes B and raises P(B) | L_{B,A} >> L_{A,B}, Δ-stable |
| Causal direction | Temporal precedence | Asymmetry of loading matrix |
| Causal breakdown | Correlation ≠ causation | Admissibility conditions (i–iii) fail |
| Causal scope | Implicit (often universal) | Explicit: scope S = (B, Π, Δ, ε) |
| Time | Ordering primitive | One observable among many; admissible when A6 holds |
| Causality absent | System is non-causal | Scope lacks stable directed coupling |

---

## 8. Open Questions

**Q-CAUSAL-01 (open):** The loading matrix L_{B,A} = |∂π_B/∂π_A| is
defined pointwise over B. For a multi-observable scope, the full loading
tensor L ∈ ℝ^{k×k} (k = |Π|) characterises all pairwise directed
couplings simultaneously. What is the formal relationship between the
eigenstructure of L and the cover partition structure of the observable
family? In particular: do dominant eigenvectors of L correspond to the
directions of strongest cover anisotropy in B?

**Q-CAUSAL-02 (open):** The stability condition σ_Δ(L_{B,A}) < ε_coupling
requires a resolution threshold ε_coupling for the coupling field itself.
How should ε_coupling be chosen relative to the working ε of the scope?
Is there a natural normalisation that makes the coupling admissibility
condition dimensionless and comparable across scopes?
