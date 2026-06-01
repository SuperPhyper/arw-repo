---
status: working-definition
layer: docs/advanced/
last_updated: 2026-05-30
depends_on:
  - docs/advanced/observable_space_cover_height.md
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/advanced/bc_stratification_dynamic_subscopes.md
  - docs/art_instantiations/generator_admissibility_taxonomy.md
related:
  - docs/bc_taxonomy/transfer_distortion_metrics.md
open_questions:
  - Is η_i intrinsic to the generator or observer-dependent? (→ Q-SIG-02)
  - Monotonicity assumption for persistence intervals (→ Q-SIG-03)
  - Restriction as meta-BC: does it enter the persistence measure or define its domain? (→ Q-SIG-04)
  - Projection loss: what transfer claims are lost when Σ is read only in projected space? (→ Q-SIG-05)
---

# BC Signature Persistence and Dominance

## Overview

This document formalises the **generator signature** Σ as a persistence measure
over BC configurations. It replaces the earlier informal use of Σ as "the set of
active BC classes" with a structure that captures not only which classes are present
but how robustly they organise the regime across resolution scales.

The construction mirrors the observable-space cover height method
(`observable_space_cover_height.md`): just as cover height integrates over all ε
simultaneously to give a scale-free stability measure per BC-space point,
BC signature persistence integrates over the characteristic scale parameter η
to give a robustness measure per BC configuration — including joint multi-BC
configurations.

### What is being aggregated

BC classes are not directly measurable. What η-variation exposes is the
**operator signature** (S1–S5, `bc_operator_signatures_arw.md`) — the
mathematical footprint through which an abstract BC-bedrock relation becomes
legible at the system level. Observables carry signatures of their underlying
BCs, but these signatures are *projections*: a mapping from abstract BC bedrock
(fundamental relational types) into the system-readable BC classes as they appear
in a concrete generator.

The persistence measure therefore operates in **projected space**: it tracks
how robustly an operator signature remains dominant as η varies. BC-class
persistence is derived from operator-signature persistence, not directly from
the abstract bedrock relations.

This projection is not lossless. Two generators may share the same Σ in
projected space while differing at the bedrock level, or vice versa. Transfer
claims grounded in Σ are therefore claims about structural similarity in
projected space — they do not guarantee equivalence at the bedrock level.
What transfer claims are lost at the projection boundary is an open question
(→ Q-SIG-05).

---

## 1. Notation

| Symbol | Meaning |
|---|---|
| G = (Λ, Σ, φ, C) | Generator (as defined in Part VI §6.2 / generator_admissibility_taxonomy.md) |
| BC | The set of active BC classes in G, BC ⊆ {Coupling, Restriction, Dissipation, Forcing, Symmetry Breaking, Aggregation} |
| η | Characteristic scale parameter — the resolution axis over which BC contributions are tracked. Distinct from ε (scope resolution threshold). |
| η_birth(σ) | Coarsest η at which BC configuration σ is non-trivially active |
| η_death(σ) | Finest η at which σ remains non-trivially active |
| p(σ) | Persistence of BC configuration σ = η_birth(σ) − η_death(σ) |
| Σ | The generator signature: the persistence measure p : 2^BC → ℝ≥0 |

**On η vs ε.** ε is a fixed threshold chosen by the observer to construct a scope.
η is a continuous axis over which BC contributions are tracked to compute
robustness — it is a meta-level parameter used to *define* Σ, not a parameter
that appears in any individual scope.

---

## 2. Individual BC Persistence

For a single BC class C_i ∈ BC, define its **persistence interval**:

```
I_i = [η_death,i , η_birth,i]
```

where η_birth,i is the coarsest resolution at which C_i's **operator signature**
(S1–S5) is non-trivially dominant in the regime partition R(π), and η_death,i
is the finest resolution at which C_i's signature still constitutes a distinct
structural contribution — before it becomes subsumed by finer-scale structure
or indistinguishable from noise.

The **individual persistence** is:

```
p({C_i}) = η_birth,i − η_death,i
```

**Interpretation.** A class with high p({C_i}) remains structurally relevant across
a wide range of resolutions — it is a robust feature of the regime architecture.
A class with low p({C_i}) is only visible in a narrow η-window: it may be a
transitional signal or an artefact of a particular observation scale.

---

## 3. Multi-BC Persistence

The individual persistence measure misses interaction effects between simultaneously
active BC classes. Two classes may each have high individual persistence while their
joint contribution is inconsistent — they conflict over the regime partition at
overlapping η-scales. Conversely, two classes may reinforce each other, producing
a joint structure more robust than either alone.

Following the multi-observable extension in `epsilon_and_scope_resolution.md`,
the persistence measure is generalised to all subsets σ ⊆ BC.

For a configuration σ = {C_{i1}, ..., C_{ik}}, define:

```
I(σ) = the η-interval over which all classes in σ are simultaneously
         non-trivially active AND their joint contribution to R(π) is
         structurally coherent (non-conflicting)
```

