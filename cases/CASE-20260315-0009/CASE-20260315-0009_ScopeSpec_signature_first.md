---
status: note
layer: cases/CASE-20260315-0009/
related:
  - cases/CASE-20260311-0001/
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/quantum_operator_extension.md
  - docs/advanced/bc_extraction_method.md
---

# ScopeSpec — Signature First: Stochastic Kuramoto
# CASE-20260315-0009

---

## 1. System Identification

```
Case ID:       CASE-20260315-0009
System name:   Stochastic Kuramoto model (σ-sweep)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART
Derived from:  CASE-20260311-0001 (deterministic Kuramoto, σ=0 limit)
```

---

## 2. State Space(s)

```
Deterministic state:   θ ∈ [0,2π)^N  (N=100 oscillator phases)
Stochastic extension:  X × Ω  (phases × probability space of noise realizations)
SDE:                   dθ_i = [ω_i + κ/N·Σsin(θⱼ−θᵢ)] dt + σ dW_i
Fixed parameters:      κ = 2.0, N = 100, ω_i ~ N(0,1) frozen
Sweep parameter:       σ ∈ [0.0, 3.0]  (noise intensity)
```

The state space extension X × Ω is the formal S5a structure. Unlike S3
(X × T, deterministic forcing), S5 extends X by a probability space Ω —
each noise realization ω ∈ Ω is a distinct trajectory. The observable
r_mean is then an integral over Ω: r_mean = ∫_Ω r(θ(t;ω)) dP(ω).

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Coupling dynamics composed with noise forcing |
| Product `×` | ✅ yes | State × probability space: θ × Ω; also sin cross terms |
| Projection `π` | ✅ yes | Ensemble average: π_Ω : trajectories → r_mean (expectation projection) |
| Tensor `⊗` | ☐ N/A | Classical |
| Cond. exp. `E[·\|G]` | ✅ **yes — primary** | r_mean = E[r(θ) \| σ] — L²(Ω) projection |

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ partial — via ensemble average
Form:          π_Ω: {trajectories} → r_mean  (projects ensemble onto scalar)
Sub-signature: expectation as projection (connects to S5)
Idempotent?:   ✅ yes — E[E[r|σ]|σ] = E[r|σ]  (tower law)
```

### S2 — Coupling  ✅ secondary

```
Present:       ✅ yes — κ=2.0 fixed
Form:          κ/N·Σsin(θⱼ−θᵢ) — same as CASE-0001
Sub-signature: Cartesian coupling (N oscillators)
Cross terms?:  ✅ yes
```

### S3 — Forcing

```
Present:       ☐ not present — W_i is white noise, not periodic forcing
Note:          σdW_i is stochastic, not deterministic periodic — S5, not S3.
               Key distinction: S3 = deterministic time-indexed input;
               S5 = stochastic probability-space input.
```

### S4 — Dissipation

```
Present:       ☐ not present as primary
Note:          Noise acts as effective temperature — analogous to thermal
               dissipation in statistical physics. But this is an analogy,
               not the S4 operator. No explicit contraction term in the SDE.
```

### S5 — Expectation as Projection  ✅ **primary**

```
Present:       ✅ yes — primary signature
Form:          State space extension: X ↦ X × Ω
               Primary observable:
               r_mean(σ) = E[|1/N·Σexp(iθⱼ)| | σ]
               = Proj_{L²(Ω,σ)}(r(θ))
Sub-signature: discrete conditional expectation
               (M=100 realizations as sample approximation)
