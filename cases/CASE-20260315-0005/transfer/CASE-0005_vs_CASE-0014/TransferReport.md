---
status: working-definition
layer: cases/CASE-20260315-0005/transfer/
date: 2026-06-02
experiment: transfer_test_dissipation_growth
pre_registration: >
  Simulationen/transfer_test_dissipation_growth/prediction_registration_dissipation_growth.md
---

# Transfer Report: CASE-20260315-0005 ↔ CASE-20260602-0014

**Dissipation-Stationary ↔ Dissipation-Growing — Cross-Fibre Transfer Test**

**Date:** 2026-06-02
**System A:** CASE-20260315-0005 — Multi-link pendulum with joint damping (γ-sweep)
**System B:** CASE-20260602-0014 — SIR with growing population N(t)=N₀·e^(ρt) (ρ-sweep)
**Observable A:** var_rel (steady-state angular variance); BC structure R³·A²·S
**Observable B:** g_max_percapita = max_t [(dI/dt)/N(t)]; BC structure D·S4·R — locked 2026-06-02

**Research question:** Does a dimension-growing order axis constitute a BC-structural break
within the Dissipation class?

---

## §1. Distortion Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| RCD | 0 | perfect_match |
| TBS_norm | 0.0000 | boundary_preserved |
| TBS_raw | 1.5300 | (raw; axes incommensurable — use norm only) |
| PCI | 1.0000 | full_compatibility |
| SDI | 0 | identical_structure |
| **Φ_raw** | **1.0000** | **highly_admissible** |
| **Φ_matched** | **1.0000** | **highly_admissible** |

Φ weights: PCI=0.4, RCD=0.3, SDI=0.2, TBS=0.1. All four components score 1.0.

---

## §2. Regime Structure Comparison

| | Scope A — CASE-0005 | Scope B — CASE-0014 |
|---|---|---|
| System | Damped two-link pendulum | Growing-population SIR |
| BC class (primary) | Dissipation (γ damping, S4) | Dissipation (ρ dilution, S4) |
| Sweep parameter | γ ∈ [0.0, 5.0] | ρ ∈ [0.0, 0.50] |
| Regime count N | 2 | 2 |
| θ* (ARW boundary) | γ* = 1.70 | ρ* = 0.17 |
| θ*/range (normalized) | 1.70/5.0 = **0.340** | 0.17/0.5 = **0.340** |
| Adjacency structure | binary, 1 edge | binary, 1 edge |
| ε_working | 0.01065 | 0.00549 |
| Observable BC structure | R³·A²·S (Restriction-primary) | D·S4·R (Dissipation-primary) |

Both scopes have identical normalized transition positions: θ*/range = 0.340.

---

## §3. Control C3 — Observable BC Structure Documentation

*Required by pre-registration §6, Control C3.*

### Scope A: var_rel

**BC structure: R³·A²·S**
Restriction × 3 (joint selection, difference, window); Aggregation × 2 (temporal variance,
IC mean); Scaling (normalization). **Primary: Restriction (S1).**

The system-level Dissipation BC is captured indirectly through the steady-state value:
as γ increases, the dissipative attractor drives joint velocities to zero, collapsing var_rel.

### Scope B: g_max_percapita

**BC structure: D·S4·R** (derived and locked 2026-06-02 in observable_selection.md)

| Step | Operation | Operator | BC Class |
|------|-----------|----------|----------|
| 1 | dI/dt recovery term: −γ_r·I | Linear contraction (S4) | **Dissipation** |
| 2 | Denominator 1/N(t) = e^(−ρt)/N₀ | Exponential scaling (S4) | **Dissipation** |
| 3 | I(t)/N(t) = i(t), quotient | Restriction (S1) | Restriction |
| 4 | max_{t∈[0,T]} | Supremum selection (S1) | Restriction |

**Primary: Dissipation (D).** The growing-N denominator e^(−ρt)/N₀ is a canonical S4
Dissipation form (exponential contraction) and directly encodes dimension-growth.

