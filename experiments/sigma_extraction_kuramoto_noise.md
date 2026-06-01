---
status: experiment-proposal
layer: experiments/
last_updated: 2026-05-30
depends_on:
  - experiments/kuramoto_oscillators.md
  - docs/advanced/bc_signature_extraction_observables.md
  - docs/advanced/bc_signature_persistence_and_dominance.md
  - docs/advanced/observable_space_cover_height.md
motivating_analysis: docs/advanced/bc_signature_extraction_observables.md
open_questions_addressed:
  - Q-EXT-01: operator signature discrimination without model equations
  - Q-EXT-02: minimum data requirements for stable Σ extraction
  - Q-SIG-02: intrinsicness of η_i vs. constellation-dependence
---

# Experiment: Σ Extraction from Observables — Kuramoto with Noise

## Motivation

`bc_signature_extraction_observables.md` defines a four-step procedure for
extracting the generator signature Σ from observable sweep data alone, without
access to governing equations. The procedure has been worked through
analytically for two constructed scenarios (clean Kuramoto and Kuramoto with
additive noise), producing the following predictions:

**Scenario A — weak noise (σ_noise = 0.1):**
- Coupling dominant, p({C}) ≈ 0.31
- Dissipation subdominant, p({D}) ≈ 0.08
- Joint persistence p({C,D}) ≈ min(p({C}), p({D})) — no conflict, separate η scales

**Scenario B — strong noise (σ_noise = 0.8):**
- Coupling and Dissipation on comparable η scales, p({C}) ≈ 0.22, p({D}) ≈ 0.19
- Joint persistence p({C,D}) ≈ 0.11 < min = 0.19 — conflict regime, signatures interfere
- Individual p({C}) reduced relative to Scenario A — η_i is not fully intrinsic

These predictions are constructed from qualitative reasoning about cover height
profiles, not from computed data. The present experiment replaces the
constructed numbers with computed ones and tests whether the extraction
procedure recovers the known BC structure of the Kuramoto model.

**The Kuramoto model is the right calibration system for this experiment**
because its BC structure is analytically known: Coupling is the primary BC,
θ* = 2σ/πK_c (Strogatz formula) provides ground truth for threshold position,
and the effect of additive noise on synchronization is well-understood. Any
deviation between extracted Σ and known BC structure is a diagnostic for
the extraction procedure, not for the model.

---

## Research Questions

**RQ1.** Does the four-step extraction procedure recover Coupling as the
dominant BC class for clean Kuramoto (σ_noise = 0), with Dissipation absent?

**RQ2.** For Kuramoto with strong noise (σ_noise = 0.8), does the cover height
profile show the predicted mixed-signature structure — reduced Coupling
dominance, emergent Dissipation signature, joint persistence below individual
minimum?

**RQ3.** Is η_birth(Coupling) stable across noise levels, or does it shift as
Dissipation becomes stronger? (Tests Q-SIG-02: intrinsicness of η_i.)

**RQ4.** What is the minimum sweep density (points per unit κ) required for
stable Σ extraction? (Tests Q-EXT-02.)

---

## System and Parameters

**Model:**

```
dθ_i/dt = ω_i + (K/N) Σ_j sin(θ_j − θ_i) + σ_noise · ξ_i(t)
```

- N = 50 oscillators
- ω_i ~ N(0, 0.5) natural frequencies (fixed across all runs)
- κ ∈ [0, 3], sweep step Δκ = 0.05 (61 points)
- σ_noise ∈ {0.0, 0.1, 0.3, 0.5, 0.8, 1.2} — six noise levels
- Integration: RK4, dt = 0.01, T_transient = 200, T_measure = 100
- Observable: r_ss = time-averaged |N⁻¹ Σ_j e^{iθ_j}|

**Scenarios:**

| Label | σ_noise | Expected dominant BC | Expected joint p |
|---|---|---|---|
| K0 | 0.0 | Coupling only | — |
| KA | 0.1 | Coupling >> Dissipation | p({C,D}) ≈ min |
| KB | 0.3 | Coupling > Dissipation | p({C,D}) slightly below min |
| KC | 0.5 | Coupling ≈ Dissipation | p({C,D}) < min, conflict visible |
| KD | 0.8 | Coupling ≈ Dissipation | p({C,D}) << min |
| KE | 1.2 | Dissipation may dominate | synchronization may not occur |

---

## Extraction Protocol

Apply the four-step procedure from `bc_signature_extraction_observables.md`
to each scenario independently.

### Step 1 — Cover height computation

For each scenario:
1. Run sweep: {(κ_i, r_ss(κ_i))} for κ_i ∈ [0, 3]
2. Compute cover height h(κ_i) using the observable-space cover height method
   (`observable_space_cover_height.md`), log-spaced ε ∈ [Δr/10, r_span], 200 steps
3. Record h(κ_i) and the ε-stratified cover structure

### Step 2 — Signature identification

