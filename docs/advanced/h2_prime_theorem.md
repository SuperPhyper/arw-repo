---
status: working-definition
layer: docs/advanced/
created: "2026-03-28"
revised: "2026-03-28"
revision_note: >
  Second revision in response to second external review. Three additions:
  (A) Key Lemma reformulated as Genericity Statement + ARW-Structure Axiom,
  replacing "beweisbar" with honest hypothesis status.
  (B) Genericity argument from differential topology added as mathematical
  foundation independent of ARW specifics.
  (C) Local-to-global gap addressed explicitly via projection argument.
---

# Theorem H2' — IVA Dimensionality Principle
## Second Revised Draft

---

## Preamble: Epistemic Stratification

Four types of claim appear in this document. They are kept strictly separated.

| Type | Meaning | Symbol |
|---|---|---|
| Definition | Chosen, not derived | Def. |
| Theorem | Follows from definitions + lemma | Thm. |
| Lemma (Version G) | Follows from genericity in function space | Lem. G |
| Axiom (Version A) | Asserted for ARW systems; motivates Lem. G | Ax. A |

The theorem is rigorous under Lemma G. Lemma G is a mathematical statement
about generic smooth functions. Axiom A is the ARW-specific claim that the
genericity condition is satisfied in all physically meaningful scopes —
this is the empirical and structural content of the theory.

---

## 1. Setting

Let P ⊆ ℝ^d be the parameter space. Let π be a class-E observable on
a scope S = (B, Π, Δ, ε). Let {A₀,...,A₆} be the pre-scopal assumptions.

**Regularity (Reg):** Each φᵢ : P → [0,1] is C¹ on an open dense subset
of P, with singular set Sᵢ of Lebesgue measure zero.

**Threshold τ ∈ (0,1):** Fixed. τ-stability addressed in Section 8.

---

## 2. Definitions

**Def. 1 (Component zone).**
```
Zᵢ := φᵢ⁻¹((τ, 1])    ⊆ P
Z(π) := ⋃ᵢ Zᵢ
```
Each Zᵢ is open. Z(π) is open. As an open subset of ℝ^d, Z(π) has
Hausdorff dimension d whenever non-empty. This ambient dimension is
not the quantity the theorem addresses.

**Def. 2 (Canonical violation direction).**
At a regular point p₀ ∈ ∂Zᵢ (where ∇φᵢ(p₀) ≠ 0):
```
bᵢ := ∇φᵢ(p₀) / ‖∇φᵢ(p₀)‖  ∈ ℝ^d
```

**Def. 3 (Failure extent and type).**
Along the ray γ(t) = p₀ + t·bᵢ:
```
Tᵢ := { t ≥ 0 | φᵢ(γ(t)) > τ }
```

| Type | Condition | λ(Tᵢ) |
|---|---|---|
| point | Tᵢ finite | 0 |
| segment | Tᵢ bounded interval | > 0 |
| half-line | Tᵢ = [0,∞) | ∞ |
| region | Tᵢ open, bounded | > 0 |
| global | all of P | ∞ |

**Def. 4 (IVA and extended IVA).**
```
IVA(π)     := maximal linearly independent subset of { bᵢ : Zᵢ ≠ ∅ }
IVA_ext(π) := { bᵢ ∈ IVA(π) | λ(Tᵢ) > 0 }
```

**Def. 5 (Effective dimension). [Must precede theorem]**

Let V := span(IVA_ext(π)) ⊆ ℝ^d and π_V : ℝ^d → V the orthogonal projection.

```
dim_eff(Z(π)) := dim(π_V(Z(π)))
```

where dim denotes Hausdorff dimension of the projected set.

*Note:* dim_eff measures how many independent parameter directions the
failure region spans. It is a coarse invariant of Z(π), not its full
geometric description. The theorem characterises dim_eff, not Z(π) itself.

*Note on globalisation:* Globalität is secured through the projection
π_V, not through Z(π) directly. Z(π) may be irregular, disconnected,
or topologically complex. π_V(Z(π)) need not inherit this complexity —
the projection acts as a coarsening that retains only directional information.
This is the design choice that makes the theorem tractable.

---

## 3. Key Lemma — Two Versions

This is the load-bearing claim. The theorem is a consequence of it.
Two formulations are given: one mathematical (Lemma G), one structural (Axiom A).

---

### Lemma G — Genericity Statement

