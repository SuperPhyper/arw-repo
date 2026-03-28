---
status: working-definition
layer: docs/advanced/
created: "2026-03-28"
tags: [IVA, Z-pi, H2-prime, theorem, observable-failure, geometry]
---

# Independent Violation Axes (IVA) and the Geometry of Z(π)

**ARW Level:** ARW (domain-neutral formalism)
**Supersedes:** H2 (BC-count heuristic) from `docs/advanced/extended_z_observable_necessity.md`
**Repo placement:** `docs/advanced/iva_z_geometry.md`
**Glossary entries:** `docs/glossary/independent_violation_axes.md`

---

## 1. Motivation: Why BC-Count Is Insufficient

The previous study (H2) proposed:

```
dim(Z(π)) ≥ max(0, |BC_active| − 1)
```

The Pitchfork normal form (CASE-0008) falsifies this as an exact statement:
with n_BC = 1 (Symmetry Breaking), dim(Z(⟨x⟩)) = 1, not 0.
The formula predicts max(0, 1−1) = 0 — incorrect.

**Root cause:** BC count conflates two distinct structural properties:
1. *How many* BC classes are active
2. *Which pre-scopal assumptions* each BC class violates, and along *which
   independent parameter directions*

The Pitchfork shows that a single Symmetry Breaking BC can violate A1
(reference uniqueness) along an entire half-line, not merely at a critical point.
The geometry of Z(π) depends on the *type* and *extent* of assumption violation,
not on the count of BC classes.

**H2' replaces H2:**

```
dim(Z(π)) = dim(span(IVA(π)))
```

where IVA(π) is the set of Independent Violation Axes — formally defined below.

---

## 2. Formal Definitions

### 2.1 Parameter Space and Tangent Vectors

Let P be the parameter space of the system (dim d ≥ 1).
Let p ∈ P be a parameter point. The tangent space T_p(P) ≅ R^d carries
unit vectors representing directions of parameter variation.

### 2.2 Assumption Failure Function

For each pre-scopal assumption Aᵢ (i = 0,...,6) and observable π, define:

```
φᵢ: P → [0,1]       (failure intensity of Aᵢ at parameter point p)
φᵢ(p) = 0  ↔  Aᵢ robust at p
φᵢ(p) = 1  ↔  Aᵢ collapses at p
```

The exclusion zone Z(π) is:

```
Z(π) = { p ∈ P | ∃ i : φᵢ(p) > φ_threshold }
```

for some threshold φ_threshold ∈ (0,1) (structural choice, typically 0.25).

### 2.3 Violation Direction

For assumption Aᵢ, a **violation direction** is a unit vector bᵢ ∈ T_p(P) such that:

```
d/dt φᵢ(p + t·bᵢ) |_{t=0}  >  0
```

i.e., φᵢ increases when moving along bᵢ from p. The violation direction points
into the region where Aᵢ is increasingly violated.

### 2.4 Violation Axis (single assumption)

A **violation axis** for Aᵢ is the full line (or ray) through p along bᵢ:

```
VA(Aᵢ, p) = { p + t·bᵢ | t ∈ T }
```

where T = R (full axis), T = [0,∞) (half-line), or T = [0, t_max] (segment),
depending on the failure type:

| Failure type | T | Example |
|---|---|---|
| point | {0} | A3 ergodicity at κ_c (Kuramoto) |
| segment | [0, t_max] | A5 reference above κ_F0 (Schools) |
| half_line | [0, ∞) | A1 symmetry in μ > 0 (Pitchfork) |
| global | R | A0 state space undefined everywhere |

### 2.5 Independent Violation Axes IVA(π)

The **Independent Violation Axes** of observable π is the maximal linearly
independent subset of violation axes across all failing assumptions:

```
IVA(π) = { b₁, b₂, ..., bₖ } ⊆ T_p(P)

such that:
  (i)  For each bᵢ: ∃ Aⱼ s.t. bᵢ is a violation direction for Aⱼ at some p ∈ Z(π)
  (ii) The set {b₁,...,bₖ} is linearly independent in T_p(P)
  (iii) k is maximal (no additional violation direction can be added while preserving independence)
```