### Mismatch note

The two observables have **different primary BC operators** (R vs D). Φ measures partition
structure transfer, not system BC equivalence. The Φ=1.000 result is consistent with
reparametrisation but does not exclude the possibility that the result reflects coincidental
partition structures across different projections. A same-observable comparison (recommended
in §8) would fully disambiguate.

---

## §4. Control C6 — ε-Matching

*Required by pre-registration §6, Control C6.*

| | Scope A | Scope B |
|---|---|---|
| ε_working | 0.01065 | 0.00549 |
| Observable span | 0.12554 | 0.01834 |
| ε_norm (ε/span) | 0.085 | 0.299 |
| N at ε_working | **2** | **2** |

Both cases have N=2 at their working epsilons. No regime count mismatch to reconcile.
**Φ_raw = Φ_matched = 1.000.** ε-matching is trivially satisfied.

The normalized ε differs by a factor of ~3.5 (0.085 vs 0.299), reflecting the narrower
observable range of g_max_percapita relative to var_rel. This difference is noted but
does not affect the admissibility verdict since both N=2 partitions are confirmed.

---

## §5. Control C7 — Non-Averaging Re-confirmation

*Required by pre-registration §6, Control C7 (novel control; no prior precedent).*

The pipeline kernel `run_sir_growing` computes at each integration step:

    g_cur = (I / N) * (beta * S / N - gamma_r)  # pointwise at time t

and records `g_max = max(g_cur)` over all time steps. This is:

- A **pointwise rate** at each t — no accumulation over t
- A **supremum selection** (Restriction S1), not expectation (Aggregation S5)
- The denominator N(t) = S+I+R evaluated at the same t as the numerator — no cross-time averaging
- A6 stationarity is not invoked — no convergence to stationary distribution is assumed

The n_ic averaging (mean over 5 IC runs per ρ-value) is a Δ-stability check, not a
structural averaging over the growing fibre ≤. It averages over perturbations δ ∈ Δ,
which is explicitly allowed under the ARW perturbation protocol.

**Control C7: CONFIRMED. g_max_percapita is non-averaging over ≤.**

Camouflage invalidation condition (pre-registration §5): **NOT triggered.**
The Φ=1.000 result is evaluable and counts against the registered prediction.

---

## §6. Prediction Assessment

**Registered prediction (§4, LOCKED):**
> Φ(stationary Dissipation ↔ growing Dissipation) < Φ(same-class baseline ≥ 0.85)
> → expected verdict: partially_admissible or inadmissible (Φ < 0.70)

**Result: REFUTED.** Φ = 1.000 >> 0.70.

**Falsifier condition (§5, LOCKED):**
> If Φ_matched ≥ 0.85 AND dimension-growing fibre confirmed AND non-averaging observable
> confirmed, THEN dimension growth is NOT a BC-structural break. It is a reparametrisation.
> Q-REL-04 resolved: Dissipation class is closed under fibre dimension growth.

**Falsifier: SATISFIED.**

- Φ_matched = 1.000 ≥ 0.85 ✓
- Dimension-growing fibre confirmed: N(t) = N₀·e^(ρt) ✓
- Non-averaging observable confirmed (Control C7, §5 above) ✓

**Resolution of Q-REL-04 (provisional):** Dimension growth along the order axis ≤ is a
**reparametrisation** of stationary Dissipation, not a BC-structural break. The Dissipation
class appears closed under fibre dimension growth at the level of partition structure transfer.
"Provisional" because caveats C-I through C-IV (§7) partially limit the interpretation.

### Calibration table

| Comparison | Φ | BC relation |
|------------|---|-------------|
| CASE-0004 ↔ CASE-0001 (Coupling same-class) | 0.9983 | same BC, same domain |
| **CASE-0005 ↔ CASE-0014 (Dissipation cross-fibre)** | **1.0000** | **same BC, cross-fibre** |
| CASE-0001 ↔ CASE-0007 (Coupling vs Aggregation) | 0.5317 | different BC classes |

