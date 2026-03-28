---
status: working-definition
layer: docs/advanced/
related_docs:
  - docs/glossary/scope.md
  - docs/advanced/epsilon_and_scope_resolution.md
  - docs/glossary/observable_range.md
  - docs/advanced/observable_decomposition.md
  - docs/notes/open_questions.md
---

# Admissible Resolution Lower Bound

## Overview

In the ARW scope tuple S = (B, Π, Δ, ε), the resolution threshold ε is
typically treated as having an upper bound only: ε must be small enough to
distinguish regimes (span(π) ≥ 2ε, plateau stability condition).

This document establishes that ε also has a **structural lower bound**,
and that this lower bound is not an empirical finding but a **corollary of
the definition of Δ**.

---

## 1. The ε–Δ Consistency Condition (Review)

From `docs/advanced/epsilon_and_scope_resolution.md`, the ε–Δ consistency
condition for bulk states x requires:

```
max_{δ ∈ Δ} |Π(x + δ) − Π(x)| < ε
```

Interpretation: a perturbation δ ∈ Δ (declared admissible noise) must not
push x across a regime boundary. If it did, x would be simultaneously in
two regimes — a contradiction.

This condition is standardly read as a constraint on ε from above:
ε must be large enough to absorb the observable fluctuations induced by Δ.

---

## 2. The Lower Bound: ε Must Exceed the Δ-Induced Signal

The same condition, read from below, gives:

```
ε  >  max_{δ ∈ Δ} |Π(x + δ) − Π(x)|   for all bulk x
```

Define the **Δ-induced observable spread** at x:

```
σ_Δ(x) = max_{δ ∈ Δ} |Π(x + δ) − Π(x)|
```

Then the admissible resolution window is:

```
σ_Δ(x)  <  ε  <  span(Π) / 2
```

The lower bound ε_min = σ_Δ is not a choice — it is **determined by Δ**.
Setting ε < ε_min produces a partition that Δ itself contradicts: the scope
declares two states as belonging to different regimes, while simultaneously
declaring them indistinguishable under perturbation.

This is an internal inconsistency of the scope tuple, not a measurement error.

---

## 3. Structural Consequence: Admissible Resolution Window

A scope S = (B, Π, Δ, ε) is **resolution-consistent** if and only if:

```
ε_min(Δ, Π)  <  ε  <  ε_max(Π)
```

where:

```
ε_min(Δ, Π) = sup_{x ∈ X_B} σ_Δ(x)
ε_max(Π)    = span(Π) / 2
```

If ε_min ≥ ε_max, no resolution-consistent scope exists for this (Π, Δ) pair.
This is a scope infeasibility condition — the observable cannot support a
valid partition given the declared perturbation tolerance.

If ε < ε_min: the scope resolves below its own perturbation tolerance.
Distinctions drawn at this scale are not Δ-stable — they are noise-level
artifacts that the scope's own Δ-definition cannot protect.

---

## 4. Substrate-Induced Lower Bounds

The Δ-induced lower bound is the sharpest formulation, but it has a
precursor: the **pre-scopal substrate** of an observable (see
`docs/advanced/observable_decomposition.md`) carries its own natural scales.

When the resolution α falls below a substrate scale, the observable's
pre-scopal assumptions begin to fail — independently of what Δ specifies.

### Examples

**Integration time T (observables r_ss, var_rel):**
Both require stationarity over T (assumption A6). If the BC sweep is so
fine that neighboring BC points differ in transient length by more than T,
the observable no longer measures a stationary property — it measures
transient position. The substrate-induced lower bound is:

```
α_min  ~  Δ(T_conv) / T_sim
```

where T_conv is the convergence time and T_sim the simulation length.

**Lyapunov time (lambda_proxy):**
lambda_proxy estimates the maximal Lyapunov exponent over finite time T.
Its substrate requires trajectory divergence to be measurable (A6.1, A6.2).
Below the Lyapunov time τ_L = 1/λ_max, trajectory divergence is not yet
established. The substrate-induced lower bound is:

```
α_min  ~  1 / (λ_max · T_sim)
```

**Relaxation time τ_relax (coupled oscillators):**
If the coupling relaxation time τ_relax(k) depends on the BC parameter k,
then sweeping k at resolution finer than Δk ~ 1/τ_relax means neighboring
BC points are within one relaxation time of each other. The system cannot
distinguish them — they are connected by its own dynamics.

### Relationship to Δ

Substrate-induced lower bounds and Δ-induced lower bounds are related but
distinct:

- Substrate bounds arise from the observable's construction.
  They fail silently: the observable is still computable, but measures
  an artifact rather than the intended quantity.
  This is an F0-type failure (observable outside R(π)).

- Δ-induced bounds arise from the scope's own consistency requirement.
  They fail structurally: the partition contradicts Δ by construction.
  This is a new failure category — call it **F5: resolution below Δ-floor**.

---

## 5. New Falsification Category: F5

| Category | Condition | Verdict | Action |
|---|---|---|---|
| F5 | ε < ε_min(Δ, Π) | Resolution-inconsistent scope | Widen ε or narrow Δ |

F5 is distinct from all existing categories:

- F0: observable outside R(π) — substrate failure
- F1: span(π) < 2ε — observable insufficient for this ε
- F2: θ* unstable under Δ — partition not reproducible
- F3: no robust plateau — collective failure
- F4: θ* at sweep boundary — measurement artifact
- **F5: ε < ε_min(Δ, Π) — scope resolves below its own perturbation floor**

F5 and F2 are dual: F2 fires when a specific θ* is Δ-unstable (a regime
boundary is too fine for Δ). F5 fires when the entire resolution level is
below the Δ-floor — all distinctions at this ε are Δ-unstable, not just
one boundary.

---

## 6. Transfer Implications

When a scope S_A is transferred to a domain with different intrinsic
perturbation structure, the ε_min of the target domain may exceed the ε_min
of the source domain.

If the transferred scope uses ε < ε_min(Δ_target, Π), the transfer is
resolution-inconsistent in the target domain even if it was consistent in
the source.

### Classical → Quantum Transfer

The clearest example of a resolution-inconsistent transfer is the attempt
to apply classical regime scopes to quantum systems.

In classical mechanics, Δ is bounded below only by measurement precision —
in principle, Δ can be made arbitrarily small, and ε can follow.

In quantum mechanics, the uncertainty principle imposes a **physically
enforced lower bound** on Δ:

```
Δx · Δp  ≥  ℏ/2
```

For any observable Π that depends jointly on position and momentum (e.g.
phase space observables, action variables), this means:

```
σ_Δ(x)  ≥  f(ℏ, Π)   for some function f
```

The Δ-induced ε_min is not a modeling choice but a **physical constant**.

A classical scope with ε < ε_min(Δ_quantum, Π) is structurally
resolution-inconsistent when transferred to the quantum domain. The
partition it draws at that scale has no admissible counterpart in the
quantum system — not because the quantum system lacks regime structure,
but because the scope's resolution is below the physical perturbation floor.

This explains why classical regime concepts (e.g. "the system is in state A
vs. state B") cannot be transferred below the quantum coherence scale:
the transfer violates F5, not F0 or F2.

**Consequence for ARW transfer metrics:**
Φ (the composite transfer score) does not currently capture F5 violations.
A transfer that scores highly on Φ may still be resolution-inconsistent if
ε < ε_min in the target domain. This is an open gap in the transfer
framework (see open questions below).

---

## 7. The Admissible Resolution Window — Summary

```
                ε_min(Δ,Π)              ε_max(Π)
                    |                       |
  ─────────────────[═══════════════════════]─────────→ ε
  too fine          admissible window        too coarse
  (F5: Δ-inconsistent)                    (F1: insufficient span)

  Substrate lower    Δ-induced lower
  bound (F0)         bound (F5)
  |                  |
  └──────────────────┘
  Both collapse the partition from below,
  but through different mechanisms.
```

A fully specified scope must satisfy both:

1. ε > ε_min(Δ, Π)          — resolution above Δ-floor (F5 check)
2. ε > substrate lower bound — observable within R(π) (F0 check)
3. ε < span(Π) / 2           — observable sufficient (F1 check)
4. θ* stable under Δ at ε    — partition reproducible (F2 check)

Conditions 1 and 2 are the **lower admissibility conditions** for ε.
Conditions 3 and 4 are the existing upper admissibility conditions.

---

## 8. Open Questions

| ID | Question | Priority |
|---|---|---|
| Q_NEW_19 | How to estimate ε_min empirically from sweep data? | high |
| Q_NEW_20 | Does F5 require a new field in ScopeSpec.yaml (epsilon_floor)? | medium |
| Q_NEW_21 | Can Φ be extended to flag F5 violations in cross-domain transfers? | high |
| Q_NEW_22 | What is the quantum ε_min for specific observables (PLV, r_ss analogs)? | medium |
| Q_NEW_23 | Is ε_min(Δ,Π) always computable, or does it require simulation? | medium |
