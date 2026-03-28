---
status: note
layer: docs/notes/
created: "2026-03-28"
---

# Research Assignment: Independent Violation Axes (IVA) and Geometry of Z(π)

## Objective

Refine and validate the Independent Violation Axes (IVA) concept as the primary determinant of the dimensionality and geometry of observable exclusion zones Z(π), replacing BC-count heuristics with a structurally grounded formulation.

---

## Background

Prior work suggested:

dim(Z(π)) ≥ max(0, |BC_active| − 1)

However, counterexamples (e.g. Pitchfork system) show that BC count alone is insufficient.
This motivates a refined formulation based on Independent Violation Axes (IVA).

---

## Core Hypothesis

### H2' — IVA Dimensionality Principle

The dimensionality of Z(π) is given by:

dim(Z(π)) = dim(span(IVA(π)))

Where:

IVA(π) = set of independent parameter-space directions along which distinct pre-scopal assumptions Aᵢ fail.

---

## Research Questions

1. How can IVA(π) be formally derived from A0–A6 decomposition?
2. What conditions guarantee independence of violation axes?
3. How do different BC types (coupling, symmetry, dissipation, restriction) map to IVA?
4. Can Z(π) geometry (point, line, surface) be predicted from IVA structure?

---

## Methodology

### 1. Formalization

- Define IVA(π) rigorously:
  - bᵢ ∈ T_p(P)
  - Aᵢ fails along bᵢ
  - linear independence condition

- Define:
  span(IVA(π)) and its dimension

---

### 2. Case Studies

#### System A: Kuramoto
- Identify IVA:
  - ergodicity collapse at κ_c
- Expected:
  dim(Z) = 0

#### System B: Pitchfork
- Identify IVA:
  - symmetry constraint axis (μ > 0)
- Expected:
  dim(Z) = 1

#### System C: Schools (multi-BC)
- Identify IVA:
  - A5 failure (κ-driven)
  - A6 failure (α-driven)
- Expected:
  dim(Z) = 2

---

### 3. BC-Type Mapping

Classify BC types:

- Coupling → local transition (point-like IVA)
- Symmetry → global constraint (extended IVA)
- Dissipation → drift axis
- Restriction → projection-induced failure

Map each to:
- associated Aᵢ
- expected IVA contribution

---

### 4. Analytical Derivation

For each observable π:

1. Decompose into A0–A6
2. Identify failure conditions
3. Map failure conditions to parameter directions
4. Construct IVA(π)
5. Compute dim(span(IVA(π)))

---

### 5. Validation

- Compare predicted dim(Z(π)) with simulation
- Check:
  - geometric match (point / line / surface)
  - independence of axes
  - robustness under perturbations

---

## Expected Results

- Replacement of BC-count heuristic with IVA-based formulation
- Correct prediction of Z(π) geometry across systems
- Identification of BC-type → IVA mapping
- Generalizable method for predicting observable failure structure

---

## Deliverables

- Formal definition of IVA (repo-ready)
- Case study analyses (Kuramoto, Pitchfork, Schools)
- Z(π) geometry predictions vs. simulation plots
- BC-type classification table
- Markdown + figures

---

## Significance

This work establishes:

- A structural theory of observable failure geometry
- A predictive method for Z(π) dimensionality
- A shift from BC-count to mechanism-based reasoning

---

## Next Steps

- Formal proof of IVA independence conditions
- Extension to composite observables
- Integration into ScopeSpec workflow
