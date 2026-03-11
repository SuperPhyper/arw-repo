# Scope Completeness: Observable Agreement Rate — Double Pendulum

**File:** `figures/scope_completeness.png`
**Case:** CASE-20260311-0003 (Double pendulum, energy sweep)

## Content

Dual-axis plot. Green area/line (left axis): smoothed observable
agreement rate OAR(ε) between λ_proxy and Var_rel. Cyan step line
(right axis): N_joint, the regime count seen by the finer observable.

## Three zones

1. **Very small ε (< 10⁻⁴):** Both observables resolve all points →
   trivial agreement (OAR ≈ 1). N_joint = 12.

2. **Intermediate ε (10⁻³ to 10⁻²):** λ_proxy collapses while Var_rel
   still discriminates → disagreement zone (OAR ≈ 0). This is the zone
   where latent degrees of freedom are active — the coupling dynamics
   (visible through Var_rel) are structurally relevant but invisible
   to λ_proxy.

3. **Large ε (> 0.05):** Both observables collapsed to N=1 → trivial
   agreement (OAR = 1).

## Key result

The disagreement zone is the diagnostic for scope incompleteness.
It pinpoints the ε-range where the scope's observables fail to
provide a consistent picture of the system's regime structure,
indicating that dynamically active degrees of freedom are only
partially captured by the current observable set.

## Connection to theory

See docs/advanced/scope_completeness.md for the formal definition
of OAR and its connection to latent degrees of freedom and
scope admissibility.
