---
status: hypothesis
layer: docs/bc_taxonomy/
created: 2026-05-30
depends_on:
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/notes/bc_bedrock_working_definition.md
  - docs/core/bc_classes_and_regime_generation.md
  - docs/glossary/scope.md
open_questions:
  - Q-REL-01
  - Q-REL-02
  - Q-REL-03
---

# BC Classes as Relation Types: Structural Analysis

*Formal companion to `bc_bedrock_working_definition.md`.*
*Informs Part IX §9.1 of the ARW monograph.*

---

## 1. The Core Claim

The BC-Bedrock establishes that the six BC classes are six ways descriptions
can organize stable distinguishability. This document refines that claim:

**Five of the six BC classes are relation types** — each organizes
distinguishability across a different relational domain. The sixth class
(Restriction) has a different status: it is the admissibility condition
for each of the five relation types, not a relation of the same kind.

This gives the taxonomy a **5 + 1 structure**:

| BC class | Relation domain | What it organizes |
|---|---|---|
| **Coupling** | Component × Component | Distinguishability between contemporaneous components |
| **Dissipation** | State × Time | Distinguishability across temporal continuation |
| **Forcing** | Regime × Regime | Distinguishability between regime organizations |
| **Symmetry Breaking** | State × State (equivalent) | Distinguishability between previously equivalent states |
| **Aggregation** | Description_level × Description_level | Distinguishability between description resolutions |
| **Restriction** | *(meta)* | Admissibility of each of the above relations |

---

## 2. The Five Relation Types

### 2.1 Coupling — Component Relations

**Formal characterization:**
A coupling BC defines a relation R_C ⊆ X × X on the state space, such
that the distinguishability of component x_i depends on the state of
other components x_j.

```
d_C(x_i) = f(x_i, {x_j : (x_i, x_j) ∈ R_C})
```

Stable distinguishability under coupling requires the relation R_C to be
coherent: the joint state must produce stable mutual distinctions that no
individual component produces alone.

**Failure characterization:**
- **Dissolution**: R_C weakens below the coupling threshold — components
  become mutually independent, collective distinguishability collapses
- **Freezing**: R_C becomes rigid — the relation locks components into
  a fixed joint configuration, eliminating individual distinguishability

**Connection to BC-Bedrock:**
Coupling organizes distinguishability *between* components at the same
time slice. The collective mode is a stable distinction that only the
relation, not its terms, can sustain.

---

### 2.2 Dissipation — Ordered-Continuation Relations

**The primitive distinction from Coupling:**
Coupling organizes distinguishability across *unordered* relations between
freedoms: R_C ⊆ X × X requires no ordering structure on X. The relation
between x_i and x_j exists without a past/future structure.

Dissipation organizes distinguishability across *ordered continuations*:
R_D ⊆ X × X_≤ where (X, ≤) carries an ordering relation. Without ≤,
there is no dissipation — there is only coupling. The ordering is what
distinguishes the two classes at the most primitive level.

Time is the most common ordering, but not the only one. The same structure
applies to developmental stages, learning sequences, organisational histories,
evolutionary lineages — any domain where an ordering relation makes
"continuation" a well-defined concept.

**Formal characterization:**

```
R_D ⊆ X × X_≤     where X_≤ = (X, ≤) is an ordered state space

Attractor(R_D) := { x ∈ X : d(x, x') is preserved for x' ≻ x along ≤ }
Repulsor(R_D)  := { x ∈ X : d(x, x') → 0 for x' ≻ x along ≤ }
```

An attractor is "a region where distinguishability is sustained along the
ordering." A repulsor is "a region where distinguishability cannot be
maintained along the ordering." Attractors, repulsors, hysteresis, and
path-dependence are *secondary* phenomena — they arise once an ordering
exists, but they are not the primitive definition.

This formulation connects Dissipation directly to the BC-Bedrock primitive:
the question is whether distinctions survive ordered continuation — not
specifically temporal continuation, but continuation along any ≤.

**The Coupling-Dissipation relationship clarified:**
Dissipation is not "Coupling + Time" but "Coupling + Ordering Relation."
The additional primitive structure is the ordering ≤, not time per se.
This explains the asymmetry in their epistemic parameters: Dissipation
has a natural C component τ because an ordering requires a scale parameter
(how far along ≤ to look); Coupling has no analogous parameter because
unordered relations have no continuation to parameterize. The "Coupling
gap" in epistemic context analysis is therefore structural, not a deficiency.