### 2.6 Theorem H2' — IVA Dimensionality Principle

**Theorem (candidate):**

For any observable π of class E (stationary expectations), its exclusion zone
satisfies:

```
dim(Z(π)) = dim(span(IVA(π)))
```

**Interpretation:** The dimensionality of the failure region equals the rank of
the matrix formed by the independent violation direction vectors — a structural
property derivable analytically from the A0–A6 substrate decomposition.

**Proof sketch:**

1. Z(π) is defined by the conjunction of failure conditions for all violated Aᵢ.
   Each failure condition φᵢ(p) > threshold defines a hypersurface in P.

2. The intersection of k hypersurfaces in R^d has codimension k generically,
   hence dimension d − k.

3. However, when failure types are half-line or region (not point), the failure
   condition is an inequality over an extended region, not an equality on a surface.
   This shifts codimension: a half-line condition in 1D has codimension 0 (measure
   non-zero), giving effective dim = 1.

4. The effective dimension is therefore:
   ```
   dim(Z(π)) = dim(span{bᵢ : failure_type ≠ point})
               + #{bᵢ : failure_type = point and independent} × 0
   ```
   Point-type failures contribute measure-zero sets (dim 0) in the span.

5. span(IVA(π)) captures the subspace spanned by all violation directions —
   its rank equals the number of independent extended failure conditions, which
   equals dim(Z(π)). □

**Status:** Theorem-candidate. Requires:
- Formal proof that hypersurface intersection formula applies to φᵢ as defined
- Treatment of non-generic cases (degenerate failure conditions)
- Extension to composite observables (non-E class)

---

## 3. Case Study Derivations

### 3.1 Kuramoto — Coupling BC

**Observable:** r_ss = |E[e^{iθ}]|  (class E)

**A0–A6 decomposition:**

| Assumption | Status in R(π) | Status at κ_c | Violation type |
|---|---|---|---|
| A0 State space (T^N) | robust | robust | — |
| A1 Group structure (S¹) | robust | robust | — |
| A2 Stationary measure | robust | fragile | — |
| A3 Ergodicity | robust | **collapses** | — |
| A4 T convergence | robust | fragile | — |
| A5 Reference (r₀=0) | robust | partially | — |
| A6 Stationarity | robust | fragile | — |

**Failure condition:** A3 collapses at κ = κ_c (phase transition).
Not for κ < κ_c or κ > κ_c — only at the critical point.

**Violation direction:**
```
b₁ = ê_κ = [1]    (unit vector along κ)
failure_type = point   (only at κ_c, not extended)
```

**IVA(r_ss) = { b₁ }** with failure_type = point

**dim(span(IVA)) = 1** but failure_type = point → **effective dim(Z) = 0**

The span is 1D but the failure set is measure-zero (a single point).
H2' refinement: point-type failures contribute 0 to effective dim(Z).

**Z(r_ss) = { κ_c }** — confirmed by simulation. ✓

---

### 3.2 Pitchfork Normal Form — Symmetry Breaking BC

**Observable:** ⟨x⟩ = E[x]  (class E)

**A0–A6 decomposition:**

| Assumption | Status μ < 0 | Status μ > 0 | Violation type |
|---|---|---|---|
| A0 State space R¹ | robust | robust | — |
| A1 Reference uniqueness | robust | **collapses** | — |
| A2 Symmetric measure | robust | robust | — |
| A3 Ergodicity | robust | robust | — |
| A4 T convergence | robust | robust | — |
| A5 Reference (x₀ = ?) | robust | **collapses** | — |
| A6 Stationarity | robust | robust | — |

**Failure condition:** A1 collapses for ALL μ > 0.
The Z₂ symmetry (x → −x) forces P_stat(x) = P_stat(−x), hence E[x] = 0
regardless of which attractor the system visits. This is not a sampling
issue — it is enforced by the symmetry structure of the broken phase.

