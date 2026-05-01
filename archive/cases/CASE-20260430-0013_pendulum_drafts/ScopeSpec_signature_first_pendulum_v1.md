---
status: note
layer: archive/cases/CASE-20260430-0013_pendulum_drafts/
case_id: CASE-20260430-0013   # assign sequential ID on repo commit
title: "Multi-Link Pendulum — Multi-Scale Observable Scope"
created: 2026-04-30
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
  - cases/CASE-20260311-0002/
related_cases:
  - CASE-20260311-0002   # same system, single-observable scope — this extends it
open_questions:
  - Q-MULTI-01
  - Q-MULTI-02
---

# ScopeSpec — Signature First
## Multi-Link Pendulum: Multi-Scale Observable Scope

This case is a deliberate extension of CASE-20260311-0002 (Multi-Link Pendulum,
var_rel primary observable). CASE-0002 used a single observable at a single
aggregation level. This case adds two further observables at the meso and macro
levels to empirically test the latent regime formation hypothesis developed in
`docs/advanced/multi_scale_observables_and_latent_regime_formation.md`.

**Scientific purpose:** Demonstrate that the multi-link pendulum contains latent
meso- and micro-level regime structure that is invisible to a macro-only scope,
and characterize the cover-collapse sequence across three observable levels.

---

## 1. System Identification

**System:** N-link mechanical pendulum (N ≥ 3; nominally N = 5 for initial run)

**State space X:**
- Joint angles: θ_i(t), i = 1..N
- Joint angular velocities: dθ_i/dt, i = 1..N
- Full state vector: x = (θ_1, ..., θ_N, dθ_1/dt, ..., dθ_N/dt) ∈ ℝ^{2N}

**Dynamics:** Lagrangian mechanics with optional damping γ and periodic forcing
amplitude A at frequency Ω. Equations of motion are coupled via the joint
constraint structure.

**BC sweep parameter:** Forcing amplitude A (primary sweep) or link count N
(secondary structural variation). A controls the energy injection into the system
and determines whether internal joint modes are excited.

**Fixed parameters (initial run):**
- N = 5 links, equal mass and length
- γ = 0.05 (light damping — sufficient to suppress transients, small enough to
  preserve internal mode structure)
- Ω = ω_0 (natural frequency of first mode) — at-resonance forcing

**B:** A ∈ [0.0, 2.0] (dimensionless forcing amplitude, normalized to first-mode
natural amplitude)

---

## 2. State Spaces and Structural Levels

| Level | State variables | Physical meaning |
|---|---|---|
| Micro | (θ_i, dθ_i/dt) for each i | Individual joint kinematics |
| Meso | Center-of-mass trajectory x_COM(t), y_COM(t) | Collective mass distribution / shape state |
| Macro | End-effector position (x_N(t), y_N(t)) | Terminal link position — "what you see from outside" |

**Key structural fact:** The end-effector position is a function of all joint angles
via forward kinematics. Two distinct joint configurations (θ_1,...,θ_N) can map to
the same end-effector position — this is the kinematic redundancy that creates the
macro-observable blindness to internal structure.

---

## 3. Primitive Operators

| Operator | Symbol | Present? | Where |
|---|---|---|---|
| Coupling | ∘ | Yes | Joint torques couple adjacent link dynamics |
| Restriction | × | Yes | Geometric constraints; forcing amplitude A restricts accessible phase space |
| Dissipation | π (projection) | Yes | Damping γ reduces amplitude |
| Forcing | external input | Yes | Periodic forcing at Ω |
| Aggregation | E[·\|G] | Yes | Observable construction (COM, end-effector both aggregate micro states) |
| Symmetry Breaking | ⊗ | No | — |

**Primary BC operator:** Restriction (A restricts the accessible state space volume
by determining the energy envelope). Secondary: Forcing (Ω determines which modes
are excited within the accessible space).

---

## 4. Observable Definitions

### π_macro — End-Effector Variance (Macro Level)

```
π_macro(x) = Var_t[ r_N(t) ]   where r_N = (x_N, y_N) end-effector position
```

Alternatively: RMS of end-effector displacement from rest position.

**BC class signature:** Pure Restriction + Aggregation (integrates over all joint
contributions; loses internal mode structure)

**Expected R(π_macro):** Valid across all A ∈ B. End-effector position is
well-defined, convergent, and finite-variance for all forcing amplitudes.

**Expected Z_cover:** Large for internal mode variation — π_macro is by
construction insensitive to rearrangements of internal joint modes that leave
the end-effector trajectory unchanged (kinematic redundancy).

