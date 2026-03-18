---
status: note
layer: cases/CASE-20260318-0004/
related:
  - docs/advanced/bc_operator_signatures_arw.md
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/arw_emergence_bc_relative.md
  - docs/advanced/bc_relative_observable_indistinguishability.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
---

# ScopeSpec — Signature First: Two Coupled Stuart-Landau Oscillators
# CASE-20260318-0004

---

## 1. System Identification

```
Case ID:       CASE-20260318-0004
System name:   Two coupled Stuart-Landau oscillators (supercritical Hopf normal form)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART (concrete system)
Purpose:       First empirical ARW emergence case — relational collapse window
```

---

## 2. State Space(s)

```
Primary state space X:    ℂ × ℂ  (joint complex amplitude of two oscillators)
                          equivalently ℝ⁴  with (x1, y1, x2, y2)
Equations of motion:
  dz_i/dt = (λ_i + iω_i - (1+iα)|z_i|²)z_i + K(z_j - z_i)

Fixed parameters:
  ω1 = 1.00, ω2 = 1.08  (frequency mismatch Δω = 0.08)
  α  = 0.20              (amplitude-phase coupling)
  λ  = 1.00, dlambda = 0.08  → λ1 = 1.08, λ2 = 0.92
  t_transient = 50, T = 200, dt = 0.01

Sweep parameter:  K ∈ [0.01, 0.12]  (coupling strength, 12 points)
```

The joint state space X = ℂ × ℂ is the natural carrier for S2:
both oscillators live in their own ℂ, coupled diffusively.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Growth `(λ_i+iω_i)z_i` composed with dissipation `−|z_i|²z_i` |
| Product `×` | ✅ yes | Joint state ℂ × ℂ; coupling term `K(z_j − z_i)` mixes factors |
| Projection `π` | ✅ yes (observable) | `plv = |mean(exp(i·Δφ))|` projects phase difference onto [0,1] |
| Tensor product `⊗` | ☐ N/A | Classical system |
| Conditional expectation `E[·\|G]` | ☐ N/A | Deterministic system |

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ yes (observable projection)
Form:          PLV = |mean(exp(i*(φ1(t) - φ2(t))))| : trajectory → [0,1]
               amp_asym = |mean|z1| - mean|z2|| : trajectory → [0,∞)
Sub-signature: measurement projection onto scalar observable space
Idempotent?:   ✅ yes (applying PLV twice gives same result)
Note:          amp_asym collapses under ε = 0.09 for all K (Π_local collapse).
               PLV distinguishes regimes (Π_rel persistence).
               This asymmetry IS the emergence condition.
```

### S2 — Product ∘ Composition (Coupling)

```
Present:       ✅ yes — PRIMARY signature
Form:          X_joint = ℂ × ℂ
               F(z1,z2) = (f(z1,z2), g(z2,z1))
               f(z1,z2) = (λ1+iω1-|z1|²)z1 + K(z2-z1)
               g(z2,z1) = (λ2+iω2-|z2|²)z2 + K(z1-z2)
Cross terms?:  ✅ yes — K(z_j - z_i) mixes z1 and z2
Coupling type: diffusive (symmetric)
K* ≈ 0.055:   incoherent → phase-locked transition
```

This is the canonical S2 instance: a product state space with cross-terms
in the dynamics. K is the sweep parameter; K* is the transition boundary.

### S3 — Time-Coupled Product (Forcing)

```
Present:       ☐ not present
Form:          N/A — autonomous system, no explicit time dependence
Note:          dz/dt = f(z; K) with no t-argument. K is fixed per run.
```

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:       ✅ yes (per oscillator)
Form:          Dissipation term per oscillator: −|z_i|²z_i
               Same S4 signature as CASE-20260315-0004 (single SL)
Role here:     Secondary — sets limit cycle amplitude (constrains observable span)
               Not the sweep axis; K is.
Note:          The S4 term is what makes amp_asym collapse:
               each oscillator is attracted to its own |z_i*| = sqrt(λ_i),
               so amplitude asymmetry = |sqrt(λ1) - sqrt(λ2)| ≈ constant.
               The constancy of amp_asym under K-variation is due to S4.
```

### S5 — Expectation / Conditional Expectation