For each scenario at each η level:
- Measure transition width w(ε) = width of the low-h region near θ*
- Test ε-dependence: fit w(ε) ~ ε^α; α > 0 → Coupling signature, α ≈ 0 → Restriction or noise floor
- Measure h_max in synchronized regime as function of σ_noise → Dissipation indicator
- Record failure signature at θ*: F-gradient slope, Z_shared width

Discriminant table (from `bc_signature_extraction_observables.md` §Step 2):

| Test | Coupling | Dissipation | Conflict |
|---|---|---|---|
| w(ε) ~ ε^α | α > 0 | flat (α ≈ 0 below noise floor) | mixed α |
| h_max(σ_noise) | stable | decreasing | decreasing + w broadening |
| F-gradient at θ* | steep, localized | diffuse | intermediate, unstable |

### Step 3 — Persistence interval extraction

For each identified BC class:
- η_birth,i = ε at which class signature first stably identifiable (scan from large ε downward)
- η_death,i = ε at which signature fragments or becomes indistinguishable from finite-N noise
- Record stability of η_birth,i across noise levels (RQ3)

For joint configurations {C, D}:
- Identify η range of coherent joint presence (both signatures active without one suppressing the other)
- Compute p({C,D}) and compare to min(p({C}), p({D}))

### Step 4 — Σ assembly and comparison

Assemble normalised Σ for each scenario. Plot:
- p({C}) and p({D}) as function of σ_noise
- p({C,D}) / min(p({C}), p({D})) as conflict index (= 1: no conflict, < 1: conflict)
- η_birth(Coupling) as function of σ_noise (tests RQ3)

---

## Expected Results and Failure Modes

### Expected results (from motivating analysis)

| Scenario | p({C}) | p({D}) | p({C,D})/min | Interpretation |
|---|---|---|---|---|
| K0 | ~0.33 | ~0 | — | Clean Coupling extraction |
| KA | ~0.31 | ~0.08 | ≈ 1.0 | Dissipation appears, no conflict |
| KB | ~0.27 | ~0.13 | ~0.85 | Mild conflict begins |
| KC | ~0.24 | ~0.17 | ~0.65 | Clear conflict regime |
| KD | ~0.22 | ~0.19 | ~0.58 | Strong conflict |
| KE | ~0.10 | ~0.25 | < 0.5 | Dissipation dominates |

### Failure modes and their diagnostics

**F-EXT-1: Coupling not recovered in K0.** The extraction procedure fails at
its simplest case. Diagnosis: cover height computation parameters wrong (ε range,
step count), or N=50 finite-size effects dominate. Resolution: increase N or
use theoretical θ* as anchor to check partition recovery.

**F-EXT-2: p({D}) does not increase with σ_noise.** Dissipation signature not
visible in cover height. Possible cause: r_ss integrates over noise → Dissipation
effect absorbed into steady-state value rather than regime partition structure.
Resolution: use a second observable sensitive to trajectory stability
(e.g., variance of r over T_measure) to expose Dissipation signature.

**F-EXT-3: p({C,D})/min does not decrease below 1.** Conflict not detected.
Possible cause: Coupling and Dissipation operate at genuinely separate η scales
even at high noise — no overlap. This would revise the motivating analysis and
suggest the two classes are structurally orthogonal in this model. Would be a
positive finding for Q-SIG-02.

**F-EXT-4: η_birth(Coupling) shifts significantly with σ_noise.** Confirms
Q-SIG-02: individual persistence is not intrinsic but constellation-dependent.
Would require revising the Σ formalism to treat η_i as a function of the full
active BC set, not as a property of each class independently.

---

## Relation to Existing Experiments

This experiment extends `experiments/kuramoto_oscillators.md` (clean Kuramoto,
scope calibration) by adding a noise dimension. The clean sweep (K0) should
reproduce the results of the existing Kuramoto experiment as a consistency check.

The noise sweep (KA–KE) is new and directly motivated by the Σ extraction
procedure. It is the first experiment in the repo whose primary output is
a generator signature Σ rather than a regime partition or threshold estimate.

---

## Output Artifacts

```
data/kuramoto_noise_sweep/
  scenario_K0.csv    ← (κ, r_ss) pairs, σ=0.0
  scenario_KA.csv    ← σ=0.1
  ...
  scenario_KE.csv    ← σ=1.2

analysis/sigma_extraction_kuramoto/
  cover_height_profiles.png     ← h(κ) for all scenarios
  signature_discrimination.png  ← w(ε) fits, h_max vs σ_noise
  persistence_profiles.png      ← p({C}), p({D}), p({C,D}) vs σ_noise
  conflict_index.png            ← p({C,D})/min vs σ_noise
  sigma_table.md                ← assembled Σ per scenario
```

---

*Motivating analysis: `docs/advanced/bc_signature_extraction_observables.md` §Constructed Example.*
*Extraction procedure: `docs/advanced/bc_signature_extraction_observables.md` §Steps 1–4.*
*Formal Σ definition: `docs/advanced/bc_signature_persistence_and_dominance.md`.*
