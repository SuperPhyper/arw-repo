---
status: note
layer: cases/CASE-20260315-0008/
related:
  - cases/CASE-20260315-0004/
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/bc_extraction_method.md
---

# ScopeSpec — Signature First: Pitchfork Normal Form
# CASE-20260315-0008

---

## 1. System Identification

```
Case ID:       CASE-20260315-0008
System name:   Pitchfork bifurcation normal form (μ-sweep)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART
```

---

## 2. State Space(s)

```
State space X:         x ∈ ℝ  (scalar real)
Equation of motion:    dx/dt = μ·x − x³
Symmetry group:        Z₂: x → −x  (preserved for all μ; broken spontaneously above μ=0)
Sweep parameter:       μ ∈ [−2.0, 2.0]
Fixed parameters:      none
```

The state space is minimal — scalar, one degree of freedom. This makes the
Pitchfork the simplest possible Symmetry Breaking system.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Linear growth `μx` composed with cubic dissipation `−x³` |
| Product `×` | ✅ yes | `x³ = x · x · x` — self-product; state-dependent contraction |
| Projection `π` | ✅ yes | Basin selection above μ=0: trajectory projects onto one of {x>0, x<0} |
| Tensor `⊗` | ☐ N/A | |
| Cond. exp. `E[·\|G]` | ☐ N/A | |

---

## 4. Derived Signatures

### S1 — Projection / Selection  ✅ primary

```
Present:       ✅ yes
Form:          Below μ=0: π: ℝ → {0}  (unique attractor)
               Above μ=0: π: ℝ → {−√μ} or {+√μ}  (basin-dependent selection)
Sub-signature: selection under parameter variation (parametric multiplicity)
Idempotent?:   ✅ yes — within each basin
```

**What makes this Symmetry Breaking rather than Restriction:**
In Restriction (CASE-0003), the projection is onto a *pre-existing* subspace.
Here, the two attractors ±√μ do not exist below μ=0 — they emerge at the
bifurcation. The projection operator itself changes at μ=0: from a single-point
projector to a two-branch selector. This parameter-dependent emergence of the
projection target is the structural hallmark of Symmetry Breaking.

### S2 — Coupling

```
Present:       ☐ not present — scalar system
```

### S3 — Forcing

```
Present:       ☐ not present — autonomous
```

### S4 — Dissipation  ✅ secondary

```
Present:       ✅ yes — secondary
Form:          −x³: cubic state-dependent contraction
               d/dt(x₁−x₂) ≈ (μ − 3x*²)(x₁−x₂) — contractive near attractor
Sub-signature: nonlinear metric contraction (same family as Stuart-Landau −|z|²z)
Contraction?:  ✅ at x* = ±√μ: linearization eigenvalue = −2μ < 0 for μ>0
```

**Structural twin relationship with CASE-0004 (Stuart-Landau):**

| Property | Pitchfork (CASE-0008) | Stuart-Landau (CASE-0004) |
|---|---|---|
| Nonlinear term | −x³ | −\|z\|²z |
| Observable | x_ss_abs = √(max(μ,0)) | r_ss = √(max(μ,0)) |
| θ* | μ_c = 0 | μ_c = 0 |
| Symmetry broken | Z₂ (discrete) | U(1) (continuous) |
| Primary BC | Symmetry Breaking | Dissipation |

Same observable form, same θ*, different primary BC class. This pair is
the most controlled comparison in the repo for testing Φ sensitivity.

### S5 — Expectation

```
Present:       ☐ not present — deterministic
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ secondary | S1: basin boundary x=0 as separator above μ=0 | Emerges above μ=0; not present below |
| Coupling | ☐ no | — | Scalar system |
| Aggregation | ☐ no | — | No coarse-graining |
| Symmetry Breaking | ✅ **primary** | S1: parameter-dependent selection onto ±√μ | Z₂ broken spontaneously at μ=0 |
| Forcing | ☐ no | — | Autonomous |
| Dissipation | ✅ secondary | S4: −x³ stabilizes symmetry-broken attractors | Structural, not primary BC |

**Primary BC class:** `Symmetry_Breaking`

---

## 6. Regime Partition

```
Control parameter θ:      μ
Sweep range:              μ ∈ [−2.0, 2.0], 41 points, linear
Expected regimes N:       2
  R1 (μ < 0):  symmetric regime — x* = 0
               Z₂ symmetry intact; unique stable fixed point
  R2 (μ > 0):  symmetry-broken regime — x* = ±√μ
               Two stable fixed points; Z₂ broken spontaneously
Transition boundary θ*:   μ_c = 0  (analytically exact, same as CASE-0004)
Transition type:          Supercritical pitchfork bifurcation
Observable at transition: x_ss_abs = √(max(μ,0)) — continuous onset
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span | Sufficient? |
|---|---|---|---|---|
| `x_ss_abs` | `mean(\|x(t→∞)\|)` over ±IC | ✅ yes | 0 to √2 ≈ 1.414 | ✅ |
| `x_ss_signed` | `x(t→∞)` per IC sign | ☐ no | ±√μ | ✅ (branch diagnostic) |
| `lambda_proxy` | `μ − 3x*²` at attractor | ☐ no | crosses 0 at μ=0 | ✅ |

### Perturbations Δ

```
IC set:      {−1.0, −0.5, −0.1, +0.1, +0.5, +1.0}
Protocol:    x_ss_abs = mean of |x_ss| over all IC values
             x(0) = 0 excluded (unstable manifold above μ=0)
Robustness:  x_ss_abs must be identical for all nonzero IC values
             (global basin — both branches give same |x_ss_abs|)
```

### Resolution ε

```
Working ε:   0.08   (same as CASE-0004 — enables direct ε comparison)
Span/ε:      1.414 / 0.08 ≈ 18
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(x_ss_abs) < ε` | `scope_rejection` | Verify −x³ term present |
| F2 | μ* shifts under IC variation | `scope_rejection` | Exclude x(0)=0; use symmetric IC set |
| F3 | No robust ε plateau near μ=0 | `scope_rejection` | Increase point density near μ=0 |
| F4 | μ* at boundary | `sweep_refinement` | Cannot happen: μ*=0 is center of [−2,2] |
| F-SYM | x_ss_signed consistently picks one branch | `open_question` | Broken ergodicity finding; not scope rejection |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-0004 Stuart-Landau | 0 | 0.0 | highly_admissible (prediction) | Identical observable, θ*, span — only BC class differs |
| CASE-0007 SIR | 0 | ~0.20 | partially_admissible | Both N=2, both analytical θ*, different domain |
| CASE-0001 Kuramoto | 2 | ~0.26 | partially_admissible | Kuramoto transition is also symmetry-breaking in phase space |

**Key scientific prediction:** CASE-0008 ↔ CASE-0004 transfer should yield
the highest Φ score of any cross-BC-class transfer in the repo, because the
observable structure is identical. If Φ is high, it means the transfer metric
is dominated by observable similarity, not BC class. If Φ is low despite
identical observables, BC class has independent structural weight in Φ.

---

## 10. Checklist

- [x] Z₂ symmetry and its breaking formally documented
- [x] Distinction from Restriction (emergent vs pre-existing projection) documented
- [x] Structural twin relationship with CASE-0004 documented
- [x] IC protocol: symmetric set, x(0)=0 excluded
- [x] Three sufficient observables identified
- [x] Q-SYM-01 registered as scientific prediction
- [ ] ε confirmed by epsilon_sweep
- [ ] Invariants.json pending (sweep_range: [−2.0, 2.0])
- [ ] go_nogo: pending

**Pipeline readiness: READY**

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
