---
status: working-definition
---

# ART Instantiation: Kuramoto Oscillators
## Coupled Oscillator Synchronization as Regime Calibration System

This document defines the ART scope for the Kuramoto oscillator experiment.
This system serves as the primary **calibration system** for Phase 1 of the
research program: its regime structure is analytically well-understood,
making it ideal for validating the partition extraction pipeline before
applying it to more complex systems.

---

## 1 System Description

**Domain:** Coupled nonlinear oscillators (physics / dynamical systems)

**Why this system:**
The Kuramoto model has a known, analytically derived phase transition
between incoherence and synchronization. This makes it possible to
verify that the ARW partition extraction pipeline recovers the correct
regime structure before applying it to systems where ground truth is unknown.

**State space X:**
A state x ∈ X is a snapshot of N oscillators:

```
x = (θ₁, θ₂, ..., θ_N, ω₁, ω₂, ..., ω_N)
```

where θᵢ ∈ [0, 2π) is the phase of oscillator i
and ωᵢ is its natural frequency drawn from a distribution g(ω).

**Key control parameter:**
Coupling strength K — the single parameter that drives regime transitions.

---

## 2 Scope Definition

### Primary Scope S_K

```
S_K = (B_K, Π_K, Δ_K, ε_K)
```

**B_K — Boundary Conditions**

- N oscillators with fixed natural frequencies ωᵢ ~ g(ω) (unimodal, symmetric)
- Global all-to-all coupling with uniform strength K
- Thermodynamic limit approximation (N large)
- No external forcing

The critical boundary condition is the **coupling class**: uniform all-to-all
coupling is a specific BC that generates a characteristic regime structure.
Changing this BC class (e.g., to network-structured coupling) changes the
regime partition — this is explicitly tested in the scope variation below.

**Π_K — Observables**

```
Π_K = { r(t), ψ(t) }
```

where the **order parameter** r(t) ∈ [0,1] measures global synchronization:

```
r(t) · e^{iψ(t)} = (1/N) Σ e^{iθⱼ(t)}
```

r ≈ 0: incoherent (phases uniformly distributed)
r ≈ 1: fully synchronized (phases locked)

Individual phase trajectories θᵢ(t) are below resolution at this scope.

**Δ_K — Admissible Perturbations**

- Small perturbations to initial phase configuration (δθ < 0.1 rad)
- Small perturbations to natural frequencies (δω < 0.05 σ_g)
- Finite-N fluctuations (1/√N corrections)

**ε_K — Resolution Threshold**

```
ε_K: Δr < 0.05
```

Order parameter differences smaller than 0.05 are indistinguishable.
Individual oscillator behavior is below resolution.

---

## 3 Regime Partition under S_K

```
A(S_K) = R_K
```

The induced partition contains three regime classes:

| Regime | Order parameter signature | Coupling range |
|---|---|---|
| R_K1 — Incoherent | r ≈ 0, fluctuating | K < K_c |
| R_K2 — Partially synchronized | 0 < r < 1, stable | K_c ≤ K < K_sat |
| R_K3 — Fully synchronized | r ≈ 1, stable | K ≥ K_sat |

**Critical value:**
```
K_c = 2 / (π · g(0))
```

This is analytically derived — the ARW pipeline must recover this boundary.

**Structural observation:**
The transition R_K1 → R_K2 is a **continuous bifurcation** (second-order).
The transition R_K2 → R_K3 is gradual — no sharp boundary exists,
it depends on ε_K.
This is a test case for how ε determines partition granularity.

---

## 4 Scope Variation: Network Coupling S_K'

To test the BC taxonomy hypothesis (*similar BC classes → similar regime structures*),
we compare uniform coupling with network-structured coupling.

```
S_K' = (B_K', Π_K, Δ_K, ε_K)
```

Only B changes — the coupling topology shifts from all-to-all to a
sparse random network (Erdős–Rényi, mean degree ⟨k⟩).

**Expected partition shift:**

| Regime | S_K (uniform) | S_K' (network) |
|---|---|---|
| Incoherent | R_K1 | R_K'1 (broader) |
| Partial sync | R_K2 | R_K'2 (fragmented into clusters) |
| Full sync | R_K3 | R_K'3 (harder to reach, higher K required) |

R_K2 splits into multiple cluster-synchronization regimes under S_K'.
This is a **partition refinement** — the network scope reveals structure
invisible under uniform coupling.

**Admissibility check S_K → S_K':**

The reduction from network to uniform coupling is admissible only if
cluster regimes can be merged into R_K2 without cross-cutting existing
class boundaries. This is testable and expected to **fail partially** —
the cluster structure in R_K'2 cannot be recovered from R_K2.

---

## 5 Cross-Scope Comparison: S_K vs. Mean-Field S_MF

The Kuramoto model has an exact mean-field description in the N → ∞ limit.

```
S_MF = (B_MF, Π_MF, Δ_MF, ε_MF)
```

where Π_MF = {r(t)} only (ψ is suppressed), and B_MF assumes
the thermodynamic limit.

**Admissibility of S_K → S_MF:**

For large N, the reduction is admissible — R_K maps cleanly onto R_MF.
For small N, the reduction is inadmissible — finite-size fluctuations
create regime ambiguity near K_c that S_MF cannot capture.

This provides a **quantitative admissibility test**: at what N does
the reduction become inadmissible? This is the first concrete
distortion metric the pipeline must compute.

---

## 6 Distortion Metrics

The Kuramoto system is used to calibrate the following metrics:

| Metric | Definition | Expected result |
|---|---|---|
| Boundary shift | |K_c(S_K) - K_c(S_MF)| as function of N | → 0 as N → ∞ |
| Regime count difference | |R_K| - |R_MF| | 0 for large N, >0 for small N |
| Partition compatibility index | Fraction of R_K classes cleanly contained in R_MF classes | < 1 near K_c for small N |

---

## 7 Falsification Conditions

- ARW pipeline fails to recover K_c analytically — partition extraction is broken
- Network coupling produces no cluster-regime structure — BC taxonomy is wrong
- Finite-N reduction is always admissible — distortion metrics are insensitive
- Regime boundaries are continuous everywhere — ε has no effect on partition structure

---

*For the formal admissibility criterion, see [docs/core/arw_scope_reduction_partition_criterion.md](../docs/core/arw_scope_reduction_partition_criterion.md).*
*For BC taxonomy, see [docs/bc_taxonomy/boundary_condition_classes.md](../docs/bc_taxonomy/boundary_condition_classes.md).*