**Substrate precondition check (A0–A6):**
- A0: State space well-defined ✓
- A1: x_N computable from joint angles via forward kinematics ✓
- A2: Time-average variance converges for periodic/quasi-periodic motion ✓
- A3: Well-defined everywhere ✓
- A4: Finite variance for bounded A ✓
- A5: Stationary after transient decay (enforced by γ > 0) ✓
- A6: No observable-specific conditions violated ✓

**Predicted sufficiency:** Sufficient for detecting large-scale transitions
(e.g., onset of gross chaotic motion at high A). Insufficient for internal
mode transitions.

---

### π_meso — Center-of-Mass Trajectory Variance (Meso Level)

```
π_meso(x) = Var_t[ r_COM(t) ]   where r_COM = (1/N) Σ_i m_i * r_i(t) / M_total
```

**BC class signature:** Aggregation (E[·|G] conditioned on all links with mass
weighting) + Restriction

**Key structural property:** The COM trajectory is sensitive to the *distribution*
of mass across links — a higher-mode internal configuration shifts the COM even
if the end-effector position is unchanged. This is the structure-preservation
property: π_meso carries inter-configuration information that π_macro loses.

**Formal structure-preservation check:**
- Var_G[π_meso] measures variation in COM trajectory shape across different
  internal mode configurations at the same end-effector position
- If Var_G[π_meso] >> E_G[Var_within], π_meso satisfies the meso criterion

**Expected R(π_meso):** Valid across all A ∈ B (same substrate arguments as
π_macro — COM is always computable and convergent).

**Expected Z_cover:** Smaller than π_macro for internal-mode variation.
π_meso can distinguish configurations that π_macro cannot, because COM captures
the spatial distribution of the chain.

**Predicted sufficiency:** Sufficient for detecting transitions between different
collective shape regimes. Partially blind to individual joint micro-variations
that cancel in the mass average.

---

### π_micro — Joint Phase Coherence (Micro Level)

```
π_micro(x) = 1 - (1/N) * Σ_i Var_t[ θ_i(t) - θ_1(t) ]   (normalized phase spread)
```

Or alternatively: the dominant singular value of the joint angle covariance matrix
(captures the fraction of variance explained by the primary mode).

**BC class signature:** Restriction (direct measurement of individual joint
kinematics without aggregation) + Coupling (inter-joint phase relationships)

**Alternative formulation:** Modal energy ratio — fraction of total kinetic energy
in the first mode vs. higher modes. This is a joint-phase coherence measure that
directly reflects whether the internal modes are in a coherent or distributed state.

**Expected R(π_micro):** Valid across all A ∈ B for the phase-spread formulation.
The modal energy ratio has potential substrate issues at mode-crossing points
(F-gradient risk; see below).

**Expected Z_cover:** Smallest of the three observables for internal structure
transitions. π_micro directly measures joint-level coordination.

**Predicted sufficiency:** Sufficient for detecting micro-level mode transitions.
May be sensitive to individual trajectory noise (F-gradient risk if mode
energies cross rapidly).

---

## 5. BC Class Assignment

**Primary BC class: Restriction**

Justification: The sweep parameter A (forcing amplitude) acts as a restriction
operator × on the accessible phase space. Low A restricts the system to small-
angle near-harmonic motion. High A opens access to large-angle nonlinear and
potentially chaotic trajectories. This is structurally a restriction on the
accessible state manifold.

**Secondary BC class: Forcing**

The driving frequency Ω acts as a Forcing operator — it imposes a periodic
external constraint that selects which internal modes are primarily excited.
At Ω = ω_0 (resonance), the first mode receives maximal energy injection.

**BC class comparison with CASE-0002:**

CASE-0002 used κ (damping coefficient) as the sweep parameter — a Dissipation +
Restriction class. This case uses A (forcing amplitude) as the primary sweep —
a Restriction + Forcing class. The internal mode structure question is new.

---

## 6. Expected Partition Structure

**Strong hypothesis (from multi-scale observable theory):**

The three observables will produce different partition structures over the same
B = A ∈ [0.0, 2.0]:

| Observable | Expected N* | Expected θ* | Predicted regime interpretation |
|---|---|---|---|
| π_macro (end-effector) | 2 | A ≈ 1.2–1.5 | Small-amplitude periodic / large-amplitude aperiodic |
| π_meso (COM) | 3–4 | A ≈ 0.6–0.8 (first), A ≈ 1.2–1.5 (second) | Unimodal shape / distributed shape / chaotic COM |
| π_micro (joint phase) | 4–6 | Multiple | Coherent / partially distributed / fully distributed joint modes |

**The latent regime hypothesis:** At intermediate A (e.g., A ≈ 0.6–0.8), π_micro
and π_meso will detect a regime transition that π_macro cannot. The end-effector
will appear to be in a stable periodic regime while internal modes have already
reorganized. This is the empirical test for latent regime formation.

**Cover-collapse sequence prediction:**

