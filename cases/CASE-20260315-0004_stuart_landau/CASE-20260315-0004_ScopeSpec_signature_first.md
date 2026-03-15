---
status: note
layer: cases/CASE-20260315-0004/
related:
  - docs/advanced/bc_extraction_method.md
  - docs/advanced/operator_signature_catalog.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
---

# ScopeSpec — Signature First: Stuart-Landau Oscillator
# CASE-20260315-0004

---

## 1. System Identification

```
Case ID:       CASE-20260315-0004
System name:   Stuart-Landau oscillator (supercritical Hopf normal form)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART (concrete system)
```

---

## 2. State Space(s)

```
Primary state space X:    z ∈ ℂ  (complex amplitude)
                          equivalently (x, y) ∈ ℝ²  with z = x + iy
Auxiliary spaces:         parameter space μ ∈ ℝ  (bifurcation parameter)
Joint state space:        X_joint = ℂ × ℝ  (if μ treated as co-state)
Dimension:                2 real degrees of freedom
Equation of motion:       dz/dt = (μ + iω)z − |z|²z
Fixed parameters:         ω = 1.0 rad/s
```

State space is continuous and smooth — no discretization required.
This is structurally the simplest possible Dissipation case.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Growth term `(μ+iω)z` composed with dissipation term `−\|z\|²z` |
| Product `×` | ✅ yes | `\|z\|²z = z · (z̄ · z)` — product of amplitude with state |
| Projection `π` | ✅ yes (asymptotic) | Trajectory converges to attractor: z* = 0 or \|z\| = sqrt(μ) |
| Tensor product `⊗` | ☐ N/A | Classical system |
| Conditional expectation `E[·\|G]` | ☐ N/A | Deterministic system |

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ asymptotically
Form:          lim_{t→∞} z(t) → attractor A(μ)
               A(μ<0) = {0},   A(μ≥0) = {z : |z| = sqrt(μ)}
Sub-signature: asymptotic projector (limit operation, not finite composition)
Idempotent?:   ✅ only asymptotically — Q-DISS-01 applies
```

This is the expected S1 structure for Dissipation: not a finite projection,
but a limit-operation convergence onto the attractor. The attractor itself
changes type at μ = 0 (point → circle), which makes this the most direct
empirical test of Q-DISS-01 in the repo.

### S2 — Product ∘ Composition (Coupling)

```
Present:       ☐ not present
Form:          N/A — single oscillator, no coupling to other systems
Cross terms?:  ☐ no
```

S2 is structurally absent. This is a key differentiator from CASE-0001
(Kuramoto) and CASE-0002 (Multi-Pendel), both of which are primarily S2 cases.

### S3 — Time-Coupled Product (Forcing)

```
Present:       ☐ not present
Form:          N/A — autonomous system, no explicit time dependence
Exogenous?:    ☐ no — μ is a fixed parameter, not a time-varying input
```

The system is autonomous: dz/dt = f(z; μ) with no explicit t-dependence.
If μ were made time-varying (μ(t) = ramp), S3 would appear — but that is
a different system.

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:       ✅ yes — primary signature
Form:          Dissipation term: −|z|²z
               For two trajectories z₁(t), z₂(t):
               d/dt|z₁ − z₂| ≤ (μ − |z|²)|z₁ − z₂|
               → contraction when |z|² > μ (outside attractor radius)
Sub-signature: state-dependent metric contraction
Contraction?:  ✅ metric contraction (state-dependent rate)
Rate c:        c(|z|) = exp((μ − |z|²)·Δt) — negative exponent outside attractor
```

The dissipation term `−|z|²z` is the defining S4 operator: it scales the
state by its own amplitude, creating a self-regulating contraction. Below the
attractor radius the system expands (μ > |z|²); above it, the dissipation
dominates (|z|² > μ) and contracts. The attractor is the fixed point of this
balance — exactly the S4 "scaling ∘ composition" structure.

**This is the canonical Dissipation-BC instance: clean, minimal, analytically
tractable, with an exact bifurcation point at μ_c = 0.**

### S5 — Expectation / Conditional Expectation

```
Present:       ☐ not present
Form:          N/A — deterministic system
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ asymptotic | S1: attractor projection in limit | Q-DISS-01: limit operation only, not finite |
| Coupling | ☐ no | — | Single oscillator; no S2 present |
| Aggregation | ☐ no | — | No coarse-graining of state space |
| Symmetry Breaking | ✅ secondary | S1+S4: Hopf bifurcation breaks U(1) symmetry | Fixed point (symmetric) → limit cycle (phase freedom) |
| Forcing | ☐ no | — | Autonomous system; no S3 |
| Dissipation | ✅ **primary** | S4: `−\|z\|²z` state-dependent contraction | Canonical instance; analytically clean |

**Primary BC class:** `Dissipation`

---

## 6. Regime Partition

```
Control parameter θ:      μ  (linear growth/decay rate)
Sweep range:              μ ∈ [−2.0, 2.0]
Expected regimes N:       2
  R1 (μ < 0):  dissipative fixed point — r_ss = 0
               all trajectories converge to z* = 0
               dissipation dominates at all amplitudes
  R2 (μ > 0):  stable limit cycle — r_ss = sqrt(μ)
               dissipation balanced by linear growth
               r_ss increases continuously with sqrt(μ)
