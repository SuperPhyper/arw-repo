---
status: working-definition
---

# Scope Completeness and Observable Agreement

## Overview

When a scope S = (B, Π, Δ, ε) has multiple observables Π = {π₁, π₂, ...},
each observable induces its own regime partition at a given ε. If these
partitions agree, the scope is **complete** — every observable sees the
same structure. If they disagree, the scope is **incomplete** — there are
active degrees of freedom that some observables capture and others do not.

This document introduces observable agreement as a diagnostic for
scope completeness, connects it to the existing concept of latent degrees
of freedom, and grounds both in empirical results from the double
pendulum (CASE-20260311-0003).

---

## The Observable Agreement Rate

### Definition

For a scope S with observables Π = {π₁, ..., πₖ} and a given resolution ε,
define the **observable agreement rate** as:

```
OAR(ε) = (1/C(k,2)) Σ_{i<j} 𝟙[N_πᵢ(ε) = N_πⱼ(ε)]
```

where N_πᵢ(ε) is the regime count induced by observable πᵢ at resolution ε,
and the sum runs over all pairs of observables.

For k = 2 (two observables), this simplifies to:

```
OAR(ε) = 𝟙[N_π₁(ε) = N_π₂(ε)]   ∈ {0, 1}
```

The **integrated agreement rate** over an ε-range is:

```
OAR_avg = (1/|E|) Σ_{ε ∈ E} OAR(ε)
```

where E is the set of ε-values in the sweep.

### Interpretation

- **OAR_avg ≈ 1**: Observables see the same partition structure across
  most ε-values. The scope is complete — its observables are sufficient
  to capture the system's regime structure.

- **OAR_avg ≪ 1**: Observables disagree across most ε-values. The scope
  is incomplete — there are dynamically active variables that are visible
  to some observables but not others.

- **OAR(ε) = 1 only at extremes**: Agreement at very small ε (both see
  everything) and very large ε (both see nothing) is trivial. The
  informative range is intermediate ε, where the disagreement reveals
  structural incompleteness.

---

## Connection to Latent Degrees of Freedom

A **latent degree of freedom** (see glossary) is a variable that is
dynamically active but suppressed by the current scope — it does not
appear in the observables Π but influences the system's evolution.

Observable disagreement is a *signature* of latent degrees of freedom:

```
OAR(ε) < 1   ⟹   ∃ variable v ∉ Π that affects some πᵢ but not πⱼ
```

More precisely: if π₁ and π₂ produce different regime counts at the
same ε, then the system has structure that one observable resolves and
the other does not. This structure originates from degrees of freedom
that are **partially latent** — visible through one projection but not
through the other.

This is distinct from *fully* latent degrees of freedom, which are
invisible to all observables in Π. Fully latent DOFs produce no
disagreement (both observables miss them equally) but can still
destabilize the scope through accumulation effects.

---

## Empirical Evidence: Double Pendulum

### System

Classical double pendulum (CASE-20260311-0003), two rigid links,
four state variables (θ₁, θ₂, dθ₁, dθ₂), energy sweep E ∈ [0.5, 30] J.

Two observables:
- π₁ = λ_proxy (Lyapunov exponent proxy): sensitivity to perturbation.
  Span = 0.069.
- π₂ = Var_rel (relative angle variance): coupling dynamics between links.
  Span = 0.297.

### Result

Independent ε-sweeps show fundamentally different plateau structures
(see [figures/multi_observable_agreement.png](../../figures/multi_observable_agreement.png)):

- λ_proxy collapses to N=1 at ε ≈ 0.008 (its full value range is only 0.069)
- Var_rel still resolves 13 regimes at ε = 0.008 (value range 0.297)

The agreement rate is **OAR_avg = 28%** (computed over 80 ε-values in
[10⁻⁴, 0.5]).

The disagreement is not random — it has a characteristic ε-profile
(see [figures/scope_completeness.png](../../figures/scope_completeness.png)):

