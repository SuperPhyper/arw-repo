---
status: hypothesis
layer: docs/art_instantiations/
created: 2026-05-07
last_updated: 2026-05-07
depends_on:
  - docs/glossary/scope.md
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/advanced/observable_decomposition.md
  - docs/art_instantiations/epistemic_context_and_functional_admissibility.md
---

# Generator Admissibility Taxonomy

## Position in the ARW/ART Framework

ARW is a post-hoc observational instrument. It takes a system as given and asks:
under which parameter configurations do stable, describable regimes exist?

This document addresses a distinct but related question: many formal systems used
across physics, mathematics, and the social sciences are not descriptions of a
single regime structure — they are **generators** of admissible scope families.
A generator G does not specify a concrete scope S = (B, Π, Δ, ε). It specifies
a structural law from which concrete scopes can be instantiated under varying
parametrizations.

Examples of generators in this sense: Hamiltonians, Lagrangians, free energy
functionals, field equations, constitutional legal systems, market mechanism
formalisms.

ARW can observe generators as objects — analyzing the family of scopes they
produce and the geometry of admissibility loss across that family. ART can use
generator classification to predict where scope admissibility will fail before
a concrete scope is instantiated.

---

## Formal Definition of a Generator

A generator G is not an element of S = (B, Π, Δ, ε). It lives at a higher level:

> G → {S_i} : a parametrized family of scopes

where each S_i = (B_i, Π_i, Δ_i, ε_i) is a concrete ARW scope instantiated
under a specific parametrization of G.

### Formal Structure

> **G = (Λ, Σ, φ, C)**

| Component | Definition | Role |
|---|---|---|
| **Λ** | Parametrization space of G — the set of all contexts in which G can be instantiated | Topological space; not necessarily metric or continuous |
| **Σ = (P, D, K)** | Signature structure: P = present signatures ⊆ {S1–S5}, D ⊆ P = dominant, K ⊆ P×P = conflict relations | Determines collapse type |
| **φ: Λ → (B, Π)** | Partial instantiation map: G determines domain and observable class only | Preserves ARW/ART separation |
| **C** | Epistemic-operational context: the totality of epistemic resources under which description remains stable | Provided by ART; contains R as special case — see `epistemic_context_and_functional_admissibility.md` |

### Note on C replacing R

Earlier formulations used R: Λ → expected regime structure as the fourth
component. C is the correct generalization: R captures only domain-specific
prior knowledge (what the generator is expected to reproduce), while C captures
the full epistemic-operational conditions under which functional admissibility
can be assessed. R ⊂ C.

See `docs/art_instantiations/epistemic_context_and_functional_admissibility.md`
for the formal definition of C and its constituent criteria.

### The ARW/ART Separation

φ is a **partial** instantiation — not a full scope generation:

- **φ determines** B_λ (the parameter domain under λ) and Π_λ (the class of
  observables the generator structurally permits)
- **Observer determines** Δ (perturbation class) and ε (resolution threshold)

The full scope arises only through observer completion: S_i = (φ(λ), Δ, ε).

This preserves the core ARW principle: the observer remains sovereign over
perturbation class and resolution. G constrains but does not determine the scope.

ARW observes G without C — asking only whether scopes are formally admissible.
ART instantiates G with C — asking whether admissible scopes remain stable,
reproducible, and compression-viable under the operative context.

---

## Admissible Regions of G

### Formal admissible region

> **A(G)** = {λ ∈ Λ : ∃ (Δ, ε) such that S = (φ(λ), Δ, ε) is admissible}

This is the ARW-level assessment: no context required, only formal admissibility
conditions (cover non-trivial, Δ-stable, within I_ε).

### Functionally admissible region

> **A_f(G | C)** = {λ ∈ A(G) : S = (φ(λ), Δ_C, ε_C) is Δ-stable,
> reproducible, compression-viable, and resource-proportional under C}

A_f(G | C) is always relative to a context C. It is an ART-level concept.
The same λ may be in A_f under one C and outside A_f under another.

Functional admissibility is **not** a truth criterion. It is an epistemic
stability criterion: a scope is functionally admissible if its structure
remains stably reproducible under the relevant perturbations and resources
of C. Newton's mechanics is in A_f under all macroscopic C despite being
formally superseded — because it is compression-viable and Δ-stable in that
regime. String theory has a rich A(G) but a partially characterized A_f(G | C)
because the compression and reproducibility criteria are not met across most
realistic C.

