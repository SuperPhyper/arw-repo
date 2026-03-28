---
status: working-definition
layer: docs/art_instantiations/
case_id: CASE-20260328-0010
created: "2026-03-28"
---

# Structural Observable Failure in Social Scopes
## ART Instantiation: German School System (CASE-20260328-0010)

---

## Abstract

We demonstrate that in multi-actor coupled social systems, classical performance
observables (subject scores, competence indices, attendance rates) exhibit structural
failure (F0) over **extended regions** of the parameter space — not at isolated
critical points as in single-BC physical systems. This extends ARW scope transition
theory from point-like transitions (e.g. κ_c in CASE-0001/Kuramoto) to broad
structural failure zones characteristic of real-world institutional systems.

Alternative observable classes — coupling-based (peer_learning_sync,
coupling_activation_index) and fluctuation-based (Δattendance/Δκ) — remain valid
and diagnostically informative precisely where classical observables fail.
Observable class switching is therefore a **structural necessity**, not an analytical
refinement.

---

## 1. System Definition

**Case:** CASE-20260328-0010 — German School System
**ART Level:** Social-institutional multi-actor regime system
**Repo layer:** `docs/art_instantiations/` + `cases/CASE-20260328-0010/`

### State Space

```
X = X_C × X_F × X_P × X_T    (dim ≈ 40)
```

| Actor | Space | Key dimensions |
|---|---|---|
| Child | X_C | competence, wellbeing, attendance, engagement |
| Family | X_F | resource access ρ, stress, trust, learning time τ_F |
| Peers | X_P | cohesion, collaborative learning, sync |
| Teacher | X_T | efficacy, workload λ_T, burnout proximity, relational quality |

### Active Boundary Conditions

| BC class | Operator | Mechanism |
|---|---|---|
| Coupling (primary) | S2 | Child ↔ {family, peers, teacher} via τ_F, τ_P, τ_T |
| Restriction | S1 | Curriculum κ selects admissible competence trajectories |
| Forcing | S3 | Policy cycles, Schuljahr rhythm, PISA drive X_T, X_C |
| Dissipation | S4 | Burnout, withdrawal, disengagement as asymptotic sinks |

---

## 2. Core Hypothesis

> In multi-actor coupled systems with persistent violation of stationarity (A6)
> and reference stability (A5), classical observables exhibit structural failure F0
> over extended regions Z(π) ⊂ P. Alternative observable classes — coupling-based
> and fluctuation-based — recover structurally inaccessible information in these regions.

### Three research questions

1. Can extended Z(π) regions be empirically identified for classical observables?
2. Do alternative observable classes provide meaningful signal where classical observables fail?
3. Can observable class switching be formalized as structural necessity?

---

## 3. Observable Sets

### 3.1 Classical Observables (Class E-like)

These observables assume stationary reference distributions (A5, A6).

| Observable | Maps | BC structure | F0 risk |
|---|---|---|---|
| `subject_score` | X_C → [0,1] | R²·A·S | High — A5 fails when class composition shifts under high κ + low α |
| `core_competence_index` | X_C → [0,1] | R²·A²·S | High — same A5/A6 violation structure |
| `attendance_rate` | X_C → [0,1] | R·S1(Θ) | Medium — step form Θ(α−α_c) near θ*_2 |

**Structural argument for F0:**
`subject_score` contains a normalization operation (A5) that requires a stable
reference class. When attendance drops below α_c ≈ 0.75 and policy pressure κ
rises simultaneously, the reference class composition shifts — the assumption
underlying the normalization is violated. This is not measurement noise: it is a
structural collapse of the observable's pre-scopal substrate.

Formally:
```
A5 violated  ↔  reference class composition not stationary
A6 violated  ↔  class state distribution drifts under κ × α interaction
→ Z(subject_score) = { (κ, α) | κ > κ_F0 AND α < α_F0 }
```

This Z(π) is **two-dimensional and extended** — contrasting with the point-like
Z(r_ss) ≈ {κ_c} in CASE-0001.

### 3.2 Alternative Observables (ARW-driven)

| Observable | Maps | BC structure | Valid in Z(classical)? |
|---|---|---|---|
| `coupling_activation_index` | τ·sync → [0,1] | A²·R | Yes — no stationarity assumption |
| `peer_learning_sync` | X_C × X_P → [0,1] | R³·A²·S | Yes — coupling quality, not reference-dependent |
| `Δattendance/Δκ` | P → R (fluctuation) | Fluctuation class | Yes — maximal sensitivity near θ* |
| `sync_volatility` | temporal var(sync) | Fluctuation class | Yes — precursor signal near transitions |
| `collapse_safety_margin` | X_T × X_F → [0,1] | R·D⁻¹ | Yes — valid across all regimes |

