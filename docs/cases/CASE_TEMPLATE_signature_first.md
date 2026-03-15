---
status: note
layer: docs/cases/
related: operator_signature_catalog.md, cross_domain_signature_matrix.md
---

# Case Template: Signature-First

This template structures a new ARW/ART case starting from operator signatures,
rather than directly from observables. It enforces the derivation chain:

```
State space(s)
  → Primitive operators present
    → Derived signatures (S1–S5)
      → BC class labels
        → Regime partition
          → Observables Π / Perturbations Δ / Resolution ε
            → Failure modes
```

**How to use:** Copy this file to `cases/CASE-YYYYMMDD-####/`, rename to
`ScopeSpec_signature_first.md`, and fill in every block. Leave `[FILL]` markers
where information is not yet available — do not delete them.

Canonical case artifacts (ScopeSpec.yaml, BCManifest.yaml, CaseRecord.yaml)
are still required alongside this document. This template provides the
**operator-level justification** for the choices made in those YAML files.

---

## 1. System Identification

```
Case ID:        CASE-YYYYMMDD-####
System name:    [FILL — e.g. "Kuramoto oscillator network"]
Domain:         [FILL — DS / CT / SP / QM / ECO / NEURO / ML / EPI]
ARW level:      ART   (this block is always ART — concrete system)
```

---

## 2. State Space(s)

Describe the mathematical state space(s) of the system before any reduction.

```
Primary state space X:    [FILL — e.g. "X = Tⁿ (n phases on circle)"]
Auxiliary spaces:         [FILL — e.g. "parameter space κ ∈ ℝ₊"]
Joint state space:        [FILL — e.g. "X_joint = Tⁿ × ℝ₊" if parameter is co-state]
Dimension / cardinality:  [FILL]
```

---

## 3. Primitive Operators Present

List which ARW primitives appear in the system's equations.
Check all that apply and give the concrete instantiation.

| Primitive | Present? | Instantiation in this system |
|---|---|---|
| Composition `∘` | ☐ yes / ☐ no | [FILL] |
| Product `×` | ☐ yes / ☐ no | [FILL] |
| Projection `π` | ☐ yes / ☐ no | [FILL] |
| Tensor product `⊗` (QM) | ☐ yes / ☐ no | [FILL or N/A] |
| Conditional expectation `E[·|G]` | ☐ yes / ☐ no | [FILL or N/A] |

---

## 4. Derived Signatures

For each signature, state whether it is present and give the system-specific form.

### S1 — Projection / Selection

```
Present:        ☐ yes / ☐ no / ☐ partial
Form:           [FILL — e.g. "Poincaré section Σ = {θ₁ = 0}"]
Sub-signature:  [FILL — e.g. "section projection / coarse-graining / idempotent projector"]
Idempotent?:    ☐ yes / ☐ no / ☐ only asymptotically
```

### S2 — Product ∘ Composition (Coupling)

```
Present:        ☐ yes / ☐ no / ☐ partial
Form:           [FILL — e.g. "F(θᵢ, θⱼ) = sin(θⱼ − θᵢ) coupling term"]
Sub-signature:  [FILL — e.g. "Cartesian coupling / parameter coupling / tensor coupling"]
Cross terms?:   ☐ yes / ☐ no
```

### S3 — Time-Coupled Product (Forcing)