Idempotent?:   ✅ yes — tower law
```

**Why this is S5 and not S3:**

| Property | S3 (Forcing) | S5 (Stochastic) |
|---|---|---|
| Extension | X × T (deterministic time) | X × Ω (probability space) |
| Input | Periodic/deterministic f(t) | Random W_i(t) |
| Observable | Time-averaged trajectory value | Ensemble-averaged expectation |
| Reduction | Stroboscopic section (S1) | Conditional expectation (S5) |
| Idempotent? | Section: yes | E[·\|σ]: yes (tower law) |

**First case where the primary observable IS an S5 operator:**
r_mean is not just a scalar extracted from trajectories — it is the
conditional expectation operator applied to r(θ). The observable and
the signature are the same mathematical object.

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ☐ no | — | |
| Coupling | ✅ secondary | S2: κ=2.0 cross terms | Established by CASE-0001 |
| Aggregation | ☐ no | — | |
| Symmetry Breaking | ☐ no | — | |
| Forcing | ☐ no | — | White noise ≠ periodic forcing |
| Dissipation | ☐ no | — | No explicit contraction term |
| Stochastic BC | ✅ **primary** | S5: r_mean = E[r\|σ] | First S5-primary case in repo |

**Primary BC class:** `Stochastic_BC`

---

## 6. Regime Partition

```
Control parameter θ:      σ  (noise intensity)
Sweep range:              σ ∈ [0.0, 3.0], 31 points, linear
Expected regimes N:       2
  R1 (σ < σ_c):  noise-tolerant — r_mean high
                  Coupling dominates noise; E[r|σ] projects onto
                  synchronized state
  R2 (σ > σ_c):  noise-dominated — r_mean low
                  Noise destroys synchronization; E[r|σ] → 0
Transition θ*:    σ_c — unknown a priori
                  Mean-field estimate: σ_c ≈ κ/2 ≈ 1.0
                  (noise-coupling balance in Fokker-Planck equation)
Transition type:  Continuous crossover (stochastic transitions are
                  typically smooth, not sharp bifurcations)
Validation:       r_mean(σ=0) must match r_ss(κ=2.0) from CASE-0001 ≈ 0.73
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `r_mean` | `E_Ω[\|1/N·Σexp(iθ_j)\|]` | ✅ yes | ~0.73 to ~0 | ✅ sufficient |
| `r_variance` | `Var_Ω[r]` over M realizations | ☐ candidate | peaks at σ_c | ☐ pending |
| `r_ss_det` | CASE-0001 r_ss at κ=2.0 (anchor) | ☐ no | — | ✅ anchor only |

### Perturbations Δ

```
Type 1 — noise realization:  M=100 independent {W_i(t)} per σ-value
Type 2 — frequency disorder:  5 resamples of ω_i ~ N(0,1)
Robustness target:             r_mean stable across both perturbation types
Note:                          σ_c may shift slightly across ω resamples
                               (finite-N effect) — accept ±5% as robust
```

### Resolution ε

```
Working ε:      0.08  (pre-estimate; span ≈ 0.73 → span/ε ≈ 9)
Concern:        Stochastic transitions are smooth — plateau may be
                narrow or absent. r_variance peak may be more robust
                indicator of σ_c than r_mean inflection.
Fallback:       If r_mean gives no plateau: use r_variance as primary
                observable and rerun epsilon_sweep.
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(r_mean) < ε` | `scope_rejection` | Verify κ=2.0 produces r≈0.73 at σ=0 |
| F2 | σ_c shifts > 10% across ω resamples | `scope_rejection` | Increase N or resamples |
| F3 | No robust ε plateau in r_mean | `scope_rejection` | Try r_variance as primary observable |
| F4 | σ_c at boundary | `sweep_refinement` | Extend range |
| F-STOCH | No plateau in r_variance either | `open_question` | S5 cases may be fundamentally non-partitionable by ε-clustering — fundamental finding |
| F-SDE | Euler-Maruyama incompatible with pipeline | `modeling_error` | Extend sweep.py for SDE |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0001 (Kuramoto, Coupling) | 2 | ~0.33 | partially_admissible | Same system; σ=0 anchor; different BC class |
| CASE-20260315-0004 (Stuart-Landau, Dissipation) | 0–1 | TBD | partially_admissible | Both use order-parameter-like observables; different BC |

---

## 10. Checklist

- [x] S5 operator formally identified as primary
- [x] Distinction S3 (deterministic forcing) vs S5 (stochastic) documented
- [x] r_mean formally identified as conditional expectation (not just average)
- [x] Euler-Maruyama integration requirement documented
- [x] σ=0 validation anchor to CASE-0001 specified
- [x] F-STOCH failure mode for fundamental non-partitionability
- [x] Q-STOCH-01/02 open questions registered
- [ ] Pipeline SDE compatibility verified (F-SDE check)
- [ ] ε confirmed by epsilon_sweep
- [ ] Invariants.json pending (sweep_range: [0.0, 3.0])
- [ ] go_nogo: pending

**Pipeline readiness: CONDITIONALLY READY**
Prerequisite: verify sweep.py supports Euler-Maruyama SDE integration
and M-realization ensemble averaging.

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