```
Present:       ☐ not present
Form:          N/A — deterministic system
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ☐ no | — | No hard state-space cut |
| Coupling | ✅ **primary** | S2: ℂ×ℂ product with K-cross-terms | Canonical. K is sweep parameter. |
| Aggregation | ☐ no | — | No coarse-graining of state space |
| Symmetry Breaking | ☐ secondary candidate | Phase coherence breaks U(1) × U(1) → U(1) at K* | Not primary focus |
| Forcing | ☐ no | — | Autonomous system |
| Dissipation | ☐ secondary | S4 per oscillator | Amplitude-fixing, not sweep axis |

**Primary BC class:** `Coupling`

---

## 6. Regime Partition

```
Control parameter θ:    K  (coupling strength)
Sweep range:            K ∈ [0.01, 0.12]
Expected regimes N:     2
  R1 (K < K*):  incoherent — PLV ≈ 0.16–0.68, amp_asym ≈ 0.082
                oscillators oscillate at different effective frequencies
  R2 (K > K*):  phase-locked — PLV = 1.0, amp_asym ≈ 0.076
                oscillators lock to common phase; freq_gap → 0
Transition K*:          ≈ 0.055–0.06  (empirical, between sweep points 5 and 6)
Transition type:        sharp (PLV jumps in one step)
```

**Key asymmetry between observables:**
- PLV spans [0.158, 1.000] = span 0.842 → SUFFICIENT (relational)
- amp_asym spans [0.073, 0.082] = span 0.009 → INSUFFICIENT (local)

This is not a measurement problem. It is the emergence structure.

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span | Sufficient? | Role |
|---|---|---|---|---|---|
| `plv` | `\|mean(exp(i·Δφ))\|` | ✅ yes | 0.842 | ✅ yes | Π_rel — relational |
| `amp_asym` | `\|mean\|z1\| - mean\|z2\|\|` | ☐ no | 0.009 | ☐ no | Π_local — collapses under ε |
| `freq_gap` | `\|mean(dφ1/dt) - mean(dφ2/dt)\|` | ☐ no | 0.110 | ✅ yes | Secondary relational |

### Emergence Window (ε-analysis)

```
Local threshold:     ε_local  = amp_asym(K_weak) = 0.082
                     For ε > 0.082: local description collapses
Relational threshold: ε_rel  = ΔPLV = |PLV(K=0.08) - PLV(K=0.03)| = 0.805
                     For ε < 0.805: relational distinction survives
Emergence window:    ε ∈ (0.082, 0.805)
Window width:        0.723  (wide; robust)
Working ε = 0.09:    interior (0.082 < 0.09 < 0.805) ✅
```

### Perturbations Δ

```
delta_01:  IC perturbation — z_i(0) within disk |z_i(0)| < 0.5
           Tests basin robustness (global attractors exist for all K)
delta_02:  Lambda-sweep — λ ∈ [0.4, 1.6] at fixed weak/strong K
           Tests BC-relative stability of emergence window
           Result: stable for λ ∈ [0.4, 1.3]; breaks at λ > 1.3 (weak K)
```

---

## 8. Failure Modes

| ID | Condition | Severity | Empirical status |
|---|---|---|---|
| F1 | span(PLV) < ε — coupling has no relational effect | scope_rejection | ❌ NOT triggered: span=0.842 |
| F2 | amp_asym > ε at phase-locked K — emergence absent | scope_rejection | ❌ NOT triggered: 0.076 < 0.09 |
| F3 | No robust ε plateau — window width < 0.5 | scope_rejection | ❌ NOT triggered: width=0.723 |
| F4 | K* at sweep boundary | sweep_refinement | ❌ NOT triggered: K*≈0.055 interior |

---

## 9. ARW Emergence Analysis

This case is the first explicit numerical instantiation of the ARW emergence
definition from `arw_emergence_bc_relative.md` (Section 4).

**Formal correspondence:**

| ARW concept | This case |
|---|---|
| Local observable O | amp_asym |
| Relational observable C | PLV |
| BC α | K (coupling strength) |
| Local collapse condition | amp_asym < ε = 0.09 for all K |
| Relational persistence condition | ΔPLV = 0.805 > ε = 0.09 |
| Emergence window | ε ∈ (0.082, 0.805) |
| BC-relative stability | Holds for λ ∈ [0.4, 1.3]; λ-bounded |

**Interpretation:**
Emergence here is not a new property appearing spontaneously.
It is a resolution-dependent asymmetry: at ε = 0.09, the local amplitude
description is indistinguishable (collapsed), while the relational phase
structure remains the only admissible description. The partition is entirely
carried by Π_rel (PLV), not Π_local (amp_asym).

---

## 10. Transfer Pre-Assessment

| Target | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-0001 (Kuramoto/Coupling) | 0 | ~0.3 | partially_admissible | Same BC class, N=2, different observable (PLV vs r_ss) |
| CASE-20260315-0004 (single SL/Dissipation) | 0 | ~0.5 | partially_admissible | Same system type, different BC class and observable |

---

*Generated: 2026-03-18*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