### Hypothetically admissible region

> **A_h(G | C)** = A(G) \ A_f(G | C)

Formally admissible but not functionally admissible under C: the scope exists
in principle but fails one or more criteria of C (Δ-stability, reproducibility,
compression viability, resource proportionality, predictive closure, or
transfer stability).

### Inadmissible region

> Λ \ A(G): no admissible scope constructible under any (Δ, ε).

---

## Three Generator Admissibility Collapse Types

### Type I — Boundary Collapse

**Definition:** Admissibility is lost sharply at a boundary in Λ. The boundary
is structurally determined by G, independent of observable or resolution choice.

**Mechanism:** G encodes a phase structure. At phase boundaries, Z_shared
activates for all class-E observables simultaneously. No observable selection
or ε adjustment can recover admissibility.

**Topology of A(G):** Bounded by a sharp hypersurface ∂A(G) in Λ. May be
disconnected after symmetry breaking.

**A_f / A_h under C:** Sharp boundary between A_f and Λ \ A(G). A_h is
typically empty or confined to the boundary neighborhood. The boundary does
not depend on C — it is generator-structural.

**Characteristic signature:** Single dominant signature S1, S2, S4, or S5.
Collapse is ε-independent.

**Canonical examples:** Hamiltonians at phase transitions; free energy
functionals at changes in minimum structure; Ginzburg-Landau at T_c;
EFT at its cutoff boundary.

---

### Type II — Solution Space Collapse

**Definition:** Admissibility is lost not at a parameter boundary of G, but
in the solution structure of G. The generator remains well-defined; solutions
in a region of Λ are non-unique, degenerate, or singular.

**Mechanism:** G's structural law admits multiple or singular solutions in
certain regions. Scopes instantiated there cannot sustain stable partitions
because the underlying state space bifurcates or collapses.

**Topology of A(G):** Interior holes or singularities not captured by ∂A(G).
Collapse lies inside Λ, not at its boundary.

**A_f / A_h under C:** The A_f / A_h boundary is Type II's characteristic
feature under C — solutions may exist in A_h (different vacuum sectors, gauge
branches) but fail reproducibility or compression-viability criteria under
realistic C. Branch selection is a mechanism for moving λ from A_h into A_f.

**Characteristic signature:** S3-dominant (Forcing). Bifurcation points appear
where S3 produces resonance or competing solutions.

**Canonical examples:** Lagrangians at action bifurcation points; field
equations at geometric singularities; gauge theories with unresolved redundancy;
ghost sectors in quadratic gravity.

---

### Type III — Consistency Collapse

**Definition:** Admissibility is lost because G itself becomes internally
inconsistent. Collapse arises from incompleteness, contradictions, or
overdetermination within G's formal structure.

**Mechanism:** G encodes structural constraints that conflict or overdetermine
the admissible state space. No consistent scope family can be instantiated in
the affected region.

**Topology of A(G):** A(G) is not well-defined in the collapsed region —
Λ itself has inconsistent structure there. ∂A(G) is gradual and
context-dependent.

**A_f / A_h under C:** Collapse occurs within A_h itself — some sub-regions
remain hypothetically describable while others do not. Recovery requires
revision of G. Under C, Type III may be partially masked if C restricts
attention to sub-regions of Λ where the conflict is not active — but this
is a C-dependent suppression, not a resolution.

**Characteristic signature:** K ≠ ∅ in Σ — conflicting signature pairs
unresolvable by dominance hierarchy. Δ is endogenous: what counts as
admissible perturbation is defined by G itself.

**Canonical examples:** Constitutional legal systems with conflicting norms;
market formalisms with incomplete contracts; axiomatic systems at Gödel
boundaries; ghost/unitarity/causality triad in quadratic gravity (risk,
not established collapse).

---

## Comparison Table