---

## 4. Methodology

### 4.1 Parameter Sweep

Primary sweep variable: **policy pressure κ ∈ [0.0, 1.0]**, 80 points, linear spacing.

Fixed baseline parameters:
```
ρ (family_resource_access)   = 0.55
teacher_turnover              = 0.10
socioeconomic_gradient (Gini) = 0.32
```

Perturbation runs for Δ-stability check:

| Run ID | Modification | Purpose |
|---|---|---|
| `low_rho` | ρ = 0.25 | Low-resource context |
| `high_turn` | teacher_turnover = 0.25 | High teacher instability |
| `high_ses` | socioeconomic_gradient = 0.48 | High SES heterogeneity |

### 4.2 Observable Evaluation Protocol

For each observable π:

1. Identify `valid_regimes` and `known_Z` from ScopeSpec
2. Test Δ-stability: does observable span remain > 2ε across perturbation runs?
3. Classify: F0 (structural failure) / F1 (insufficient span) / valid

### 4.3 F0 Detection

The F0 proxy is constructed from joint violation of A5 and A6:

```python
a5_violation = sigmoid(κ, k=8, x0=0.58) × sigmoid(1−α, k=10, x0=0.25)
F0_active    = a5_violation > 0.25
```

This detects the region where both conditions are simultaneously violated,
producing the extended Z(π) characterizing this social system.

---

## 5. Results

### 5.1 Figure 1 — κ-Sweep Observable Comparison

![Fig 1](figures/fig1_kappa_sweep.png)

**Key findings:**

- `subject_score` enters Z(π) at κ ≈ 0.55 (F0 onset). The observable continues to
  produce numerical output but loses reference validity — values become structurally
  uninformative. Perturbation runs show high variance in this zone, confirming
  Δ-instability (F2 signal alongside F0).

- `attendance_rate` shows the predicted step-function form (S1 Restriction BC)
  near α_c ≈ 0.75. The threshold is a genuine regime signal — valid as a θ*_2
  indicator within R(attendance_rate).

- `coupling_activation_index` declines monotonically and smoothly across κ,
  remaining valid throughout. It carries diagnostic signal precisely where
  `subject_score` fails.

- `Δattendance/Δκ` (fluctuation observable) peaks near θ*_2, showing maximal
  sensitivity at the transition — the direct analog of χ = ∂r_ss/∂κ from CASE-0001.
  This confirms the fluctuation observable class as structurally privileged near
  regime boundaries (K6 consequence).

- `peer_learning_sync` and `sync_volatility` together provide an early-warning
  structure: sync quality degrades before quantity collapses, and volatility rises
  before the observable itself fails.

- `collapse_safety_margin` remains monotonically valid across all κ — the only
  observable with R(π) ⊇ {θ*_1, θ*_2, θ*_3} simultaneously.

### 5.2 Figure 2 — BC Dominance Heatmaps (κ × ρ space)

![Fig 2](figures/fig2_bc_heatmaps.png)

**Key findings:**

- Coupling BC (w_C) dominates the high-ρ / low-κ quadrant — the structural
  condition for R1 (Integrated Learning).

- Restriction BC (w_R) expands with κ at moderate ρ — the R2 corridor.

- Dissipation BC (w_D) dominates the low-ρ / high-κ quadrant. The red θ*_3
  contour marks the collapse boundary. Notably, this boundary is **ρ-dependent**:
  at low ρ, dissipative collapse occurs at κ ≈ 0.55; at high ρ, the system
  withstands κ ≈ 0.80 before collapse.

- This ρ-dependence formalizes the **P4 conditionality** from the policy model:
  removing homework (Restriction ↓) has null effect on Coupling activation when
  ρ < 0.4, because the family coupling operator τ_F requires resource capacity
  to activate.

### 5.3 Figure 3 — Regime Map and Failure Classification

![Fig 3](figures/fig3_regime_failure.png)

**Regime Map (Panel A):**
Four regimes are clearly separated in (κ, ρ) space:
- R1 (Integrated Learning): high ρ, low-to-moderate κ
- R2 (Competence Isolation): moderate ρ, high κ
- R3 (Attendance Fragmentation): low ρ, moderate κ
- R4 (Dissipative Collapse): low ρ, high κ

The θ*_1 boundary at κ ≈ 0.52 separates R1 from R2 along the κ axis.
The ρ_c ≈ 0.40 threshold separates viable from compromised family coupling.

**F0 Failure Map (Panel B):**

The F0 zone for classical observables covers approximately **38% of the full
(κ, ρ) parameter space** — not a point, not a line, but an extended two-dimensional
region. This is the principal empirical finding of this study.

