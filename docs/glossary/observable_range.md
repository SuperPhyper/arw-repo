---
status: working-definition
last_updated: 2026-04-29
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
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

---

## Falsification Categories Involving Observable Range

### F0 — Range Violation (substrate failure)

Pre-scope assumptions of π break down at some x ∈ X_B.
The scope may be valid, but π is structurally unreliable in this region.
F0 calls for a different observable, not a different scope.

### F1 — Observable Insufficiency (topology-corrected)

The observable cover C_ε is trivial — the observable produces no detectable
distinctions at the chosen resolution.

**Corrected F1 criterion (Felder 2026):**
The general necessary condition for cover non-triviality is:

```
ε < ε*(O, X_B)
```

where ε*(O, X_B) is the smallest ε at which C_ε collapses to a single component
(see `docs/core/cover_stability_criterion.md` §1). ε*(O, X_B) depends on the
**topology** of the observable image O(X_B), not only its span.

The previous shorthand `span(π) < 2ε → F1` is a sufficient condition for
cover triviality **when O(X_B) is a connected interval**. For observables with
non-interval image topology (e.g. bimodal, multi-branch, fragmented), ε*(O,X)
can be substantially smaller than ½·span(O), and the shorthand produces
**false negatives**: an observable whose image is fragmented into components
separated by a gap larger than ε would pass the span check but already have a
trivial cover.

**For typical ARW observables** (monotone, unimodal image): the two formulations
agree. The distinction matters for multi-modal or fragmented observable images.

### F-gradient — Descriptive Crossover (cover-stability failure within R(π))

*New category (Felder 2026 §6.2, v2). Added 2026-04-29.*

An observable π can be structurally sound (fully within R(π)) and have sufficient
span (F1 not triggered), yet still fail to sustain a stable cover at a specific
region of parameter space — because the observable is **too steep** there.

**Definition (descriptive crossover zone):**

```
Z_cover(π, ε) := { x ∈ X_B : σ_Δ(x) ≥ ε }
```

where σ_Δ(x) = sup_{δ ∈ Δ} |O(x+δ) − O(x)| is the perturbation spread
(`docs/glossary/perturbation_spread.md`). Z_cover(π, ε) is the set of states
where the observable gradient is too large for the chosen (ε, Δ) pair to sustain
a stable cover element.

**F-gradient occurs when Z_cover(π, ε) ∩ R(π) ≠ ∅** — cover stability fails
within the valid range of π.

**F-gradient** (falsification category):
```
Observable is within R(π) everywhere in X_B,
but σ_Δ(x) ≥ ε at some x ∈ X_B.
→ Cover C_ε is not Δ-stable at x.
→ Severity: observable_replacement (or scope_adjustment)
```

Remedies: increase ε (accepting coarser partition), reduce ‖Δ‖ (tighter
perturbation class), or replace π with an observable of lower gradient magnitude
in the affected region.

### Distinction Table

| Category | Location | Cause | Observable valid? | Remedy |
|---|---|---|---|---|
| F0 | x ∈ Z(π) | Pre-scope substrate fails | No | Replace observable |
| F1 | all x ∈ X_B | ε ≥ ε*(O,X) — cover trivial | Yes (but insufficient spread) | Replace or widen span |
| F-gradient | x ∈ Z_cover ∩ R(π) | σ_Δ(x) ≥ ε — gradient too steep | Yes (substrate ok) | Adjust ε, Δ, or replace π |
| Z_shared | x ∈ transition | Ergodicity/stationarity fails universally | N/A | Not fixable; applies to all class-E observables |

**Key diagnostic distinction (F0 vs. F-gradient):**
Both produce high σ_Δ and an unstable stability mask. They can only be
distinguished by substrate analysis: F0 is diagnosed by checking pre-scope
assumptions A_i; F-gradient is diagnosed when all A_i hold but |∇O| is large
(Lipschitz bound from `docs/core/cover_stability_criterion.md` §4).

---

## Descriptive Crossover vs. Exclusion Zone

A **descriptive crossover** (F-gradient region) differs structurally from an exclusion zone:

- **Exclusion zone Z(π):** π is not well-defined. The observable itself fails.
  Determined by pre-scope substrate analysis (see `docs/advanced/observable_decomposition.md`).

- **Descriptive crossover Z_cover(π, ε) ∩ R(π):** π is well-defined, but
  σ_Δ(x) ≥ ε. The cover construction fails to produce a stable partition element here.
  Determined by computing σ_Δ (or its Lipschitz upper bound |∇O|·r).

**Empirical example (CASE-20260311-0003, Felder 2026 §6.2):**
The conservative pendulum with observable ω(E,ω₀) exhibits:
- Primary exclusion zone: E ≈ E_sep = 2ω₀² — the separatrix, where ω diverges (true Z(π))
- Secondary descriptive crossover: E ≈ ω₀² — the anharmonic crossover, where |∂ω/∂E|
  becomes large (σ_Δ ≈ 0.36 >> ε = 0.05), but ω remains well-defined (inside R(π))

At ε = 0.05 the two zones merge into one connected instability band (~4% of parameter
window). Only substrate analysis separates them conceptually.

---

## Examples

### r_ss (Kuramoto order parameter)

```
R(r_ss) = { κ ≪ κ_c } ∪ { κ ≫ κ_c }
Z(r_ss) = { κ ≈ κ_c }
```

In Z(r_ss), r_ss simultaneously violates five pre-scope assumptions:
ergodicity (A3.2), uniqueness of μ_stat (A3.4), decay of transients (A3.5),
negligibility of critical fluctuations (A4.2), T-independence (A6.2).

F0 classification for CASE-20260311-0001 at κ ≈ κ_c is documented in the
CASE-0001 CaseRecord.

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

### ω(E, ω₀) (conservative pendulum frequency)

```
R(ω) = X_B \ { E ≈ E_sep }           — ω well-defined away from separatrix
Z(ω) = { E ≈ E_sep = 2ω₀² }          — ω diverges at separatrix
Z_cover(ω, ε=0.05) = { E ≈ ω₀² }    — F-gradient: |∂ω/∂E| large at anharmonic crossover
```

Cover stability fails both at Z(ω) (F0) and at Z_cover (F-gradient) for typical
ε values. See `docs/core/cover_stability_criterion.md` §7.

---

## Consequence for Observable Selection

An observable π should be chosen such that R(π) fully covers the parameter
region of interest — in particular the regime boundaries θ* — and such that
Z_cover(π, ε) is either empty or confined to known transition zones.

If no single π achieves this, multiple observables with overlapping ranges
should be combined. Each observable defines its own scope S_i; coupling
is achieved through operator algebra, not through a shared ε.

When Z_cover(π, ε) is non-empty within R(π), consider:
1. Increasing ε (accepting coarser partition — the cover becomes stable at coarser resolution)
2. Reducing ‖Δ‖ (tighter perturbation class)
3. Applying a stability mask before ε-sweep (exclude Z_cover states from the analysis)
4. Selecting a different observable with smaller gradient magnitude in that region

---

## Related Concepts

- Pre-scope substrate and decomposition → `docs/advanced/observable_decomposition.md`
- Perturbation spread σ_Δ(x) → `docs/glossary/perturbation_spread.md`
- Cover stability criterion and ε*(O,X) → `docs/core/cover_stability_criterion.md`
- Scope tuple S = (B, Π, Δ, ε) → `docs/glossary/scope.md`
- Observable information (necessary condition) → `docs/core/observable_information.md`
- Consequences for scope design → `docs/advanced/observable_consequences.md`
