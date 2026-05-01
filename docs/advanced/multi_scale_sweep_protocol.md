---
status: note
layer: docs/advanced/
title: "Multi-Scale Sweep Protocol"
created: 2026-04-30
depends_on:
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
  - docs/glossary/scope.md
  - docs/advanced/cover_height.md
related_cases:
  - CASE-20260430-XXXX
open_questions:
  - Q-MULTI-01
  - Q-MULTI-02
---

# Multi-Scale Sweep Protocol

This document specifies the sweep protocol for cases with multi-level
observable families Π = {π_micro, π_meso, π_macro}. The protocol ensures
that the parameter grid is dense enough to resolve the finest observable's
regime structure, from which coarser cover levels are derived as
aggregations — not as independent sweeps.

---

## 1. Core Principle

A multi-scope sweep requires only **one pass** over the parameter domain B,
but the grid density must be set by the observable with the largest gradient
relative to its working ε — that is, the observable whose cover structure
imposes the finest resolution requirement on B.

**Grid density is determined by G_max/ε, not by a fixed observable hierarchy.**

In a typical multi-scale case, π_micro has the largest G_max/ε ratio and
therefore determines the grid density. But this is an empirical property
of the specific system and working ε-values — not a formal consequence of
being labelled "micro". If a configurational observable π_κ or a meso-level
observable has a larger G_max/ε ratio, it sets the grid density instead.

The practical consequence is unchanged: the finest grid required by any
observable in Π is the grid for all observables. All covers are constructed
from the same sweep dataset by applying their respective working ε values.

**Note on the nesting assumption:**

The ordering boundaries(π_macro) ⊆ boundaries(π_meso) ⊆ boundaries(π_micro)
is a testable empirical hypothesis for each case — not a formal axiom. Cover
boundaries at different observable levels need not nest. Non-nesting is a
positive finding (see Section 4 consistency checks), not an error.

---

## 2. Grid Density Determination

### Step 1 — Estimate gradients for all observables in Π

Before the main sweep, estimate the gradient of each π_ℓ ∈ Π along each
sweep axis b_j:

```
G_ℓ(b_j) = |∂π_ℓ / ∂b_j|   for each observable ℓ, each axis j
```

This can be done analytically or via a sparse pilot sweep (10–20 points).

### Step 2 — Identify the grid-determining observable per axis

For each sweep axis b_j, the minimum grid spacing is set by the observable
with the largest G_max/ε ratio:

```
ℓ*(b_j) = argmax_ℓ  G_ℓ,max(b_j) / ε_ℓ

Δb_j,min = ε_{ℓ*} / G_{ℓ*,max}(b_j)
```

This ensures that adjacent grid points differ by at most ε_ℓ in each
observable — i.e., no cover boundary falls between two grid points
undetected for any observable in Π.

### Step 3 — Verify all observables are adequately resolved

For each observable π_ℓ ∈ Π, confirm:

```
Δb_j,min ≤ ε_ℓ / G_ℓ,max(b_j)   for all ℓ
```

If this holds for all observables, the grid is sufficient. The
grid-determining observable ℓ* typically but not necessarily corresponds
to the observable labelled "micro" — this should be verified empirically
per case, not assumed.

---

## 3. Sweep Execution

**One sweep, all observables measured simultaneously.**

At each grid point b_i ∈ B_grid:

1. Simulate the system from initial condition x_0 + δ (for each δ ∈ Δ sample)
2. Record the full trajectory x(t) for t ∈ [T_transient, T_sim]
3. Compute all three observables from the same trajectory:
   - π_micro(b_i) = joint phase coherence (or modal energy ratio)
   - π_meso(b_i)  = COM trajectory variance
   - π_macro(b_i) = end-effector variance
4. Record all conditioned parameter values in BCManifest for this run

**No separate sweeps at different resolutions.** The three observables are
computed from one simulation per grid point. This is both computationally
efficient and scientifically necessary — it guarantees that observable
differences at the same b_i reflect genuine structural differences, not
simulation artifacts from different runs.

---

## 4. Cover Construction Order

After the sweep, covers are constructed from fine to coarse:

### Level 1 — Micro cover (finest)

```
C_ε_micro(π_micro, B_grid)
```

Constructed first, on the full fine grid. Determines N*_micro and
the set of micro-regime boundaries {θ*_micro,k}.

### Level 2 — Meso cover

```
C_ε_meso(π_meso, B_grid)
```

