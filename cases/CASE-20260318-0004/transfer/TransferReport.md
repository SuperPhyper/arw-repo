---
status: working-definition
layer: cases/CASE-20260318-0004/transfer/
date: 2026-06-02
related_cases: [CASE-20260318-0004, CASE-20260311-0001]
---

# Transfer Report: CASE-20260318-0004 to CASE-20260311-0001

**Date:** 2026-06-02
**System A:** stuart_landau_coupled (Coupled Stuart-Landau, K-sweep)
**System B:** kuramoto (Kuramoto oscillators, kappa-sweep)
**Direction:** A to B
**Recomputed:** 2026-06-02 (corrected sweep_range=[0.01,0.12] and theta_star=0.055 in Invariants.json)

---

## Distortion Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| RCD    | 0     | perfect_match  |
| TBS    | 0.008333 | boundary_preserved |
| PCI    | 1.0   | full_compatibility |
| SDI    | 0     | identical_structure |
| **Phi** | **0.9983** | **highly_admissible** |

TBS is normalized: |theta*_A / range_A - theta*_B / range_B| = |0.055/0.11 - 1.475/3.0| = |0.500 - 0.492| = 0.008.
Previous computation (2026-03-29) used raw TBS = 1.44 (sweep_range was null). That value is invalid.

---

## Regime Structure Comparison

| | Scope A (stuart_landau_coupled) | Scope B (kuramoto) |
|---|---|---|
| System | Coupled Stuart-Landau oscillators | Kuramoto oscillators |
| Primary observable | PLV (phase-locking value) | r_ss (order parameter) |
| BC class | Coupling | Coupling |
| Regime count | 4 | 4 |
| Adjacency edges | 3 | 3 |
| theta* (primary transition) | K* = 0.055 | kappa* = 1.475 |
| theta* normalized | 0.055 / 0.11 = 0.500 | 1.475 / 3.0 = 0.492 |
| epsilon_working | 0.09 | 0.09 |

---

## Admissibility Assessment

Phi = 0.9983 → **highly_admissible**

Both cases share the same BC class (Coupling), the same regime count (N=4), the same
linear adjacency graph structure (3 edges), and nearly identical normalized transition
positions (TBS = 0.008). The partition of Scope B is a structurally compatible
coarsening of Scope A.

---

## Observable BC Structures

This section is required for Control C3 of the pre-registered transfer experiment
(transfer_test_0004_0001_coupling/design/controls_checklist.md).

Per the ARW/ART principle established 2026-03-18: Phi measures observable transfer,
not system transfer. The observable BC structures are documented here.

### PLV (CASE-0004, Scope A)

PLV = |mean(exp(i*(phi_1(t) - phi_2(t))))| over t in [t_transient, T]

Pre-scopal substrate requirements:
- A0 (well-defined state): satisfied — z_i in C, phases defined for |z_i| > 0 (always on limit cycle)
- A2 (stationarity): satisfied — limit cycle attractor gives stationary phase dynamics
- A3 (ergodicity): satisfied away from K*; violated at K* (critical slowing) — Z_shared applies at transition
- A5 (observability): satisfied — PLV is a well-defined real-valued map from state to [0,1]

Primitive operators structurally present in PLV:
- C (Coupling) — primary: PLV directly and exclusively measures inter-oscillator phase coherence
  produced by the coupling term K(z_j - z_i). Without coupling, PLV = 0 (independent oscillators
  with incommensurate frequencies). PLV collapses at K=0 and saturates at K >> K*.
- A (Aggregation) — secondary: PLV is a temporal mean over the trajectory. The time-aggregation
  is intrinsic to the observable definition.
- R (Restriction) — tertiary: computation occurs on the limit cycle attractor (amplitude
  restricted by the Stuart-Landau nonlinearity). The amplitude restriction lambda confines
  the state space that PLV acts on.
- S (Symmetry) — present: PLV is invariant under global phase rotation (phi_1, phi_2) ->
  (phi_1 + c, phi_2 + c). This symmetry invariance is structurally built in.

BC structure notation: **C . A . R** (Coupling-dominated, Aggregation secondary, Restriction tertiary)

PLV is a relational observable (Kuramoto: Π_rel in ARW emergence formalism). It measures
the inter-oscillator relationship directly created by the Coupling BC.

### r_ss (CASE-0001, Scope B)

r_ss = |mean(exp(i*theta_j))| — Kuramoto order parameter, time-averaged over ensemble

BC structure (established 2026-03-18): **R^3 . A . D** (Restriction-dominated)

r_ss measures how strongly individual oscillator phases are attracted toward the mean field —
a Restriction-class quantity. Although it operates on a Coupling-class system, the observable
structure is dominated by how the mean-field coupling imposes a Restriction on individual phases.

### Structural contrast and transfer interpretation

| | PLV (CASE-0004) | r_ss (CASE-0001) |
|---|---|---|
| System BC class | Coupling | Coupling |
| Observable BC structure | C . A . R | R^3 . A . D |
| Primary operator | Coupling | Restriction |
| Observable type | relational (inter-oscillator) | collective (mean-field) |

The two observables carry different BC structures despite operating on same-BC-class systems.
PLV is Coupling-dominated; r_ss is Restriction-dominated. This is the observable-system BC
structure mismatch documented in the ARW/ART findings (2026-03-18).

The high Phi = 0.9983 is therefore a strong result: structural homology at the partition
level holds across this observable BC mismatch. Both observables — despite measuring
different aspects of collective synchronization — resolve the same four-regime partition
at epsilon = 0.09 with the same transition topology (linear, 3 edges). This supports the
ARW prediction that partition structure is more conserved than observable structure across
same-BC-class systems.

---

## Registered Prediction Assessment

Pre-registered prediction (transfer_test_0004_0001_coupling/prediction_registration.md, 2026-06-02):
Phi_matched >= 0.85 (highly_admissible or partially_admissible)

Result: Phi = 0.9983 (highly_admissible)

**Outcome: CONFIRMED** — hierarchical factorisation supported.
Same BC class + matched epsilon + matching N and adjacency structure -> Phi >= 0.85.
TBS_norm = 0.008 (nearly zero) further confirms structural alignment despite different parameter spaces.

Note: epsilon is matched (both epsilon_working = 0.09), so Phi_raw = Phi_matched = 0.9983.

---

## Notes

- PCI approximation used (structural); full PCI requires aligned annotated results.
- SDI = 0 means identical graph structure (same node count, edge count, linear topology) — in
  the pipeline convention SDI is a distance (0 = identical), not a similarity score.
- Phi weights (pipeline): PCI=0.4, RCD=0.3, SDI=0.2, TBS=0.1.
- N=4 for CASE-0004 (richer than predicted N=2; three transitions at K=0.035, 0.045, 0.055).
  The primary phase-locking transition is R2->R3 at K=0.055, matching go_nogo criterion.

*Generated by pipeline.transfer, recomputed 2026-06-02 with corrected Invariants.json*