The cross-fibre Dissipation result (1.000) exceeds even the same-class Coupling reference
(0.9983). Dissipation shows at least as strong structural coherence across fibre dimensionality
as Coupling shows across system types within the same BC class.

---

## §7. Caveats

**C-I — TBS_norm = 0 is partly coincidental.**
The ARW observational θ*_B = 0.17 differs from the analytical threshold ρ* ≈ 0.197.
Analytically: TBS_norm = |1.70/5.0 − 0.197/0.5| = |0.34 − 0.394| = 0.054 (still
boundary_preserved; TBS_score = 0.892; Φ_analytical ≈ 0.993). The conclusion is unchanged.
The exact TBS_norm = 0 is an artifact of the ARW observational boundary, not a deep
physical identity. The Φ=1.000 reported here is the correct ARW result; the analytical
correction gives Φ ≈ 0.993 — both highly_admissible.

**C-II — Observable BC mismatch.**
var_rel is Restriction-primary; g_max_percapita is Dissipation-primary. The Φ=1.000 could
reflect (a) genuine reparametrisation, or (b) coincidental partition structures. A
same-observable comparison would fully disambiguate (see §8, Recommendation 1).

**C-III — Camouflage limitation (pre-registration §7.1).**
Control C7 confirms non-averaging by structure, but does not exclude subtle aggregation
effects undetected by the BC decomposition. Full validation requires a ground-truth
dimension-growing system with a known BC-structural break. This is a separate program.

**C-IV — Narrow N2 ε-window in CASE-0014.**
N2 ε-window = [0.00531, 0.00570], width = 0.00039. The partition is structurally valid
but near the F-gradient boundary. A strategic re-sweep (8 points dense around ρ=0.15–0.25)
would widen the window and harden the partition robustness (see §8, Recommendation 2).

---

## §8. Recommended Next Steps

1. **Same-observable control:** Compute g_max_percapita for a fixed-N SIR variant (β-sweep
   or γ_r-sweep) and compare with CASE-0014 (ρ-sweep). If Φ ≈ 1.0 again, the cross-fibre
   result is reinforced. Addresses C-II.

2. **Strategic re-sweep of CASE-0014:** Dense 8-point sweep around ρ=0.15–0.25 (following
   CASE-0007 precedent). Widens N2 ε-window. Addresses C-IV.

3. **Analytical θ* discrepancy note:** Document Q-OBS-01: why does g_max_percapita
   detect the regime transition at ρ=0.17 rather than the analytical ρ*=0.197?
   Answer: steep g_max gradient in R1 displaces the largest-jump boundary earlier.

4. **Multi-axis extension (Limitation §7.2 of pre-registration):** Multi-axis partial
   orders require pipeline architecture changes; defer to separate project.

---

## §9. Summary

| Item | Result |
|------|--------|
| **Φ_raw** | **1.0000** |
| **Φ_matched** | **1.0000** |
| **Admissibility** | **highly_admissible** |
| RCD | 0 (N=2 both) |
| TBS_norm | 0.000 (boundary at 34% of range, both) |
| PCI | 1.000 (full compatibility) |
| SDI | 0 (identical structure) |
| Registered prediction (Φ < 0.70) | **REFUTED** |
| Falsifier condition (Φ ≥ 0.85) | **SATISFIED** |
| **Q-REL-04** | **Dimension growth = reparametrisation (provisional; caveats C-I–C-IV)** |
| Control C3 | ✓ Observable BC mismatch documented |
| Control C6 | ✓ Φ_raw = Φ_matched = 1.000; N=2 both; ε-matching trivial |
| Control C7 | ✓ g_max_percapita non-averaging confirmed by structure and kernel |

*Transfer report written 2026-06-02.*
*Calibration: CASE-0004↔CASE-0001 Φ=0.9983; CASE-0001↔CASE-0007 Φ=0.5317.*
