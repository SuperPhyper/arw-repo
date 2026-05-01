---
status: note
layer: archive/cases/CASE-20260430-0013_pendulum_drafts/
case_id: CASE-20260430-0013   # assign sequential ID on repo commit
title: "Multi-Link Pendulum — Multi-Scale Observable Scope"
version: 2
created: 2026-04-30
changes_from_v1: >
  B redefined as full parameter tuple (A, γ, Ω, N, m, l).
  Sweep parameter A is a projection of B, not B itself.
  Conditioning variables explicitly declared with tracked ranges.
  Parameter-space cover logic added: same π_macro value can appear
  in multiple meso/micro regimes at different parameter-tuple coordinates.
  Sections 1, 2, 6, 8 substantially revised. Section 3 (new) added.
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
  - cases/CASE-20260311-0002/
related_cases:
  - CASE-20260311-0002
open_questions:
  - Q-MULTI-01
  - Q-MULTI-02
  - Q-MULTI-03
---

# ScopeSpec — Signature First (v2)
## Multi-Link Pendulum: Multi-Scale Observable Scope

This case empirically tests the latent regime formation hypothesis from
`docs/advanced/multi_scale_observables_and_latent_regime_formation.md`
using a multi-link pendulum with three observables at distinct aggregation
levels.

**v2 revision:** B is now defined as the full parameter tuple. The sweep
over forcing amplitude A is a one-dimensional projection of B, not B itself.
All other parameters are tracked (conditioned) but not varied in the initial
run. This enables the cover to be formed over the full parameter space, where
the same macro-observable value can appear at multiple distinct points that
differ in their meso/micro regime assignment.

---

## 1. System Identification

**System:** N-link mechanical pendulum

**State space X:**
```
x = (θ_1, ..., θ_N, dθ_1/dt, ..., dθ_N/dt) ∈ ℝ^{2N}
```

**Full parameter tuple (B components):**

| Parameter | Symbol | Role | Type |
|---|---|---|---|
| Forcing amplitude | A | Primary sweep axis | Active |
| Damping coefficient | γ | Controls transient decay / energy dissipation | Conditioned |
| Forcing frequency | Ω | Selects mode excitation pattern | Conditioned |
| Link count | N | Structural complexity | Conditioned |
| Link mass (uniform) | m | Energy scale | Conditioned |
| Link length (uniform) | l | Geometric scale | Conditioned |

**B — Full parameter domain:**
```
B = A × γ × Ω × N × m × l
  = [0.0, 2.0] × {0.05} × {ω_0} × {5} × {1.0} × {1.0}
```

The initial run fixes all conditioned parameters at their nominal values
(curly braces = single fixed value). B collapses to a 1D sweep over A
for this run. Future runs extend to 2D or higher by releasing one
conditioned parameter at a time.

**Sweep parameter:** A ∈ [0.0, 2.0] (dimensionless, normalized to
first-mode natural amplitude)

**Conditioned parameters (tracked, not varied — initial run):**

| Symbol | Value | Tracking rationale |
|---|---|---|
| γ | 0.05 | Light damping: suppresses transients, preserves internal modes. Must be tracked because γ determines which meso/micro regimes are accessible. |
| Ω | ω_0 | At-resonance forcing: maximizes first-mode energy injection. Tracked because Ω selects the mode excitation pattern — changing Ω changes which micro regimes form at a given A. |
| N | 5 | Determines number of internal degrees of freedom. Tracked because N directly determines the dimensionality of the micro observable. |
| m, l | 1.0, 1.0 | Set energy and geometric scale. Tracked for dimensional consistency across runs. |

**Why tracking matters:** A conditioned parameter that is not tracked is an
implicit degree of freedom in B. If γ is not recorded, two runs at the same
A but different γ become indistinguishable in the dataset, contaminating the
cover. All conditioned parameters must appear in the BCManifest.

---

## 2. Parameter-Space Cover Structure