As ε increases from 0:
1. π_micro loses non-trivial cover first (micro mode variations fall below ε)
2. π_meso loses non-trivial cover at higher ε (COM shape transitions merge)
3. π_macro retains non-trivial cover longest (gross motion transitions persist)

If this ordering is confirmed, it validates the multi-scale structure hypothesis.
If π_macro collapses at lower ε than π_meso, the meso structure is fragile and
the hypothesis requires revision.

---

## 7. Perturbation Class Δ

**Δ:** Small perturbations to initial joint angles and velocities:

```
Δ = { δ : ||δθ_i(0)|| ≤ r_θ = 0.05 rad,  ||δ(dθ_i/dt)(0)|| ≤ r_ω = 0.05 rad/s  for all i }
```

**Justification:** Small enough to test regime robustness without crossing
qualitative boundaries. Applies uniformly to all joints — no joint-specific
perturbation structure (preserves symmetry of Δ).

**Δ-stability concern for π_micro:** Near mode-crossing points, π_micro may
be sensitive to which mode receives the perturbation energy. A joint-uniform
perturbation class may need to be restricted to test whether mode-specific
perturbations break the partition (F2 check).

---

## 8. Resolution Vector ε_vector

**Three-component resolution vector:** ε_vector = (ε_macro, ε_meso, ε_micro)

Each component is to be determined empirically via ε-sweep for the respective
observable. Initial estimates based on expected observable ranges:

| Observable | Expected span | Initial ε estimate | Plateau check required |
|---|---|---|---|
| π_macro | O(1) (normalized amplitude) | ε_macro ≈ 0.05–0.15 | Yes — ε-sweep |
| π_meso | O(0.5) | ε_meso ≈ 0.03–0.10 | Yes — ε-sweep |
| π_micro | O(1) (normalized coherence) | ε_micro ≈ 0.05–0.20 | Yes — ε-sweep |

The joint admissible region in ℝ³ is the Cartesian product of individual I_ε
intervals (decoupled case assumption; may need revision if observables are
correlated).

---

## 9. Falsification Conditions

| ID | Observable | Condition | Expected severity |
|---|---|---|---|
| F0-risk | π_micro (modal energy ratio variant) | Mode energy ratio undefined at mode-crossing points | observable_replacement (use phase-spread variant instead) |
| F-gradient-risk | π_micro | High |∂π_micro/∂A| near mode transitions | scope_refinement (apply stability mask) |
| F1-risk | π_macro | If span(π_macro) < 2ε across full B | observable_replacement (increase measurement window) |
| F2-risk | π_micro | If partition boundary θ*_micro shifts under Δ at mode-crossing | scope_refinement (tighten Δ or narrow B) |
| F3 | All three | If no observable produces a plateau | scope_redesign (reconsider B or Ω) |

**Scope mismatch diagnostic (not a falsification — a positive finding):**

If π_macro produces N*_macro = 2 while π_meso produces N*_meso > 2 at the
same B, this confirms the latent regime hypothesis. It is NOT a scope failure;
it is the expected positive result.

---

## 10. Connection to CASE-0002

CASE-0002 (Multi-Link Pendulum, var_rel, single observable) used var_rel of the
full joint angle trajectory. var_rel is a scalar that aggregates variance across
all joints without preserving inter-joint structure — it is closest to π_macro
in the current scheme (Aggregation-class, loses internal mode distribution).

This case explicitly tests whether the regime boundary found in CASE-0002 is a
macro-level artifact or whether it corresponds to a genuine multi-scale
transition. If π_meso and π_micro find earlier transitions at lower A, the
CASE-0002 boundary is a macro-collapse point with latent predecessors.

Transfer analysis between this case and CASE-0002 (at the π_macro level) will
yield Φ that can be compared against the multi-observable analysis.

---

## 11. Pre-Registration Statement

This ScopeSpec pre-registers the following empirically testable predictions
before any simulation is run:

**P1 (Cover-collapse ordering):** ε*(π_micro) < ε*(π_meso) < ε*(π_macro)

**P2 (Latent regime):** ∃ A_latent ∈ B such that the partition under π_meso
or π_micro is non-trivial at A_latent while the partition under π_macro is
trivial (all states in one cover element).

**P3 (Abrupt macro transition):** The first regime boundary detected by
π_macro occurs at a higher A value than the first boundary detected by
π_micro or π_meso.

**P4 (Scope mismatch confirmation):** N*_meso > N*_macro or N*_micro > N*_macro
when evaluated at the same working ε_macro.

If P1–P4 are all confirmed, this constitutes strong empirical support for the
multi-scale observable theory and the latent regime formation hypothesis
(Q-MULTI-01 partially answered).

If P1–P4 are not confirmed (e.g., all three observables produce the same N* and θ*),
the multi-scale structure hypothesis requires revision.