**Failure characterization:**
- **Weakening**: temporal distinguishability preservation decreases —
  basins flatten, attractors weaken, states wander across what were
  formerly stable distinctions → indistinguishability
- **Deepening**: temporal distinguishability preservation concentrates —
  basins deepen, the system locks into fewer regions of sustained
  distinction → discretization toward a single attractor

---

### 2.3 Forcing — Inter-Regime Relations

**Formal characterization:**
A forcing BC defines a relation R_F ⊆ Regime_A × Regime_B such that
the organizational structure of Regime A (its B_A, Π_A, Δ_A, ε_A)
constrains what distinctions are admissibly producible in Regime B.

```
Adm_F(Regime_B | Regime_A) = f(R_F(A, B), B_B, Π_B)
```

The forcing BC is specifically **directional**: A organizes B, not
symmetrically. This distinguishes Forcing from Coupling (symmetric
component relations) by the asymmetry of the inter-regime relation.

**Critical distinction from Coupling:**
- Coupling: components interact symmetrically within one regime
- Forcing: one regime's structure constrains another regime's admissibility

**Failure characterization:**
- **Decoupling**: R_F weakens → Regime B reverts to autonomous structure;
  distinctions that depended on A's organizational reach dissolve
- **Absorption**: R_F overwhelms → Regime B's organizational autonomy
  is subsumed into Regime A's structure; two regimes collapse to one
  (asymmetrically: A's structure survives, B's does not)

**Generalization beyond frequency/rhythm:**
The inter-regime relation covers:
- Temporal forcing (external rhythm imposing on internal rhythm) —
  a special case where R_F relates by frequency ratio
- Governance forcing (institutional regime organizing operational regime)
- Normative forcing (cultural regime constraining epistemic regime)
All are instances of the same structural condition: an inter-regime
relation where one regime's organizational structure determines what
the other regime can admissibly distinguish.

---

### 2.4 Symmetry Breaking — Equivalent-State Relations

**Formal characterization:**
A symmetry breaking BC acts on a relation R_SB ⊆ X × X where (x, y) ∈ R_SB
means x and y are equivalent under the symmetry group G. Before breaking,
no distinctions within the equivalence class are stable. After breaking,
one element of the class is selected, and the equivalence relation
R_SB is broken: x and y become distinguishable.

```
Before break: d(x, y) = 0  for all (x, y) ∈ R_SB
After break:  d(x, y) > 0  for (x, y) in the broken class
```

**What makes this a distinct class:**
The breaking event creates hysteresis: the newly created distinction
is asymmetric in cost — reaching the unselected branch requires crossing
a boundary that did not exist before the break. The relation R_SB is
not restored by removing the breaking perturbation.

**Failure characterization:**
- **Forward break**: symmetry breaks, topology changes, hysteresis created;
  approached by increasing fluctuations as the bifurcation nears (Z_shared
  at the bifurcation itself)
- **Restoration approach**: the broken state approaches a restoration
  bifurcation; the hysteresis narrows; secondary structures may redirect
  restoration toward a second-order break rather than symmetry recovery

---

### 2.5 Aggregation — Description-Level Relations

**Formal characterization:**
An aggregation BC defines a relation R_A ⊆ D_fine × D_coarse between
description levels, such that the coarse-grained description D_coarse
is derived from D_fine by suppressing distinctions below the aggregation
grain N.

```
D_coarse = A_N(D_fine)   where A_N suppresses within-group distinctions
```

The admissibility of D_coarse as a valid description of the phenomena
depends on the coherence of D_fine at grain N (the N* condition).

**What makes this a distinct class:**
Aggregation is a condition on the description, not on the system. The
same physical process produces different regime structures under different
aggregation grains — and both are valid within their respective scopes.

**Failure characterization:**
- **N* failure**: fine-level heterogeneity exceeds what the coarse
  description can coherently represent → F0 (aggregate incoherent)
- **Grain too coarse**: the aggregation relation maps over distinctions
  that the question requires to be visible → F1 (insufficient resolution)

---

## 3. Restriction as Meta-Relation

### 3.1 The Structural Claim

Restriction does not define a relation of the same type as the five above.
Instead, for each relation type τ, Restriction is the operator that produces
the **admissibility boundary set** of R_τ:

```
Θ(R_τ) = { θ* ∈ P : R_τ changes its admissibility regime at θ* }
```

For parameters below θ*(τ): R_τ organizes stable distinguishability.
At θ*(τ): R_τ can no longer sustain that organization — this is the
regime boundary, identifiable in the scope tuple as θ* (Part II).
Above θ*(τ): R_τ is structurally inoperable.

