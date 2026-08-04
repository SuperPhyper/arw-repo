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

**General (action) form — canonical as of 2026-07-17 (monograph Part VII
V2.3, decision D2).** The additive form above presupposes a linear state
space. The general definition writes each δ ∈ Δ as an admissible
perturbation **action** T_δ : X → X and takes a metric d on the descriptive
space D_π:

```
σ_Δ(x) := sup_{δ ∈ Δ} d( O(T_δ x), O(x) )
```

Manifolds, graphs, discrete configurations, probability distributions, and
institutional configurations all admit perturbations without admitting
addition; T_δ x = x + δ on a vector space is the special case, and Felder
(2026) Definition 4 is that additive instance. Every current pipeline case
is additive, so no computed value changes; the general form is what makes
the framework's domain-neutrality claim formally hold.

**Global condition refined (2026-07-17, sharpened 2026-07-18).** The bare
global bound sup_{x∈X} σ_Δ(x) < ε would forbid every perturbation-sensitive
transition state — yet boundary states are exactly what the framework
defines and measures. The canonical pair is the **bulk supremum plus bounded
boundary layer**, the layer stated as a *fraction* (comparable across
scopes) and on the assignment-instability indicator (below):

```
sup_{x ∈ X_bulk} σ_Δ(x) < ε     and     μ({ x ∈ X_B : χ_{Δ,ε}(x) = 1 }) / μ(X_B) ≤ τ_∂
```

for a declared boundary-mass tolerance τ_∂ (μ(X_B) finite and positive;
discrete sweeps: fraction of assignment-unstable samples). Below τ_∂ the
layer is a diagnostic regime boundary; its *crossing* of τ_∂ constitutes an
F-gradient event. §2 below and `cover_stability_criterion.md` should be
read with this refinement; their sup_{x∈X} form is the idealised statement.

**σ vs. χ — spread is not assignment instability (2026-07-18, sweep-form
corrected same day; monograph Part VII Def 6a).** σ_Δ measures how far the
descriptive value can move; the **assignment instability** measures whether
the *regime assignment* changes. Since the partition is defined only on the
sweep nodes, χ is defined there, by component identity across the
unperturbed and perturbed adjacency graphs:

```
χ_{Δ,ε}(x_j) = 1  iff  ∃ δ ∈ Δ : C_ε^δ(x_j) ≢ C_ε(x_j)
```

where C_ε(x_j) is x_j's component in G_ε, C_ε^δ(x_j) its component in the
perturbed graph G_ε^δ (edges on values perturbed by T_{δ,π}), and ≡ is
component identity as sample sets up to the declared boundary-sample
tolerance. (A state-space form r_ε(T_δ x) would be undefined — a perturbed
point need not be a sweep node, and the general regime construction is open,
Q_NEW_25.) A partition boundary state is defined by χ = 1, not by large σ.
The two differ in both directions: a value can move 2ε inside a wide regime
(large σ, χ = 0); at an assignment edge a small motion flips the component
(small σ, χ = 1). σ-based masks remain the **implemented proxy**, but the
σ↔χ error relation is **not yet characterised** — both false positives and
false negatives are possible; the documented one-sided failure (C1) concerns
the pointwise-gradient approximation *to σ*, not σ→χ. **Implementation
gap:** χ is computed nowhere in the pipeline; computing it and
characterising the σ↔χ divergence are one registered question (Q_NEW_26).
Consequence for repairs: the "never lower ε" direction rule is a
**proxy-based pipeline convention**, not a theorem about χ — ε changes the
partition itself, so its effect on the exact boundary fraction is not
guaranteed monotone; ε-repairs stay within the selected plateau and are
verified by recomputation. Support typing: perturbations act per observable
on its support, T_{δ,π} : U_π(X) → U_π(X) (states, trajectory segments,
ensembles, measures, datasets); the induced action is part of the
observable's substrate declaration.

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

`pipeline/epsilon_kappa_map.py::compute_sigma_delta_windowed` computes σ_Δ directly
on the sweep grid:

```
σ_Δ(b_i) = max_{ j : |b_j − b_i| ≤ r } |O(b_j) − O(b_i)|
```

where the window radius r = sup{‖δ‖ : δ ∈ Δ} discretises the perturbation class.
The output field `sigma_delta_windowed` carries the σ_Δ field alongside
`proxy_pointwise`, `proxy_localmax`, and a per-point `pointwise_underestimates`
flag; the binary stability mask is {σ_Δ(b_i) < ε} over that field.

The same module also computes the pointwise gradient |∂O/∂κ| — the leading-order
Lipschitz proxy, **not** σ_Δ. Per C1 (2026-06-02) it under-reports σ_Δ at θ*
(one-sided false negatives), so mask construction must use the direct field or
the local-max bound, never the pointwise proxy near transitions.

A standalone `pipeline/stability_mask.py` is **planned but not implemented**
(action item E-1).
*(Corrected 2026-08-04, core-concept drift audit: this section previously
attributed the direct computation to the unimplemented `stability_mask.py` and
described `epsilon_kappa_map.py` as proxy-only.)*

---

## Related Concepts

- Admissible resolution regime → `docs/core/cover_stability_criterion.md`
- ε*(O,X) collapse threshold → `docs/advanced/epsilon_and_scope_resolution.md` §4
- Observable range R(π) and exclusion zone Z(π) → `docs/glossary/observable_range.md`
- Descriptive crossover (F-gradient) → `docs/glossary/observable_range.md`
- Observable information → `docs/core/observable_information.md`
- ε–Δ interaction → `docs/advanced/epsilon_and_scope_resolution.md` §5
