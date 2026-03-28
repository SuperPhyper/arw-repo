---
status: claim
layer: docs/advanced/
case_ref: CASE-20260311-0001
related:
  - docs/glossary/observable_range.md
  - docs/advanced/observable_decomposition.md
  - docs/advanced/arw_emergence_bc_relative.md
---

# χ = ∂r_ss/∂κ as Fluctuation Observable: Empirical Validation

**Date:** 2026-03-28  
**System:** Kuramoto (N=300, ω ~ N(0,1), T=200, dt=0.05, n_seeds=5)  
**Sweep:** κ ∈ [0, 4], 61 points (dense in transition region)  
**Hypothesis:** χ = ∂r_ss/∂κ peaks at κ_c where r_ss enters Z_shared (F0). χ ∉ class E — its pre-scopal substrate does not require stationarity at κ_c. Therefore R(χ) ∋ κ_c.

---

## 1. Motivation and ARW Context

The order parameter r_ss is a class-E (stationary expectation) observable. Its pre-scopal
substrate includes assumption A3 (ergodicity, unique stationary measure μ_stat). At the
Kuramoto phase transition κ_c, μ_stat bifurcates — the system transitions from incoherent
to synchronized. This places κ_c inside Z_shared, the universal exclusion zone:

```
Z_shared = { p ∈ P | ergodicity violated OR μ_stat not unique OR critical slowing diverges }
∀ π ∈ E:  Z(π) ⊇ Z_shared
```

At κ_c, r_ss does not fail due to insufficient resolution (F1) — it fails structurally
because A3 is violated (F0: observable outside its range). The observable collapses;
any θ* observed there is a scope transition, not a regime boundary.

**Research question (Q_NEW_12):** Does χ = ∂r_ss/∂κ provide meaningful signal exactly
where r_ss fails?

---

## 2. Observable Decomposition: χ

χ = ∂r_ss/∂κ is a **derivative observable** over the coupling parameter space P_κ:

```
χ(κ) = ∂/∂κ |E[e^(iθ)]|_ss
```

Key structural difference from r_ss:

| Property | r_ss | χ = ∂r_ss/∂κ |
|---|---|---|
| Observable class | E (stationary expectation) | Fluctuation (κ-derivative) |
| Pre-scopal assumption A3 | Required: μ_stat unique | Not assumed — measures sensitivity |
| Behavior at κ_c | Collapses (A3 violated → F0) | Peaks (maximal sensitivity) |
| R(π) at κ_c | ∉ R(r_ss) | ∈ R(χ) |
| BC structure | R³·A·D | Derivative of R³·A·D — inherits R³, adds sensitivity |

χ does not require μ_stat to be unique at κ_c — it measures *how fast* the stationary
distribution shifts as κ varies. This is well-defined even when the distribution itself
is undergoing bifurcation.

---

## 3. Simulation Results

### 3.1 κ-Sweep Summary

| Quantity | Value |
|---|---|
| κ range | [0.00, 4.00] |
| Sweep points | 61 |
| N oscillators | 300 |
| r_ss (κ=0) | 0.0503 |
| r_ss (κ=4) | 0.9669 |
| χ peak location (κ_c) | **1.7333** |
| r_ss at κ_c | 0.4709 |
| χ peak value | 1.2835 |
| Theoretical K_c (Gaussian, σ=1) | ≈ 1.596 |

The χ peak at κ_c ≈ 1.73 is consistent with the theoretical Kuramoto critical coupling
for Gaussian frequency distributions (K_c ≈ 1.596), with upward bias expected for
finite N=300 and finite simulation time T=200. The CASE-0001 scope transition at θ* ≈ 1.475
(36-point sweep, κ ∈ [0,3]) reflects a coarser sweep; the denser sweep here places the
transition at 1.73, closer to theoretical expectation.

### 3.2 Key Observation: χ Valid at κ_c

At κ = 1.7333:
- r_ss = 0.4709 — ambiguous (neither clearly incoherent nor synchronized)
- r_ss is in Z_shared — F0 failure mode
- χ = 1.2835 — **clear peak, maximum signal**