Transition boundary θ*:   μ_c = 0  (analytically exact)
Transition type:          supercritical Hopf bifurcation
                          r_ss = sqrt(max(μ, 0)) — continuous onset, no jump
```

**Note on ε:** The transition at μ* = 0 is continuous (r_ss ∝ sqrt(μ)),
not a step. This means the regime boundary will appear as a smooth onset
in r_ss rather than a sharp jump. ε must be calibrated to the plateau of
N=2 stability, not to a sharp discontinuity.

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula / description | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `r_ss` | `lim_{t→∞} \|z(t)\|` — steady-state amplitude | ✅ yes | 0 to sqrt(2) ≈ 1.414 | ✅ yes |
| `lambda_proxy` | local divergence rate proxy | ☐ no | low in R1 regime | ☐ insufficient |

**r_ss** is the natural order parameter for this bifurcation — exact analog
of the Kuramoto r_ss in CASE-0001. Expected span ≈ 1.414 across μ ∈ [−2, 2].
For ε = 0.08: span/ε ≈ 17.7 — well sufficient.

### Perturbations Δ

```
Perturbation type:    Initial condition variation
                      z(0) drawn uniformly from disk |z(0)| < 0.5
Robustness check:     10 independent runs per μ-value
                      Partition stable if r_ss variance < 0.02 across runs
```

**Why IC perturbation is appropriate:** The system has a global attractor for
each μ-value (by Lyapunov argument). All initial conditions in the basin
converge to the same r_ss. IC perturbation directly tests this basin robustness.

### Resolution ε

```
Working ε:            0.08  (conservative pre-estimate)
Plateau location:     to be determined by epsilon_sweep pipeline
Plateau width w:      expected wide — r_ss has large span and clean plateau
Choice justification: span(r_ss) ≈ 1.414; working ε = 0.08 ≈ span/18
                      Adjust after epsilon_sweep confirms plateau interior
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(r_ss) < ε` — Dissipation BC has no observable effect | `scope_rejection` | Unlikely given span ≈ 1.414; would indicate integration error |
| F2 | `μ*` shifts under IC perturbation | `scope_rejection` | Check integration time; extend t_transient |
| F3 | No robust ε plateau for r_ss | `scope_rejection` | Check for numerical noise; reduce dt_max |
| F4 | `μ* = −2.0` or `μ* = 2.0` at sweep boundary | `sweep_refinement` | Extend range; theoretical μ* = 0 should be well interior |
| F-DISS | Dissipation → Restriction collapses at high μ: r_ss plateau vanishes | `open_question` | Documents Q-DISS-01; not a scope rejection — record as finding |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0001 (Kuramoto / Coupling) | 2 | ~0.25 (θ*=0 vs θ*=1.475, ranges differ) | partially_admissible | Same domain (DS), different BC class — first cross-BC transfer test |
| CASE-20260311-0003 (Doppelpendel / Restriction) | 7 | ~0.50 | inadmissible (raw) | High RCD expected; but matched-ε Φ may be more informative re Q-DISS-01 |

*TBS_norm requires sweep_range in both Invariants.json — will be computable
after pipeline run.*

---

## 10. Checklist Before Pipeline

- [x] State space defined: ℂ, continuous, smooth
- [x] Primary BC justified by S4 signature
- [x] Primary observable identified: r_ss, span ≈ 1.414
- [x] Control parameter: μ ∈ [−2.0, 2.0], 41 points, linear spacing
- [x] θ* known analytically: μ_c = 0 (interior of sweep)
- [x] Perturbations Δ defined: IC noise, 10 runs
- [x] Failure modes F1–F4 documented
- [x] Q-DISS-01 registered as open question linked to this case
- [ ] ε confirmed by epsilon_sweep — working value 0.08 is pre-estimate
- [ ] PartitionResult.json pending
- [ ] Invariants.json pending (sweep_range: [−2.0, 2.0] to be written)
- [ ] go_nogo: pending

**Pipeline readiness: READY — all prerequisites satisfied**

---

## Why Stuart-Landau is the Canonical Dissipation Case

| Property | Stuart-Landau | Alternatives |
|---|---|---|
| S4 form | `−\|z\|²z`: explicit, state-dependent | Damped oscillator: linear only |
| N regimes | 2: fixed point + limit cycle | Damped oscillator: 1 only |
| θ* known | μ_c = 0 analytically exact | Logistic: K known but no transition |
| Observable | r_ss = sqrt(max(μ,0)): direct, clean | Van der Pol: amplitude less clean |
| Q-DISS-01 | Directly testable: does S4→S1 hold? | Other systems: less direct test |
| Data needed | None — fully analytical/simulatable | Agent systems: data required |
| Existing transfer | r_ss analogous to Kuramoto r_ss | Enables meaningful cross-BC comparison |

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
