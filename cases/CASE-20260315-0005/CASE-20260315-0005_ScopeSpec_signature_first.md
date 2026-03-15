---
status: note
layer: cases/CASE-20260315-0005/
related:
  - cases/CASE-20260311-0002/
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/bc_extraction_method.md
---

# ScopeSpec — Signature First: Multi-Pendel + Damping
# CASE-20260315-0005

---

## 1. System Identification

```
Case ID:       CASE-20260315-0005
System name:   Multi-Link-Pendel with joint damping (γ-sweep)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART
Derived from:  CASE-20260311-0002 (same system, κ fixed, γ swept)
```

---

## 2. State Space(s)

```
Primary state space X:   τ ∈ [-π,π]^n × ℝ^n  (joint angles + velocities)
Fixed parameters:        κ = 3.25  (above Coupling transition from CASE-0002)
                         ω_i distribution: same as CASE-0002
Sweep parameter:         γ ∈ [0.0, 5.0]  (joint damping coefficient)
Equation of motion:      τ̈ = f(τ, τ̇; κ) − γ · τ̇
```

The key structural point: at γ = 0 this system is identical to CASE-0002
at κ = 3.25. The γ-sweep adds the Dissipation dimension to an already
fully characterized Coupling baseline.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Coupling dynamics `f(τ,τ̇;κ)` composed with damping `−γτ̇` |
| Product `×` | ✅ yes | Joint state space `τ × τ̇`; coupling cross terms between joints |
| Projection `π` | ✅ asymptotic | High-γ attractor: τ̇ → 0 (overdamped fixed point) |
| Tensor product `⊗` | ☐ N/A | Classical system |
| Cond. expectation `E[·\|G]` | ☐ N/A | Deterministic |

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ asymptotically (γ → ∞)
Form:          π_damp : (τ, τ̇) → (τ_eq, 0)  as t → ∞
               overdamped fixed point: all velocity components → 0
Idempotent?:   ✅ asymptotically only — Q-DISS-01 applies
```

### S2 — Product ∘ Composition (Coupling)

```
Present:       ✅ yes — secondary (κ = 3.25 fixed)
Form:          f(τ_i, τ_j) — coupling cross terms between joints i,j
Sub-signature: Cartesian coupling, same as CASE-0002
Cross terms?:  ✅ yes — established by CASE-0002
```

S2 is structurally present throughout the entire γ-sweep. The scientific
question is: at what γ* does S4 (Dissipation) dominate S2 (Coupling) in
determining the observable regime structure?

### S3 — Time-Coupled Product (Forcing)

```
Present:       ☐ not present
Form:          N/A — autonomous system at all γ values
```

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:       ✅ yes — primary signature
Form:          Damping term: −γ · τ̇
               Linear velocity contraction per joint
Sub-signature: exponential decay (linear damping)
Contraction?:  ✅ exponential decay: ‖τ̇(t)‖ ≤ ‖τ̇(0)‖ · exp(−γt)
               (upper bound, neglecting coupling energy injection)
Rate c:        c = exp(−γ · Δt)  — tunable via sweep parameter
```

**S4 vs S2 competition:** This case is structurally a competition between
two signatures: S4 (Dissipation, γ-controlled) and S2 (Coupling, κ-fixed).
At low γ: S2 dominates → cooperative dynamics (same as CASE-0002).
At high γ: S4 dominates → all motion suppressed.
γ* is the crossover point — not a sharp bifurcation but a continuous
transition in var_rel.

### S5 — Expectation as Projection

```
Present:       ☐ not present
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ asymptotic | S1: overdamped fixed point in γ→∞ limit | Q-DISS-01 applies |
| Coupling | ✅ secondary | S2: κ=3.25 fixed; cross terms present throughout | Established by CASE-0002 |
| Aggregation | ☐ no | — | No coarse-graining |
| Symmetry Breaking | ☐ no | — | No symmetry change across γ-sweep |
| Forcing | ☐ no | — | Autonomous system |
| Dissipation | ✅ **primary** | S4: `−γτ̇` linear velocity contraction | Tunable, dominant at γ > γ* |

**Primary BC class:** `Dissipation`

---

## 6. Regime Partition

```
Control parameter θ:      γ  (joint damping coefficient)
Sweep range:              γ ∈ [0.0, 5.0], 26 points, linear spacing
Expected regimes N:       2
  R1 (γ < γ*):  coupling-dominated — var_rel high
                 Dissipation present but Coupling sustains cooperative motion
  R2 (γ > γ*):  dissipation-dominated — var_rel low
                 All joint motion suppressed; system approaches rest
Transition boundary θ*:   γ* unknown a priori — to be determined by pipeline
                           Expected in range γ* ∈ (0.5, 3.0) based on
                           κ = 3.25 energy injection estimate
Validation anchor:        γ = 0 must reproduce CASE-0002 result at κ = 3.25
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `var_rel` | `Var(τ_i) / Var_max` normalized joint variance | ✅ yes | 0 to ~1.0 | ✅ yes |
| `energy_ss` | `0.5 · Σ(τ̇_i²)` steady-state kinetic energy | ☐ candidate | monotone decay with γ | ☐ pending |
| `lambda_proxy` | local divergence rate proxy | ☐ no | low span expected | ☐ insufficient |

**Observable continuity with CASE-0002:** var_rel is identical to the
primary observable in CASE-0002. This enables direct comparison:
CASE-0002 var_rel(κ) vs CASE-0005 var_rel(γ) — same observable, different
parameter axis. Transfer metrics will be computable on a shared scale.

### Perturbations Δ

```
Perturbation type:    IC variation: τ(0) ∈ [-0.1, 0.1]^n, τ̇(0) = 0
n_runs:               10 per γ-value
Protocol:             identical to CASE-0002 for comparability
```

### Resolution ε

```
Working ε:            0.05  (conservative pre-estimate)
Basis:                CASE-0002 ε_working = 0.023; damping expected
                      to produce wider span → larger ε tolerable
Plateau status:       pending epsilon_sweep
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(var_rel) < ε` across all γ | `scope_rejection` | Verify κ=3.25 produces nonzero var_rel at γ=0 |
| F2 | `γ*` unstable across IC runs | `scope_rejection` | Increase n_runs |
| F3 | No robust ε plateau | `scope_rejection` | Extend integration time; increase t_transient |
| F4 | `γ*` at sweep boundary | `sweep_refinement` | Extend range |
| F-ANC | γ=0 does not reproduce CASE-0002 at κ=3.25 | `modeling_error` | Check equation of motion; implementation error |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0002 (same system, κ-sweep) | 1 | low (same system) | highly_admissible | Same observable var_rel; γ=0 is exact anchor |
| CASE-20260315-0004 (Stuart-Landau, Dissipation) | 1–2 | TBD | partially_admissible | Same BC class, different observable (var_rel vs r_ss) |
| CASE-20260315-0006 (same system, Ω-sweep, Forcing) | 1–2 | TBD | partially_admissible | Same system, different BC; coordinated pair |

---

## 10. Checklist

- [x] State space continuous and smooth
- [x] Primary BC (Dissipation) justified by S4 signature
- [x] Secondary BC (Coupling) documented and justified
- [x] Primary observable: var_rel — same as CASE-0002
- [x] Validation anchor: γ=0 → CASE-0002 result
- [x] Sweep range covers expected γ* interior
- [x] Failure modes F1–F4 + F-ANC documented
- [ ] ε confirmed by epsilon_sweep
- [ ] PartitionResult.json pending
- [ ] Invariants.json pending (sweep_range: [0.0, 5.0])
- [ ] go_nogo: pending

**Pipeline readiness: READY**

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