**Restriction = Θ**: not a relation itself, but the operator that maps
each relation type to its critical parameter set.

**Critical parameter values per relation type:**

| Relation type | Critical parameter θ* | What changes at θ* |
|---|---|---|
| Coupling | κ_c | below: no collective mode; above: collective mode exists |
| Dissipation | τ* (memory horizon) | below: past organizes present; beyond: past loses organizing influence |
| Forcing | ρ* (compatibility threshold) | below: inter-regime coupling cannot be stably maintained |
| Symmetry Breaking | λ_c (bifurcation value) | at λ_c: equivalence class loses stability; two branches emerge |
| Aggregation | N* | above N*: aggregate no longer computes a coherent quantity |

The primitive objects are therefore the pairs **(R_τ, Θ(R_τ))** — not six
separate BC classes. The five relation types describe the organizing structure.
Restriction describes the boundaries of that organization.

**Die Relation erzeugt Regime. Restriction erzeugt deren Rand.**
(*The relation generates regimes. Restriction generates their boundaries.*)

### 3.2 Restriction as Boundary Operator, Not Sixth Relation

This sharpens the earlier characterization. Restriction is:

- Not "another relation" alongside the five
- Not merely "a condition for relations"
- But the **operator Θ that maps each relation type to its critical boundary set**

This explains three observations simultaneously:
1. Why Restriction is structurally different from the other five (it operates on relation types, not on state space)
2. Why it is indispensable (without Θ(R_τ), R_τ has no defined validity domain)
3. Why failure signatures are tightly coupled to Restriction: every failure is a crossing of θ*(τ) for some τ — F0, F-gradient, and Z_shared describe the observable behavior AT θ*(τ) for different relation types

### 3.3 Connection to the Scope Tuple's θ*

The regime boundary θ* introduced in Part II of the monograph (the
scope-dependent transition point) is now formally grounded:

```
θ* = the critical parameter value in Θ(R_τ) for whatever relation type τ
     is organizing the current regime
```

Every θ* that appears in a scope analysis is a Restriction boundary for
some R_τ. The failure mode taxonomy (F0, F-gradient, Z_shared) describes
what happens at θ* for each relation type's characteristic behavior.

This is why Restriction appears in every multi-BC analysis: any combination
of the other five classes has an implicit Restriction component that
determines where the combined relation is admissible.

### 3.3 Projection as Special Case

The "projection onto a lower-dimensional subspace" formulation of
Restriction (used in the monograph for accessibility) is a special
case of the meta-condition: the projection defines the admissible
subspace explicitly as a geometric subspace. The general case is
any admissibility condition — parametric, energetic, informational,
topological — that defines the boundary of stable distinctions.

---

## 4. The 5 + 1 Structure and Completeness

### 4.1 The Question

If the five relation types (Component, Temporal, Inter-Regime, Equivalent-State,
Description-Level) are the fundamental domains over which distinguishability
can be organized, and Restriction is the meta-condition on each, then:

**Are these five domains exhaustive?**

Stated as a falsification criterion: to add a seventh BC class, one would
need to identify a relation domain not reducible to one of the five, plus
an associated admissibility condition. The burden of proof is on the
new domain.

### 4.2 Candidate Relation Domains

The following table surveys the candidate domains to check exhaustiveness:

| Candidate | Covered by |
|---|---|
| Spatial relations between components | Coupling |
| Temporal relations (memory, history) | Dissipation |
| Cross-level relations (macro/micro) | Aggregation |
| Inter-regime relations | Forcing |
| Degeneracy relations (equivalent states) | Symmetry Breaking |
| Topological relations (connectivity, boundary) | Restriction (meta) |
| Probabilistic relations | → reducible to Aggregation + Restriction |
| Information-theoretic relations | → reducible to Aggregation |

No candidate has been identified that is irreducible to the existing five.
This is not a proof of completeness but a consistency check.

### 4.3 The Dissipation-Coupling Duality

Dissipation (temporal coupling) and Coupling (spatial/component coupling)
are structurally related: both are relations between elements of the
system, differing only in the relation domain (time vs. space). This
suggests a possible deeper unification:

- Coupling = self-relation of system at equal times
- Dissipation = self-relation of system across time

If these are two instances of the same relation type over different
domains, the taxonomy might reduce further to:
- **Self-relation** (two modes: spatial and temporal)
- **Inter-regime relation**
- **Equivalent-state relation**
- **Description-level relation**
- **Admissibility meta-condition**