| Property | Type I — Boundary | Type II — Solution Space | Type III — Consistency |
|---|---|---|---|
| Collapse location | ∂A(G) in Λ | Interior of Λ | Internal structure of G |
| Generator coherent at collapse? | Yes | Yes | Partial |
| ε-dependent? | No | Partially | Context-dependent |
| C-dependent? | No | Partially (branch selection) | Yes — C can suppress but not resolve |
| A_f / A_h boundary | Sharp, at ∂A(G) | Interior bifurcation | Gradual, within A_h |
| ARW F-category analog | Z_shared | F2 at generator level | None |
| Recovery mechanism | None | Branch selection | Generator revision |
| Dominant signature | S1, S2, S4, S5 | S3 | K ≠ ∅ |
| Δ endogenous? | No | No | Yes |

---

## Signature Inference for Generator Type (Q-GEN-02, partially answered)

| Dominant signature | Inferred collapse type | Characteristic geometry |
|---|---|---|
| S1 (Projection/Selection) | Type I | Discrete sector transitions |
| S2 (Coupling) | Type I | Critical coupling threshold |
| S3 (Forcing) | Type II | Resonance bifurcation |
| S4 (Dissipation) | Type I | Attractor topology change |
| S5 (Stochastic expectation) | Type I | Statistically defined boundary |
| K ≠ ∅ (signature conflict) | Type III | Gradual; requires conflict analysis |

**Limitation:** Type III cannot be inferred from individual signatures alone.
It requires explicit analysis of conflict relations K. This is the boundary of
pure signature-first inference at the generator level.

---

## Self-Referential Structure

ARW applied to generators produces a meta-scope: a scope whose object is a
scope-generating structure. G specifies conditions under which scopes are
possible — structurally the same function ARW performs.

The ARW/ART separation maps onto this precisely:
- ARW without C: observes formal admissibility A(G)
- ART with C: assesses functional admissibility A_f(G | C)

The falsification condition for ARW itself is precise: ARW cannot describe
systems that admit no stable regime structure under any parametrization. This
is A(G) = ∅ for all possible G — the outer boundary of the framework.

---

## Relationship to Existing ARW Falsification Categories

```
Generator G
    │
    ├─ Type I → forces Z_shared in all S_i near boundary
    │            → observable-level: F0 for any class-E π
    │
    ├─ Type II → forces F2-type instability at bifurcation
    │             → may appear as F3 if no branch selected
    │
    └─ Type III → forces F1_BC or F3 in affected S_i
                   → no single F-category captures generator cause
```

---

## ART Application Protocol

1. **Identify G** — what formal object generates the scope family?
2. **Read Σ** — identify P, D, K from governing equations using S1–S5
3. **Infer collapse type** — use signature inference table above
4. **Specify C** — define the epistemic-operational context: available
   observables, Δ-class, ε, resources, reproducibility requirements
   (see `epistemic_context_and_functional_admissibility.md`)
5. **Determine A_f(G | C)** — apply C-criteria to identify operationally
   viable sub-region
6. **Instantiate selectively** — restrict scope construction to A_f(G | C)
7. **Document in ScopeSpec** — add a `generator` block recording G's type,
   C specification, and predicted A_f boundary as pre-registered prediction

---

## Open Questions

- **Q-GEN-01** (open): Is the three-type taxonomy exhaustive? Candidate gap:
  non-autonomous generators may produce collapse geometries not captured.

- **Q-GEN-02** (partially answered, 2026-05-07): Signature-first inference
  works for Type I and II. Type III requires conflict analysis of K.

- **Q-GEN-03** (partially answered, 2026-05-07): G = (Λ, Σ, φ, C) established.
  Open: formal topology conditions on Λ per collapse type; formal definition
  of A_f / A_h boundary independent of specific C.

- **Q-GEN-04** (new, 2026-05-07): What is the minimal C that makes A_f(G | C)
  non-empty for each collapse type? This would characterize the minimum epistemic
  resources required to operationalize a generator of each type.

---

## Validation Cases (candidate)

| Collapse type | Candidate case | Expected evidence |
|---|---|---|
| Type I | CASE-20260315-0008 (Pitchfork, μ-sweep) | Sharp A(G) boundary at μ = 0 |
| Type II | CASE-20260311-0003 (Doppelpendel, E-sweep) | Interior collapse at E_sep |
| Type III | CASE-20260328-0010 (German School System) | Gradual A_f loss; multi-BC conflict |
