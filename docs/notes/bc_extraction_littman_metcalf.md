---
status: hypothesis
layer: docs/notes/
related:
  - docs/advanced/bc_extraction_method.md
  - docs/advanced/operator_signature_catalog.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
source: isodisperse_methode_v6_sweetspot.docx
---

# BC Extraction: Littman-Metcalf Isodisperse Tuning Method

Application of `bc_extraction_method.md` Steps A–E to the isodisperse
pivot-point design method for mode-hop-free operation in Littman-Metcalf
external-cavity lasers.

---

## Step A — Qualitative Category Collection

The document describes a laser resonator that must remain within a single
longitudinal mode number N across a continuous wavelength tuning range
[λ_lo, λ_hi]. The core regime indicators are:

| Indicator | Description |
|---|---|
| Mode-hop | N crosses an integer — discrete jump to new resonance mode |
| Mode-hop-free operation | ⌊N(λ)⌋ = const. across full gain bandwidth |
| ΔN = 0 | Net change in mode number across sweep is zero — isodisperse condition |
| β-constraint satisfied | β(λ) ∈ [26°, 56°] — grating operates in efficient regime |
| β-constraint violated | β_lo < 26° — grating efficiency reduced (CO₂ case) |
| Sweet spot | α = 5°, b = −3.325 mm — four of seven systems land here without adjustment |
| Sweet-spot deviation | System requires α ≠ 5°, shifting b_opt(0) away from sweet spot |

---

## Step B — Scenario Reconstruction

### Core scenario: wavelength tuning in Littman-Metcalf resonator

```
Trigger:            rotation of feedback mirror changes λ
Components:         diode facet D, grating G, pivot point P(a,b), feedback mirror
Constraint:         grating equation sin β = λ·g − cos α  (fixes β for each λ)
State change:       OWL(λ) = 2·(l₀ + l₁) changes with λ → N(λ) = OWL(λ)/λ changes
Critical event:     N(λ) passes integer → mode hop
Goal:               choose P(a,b) such that N(λ_lo) = N(λ_hi)  → ΔN = 0
```

### Sweet-spot scenario

```
Trigger:            design choice α = 5°, δ = 0
Discovery:          b_opt(0) = −x₀·tan α = −3.325 mm  (for x₀ = 38 mm)
                    this value is independent of g, λ_lo, λ_hi
Consequence:        four independent laser systems (TEC500, Ti:Sa, 1µm, Ho/Tm)
                    share identical b_opt(0) without coordination
Structural role:    α acts as a global BC parameter that fixes the pivot offset
                    independently of all other design variables
```

---

## Step C — Structural Variable Identification

| Axis | Instantiation | Candidate BC | Candidate signature |
|---|---|---|---|
| Admissibility | β(λ) ∈ [26°, 56°] — grating constraint on (α, g) combinations | Restriction | S1: projection onto admissible (α, g) subset |
| Coupling | OWL(λ) couples wavelength λ to geometric path lengths l₀, l₁ via β(λ) | Coupling | S2: λ × geometry product state with cross terms |
| Forcing | Grating equation imposes λ → β(λ) as exogenous constraint | Forcing | S3: X × T where T = λ-axis (wavelength as index) |
| Reduction | ΔN = 0 collapses the full N(λ) function to a single integer class | Aggregation | S1: quotient projection N(λ) → ⌊N⌋ = const. |
| Contraction | b_opt(0) = −x₀·tan α: all systems with same α contract to same pivot offset | Dissipation (structural analogy) | S4: parameter space contracts to invariant line |
| Invariance | b_opt(0) independent of g, λ — symmetry in design space | Symmetry Breaking | S1 + S3: selection of invariant submanifold |

---

## Step D — Operator Signature Identification

### S1 — Projection / Selection ✅ strong

**Form 1 — β-admissibility projection:**
```
π_β : (α, g, λ) → {(α, g) : β(λ) ∈ [26°, 56°] for all λ ∈ [λ_lo, λ_hi]}
```
This is an explicit admissibility constraint — a projection onto the feasible
design subspace. Idempotent: re-applying the constraint returns the same set.

**Form 2 — isodisperse condition as quotient projection:**
```
π_N : N(λ) → ⌊N(λ)⌋ = const.
```
The ΔN = 0 condition projects the continuous mode-number function onto a
single integer equivalence class. All λ in the gain bandwidth are identified
(coarse-grained) to a single mode.

**Sub-signatures:** admissibility projection (Form 1), quotient/coarse-graining (Form 2)
**Idempotent?** ✅ yes — both forms

**BC candidate:** Restriction (Form 1), Aggregation (Form 2)

---

### S2 — Product ∘ Composition (Coupling) ✅ strong