The failure is not at a point (μ = μ_c) but over a half-line (μ > 0).

**Violation direction:**
```
b₁ = ê_μ = [1]    (unit vector along μ)
failure_type = half_line   (μ > 0, semi-infinite)
```

**IVA(⟨x⟩) = { b₁ }** with failure_type = half_line

**dim(span(IVA)) = 1** and failure_type = half_line → **effective dim(Z) = 1**

**Z(⟨x⟩) = { μ > 0 }** — confirmed by simulation. ✓

**Key insight:** Same n_IVA = 1 as Kuramoto, but different failure_type
produces different dim(Z). BC count is irrelevant — failure type determines geometry.

---

### 3.3 German Schools — Multi-BC (Restriction + Forcing + Coupling + Dissipation)

**Observable:** subject_score ≈ E[grade | curriculum_reference]  (class E)

**A0–A6 decomposition:**

| Assumption | Failure condition | Parameter axis | Failure type |
|---|---|---|---|
| A0–A2 | robust throughout | — | — |
| A3 Ergodicity | fragile at θ*_3 | λ_T axis | point? |
| A4 T convergence | partially at high κ | κ axis | segment |
| **A5 Reference stability** | **collapses: κ > 0.58** | **κ axis** | **region** |
| **A6 Stationarity** | **collapses: α < 0.75** | **α axis** | **region** |

**Two independent failure axes:**

```
b₁ = ê_κ = [1, 0]     A5 fails along κ (curriculum reference instability)
            failure_type = region  (κ > κ_F0 = 0.58)

b₂ = ê_α = [0, 1]     A6 fails along α (attendance-driven non-stationarity)
            failure_type = region  (α < α_F0 = 0.75, i.e. 1−α > 0.25)
```

**Independence check:**
```
b₁ · b₂ = [1,0] · [0,1] = 0    (orthogonal → linearly independent ✓)
rank([b₁; b₂]) = rank([[1,0],[0,1]]) = 2 ✓
```

**IVA(subject_score) = { b₁, b₂ }** with both failure_type = region

**dim(span(IVA)) = 2** → **effective dim(Z) = 2**

**Z(subject_score) ≈ { (κ,α) | κ > 0.58 AND α < 0.75 }**

This is a 2D rectangular region in (κ,α) space, covering ~38% of the
policy-relevant parameter rectangle. Confirmed by simulation. ✓

---

## 4. BC-Type → IVA Mapping (all 6 BC classes)

This table maps each BC class to its characteristic IVA structure.
Two classes (Coupling, Symmetry Breaking) are formally derived.
Four remain empirically open.

| BC Class | Primary Aᵢ violated | Violation condition | Failure type | dim contrib. | Status |
|---|---|---|---|---|---|
| **Coupling** | A3: ergodicity | κ → κ_c (critical transition) | **point** | 0 | Formally derived |
| **Symmetry Breaking** | A1: reference uniqueness | μ > μ_c (broken phase) | **half_line** | 1 | Formally derived |
| Restriction | A5: reference stability | κ > κ_F0 (composition shift) | region? | 1? | Empirically observed |
| Forcing | A6: stationarity | ω·λ_T > threshold | region? | 1? | Hypothesized |
| Dissipation | A4+A6: convergence+stationarity | burnout → 1 (asymptotic) | half_line? | 1? | Hypothesized |
| Aggregation | A2: measure validity | N → 0 (sample collapse) | point? | 0? | Hypothesized |

**Formally derived structures:**

- **Coupling → point:** Phase transitions are by definition parameter-specific.
  A3 (ergodicity) fails at κ_c, not in a neighbourhood. The IVA direction exists
  but has measure-zero failure type.

- **Symmetry Breaking → half_line:** The broken-symmetry phase is not a
  neighbourhood of μ_c — it is the entire region μ > μ_c. The symmetry constraint
  persists and extends. This is a structural property of Z₂-broken systems,
  not specific to the Pitchfork.