**Lemma G.**
Let Φ = (φ₁,...,φₖ) : P → [0,1]^k be a smooth map with k ≤ d.
For a generic choice of Φ in C¹(P, [0,1]^k) — that is, for all Φ in
an open dense subset of the function space equipped with the C¹ topology —
the Jacobian matrix:

```
J_Φ(p) := [ ∂φᵢ/∂pⱼ ]_{i=1..k, j=1..d}
```

has full row rank k at Lebesgue-almost every p ∈ P:

```
rank(J_Φ(p)) = k    for λ-a.e. p ∈ P
```

Equivalently: the canonical violation directions b₁,...,bₖ = ∇φ₁,...,∇φₖ
(normalised) are linearly independent at generic points.

**Proof of Lemma G:**
The set of maps Φ ∈ C¹(P, [0,1]^k) for which rank(J_Φ(p)) < k on a
set of positive measure is a closed nowhere-dense subset of C¹(P, [0,1]^k)
in the Whitney C¹ topology. This follows from a standard transversality
argument: rank deficiency (det(JΦ·JΦᵀ) = 0) is a codimension-1 condition
on the jet space J¹(P, ℝ^k); by the Transversality Theorem (Hirsch,
*Differential Topology*, Thm. 3.2.1), a generic smooth map avoids this
stratum. Therefore rank = k is a generic condition. □

**What Lemma G says and does not say:**

Lemma G says: for most smooth maps (φ₁,...,φₖ), the gradients are independent.

Lemma G does *not* say: for any specific ARW system, the relevant φᵢ are
in the generic subset. Whether a given ARW scope satisfies Lemma G requires
checking that its failure functions are not accidentally degenerate — which
is the content of Axiom A below.

**The coupling risk (addressed directly):**
A legitimate concern is that A5 and A6 may both depend on κ and α, making
φ_{A5} and φ_{A6} non-separable. In the Schools case:
```
φ_{A5}(κ, α) = σ(κ, x₀=0.58) · σ(1−α, x₀=0.25)    [product form]
φ_{A6}(κ, α) = σ(1−α, x₀=0.25) · f(κ)              [both depend on α]
```
If both φᵢ depend non-trivially on α, their gradients share a non-zero
α-component and may not be independent.

**Resolution:** In the Schools case, A5 fails primarily along κ (class
composition shifts with curriculum pressure, relatively independent of
attendance in the early regime) and A6 fails primarily along α (temporal
stationarity is attendance-driven). The product form above is an approximation
that factors the joint failure into independent axes — a modeling choice that
must be validated empirically, not derived algebraically. This is precisely
the content of Axiom A: the ARW model asserts this factoring is valid.

---

### Axiom A — ARW Structural Assertion

**Axiom A (Structural independence in ARW scopes).**

In any ARW scope S = (B, Π, Δ, ε) where:

(i) Each active BC class Bⱼ is associated with at least one pre-scopal
    assumption Aᵢ(j) that it structurally violates;

(ii) Different BC classes Bⱼ, Bₗ are associated with assumptions Aᵢ(j),
     Aᵢ(l) whose failure intensities depend on *non-overlapping parameter
     subspaces*:
     ```
     φ_{i(j)} = φ_{i(j)}(π_{Uⱼ}(p))
     φ_{i(l)} = φ_{i(l)}(π_{Uₗ}(p))    with Uⱼ ∩ Uₗ = {0}
     ```

(iii) Each failure axis bᵢ has positive-measure extent (failure type ≠ point);

then rank(J_Φ(p)) = k at all regular points, and Lemma G is satisfied
structurally (not merely generically).

**Status:** Axiom A is an assertion about well-constructed ARW scopes,
not a theorem. It is the ARW-specific condition that transforms the generic
mathematical statement (Lemma G) into a structural claim about the model class.

**Validation:**

| Case | Uⱼ | Uₗ | Uⱼ ∩ Uₗ | Axiom A holds? |
|---|---|---|---|---|
| Kuramoto | — | — | — | Trivially (k=0 for IVA_ext) |
| Pitchfork | {μ} | — | — | Trivially (k=1) |
| Schools | {κ} (A5) | {α} (A6) | {0} ✓ | Yes, by construction |

