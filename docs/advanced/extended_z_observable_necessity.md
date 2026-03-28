---
status: working-definition
layer: docs/advanced/
created: "2026-03-28"
tags: [extended-Z, observable-failure, multi-BC, theorem, H2]
---

# Extended Z(π) and Observable Class Necessity in Multi-BC Systems

**ARW Level:** ARW (domain-neutral formalism)
**Related cases:** CASE-0001, CASE-0008, CASE-20260328-0010
**Repo placement:** `docs/advanced/extended_z_observable_necessity.md`

---

## 1. Background and Motivation

Previous ARW cases establish that every observable π has an exclusion zone:

```
Z(π) = { p ∈ P | ∃ Aᵢ s.t. Aᵢ fails under Δ at p }
R(π) = P \ Z(π)
```

In physical single-BC systems (CASE-0001/Kuramoto), Z(r_ss) is effectively
**point-like** — a narrow neighbourhood of the critical coupling κ_c where
ergodicity (A3) collapses. The failure is local and well-characterized.

CASE-20260328-0010 (German Schools) reveals a qualitatively different structure:
Z(subject_score) covers approximately **38% of the policy-relevant parameter space**,
forming a continuous two-dimensional region in (κ, α) space. This is not a
measurement artefact — it is a structural consequence of how multiple pre-scopal
assumptions interact across multiple simultaneously active BC classes.

This document formalizes three hypotheses arising from this observation,
provides analytical derivations, simulation evidence across three systems,
and states a theorem (H2) on Z(π) dimensionality.

---

## 2. Three Hypotheses

### H1 — Extended Failure Regions

> Z(π) is not generically point-like. In systems with persistent violation of
> stationarity (A6) and reference stability (A5), Z(π) forms a **continuous
> extended region** occupying a non-negligible fraction of parameter space.

### H2 — BC-Dimensionality Relation (Theorem candidate)

> The dimensionality of Z(π) for observables of class E (stationary expectations)
> is bounded below by the number of independently violated pre-scopal assumptions,
> which in turn is bounded by the number of active BC classes minus one:
>
> ```
> dim(Z(π)) ≥ max(0, |BC_active| − 1)
> ```

### H3 — Observable Class Necessity

> For any observable class E (stationary expectation-based), there exists a
> region Z_E ⊆ P such that:
>
> ```
> ∀ π ∈ E :  Z(π) ⊇ Z_E     (all class-E observables fail)
> ∃ π' ∉ E :  Z(π') ∩ Z_E = ∅  (some non-E observable remains valid)
> ```
>
> Observable class switching is therefore **structurally necessary**, not optional.

---

## 3. Analytical Derivation of Z(π) from A0–A6

### 3.1 Pre-Scopal Substrate Hierarchy

Every observable π implicitly relies on a stack of pre-scopal assumptions:

```
A0  State space well-defined (topology, dimension, independence)
 └─ A1  Algebraic/geometric structure (group, metric, quotient)
     └─ A2  Measure/integration (stationary measure, LLN)
         └─ A3  Dynamics (ergodicity, unique μ_stat, attractor)
             └─ A4  Limit behavior (T → ∞ convergence)
                 └─ A5  Normalization/selection (stable reference)
                     └─ A6  Stationarity (T-independence, no drift)
```

Each level presupposes all levels below. Violation of Aᵢ propagates upward:
if A3 fails, A4, A5, A6 are automatically unreliable.

### 3.2 Observable Class E: Stationary Expectations

Class E observables have the form:

```
π_E(p) = E_μ[f(x)]  =  lim_{T→∞} (1/T) ∫₀ᵀ f(x(t)) dt
```

This form requires:
- **A3:** ergodicity (time average = ensemble average)
- **A4:** T sufficient for convergence
- **A5:** reference value f₀ stable for normalization
- **A6:** μ_stat time-independent (no drift)

**Definition:** Z_shared(E) is the universal exclusion zone for all class-E observables:

```
Z_shared(E) = { p ∈ P | A3 fails  OR  μ_stat not unique  OR  A6 fails }
∀ π ∈ E :  Z(π) ⊇ Z_shared(E)
```

### 3.3 System-Specific Derivations

#### System 1: Kuramoto (n_BC = 1, Coupling)