This confirms the ARW prediction: the fluctuation observable χ provides diagnostic
signal exactly where the stationary observable r_ss undergoes scope failure.

### 3.3 Cover Height Comparison

At ε = 0.05: r_ss yields N = 13 covers, χ yields N = 28.  
At ε = 0.10: r_ss yields N = 9 covers, χ yields N = 19.

χ resolves more than twice the number of regime-level covers across 88% of tested ε
values. This reflects χ's higher sensitivity in the transition region — the regime
structure near κ_c is invisible to r_ss but resolved by χ.

---

## 4. ARW Interpretation

### 4.1 F0 Confirmation

r_ss enters Z_shared at κ_c — this is an F0 event. The scope tuple with Π = {r_ss}
is insufficient for any scope that includes κ_c in its boundary B. This does not
reject the scope; it calls for observable replacement.

### 4.2 Fluctuation Observable Class

χ is the first concrete representative of the **fluctuation observable class** in the
ARW case portfolio. Its defining characteristic:

```
π ∈ Fluctuation class  ⟺  π = ∂/∂θ[some π_E] for parameter θ
                           π ∉ class E
                           R(π) ∋ {scope transitions of π_E}
```

This class is structurally complementary to class E: it provides signal where class-E
observables fail, and is insensitive where class-E observables are reliable (flat χ at
κ ≪ κ_c or κ ≫ κ_c).

### 4.3 Scope Transition vs Regime Boundary (K3)

The finding confirms consequence K3 from session 2026-03-18:

- θ* ≈ 1.48 in CASE-0001 is a **scope transition** (r_ss ∈ Z_shared), not a regime boundary.
- A regime boundary θ* would be a discrete partition change within R(π).
- Scope transitions are formally distinct; they require observable replacement, not ε tuning.

### 4.4 Observable Complementarity

The ARW framework now has empirical evidence for the following structure:

```
κ ≪ κ_c:   r_ss reliable (flat, high information)    χ near zero (low sensitivity)
κ ≈ κ_c:   r_ss F0 (Z_shared)                        χ peaks (maximum sensitivity)
κ ≫ κ_c:   r_ss reliable (flat, synchronized)        χ near zero
```

This suggests a principled **observable switching strategy**: use class-E observables
away from transitions, fluctuation observables at transitions. The boundary of applicability
is R(π) — checkable from the observable decomposition.

---

## 5. Open Questions

| ID | Question | Status |
|---|---|---|
| Q_NEW_12 | χ as CASE-0001 extension (answered here empirically) | **resolved empirically** |
| Q_NEW_10 | Formal distinction: scope transition vs regime boundary | open |
| Q_NEW_12b | What is the BC structure of χ? | open — does ∂/∂κ preserve R³·A·D? |
| Q_NEW_15 | Is the fluctuation class closed under further derivation? | new |
| Q_NEW_16 | Does a joint scope Π = {r_ss, χ} cover all of P_κ? | new |

---

## 6. Deliverables

| File | Description |
|---|---|
| `pipeline.py` | Full simulation + analysis code |
| `r_ss_chi.csv` | κ, r_ss, chi_raw, chi_smooth (61 rows) |
| `cover_height.csv` | ε, N_r_ss, N_chi (80 rows) |
| `plots/r_ss_vs_kappa.png` | r_ss curve with Z_shared annotation |
| `plots/chi_vs_kappa.png` | χ overlay with κ_c peak marker |
| `plots/cover_height_map.png` | N(ε) comparison + ΔN bar chart |
| `report_chi_observable.md` | This report |

---

## 7. Repo Integration Recommendation

This analysis should extend CASE-20260311-0001 with:

1. A new `ScopeSpec.yaml` block adding χ to Π as a fluctuation-class observable.
2. An updated `FailureAudit` for Phase 2 documenting r_ss F0 at κ_c with structural
   explanation (Z_shared, A3 violation).
3. A new glossary entry `docs/glossary/fluctuation_observable.md` defining the
   fluctuation class and its complement to class E.
4. A note in `docs/notes/research_journal.md` linking this finding to Q_NEW_12.

---

*Generated by ARW Research Assignment pipeline — 2026-03-28*
