---
status: note
layer: cases/CASE-20260315-0006/
related:
  - cases/CASE-20260311-0002/
  - cases/CASE-20260315-0005/
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/bc_extraction_method.md
---

# ScopeSpec — Signature First: Multi-Pendel + Forcing
# CASE-20260315-0006

---

## 1. System Identification

```
Case ID:       CASE-20260315-0006
System name:   Multi-Link-Pendel with periodic base excitation (Ω-sweep)
Domain:        DS — Dynamical Systems / Physics
ARW level:     ART
Derived from:  CASE-20260311-0002 (same system, κ=1.0 fixed, Ω swept)
```

---

## 2. State Space(s)

```
Primary state space X:   τ ∈ [-π,π]^n × ℝ^n  (joint angles + velocities)
Extended state space:    X × S¹  (joint state + forcing phase φ = Ω·t mod 2π)
Fixed parameters:        κ = 1.0  (below Coupling transition — incoherent baseline)
                         A = 0.5  (forcing amplitude)
Sweep parameter:         Ω ∈ [0.1, 10.0]  (excitation frequency, log-spaced)
Equation of motion:      τ̈ = f(τ, τ̇; κ) + A·sin(Ω·t)
```

The state space extension X × S¹ is the formal S3 structure: the time
axis is compactified to a circle by the periodic forcing. This makes the
stroboscopic map (sampled at t = k·2π/Ω) available as a discrete reduction.

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation |
|---|---|---|
| Composition `∘` | ✅ yes | Coupling `f(τ,τ̇;κ)` composed with forcing `+A·sin(Ω·t)` |
| Product `×` | ✅ yes | State × time: `X × S¹`; joint-joint cross terms (κ=1.0) |
| Projection `π` | ✅ yes | Poincaré section: `Σ_{φ=0} = {t : Ω·t = 0 mod 2π}` |
| Tensor product `⊗` | ☐ N/A | Classical |
| Cond. expectation `E[·\|G]` | ☐ N/A | Deterministic |

**Note on S3 + S1 combination:** The Poincaré section (S1) is
*induced* by the periodic forcing (S3) — it is the natural projection
onto the stroboscopic surface. This S3 → S1 derivation is a clean
instance of the operator chain documented in `operator_signature_catalog.md`.

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ yes — induced by S3
Form:          Poincaré section Σ_{φ=0}: continuous flow → discrete return map
               π_strob : (τ(t), τ̇(t), φ(t)) → (τ(t_k), τ̇(t_k))
               where t_k = k · 2π/Ω
Sub-signature: section projection (stroboscopic)
Idempotent?:   ✅ yes — sampling at fixed phase is idempotent
```

This is a textbook S1 instance from the cross-domain matrix (DS row:
"Poincaré section → First-Return Map"). It is derived from S3 — the
forcing creates the periodic structure that makes the section natural.

### S2 — Product ∘ Composition (Coupling)

```
Present:       ✅ yes — secondary (κ=1.0)
Form:          f(τ_i, τ_j) — coupling cross terms, same as CASE-0002
Sub-signature: Cartesian coupling (below transition; incoherent regime)
Cross terms?:  ✅ yes — but weaker effect than in CASE-0002 at κ=3.25
```

At κ = 1.0 the system is in the incoherent Coupling regime — joints are
weakly coupled but do not synchronize. This is the background structure
on which Forcing (S3) operates.

### S3 — Time-Coupled Product (Forcing)

```
Present:       ✅ yes — primary signature
Form:          A·sin(Ω·t): periodic external excitation
               State space extension: X ↦ X × S¹
T structure:   T = S¹  (period 2π/Ω, continuous)
Exogenous?:    ✅ yes — Ω and A not determined by τ
Stroboscopic:  ✅ available — Poincaré section at φ = 0 mod 2π
```

**S3 is the primary signature.** The observable structure is entirely
driven by the resonance relationship between Ω and the natural frequencies
of the pendulum chain. This is the defining feature of Forcing-BC cases:
the regime partition is determined by the forcing frequency relative to
system resonances — not by a coupling threshold (S2) or a decay rate (S4).

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:       ☐ not present  (γ = 0 by design)
Form:          N/A
Note:          Deliberate choice: γ=0 isolates Forcing from Dissipation.
               CASE-0005 covers the γ-axis. CASE-0006 covers the Ω-axis.
```

### S5 — Expectation as Projection

```
Present:       ☐ not present
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ partial | S1: Poincaré section induced by forcing | Structural, not a dynamical BC |
| Coupling | ✅ secondary | S2: κ=1.0 cross terms present | Below transition; incoherent regime |
| Aggregation | ☐ no | — | |
| Symmetry Breaking | ☐ no | — | No spontaneous symmetry breaking |
| Forcing | ✅ **primary** | S3: `A·sin(Ω·t)` periodic external input | Textbook S3 instance |
| Dissipation | ☐ no | — | γ=0 by design |

**Primary BC class:** `Forcing`

---

## 6. Regime Partition

```
Control parameter θ:      Ω  (excitation frequency)
Sweep range:              Ω ∈ [0.1, 10.0], 50 points, log-spaced
Expected regimes N:       ≥ 3 (resonance structure)
  R1 (Ω << ω_nat):  quasi-static off-resonance — var_rel low
  R2 (Ω ≈ ω_nat_k): resonance band k — var_rel high
  R3 (Ω >> ω_nat):  high-frequency averaging — var_rel low
  [additional resonance bands possible for multi-link chain]

