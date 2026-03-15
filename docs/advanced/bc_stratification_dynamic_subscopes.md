---
status: hypothesis
layer: docs/advanced
related_docs:
  - docs/advanced/bc_operator_signatures_arw.md
  - docs/notes/open_questions.md (Q2, Q9, Q15)
  - docs/bc_taxonomy/boundary_condition_classes.md
---

# BC Stratification and Dynamic Subscopes

## Overview

The standard ARW BC taxonomy treats all boundary-condition classes as operating
on the same structural level — as constraints, couplings, or modifications of the
state space X_B within a given scope S = (B, Π, Δ, ε).

This document argues that this picture is incomplete.

**Central hypothesis:**

BC classes are not all primitive on the same structural level.
Some BCs — specifically Dissipation and Forcing — are defined not on the state space,
but on the *dynamical structure* of the system: on flows, vector fields, and trajectories.
They are **derived BCs on a dynamic subscope**, not primary BCs on the state space.

This stratification has consequences for scope construction, perturbation logic,
observable selection, and the interpretation of regime transitions.

---

# 1. Two Levels of BC Structure

## 1.1 State-space BCs

Restriction, Coupling, Aggregation, and Symmetry breaking are definable
purely in terms of the state space X and its structure:

- **Restriction** selects X_B ⊆ X — a subset of admissible states.
  It exists independently of any dynamics.
- **Coupling** defines a dependency structure between subsystems X₁, X₂ ⊆ X.
  It modifies the product structure X₁ × X₂ by introducing interaction terms.
  It exists as a structural property of the configuration space.
- **Aggregation** introduces a coarse-graining map X → X/~ .
  It reduces distinctions in the state space.
- **Symmetry breaking** lifts a degeneracy in X — it selects among
  symmetry-equivalent states.

All of these can be stated without reference to time or dynamics.
They are **static BCs**: properties of the state space, not of its evolution.

## 1.2 Dynamic BCs

Dissipation and Forcing cannot be defined on the state space alone.
They require the dynamical structure — a vector field f: X → TX,
or equivalently, a flow φ_t: X → X.

- **Dissipation** is a property of the flow: contraction of phase-space volume,
  convergence toward attractors, irreversibility under time reversal.
  It is not visible in any single state x ∈ X — only in the trajectory {φ_t(x)}.
- **Forcing** is an external term in the vector field: ẋ = f(x) + g(t).
  It modifies the dynamics directly, not the state space.

Neither can be read off from X_B alone.
They are **dynamic BCs**: properties of the flow structure on X_B.

---

# 2. The Dynamic Subscope

To make dynamic BCs observable, a different scope is required.

Define the **dynamic subscope** S_dyn as a scope whose objects are not states,
but dynamical structures:

S_dyn = (B_dyn, Π_dyn, Δ_dyn, ε_dyn)

where:

- B_dyn selects admissible flows or vector fields on X_B
- Π_dyn consists of trajectory observables: contraction rates, Lyapunov exponents,
  residence times, attractor geometry
- Δ_dyn consists of perturbations of the flow (e.g., δλ for decay rate,
  δg for forcing amplitude)
- ε_dyn is the resolution threshold on trajectory-space distinctions

The dynamic subscope is **derived from** the state-space scope S:
it presupposes X_B and the coupling structure, and adds the temporal dimension.

This gives a natural ordering:

S_state (state-space scope)  
→ S_dyn (dynamic subscope, derived from S_state)

Static BCs are visible in S_state.
Dynamic BCs are visible only in S_dyn.

---

# 3. Consequences for the BC Taxonomy

The standard six-class taxonomy can now be stratified:

| BC class | Scope level | Objects | Primitive or derived |
|---|---|---|---|
| Restriction | S_state | states, configurations | primitive |
| Coupling | S_state | state dependencies | primitive |
| Aggregation | S_state | equivalence classes | primitive |
| Symmetry breaking | S_state | degeneracy structure | primitive |
| Dissipation | S_dyn | flows, attractors | derived |
| Forcing | S_dyn | vector field modifications | derived |

This is not a claim that dynamic BCs are less real or less important.
It is a structural claim: they require a richer scope to be visible,
and they operate on objects of a different type.

---

# 4. Consequences for Perturbation Logic

The stratification explains the asymmetry in perturbation logic observed
when comparing Coupling-Cases (CASE-0001, CASE-0002) with the proposed
Dissipation-Case (CASE-0004).

For **static BCs**, perturbation is natural within S_state:

- δκ (coupling strength perturbation) is a perturbation of the state-space structure.
  It modifies the coupling matrix — an object in S_state.
- The swept parameter and the perturbation parameter live in the same space.

For **dynamic BCs**, perturbation must be performed in S_dyn:

- δλ (decay rate perturbation) is a perturbation of the flow structure.
  It modifies the contraction rate — an object in S_dyn, not S_state.
- The swept parameter (e.g., time t or observation window) lives in S_state,
  but the perturbation parameter δλ lives in S_dyn.

This means that Dissipation-Cases are inherently **cross-scope**:
the sweep is in S_state, the perturbation is in S_dyn.

The robustness condition for Dissipation regimes therefore reads:

> The partition is stable under perturbations δλ ∈ Δ_dyn,
> where Δ_dyn contains perturbations of the flow,
> not of the state-space configuration.