Constructed on the same grid with ε_meso > ε_micro (wider resolution).
Expected: N*_meso ≤ N*_micro. The meso cover is a coarsening of the
micro cover in the following sense: each meso cover element should
contain one or more micro cover elements.

**Consistency check:** For each meso boundary θ*_meso, verify that a
micro boundary θ*_micro exists within the micro grid spacing. If a meso
boundary has no micro predecessor, the nesting assumption is violated —
this is a structural finding, not an error.

### Level 3 — Macro cover (coarsest)

```
C_ε_macro(π_macro, B_grid)
```

Constructed last. Expected: N*_macro ≤ N*_meso. Each macro cover element
should contain one or more meso cover elements.

**The latent regime diagnostic:** A_latent values are identified as
grid points b_i where:

```
C_ε_micro(π_micro, b_i) is in a non-trivial boundary region
AND
C_ε_macro(π_macro, b_i) is in the interior of a macro cover element
```

These are the points where internal structure is already reorganized
but the macro observable has not yet registered the transition.

---

## 5. Anisotropy Detection

The cover construction across observables reveals anisotropy in B:

**Cover anisotropy:** If cover boundaries of different observables are not
parallel in a 2D sweep (as in CASE-0002's diagonal boundary structure), the
observable family is anisotropic with respect to B's geometry. This is a
positive empirical finding about the coupling structure of the observables —
not a scope problem.

**Gradient anisotropy per observable pair:** The ratio

```
R_aniso(π_ℓ, π_m, b_j) = G_ℓ(b_j) / G_m(b_j)
```

measures how much more sensitive π_ℓ is than π_m to variation along axis b_j.
A large ratio means π_ℓ resolves structure along b_j that π_m does not — which
is the cover-geometric definition of π_m being latent with respect to π_ℓ
along that axis (see `docs/glossary/scope_extended_definition.md`, Section 4).

**Note:** R_aniso is defined for any observable pair in Π — not only for
micro/macro comparisons. Including a configurational observable π_κ allows
measuring how strongly the coupling structure co-varies with the dynamic
observables across B.

---

## 6. Protocol Summary

```
MULTI-SCALE SWEEP PROTOCOL
===========================

PRE-SWEEP
  1. Estimate G_ℓ,max along each sweep axis for all π_ℓ ∈ Π (pilot or analytic)
  2. For each axis b_j: ℓ*(b_j) = argmax_ℓ G_ℓ,max / ε_ℓ
  3. Set Δb_j,min = ε_{ℓ*} / G_{ℓ*,max}  per axis
  4. Construct B_grid at density Δb_min
  5. Record all conditioned parameter values in BCManifest
     (including observable-specific T_sim requirements)

SWEEP (one pass)
  For each b_i in B_grid:
    For each δ in Δ_sample:
      Simulate x(t; b_i, x_0 + δ)
      Compute π_micro(b_i, δ), π_meso(b_i, δ), π_macro(b_i, δ)
    Record mean and σ_Δ for each observable at b_i

POST-SWEEP — COVER CONSTRUCTION (fine to coarse)
  1. Build C_ε_micro  →  extract N*_micro, {θ*_micro}
  2. Build C_ε_meso   →  extract N*_meso,  {θ*_meso}
     Check: each θ*_meso has a θ*_micro predecessor within Δb_min
  3. Build C_ε_macro  →  extract N*_macro, {θ*_macro}
     Check: each θ*_macro has a θ*_meso predecessor within Δb_min

LATENT REGIME IDENTIFICATION
  Flag b_i where:
    σ_Δ(π_micro, b_i) ≥ ε_micro  (micro boundary region)
    AND
    σ_Δ(π_macro, b_i) < ε_macro  (macro interior)

ANISOTROPY MEASUREMENT
  Compute R_aniso(b_j) = G_micro / G_macro per axis
  Report in CaseRecord under findings
```

---

## 7. Relation to Existing ARW Pipeline

This protocol extends the standard ARW pipeline
(see [Pipeline Reference](../Pipeline-Reference.md)) at two points:

**Pre-sweep:** The pilot gradient estimation step is new. It replaces
the assumption of uniform grid spacing with an observable-informed
adaptive density. For cases with a single observable, this step is
trivially the existing ε-sweep initialization.

**Post-sweep:** Cover construction now proceeds in a fixed order
(micro → meso → macro) with explicit nesting consistency checks.
The latent regime identification step is new — it has no analogue
in single-observable cases.

All other pipeline steps (BCManifest, Invariants.json, ScopeSpec,
falsification audit, transfer analysis) remain unchanged.
