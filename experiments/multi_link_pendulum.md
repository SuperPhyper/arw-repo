---
status: working-definition
---

# ART Instantiation: Multi-Link Pendulum
## Mechanical Scope Reduction and Admissibility Testing

This document defines the ART scope for the multi-link pendulum experiment.
The pendulum provides a mechanical system with tunable coupling strength,
enabling direct testing of the admissible reduction criterion under
controlled conditions. A minimal version of this example appears in
[docs/overview/minimal_example.md](../docs/overview/minimal_example.md).

---

## 1 System Description

**Domain:** Classical mechanics — constrained rigid-body dynamics

**Why this system:**
The multi-link pendulum has a well-understood transition between
regular and chaotic motion, tunable via coupling (joint stiffness)
and driving. Scope reduction from {θ₁, θ₂} to {θ_mode} has a
clear physical interpretation and an analytically testable
admissibility condition.

**State space X:**
For a two-link planar pendulum:

```
x = (θ₁, θ₂, θ̇₁, θ̇₂)
```

where θᵢ is the angle of link i from vertical
and θ̇ᵢ is its angular velocity.

Extensions to n-link systems increase the state space to 2n dimensions.

**Control parameters:**
- Joint stiffness κ (coupling strength between links)
- Driving amplitude A and frequency Ω (external forcing)
- Damping coefficient γ

---

## 2 Scope Definition

### Full Scope S_P

```
S_P = (B_P, Π_P, Δ_P, ε_P)
```

**B_P — Boundary Conditions**

- Fixed pivot at top link
- Bounded total energy (E < E_max)
- Passive joint coupling with stiffness κ
- Optional periodic driving with amplitude A, frequency Ω
- Physical realizability: no link overlap

BC class: **coupling + dissipation + optional forcing**

**Π_P — Observables**

```
Π_P = { θ₁(t), θ₂(t), θ̇₁(t), θ̇₂(t) }
```

All degrees of freedom are tracked. Both relative and absolute
motion are distinguishable.

**Δ_P — Admissible Perturbations**

- Small perturbations to initial conditions: δθ < 0.01 rad
- Small perturbations to driving amplitude: δA < 0.05 A
- Measurement noise at physical precision level

**ε_P — Resolution Threshold**

```
ε_P: angular differences < 0.01 rad are indistinguishable
```

---

## 3 Regime Partition under S_P

```
A(S_P) = R_P
```

| Regime | Behavioral signature | Parameter region |
|---|---|---|
| R_P1 — Periodic | Both links oscillate with commensurate frequencies, closed orbits in phase space | Low A, moderate κ |
| R_P2 — Quasi-periodic | Incommensurate frequencies, torus structure in phase space, no chaos | Moderate A, moderate κ |
| R_P3 — Chaotic | Sensitive dependence on initial conditions, positive Lyapunov exponent | High A or low κ |
| R_P4 — Locked | θ₁ ≈ θ₂ throughout — links move as single unit | High κ |

**Structural observation:**
R_P3 (chaos) is formally an ARW **scope-mismatch signal** —
under S_P, chaos indicates that θ̇₁, θ̇₂ are no longer sufficient
to produce a stable partition. The scope has lost ordering dominance
in this region.

R_P4 is the regime that enables the admissible reduction below.

---

## 4 Reduced Scope S_P'

Under high joint stiffness (κ → ∞), θ₁ ≈ θ₂ at all times.
The relative angle becomes dynamically irrelevant — a latent degree of freedom.

A reduced scope becomes admissible:

```
S_P' = (B_P', Π_P', Δ_P', ε_P')
```

**B_P' — Boundary Conditions**

B_P augmented with: **stiff-coupling constraint** θ₁ - θ₂ < δ_stiff

**Π_P' — Observables**

```
Π_P' = { θ_mode(t), θ̇_mode(t) }
```

where θ_mode = (θ₁ + θ₂) / 2 is the collective mode angle.
The relative coordinate θ_rel = θ₁ - θ₂ is suppressed.

**ε_P' — Resolution Threshold**

ε_P' > ε_P — coarser resolution, consistent with fewer observables.

---

## 5 Admissibility Analysis: S_P → S_P'

```
A(S_P') = R_P'
```

Reduced partition:

| Regime | Signature under S_P' |
|---|---|
| R_P'1 — Ordered motion | θ_mode oscillates regularly |
| R_P'2 — Chaotic motion | θ_mode shows sensitive dependence |

**Compatibility check:**

| S_P regime | Maps to S_P' regime | Compatible? |
|---|---|---|
| R_P1 (Periodic) | R_P'1 (Ordered) | ✓ — fully contained |
| R_P4 (Locked) | R_P'1 (Ordered) | ✓ — fully contained |
| R_P2 (Quasi-periodic) | R_P'1 (Ordered) | ✓ under high κ |
| R_P3 (Chaotic) | R_P'2 (Chaotic) | ✓ — fully contained |
| R_P2 (Quasi-periodic) | R_P'1 or R_P'2 | ⚠ κ-dependent |

**Result:** Admissible under high κ, partially inadmissible under moderate κ.

The **admissibility boundary** — the value of κ at which the reduction
becomes inadmissible — is the primary experimental observable.

This boundary is a concrete distortion metric:
at what coupling strength does the reduced scope begin fragmenting
R_P2 across the partition boundary?

---

## 6 Extension: Three-Link System

For a three-link pendulum (θ₁, θ₂, θ₃), two distinct reductions are possible:

**S_P → S_P'(12):** collapse links 1 and 2, keep link 3 explicit
**S_P → S_P'(123):** collapse all three links to single mode

These produce different partitions and different admissibility thresholds,
enabling a systematic study of how **reduction path** affects partition distortion.

---

## 7 Connection to ARW Research Questions

| Research question | Pendulum test |
|---|---|
| Do BC classes generate characteristic regime structures? | Coupling BC generates R_P4 (locked regime) not present without coupling |
| When is scope reduction admissible? | κ-dependent admissibility boundary of S_P → S_P' |
| Can distortion be quantified? | Measure partition compatibility index as function of κ |
| Does chaos signal scope mismatch? | R_P3 appears where S_P loses ordering dominance |

---

## 8 Falsification Conditions

- No stable regime partition emerges under S_P — partitioning pipeline fails
- R_P4 does not appear under high κ — coupling BC does not generate locked regime
- Admissibility boundary is discontinuous or not monotone in κ — reduction criterion is ill-defined
- Chaos in R_P3 is recoverable by S_P without scope change — scope-mismatch interpretation is wrong

---

*For the minimal worked example, see [docs/overview/minimal_example.md](../docs/overview/minimal_example.md).*
*For the admissibility criterion, see [docs/core/arw_scope_reduction_partition_criterion.md](../docs/core/arw_scope_reduction_partition_criterion.md).*
