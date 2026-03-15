
# Kuramoto Case Notes

## Case Description

This case studies regime detection in the Kuramoto model using the ARW pipeline concept of **BC-driven perturbations**.

Boundary condition (BC):
κ — coupling strength

Observable:
r_ss — steady-state Kuramoto order parameter

Goal:
Detect regime partitions in κ-space using observable threshold ε.

---

## Experimental Setup

Common κ sweep:

κ ∈ [0,3]

Sweep step:

Δκ = 0.017

Simulation parameters:

- N = 500 oscillators
- T = 200
- dt = 0.05

Observable:

r_ss = mean order parameter in the final 20% of the simulation.

---

## Partition Rule

Regime change detected when

|Π(κᵢ₊₁) − Π(κᵢ)| > ε

with

Π(κ) = r_ss

---

## Results

### ε = 0.05

Regimes: 3

Distribution:

86 | 1 | 90

Transitions:

κ ≈ 1.4535  
κ ≈ 1.4705

Observation:

The intermediate regime is only **one sweep point wide**.

---

### ε = 0.09

Regimes: 2

Distribution:

87 | 90

Transition:

κ ≈ 1.4705

---

## Interpretation

The main synchronization transition appears near

κ ≈ 1.47

At smaller ε the transition region splits into a very narrow pre-transition regime.

This indicates:

- a robust primary regime boundary
- ε-dependent fine structure.

---

## Significance

The Kuramoto model demonstrates that regime partitions depend on:

- BC perturbation size Δκ
- observable resolution ε

Therefore regime maps are **scope dependent descriptions** rather than intrinsic discrete structures.