```
Present:        ☐ yes / ☐ no / ☐ partial
Form:           [FILL — e.g. "κ(t) time-variant / external periodic drive"]
T structure:    [FILL — e.g. "T = ℝ continuous / T = S¹ periodic / T = ℤ discrete"]
Exogenous?:     ☐ yes (T not determined by X) / ☐ no
```

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:        ☐ yes / ☐ no / ☐ partial
Form:           [FILL — e.g. "friction term −γθ̇ / Lindblad dissipator"]
Contraction?:   ☐ metric contraction / ☐ exponential decay / ☐ asymptotic only
Rate c:         [FILL — e.g. "c = e^{−γΔt}"]
```

### S5 — Expectation / Conditional Expectation as Projection

```
Present:        ☐ yes / ☐ no / ☐ partial
Form:           [FILL — e.g. "order parameter r = |E[e^{iθ}]|"]
Sub-signature:  [FILL — e.g. "MMSE / Mori-Zwanzig / discrete attention / L²-projection"]
Idempotent?:    ☐ yes / ☐ no / ☐ in limit
```

---

## 5. BC Class Labels

Assign BC classes based on the signatures identified above.
Each BC label must be justified by at least one signature in Section 4.

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ☐ yes / ☐ no | [FILL — e.g. S1: Poincaré section] | [FILL] |
| Coupling | ☐ yes / ☐ no | [FILL — e.g. S2: Kuramoto cross terms] | [FILL] |
| Aggregation | ☐ yes / ☐ no | [FILL — e.g. S1: coarse-graining to r] | [FILL] |
| Symmetry Breaking | ☐ yes / ☐ no | [FILL] | [FILL] |
| Forcing | ☐ yes / ☐ no | [FILL — e.g. S3: seasonal κ(t)] | [FILL] |
| Dissipation | ☐ yes / ☐ no | [FILL — e.g. S4: friction term] | [FILL] |

**Primary BC class** (for BCManifest.yaml): `[FILL]`

---

## 6. Regime Partition

Describe the expected regime structure, derived from the BC class above.

```
Control parameter θ:      [FILL — e.g. "κ (coupling strength)"]
Sweep range:              [FILL — e.g. "κ ∈ [0, 3]"]
Expected regimes N:       [FILL — e.g. "N = 3: incoherent / partial / synchronized"]
Transition boundary θ*:   [FILL — e.g. "κ_c ≈ 1.5"]
Regime boundaries:        [FILL — list approximate boundaries]
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

This block feeds directly into `ScopeSpec.yaml`. Fill one row per observable.

### Observables Π

| Observable key | Formula / description | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| [FILL] | [FILL] | ☐ yes / ☐ no | [FILL] | ☐ yes / ☐ no |
| [FILL] | [FILL] | ☐ yes / ☐ no | [FILL] | ☐ yes / ☐ no |

*At least one observable must be marked `primary: true`. Sufficiency requires
`span(π) ≥ 2ε`. If insufficient, replace observable — do not reject scope.*

### Perturbations Δ

```
Perturbation type:    [FILL — e.g. "initial condition noise σ = 0.01"]
Robustness check:     [FILL — e.g. "partition stable under 10 independent runs"]
```

### Resolution ε

```
Working ε:            [FILL — e.g. "ε = 0.09"]
Plateau location:     [FILL — e.g. "N=4 plateau, ε ∈ [0.07, 0.13]"]
Plateau width w:      [FILL — e.g. "w = 0.62"]
Choice justification: [FILL — e.g. "center of widest stable plateau for primary observable"]
```

*ε must be chosen from within a stable plateau. If working ε sits at a plateau
boundary, flag as fragile and move to plateau interior.*

---

## 8. Failure Modes

Document known or anticipated failure conditions. Each entry maps to a falsification
code F1–F4 (see `docs/core/` for definitions).

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(ALL π_i) < ε` — BC has no effect | `scope_rejection` | Replace BC class or observable |
| F2 | `θ*` unstable under Δ | `scope_rejection` | Increase sweep density or widen Δ |
| F3 | No robust plateau for ALL observables | `scope_rejection` | Reassess ε strategy |
| F4 | `θ*` at sweep boundary | `sweep_refinement` | Extend sweep range |
| [FILL] | [system-specific failure mode] | [FILL] | [FILL] |

---

## 9. Transfer Pre-Assessment

Before running the transfer pipeline, record the expected transferability to known cases.

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| [FILL — e.g. CASE-20260311-0001] | [FILL] | [FILL] | [FILL] | [FILL — e.g. same BC class, different domain] |

*RCD = |N_A − N_B|; TBS_norm = |θ*_A/range_A − θ*_B/range_B|;
Φ < 0.3 → highly admissible; 0.3–0.6 → partially; > 0.6 → inadmissible*

---

## 10. Checklist Before Handing Off to Pipeline

- [ ] All `[FILL]` markers resolved or explicitly marked as `[UNKNOWN — reason]`
- [ ] Primary BC class entered in `BCManifest.yaml`
- [ ] Primary observable marked in `ScopeSpec.yaml` Pi-block
- [ ] ε value is inside a stable plateau (not at boundary)
- [ ] `sweep_range` will be written to `Invariants.json` by `invariants.py`
- [ ] At least one failure mode documented per F1–F4
- [ ] `go_nogo` set to `pending` in `CaseRecord.yaml`

---

*Template version: 2026-03-14*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