**Form:**
```
X_joint = λ × (a, b, x₀, δ, α, g)
OWL(λ; a, b, ...) = 2·(l₀(λ) + l₁(λ; a, b))
```
The mode number N(λ) = OWL(λ)/λ is a genuine product-state function:
wavelength λ and geometry (a, b) enter with cross terms via S(λ) = sin(α+β(λ))
and C(λ) = cos(α+β(λ)). The factors S and C are wavelength-dependent and
a, b are not interchangeable — a classic S2 cross-term structure.

**Cross terms?** ✅ yes — λ_hi·S_lo − λ_lo·S_hi and λ_hi·C_lo − λ_lo·C_hi
**BC candidate:** Coupling

---

### S3 — Time-Coupled Product (Forcing) ✅ strong

**Form:**
```
X ↦ X × Λ,   Φ : Λ × X_geom → OWL
```
where Λ = [λ_lo, λ_hi] is the wavelength axis playing the role of T.
The grating equation sin β = λ·g − cos α imposes β(λ) as an exogenous
constraint on the geometry for each λ — exactly the S3 structure.

**T structure:** T = [λ_lo, λ_hi] ⊂ ℝ — continuous, ordered
**Exogenous?** ✅ yes — λ is the tuning parameter, not determined by geometry
**BC candidate:** Forcing

**Note:** S3 and S2 are both strongly present. The distinction:
- S2 describes the coupling *between* geometry and wavelength in OWL
- S3 describes the wavelength axis as an *exogenous forcing* on the grating equation
Both are valid and operate at different structural levels.

---

### S4 — Scaling ∘ Composition (Dissipation) ✅ partial — unusual form

**Form:**
```
b_opt(0) = −x₀ · tan α
```
This is not a dynamical contraction, but a **parametric invariance**: all systems
with the same (x₀, α) contract to the same b_opt(0), regardless of g, λ_lo, λ_hi.
In the (g, λ)-space, the map (g, λ_lo, λ_hi) → b_opt(0) has a zero-dimensional
image — a fixed point in b-space.

This is S4 in its **parameter-space form**: the design space contracts to an
invariant line b_opt(a) = m·a + b_opt(0) under the isodisperse condition.

**Contraction?** ✅ parametric fixed-point (not dynamical decay)
**Rate c:** not applicable — this is a design-space contraction, not temporal
**BC candidate:** Dissipation (non-standard; parameter-space analog)

**Important note:** This is a structurally novel S4 instance — it is not
time-evolution dissipation but rather **design-space collapse**. The invariant
`b_opt(0) = −x₀·tan α` is a conserved quantity under variation of (g, λ),
analogous to a symmetry. This may warrant a new sub-signature entry in the
operator catalog. → Q-OPT-01 below.

---

### S5 — Expectation as Projection ☐ not present

No stochastic or belief-state structure is present. The system is fully
deterministic. S5 does not apply.

---

## BC Candidate Set

| BC Class | Assigned | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ | S1 Form 1: β-admissibility projection | Explicit design constraint; idempotent |
| Aggregation | ✅ | S1 Form 2: N(λ) → ⌊N⌋ = const. | Isodisperse condition as quotient projection |
| Coupling | ✅ | S2: OWL = f(λ, a, b) with cross terms | Core structural coupling in the system |
| Forcing | ✅ | S3: grating equation λ → β(λ) | Wavelength as exogenous index |
| Dissipation | ✅ partial | S4: b_opt(0) = −x₀·tan α | Parameter-space fixed point; non-standard form |
| Symmetry Breaking | ✅ partial | S1+S3: sweet-spot invariance selects α = 5° | Design symmetry broken by α choice |

---

## Step E — Pre-Screening

### P1 — Continuous control parameter ✅ SATISFIED

Multiple natural candidates exist:

| Candidate θ | Range | Role |
|---|---|---|
| α (grating angle) | [5°, 20°] | Primary design parameter; determines b_opt(0) |
| κ = b − b_opt(a) | continuous | Deviation from isodisperse line; directly measures ΔN |
| λ (wavelength) | [λ_lo, λ_hi] | Natural sweep axis (already used in document) |
| a (pivot horizontal) | mechanical range | Secondary; b_opt = m·a + b_opt(0) is linear in a |

**Best candidate for pipeline case:** α ∈ [5°, 20°] with b fixed at sweet-spot
value −3.325 mm, sweeping systems across α-values.
Or: κ = ΔN as a function of b-deviation from b_opt — maps directly to the
isodisperse condition.

### P2 — Span-capable observable ✅ SATISFIED

Multiple clean observables:

| Observable Π | Formula | Span | Type |
|---|---|---|---|
| `delta_N` | N(λ_hi) − N(λ_lo) | ~hundreds (uncorrected) → 0 (corrected) | Direct BC effect |
| `floor_N_range` | max(⌊N(λ)⌋) − min(⌊N(λ)⌋) across λ | 0 (isodisperse) or ≥1 (not) | Binary regime indicator |
| `OWL_range` | OWL(λ_hi) − OWL(λ_lo) | system-dependent (7–24 mm) | Structural proxy |
| `b_deviation` | b − b_opt(a) | continuous, measurable | Distance to isodisperse line |

**Primary observable candidate:** `delta_N` = ΔN — directly measures the BC
condition. Span is large (many hundreds without correction, exactly 0 at isodisperse).

### P3 — Identifiable primary BC ✅ SATISFIED (with note)

**Primary BC: Coupling (S2)**

Justification: The core structural mechanism is the coupling of wavelength λ to
resonator geometry (a, b) through OWL(λ; a, b). The ΔN = 0 condition is a
specific constraint on this coupling — it selects the pivot (a, b) that makes the
coupling wavelength-neutral over [λ_lo, λ_hi].

All other BCs are secondary:
- Restriction (S1): defines the feasible design space (prerequisite, not primary mechanism)
- Forcing (S3): the grating equation is the mechanism that makes λ enter the coupling
- Aggregation (S1): the ΔN = 0 condition is the *goal*, not the BC itself
- Dissipation (S4): the sweet-spot invariance is a consequence, not the driver

**Pre-Screening verdict: ✅ PASS — pipeline-admissible**

---

## Step F — Minimal Formalization

### Proposed minimal case setup

```
System:         Littman-Metcalf resonator, single gain medium
                x₀ = 38 mm, δ = 0, a = 0 (fixed)
θ:              b ∈ [b_opt − Δ, b_opt + Δ]  (deviation from isodisperse pivot)
                or equivalently: α ∈ [5°, 20°] with b fixed at −3.325 mm
Primary BC:     Coupling (S2: OWL couples λ to geometry)
Observable Π:   delta_N = |N(λ_hi) − N(λ_lo)|
Expected:       R1: b near b_opt → delta_N ≈ 0 (isodisperse, mode-hop-free)
                R2: b deviating from b_opt → delta_N > 0 (mode hops present)
θ*:             b = b_opt(a) — analytically known transition
Sweep design:   vary b around b_opt; compute delta_N for each system in Section 4
Data:           fully analytical — no experiment needed; pipeline can run on
                computed N(λ) values from the document's formulas
```

### Why this case is particularly clean

Unlike the Shame case, this system has:
- An analytically known θ* (b_opt = m·a + b_opt(0))
- A directly computable observable (ΔN)
- No measurement protocol needed — values follow from closed-form expressions
- Seven existing system instances (UV/Vis through CO₂) as ready-made sweep points

The regime transition is also analytically sharp: ΔN = 0 is an exact condition,
not a statistical threshold. This makes ε-calibration straightforward:
ε must be small enough to distinguish ΔN = 0 from ΔN = 1.

---

## New Open Questions

| ID | Question | Status | Implication |
|---|---|---|---|
| Q-OPT-01 | Does `b_opt(0) = −x₀·tan α` (design-space fixed point) constitute a new S4 sub-signature "parametric invariance"? | open | Would extend operator_signature_catalog.md with a non-dynamical S4 instance |
| Q-OPT-02 | The sweet spot (4 systems sharing b_opt(0)) is a multi-system Transfer with Φ ≈ 1 by construction — does this qualify as a "trivial transfer" case worth documenting? | open | Transfer metrics would yield RCD=0, TBS_norm=0 by design — not by empirical coincidence |
| Q-OPT-03 | Is the β-admissibility constraint (S1) better classified as a Restriction BC or as a Scope Boundary B in the scope tuple? | open | β ∈ [26°, 56°] functions as B (boundary condition on admissible states), not as a dynamical BC |

---

## Comparison with Shame Case

| Dimension | Shame (CASE-20260315-SOC1) | Littman-Metcalf (this case) |
|---|---|---|
| Control parameter P1 | ❌ Blocked — no natural continuous θ | ✅ Clean — b, α, or ΔN deviation |
| Observable P2 | ❌ Blocked — all proxies measure inputs or consequences | ✅ Clean — ΔN is direct BC effect |
| Primary BC P3 | ❌ Blocked — three co-equal BCs | ✅ Clear — Coupling is primary |
| Data needed | Empirical dataset or experiment | None — fully analytical |
| θ* known? | Unknown a priori | Analytically exact: b_opt = m·a + b_opt(0) |
| Pipeline readiness | NOT READY | READY |

The contrast confirms the BC extraction method's diagnostic value: the Pre-Screening
step correctly distinguishes a pipeline-admissible case from a blocked one, and
the blocker taxonomy (B.1–B.7) does not trigger here.

---

*Generated: 2026-03-15*
*Method: docs/advanced/bc_extraction_method.md*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