The central motivation for the full-tuple B formulation:

**Claim:** The same macro-observable value π_macro(x) = c can be realized
at multiple points b = (A, γ, Ω, N, m, l) ∈ B that lie in *different*
meso or micro cover elements.

Formally:

```
∃ b₁, b₂ ∈ B :
    π_macro(b₁) ≈_ε π_macro(b₂)      [same macro cover element]
    π_meso(b₁)  ≉_ε π_meso(b₂)       [different meso cover elements]
```

This is not a measurement ambiguity — it is a structural property of the
observable family. The macro cover is non-injective with respect to the
meso cover: a single macro cover element C_macro spans multiple meso
cover elements.

**Mechanism in this system:** Kinematic redundancy. The end-effector
position (x_N, y_N) is determined by the sum of all joint angle
contributions. Different internal joint configurations — corresponding to
different internal mode distributions — can produce the same end-effector
trajectory variance. The meso observable (COM trajectory) and the micro
observable (joint phase coherence) are sensitive to which internal
configuration is active.

**Consequence for the initial 1D sweep:** Over A ∈ [0.0, 2.0] at fixed
(γ, Ω, N, m, l), the cover structure is:

- C_ε(π_macro, A) partitions the A-axis into N*_macro regimes
- C_ε(π_meso, A) partitions the same A-axis into N*_meso regimes (expected: N*_meso > N*_macro)
- C_ε(π_micro, A) partitions the same A-axis into N*_micro regimes (expected: N*_micro ≥ N*_meso)

The A-values where π_macro is in a single cover element but π_meso or
π_micro shows a partition boundary are the **latent regime points**:
the macro cover is stable, but the underlying parameter-space structure
is not uniform.

**Consequence for multi-run analysis:** When conditioned parameters are
released (e.g., Ω varied across runs), the same A value at different Ω
will produce different meso/micro regimes. The macro cover may remain
stable across Ω, while the meso/micro covers shift. This is the
multi-dimensional version of the same non-injectivity.

---

## 3. State Spaces and Structural Levels

| Level | Observable | Physical meaning | Aggregation type |
|---|---|---|---|
| Micro | Joint phase coherence π_micro | Internal coupling structure | None (direct) |
| Meso | COM trajectory variance π_meso | Collective mass distribution | Structure-preserving (mass-weighted) |
| Macro | End-effector variance π_macro | Terminal output | Full aggregation (loses internal structure) |

---

## 4. Primitive Operators

| Operator | Symbol | Present? | Where |
|---|---|---|---|
| Coupling | ∘ | Yes | Joint torques couple adjacent link dynamics |
| Restriction | × | Yes | A restricts accessible phase space volume |
| Dissipation | π_proj | Yes | γ damps amplitude |
| Forcing | F_ext | Yes | Periodic forcing at Ω |
| Aggregation | E[·\|G] | Yes | Observable construction for π_meso and π_macro |
| Symmetry Breaking | ⊗ | No | — |

**Primary BC class:** Restriction (A restricts accessible state manifold).
**Secondary BC class:** Forcing (Ω selects mode excitation pattern).

---

## 5. Observable Definitions

### π_macro — End-Effector Variance

```
π_macro(b) = Var_t[ ||r_N(t) - r_N,rest|| ]
```

where r_N = (x_N, y_N) is the end-effector position and r_N,rest is the
rest position. Scalar variance over the simulation window T_sim.

**BC class signature:** Aggregation + Restriction
**Aggregation type:** Full (no group structure — integrates over all joint
contributions via forward kinematics)
**Structure preserved:** None beyond gross displacement amplitude
**Expected R(π_macro):** All b ∈ B (substrate sound everywhere)
**Expected Z_cover:** Large for internal mode variation at fixed A

**Substrate check (A0–A6):** All satisfied. End-effector position is
always computable, convergent (γ > 0 ensures stationarity), and
finite-variance for bounded A.

---

### π_meso — Center-of-Mass Trajectory Variance