The **multi-BC persistence** is:

```
p(σ) = |I(σ)|
```

**Boundary conditions on p:**

- p(∅) = 0 by convention
- p({C_i}) = individual persistence as above
- p(σ) ≤ min_{C_i ∈ σ} p({C_i})  — joint persistence cannot exceed the minimum individual persistence
- p(σ) = 0 if the classes in σ are structurally conflicting throughout their
  overlap region (masking without coherent joint structure)

**Relation to Part V masking.** Multi-BC masking (Part V §5.3) corresponds to
p(σ) < min p({C_i}): the joint persistence is shorter than the individual
persistences because conflict suppresses one class's visibility within the
overlap region. The persistence measure makes this quantitative.

---

## 4. The Generator Signature Σ

The **generator signature** is the full persistence measure:

```
Σ : 2^BC → ℝ≥0,    σ ↦ p(σ)
```

Σ is a monotone submodular function on the power set of active BC classes:
p(σ ∪ τ) + p(σ ∩ τ) ≤ p(σ) + p(τ) in the conflicting case, with equality
when classes are structurally independent.

**What Σ encodes:**

1. **Presence**: which classes are active — {C_i : p({C_i}) > 0}
2. **Individual robustness**: how persistently each class organises the regime
3. **Interaction structure**: whether joint configurations are coherent, reinforcing,
   or conflicting — encoded in the gap between p(σ) and min p({C_i} : C_i ∈ σ)

The earlier informal definition "Σ = set of active BC classes" is recovered as the
support of Σ: supp(Σ) = {C_i : p({C_i}) > 0}. Σ extends this with the full
interaction structure.

---

## 5. Dominance

The **dominance order** on BC is induced by individual persistence:

```
C_i ≻ C_j  iff  p({C_i}) > p({C_j})
```

The **dominant configuration** of G is argmax_{σ} p(σ) — the multi-BC combination
with the highest joint persistence.

**Note on Restriction.** If Restriction is a meta-relation (admissibility condition
on all other relation types — see `bc_bedrock_working_definition.md` §3), its
dominance is of a different logical type: it does not enter the dominance ordering
alongside the other classes but defines the η-domain within which the other classes
can be active. In that case, p(Restriction) is not comparable to p(Coupling) etc.
but is instead the η-extent of the admissible region for G as a whole.
This remains an open question (→ Q-SIG-04).

---

## 6. Transfer Compatibility via Σ

Two generators G and G' have **compatible signatures** to degree d if:

```
d(Σ, Σ') = 1 − (1/Z) Σ_{σ ⊆ BC ∩ BC'} |p(σ) − p'(σ)| / max(p(σ), p'(σ))
```

where BC ∩ BC' is the set of shared active BC classes and Z normalises over
all non-empty subsets of BC ∩ BC'.

d = 1: perfect signature match — same persistence profile over all shared
BC configurations. d = 0: no shared structure in persistence.

**Relation to the old transfer metrics.** RCD, TBS_norm, PCI, SDI
(transfer_distortion_metrics.md) measure partition-level consequences of Σ.
They remain valid for same-system scope reductions. For cross-system transfer,
d(Σ, Σ') is the appropriate prior; partition-level metrics serve as downstream
confirmation when a state-space correspondence is available.

---

## 7. Open Questions

**Q-SIG-02 — Intrinsicness of η_i.** Is the persistence interval I_i an intrinsic
property of C_i in G, or does it depend on the full constellation of active classes?
If I_i shifts when other classes are added to BC, then individual persistence is
not well-defined independently of the generator context.

**Q-SIG-03 — Monotonicity.** The construction assumes that each BC class has a
contiguous activity interval [η_death,i, η_birth,i]. In Multi-BC generators with
strong interactions, a class could be active at coarse η, suppressed at intermediate
η by another class, and re-emerge at fine η. This would produce a non-contiguous
"barcode" rather than a single interval. Whether this occurs, and how to handle it,
is open.

**Q-SIG-05 — Projection loss.** Σ is defined in projected space (operator
signatures → system-readable BC classes). Bedrock-level structure that does
not produce a distinct operator signature at any η scale is invisible to Σ.
It is open whether this is a fundamental limit or an artefact of the current
operator vocabulary (S1–S5). If S1–S5 are not exhaustive at the bedrock level,
Σ-based transfer claims may miss structural kinship that a bedrock-level
comparison would reveal.

**Q-SIG-04 — Restriction as meta-BC.** If Restriction is formally an admissibility
operator on the other five relation types (see bc_bedrock_working_definition.md),
it does not belong in the same persistence lattice. The architecture of Σ would
then be two-layered: Restriction defines the admissible η-domain; the other five
classes are measured within that domain.

---

*Connected to: Part VI §6.2–6.3 (book draft), Part VII §V4 (formal transfer metrics).*
*Supersedes the informal Σ usage in generator_admissibility_taxonomy.md §2.*
*For bottom-up extraction of Σ from observable data: `bc_signature_extraction_observables.md`.*
