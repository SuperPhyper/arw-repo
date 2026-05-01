---
status: working-definition
layer: docs/advanced/
title: "Invariance as Scope-Persistence"
created: 2026-05-01
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/scope_extended_definition.md
  - docs/advanced/causality_as_directed_observable_structure.md
open_questions:
  - Q-INV-01
  - Q-INV-02
---

# Invariance as Scope-Persistence

This document develops the ARW treatment of invariance. It places the ARW
concept in explicit relation to classical invariance (Noether, Einstein) and
identifies where ARW generalises, where it is compatible, and where important
distinctions must be maintained.

---

## 1. Classical Invariance: Two Forms

**Noether invariance** identifies quantities preserved under specific
transformations of a system's variables:

> A continuous symmetry of the action → a conserved quantity.

The transformation is given (time translation, spatial translation, rotation).
The invariant is derived from it. Invariance is a property of the system's
equations under that transformation.

**Einstein invariance** separates physical content from coordinate choice:

> Physical laws must be invariant under coordinate transformations.

The transformation is a change of description (coordinate system). The
invariant is the physical content that survives across descriptions. Invariance
is a constraint on what counts as a physically meaningful statement.

Both forms share the same structure:

```
Transformation T applied → quantity / law Q unchanged
```

The transformation is known in advance. Invariance is a check — does Q
survive T?

---

## 2. ARW Invariance: Scope-Persistence

ARW generalises this structure in one step:

> An invariant is a structure that persists across admissible changes of scope.

A **scope transformation** is any change to one or more components of
S = (B, Π, Δ, ε): extending B, replacing an observable in Π, tightening Δ,
changing ε. The invariant is whatever cover structure, partition boundary,
or observable relationship survives the transformation.

Formally: a structure Q is a **scope-invariant** with respect to a set of
scope transformations T = {T_1, T_2,...} if:

```
Q(S) = Q(T_i(S))   for all T_i ∈ T
```

where Q(S) is the value or structural property of Q evaluated within scope S.

**The key difference from classical invariance:**

In Noether and Einstein, the transformation T is specified in advance. The
question is: does Q survive T?

In ARW, T is a free variable — an open search over possible scope changes.
The question becomes: for which Q does Q survive across the broadest set
of scope transformations? This is invariance as a search problem, not a
verification problem.

---

## 3. Mapping to Classical Invariance

| Classical concept | ARW analogue |
|---|---|
| Coordinate transformation | Scope transformation T(S) |
| Symmetry of the system | Stability of a description across T |
| Conserved quantity | Scope-persistent cover structure |
| Dynamical invariant (Noether) | Scope-invariant partition boundary θ* |
| Covariant law (Einstein) | Scope-invariant observable relationship |

**Precise mapping:**

```
Noether:   invariance under transformation of variables
Einstein:  invariance under transformation of coordinates
ARW:       invariance under transformation of descriptions
```

Classical invariants are special cases of scope-invariants: they are
structures that persist under a specific, named class of scope transformations
(those corresponding to physical symmetries or coordinate changes). ARW
invariants are more general because the scope transformation is not restricted
to physically motivated symmetries.

---

## 4. Pre-Scopal Structure and Invariants

The deepest invariants in ARW are **pre-scopal structures** — properties of
the system's state space and governing equations that are independent of any
particular choice of (B, Π, Δ, ε).

**Pre-scopal structures are what every scope transformation survives.**

They are not directly observable in any single scope. They are inferred from
the persistence of certain structures across multiple scopes: if a partition
boundary θ* appears at the same normalised BC value regardless of which
observable is used, which ε is chosen, or which Δ class is declared, then
θ* is evidence of a pre-scopal structure in the system.

This connects to Noether's insight from the opposite direction:

- Noether: a known symmetry implies a conserved quantity.
- ARW: a persistent scope-invariant implies an underlying structure
  that constrains all valid descriptions of the system.

The ARW move is inferential — from observed persistence across descriptions
to the existence of something that all descriptions are constrained by.

---

## 5. Invariant ≠ Observable in Every Scope

This is the critical distinction that prevents confusion.