**Open questions for remaining BC classes:**

| ID | Question |
|---|---|
| Q-IVA-01 | Does Restriction always generate a region-type failure, or can it be point-like when the curriculum change is abrupt (step function κ)? |
| Q-IVA-02 | Does Dissipation generate a half_line (asymptotic attractor → burnout phase persists) or a segment (finite recovery possible)? |
| Q-IVA-03 | Is Forcing's IVA along the ω axis (frequency) or the λ_T axis (amplitude)? Are these independent? |
| Q-IVA-04 | Does Aggregation generate point-like failure (only at N=0) or segment (finite-N effects)? |

---

## 5. Simulation Evidence

### Figure 1 — Z(π) Geometry: Prediction vs. Simulation

![Fig 1](figures/fig_iva1_geometry.png)

Three rows, three columns (IVA diagram / simulation / summary):

**Kuramoto:** IVA diagram shows single violation arrow at κ_c. Simulation
confirms narrow Z(π) peak. H2' prediction: dim=0. Confirmed. ✓

**Pitchfork:** IVA diagram shows half-line arrow from μ=0 to +∞.
Simulation confirms F0 proxy rises at μ=0 and remains elevated throughout
μ > 0. H2' prediction: dim=1. Confirmed. ✓

**Schools:** IVA diagram shows two orthogonal arrows (b₁ along κ, b₂ along α).
Simulation 2D heatmap shows extended region in lower-right (κ, α) quadrant.
F0 boundary (white contour) matches the predicted rectangle. H2' prediction:
dim=2. Confirmed. ✓

### Figure 2 — BC-Type → IVA Mapping Table

![Fig 2](figures/fig_iva2_bc_mapping.png)

All six BC classes with assumption, violation condition, direction, failure type,
dim contribution, and derivation status. Green = formally derived; yellow = open.

### Figure 3 — H2' Theorem Validation

![Fig 3](figures/fig_iva3_h2prime.png)

Three panels — one per system — overlaying analytical prediction (IVA-derived
geometry) on simulated Z(π) distribution:

- Kuramoto: vertical line at κ_c overlaps simulation peak. ✓
- Pitchfork: half-line shading covers entire simulated F0 region. ✓
- Schools: 2D rectangle (b₁ × b₂ onset) overlaps simulated 2D heatmap contour. ✓

---

## 6. Refined Theorem H2' (Full Statement)

**Definition (effective dimension):**
```
dim_eff(Z(π)) = dim(span{ bᵢ ∈ IVA(π) | failure_type(bᵢ) ≠ point })
```

Point-type failure axes are excluded because they generate measure-zero
sets that do not contribute to the dimension of the failure region.

**Theorem H2' (IVA Dimensionality Principle):**

For any observable π of class E with IVA(π) = {b₁,...,bₖ}:

```
dim(Z(π)) = dim_eff(Z(π))
           = dim(span{ bᵢ | failure_type(bᵢ) ∈ {segment, half_line, region, global} })
```

**Corollaries:**

*C1 (Coupling BC):*
If the only active BC class is Coupling, then IVA contains only point-type
violation axes (ergodicity at κ_c), so dim(Z) = 0.

*C2 (Symmetry Breaking BC):*
If Symmetry Breaking is active, IVA contains at least one half_line-type axis
(broken symmetry phase persists), so dim(Z) ≥ 1.

*C3 (Multi-BC with independent extended failures):*
If n BC classes generate n linearly independent extended (non-point) failure
axes, then dim(Z) = n.