```
π_meso(b) = Var_t[ ||r_COM(t) - r_COM,rest|| ]

r_COM(t) = (Σ_i m_i * r_i(t)) / M_total
```

**BC class signature:** Aggregation (mass-weighted) + Restriction
**Aggregation type:** Structure-preserving — mass-weighted average
retains spatial distribution of the chain. A configuration with energy
concentrated in higher links shifts r_COM differently than one with
energy in lower links, even if end-effector variance is identical.

**Structure-preservation criterion (formal check):**
```
Var_{configs at fixed π_macro}[ π_meso ] >> 0
```
i.e., π_meso varies across internal configurations that produce the
same π_macro value. This is the operational test that π_meso is not
simply a rescaled version of π_macro.

**Expected R(π_meso):** All b ∈ B
**Expected Z_cover:** Smaller than π_macro for internal mode variation

---

### π_micro — Joint Phase Coherence

```
π_micro(b) = 1 - (1/N) * Σ_i Var_t[ θ_i(t) - θ_1(t) ]   (normalized)
```

π_micro = 1: all joints move in phase (first-mode dominance)
π_micro → 0: joints move incoherently (distributed higher modes)

**BC class signature:** Restriction + Coupling
**Aggregation type:** None — direct measurement of inter-joint phase
relationships. No information is compressed away.

**Alternative formulation (modal energy ratio):**
```
π_micro_modal(b) = E_1(b) / E_total(b)
```
where E_1 is kinetic energy in the first normal mode. This variant has
F-gradient risk at mode-crossing points (see Section 8).

**Expected R(π_micro):** All b ∈ B for the phase-spread formulation.
**Expected Z_cover:** Smallest — most sensitive to internal structure.

---

## 6. B — Parameter Domain and Conditioning Table

The full parameter domain B and the status of each component for the
initial run:

| Parameter | Symbol | Domain | Initial run | Future extension |
|---|---|---|---|---|
| Forcing amplitude | A | [0.0, 2.0] | **Sweep axis** | — |
| Damping | γ | [0.01, 0.20] | Fixed: 0.05 | 2D sweep with A |
| Forcing frequency | Ω | [0.5ω_0, 2.0ω_0] | Fixed: ω_0 | 2D sweep with A |
| Link count | N | {3, 4, 5, 6, 7} | Fixed: 5 | Separate runs |
| Link mass | m | [0.5, 2.0] | Fixed: 1.0 | Scale variation |
| Link length | l | [0.5, 2.0] | Fixed: 1.0 | Scale variation |

**BCManifest requirement:** All six parameters must appear in BCManifest.yaml
with their values for each run. The sweep_range field covers A only; the
conditioned values are recorded in a separate `conditioned_parameters` block.

**Why the full tuple is B, not just A:**

The cover C_ε(π, b) is formally a partition of B, not of the A-axis alone.
The initial run produces a 1D slice of this cover at fixed (γ, Ω, N, m, l).
The partition boundaries θ* found in this run are valid only at these
conditioned values — they are not claims about B as a whole.

Two runs at the same A but different Ω are at *different points in B* and
may lie in different meso/micro cover elements. Recording only A would
conflate these points and corrupt the cover structure.

---

## 7. Perturbation Class Δ

```
Δ = { δ : ||δθ_i(0)|| ≤ 0.05 rad  and  ||δ(dθ_i/dt)(0)|| ≤ 0.05 rad/s  for all i }
```

Δ perturbs only initial conditions (state space), not parameter values.
Parameter values are fixed by B — they are not perturbed.

**Δ-stability concern for π_micro:** Near mode-crossing points in A,
π_micro may be sensitive to the direction of the initial condition
perturbation (which modes receive energy). A supplementary Δ-test with
mode-specific perturbations (energy injected into mode 1 vs. mode 2)
should be run at suspected mode-crossing A values.

---

## 8. Resolution Vector ε_vector

