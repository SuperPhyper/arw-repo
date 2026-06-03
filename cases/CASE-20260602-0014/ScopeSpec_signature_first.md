---
status: working-definition
layer: cases/CASE-20260602-0014/
date: 2026-06-02
protocol: signature-first (pre-pipeline)
observable_locked: true
observable_lock_date: 2026-06-02
observable_lock_ref: >
  Simulationen/transfer_test_dissipation_growth/design/observable_selection.md
---

# ScopeSpec Signature-First — CASE-20260602-0014
# System: SIR with growing population (rho-sweep)
# BC Class: Dissipation (dimension-growing fibre)
# Role: Scope B in transfer_test_dissipation_growth experiment

---

## §1. System Identification

**System:** SIR epidemic model with growing total population N(t) = N₀·e^(ρt)

**Equations of motion (absolute counts):**

    dS/dt = ρ·N(t) − β·S·I/N      [births go to susceptibles]
    dI/dt = β·S·I/N − γ_r·I
    dR/dt = γ_r·I
    N(t)  = S(t) + I(t) + R(t) = N₀·e^(ρt)   [grows by construction]

**Fraction dynamics:**

    ds/dt = ρ(1−s) − β·s·i
    di/dt = i · (β·s − γ_r − ρ)      ← ρ appears as additive removal rate

**Structural novelty vs CASE-0007 (fixed-N SIR):**
CASE-0007 uses the standard SIR with fixed N=10000 and sweeps β (transmission rate).
CASE-0014 uses a growing-N SIR: new susceptibles are continuously added at rate ρ·N.
The growing population creates a dimension-growing fibre over the time axis ≤:
as t increases, the total state space "volume" grows exponentially.

---

## §2. State Space and Primitive Operators

**State space X:**
(S, I, R) ∈ ℝ³₊ with S+I+R=N(t). Three compartments; total size grows.

**Primitive operators present:**

| Operator | Source in system | BC class signature |
|----------|------------------|--------------------|
| S5 quotient (N micro-states → 3 compartments) | SIR mean-field itself | Aggregation (constitutive, inherited from CASE-0007) |
| S4 contraction (−γ_r·I, linear decay of I) | Recovery/removal term | **Dissipation** |
| S4 exponential growth (N(t) = N₀·e^(ρt)) | Birth term ρ·N | **Dissipation** (dilution of fraction) |
| S1 constraint (S+I+R=N, simplex restriction) | Compartmental constraint | Restriction |
| S2 (β·S·I/N transmission, product of S and I) | Transmission term | Coupling |

**Dominant operator for sweep axis ρ:**
The ρ-sweep controls the RATE OF DILUTION of the infected fraction:
di/dt = i·(β·s − γ_r − ρ). As ρ increases, the effective removal rate (γ_r + ρ)
increases — this is a Dissipation action on the fraction observable.
The dilution by exponentially growing N(t) = N₀·e^(ρt) is an S4 (Dissipation) contraction
on the fraction i = I/N.

---

## §3. BC Inference — Signature-First Analysis

### Regime signatures in ρ-space

**Analytical regime boundary:**
Epidemic threshold for fraction i(t):
    R₀_eff = β·s₀ / (γ_r + ρ) = 1  →  ρ* = β·s₀ − γ_r

With β=0.3, γ_r=0.1, s₀=0.99: **ρ* ≈ 0.197**

**Regime R1 (ρ < ρ*): Dissipation-insufficient regime**
- R₀_eff > 1: infected fraction grows initially; epidemic reaches endemic equilibrium
- Endemic equilibrium: i* = ρ(β − γ_r − ρ) / [β(γ_r + ρ)] > 0
- Observable g_max_percapita: HIGH (epidemic velocity per capita positive)
- Signature: exponential initial growth of i(t), followed by endemic state

**Regime R2 (ρ > ρ*): Dissipation-dominant regime**
- R₀_eff < 1: infected fraction decays from first time step
- Epidemic diluted out by fast population growth: births suppress epidemic via dilution
- Observable g_max_percapita: LOW (epidemic velocity per capita small or negative after peak)
- Signature: exponential decay of i(t) from initial conditions

**BC-class assignment:**
The transition at ρ* is driven by the Dissipation (dilution rate ρ) dominating the
Coupling (transmission β·s₀). This is a **Dissipation ↔ Coupling co-existence crossover**
— exactly analogous to CASE-0005 where Dissipation (γ) dominates Coupling (κ=3.25).

