---
status: hypothesis
layer: docs/notes/
related:
  - docs/advanced/bc_extraction_method.md
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/cross_domain_signature_matrix.md
  - cases/CASE-20260315-0005/
  - cases/CASE-20260315-0009/
  - docs/notes/social_bc_extraction_method.md
---

# Aggregated Boundary Condition Structures

## Motivation

Many real systems are not governed by a single boundary condition (BC),
but by **multiple interacting BCs** that jointly determine regime structure.

In earlier ARW cases (e.g. Kuramoto or Littman-Metcalf), a **single dominant
BC** could be identified and directly mapped to an operator signature. The
BCManifest records exactly one primary BC class, with others listed as secondary.

However, this primary/secondary distinction already implicitly assumes an
aggregation: the primary BC dominates, the secondary BCs co-exist. The question
this document addresses is: **what are the structural types of co-existence,
and can they be expressed in terms of the ARW primitive basis?**

This is an ARW-level question (about operator structure) with ART-level
evidence (from existing cases). Both levels are kept explicitly separate below.

---

## ARW Level — Formal Framework

*This section contains domain-neutral ARW claims about operator structure.
Statements here must hold independently of any specific domain.*

### Definition

An **Aggregated BC Structure (BCₐ)** is a boundary-condition configuration
whose regime effects arise from the **interaction of multiple primitive BC
classes** rather than from a single BC.

The aggregation is expressed using operators from the ARW primitive basis:

| Aggregation type | Operator form | Primitive used |
|---|---|---|
| Sequential | `BC_n ∘ BC_{n-1} ∘ ... ∘ BC_1` | Composition `∘` |
| Parallel (additive) | `BC_1 × BC_2` on joint state | Product `×` |
| Hierarchical | `BC_macro ∘ π ∘ BC_micro` | Composition + Projection |
| Emergent | `π(BC_micro^N)` as N → ∞ | Projection (limit) |
| Competitive | `argdom{BC_1, BC_2}` under θ-sweep | Not a primitive — see note |

**Note on Competitive Aggregation and `argdom`:**
The Competitive type — where two BCs compete and one dominates above a
threshold θ* — is already present in the existing cases (CASE-0005, CASE-0009)
but cannot be expressed as a finite combination of `∘`, `×`, `π` alone.
The dominance crossover at θ* is an emergent property of the competition,
not a primitive composition. `argdom` is therefore a **candidate new primitive**
or a limit-operation (analogous to the asymptotic S4 → S1 relationship).
This is an open question — Q-AGG-01 below.

### Relation to Primitive Signatures

Primitive BC signatures from `operator_signature_catalog.md`:

| Signature | Structure |
|---|---|
| S1 | Projection / selection: `p ∘ p = p` |
| S2 | Product ∘ Composition: `X₁ × X₂`, cross terms |
| S3 | Time-coupled product: `X × T` |
| S4 | Scaling ∘ Composition: contraction |
| S5 | Conditional expectation: `E[·\|G]` |

Aggregated BC structures describe **how these primitive signatures combine**
via the ARW primitive operators. The five aggregation types are not new
primitives — they are structured compositions of the existing ones, except
where explicitly noted (Competitive).

### Operator-Level Representations

**Sequential:**
```
BC_total = S4 ∘ S2 ∘ S1
```
Each BC applies to the output of the previous one. The regime structure
is determined by the full chain, not by any single component.

**Parallel (joint state):**
```
X_joint = X₁ × X₂,   F = (S1(x₁), S2(x₁, x₂))
```
Multiple BCs act simultaneously on a product state. The regime is jointly
determined — neither BC alone produces the observed partition.

**Hierarchical:**
```
BC_macro ∘ π ∘ BC_micro
```
A projection (S1) separates the micro and macro levels. The macro BC
constrains the projected state; the micro BC constrains the pre-image.

**Emergent:**
```
lim_{N→∞} π(BC_micro^N) → BC_macro
```
Analogous to the S4 → S1 asymptotic relationship (Q-DISS-01): a macro-level
BC emerges from a large number of micro-level BC interactions in the limit.
Not a finite composition — a limit operation.

**Competitive:**
```
γ < γ*: S2 dominant → Coupling regime
γ > γ*: S4 dominant → Dissipation regime
```
The regime is determined by which BC has larger effect at the current
parameter value. θ* is the crossover — not a bifurcation in the classical
sense but a dominance inversion. `argdom` is not yet formally defined
as a primitive. → Q-AGG-01.

---

## ART Level — Evidence from Existing Cases

*This section contains ART-level instantiations — concrete system examples
from the repo. Statements here are evidence for the ARW hypotheses above,
not extensions of the formal framework.*

### Competitive Aggregation — CASE-20260315-0005

**System:** Multi-Link-Pendel with joint damping (γ-sweep)

```
BC_1: Coupling (S2, κ=3.25 fixed, above transition)
BC_2: Dissipation (S4, γ swept 0→5)
Aggregation type: Competitive
Dominance crossover: γ* where S4 overcomes S2 energy injection
Observable signature: var_rel decays from high (S2-dominated) to low (S4-dominated)
```

This case was designed to probe S4 vs S2 competition directly. The BCManifest
already records this as primary/secondary competition. Aggregation taxonomy
provides the formal label: **Competitive Aggregation (S4 vs S2)**.

### Competitive Aggregation — CASE-20260315-0009

**System:** Stochastic Kuramoto (σ-sweep)