In the equivalent physical case (CASE-0001/Kuramoto), Z(r_ss) is effectively
one-dimensional (near κ_c). In this social system, Z(subject_score) is
two-dimensional and proportional to the size of the crisis-relevant parameter region.

**Failure Classification Table (Panel D):**

| Observable | κ=0.2 | κ=0.5 | κ=0.8 |
|---|---|---|---|
| subject_score | 0.73 | 0.62 | **F0** |
| core_competence | 0.78 | 0.69 | **F0** |
| coupling_act. | 0.61 | 0.41 | 0.22 |
| peer_sync | 0.58 | 0.38 | 0.18 |
| collapse_safety | 0.82 | 0.58 | 0.31 |

F0 entries (κ=0.8) mark the zone where classical observables produce values
that are structurally uninformative — not inaccurate in the naive sense, but
invalid as regime indicators.

**Observable Comparison at κ=0.70 (Panel C):**

At high policy pressure, `subject_score` and `coupling_activation_index` diverge
increasingly with decreasing ρ. Below ρ < 0.4, `subject_score` is in Z(π) while
`coupling_activation_index` retains full discriminability. This is the empirical
confirmation of the structural argument: the two observables have non-overlapping
Z(π) boundaries.

### 5.4 Figure 4 — BC Dominance Timeline

![Fig 4](figures/fig4_bc_timeline.png)

The stacked-area plot makes the **BC dominance shift** visible as a dynamic process:

1. κ ∈ [0.0, 0.52]: Coupling dominant (w_C > 0.45) → R1
2. κ ∈ [0.52, 0.72]: Restriction rises, Coupling falls → R1/R2 transition at θ*_1
3. κ > 0.72: Dissipation accumulates, Forcing contributes → R2/R3 → θ*_3 corridor

The individual BC weight panel confirms that no BC class is ever zero — this is a
genuinely multi-BC system throughout the sweep, unlike single-BC physical cases
where one BC class is structurally absent.

---

## 6. Discussion

### 6.1 Extended Z(π) as a Social-System Signature

In physical systems (CASE-0001, CASE-0002, CASE-0003), F0 is a local phenomenon:
the observable fails at a specific critical point where one pre-scopal assumption
(typically A3/A4 ergodicity) breaks down. The failure is narrow because the
system transitions quickly through the critical zone.

In this social system, F0 is **extended** because:

1. **Violations are gradual:** A5 (reference stability) degrades continuously with
   κ, not abruptly. The school class composition shifts as attendance erodes — a
   process that operates over weeks to months, not at a single parameter value.

2. **Violations are coupled:** A5 and A6 failures reinforce each other. Low
   attendance erodes the reference class (A5), which in turn destabilizes the
   temporal distribution of class states (A6). This coupling extends the failure zone.

3. **Multiple BC classes are active:** In a single-BC system, one mechanism
   dominates near the transition. In this multi-BC system, Restriction, Forcing,
   and Dissipation simultaneously push the system toward the failure zone,
   expanding Z(π) across a larger parameter region.

This suggests a general principle: **the dimensionality of Z(π) scales with the
number of active BC classes**. Multi-BC systems have higher-dimensional failure
zones than single-BC systems.

### 6.2 Observable Class Switching as Structural Necessity

The standard view in education research treats alternative observables (wellbeing,
relational quality, coupling time) as *supplementary* to classical performance
metrics. This study provides a formal counterargument:

In the region κ > 0.55 × α < 0.80, subject_score is in Z(π). It does not provide
less information — it provides *structurally invalid* information. Using it as a
primary partition observable in this region is equivalent to using r_ss at κ_c in
CASE-0001: the observable continues to produce numbers, but the numbers do not
correspond to regime structure.

Observable class switching is therefore **structurally required**, not optional.
The coupling-based and fluctuation-based observables carry valid signal in the
regions where classical observables fail — and this complementarity is derivable
from the pre-scopal substrate analysis, not discovered empirically.

### 6.3 Policy Implications (ART Level)

The F0 finding has a direct policy corollary:

> Any policy evaluation that uses subject scores as the primary outcome metric in
> high-pressure / low-attendance contexts is evaluating a measurement in Z(π).
> The policy may succeed or fail — the measurement cannot determine which.

This applies specifically to policy combination PC4 (bound Ganztag + high κ):
the policy is designed to improve subject scores, evaluated using subject scores,
in the parameter region where subject scores are structurally uninformative.

The governance observables — `coupling_activation_index`, `collapse_safety_margin`,
`peer_learning_sync` — remain valid throughout and provide the correct measurement
basis for policy evaluation in this region.

---

## 7. Conclusions

