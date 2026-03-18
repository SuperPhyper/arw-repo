---
status: complete
layer: cases/CASE-20260318-0004/audits/
---

# Failure Audit — Phase 1
# CASE-20260318-0004: Coupled Stuart-Landau oscillators (K-sweep)
# Date: 2026-03-18

## Summary

All four falsification conditions (F1–F4) checked against simulation data.
None triggered. Case proceeds to go_nogo evaluation pending formal pipeline artifacts.

---

## F1: Coupling BC has no relational effect — span(PLV) < ε

**Condition:** max(PLV) - min(PLV) < 0.09

**Empirical result:**
- PLV range: [0.158 (K=0.01), 1.000 (K=0.06+)]
- span(PLV) = 0.842

**Verdict:** ❌ NOT TRIGGERED — span 0.842 >> ε 0.09

---

## F2: Emergence window absent — amp_asym > ε at phase-locked K

**Condition:** amp_asym(K=0.08) > 0.09

**Empirical result:**
- amp_asym(K=0.08) = 0.076

**Verdict:** ❌ NOT TRIGGERED — 0.076 < ε 0.09

**Note:** amp_asym is classified as `observable_insufficiency`, NOT scope rejection.
The local collapse (amp_asym < ε for all K) is the intended emergence condition,
not a failure. See ScopeSpec.yaml: observable_sufficiency.amp_asym.interpretation.

---

## F3: No robust ε plateau — N=2 window width < 0.5

**Condition:** emergence window width < 0.5

**Empirical result:**
- Emergence window: ε ∈ [0.082, 0.805]
- Width = 0.723

**Verdict:** ❌ NOT TRIGGERED — width 0.723 >> threshold 0.5

---

## F4: K* at sweep boundary

**Condition:** theta_star at K=0.01 or K=0.12

**Empirical result:**
- K* ≈ 0.055–0.06 (between points 5 and 6 of 12)
- Normalized position: (0.055 - 0.01) / (0.12 - 0.01) = 0.41 (well interior)

**Verdict:** ❌ NOT TRIGGERED — K* interior

---

## Additional Finding: Lambda-Robustness Boundary

**Not a falsification condition (no F-ID assigned yet); recorded as open finding.**

The lambda-sweep (delta_02) shows:
- Emergence condition (amp_asym < ε) holds for λ ∈ [0.4, 1.3] at weak K
- Breaks at λ > 1.3: amp_asym(K=0.03) = 0.092 (K=1.3), 0.095 (K=1.4)

**Interpretation:** The emergence window is BC-relative and λ-bounded.
This confirms the theoretical prediction in bc_relative_observable_indistinguishability.md
(Section 5: indistinguishability is direction-dependent in BC space).

**Registered as:** Q-EMERGE-02 in CaseRecord.yaml

---

## Go/No-Go Pre-Assessment

| Criterion | Status |
|---|---|
| N = 2 partition recoverable | ✅ confirmed analytically |
| K* interior of sweep | ✅ K* ≈ 0.055 |
| PLV sufficient | ✅ span = 0.842 >> 2ε |
| amp_asym insufficient (intentional) | ✅ confirmed — emergence condition |
| Emergence window width > 0.5 | ✅ width = 0.723 |
| F1–F4 not triggered | ✅ all clear |

**Pre-assessment: GO** — pending formal PartitionResult.json from pipeline.extract_partition.