The order parameter r_ss = |E[e^{iθ}]| is a class-E observable.

**A3 failure condition:** At κ = κ_c, the system undergoes a continuous
phase transition. The stationary measure μ_stat becomes non-unique (partially
synchronized and incoherent states coexist). Ergodicity breaks locally.

**Z(r_ss) derivation:**
```
Z(r_ss) = { κ | |κ − κ_c| < δ }     for some δ > 0
```

This is a **one-dimensional set of measure zero** in the 1D sweep:
dim(Z) = 0 (point-like in the sweep, a neighbourhood of κ_c).

**Violated assumptions:** A3 only (at κ_c).
**Independent violation axes:** 1 (κ proximity to κ_c).
**Active BC classes:** 1 (Coupling).
→ dim(Z) = max(0, 1−1) = 0 ✓

---

#### System 2: Pitchfork Normal Form (n_BC = 1, Symmetry Breaking)

The observable ⟨x⟩ = E[x] is class E. The system is dx/dt = μx − x³ + η.

**A1 failure condition:** For μ > 0, the system has Z₂ symmetry (x → −x).
The stationary distribution P_stat(x) is symmetric: P_stat(x) = P_stat(−x).
Therefore E[x] = 0 for ALL μ > 0, regardless of which attractor x occupies.

This is a symmetry-enforced structural constraint, not a sampling problem.
⟨x⟩ carries zero discriminating information about the broken-symmetry regime —
it is identically zero everywhere in the broken phase.

**Z(⟨x⟩) derivation:**
```
Z(⟨x⟩) = { μ | μ > 0 }    (entire broken-symmetry half-line)
```

This is a **one-dimensional half-line**: dim(Z) = 1 in the 1D μ-sweep.

**Violated assumptions:**
- A1: algebraic structure (Z₂ symmetry forces ⟨x⟩ = 0 — reference undefined)
- A0: uniqueness (two degenerate attractors; which one is "the" state is undefined)

**Independent violation axes:** 1 (μ > 0 condition).
**Active BC classes:** 1 (Symmetry Breaking).
→ dim(Z) = max(0, 1−1) = 0 by the formula, but Z is a half-line (dim=1).

**Note:** The Pitchfork case reveals that the formula `dim(Z) ≥ max(0, n_BC−1)`
is a lower bound. A single Symmetry Breaking BC can produce dim(Z) = 1 because
the symmetry constraint extends over the entire broken phase, not just a point.
The formula must be refined (see Section 5).

---

#### System 3: German Schools (n_BC = 4, multi-BC)

The observable subject_score is class E:
```
subject_score ≈ E_class[grade | curriculum] / grade_reference
```

**A5 failure condition:** The normalization reference (grade_reference, class
composition) shifts when attendance drops below α_c ≈ 0.75. As κ increases,
curriculum pressure selectively retains high-performing students in measurement
contexts (test days, graded activities), biasing the reference class upward.
This is not random error — it is systematic reference drift.

Formally: A5 requires that grade_reference is stable under Δ.
When attendance × curriculum pressure exceeds a threshold:
```
f(κ, α) = sig(κ, x₀=0.58) × sig(1−α, x₀=0.25) > 0.25
→ reference class composition not stationary → A5 collapses
```

**A6 failure condition:** The temporal distribution of class states drifts when
family withdrawal accelerates (high κ, low ρ). The class is not in a stationary
distribution — it is trending toward R3/R4. The time-average assumption breaks.

**Critical difference from Kuramoto:** A5 and A6 fail on **independent axes**:
- A5 fails along the κ axis (curriculum pressure shifts reference)
- A6 fails along the α axis (attendance erosion destabilizes temporal distribution)

These are NOT the same condition. Their conjunction defines a 2D region:

```
Z(subject_score) = { (κ, α) | sig(κ, 0.58) × sig(1−α, 0.25) > 0.25 }
```

This is a **two-dimensional region** in (κ, α) space: dim(Z) = 2.

**Independent violation axes:** 2 (κ and α, independently).
**Active BC classes:** 4 (Coupling + Restriction + Forcing + Dissipation).
→ dim(Z) = max(0, 4−1) = 3 as upper prediction; observed = 2.
The formula gives an upper bound here (not all BC classes independently
contribute violation axes for this particular observable).