*C4 (Observable class necessity — refined):*
For any system with dim(Z(π)) ≥ 1 for all π ∈ E, there must exist π' ∉ E
with Z(π') ∩ Z_E = ∅ for full parameter-space observability.

**Status:** Theorem-candidate. Proof sketch provided. Formal proof requires:
- Measure theory on failure sets (Lebesgue measure of Z(π))
- Genericity argument for hypersurface intersections
- Treatment of non-smooth φᵢ (sigmoid approximations vs. sharp thresholds)

---

## 7. Implications for ScopeSpec Workflow

H2' enables a **predictive pre-pipeline step** for observable failure analysis:

```
Step 1: Decompose π into A0–A6 substrate
Step 2: For each Aᵢ that fails: identify violation direction bᵢ and failure_type
Step 3: Compute IVA(π) = maximal independent subset of {bᵢ}
Step 4: Compute dim(Z(π)) = dim_eff(span(IVA(π)))
Step 5: If dim(Z(π)) ≥ 1: flag π as class-E insufficient in Z(π)
         → add alternative (non-E) observable to Π block
Step 6: Design sweep to include at least dim(Z(π)) independent sweep dimensions
```

This replaces the current empirical F0 detection (post-hoc, simulation-based)
with an analytical pre-sweep derivation. For social systems where empirical data
is expensive to collect, this is the critical practical contribution.

---

## 8. Open Questions

| ID | Question | Priority |
|---|---|---|
| Q-IVA-01 | Restriction BC failure type: region or point? Depends on κ continuity. | high |
| Q-IVA-02 | Dissipation BC: half_line (asymptotic) or segment (finite recovery)? | high |
| Q-IVA-03 | Forcing BC: IVA along ω or λ_T? Independent? | medium |
| Q-IVA-04 | Aggregation BC: point or segment? N-dependence structure? | medium |
| Q-IVA-05 | Do non-E observables (fluctuation class) have their own IVA? | high |
| Q-IVA-06 | Composite observables (E ∘ non-E): how does IVA compose? | medium |
| Q-IVA-07 | Can IVA axes be non-orthogonal and still independent? Does angle between axes affect Z(π) shape? | low |

---

## 9. Glossary Entry (draft)

### `independent_violation_axes`

**Status:** working-definition  
**Layer:** docs/glossary/  
**File:** `docs/glossary/independent_violation_axes.md`

---
**Definition:**

Let π be an observable with pre-scopal substrate assumptions {A₀,...,A₆}.
For each assumption Aᵢ that fails within some region of parameter space P,
let bᵢ ∈ T(P) be the unit vector along which Aᵢ's failure intensity φᵢ increases.

The **Independent Violation Axes** of π is the maximal linearly independent
subset of these violation directions:

```
IVA(π) = maximal { bᵢ : bᵢ violation direction for Aᵢ }  s.t.  rank({bᵢ}) = |IVA(π)|
```

Each element bᵢ carries a **failure type** attribute:
- `point`: failure at a single parameter value (measure zero)
- `segment`: failure over a bounded interval
- `half_line`: failure over a semi-infinite ray
- `region`: failure over a multi-dimensional connected region
- `global`: failure everywhere in P

**The dimensionality theorem (H2'):**

```
dim(Z(π)) = dim(span{ bᵢ ∈ IVA(π) | failure_type(bᵢ) ≠ point })
```

**Known IVA structures (derived):**

| System | Observable | IVA | failure_type | dim(Z) |
|---|---|---|---|---|
| Kuramoto | r_ss | {ê_κ} | point | 0 |
| Pitchfork | ⟨x⟩ | {ê_μ} | half_line | 1 |
| Schools | subject_score | {ê_κ, ê_α} | region × region | 2 |

**Repo placement:** `docs/glossary/independent_violation_axes.md`  
**See also:** `observable_range.md`, `z_dimensionality.md`, `observable_class_E.md`

---

## 10. Repo Placement

```
docs/advanced/
└── iva_z_geometry.md              ← this document

docs/glossary/
├── independent_violation_axes.md  ← formal definition (Section 9)
├── z_dimensionality.md            ← updated with H2' reference
└── observable_class_E.md          ← cross-reference

docs/notes/research_journal.md
└── Session 2026-03-28: IVA formalism, H2' theorem — replaces H2

docs/notes/open_questions.md
└── Q-IVA-01 through Q-IVA-07
```