A scope-invariant Q may exist — may persist across scope transformations —
without being observable in any particular scope.

**Example:** A partition boundary θ* that exists in the micro-level cover
C_ε(π_micro, B) but not in the macro-level cover C_ε(π_macro, B) is
scope-invariant with respect to changes in ε and Δ (it persists robustly
at the micro level) but is not observable in a scope whose Π contains only
π_macro.

**Formally:**

```
Q scope-invariant  ≢  Q observable in scope S
```

A structure is scope-invariant if it persists across admissible scope
transformations of the scopes in which it is observable. Scopes in which
it is not observable simply do not detect it — they do not falsify it.

**Consequence for scope design:** The absence of a structure in a scope is
not evidence of its non-existence. It is evidence that the current (Π, ε, Δ)
does not resolve it. This is the ARW reformulation of the classical problem
of hidden variables — not as a metaphysical claim, but as a descriptive gap.

**Connection to Noether:** A Noether-invariant quantity (e.g., energy) is
not automatically measurable in every scope. A scope that uses only phase
observables and no energy observable has no access to energy conservation —
even though energy is conserved. The invariant exists; the scope does not
resolve it.

---

## 6. Scope-Invariance as a Research Programme

The ARW research programme can be partially characterised as:

> Identify structures that persist across the broadest admissible set of
> scope transformations for a given class of systems.

This is operationalised through the transfer analysis framework (Φ, RCD,
TBS_norm): high transfer admissibility between two scopes S_A and S_B means
that the partition structure is approximately scope-invariant across the
transformation S_A → S_B.

**The transfer metric Φ is therefore a scope-invariance measure:**
it quantifies how much of the partition structure survives a specific
scope transformation (change of system, observable, or BC domain).

A high Φ across a wide class of transformations identifies a robust
scope-invariant. A low Φ identifies a scope-dependent structure — one
that is real within its scope but does not generalise.

---

## 7. Relation to Einstein: Scope-Covariance

Einstein's requirement that physical laws be coordinate-invariant can be
reformulated in ARW terms as a **scope-covariance** requirement:

> A physically meaningful statement must be expressible in a form that
> is invariant under admissible scope transformations.

"Admissible scope transformations" in the physical context are those that
preserve the pre-scopal substrate — they change the description without
changing what is being described. A statement that holds only in one scope
but not in any other is not a physical law; it is a scope-artefact.

ARW makes this criterion operational: a scope-artefact is a structure whose
transfer admissibility Φ is low across the relevant class of scope
transformations. A robust physical claim should have high Φ across all
scopes that resolve the relevant dimension of the system.

---

## 8. Summary

```
Classical invariance:
  Given transformation T, find Q such that T(Q) = Q.
  → Invariance as verification.

ARW invariance:
  Given a class of systems, find Q such that Q persists across
  all admissible scope transformations.
  → Invariance as search.

Relation:
  Classical invariants are scope-invariants restricted to physically
  motivated transformation classes.
  ARW invariants are more general: the transformation class is open.

Critical distinction:
  Scope-invariant ≠ observable in every scope.
  Absence in a scope is a descriptive gap, not a falsification.

Research consequence:
  Transfer admissibility Φ is a scope-invariance measure.
  High Φ across wide transformation classes identifies robust invariants.
  Pre-scopal structures are the limiting case: invariants that survive
  every admissible scope transformation.
```

---

## 9. Open Questions

**Q-INV-01 (open):** Is there a formal criterion — analogous to Noether's
theorem — that maps from a specified class of scope transformations to the
existence of a scope-invariant? That is: if a scope is stable under a
one-parameter family of observable substitutions, does this imply the
existence of a conserved structure in the partition? The analogy with
Noether suggests this may be possible but the precise formulation requires
careful treatment of what "scope symmetry" means formally.

**Q-INV-02 (open):** The transfer metric Φ measures scope-invariance
between specific pairs of scopes. A more general measure would quantify
invariance across a whole class of scope transformations simultaneously —
analogous to a group-theoretic treatment of symmetry. What is the
appropriate mathematical structure for this generalisation, and does it
connect to existing invariance theory in dynamical systems or topology?