Transition boundaries θ*: Ω*_k ≈ natural frequencies of pendulum chain
                          — unknown a priori; must be determined by sweep
Transition type:          resonance peaks — non-monotone var_rel(Ω)
                          this is structurally distinct from all other
                          cases in the repo (which have monotone transitions)
```

**Critical difference from other cases:** var_rel(Ω) is non-monotone.
The pipeline must handle a non-monotone observable correctly.
The ε-plateau analysis may yield multiple narrow plateaus (one per
resonance gap) rather than a single wide plateau.

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `var_rel` | `<Var(τ_i)>_t / Var_max` time-averaged | ✅ yes | 0 to ~1.0; non-monotone | ✅ sufficient |
| `response_amplitude` | `<max_t(\|τ_i(t)\|)>_i` mean peak amplitude | ☐ candidate | peaks at resonance | ☐ pending |
| `lambda_proxy` | local divergence proxy | ☐ no | insufficient expected | ☐ insufficient |

**Measurement protocol note:** var_rel must be time-averaged over at
least 50 complete forcing periods to suppress transient and phase effects.
The averaging window must scale with 1/Ω across the sweep.

### Perturbations Δ

```
Perturbation type 1:  IC variation: τ(0) ∈ [-0.1,0.1]^n, τ̇(0) = 0
Perturbation type 2:  Forcing phase: φ₀ ∈ {0, π/4, π/2, π}
n_runs:               10 per Ω-value (IC variation)
                      4 phases × 3 IC draws per Ω-value (phase robustness)
Robustness target:    Regime boundaries stable across all phase offsets
```

### Resolution ε

```
Working ε:            0.08  (larger than other cases — resonance peaks
                      may require wider ε to bridge narrow off-resonance dips)
Plateau status:       pending epsilon_sweep
Note:                 Non-monotone observable may produce multiple plateaus.
                      Pipeline must report ALL stable plateaus, not just widest.
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(var_rel) < ε` across all Ω | `scope_rejection` | Check amplitude A; verify κ=1.0 produces response |
| F2 | Resonance peaks shift under phase perturbation | `scope_rejection` | Increase averaging window length |
| F3 | No robust ε plateau — all resonance peaks too narrow | `scope_rejection` | Increase sweep density; consider log-finer spacing near peaks |
| F4 | All Ω* at sweep boundary | `sweep_refinement` | Extend range; resonances should be interior |
| F-RES | Resonance peaks merge — no stable N > 2 partition | `sweep_refinement` | Increase Ω resolution near resonance bands |
| F-MON | Pipeline assumes monotone observable — fails on non-monotone var_rel | `modeling_error` | Verify pipeline handles non-monotone observables before running |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0002 (same system, κ-sweep) | 1–2 | TBD | partially_admissible | Same system; different BC class (Forcing vs Coupling) |
| CASE-20260315-0005 (same system, γ-sweep) | 0–2 | TBD | partially_admissible | Same system; different BC class (Forcing vs Dissipation) |
| CASE-20260315-0004 (Stuart-Landau) | 1–3 | TBD | inadmissible (estimate) | Different system and BC class |

---

## 10. Checklist

- [x] State space extended to X × S¹ (S3 structure explicit)
- [x] Primary BC (Forcing) justified by S3 signature
- [x] Secondary BC (Coupling) documented: κ=1.0 incoherent baseline
- [x] γ=0 design choice documented: isolates Forcing from Dissipation
- [x] Non-monotone observable documented as structural feature
- [x] Poincaré section (S1 induced by S3) documented
- [x] Measurement protocol scales with 1/Ω
- [x] Failure mode F-MON added: pipeline non-monotone compatibility check
- [ ] Pipeline non-monotone compatibility verified before run
- [ ] ε confirmed by epsilon_sweep
- [ ] PartitionResult.json pending
- [ ] Invariants.json pending (sweep_range: [0.1, 10.0])
- [ ] go_nogo: pending

**Pipeline readiness: READY — with prerequisite: verify pipeline handles
non-monotone observables (F-MON check)**

---

## Scientific Significance: Completing the Multi-Pendel BC Map

With this case, the Multi-Link-Pendel system now covers all three
swept BC axes:

| Case | Parameter | BC | Status |
|---|---|---|---|
| CASE-20260311-0002 | κ ∈ [0,10] | Coupling | go |
| CASE-20260315-0005 | γ ∈ [0,5] | Dissipation | pending |
| CASE-20260315-0006 | Ω ∈ [0.1,10] | Forcing | pending |

This is the first complete BC-axis coverage of a single physical system
in the ARW repo — enabling a 3×3 transfer matrix across all BC-class pairs.

---

*Generated: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