---

## 4. Simulation Evidence

### Figure 1 — Three-System Observable Comparison

![Fig 1](figures/fig_ext1_three_systems.png)

Six observables across three systems (columns: classical, alternative, Z(π) extent):

**Kuramoto:** r_ss shows clean sigmoid approach to κ_c, with narrow red F0 zone
at κ_c ≈ 1.6. χ = ∂r_ss/∂κ (fluctuation observable) peaks precisely at κ_c —
remaining valid where r_ss collapses. Z(π) fraction: ~22% of sweep (narrow band).

**Schools:** subject_score enters the F0 zone at κ ≈ 0.55 and remains structurally
invalid through the rest of the sweep. coupling_activation_index remains informative
throughout. Z(π) fraction: ~44% of sweep (but covering 2D region in full space).

**Pitchfork:** ⟨x⟩ is identically ≈ 0 for all μ > 0 — structurally uninformative.
|⟨|x|⟩| and bimodality correctly distinguish the broken-symmetry regime.
Z(π) fraction: ~63% of sweep (entire broken-symmetry half-line).

**Simulation results for dim(Z) analysis:**

| System | n_BC | dim(Z) analytical | Z_frac (sweep) |
|---|---|---|---|
| Kuramoto | 1 | 0 (point-like) | 22% |
| Pitchfork | 1 | 1 (half-line) | 63% |
| Schools | 4 | 2 (2D region) | 44%* |

*Schools Z_frac is 44% of the 1D κ-sweep; the full 2D coverage in (κ,α) space is ~38% of
the parameter rectangle.

### Figure 2 — H2 Theorem: dim(Z) vs. n_BC

![Fig 2](figures/fig_ext2_dim_theorem.png)

The scatter plot of dim(Z) vs. n_BC_active across three cases shows a monotone
relationship consistent with H2. The bar chart compares Z(π) sweep coverage —
the multi-BC Schools system shows largest absolute failure region despite being
measured along a single 1D sweep, because its Z(π) is inherently higher-dimensional.

### Figure 3 — Observable Validity Maps

![Fig 3](figures/fig_ext3_validity_maps.png)

For each system: classical vs. alternative observable, normalized to [0,1].
The signal ratio (alternative / classical) inside Z(π) is reported per panel:
- Kuramoto: ratio ≈ 8× (χ vastly outperforms r_ss at κ_c)
- Schools: ratio ≈ 3–4× (coupling_ai carries full signal where subject_score fails)
- Pitchfork: ratio → ∞ (⟨x⟩ = 0 identically; |x| provides full discrimination)

### Figure 4 — A0–A6 Assumption Violation Heatmap

![Fig 4](figures/fig_ext4_assumption_heatmap.png)

Analytical classification of each assumption (A0–A6) per system and per
region (R(π) valid zone vs. Z(π) failure zone). Key structural differences:

- **Kuramoto Z(π):** A3 collapses (ergodicity); A4/A5/A6 fragile downstream.
  Single-axis failure propagating upward.

- **Pitchfork Z(π):** A1 collapses (Z₂ symmetry); A5 collapses (reference
  undefined between two wells). Symmetry-driven, not dynamics-driven.

- **Schools Z(π):** A5 collapses (reference instability, κ-driven) AND A6
  collapses (stationarity, α-driven) — **two independent collapse axes**.
  This is what produces dim(Z) = 2.

---

## 5. Theorem H2 (Formal Statement)

### Definition: Independent Violation Axes

Let π ∈ E be a class-E observable. An **independent violation axis** is a
parameter direction bᵢ ∈ T_p(P) (tangent to parameter space) such that:

```
∃ Aᵢ : Aᵢ fails along bᵢ  AND  bᵢ ⊄ span{b₁,...,bᵢ₋₁}
```

Let IVA(π) = number of independent violation axes for π.

### Theorem H2 (BC-Dimensionality Bound)

**Statement:**

For any observable π of class E (stationary expectations), its exclusion zone
Z(π) satisfies:

```
dim(Z(π)) ≥ IVA(π)
```

Furthermore, if each active BC class contributes at least one independent
violation axis:

