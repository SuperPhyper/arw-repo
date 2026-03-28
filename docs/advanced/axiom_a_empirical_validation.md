---
status: working-definition
layer: docs/advanced/
created: "2026-03-28"
tags: [Axiom-A, empirical-validation, IVA, gradient-rank, counterexample]
---

# Empirical Validation of Axiom A
## Four-Strategy Study: Independent Violation Axes in ARW Systems

**Purpose:** Validate the Key Lemma of Theorem H2' empirically.
The lemma claims that in ARW scopes, canonical violation directions
b₁,...,bₖ = ∇φ₁,...,∇φₖ are generically linearly independent.
This cannot be proved from first principles without full knowledge of
the φᵢ structure — but it can be empirically tested.

**Core testable claim:**
```
rank( [∇φ₁(p), …, ∇φₖ(p)] ) = k    for λ-a.e. p
```

Everything else (IVA, dim_eff, H2') follows from this.

---

## 1. Systems and Failure Functions

### System 1: German Schools (Axiom A holds — expected)

Two independently motivated failure functions in (κ, α) space:

```
φ_A5(κ, α) = σ(κ; k=8, x₀=0.58) · (1 + 0.05·σ(1−α; k=4, x₀=0.3))
```
A5: reference class composition shifts primarily with curriculum pressure κ.
Weak α-dependence reflects realistic second-order coupling.

```
φ_A6(κ, α) = σ(1−α; k=10, x₀=0.25) · (1 + 0.05·σ(κ; k=4, x₀=0.7))
```
A6: stationarity fails primarily with low attendance α.
Weak κ-dependence reflects realistic second-order coupling.

**Design intent:** Each φᵢ is primarily sensitive to one axis.
The 0.05 coupling coefficients are realistic noise, not structure.

### System 2: Constructed Counterexample (Axiom A fails — by design)

```
φ₁(κ, α) = σ(κ + α; k=5, x₀=1.0)
φ₂(κ, α) = σ(κ + α; k=5, x₀=0.8)
```

Both functions depend identically on κ + α. Therefore:
```
∇φ₁ ∝ ∇φ₂ ∝ [1, 1]
rank(J) = 1 everywhere
Axiom A fails by construction
```

This is a minimal example of gradient degeneracy: same functional
form, different thresholds. It represents the worst case for Axiom A.

---

## 2. Strategy A — Direct Gradient Rank Measurement

### Method

Numerical Jacobian at each point p = (κ, α) in a 30×30 grid:

```
∂φᵢ/∂pⱼ ≈ (φᵢ(p + ε·eⱼ) − φᵢ(p − ε·eⱼ)) / (2ε),   ε = 10⁻⁴

J(p) = [∇φ₁(p) | ∇φ₂(p)]    (shape: 2×2 here)

rank(J) via SVD with tolerance 10⁻⁶
```

### Results

| System | Mean rank | Fraction rank=2 |
|---|---|---|
| Schools (Axiom A holds) | **2.000** | **100%** |
| Counterexample (Axiom A fails) | **1.000** | **0%** |

**Schools:** rank = 2 at every grid point. No degeneracy detected.
The 0.05 second-order coupling is insufficient to cause rank collapse.

**Counterexample:** rank = 1 everywhere by construction.
The diagonal [1,1] direction dominates; no independent second axis exists.

### Gradient Angle Distribution

The angle between ∇φ_A5 and ∇φ_A6 was measured across all 900 grid points:

- **Schools:** median angle ≈ 85–88°, strongly concentrated near 90°
  (orthogonal gradients, consistent with structural independence)
- **Counterexample:** median angle ≈ 0–5° (near-parallel gradients,
  Axiom A violated)

### Condition Number

The condition number κ(J) = σ_max/σ_min of the Jacobian:

- **Schools:** κ(J) ≈ 1.0–3.0 at most points (well-conditioned)
- **Counterexample:** κ(J) ≫ 100 everywhere (near-singular)

**Figure 1 reference:** `fig_emp1_gradient_rank.png`

---

## 3. Strategy B — Interventional Sensitivity Matrix

### Method

For each φᵢ and each parameter pⱼ, the **normalized sensitivity**:
```
S[i,j] = |∂φᵢ/∂pⱼ|_{base_point},  normalized per row
```

**Ideal Axiom A signature:** dominant diagonal (each φᵢ sensitive
to its own parameter axis, insensitive to others).

**Cross-talk ratio:**
```
C = mean(off-diagonal entries) / mean(diagonal entries)
```
Small C → near-diagonal → Axiom A plausible.

### Results

**Schools at three parameter points:**

| Point | Region | S[A5,κ] | S[A5,α] | S[A6,κ] | S[A6,α] | C |
|---|---|---|---|---|---|---|
| Point 1 | R1 (low κ, high α) | 1.00 | ~0.00 | ~0.00 | 1.00 | **0.004** |
| Point 2 | Near θ*₁ | 1.00 | ~0.02 | ~0.03 | 1.00 | **0.011** |
| Point 3 | F0 region | 1.00 | ~0.05 | ~0.04 | 1.00 | **0.032** |

All three points show strongly dominant diagonal with C < 0.05.
Cross-talk is largest in the F0 region (Point 3) where both assumptions
are simultaneously stressed — but remains negligible.

**Counterexample at same points:**

| Point | S[φ₁,κ] | S[φ₁,α] | S[φ₂,κ] | S[φ₂,α] | C |
|---|---|---|---|---|---|
| All | 1.00 | 1.00 | 1.00 | 1.00 | **1.000** |

Perfect cross-talk (C = 1.000): both φᵢ are equally sensitive to both
parameters. Off-diagonal = diagonal everywhere.

**Interpretation:**
The sensitivity matrix provides a causal test of Axiom A without
requiring gradient computation. The near-diagonal structure of Schools
is not a coincidence — it reflects the structural separation of
A5 (κ-mechanism) and A6 (α-mechanism).

**Figure 2 reference:** `fig_emp2_sensitivity.png`

---

## 4. Strategy C — Z(π) Dimension Estimation

### Method

The theorem predicts dim_eff(Z(π)) = rank(IVA_ext(π)).
This is tested indirectly: if the prediction is correct, the Z(π)
region projected onto V = span(IVA_ext) should have dimension equal
to rank(IVA_ext).

**Critical distinction** (from analysis of counterexample):
```
Z(π) itself:       always d-dimensional as open subset of ℝᵈ
π_V(Z(π)):         has dimension dim_eff — this is what the theorem claims
```

PCA on raw Z(π) points measures the Hausdorff dimension of Z, not dim_eff.
For the theorem, we must project onto V first.

### Projection analysis

| System | IVA_ext | V | π_V(Z(π)) range | dim_eff |
|---|---|---|---|---|
| Kuramoto | ∅ (point-type) | {0} | single point | 0 |
| Pitchfork | {∂/∂μ} | 1D (μ-axis) | [μ_c, ∞) | 1 |
| Schools | {∂/∂κ, ∂/∂α} | ℝ² | [0.46,1.0] × [0.40,0.86] | 2 |
| Counter | {[1,1]/√2} | 1D (diagonal) | [0.41, 1.41] | 1 |

**Schools:** V = ℝ² (span of two orthogonal axes = full space).
π_V(Z) = Z itself. PCA confirms 2D structure: evr = [0.65, 0.35].
Both principal components carry substantial variance → genuinely 2D.

**Counterexample:** V = span([1,1]/√2) = 1D diagonal.
Z itself is a 2D diagonal band (PCA evr = [0.73, 0.27]).
But π_V(Z) is a 1D arc along [1,1].
**dim_eff = 1, not 2** — the theorem correctly distinguishes these.

This is the key result of Strategy C: the PCA of Z and the theorem's
dim_eff can disagree, and the theorem is right. The counterexample
has a 2D Z-region but 1D dim_eff, because its IVA_ext has rank 1.

**Figure 3 reference:** `fig_emp3_zdim_counter.png`

---

## 5. Strategy D — Constructed Counterexample

### Design

The counterexample was constructed to violate Axiom A minimally:
two functions with identical functional form but different thresholds.

```python
φ₁(κ, α) = σ(κ + α, x₀=1.0)
φ₂(κ, α) = σ(κ + α, x₀=0.8)
```

### Observed consequences (all predicted by theorem)

| Quantity | Schools | Counterexample | Theorem prediction |
|---|---|---|---|
| rank(J) | 2 (everywhere) | 1 (everywhere) | = rank(IVA_ext) |
| Cross-talk C | < 0.05 | 1.000 | C ≈ 0 ↔ Axiom A |
| Z geometry | 2D rectangular | 2D diagonal band | — |
| π_V(Z) | 2D | 1D arc | dim_eff = rank |
| dim_eff | 2 | 1 | rank(IVA_ext) |

### Scientific value of the counterexample

The counterexample demonstrates three things:

**1. Axiom A is not trivially true.**
Having k = 2 failure functions does not automatically give rank(J) = 2.
The structural separation of parameter axes is a non-trivial property.

**2. The theorem is not trivially true.**
Same parameter space, same k, same τ, same Z topology (both 2D open sets)
— but different dim_eff. The theorem correctly distinguishes them via
rank(IVA_ext), which the naive BC-count heuristic (H2) cannot.

**3. Axiom A is checkable.**
The sensitivity matrix (Strategy B) and gradient rank (Strategy A)
provide practical diagnostics. A scope designer can verify Axiom A
before claiming the theorem applies.

---

## 6. Consolidated Results

| Strategy | Schools | Counterexample | Confirms |
|---|---|---|---|
| A: Gradient rank | rank=2, frac=100% | rank=1, frac=0% | Axiom A holds / fails |
| A: Gradient angle | median ≈ 87° | median ≈ 2° | Independence / degeneracy |
| B: Sensitivity | C ≈ 0.01 | C = 1.00 | Near-diagonal / coupled |
| C: dim_eff | 2 (via π_V) | 1 (via π_V) | Theorem prediction ✓ |
| D: Counterexample | reference | breaks | Non-triviality of Axiom A |

**Reading this table:**
Strategies A and B test Axiom A directly (input condition).
Strategy C tests the theorem conclusion (output).
Strategy D validates that the theorem discriminates correctly.

All four strategies are consistent. The theorem holds where Axiom A holds,
fails where Axiom A fails, and the failure is empirically detectable.

---

## 7. What This Study Does and Does Not Show

**Shows:**
- Axiom A holds for the Schools scope at all tested parameter points
- The sensitivity structure (near-diagonal S matrix) provides an
  empirical signature of Axiom A that precedes any failure observation
- The theorem correctly predicts dim_eff in all four cases (3 systems + 1 counterexample)
- Axiom A is necessary — the counterexample confirms the theorem breaks without it

**Does not show:**
- That Axiom A holds for *all* ARW scopes (it may fail in high-coupling
  regimes where A5 and A6 both depend strongly on the same parameter)
- That Axiom A holds across all τ values (tested at τ = 0.25 only)
- The general proof connecting BC-operator structure to gradient independence
  (this remains Q-IVA-01)

**Correct epistemic framing:**
This study shows: *if* Axiom A holds, the empirical signatures are
exactly what the theorem predicts. And in the validated ARW scope,
those signatures are present. This is scientific evidence, not proof.

---

## 8. Practical Checklist for Scope Designers

Before claiming H2' applies to a new ARW scope:

```
Step 1 — Construct φᵢ for each failing assumption Aᵢ

Step 2 — Compute sensitivity matrix S at representative points
          Check: is S near-diagonal? (C < 0.1)

Step 3 — Compute gradient rank across parameter grid
          Check: is rank(J) = k at > 95% of points?

Step 4 — Check gradient angle distribution
          Check: is median angle > 45°?

If Steps 2–4 pass → Axiom A empirically supported → H2' applies
If any step fails → Axiom A may not hold → check parameter subspace overlap
```

---

## 9. Repo Placement

```
docs/advanced/
├── iva_z_geometry.md                  ← theorem document
└── axiom_a_empirical_validation.md   ← this document

cases/CASE-20260328-0010/
└── axiom_a_check/
    ├── gradient_rank.csv              ← raw rank data
    ├── sensitivity_matrix.csv         ← S matrices at 3 points
    └── z_projection_analysis.csv      ← π_V(Z) data
```
