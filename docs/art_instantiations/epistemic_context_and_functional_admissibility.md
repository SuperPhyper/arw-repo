---
status: hypothesis
layer: docs/art_instantiations/
created: 2026-05-07
depends_on:
  - docs/glossary/scope.md
  - docs/art_instantiations/generator_admissibility_taxonomy.md
---

# Epistemic Context and Functional Admissibility

## Core Claim

Functional admissibility A_f is not a property of a generator G alone.
It is a relation:

> **A_f(G | C)**

where C is the **epistemic-operational context** — the totality of epistemic
resources and constraints under which description remains stably viable.

This document defines C formally and specifies the criteria by which
A_f(G | C) is assessed.

---

## Motivation

ARW's admissibility conditions (cover non-trivial, Δ-stable, within I_ε)
determine whether a scope is formally admissible — A(G). But formal
admissibility is not sufficient to determine whether instantiating a scope
under a given parametrization λ is epistemically justified.

The gap is visible in science itself:

- **Newton's mechanics** is formally superseded but remains in A_f under all
  macroscopic C — because it is Δ-stable, reproducible, and compression-viable
  in that regime
- **String theory** has a formally rich A(G) — large A_h — but a partially
  characterized A_f(G | C) because reproducibility and compression-viability
  criteria are not met across most realistic C
- **EFT gravity** has a well-characterized A_f(G | C) precisely because it
  explicitly encodes C through its cutoff — the admissibility geometry is
  made visible by construction

The common structure: what counts as "working science" is not determined by
formal truth but by epistemic stability under the operative context.

---

## Formal Definition of C

An epistemic-operational context C is a tuple:

> **C = (O, Δ_C, ε_C, ρ, τ, σ, κ)**

| Component | Symbol | Definition |
|---|---|---|
| Available observables | O | The set of observables accessible under C; constrains Π_λ = φ(λ) ∩ O |
| Perturbation class | Δ_C | The class of perturbations relevant under C; determines what "stable" means |
| Resolution threshold | ε_C | The operative resolution; determines granularity of admissible partitions |
| Resource bound | ρ | Computational, experimental, or institutional resources available for scope instantiation |
| Temporal contingency | τ | Time horizon over which reproducibility is assessed |
| Stability requirement | σ | Minimum Δ-stability threshold required for functional use |
| Compression demand | κ | Required ratio of complexity reduction to operative coherence loss |

C is provided by ART, not ARW. ARW assesses formal admissibility without C;
ART assesses functional admissibility with C.

---

## The Seven Criteria of A_f(G | C)

λ ∈ A_f(G | C) iff all of the following hold for S = (φ(λ), Δ_C, ε_C):

### 1. Δ-Stability
S remains structurally consistent under all perturbations in Δ_C. The
observable partition does not collapse under the perturbations relevant
to C. This is the existing ARW Δ-stability condition, now indexed to C.

### 2. Reproducibility
The scope structure S(λ) can be reconstructed by independent instantiation
within the temporal contingency τ. The same parametrization λ under the
same C reliably produces the same partition structure.

### 3. Observable Persistence
The central observables in Π_λ ∩ O remain distinguishable under C — they
do not merge, collapse, or leave the observable range R(π) under operative
conditions.

### 4. Resource Proportionality
The cost of instantiating S under C — measured against ρ — is proportional
to the informational yield. Scopes that are formally admissible but require
diverging resources relative to their descriptive gain are in A_h, not A_f.

### 5. Predictive Closure
Local predictions derived from S stabilize within τ. The scope does not
require indefinitely refined ε or Δ-narrowing to produce stable predictions
under C.

### 6. Compression Viability
S reduces the complexity of the described system without losing operative
coherence — it achieves a compression ratio ≥ κ. This is the
information-economic criterion: a scope is functionally admissible only if
it compresses the system's structure in a way that is stable and useful
under C.

Compression viability is the deepest criterion because it connects
admissibility to information economy. It explains why certain descriptions
persist across epistemic contexts even when formally superseded: they remain
compression-viable under a wide range of C.