**C1 — Extended F0 confirmed:**
Classical observables exhibit structural failure (F0) over a two-dimensional
extended region of (κ, ρ) space, covering approximately 38% of the policy-relevant
parameter space. This is not measurement error — it is a structural consequence
of pre-scopal assumption violations (A5, A6) under joint high-κ / low-α conditions.

**C2 — Alternative observables are valid in Z(classical):**
Coupling-based observables (coupling_activation_index, peer_learning_sync) and
fluctuation-based observables (Δattendance/Δκ, sync_volatility) remain in R(π)
throughout the sweep. They are not supplementary — they are the only valid
primary observables in the failure region.

**C3 — Observable class switching is structurally necessary:**
The complementarity of classical and alternative observables is derivable from
BC structure analysis prior to any empirical sweep. Observable class switching
should be specified at the ScopeSpec level, not discovered post-hoc.

**C4 — ARW extension: extended Z(π) in multi-BC systems:**
This case extends ARW from point-like scope transitions to extended structural
failure regions. The hypothesis that Z(π) dimensionality scales with active BC
class count is consistent with all current cases and should be formalized as an
open research question.

---

## 8. Open Questions

| ID | Question | Priority |
|---|---|---|
| Q-0010-05 | Formal derivation: does dim(Z(π)) scale with number of active BC classes? | high |
| Q-0010-06 | Is θ*_3 hysteretic? What is the recovery path from R4? | high |
| Q-0010-07 | Can sync_volatility serve as χ-analog (fluctuation observable near θ*_2)? | high |
| Q-0010-08 | Minimal observable set for unique BC inference in multi-actor systems? | medium |
| Q-0010-09 | Does ρ-conditionality generalize to other resource-constrained social systems? | medium |
| Q-0010-10 | Empirical calibration of κ_F0 and α_F0 thresholds from real school data | high |

---

## 9. Relation to Existing Cases

| Case | Shared structure | Key difference |
|---|---|---|
| CASE-0001 (Kuramoto) | F0 at critical coupling; fluctuation observable class | Point-like Z(r_ss) vs. extended Z(subject_score) |
| CASE-SOC1 (Shame) | Social Restriction BC; actor-level state space | Single-BC vs. multi-BC |
| CASE-0007 (SIR) | Aggregation BC (population dynamics) | No Coupling BC; no actor individuation |
| CASE-0004 (Stuart-Landau) | Emergence window; multi-observable analysis | Physical system; no extended Z(π) |

---

## 10. Repo Placement

```
cases/CASE-20260328-0010/
├── ScopeSpec.yaml                        ← S = (B, Π, Δ, ε) v2.0, incl. policy vector
├── BCManifest.yaml                       ← multi-BC; subject BC classification
├── ScopeSpec_signature_first.md          ← pre-pipeline BC inference
├── research_report.md                    ← this document
└── figures/
    ├── fig1_kappa_sweep.png              ← observable comparison across κ
    ├── fig2_bc_heatmaps.png              ← BC weights over (κ × ρ) space
    ├── fig3_regime_failure.png           ← regime map + F0 classification
    └── fig4_bc_timeline.png             ← BC dominance shift over κ

docs/art_instantiations/
└── german_school_system.md              ← domain narrative (to be written)

docs/notes/research_journal.md
└── Session 2026-03-28: extended Z(π) in social scopes (→ this case)
```

---

## Appendix A — Simulation Parameters

| Parameter | Baseline | Perturbation range |
|---|---|---|
| κ (policy pressure) | sweep [0, 1] | — |
| ρ (family resources) | 0.55 | [0.10, 0.95] |
| teacher_turnover | 0.10 | [0.05, 0.25] |
| socioeconomic_gradient | 0.32 | [0.20, 0.48] |
| ε_working | 0.07 | — |

## Appendix B — BC Weight Computation

```python
w_C = sigmoid(coupling_activation × 3 − 1)
w_R = sigmoid(κ × 1.8 − 0.6)
w_F = sigmoid(workload × κ × 1.5 − 0.8)
w_D = sigmoid(burnout × 2.5 − 1.0)

w_i = w_i_raw / (w_C_raw + w_R_raw + w_F_raw + w_D_raw)

coupling_activation =
  (τ_F × min(ρ,1) × family_sync
   + τ_P × peer_cohesion × peer_sync
   + τ_T × (1 − burnout) × teacher_sync) / 3
```

## Appendix C — F0 Detection Proxy

```python
a5_violation = sigmoid(κ, k=8, x0=0.58) × sigmoid(1−α, k=10, x0=0.25)
F0_active    = a5_violation > 0.25
```

This proxy captures the joint violation of A5 (reference class stability) and A6
(stationarity of class state distribution). The thresholds κ_F0 ≈ 0.58 and
α_F0 ≈ 0.75 are initial estimates requiring empirical calibration from real school data.