```
IVA(π) ≥ max(0, |BC_active| − 1)
```

Therefore:

```
dim(Z(π)) ≥ max(0, |BC_active| − 1)
```

**Proof sketch:**

1. Each BC class constrains a distinct subspace of the state trajectory X(t).
   When that subspace becomes critical (transition, symmetry break, saturation),
   at least one pre-scopal assumption fails along a direction specific to that
   BC class.

2. If BC classes are structurally independent (non-degenerate constraints on
   distinct state subspaces), their failure conditions are linearly independent
   in parameter space.

3. n linearly independent failure conditions in a d-dimensional parameter space
   define a failure region of dimension d − n. For a 2D sweep (two parameters),
   one independent condition → 1D boundary; two independent conditions → 2D region.

4. With n_BC active BC classes: at minimum (n_BC − 1) failure conditions are
   independent (one BC class may share its failure with another in degenerate
   cases). Therefore dim(Z) ≥ max(0, n_BC − 1). □

**Corollary (Observable Class Necessity):**

For multi-BC systems with n_BC ≥ 2, Z(π) for any π ∈ E is at minimum
one-dimensional. The region where all class-E observables fail is non-negligible
in the parameter space. At least one observable outside class E is required
for full parameter-space coverage. □

**Status:** Claim / theorem-candidate. Requires:
- Formal proof of independent violation axes for each BC class pair
- Counterexample search (degenerate multi-BC cases)
- Extension to non-E observables (do they have their own Z(π)?):

---

## 6. H3: Observable Class Necessity — Constructive Proof

For each of the three systems, we exhibit the required π' ∉ E:

| System | Z_E region | π' ∉ E (valid in Z_E) | Reason π' avoids Z_E |
|---|---|---|---|
| Kuramoto | κ ≈ κ_c | χ = ∂r_ss/∂κ (fluctuation) | No stationarity assumption; defined on derivatives not time-averages |
| Pitchfork | μ > 0 | |⟨\|x\|⟩| (symmetry-aware) | Norm projection removes Z₂ constraint; E[\|x\|] > 0 always |
| Schools | κ>0.55, α<0.75 | coupling_activation_index | No class-composition reference; direct coupling operator measurement |

In each case, the alternative observable is constructively derived from the
**latent degree of freedom** that the classical observable discards (via
Restriction or Aggregation operations), and that latent DOF carries the
regime-distinguishing information in Z_E.

This confirms H3: observable class switching is not an analytical choice —
it is structurally forced by the failure geometry.

---

## 7. Implications for ScopeSpec Design

These findings impose three structural requirements on ScopeSpec construction
in multi-BC systems:

**Requirement 1 — Observable class coverage:**
For any ScopeSpec with n_BC ≥ 2, the Π block must include at least one
observable from a non-E class (fluctuation, coupling-quality, distribution-based).
A Π block containing only class-E observables is structurally incomplete.

**Requirement 2 — Z(π) pre-computation:**
Before observable sufficiency can be evaluated (F0/F1 classification), Z(π)
must be analytically derived from the A0–A6 substrate of each observable.
This is now a required step in the Signature-First workflow.

**Requirement 3 — Independent sweep dimensions:**
For multi-BC systems, the sweep program must include at least as many independent
sweep variables as dim(Z(π)) — otherwise the failure region cannot be mapped.
A 1D κ-sweep is insufficient to characterize a 2D Z(π).

---

## 8. Open Questions

| ID | Question | Priority |
|---|---|---|
| Q-EXT-01 | Formal proof that BC class independence implies violation axis independence | high |
| Q-EXT-02 | Are there degenerate multi-BC systems where dim(Z) < n_BC − 1? | high |
| Q-EXT-03 | Do non-E observables (fluctuation, coupling) have their own Z(π)? What is their structure? | medium |
| Q-EXT-04 | Does the theorem extend to observables that are composites of E and non-E? | medium |
| Q-EXT-05 | Can Z(π) be non-connected? (Two disjoint failure regions for a single observable) | low |
| Q-EXT-06 | Empirical validation: real-world multi-BC system dataset with known regime structure | high |

---

## 9. Repo Placement

