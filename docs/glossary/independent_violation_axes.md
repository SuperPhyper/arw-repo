---
status: working-definition
layer: docs/glossary/
created: "2026-03-29"
depends_on:
  - docs/glossary/observable_range.md
  - docs/advanced/iva_z_geometry.md
  - docs/advanced/h2_prime_theorem.md
---

# Independent Violation Axes (IVA)

## Definition

Let π be an observable on a scope S = (B, Π, Δ, ε) with pre-scopal assumptions
{A₀,...,A₆}. For each assumption Aᵢ, define the **failure intensity function**:

```
φᵢ : P → [0,1]
```

where φᵢ(p) = 0 means Aᵢ holds robustly at p, and φᵢ(p) > φ_threshold means Aᵢ
is violated at p (see [Observable Range R(π)](observable_range.md) for Z(π) definition).

A **violation direction** for Aᵢ at p is a unit vector bᵢ ∈ T_p(P) along which
φᵢ increases:

```
d/dt φᵢ(p + t·bᵢ) |_{t=0}  >  0
```

The **Independent Violation Axes** of π is the maximal linearly independent
set of violation directions across all failing assumptions:

```
IVA(π) = { b₁, ..., bₖ } ⊆ T_p(P)
```

satisfying: (i) each bᵢ is a violation direction for some Aⱼ in Z(π),
(ii) {b₁,...,bₖ} is linearly independent, and (iii) k is maximal.

---

## Role: Theorem H2'

IVA(π) is the central quantity in **Theorem H2' — the IVA Dimensionality Principle**:

```
dim(Z(π)) = dim(span(IVA(π)))
```

The dimensionality of the exclusion zone equals the rank of the independent
violation directions — determined structurally from the A₀–A₆ substrate
decomposition, not from BC count.

This replaces the earlier H2 heuristic `dim(Z(π)) ≥ max(0, |BC_active| − 1)`,
which was falsified by CASE-0008 (Pitchfork: single BC, dim(Z) = 1, not 0).

---

## Violation Axis Types

The extent of each violation axis depends on the failure type of the assumption:

| Type | Parameter set T | Example |
|---|---|---|
| point | {p₀} | A3 ergodicity collapse at κ_c (Kuramoto, CASE-0001) |
| segment | [0, t_max] | A5 reference failure above κ_F0 (Schools, CASE-20260328-0010) |
| half_line | [0, ∞) | A1 symmetry breaking in μ > 0 (Pitchfork, CASE-0008) |
| global | all of P | A0 state space undefined everywhere |

---

## Key Assumption: Axiom A

The theorem requires that the violation directions b₁,...,bₖ are generically
linearly independent — i.e., no bᵢ is a linear combination of the others.
This is formalized as:

**Axiom A (ARW Structure Axiom):** In all physically meaningful ARW scopes, the
gradients {∇φ₁(p),...,∇φₖ(p)} are linearly independent for λ-a.e. p ∈ Z(π).

Axiom A is empirically validated in `docs/advanced/axiom_a_empirical_validation.md`
via gradient-rank analysis across multiple systems (4-strategy study).

---

## Canonical Reference

Full formal treatment: [IVA and Geometry of Z(π)](../advanced/iva_z_geometry.md)
Theorem proof: [Theorem H2' — IVA Dimensionality Principle](../advanced/h2_prime_theorem.md)
Empirical validation: [Axiom A Empirical Validation](../advanced/axiom_a_empirical_validation.md)
