---
status: note
layer: cases/CASE-20260315-0007/
related:
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/cross_domain_signature_matrix.md
  - docs/advanced/bc_extraction_method.md
---

# ScopeSpec — Signature First: SIR Epidemic Model
# CASE-20260315-0007

---

## 1. System Identification

```
Case ID:       CASE-20260315-0007
System name:   SIR epidemic model (β-sweep)
Domain:        EPI — Epidemiology / Social Systems
ARW level:     ART
```

---

## 2. State Space(s)

```
Micro state space:    {0,1,2}^N  (N individuals, each susceptible/infected/recovered)
Macro state space X:  (S,I,R) ∈ [0,1]³,  S+I+R = 1  (compartment fractions)
Aggregation map:      π_SIR : {0,1,2}^N → [0,1]³
Fixed params:         γ_r = 0.1, N = 10000, S₀=0.99, I₀=0.01
Sweep parameter:      β ∈ [0.0, 0.5]  (transmission rate)
```

**Key structural point:** The macro state space (S,I,R) is not a simplification
of the micro space — it IS the Aggregation BC in action. The model is defined
at the macro level; the micro level exists only to motivate the operator.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Infection dynamics: β·S·I composed with recovery −γ_r·I |
| Product `×` | ✅ yes | S·I product term (bilinear coupling between compartments) |
| Projection `π` | ✅ yes | π_SIR: micro {0,1,2}^N → macro (S,I,R) — constitutive |
| Tensor product `⊗` | ☐ N/A | Classical |
| Cond. expectation `E[·\|G]` | ☐ N/A | Deterministic ODE |

---

## 4. Derived Signatures

### S1 — Projection / Selection  ✅ primary (quotient form)

```
Present:       ✅ yes — constitutive (the model IS the projection)
Form:          π_SIR : {0,1,2}^N → [0,1]³
               (S,I,R) = (|susceptible|/N, |infected|/N, |recovered|/N)
Sub-signature: quotient / coarse-graining projection
Idempotent?:   ✅ yes — applying π_SIR twice returns the same macro state
```

**Critical distinction from Restriction (CASE-0003):**
- Restriction (S1 selection): selects a *subset* of existing states
- Aggregation (S1 quotient): *identifies* distinct micro-states as equivalent,
  mapping many-to-one onto macro-states

Both are S1, but the sub-signature and BC semantics differ. This case is
the first in the repo to use S1 in its quotient form.

**Secondary S1 — admissibility restriction:**
```
Form:          S + I + R = 1  constrains state to 2-simplex Δ²
Sub-signature: admissibility selection (Restriction sub-form)
```

### S2 — Product ∘ Composition (Coupling)

```
Present:       ✅ partial — bilinear interaction only
Form:          β · S · I  (product of two compartment fractions)
Note:          This is not agent-level coupling (S2 in full sense) but
               a mean-field approximation. The product S·I represents
               the expected collision rate under homogeneous mixing.
               True agent-level coupling would require a network model.
```

### S3 — Forcing

```
Present:       ☐ not present (β fixed per sweep point)
Latent:        β = β(t) would activate S3 — seasonal SIR is an S3 case.
               This case deliberately uses constant β to isolate Aggregation.
```

### S4 — Dissipation

```
Present:       ☐ not present as primary
Note:          −γ_r·I is a linear decay term (S4 sub-form), but recovery
               is part of the SIR dynamics, not an added dissipation.
               Plays a structural role but is not the primary BC mechanism.
```

### S5 — Expectation as Projection