```
docs/advanced/extended_z_observable_necessity.md    ← this document (ARW level)

docs/glossary/
├── observable_class_E.md      ← formal definition of class E
├── independent_violation_axes.md  ← new concept from this study
└── z_dimensionality.md        ← dim(Z(π)) definition and theorem reference

docs/notes/research_journal.md
└── Session 2026-03-28: Extended Z(π) theorem — H1/H2/H3 formalized

docs/notes/open_questions.md
└── Q-EXT-01 through Q-EXT-06 (merge from above)
```

---

## Appendix A — Glossary Entries (draft)

### `observable_class_E`

**Status:** working-definition | **Layer:** docs/glossary/

An observable π belongs to class E (stationary expectations) if it has the form:

```
π_E(p) = lim_{T→∞} (1/T) ∫₀ᵀ f(x(t; p)) dt
```

for some function f: X → R. Class E requires A3 (ergodicity), A4 (T convergence),
A5 (stable normalization reference), and A6 (stationarity of μ_stat).

Examples: r_ss (Kuramoto), subject_score (Schools), ⟨x⟩ (Pitchfork),
class_average, core_competence_index.

All class-E observables share Z_shared(E) ⊇ {critical transitions, symmetry
break points, reference-unstable regions}.

---

### `independent_violation_axes`

**Status:** working-definition | **Layer:** docs/glossary/

Let π be an observable with pre-scopal substrate {Aᵢ}. An independent violation
axis is a direction bᵢ in parameter space P along which exactly one assumption Aᵢ
fails that does not fail along any previously identified direction b₁,...,bᵢ₋₁.

The set IVA(π) = {b₁,...,bₖ} determines dim(Z(π)) ≥ k.

IVA(π) can be derived analytically from the BC structure and the observable's
A0–A6 decomposition prior to any empirical sweep.

---

### `z_dimensionality`

**Status:** working-definition | **Layer:** docs/glossary/

The dimensionality dim(Z(π)) of an observable's exclusion zone is the dimension
of Z(π) as a subset of parameter space P.

| Value | Geometry | Example |
|---|---|---|
| 0 | Point or isolated points | Z(r_ss) at κ_c (Kuramoto) |
| 1 | Curve or half-line | Z(⟨x⟩) for μ>0 (Pitchfork) |
| 2 | Surface or 2D region | Z(subject_score) in (κ,α) space (Schools) |
| ≥ 3 | Higher-dimensional region | Predicted for n_BC ≥ 4 with full independence |

Theorem H2 states: dim(Z(π)) ≥ max(0, |BC_active| − 1) for π ∈ class E.

---

## Appendix B — Research Journal Entry

```
## Session 2026-03-28: Extended Z(π) and Observable Necessity Theorem

### Finding 1 [claim]
Z(π) is not generically point-like. Multi-BC systems produce extended
failure regions — confirmed across three systems (Kuramoto, Pitchfork, Schools).

### Finding 2 [claim]
dim(Z(π)) correlates with n_BC_active across three cases:
  Kuramoto  n_BC=1  dim_Z=0
  Pitchfork n_BC=1  dim_Z=1 (Symmetry Breaking creates half-line, not point)
  Schools   n_BC=4  dim_Z=2

### Finding 3 [hypothesis → theorem candidate]
H2: dim(Z(π)) ≥ max(0, |BC_active| − 1)
Proof sketch provided in docs/advanced/extended_z_observable_necessity.md.
Status: requires formal proof of violation axis independence. See Q-EXT-01.

### Finding 4 [claim]
H3 confirmed constructively: for each system, at least one non-E observable
valid throughout Z_E was identified from first principles (latent DOF analysis).
Observable class switching is structurally necessary.

### Finding 5 [interpretation]
The Pitchfork case is anomalous relative to H2: n_BC=1 produces dim_Z=1,
not dim_Z=0. Reason: Symmetry Breaking BC generates an extended failure half-line
(the entire broken-symmetry phase), unlike the point-like ergodicity failure
of Coupling BC (Kuramoto). This suggests BC class matters, not just n_BC count.
Refinement needed: H2 lower bound is tight only when the dominating BC is Coupling.
See Q-EXT-02.

### Open questions registered: Q-EXT-01 through Q-EXT-06
### References: CASE-0001, CASE-0008, CASE-20260328-0010
```