### 7. Transfer Stability
The scope structure S(λ) remains coherent under scope transfer — when φ is
applied to a related parametrization λ' ∈ A_f(G | C'), the resulting scope
preserves the structural relationships established under λ. Transfer
instability indicates that λ is boundary-adjacent in A_f even if formally
interior to A(G).

---

## Science as Stability Filter

The criteria above imply a specific epistemological position:

> Science is not a truth generator. It is a stability filter for description.

A scope is admitted into scientific practice not because it is true, but
because it satisfies the criteria of A_f(G | C) under the operative epistemic
context of a research community. When C changes — new instruments, new
resource bounds, new temporal contingencies — the boundary of A_f shifts,
and descriptions that were functionally admissible may become hypothetically
admissible or inadmissible.

This is not relativism. The formal admissibility conditions of ARW (A(G))
are context-independent — they are determined by the generator structure alone.
What is context-dependent is the further selection of A_f within A(G). The
progression from A_h to A_f is a movement from formal coherence to epistemic
operability.

---

## Emergent Degrees of Freedom as New Compression Axes

Under this framework, emergent degrees of freedom are not merely new physics —
they are new stable compression axes that enter A_f(G | C) when:

1. A coarser ε_C makes finer-grained descriptions leave A_f (compression
   demand κ forces aggregation)
2. A new collective observable enters O that was not accessible at finer scale
3. The new collective observable has higher compression viability than the
   fine-grained description under C

This is why emergence in ARW is associated with scope splitting: the original
fine-grained scope leaves A_f, and a new coarser scope with a collective
observable enters A_f — not because the physics changed, but because the
compression-viable description changed under C.

---

## Time as an Exceptionally Stable Compression Axis

Among all structural primitives in scientific description, temporal ordering
has unusually high A_f stability across a wide range of C. This is not a
fundamental ontological fact — it is an epistemic-operational one:

- Temporal descriptions are causally reproducible: the same sequence of
  states can be reconstructed independently under most realistic C
- Temporal ordering is compression-viable across an enormous range of
  complexity scales — from thermodynamics to social systems
- Temporal descriptions achieve predictive closure efficiently: local
  time-ordered predictions stabilize faster than spatially or modally
  organized alternatives under most C

This explains why time appears as a structural primitive in nearly all
scientific frameworks — not because it is ontologically fundamental, but
because it is functionally admissible under an exceptionally broad class
of C. Frameworks that attempt to eliminate time as a primitive (timeless
quantum gravity approaches, for example) face the challenge of reproducing
time's compression-viability from more primitive structures — which is
exactly the Lorentz reconstruction problem identified in the quadratic
gravity literature.

---

## Relationship to ARW Falsification Categories

The A_f / A_h distinction does not replace F0–F4. F0–F4 describe failure
modes of individual scopes — they are A(G)-level diagnostics. The C-criteria
operate one level higher: they determine which formally admissible scopes
enter A_f.

The connection:
- F0 (substrate failure) prevents entry into A(G) — no C can rescue it
- F1, F2 (partition/stability failure) may be C-dependent — a scope failing
  F2 under one Δ_C may be stable under a different Δ_C'
- F3 (no admissible ε) prevents entry into A(G) — C-independent
- A scope in A(G) but failing compression viability or resource
  proportionality under C is in A_h(G | C) — this is a new category
  not captured by F0–F4

---

## Open Questions

- **Q-EPO-01** (open): Can the seven criteria be formally ordered by strength?
  Is there a minimal subset sufficient for A_f under specific collapse types?

- **Q-EPO-02** (open): Is compression viability (κ) formally related to
  existing ARW cover metrics? Cover height measures multiscale persistence —
  this may be the formal bridge to κ.

- **Q-EPO-03** (open): What is the formal relationship between C and the
  three generator collapse types? Does each collapse type impose a
  characteristic structure on the minimum C required for non-empty A_f?

- **Q-GEN-04** (registered in generator_admissibility_taxonomy.md): What is
  the minimal C that makes A_f(G | C) non-empty for each collapse type?
