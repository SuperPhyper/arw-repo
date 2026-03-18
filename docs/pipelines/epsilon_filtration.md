---
status: working-definition
layer: docs/pipelines/
---

# ε-Filtration Pipeline for BC-Regime Analysis

## Purpose

This document describes the **ε-filtration pipeline** used to analyze
observable regime structure across boundary-condition (BC) parameter spaces.

The method detects regions where observable behavior remains stable
under changes of BC resolution.

It produces three main diagnostics:

- **height fields**
- **entry scales**
- **persistence width**

These quantities identify robust regimes and sensitive transition zones.

---

# Relation to ARW

The pipeline operates on a scope

S = (B, Π, Δ, ε)

where:

| component | role in the pipeline |
|---|---|
| **B** | BC parameter space (e.g. κ, σ) |
| **Π** | observable projection O = π(x) |
| **Δ** | admissible perturbations; here instantiated as BC-induced variation along sweep |
| **ε** | BC resolution scale |

---

# Pipeline Overview

Input:

- BC sweep data
- observable values

Example:

(kappa, sigma) -> observable

Output:

- height fields
- persistence intervals
- regime structure plots

---

# Steps

1. Define BC grid
2. Compute observable field
3. Define ε scales
4. Evaluate indistinguishability
5. Compute membership
6. Aggregate height
7. Extract entry/leave
8. Compute persistence width

---

# Interpretation

ε-filtration acts as BC coarse-graining.

Persistent regions = stable regimes  
Low persistence = transitions

---

# Status

working-definition