1. **Very small ε** (< 10⁻⁴): both observables resolve all 12 points
   individually → trivial agreement (OAR = 1)
2. **Intermediate ε** (10⁻³ to 10⁻²): λ_proxy collapses while Var_rel
   still discriminates → disagreement zone (OAR ≈ 0)
3. **Large ε** (> 0.05): both collapsed to N=1 → trivial agreement (OAR = 1)

### Interpretation

The disagreement zone corresponds to ε-values where the system has
structure that Var_rel can see (differences in coupling dynamics) but
λ_proxy cannot (because all trajectories have similar divergence rates).

The latent degrees of freedom are the **coupling dynamics between links**
(the relative motion θ₁ − θ₂ and its derivatives). These are dynamically
active at all energies, but they are only visible through Var_rel, not
through λ_proxy. At a given energy, two configurations may have nearly
identical Lyapunov behavior but very different coupling patterns — and
only Var_rel can tell them apart.

### Contrast: Kuramoto

The Kuramoto system has a single observable (r_ss), so OAR is trivially 1.
But more importantly: the order parameter r_ss is a *sufficient statistic*
for the synchronization regime — it captures the relevant structure without
residual latent DOFs. This is why the ε-sweep produces clean, robust
plateaus: there is no hidden structure that would complicate the partition.

---

## Scope Completeness as a Diagnostic

### The Criterion

A scope S is **ε-complete at resolution ε₀** if:

```
OAR(ε₀) = 1   and   ε₀ is not in a trivial-agreement zone
```

A scope is **structurally complete** if:

```
∃ non-trivial ε-interval I where OAR(ε) = 1  ∀ε ∈ I
```

Structural completeness means there exists a resolution range where all
observables agree — and this agreement is not an artifact of over-coarsening
or under-resolving.

### Using Scope Completeness

When OAR_avg is low:

1. **Identify the disagreement zone** in the ε-profile
2. **Determine which observable is more discriminating** (higher N at
   intermediate ε) — this observable captures structure the other misses
3. **Ask: what degrees of freedom drive the discrepancy?** This points
   directly to the latent DOFs
4. **Either extend the scope** (add observables that capture the missing
   DOFs) or **accept the incompleteness** and document which aspect of
   the system each observable captures

### Relation to Existing Framework Concepts

**Admissible reduction** (docs/core/arw_scope_reduction_partition_criterion.md):
A scope transition S → S' is admissible if the partition coarsens
consistently. Observable disagreement suggests that reducing from
two observables to one may *not* be an admissible reduction — the
lost observable carried non-redundant structural information.

**Emergence** (docs/advanced/emergence_overview.md): If a system transition
causes previously agreeing observables to disagree, this is a sign that
new degrees of freedom have become relevant — a scope transition may
be required. The OAR drop is a *precursor* of scope failure.

**ε-interval** (docs/advanced/epsilon_and_scope_resolution.md § 4):
For multi-observable scopes, the admissible ε-interval must be defined
per-observable: I_ε = [ε₁_min, ε₁_max] × [ε₂_min, ε₂_max]. The OAR
measures whether the component intervals overlap — if they do, a single ε
suffices; if they don't, the scope requires per-observable resolution.

---

## Open Questions

- **Weighted OAR:** Should observables with wider dynamic range count
  more? Currently OAR treats all observables equally, but a narrow-range
  observable that collapses early may be less informative.
- **Cross-system comparison:** Is OAR_avg comparable across systems?
  A Kuramoto-like system with one natural observable will always have
  OAR = 1, but that doesn't mean the scope is "better" — just simpler.
- **OAR as a function of BC parameter:** Does OAR(κ) or OAR(E) vary?
  At some parameter values the observables may agree (because the system
  is in a simple regime) and at others they may disagree (transition region).
  This would connect scope completeness to the I_ε(κ) robustness analysis.
- **Threshold for "incomplete":** What OAR_avg is "too low"? This likely
  depends on the application. For a partition used in downstream analysis,
  any OAR < 1 at the working ε is a warning.