Whether this further reduction is valid or whether Coupling and Dissipation
are genuinely distinct is an open question (Q-REL-01).

---

## 5. Open Questions

**Q-REL-01:** Are Coupling and Dissipation instances of the same relation
type (self-relation of a system) over different domains (spatial/temporal),
or are they genuinely distinct in a way that resists unification?

*Formal test:* Can the failure signatures of both be derived from a single
formal structure with domain as parameter? If yes, the taxonomy may reduce
from 5+1 to 4+1.

**Q-REL-02:** Can Restriction be formally expressed as a functor or natural
transformation over the other five relation types in a categorical framework?

*Informal version:* Is there a universal "boundary operator" ∂ such that
Adm(R_τ) = ∂(R_τ) for each relation type τ?

**Q-REL-03:** Does the 5+1 structure ground a formal derivation of the
taxonomy from a primitive set? Specifically: given the BC-Bedrock claim
(stable distinguishability as the primitive object), can the five relation
types be *derived* as the exhaustive set of structurally irreducible
ways to organize distinguishability across the available relational domains?

*Blocking condition:* To answer yes, one would need a formal theory of
relational domains (component, temporal, inter-regime, equivalent-state,
description-level) and a proof that these are exhaustive. Neither currently
exists within ARW.

---

## 6. Implications

### For the Monograph

The 5+1 structure sharpens the answer to "why exactly six?" (Part III §3.1
and Part IX §9.1):
- Not: "the taxonomy is a well-supported empirical classification"
- But: "the taxonomy may have a structural derivation from five relation
  domains plus one admissibility meta-condition"

The key shift: from a working taxonomy that is *open to revision* to a
structured hypothesis about *what revision would require* (identifying a
sixth irreducible relation domain).

### For Part V (Failure Signatures)

The relational structure predicts failure mode structure:
- Each relation type has a failure mode that reflects the relation breaking
  (in two directions)
- Restriction failure changes the admissibility of the relation itself,
  which is why restriction failure is always present when any other BC
  class fails beyond its admissible range

### For the Generator Admissibility Taxonomy

The relational structure has direct implications for
`docs/art_instantiations/generator_admissibility_taxonomy.md`:

1. **Missing S6 signature**: Symmetry Breaking has no operator signature in
   S1-S5, causing Type II collapse to conflate bifurcation (Symmetry Breaking)
   with resonance (Forcing). A separate S6 would split Type II into Type II-a
   (Forcing incommensurability) and Type II-b (Symmetry Breaking bifurcation).

2. **A(G) as intersection of embedded Restrictions**: The formally admissible
   region of a generator is the intersection of all embedded Restriction
   conditions: A(G) = ∩_τ Adm(R_τ). Type I collapse = one Adm(R_τ) boundary
   crossed; Type III = multiple Adm(R_τ) mutually incompatible (K ≠ ∅).

3. **C as epistemic Restriction**: The context tuple C = (O, Δ_C, ε_C, ρ, τ, σ, κ)
   is the epistemic-level instantiation of the Restriction meta-relation. The
   seven C components map onto the five embedded Restriction conditions plus two
   observational components. A_f(G | C) = A(G) ∩ Adm_Restriction(C).

### For Transfer (Part VI)

Transfer is specifically the question of when Forcing-type relations
(inter-regime relations in the general sense) can be validly established
between systems. The 5+1 structure suggests that Transfer validity is
determined by:
(a) Whether the BC class structures are analogous
(b) Whether the Restriction conditions (admissibility) are compatible
(c) Whether the failure mode profiles align

### For the Bedrock

The reformulation of Dissipation as temporal distinguishability connects
all six classes directly to the BC-Bedrock primitive:
- Coupling: stable distinguishability between components
- Dissipation: stable distinguishability over temporal continuation
- Forcing: stable distinguishability between regimes
- Symmetry Breaking: stable distinguishability between equivalent states
- Aggregation: stable distinguishability across description levels
- Restriction: the domain within which any of the above is admissible

---

## 7. Status and Promotion Conditions

This document is at **hypothesis** level.

Promotion to **working-definition** requires:
- At least one case study that operationalizes the Restriction-as-meta-relation
  claim (i.e., where restricting the admissible space of an inter-regime
  relation changes the forcing BC's failure signature predictably)
- Consistent derivation of failure signatures from the relational structure
  across at least two BC classes
- No contradictions with existing case records

Promotion to **definition** would require:
- Formal derivation of the 5+1 structure from the BC-Bedrock primitive
- Resolution of Q-REL-01 through Q-REL-03
- Review by at least one independent session
