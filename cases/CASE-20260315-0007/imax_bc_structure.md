---
status: working-definition
layer: cases/CASE-20260315-0007/
date: 2026-06-02
related_cases: [CASE-20260315-0007, CASE-20260311-0001]
---

# I_peak Observable BC Structure — CASE-20260315-0007

## Purpose

Formal characterisation of the BC structure of I_peak = max_t I(t)/N (peak infected
fraction) for CASE-20260315-0007 (SIR epidemic model). Required for Controls C1 and C3
of the pre-registered transfer experiment transfer_test_0001_0007_aggregation/.

---

## Observable Definition

I_peak = max_{t in [0, T]} I(t)

where I(t) is the infected fraction from the ODE:
  dI/dt = beta * S * I - gamma_r * I

- Domain: full trajectory in [0,1]^3, S+I+R=1
- Codomain: [0, 1]
- Sub-threshold (beta < beta*=0.101): I_peak ~= I(0) = 0.01
- Super-threshold (beta > beta*): I_peak grows to ~0.48 at beta=0.5

---

## Pre-Scopal Substrate Analysis (A0-A6)

| Substrate | Requirement | Status for I_peak | Notes |
|-----------|-------------|-------------------|-------|
| A0 | State well-defined | satisfied | (S,I,R) in [0,1]^3 with S+I+R=1 |
| A1 | Topology/continuity | satisfied | I(t) is a smooth ODE solution |
| A2 | Stationarity | satisfied | Deterministic ODE with unique trajectory per beta |
| A3 | Ergodicity | satisfied | Deterministic system; time-max is well-defined |
| A4 | Differentiability | satisfied | I(t) differentiable (RK4 ODE) |
| A5 | Observability | satisfied | I_peak is a well-defined real-valued functional |
| A6 | Reference frame independence | satisfied | I is a population fraction — dimensionless, reference-independent |

No Z_shared exclusion zone applies: the SIR model is deterministic and I_peak is
a global max over the full trajectory (not a steady-state measure), so critical
slowing at beta* does not affect the observable's well-definedness.

---

## Primitive Operator Decomposition

### A — Aggregation (PRIMARY, LEVEL 1): SIR quotient projection

The SIR model itself is the first Aggregation operator. It is the quotient projection:

  pi_SIR: {0,1,2}^N -> [0,1]^3
  pi_SIR(x_1,...,x_N) = (|{i: x_i=0}|/N, |{i: x_i=1}|/N, |{i: x_i=2}|/N)

This is the canonical S1-quotient (Aggregation BC): it identifies all micro-states
with the same macro-compartment counts as equivalent. I_peak is computed ON this
already-aggregated description. The Aggregation BC is constitutive to the observable
domain.

### A — Aggregation (SECONDARY, LEVEL 2): temporal maximum

I_peak = max_t I(t) applies a second aggregation: the temporal maximum over the
full trajectory. This selects the extreme value from the time-series of the
(already aggregated) infected fraction. The max operation is a non-linear
aggregation over time.

Two aggregation levels are thus structurally present:
1. A1: Population-level quotient (SIR projection from N individuals)
2. A2: Temporal maximum (max over trajectory)

### R — Restriction (TERTIARY): simplex constraint

The state space is restricted to the 2-simplex S+I+R=1. This Restriction BC
confines the domain on which I_peak is measured. It is a precondition for the
SIR model (the admissibility constraint), not a driver of I_peak's information.

### S — No symmetry

I_peak has no special symmetry structure. It is a scalar value with no invariance
group beyond dimensional consistency.

---

## BC Structure Notation

**I_peak: A² . R**

- A² (double Aggregation): constitutive (SIR quotient) + temporal max
- R (Restriction): simplex constraint as precondition

---

## Contrast with r_ss and PLV

| Property | I_peak (CASE-0007) | PLV (CASE-0004) | r_ss (CASE-0001) |
|----------|--------------------|-----------------|-----------------|
| System BC class | Aggregation | Coupling | Coupling |
| Observable BC structure | A² . R | C . A . R | R³ . A . D |
| Primary operator | Aggregation | Coupling | Restriction |
| Type | Population fraction max | Inter-oscillator coherence | Mean-field order param |
| Aggregation level | 2 (quotient + temporal max) | 1 (temporal mean) | 1 (spatial mean) |

I_peak and r_ss both involve Aggregation (temporal averaging/extremum), but:
- r_ss is Restriction-dominated (measures mean-field attraction = Restriction effect)
- I_peak is Aggregation-dominated (measures the quotient projection effect directly)

This BC structure mismatch compounds the system-level BC class mismatch
(Aggregation vs Coupling), providing two independent reasons for low Phi in
the CASE-0007 ↔ CASE-0001 transfer test.

---

## Implications for Transfer

The expected low Phi (registered prediction: Phi_matched <= 0.70) is supported by:

1. **System BC mismatch:** Aggregation (S1-quotient) vs Coupling (S2-cross-term)
   — different primitive operators at the highest level of the hierarchy.

2. **Observable BC mismatch:** A².R vs R³.A.D — different primary operators.

3. **Structural difference:** N=2 (SIR) vs N=4 (Kuramoto at eps=0.09) — RCD=2.

4. **TBS_norm difference:** theta*_A/range_A = 0.20/0.50 = 0.400 vs
   theta*_B/range_B = 1.475/3.0 = 0.492 — TBS_norm = 0.092 (moderate).

All four sources of dissimilarity predict reduced Phi relative to the
CASE-0004 ↔ CASE-0001 same-BC-class result (Phi=0.9983).