```
ε_vector = (ε_macro, ε_meso, ε_micro)
```

Each component determined empirically via ε-sweep. Initial estimates:

| Observable | Expected span | ε estimate | Notes |
|---|---|---|---|
| π_macro | O(1) | 0.05–0.15 | Wide span expected across full A range |
| π_meso | O(0.5–0.8) | 0.03–0.10 | Narrower span; more sensitive to internal structure |
| π_micro | O(1) | 0.05–0.20 | F-gradient risk near mode crossings; stability mask required |

The joint admissible region is ℝ³ (Cartesian product of I_ε per
observable). Cross-observable ε constraints are not assumed for the
initial run but must be checked empirically (Q-MULTI-02 related).

---

## 9. Falsification Conditions

| ID | Observable | Trigger | Severity |
|---|---|---|---|
| F0-risk | π_micro (modal variant) | Mode energy ratio undefined at mode crossing | observable_replacement → use phase-spread variant |
| F-gradient | π_micro | σ_Δ ≥ ε near mode transition | scope_refinement (stability mask) |
| F1-risk | π_macro | span(π_macro) < 2ε | observable_replacement |
| F2-risk | π_micro | θ*_micro unstable under Δ at mode crossing | scope_refinement (tighten Δ or narrow B_A) |
| F3 | All | No observable produces plateau | scope_redesign |

**Positive finding (not falsification):**

N*_meso > N*_macro or N*_micro > N*_macro at the same B confirms latent
regime structure. The macro cover being coarser than the meso/micro covers
is the expected scientific result, not a scope failure.

**Conditioning contamination (new in v2):**

If a conditioned parameter drifts between runs (e.g., numerical integration
step size changes effective γ), the cover at fixed A is no longer a clean
1D slice of B. BCManifest must record all conditioned values per run with
sufficient precision to detect this.

---

## 10. Connection to CASE-0002

CASE-0002 used var_rel over the full joint angle trajectory — a scalar
that aggregates across all joints without preserving inter-joint
structure. This corresponds to a macro-class observable in the current
scheme.

The regime boundary found in CASE-0002 at θ* (diagonal in κ, γ space)
may correspond to a macro-collapse point with latent meso/micro
predecessors. This case tests that hypothesis directly by adding the
meso and micro levels.

**Transfer analysis:** Φ(CASE-0002, this case at π_macro level) measures
whether the macro-level partition here is structurally compatible with
CASE-0002. RCD and TBS_norm between the two macro partitions will
indicate whether the different sweep parameters (κ vs. A) produce
comparable macro structure.

---

## 11. Pre-Registration

**P1 (Cover-collapse ordering):** ε*(π_micro) < ε*(π_meso) < ε*(π_macro)

**P2 (Latent regime existence):** ∃ A_latent ∈ [0.0, 2.0] such that
C_ε(π_meso, A_latent) or C_ε(π_micro, A_latent) is non-trivial while
C_ε(π_macro, A_latent) is trivial (single cover element).

**P3 (Macro transition lag):** θ*_macro > θ*_meso and θ*_macro > θ*_micro
(the first macro boundary occurs at higher A than the first meso or micro boundary).

**P4 (Non-injectivity confirmation):** ∃ A₁, A₂ ∈ B_A such that
π_macro(A₁) ≈_ε π_macro(A₂) but π_meso(A₁) ≉_ε π_meso(A₂) — i.e.,
two A values in the same macro cover element lie in different meso
cover elements.

**P5 (Conditioning sensitivity):** Running at Ω = 1.5ω_0 (off-resonance)
at the same A-sweep produces different θ*_micro and θ*_meso values while
θ*_macro remains approximately stable — confirming that Ω is a latent
parameter for meso/micro structure but not for macro structure.

P1–P4 test the multi-scale hypothesis at fixed conditioning values.
P5 is the first extension beyond the initial 1D slice, testing whether
the meso/micro covers are sensitive to conditioned parameter variation
that the macro cover does not detect.
