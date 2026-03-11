---
status: working-definition
---

# Latent Degrees of Freedom

## Definition

Latent degrees of freedom are state-space variables that remain dynamically
active but are suppressed by the current scope S = (B, Π, Δ, ε). They do
not appear in the observables Π — or appear only below the resolution
threshold ε — yet they influence the system's evolution and can affect
the partition structure indirectly.

## Formal Characterization

A degree of freedom v is latent under scope S if:

```
∂Π/∂v ≈ 0   or   |∂Π/∂v| < ε   for all π ∈ Π
```

That is: changes in v produce no observable-distinguishable effect under S.
But v is dynamically active: it evolves according to the system's equations
of motion and can couple to the observed variables over time.

## Two Types

**Fully latent:** Invisible to all observables in Π. No single observable
sees the effect of v. These DOFs can accumulate influence and eventually
destabilize the scope (triggering a scope transition).

**Partially latent:** Visible through some observables but not others.
If Π = {π₁, π₂} and v affects π₂ but not π₁, then v is partially latent.
This produces observable disagreement — π₁ and π₂ see different regime
structures at the same ε.

## Diagnostic: Observable Agreement

When multiple observables disagree on the regime count at a given ε,
this is a signature of partially latent degrees of freedom. The
observable agreement rate (OAR) quantifies this: low OAR indicates
that the scope's observables do not jointly capture all active structure.

See [docs/advanced/scope_completeness.md](../advanced/scope_completeness.md)
for the formal treatment and empirical evidence from the double pendulum.

## Role in ARW

Latent DOFs are the mechanism behind several ARW phenomena:

- **Scope instability:** Accumulated latent influence can push the system
  past a regime boundary, making the current scope assignment incorrect.
- **Emergence:** When latent DOFs become observable (through scope
  transition or ε reduction), the partition reorganizes — this is the
  formal emergence condition.
- **Scope incompleteness:** A scope with partially latent DOFs is
  incomplete — its observables provide an inconsistent picture of
  the system's regime structure.

## Example: Double Pendulum

The double pendulum (4 DOFs) observed through λ_proxy and Var_rel
has partially latent DOFs: the coupling dynamics (relative motion
between links) are visible through Var_rel but invisible through
λ_proxy. This produces an OAR of ~28% across the ε-range.

See [figures/scope_completeness.png](../../figures/scope_completeness.png).

## Related Concepts

- [Scope](scope.md)
- [Admissibility](admissibility.md)
- [Emergence](emergence.md)
- [Scope Completeness](../advanced/scope_completeness.md)