Primary BC class: **Dissipation** (the ρ-parameter is the Dissipation sweep axis)
Secondary BC class: Aggregation (SIR quotient is constitutive), Coupling (β·S·I/N term)

---

## §4. Observable Selection (LOCKED)

**Observable key: `g_max_percapita`**

    g_max = max_{t ∈ [0,T]} [ (dI/dt) / N(t) ]
          = max_t [ i(t) · (β·s(t) − γ_r) ]

**Derivation:** See `Simulationen/transfer_test_dissipation_growth/design/observable_selection.md`
(locked 2026-06-02) for full A0–A6 substrate analysis and BC structure derivation.

**BC structure: D·S4·R** (Dissipation-primary; non-averaging)
**Control C2 satisfied:** Primary operator is Dissipation (NOT Aggregation) ✓
**Control C7 satisfied:** Non-averaging over ≤ confirmed by BC structure decomposition ✓

**Why not Candidate 2 (I_peak_frac):**
i(t) = I(t)/N(t) satisfies di/dt = i·(β·s − γ_r − ρ) — IDENTICAL to fixed-N SIR with
effective recovery (γ_r + ρ). The growing-N structure is structurally absorbed (camouflage).
See observable_selection.md §5 for disqualification record.

**Secondary observable (diagnostic only, NOT used for regime partition):**
- `I_peak_frac`: carried along for comparison to CASE-0007 (structural camouflage documented)
- `rho_effective_early`: early growth rate diagnostic (log(i(T_e)/i₀)/T_e)

---

## §5. Scope Tuple Draft

**S = (B, Π, Δ, ε)**

**B (boundary constraints):**
- State space: (S, I, R) ∈ ℝ³₊ with S+I+R=N(t), N₀=10000
- Fixed params: β=0.3, γ_r=0.1, S(0)=9900, I(0)=100, R(0)=0
- Sweep: ρ ∈ [0.0, 0.50], 26 points linear (step 0.02)
- Analytical ρ* ≈ 0.197 is INTERIOR to sweep ✓

**Π (observables):**
- g_max_percapita (primary): D·S4·R structure; Dissipation-primary ✓
- I_peak_frac (diagnostic only): camouflage-documented

**Δ (perturbations):**
- IC variation: I(0) ∈ [50, 150] (±50% of nominal I₀=100)
- n_runs = 10 independent runs per ρ-value

**ε (resolution):**
- Working epsilon: 0.05 (pre-estimate; span of g_max_percapita ≈ 0.01–0.10 expected)
- To be confirmed by epsilon_sweep pipeline

---

## §6. Expected Pipeline Outcome

| Artifact | Expected value |
|----------|----------------|
| N (regime count) | 2 |
| θ* (transition boundary) | ρ* ≈ 0.197 ± 0.02 |
| var span (g_max_percapita) | ~0.09 across sweep (to be confirmed) |
| go_nogo | go (if N=2 with θ* interior, F1-F4 not triggered) |

**Sweep design note:**
With analytical ρ* ≈ 0.197, the 26-point grid (step 0.02) gives points at
ρ = 0.18 and ρ = 0.20 straddling the transition. This should give a clean binary
partition without needing strategic redesign. If F-gradient appears at eps=0.05 (as in
CASE-0007's first sweep attempt), increase to eps=0.08 or eps=0.10 per CASE-0007 precedent.

---

## §7. Relationship to Transfer Experiment

This case is **Scope B** in the transfer test:
`Simulationen/transfer_test_dissipation_growth/prediction_registration_dissipation_growth.md`

Transfer comparison: CASE-20260315-0005 (Scope A, stationary Dissipation) ↔ CASE-20260602-0014 (Scope B, dimension-growing Dissipation)

Research question: Does Φ(CASE-0005, CASE-0014) indicate a BC-structural break (Φ < 0.70)
or reparametrization (Φ ≥ 0.85)?

**Both cases must reach go_nogo=go before transfer.py is run.**
**sweep_range must be present in both Invariants.json files.**

---

*Pre-pipeline signature-first artifact. Created 2026-06-02. Observable locked.*
*Next step: run pipeline after CASE-0005 go_nogo confirmed.*