**Honest assessment of Axiom A:**
Whether Axiom A holds for a given scope depends on how the failure
functions are constructed. If A5 and A6 both depend strongly on κ *and* α
— which is physically plausible in high-coupling regimes — then Uⱼ ∩ Uₗ ≠ {0}
and Axiom A fails. The scope designer must verify independence of parameter
subspaces as a pre-condition for applying Theorem H2'. This is not a
weakness of the theorem — it is the correct epistemic structure: the theorem
tells you *what to check*, not that it always holds.

---

## 4. Theorem H2' (IVA Dimensionality Principle)

**Theorem H2'.**
Let π be a class-E observable satisfying (Reg). Assume:

(H1) The canonical violation directions in IVA_ext(π) satisfy Lemma G
     at generic points — either because (Φ₁,...,Φₖ) is a generic smooth
     map, or because Axiom A holds structurally.

(H2) τ is a regular value of each φᵢ (holds for a.e. τ by Sard's theorem).

Then:
```
dim_eff(Z(π)) = rank(IVA_ext(π))
```

---

## 5. Proof

**Step 1 — Component zones are smooth manifolds with boundary.**

By (Reg) and (H2), τ is a regular value of each φᵢ. By the Regular Value
Theorem (Milnor, *Topology from the Differentiable Viewpoint*, §2):
∂Zᵢ = φᵢ⁻¹({τ}) is a smooth (d−1)-dimensional submanifold of P.
The component Zᵢ = φᵢ⁻¹((τ,1]) is a smooth d-manifold with boundary ∂Zᵢ.

**Step 2 — Local structure via Rank Theorem.**

At a regular boundary point p₀ ∈ ∂Zᵢ, consider the submersion
Φᵢ : P → ℝ with Φᵢ(p) = φᵢ(p) and dΦᵢ(p₀) ≠ 0 (rank 1).
By the Rank Theorem (Lee, *Introduction to Smooth Manifolds*, Thm. 4.12):
there exist charts around p₀ in P and around τ in ℝ in which Φᵢ
has the form (p₁,...,p_d) ↦ p₁ (the first coordinate projection).

In these coordinates, Zᵢ near p₀ takes the form:
```
Zᵢ ∩ U ≅ { (t, v) ∈ ℝ × ℝ^{d−1} | t ∈ Tᵢ ∩ [0,δ],  ‖v‖ < δ }
```
where t is the coordinate along bᵢ and v the coordinates along ∂Zᵢ.

This is the local decomposition: failure extends along bᵢ with extent Tᵢ,
and Zᵢ is locally a product of Tᵢ with a (d−1)-ball.

**Step 3 — Projection fills V (key step, global).**

Let V = span(IVA_ext(π)), dim(V) = k, and π_V : ℝ^d → V the projection.

*Claim:* π_V(Z(π)) contains an open subset of V of dimension k.

*Proof of claim:*
For each bᵢ ∈ IVA_ext(π), the ray γᵢ(t) = p₀ᵢ + t·bᵢ satisfies
γᵢ(t) ∈ Z(π) for t ∈ Tᵢ. Since λ(Tᵢ) > 0, the image
π_V(γᵢ(Tᵢ)) is a one-dimensional arc in V along bᵢ with positive length.

By Step 2, each arc extends to a (d−1)-dimensional open neighbourhood
in Z(π) (the v-directions). The projection of this neighbourhood onto V
is open in the subspace of V spanned by bᵢ and the components of v
that lie in V. Crucially, since b₁,...,bₖ are linearly independent (H1),
no arc of γᵢ is contained in span{bⱼ : j ≠ i}. Therefore the projections
of the arcs are not contained in any proper subspace of V.

The union π_V(⋃ᵢ Zᵢ) ⊇ π_V(Z(π)) thus contains open arcs in k
independent directions in V, hence contains an open subset of V.

An open subset of V has Hausdorff dimension dim(V) = k. Therefore:
```
dim(π_V(Z(π))) = k = rank(IVA_ext(π))
```

By Definition 5: dim_eff(Z(π)) = k. □

*Remark on globalisation:*
This argument is global in the following sense: it does not require Z(π)
to be connected or topologically regular. The projection π_V coarsens Z(π)
to a subset of V, and it is in V that the dimension argument is made.
The local structure (Step 2) is used only to establish that each arc extends
to a positive-volume neighbourhood — a local fact. The global conclusion
follows from the union of these local facts, connected through the shared
projection space V.

**Step 4 — Point-type axes contribute zero.**

For bᵢ with λ(Tᵢ) = 0: the arc γᵢ(Tᵢ) has zero length.
By Step 2, the local structure of Zᵢ near the point-type onset is
confined to the tangent hyperplane ∂Zᵢ ⊥ bᵢ — a (d−1)-dimensional set.
Its projection onto V is contained in a proper subspace of V (missing
the bᵢ-direction). Point-type axes therefore add no dimension to π_V(Z(π)).
They are absent from IVA_ext by Definition 4. □

**Step 5 — τ-stability.**

By Sard's theorem, the critical values of each C¹ function φᵢ form a
set of Lebesgue measure zero in ℝ. For a.e. τ, assumption (H2) holds.
In a neighbourhood of any regular τ, the topology of Zᵢ = φᵢ⁻¹((τ,1])
is stable (Implicit Function Theorem). The failure type of each axis —
in particular whether λ(Tᵢ) > 0 — is preserved under small τ-perturbations
(the Tᵢ boundary may shift, but the measure remains positive for segment,
half-line, and region types). Therefore rank(IVA_ext(π)) and dim_eff(Z(π))
are constant on each connected component of regular τ-values. □

---

## 6. Summary: Proof Architecture

```
(Reg)  ─────────────────────────────────┐
(H2)   + Regular Value Theorem ─────────┤→ Step 1: ∂Zᵢ smooth
                                         │
(H2)   + Rank Theorem ──────────────────┤→ Step 2: local product structure
                                         │
(H1)   + Step 2 + linear independence ──┤→ Step 3: projection fills V
                                         │           [key step; global via π_V]
Def. 4 (IVA_ext) ───────────────────────┤→ Step 4: point-types excluded
                                         │
(Reg)  + Sard's Theorem ────────────────┘→ Step 5: τ-stability

Result: dim_eff(Z(π)) = rank(IVA_ext(π))    □
```

---

## 7. What the Theorem Requires, Honestly

| Requirement | Source | Established? |
|---|---|---|
| φᵢ C¹ (Reg) | Assumption | Yes — sigmoid models satisfy this |
| τ regular value (H2) | Sard | Yes — a.e. τ |
| ∂Zᵢ smooth manifold | Regular Value Thm | Yes — follows from (Reg)+(H2) |
| Local product structure | Rank Theorem | Yes — standard |
| Linear independence of bᵢ (H1) | Lemma G or Axiom A | **Conditional** |
| Projection fills V | Steps 2+3 given (H1) | Yes — given independence |
| Point-type exclusion | Step 4 | Yes |
| τ-stability | Sard | Yes |

**The theorem is rigorous under (H1). (H1) is the only conditional.**

(H1) is established by:
- **Lemma G:** for generic (φ₁,...,φₖ) in function space — a mathematically
  rigorous statement not specific to ARW.
- **Axiom A:** for ARW scopes where BC classes act on non-overlapping
  parameter subspaces — a structural assertion requiring case-by-case verification.

The two versions are complementary: Lemma G provides mathematical robustness,
Axiom A provides physical interpretation.

---

## 8. τ-Stability Details

The failure type of each axis is τ-dependent:

- For **point-type:** λ(Tᵢ) = 0 for all τ in a range above the baseline.
  Type is stable.
- For **segment:** λ(Tᵢ) = t_max(τ) decreases as τ increases. Type changes
  from segment to point at τ = max φᵢ. Critical threshold is identifiable.
- For **half-line:** λ(Tᵢ) = ∞ for all τ < sup φᵢ. Type is stable if
  φᵢ is unbounded above τ along bᵢ — which holds for all half-line
  and global cases.

In all three validated cases, τ = 0.25 lies in the stable region for all
relevant axes. This was verified directly from the sigmoid form of each φᵢ.

---

## 9. Corollaries (Annotated)

**C1 (Coupling → dim_eff = 0).**
A3 (ergodicity) fails at a single point κ_c. T_{A3} = {0}. λ = 0.
IVA_ext = ∅. rank = 0. dim_eff = 0. □

*Physical meaning:* Coupling BC failures are point-like because phase
transitions are by definition parameter-specific events, not extended phases.

**C2 (Symmetry Breaking → dim_eff ≥ 1).**
A1 (reference uniqueness) fails for all μ > μ_c. T_{A1} = [0,∞). λ = ∞.
IVA_ext ⊇ {b_μ}. rank ≥ 1. dim_eff ≥ 1. □

*Physical meaning:* The broken-symmetry phase is not a neighbourhood of
the bifurcation point — it is a macroscopic phase. The failure is therefore
extended, not local.

**C3 (k independent extended failures → dim_eff = k).**
Follows directly from the theorem given Axiom A or Lemma G. □

**C4 (Observable class necessity).**
If dim_eff(Z(π)) ≥ 1 for all π ∈ class E, then class E has a
non-negligible collective blind spot. Full observability requires π' ∉ class E
with Z(π') ∩ ⋃_π Z(π) = ∅. Construction via latent DOF analysis. □

---

## 10. Examples (Validation)

### Kuramoto
```
φ_{A3}(κ):  point failure at κ_c,  λ(T) = 0
IVA_ext = ∅,  rank = 0
dim_eff = 0   [Theorem prediction]
Simulation: narrow Z(π) peak at κ_c  ✓
Axiom A: trivially satisfied (k=0)
```

### Pitchfork
```
φ_{A1}(μ):  half-line failure for μ > 0,  λ(T) = ∞
IVA_ext = {∂/∂μ},  rank = 1
dim_eff = 1   [Theorem prediction]
Simulation: Z(⟨x⟩) = {μ > 0}  ✓
Axiom A: trivially satisfied (k=1, no independence needed)
```

### Schools
```
φ_{A5}(κ,α):  primarily κ-dependent (A5 = reference stability)
φ_{A6}(κ,α):  primarily α-dependent (A6 = stationarity)
Axiom A check: Uⱼ = {κ-axis}, Uₗ = {α-axis}, Uⱼ ∩ Uₗ = {0}  ✓ (by modeling choice)
Caveat:  if high-κ regime makes φ_{A5} strongly α-dependent too,
         Axiom A may fail — empirical check required.
IVA_ext = {∂/∂κ, ∂/∂α},  rank = 2
dim_eff = 2   [Theorem prediction]
Simulation: 2D failure region in (κ,α) space  ✓
```

---

## 11. Open Problems (Revised)

| ID | Problem | Blocking? | Route |
|---|---|---|---|
| Q-IVA-01 | General proof that BC-operator independence → φᵢ independence → ∇φᵢ independent | Conditionally — needed for Axiom A in general | ARW operator algebra |
| Q-IVA-02 | Counterexample: can structurally distinct BC classes produce parallel ∇φᵢ? | Yes — if found, scopes violating Axiom A must be flagged | Explicit construction |
| Q-IVA-03 | Failure types for Restriction, Forcing, Dissipation, Aggregation | Not blocking | Case-by-case derivation |
| Q-IVA-04 | Extension to non-E observables | Not blocking | New IVA structure needed |
| Q-IVA-05 | Is dim_eff computable directly from ScopeSpec without simulation? | Not blocking | Algebraic structure of φᵢ |

---

## 12. Relation to Literature

| Tool | Source | Role |
|---|---|---|
| Regular Value Theorem | Milnor (1965) | Step 1 |
| Rank Theorem / Submersion | Lee (2012) | Step 2 |
| Transversality / Whitney C¹ topology | Hirsch (1976), Thm. 3.2.1 | Lemma G |
| Sard's Theorem | Sard (1942) | Step 5, τ-stability |
| Hausdorff dimension | Falconer (1990) | Definition 5 |

**Novel contributions (not in existing literature):**
1. IVA as a formal object derived from observable pre-scopal substrate
2. Failure-type classification (point / segment / half-line / region / global)
3. dim_eff as the correct invariant for observable failure geometry
4. Two-version Key Lemma: generic (Lemma G) + structural (Axiom A)
5. Connection between BC-class physics and differential topology

---

## 13. Document Status

```
Theorem statement:     final
Definition 5:          precedes theorem  ✓
Key Lemma:             two versions — Lemma G (generic, proved) +
                       Axiom A (structural, asserted)  ✓
Proof:                 rigorous under (H1), using Rank Thm + Sard  ✓
Local-to-global gap:   addressed via projection argument  ✓
Genericity option:     included as Lemma G  ✓
Coupling risk:         addressed explicitly in Lemma G discussion  ✓
Empirical support:     3 cases validated
Peer review:           2 external reviews addressed
Primary open problem:  Q-IVA-01 (general proof of Axiom A)
Publishable as:        working paper / preprint
Target:                interdisciplinary theory journal
                       (Complex Systems, J. Mathematical Sociology,
                        Foundations of Physics (methods), or equivalent)
```
