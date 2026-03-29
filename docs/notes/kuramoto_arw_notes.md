---
status: note
layer: docs/notes/
---


# Kuramoto BC‑Perturbation Study Notes

## Context

Goal: explore how regime partitions in a Kuramoto system depend on

- boundary condition parameter κ (coupling strength)
- observable resolution ε
- BC perturbation size Δκ

The work was motivated by the ARW pipeline idea:

- regimes are detected through **BC‑based perturbations**
- perturbations originate from the **boundary condition under investigation**
- ε determines the **observable distinguishability threshold**
- Δκ determines the **minimum BC perturbation applied**

Therefore:

Δκ acts as the **lower bound of detectable partitioning**.

---

# Core Methodological Principles

## 1. Perturbations originate from the BC

For Kuramoto:

κ → κ + δκ

Not:

state → state + δ

This means perturbations are **structural variations of the BC**.

---

## 2. ε determines observable resolution

Partition rule:

|Π(κᵢ₊₁) − Π(κᵢ)| > ε

where

Π(κ) = observable (here steady state order parameter r_ss).

ε defines **how much observable difference counts as a regime change**.

---

## 3. Δκ limits the smallest detectable regime

If Δκ is too large, narrow regimes cannot be detected.

Therefore:

Δκ ≤ smallest regime width we want to detect.

For comparisons across ε:

**Δκ must be fixed** and chosen based on the **finest ε case**.

---

# Experimental Design Used

A common sweep was performed:

κ ∈ [0,3]

with

Δκ = 0.017

This was chosen to support ε = 0.05.

Number of sweep points:

177

Simulation parameters:

- N = 500 oscillators
- T = 200
- dt = 0.05

Observable:

r_ss = mean order parameter in final 20% of simulation.

---

# Partition Results

## ε = 0.05

Regimes: 3

Distribution:

86 | 1 | 90

Transitions:

κ ≈ 1.4535  
κ ≈ 1.4705

Observation:

The middle regime is **only one sweep point wide**.

---

## ε = 0.09

Regimes: 2

Distribution:

87 | 90

Transition:

κ ≈ 1.4705

---

# Key Observations

1. The **main synchronization boundary** appears stable near

κ ≈ 1.47

2. At smaller ε the transition region splits into sub‑structure.

3. The additional regime detected at ε = 0.05 is extremely narrow.

4. Kuramoto partitions are therefore **strongly resolution dependent**.

---

# Important Interpretation

The Kuramoto order parameter varies smoothly with κ.

Therefore regime partitions are not intrinsic discrete objects but emerge from:

- BC resolution Δκ
- observable threshold ε

This implies:

Regime maps are **scope‑dependent descriptions**.

---

# Major Insight

Kuramoto is an excellent test system because it shows:

continuous observable dynamics

but

discrete regime maps produced by measurement choices.

This highlights the ARW question:

Which regime structures are **robust under scope changes**?

---

# Open Questions

## 1. Robustness of the pre‑transition regime

Is the tiny regime at ε = 0.05 a real structure or a discretization artifact?

Tests:

- local high‑resolution sweep around κ ∈ [1.43,1.49]
- ensemble runs with multiple seeds

---

## 2. Dependence on oscillator population size

Kuramoto transitions sharpen as N increases.

Question:

How does regime partitioning behave under

N sweep?

Possible study:

R(κ, ε, N)

---

## 3. BC‑resolution vs observable resolution

The relation between

Δκ and ε

needs formal constraints.

Possible condition:

Δκ ≤ ε / max(|dΠ/dκ|)

to ensure transitions cannot be skipped.

---

## 4. Regime hierarchy

Small ε splits larger regimes.

This suggests a **regime tree** similar to hierarchical clustering.

Possible representation:

ε → regime merge tree.

---

## 5. ARW interpretation

Key conceptual question:

Are regimes properties of the system

or

properties of the scope?

Kuramoto suggests:

they are **joint products of dynamics and measurement resolution**.

---

# Potential Next Experiments

1. Local high‑resolution sweep near the transition.
2. Ensemble simulations to estimate observable variance.
3. N scaling study.
4. Regime hierarchy construction across ε.
5. 2D regime map R(κ, ε).

---

# Relevance for ARW

This case illustrates:

- BC‑driven perturbation experiments
- scope‑dependent regime detection
- robustness analysis across ε

The Kuramoto model therefore provides a clean sandbox for testing ARW regime concepts.