This is structurally consistent with the ARW falsification framework
(F1–F4), but requires explicit recognition that Δ operates in S_dyn.

---

# 5. Layered Scopes and Scope Interaction

A system with both static and dynamic BCs active simultaneously
— for example, a dissipative coupled oscillator, or a population with
carrying capacity and extinction dynamics —
requires a **layered scope**:

S_layered = (S_state, S_dyn)

where S_dyn is built on top of S_state.

The interaction between layers produces phenomena not visible in either alone:

- The state-space structure (Restriction, Coupling) shapes which attractors
  are geometrically possible in S_dyn.
- The flow structure (Dissipation) determines which of those attractors
  are dynamically reachable and stable.
- Regime partitions in S_layered reflect both the geometric structure of X_B
  and the flow structure on X_B simultaneously.

This layering is the structural reason why Populationsdynamik (CASE-0005)
is more complex than Isotopzerfall (CASE-0004):

- CASE-0004: only S_dyn is non-trivial. S_state is simple (1D, no coupling).
  Clean isolation of Dissipation BC.
- CASE-0005: both S_state (Restriction via carrying capacity K,
  Coupling via predator-prey interaction) and S_dyn (Dissipation via
  extinction dynamics) are non-trivial simultaneously.
  The layered interaction produces the extinction threshold as a
  scope-boundary phenomenon.

---

# 6. Dynamic Scope Boundaries Revisited

This framework resolves the earlier observation that dynamic scope boundaries
operate at a different description resolution than the scope interior.

A dynamic scope boundary — such as an extinction event or a crisis onset —
is a transition *between* S_state and S_dyn levels:

- Inside the normal regime, S_state is the relevant description level.
  The system occupies a region of X_B with stable observable values.
- At the boundary, S_dyn becomes dominant: the flow structure determines
  whether the system is pulled toward a new attractor or remains in the
  current basin.
- After the transition, S_state is again the relevant level —
  but now a different, reduced X_B.

The description resolution shift at the boundary is therefore not accidental:
it reflects the structural fact that the boundary is a S_dyn phenomenon
embedded in an S_state description. It requires finer ε (or different Π)
to resolve because it lives on a different scope level.

This connects directly to Q2 (state-dependent ε) and Q3 (multiple ε):
the ε required near a dynamic scope boundary is the ε_dyn of S_dyn,
not the ε of S_state. A single uniform ε cannot capture both.

---

# 7. Implications for ARW Formalization

The BC stratification suggests three extensions to the current ARW framework:

**7.1 Explicit scope level annotation**

BC classes in ScopeSpec and BCManifest should carry a scope-level marker:

```yaml
BC:
  class: Dissipation
  scope_level: dynamic
  # vs.
  class: Coupling
  scope_level: state
```

This makes cross-scope perturbation logic explicit and prevents
conflation of Δ_state and Δ_dyn in falsification conditions.

**7.2 Layered scope specification**

For systems with both static and dynamic BCs, ScopeSpec should
support a layered structure:

```yaml
S_state:
  B: ...
  Pi: [state observables]
  Delta: [state perturbations]
  epsilon: ...
S_dyn:
  B_dyn: [admissible flows]
  Pi_dyn: [trajectory observables]
  Delta_dyn: [flow perturbations]
  epsilon_dyn: ...
```

**7.3 Scope-level transfer metrics**

Transfer admissibility between cases with different scope-level BC structures
(e.g., a Coupling case and a Dissipation case) should explicitly account
for the scope level mismatch. Cross-level transfer may require matched-ε
correction not only for N (regime count) but for scope level alignment.

---

# 8. Open Questions

This document raises the following new questions, connected to existing entries:

**Q-new-A — Is the state/dynamic stratification exhaustive?**
Are Restriction, Coupling, Aggregation, Symmetry breaking, Dissipation, Forcing
the only BC classes, or are there BCs that operate on a third structural level
(e.g., on the space of flows of flows — second-order dynamics)?

**Q-new-B — Can dynamic BCs generate static BC structure?**
Dissipation can create effective Restriction: the attractor geometry
defines an effective X_B that the system cannot escape.
Is this a general mechanism? Can all static BCs be generated
as long-time limits of dynamic BCs?

**Q-new-C — Perturbation mixing across scope levels**
In layered scopes, a perturbation in S_dyn (δλ) may induce
structural changes in S_state (new attractor → new effective X_B).
Under what conditions is this cross-level perturbation controllable?
When does it constitute a scope transition rather than a regime shift?

These questions connect to Q2, Q3, Q9, and Q15 in `docs/notes/open_questions.md`.

---

# 9. Summary

The central claim of this document:

> BC classes are not all primitive on the same structural level.
> Static BCs (Restriction, Coupling, Aggregation, Symmetry breaking)
> operate on the state space and are visible within S_state.
> Dynamic BCs (Dissipation, Forcing) operate on the flow structure
> and are only visible within a derived dynamic subscope S_dyn.

Consequences:

- Perturbation logic differs between static and dynamic BCs
  because their parameters live in different scope levels.
- Systems with both BC types require layered scope specifications.
- Dynamic scope boundaries are S_dyn phenomena embedded in S_state descriptions,
  which explains their different description resolution.
- The BC stratification provides a structural basis for the design of
  CASE-0004 (Isotopzerfall) and CASE-0005 (Populationsdynamik)
  as probes of the dynamic subscope.