```
Present:       ☐ not present in deterministic ODE form
Note:          Stochastic SIR would activate S5 — see CASE-0009 for the
               stochastic pattern. Here ODE formulation is used deliberately.
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ secondary | S1 selection: S+I+R=1 constraint | Structural; not the primary mechanism |
| Coupling | ✅ partial | S2: β·S·I mean-field product | Mean-field only; not agent-level |
| Aggregation | ✅ **primary** | S1 quotient: π_SIR micro→macro | Constitutive — the model IS the aggregation |
| Symmetry Breaking | ☐ no | — | No symmetry change across β-sweep |
| Forcing | ☐ latent | S3: β(t) would activate | Constant β here |
| Dissipation | ☐ partial | S4: −γ_r·I recovery decay | Part of dynamics; not primary BC |

**Primary BC class:** `Aggregation`

---

## 6. Regime Partition

```
Control parameter θ:      β  (transmission rate)
Sweep range:              β ∈ [0.0, 0.5], 51 points, linear
Expected regimes N:       2
  R1 (β < β*):  sub-threshold — no epidemic
                I(t) → 0 monotonically; I_peak ≈ I(0) = 0.01
  R2 (β > β*):  super-threshold — epidemic wave
                I(t) rises to I_peak then decays; I_peak >> I(0)
Transition boundary θ*:   β* = γ_r / S(0) = 0.1/0.99 ≈ 0.1010
                          Analytically exact — transcritical bifurcation (R₀=1)
Transition type:          Transcritical bifurcation
                          I_peak continuous at β* (no jump) — similar to
                          Stuart-Landau (CASE-0004): smooth onset
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `I_peak` | `max_t I(t)` | ✅ yes | ~0.01 to ~0.80 | ✅ sufficient |
| `R_final` | `lim_{t→∞} R(t)` | ☐ no | ~0 to ~0.95 | ✅ sufficient |
| `lambda_proxy` | `(β·S₀ − γ_r)·I₀` at t=0 | ☐ no | crosses zero at β* | ✅ sufficient |

**Note:** This is the first case with three simultaneously sufficient
observables — useful for multi-observable agreement testing
(`epsilon_multi_observable.py`).

### Perturbations Δ

```
Perturbation type:    I(0) ∈ [0.005, 0.02], S(0) = 1−I(0), R(0) = 0
n_runs:               10 per β-value
Robustness:           β* = 0.101 is structural (R₀=1) — independent of I(0)
                      Partition should be fully stable under IC variation
```

### Resolution ε

```
Working ε:            0.05
Span / ε:             I_peak span ≈ 0.79; span/ε ≈ 16 — well sufficient
Plateau expected:     wide — analytical threshold produces clear step in I_peak
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(I_peak) < ε` | `scope_rejection` | Verify integration; check γ_r value |
| F2 | β* shifts under I(0) variation | `scope_rejection` | Check for finite-size effects; use N=10000 |
| F3 | No robust ε plateau | `scope_rejection` | Increase integration time to t=1000 |
| F4 | β* at boundary | `sweep_refinement` | Theoretical β*=0.101 is interior; unlikely |
| F-AGG | lambda_proxy and I_peak disagree on β* | `open_question` | Documents multi-observable disagreement; not scope rejection |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0003 (Doppelpendel, Restriction) | 7 | ~0.45 | inadmissible (raw) | Different BC sub-signature (quotient vs selection); high RCD |
| CASE-20260315-0008 (Pitchfork, Sym. Breaking) | 0 | ~0.20 | partially_admissible | Both N=2, both analytically known θ*; different BC |
| CASE-20260315-SOC1 (Shame, blocked) | TBD | TBD | TBD | SIR as EPI anchor for SOC transfer validation |

---

## 10. Checklist

- [x] Aggregation operator π_SIR formally defined
- [x] Distinction from Restriction (quotient vs selection) documented
- [x] Three sufficient observables identified
- [x] Analytical θ* = 0.101 confirmed as interior
- [x] Latent Forcing (β(t)) documented but excluded by design
- [x] Failure mode F-AGG for multi-observable disagreement
- [ ] ε confirmed by epsilon_sweep
- [ ] Multi-observable agreement run via epsilon_multi_observable.py
- [ ] Invariants.json pending (sweep_range: [0.0, 0.5])
- [ ] go_nogo: pending

**Pipeline readiness: READY**

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