```
BC_1: Coupling (S2, κ=2.0 fixed, above deterministic threshold)
BC_2: Stochastic BC (S5, σ swept 0→3)
Aggregation type: Competitive
Dominance crossover: σ_c where S5 overcomes S2 synchronization
Observable signature: r_mean decays from r_ss (S2-dominated) to 0 (S5-dominated)
```

Structurally identical to CASE-0005 in aggregation type — both are S_i vs S2
competitive cases. The parallel structure of CASE-0005 (S4 vs S2) and CASE-0009
(S5 vs S2) suggests a general pattern: **Coupling (S2) as the baseline BC that
other BCs compete against**.

### Sequential Aggregation — Social Shame Scenario

**System:** CASE-20260315-SOC1 (exploratory, pipeline-blocked)

```
BC chain: S1 (norm restriction) → S2 (observer activation) → S4 (reputation decay)
Aggregation type: Sequential
Causal structure: norm violation activates observer network activates reputation update
Operator form: S4 ∘ S2 ∘ S1
```

The shame scenario is a Sequential Aggregation. Each BC in the chain
activates the next — the regime is not determined by any single BC but by
the full causal sequence. This is why the Shame case resisted a single
primary BC assignment in the Pre-Screening (Blocker B.2): it is genuinely
sequential, not competitive.

### Parallel Aggregation — Littman-Metcalf Laser

**System:** BC extraction from `isodisperse_methode_v6_sweetspot.docx`

```
BC_1: Restriction (S1, β-admissibility constraint on α, g)
BC_2: Coupling (S2, OWL = f(λ, a, b) with cross terms)
BC_3: Forcing (S3, grating equation λ → β(λ) as exogenous index)
Aggregation type: Parallel
Structure: all three BCs act simultaneously on the same state space
Primary BC: Coupling (S2 — the ΔN=0 condition operates on the coupling)
```

In Littman-Metcalf, the three BCs co-exist without causal ordering — all
three are structurally present for all λ in the sweep. This is Parallel
Aggregation: `S_total = S1 × S2 × S3` on the joint design space.

---

## Methodological Strategy

The BC Extraction Method (`bc_extraction_method.md`) handles single-BC cases
through Pre-Screening and Formalization. Aggregated BC structures require an
additional stage:

### Stage 1 — Primitive BC Identification (existing method)

```
qualitative observation → BC candidate set → operator signatures (S1–S5)
```

### Stage 2 — Aggregation Structure Detection (new)

For each BC candidate set with more than one entry, determine the
aggregation type using the following decision criteria:

| Question | If yes → |
|---|---|
| Do the BCs activate in a fixed causal order? | Sequential |
| Do the BCs act simultaneously on a product state? | Parallel |
| Does one BC govern multiple lower-level BCs? | Hierarchical |
| Does a macro-BC emerge from many micro-BC interactions? | Emergent |
| Does one BC dominate the other above a parameter threshold? | Competitive |

### Stage 3 — Primary BC Selection

For pipeline formalization (`CASE_TEMPLATE_signature_first.md`), a single
primary BC must be identified. The aggregation type determines the selection
strategy:

| Aggregation type | Primary BC selection strategy |
|---|---|
| Competitive | BC that dominates in the swept regime (determined by sweep direction) |
| Sequential | First BC in the causal chain (the trigger) or the BC at the observed transition |
| Parallel | BC whose signature is most directly modulated by the control parameter θ |
| Hierarchical | Macro-level BC |
| Emergent | Macro-level emergent BC (if identifiable); else Exploration-only |

### Stage 4 — Minimal Model Construction

Build the smallest dynamical model that captures the aggregation structure —
not all BCs, only those necessary for the observed regime transition.

---

## Open Questions

| ID | Question | Status | Implication |
|---|---|---|---|
| Q-AGG-01 | Is Competitive Aggregation (`argdom`) expressible as a finite combination of `∘`, `×`, `π`, or does it require a new primitive? | open | If new primitive needed: extends ARW operator basis |
| Q-AGG-02 | Does the aggregation type affect transfer metrics? Specifically: do two Competitive-Aggregation cases transfer better to each other than to Sequential cases, controlling for BC class? | open | Would require transfer comparison across CASE-0005, CASE-0009, and a Sequential case |
| Q-AGG-03 | Is there a canonical ordering of BCs in Sequential Aggregation across domains, or is the ordering domain-specific? | open | If canonical: suggests a universal causal grammar of BC activation |
| Q-AGG-04 | CASE-0005 (S4 vs S2) and CASE-0009 (S5 vs S2) are both S2-competitive. Is S2 (Coupling) structurally privileged as the "default BC" that other BCs compete against? | open | Would suggest a BC hierarchy in the ARW framework |

---

## Relation to Existing Repo Artifacts

| Artifact | Relation |
|---|---|
| `operator_signature_catalog.md` | Provides the primitive signatures S1–S5 that are inputs to aggregation |
| `bc_extraction_method.md` | Stage 1 of this method; Stages 2–4 are extensions |
| `cross_domain_signature_matrix.md` | Provides domain instantiations of each signature — also of aggregated forms |
| CASE-20260315-0005 | Empirical instance of Competitive Aggregation (S4 vs S2) |
| CASE-20260315-0009 | Empirical instance of Competitive Aggregation (S5 vs S2) |
| CASE-20260315-SOC1 | Empirical instance of Sequential Aggregation (S1 → S2 → S4); pipeline-blocked |
| `bc_extraction_littman_metcalf.md` | Empirical instance of Parallel Aggregation (S1 + S2 + S3) |

---

*Revised from: aggregated_bc_structures.md (uploaded 2026-03-15)*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
