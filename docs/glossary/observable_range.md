---
status: working-definition
---

# Observable Range R(π)

## Definition

Let π be an observable with pre-scope substrate A = {A_i} and let P be the
parameter space of the system. The **observable range** R(π) is the maximal
subset of P on which all pre-scope assumptions A_i are stable under Δ
(admissible perturbations):

```
R(π) = { p ∈ P | ∀ A_i ∈ A : A_i stable under Δ at p }
```

The complement Z(π) = P \ R(π) is called the **exclusion zone** of π.

## Motivation

Every non-trivial observable π carries a pre-scope substrate — a hierarchy
of assumptions about state space, measure, dynamics, and approximation that
guarantee its algebraic and topological well-definedness. This substrate
precedes the scope definition S = (B, Π, Δ, ε): it constitutes π as a
well-defined expression before the scope takes effect.

The observable range makes explicit in which region of parameter space
this substrate fully holds.

## Relationship to Scope

```
R(π)        — pre-scope, follows from the substrate structure of π
B           — scope parameter, selects X_B ⊆ X
R(π) ∩ B   — effective domain: scope and observable hold jointly
```

If B includes the exclusion zone Z(π), a structural warning arises:
the observable is being used outside its range. This is neither
observable insufficiency (F1) nor scope rejection (F2–F4), but an
independent category:

```
F0: Observable outside its range
    → pre-scope substrate does not hold
    → observable must be replaced or restricted to R(π) ∩ B
    → severity: observable_replacement
```

## Distinction from Existing Categories

- **Observable insufficiency** (existing): span(π) < 2ε — the observable
  has insufficient spread for the chosen resolution. Scope remains valid.
- **F0 / Range violation** (new): pre-scope assumptions of π break down.
  The scope may be valid, but π is structurally unreliable in this region.
  The distinction matters: F0 calls for a different observable, not a
  different scope.

## Examples

### r_ss (Kuramoto order parameter)

```
R(r_ss) = { κ ≪ κ_c } ∪ { κ ≫ κ_c }
Z(r_ss) = { κ ≈ κ_c }
```

In Z(r_ss), r_ss simultaneously violates five pre-scope assumptions:
ergodicity (A3.2), uniqueness of μ_stat (A3.4), decay of transients (A3.5),
negligibility of critical fluctuations (A4.2), T-independence (A6.2).

### var_rel (relative angular variance)

```
R(var_rel) = { E < E_diff, |Δθ| ≪ 2π }
Z(var_rel) = { chaotic diffusion } ∪ { phase wrapping at large amplitudes }
```

### lambda_proxy (finite Lyapunov estimator)

```
R(lambda_proxy) = { deeply chaotic: λ_true ≫ 0 } ∪ { deeply ordered: λ_true ≪ 0 }
Z(lambda_proxy) = { transition regions } ∪ { weak chaos: λ_true ≈ 0 }
```

A6.1 and A6.2 (finite T, finite δθ(0)) are **violated by construction** —
lambda_proxy structurally never takes the defining limits of the true Lyapunov
exponent. This makes Z(lambda_proxy) particularly wide.

### σ²(θ) (phase variance)

```
R(σ²(θ)) = { κ: σ(θ) ≪ π  and  P(θ) unimodal  and  ergodic }
Z(σ²(θ)) = Z_shared ∪ Z_wrap ∪ Z_multi
  Z_shared = { κ ≈ κ_c }          — shared with r_ss
  Z_wrap   = { σ(θ) ≈ π }         — phase wrapping on R
  Z_multi  = { P(θ) multimodal }  — θ̄ not a valid location parameter
```

## Consequence for Observable Selection

An observable π should be chosen such that R(π) fully covers the parameter
region of interest — in particular the regime boundaries θ*.

If no single π achieves this, multiple observables with overlapping ranges
should be combined. Each observable defines its own scope S_i; coupling
is achieved through operator algebra, not through a shared ε.

## Related Concepts

- Pre-scope substrate and decomposition → `docs/advanced/observable_decomposition.md`
- Scope tuple S = (B, Π, Δ, ε) → `docs/glossary/scope.md`
- Falsification categories F1–F4 → `docs/core/`
- Observable insufficiency → `docs/bc_taxonomy/`
- Consequences for scope design → `docs/advanced/observable_consequences.md`
