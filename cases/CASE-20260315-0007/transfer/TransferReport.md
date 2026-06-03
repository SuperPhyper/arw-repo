---
status: working-definition
layer: cases/CASE-20260315-0007/transfer/
date: 2026-06-02
related_cases: [CASE-20260315-0007, CASE-20260311-0001]
---

# Transfer Report: CASE-20260315-0007 to CASE-20260311-0001
# Control Experiment: Aggregation (SIR) vs Coupling (Kuramoto)

**Date:** 2026-06-02
**System A:** sir_epidemic (SIR, beta-sweep)
**System B:** kuramoto (Kuramoto, kappa-sweep)
**Direction:** A to B
**Role:** Control arm — different BC classes, Phi expected LOW

---

## Distortion Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| RCD | 2 | significant_mismatch (N_A=2, N_B=4) |
| TBS | 0.0917 | moderate_shift |
| PCI | 0.5 | partial_compatibility |
| SDI | 4 | significant_distortion |
| **Phi_raw** | **0.5317** | **inadmissible** |
| **Phi_matched** | **0.5317** | **inadmissible** |

**epsilon-matching note:**
CASE-0007: epsilon_working = 0.10 (updated from 0.05; see FailureAudit)
CASE-0001: epsilon_working = 0.09
At epsilon=0.10, CASE-0001 still has N=4 (confirmed from EpsilonSweep.json).
Therefore RCD is unchanged at matched epsilon. Phi_matched = Phi_raw = 0.5317.

---

## Regime Structure Comparison

| | Scope A (SIR epidemic) | Scope B (Kuramoto) |
|---|---|---|
| System | SIR ODE | Kuramoto oscillators |
| Primary observable | I_peak | r_ss |
| BC class | Aggregation | Coupling |
| Observable BC structure | A2.R | R3.A.D |
| Regime count (N) | 2 | 4 |
| Adjacency edges | 1 | 3 |
| theta* (pipeline) | 0.200 | 1.475 |
| sweep_range | [0.0, 0.5] | [0.0, 3.0] |
| theta* normalized | 0.200/0.500 = 0.400 | 1.475/3.0 = 0.492 |
| epsilon_working | 0.10 | 0.09 |

---

## Admissibility Assessment

Phi = 0.5317 (raw) = 0.5317 (matched) → **inadmissible**

The scope transfer A to B fails the admissibility criterion. The partition of Scope B
(N=4, linear adjacency with 3 edges) is not a compatible coarsening of Scope A (N=2,
single edge). The structural mismatch is compounded by the BC-class distance between
Aggregation (SIR) and Coupling (Kuramoto).

---

## Observable BC Structures (Control C3)

### I_peak (CASE-0007, Scope A)

I_peak = max_t I(t)/N (peak infected fraction)

BC structure: **A2 . R** (double Aggregation, Restriction tertiary)
- A1 (primary): SIR quotient projection — the model itself is the Aggregation operator,
  projecting N individual micro-states onto 3 macro-compartments
- A2 (secondary): temporal maximum over full trajectory
- R (tertiary): simplex constraint S+I+R=1 as admissibility restriction

See `imax_bc_structure.md` for full A0-A6 derivation.

### r_ss (CASE-0001, Scope B)

r_ss = |mean(exp(i*theta_j))| — Kuramoto order parameter

BC structure: **R3 . A . D** (Restriction-dominated)
Established session 2026-03-18.

### Structural Contrast

| | I_peak | r_ss |
|---|---|---|
| System BC class | Aggregation | Coupling |
| Observable BC structure | A2.R | R3.A.D |
| Primary operator | Aggregation (quotient) | Restriction (mean-field) |
| Aggregation levels | 2 | 1 |

Two independent sources of dissimilarity:
1. System-level: Aggregation vs Coupling (different primitive operators)
2. Observable-level: A2.R vs R3.A.D (different primary operators)

---

## Registered Prediction Assessment

Pre-registered prediction (transfer_test_0001_0007_aggregation/, 2026-06-02):
- Phi_matched <= 0.70 → Result: 0.5317 <= 0.70 ✅
- Monotonic ordering: Phi(0001-0007) < Phi(0001-0003) < Phi(0001-0004)
  → 0.5317 < 0.95 (matched-eps) < 0.9983 ✅

**Outcome: §5 table row 1 — STRONG CONFIRMATION**
Phi_matched = 0.5317 <= 0.60 AND monotonic ordering holds.

> "Strong confirmation — BC-class distance dominant"

The transfer metric correctly discriminates Aggregation (SIR) from Coupling (Kuramoto)
with inadmissible Phi, while same-BC-class pairs (CASE-0004 vs CASE-0001) achieve
Phi=0.9983. The monotonic ordering across all three pairs validates the hierarchical
factorisation hypothesis.

---

## Monotonic Ordering Summary

| Pair | BC Classes | Phi | Verdict |
|------|-----------|-----|---------|
| CASE-0001 vs CASE-0004 | Coupling vs Coupling | 0.9983 | highly_admissible |
| CASE-0001 vs CASE-0003 | Coupling vs Restriction | 0.95 (matched-eps) | highly_admissible |
| CASE-0001 vs CASE-0007 | Coupling vs Aggregation | 0.5317 | **inadmissible** |

Ordering: 0.5317 < 0.95 < 0.9983 — monotonically decreasing with BC-class distance.

Note: CASE-0001 vs CASE-0003 both belong to DS domain (different BC classes);
the high matched-eps Phi is explained by partition structural similarity (matched N
at corrected eps). The BC-class-level penalty is absorbed by the matched-eps correction.
CASE-0001 vs CASE-0007 is a cross-domain transfer (DS to EPI) with no such structural
similarity — this is the clearest BC-class distance signal.

---

## Controls Status

| Control | Status | Evidence |
|---------|--------|----------|
| C1: I_peak BC structure characterised | ✅ | imax_bc_structure.md: A2.R |
| C2: I_peak sufficient at eps=0.10 | ✅ | span=0.47 >> 2*eps=0.20; FailureAudit |
| C3: Observable BC structures in report | ✅ | This section |
| C4: sweep_range in both Invariants.json | ✅ | [0.0,0.5] and [0.0,3.0] confirmed |
| C5: CASE-0007 go_nogo = go | ✅ | CaseRecord.yaml: decision=go (2026-06-02) |
| C6: eps-mismatch documented, both Phi values | ✅ | See epsilon-matching note above |

---

## Notes

- PCI=0.5: structural PCI approximation; full PCI would require aligned annotated results
- SDI=4: measures graph structure distance (4 node/edge differences: N=2 vs N=4)
- F-gradient finding at eps=0.05: I_peak gradient sigma_Delta < eps at fine sweep resolution.
  Resolved by eps=0.10 and 8 strategic sweep points. See FailureAudit_Phase1.md.
- theta* for CASE-0007: pipeline gives 0.20 (midpoint of 0.10-0.30 sweep gap);
  analytical beta* = 0.101. The sweep gap shifts the apparent theta* but N=2 partition
  and interior position are confirmed.

*Generated 2026-06-02*
