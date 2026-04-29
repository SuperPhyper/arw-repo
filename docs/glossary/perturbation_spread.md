---
status: definition
layer: docs/glossary/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
---

# Perturbation Spread σ_Δ(x)

## Definition

Let O : X → ℝ be an observable and Δ the admissible perturbation class
(scope component of S = (B, Π, Δ, ε)). The **perturbation spread** at state x is:

```
σ_Δ(x) := sup_{δ ∈ Δ} |O(x+δ) − O(x)|
```

σ_Δ(x) is the worst-case observable shift produced by any admissible perturbation
at state x. It quantifies how much the observable can vary at x under noise
that the scope is required to tolerate.

*Source: Felder (2026), Definition 4. Previously implicit in ARW as the
"ε–Δ consistency condition" — now a named, formal quantity.*

---

## Role in the ARW Framework

### 1. Pointwise stability criterion

A state x is **pointwise stable** iff:

```
σ_Δ(x) < ε
```

That is: all admissible perturbations leave x within its cover element.
A state with σ_Δ(x) ≥ ε is descriptively unstable — admissible noise
can push its observable value across the resolution threshold.

### 2. Lower bound on admissible ε

The admissible resolution regime requires (see `docs/core/cover_stability_criterion.md`):

```
sup_{x ∈ X} σ_Δ(x)  <  ε  <  ε*(O,X)
```

The infimum of the admissible interval is:

```
ε_min = sup_{x ∈ bulk} σ_Δ(x)
```

(The bulk excludes known boundary states where σ_Δ diverges by construction.)
This makes σ_Δ the formal definition of what was previously called "the
consistency condition" in `docs/advanced/epsilon_and_scope_resolution.md` §5:

```
ε_min ≈ max_{x ∈ bulk} max_{δ ∈ Δ} |Π(x+δ) − Π(x)|
```

The two expressions are identical; σ_Δ(x) is now the canonical name.

### 3. Empirical proxy for Z(π)

The exclusion zone Z(π) (see `docs/glossary/observable_range.md`) is the region
where pre-scope substrates fail. High σ_Δ(x) is an empirical signature of Z(π):
as the substrate breaks down, the observable becomes hypersensitive to perturbations.

```
Z(π) ⊆ { x : σ_Δ(x) ≫ ε }   (containment, not equality)
```

The containment is strict because σ_Δ can also be high in **descriptive crossover**
regions (F-gradient) where the observable is structurally valid but too steep.
See `docs/glossary/observable_range.md` §Descriptive Crossover.

### 4. Lipschitz bound (Corollary 1, Felder 2026)

If O is Lipschitz with constant L and Δ is norm-bounded by r (‖δ‖ ≤ r), then:

```
σ_Δ(x) ≤ L · r
```

For locally smooth O, L(x) = |∂O/∂κ| (local gradient magnitude).
This makes the gradient field a first-order upper bound on σ_Δ(x), formally
justifying the gradient proxy in `pipeline/epsilon_kappa_map.py`.

---

## Notation and Conventions

- **Observable argument:** σ_Δ is always defined relative to a specific observable O.
  When multiple observables are in scope, write σ_Δ(x; O) to disambiguate.
- **Supremum vs. maximum:** For continuous Δ and smooth O, the sup is attained.
  For finite Δ (pipeline: a finite set of parameter shifts), the sup is a max.
- **ARW notation:** In ARW documents, O corresponds to π ∈ Π and x to states
  in the BC-parameterized state space X_B. σ_Δ(x) is the worst-case |Π(x+δ)−Π(x)|.

---

## Pipeline Computation

`pipeline/stability_mask.py` (planned, action item E-1) computes σ_Δ directly:

```
σ_Δ(b_i) = max_{δ ∈ Δ_finite} |O(b_i + δ) − O(b_i)|
```

where Δ_finite is a finite sample of the perturbation class.
The output includes the σ_Δ field, the binary stability mask {σ_Δ(b_i) < ε},
the unstable fraction, and the gradient-bound comparison.

The existing `pipeline/epsilon_kappa_map.py` computes |∂O/∂κ| as a gradient proxy —
this is the leading-order Lipschitz bound, not σ_Δ directly.

---

## Related Concepts

- Admissible resolution regime → `docs/core/cover_stability_criterion.md`
- ε*(O,X) collapse threshold → `docs/advanced/epsilon_and_scope_resolution.md` §4
- Observable range R(π) and exclusion zone Z(π) → `docs/glossary/observable_range.md`
- Descriptive crossover (F-gradient) → `docs/glossary/observable_range.md`
- Observable information → `docs/core/observable_information.md`
- ε–Δ interaction → `docs/advanced/epsilon_and_scope_resolution.md` §5
