---
status: working-definition
---

# Transfer Distortion Metrics

This document defines the formal metrics used to quantify how much
structural information is lost or distorted when a scope transition
S → S' is performed.

These metrics operationalize the ARW admissibility criterion:
instead of a binary admissible/inadmissible verdict, they provide
a graded measure of how close to admissible a given reduction is.

The metrics were developed in [experiments/aggregation_meanfield.md](../../experiments/aggregation_meanfield.md)
and are reused in the labyrinth transfer experiments.

---

## Conceptual Setup

Given two scopes S and S' over the same system, with induced partitions:

```
A(S)  = R     (fine-grained partition, N classes)
A(S') = R'    (coarse-grained partition, M classes)
```

A perfectly admissible reduction has M ≤ N and every class Rᵢ ∈ R
is fully contained within some class R'ⱼ ∈ R':

```
∀i ∃j: Rᵢ ⊆ R'ⱼ
```

Distortion occurs when this containment fails — some Rᵢ straddles
a boundary in R', or some R'ⱼ has no correspondent in R.

---

## Metric 1 — Regime Count Discrepancy (RCD)

**Definition:**

```
RCD = |N - M|
```

where N = |R| and M = |R'|.

**Interpretation:**
The number of regime classes that are either merged or lost under the scope transition.

**Expected behavior:**
- RCD = 0: scope transition preserves partition cardinality (possible only if ε changes without BC change)
- RCD > 0: classes have merged (aggregation, coarsening) or split (refinement)
- RCD is unsigned — it does not distinguish merger from creation

**Limitations:**
RCD only counts classes. Two partitions can have RCD = 0 while being
structurally incompatible (same count, different boundaries).
Must be used alongside PCI.

**Experimental targets:**

| System | Expected RCD | Reason |
|---|---|---|
| Kuramoto S_K → S_MF (large N) | 0 | Mean-field recovers same 3 classes |
| Consensus S_Op → S_MF (any N) | 1 | R_Op4 (frozen disorder) has no MF equivalent |
| Labyrinth zone → episode scope | 3–4 | Intra-episode mode structure invisible at episode level |

---

## Metric 2 — Transition Boundary Shift (TBS)

**Definition:**

For scopes over the *same* control parameter axis:

```
TBS_raw = |θ*(S) - θ*(S')|
```

For *cross-system-type* transfers where θ is measured on incommensurable axes
(e.g. κ dimensionless vs. E in Joules), use the normalised form:

```
TBS_norm = |θ*(S) / range(S)  −  θ*(S') / range(S')|
```

where `range(S) = max(θ) − min(θ)` is the sweep range stored in `Invariants.json`.
TBS_norm ∈ [0, 1] expresses θ* as a fraction of the explored BC space.

`pipeline.transfer` uses TBS_norm automatically when `sweep_range` is present in
both Invariants files; it falls back to TBS_raw otherwise (logged as `method: raw_only`).

**Interpretation:**
How far into its respective BC space does each scope place the primary transition?
TBS_norm ≈ 0 means both scopes transition at the same relative position.
TBS_norm ≈ 0.5 means one scope transitions at 25% and the other at 75% of its range.

**Expected behavior:**
- TBS_norm → 0 for same-class transfers with matched BC parameterisation
- TBS_norm > 0 for cross-BC-class transfers (different classes place transitions differently)
- TBS_raw(N) ~ N^{-α} for mean-field comparisons within the same system type

**Experimental targets:**

| System | Control parameter θ | Expected TBS |
|---|---|---|
| Kuramoto S_K → S_MF (same axis) | Coupling K | TBS_raw → 0 as N → ∞ |
| Kuramoto (CASE-0001) → Pendulum (CASE-0002) | κ [0,3] vs κ [0,10] | TBS_norm ≈ 0.167 (moderate_shift) |
| Kuramoto (CASE-0001) → Doppelpendel (CASE-0003) | κ vs E (J) | TBS_norm ≈ 0.356 (moderate_shift) |

---

## Metric 3 — Partition Compatibility Index (PCI)

**Definition:**

For each regime class Rᵢ ∈ R, define the compatibility:

```
pᵢ = fraction of states x ∈ Rᵢ correctly classified under S'
   = |{ x ∈ Rᵢ : [x]_S ⊆ [x]_S' }| / |Rᵢ|
```

Overall PCI:

```
PCI = (1/N) Σᵢ pᵢ
```

**Interpretation:**
The fraction of fine-grained regime assignments that survive the scope transition.
PCI = 1 means perfect admissibility.
PCI < 1 identifies which regime classes are being distorted and by how much.

**Expected behavior:**
- PCI = 1 for bulk regime states far from boundaries
- PCI < 1 near transition boundaries (boundary-straddling states)
- PCI depends on ε: larger ε shrinks boundary regions, increases PCI

**Per-class PCI:**
The per-class values pᵢ reveal which specific regimes are being distorted.
In the consensus model: pᵢ near the R_Op1/R_Op2 boundary is expected
to be lowest — these are the states most affected by finite-N fluctuations.

**Experimental targets:**

| System | Expected PCI | Notes |
|---|---|---|
| Kuramoto S_K → S_MF (large N) | > 0.95 | Small boundary region only |
| Consensus S_Op → S_MF (small N) | 0.7–0.9 near transition | Boundary region is large at small N |
| Labyrinth: zone scope → episode scope | < 0.5 | Episode scope loses most intra-episode structure |

---

## Metric 4 — Structural Distortion Index (SDI)

**Definition:**

Define the regime graph G_S as the directed graph where:
- nodes = regime classes in R
- edges = admissible transitions between regime classes under Δ

```
SDI = graph_edit_distance(G_S, G_S')
```

where graph_edit_distance counts the minimum number of
node insertions, deletions, and edge changes to transform
G_S into G_S'.

**Interpretation:**
SDI measures how much the *transition topology* changes under the scope transition.
Two partitions with the same classes but different transition structures
have PCI = 1 but SDI > 0.

**Expected behavior:**
- SDI = 0 for admissible reductions that preserve partition type
- SDI > 0 when BC changes alter which transitions are possible
- SDI is sensitive to regime merging: if R₁ and R₂ merge into R'₁,
  all edges incident to R₁ or R₂ become incident to R'₁

**Note on computation:**
Graph edit distance is NP-hard in general but tractable for
small partition sizes (< 20 regimes).
For the experimental systems (3–6 regime classes), exact computation is feasible.

**Experimental targets:**

| System | Expected SDI | Reason |
|---|---|---|
| Kuramoto S_K → S_MF (large N) | 0 | Same 3-class sequential structure |
| Consensus S_Op → S_MF | 1 | R_Op4 node deleted; its edges lost |
| Geopolitical S_A → S_G | 2–3 | R_A4 and R_A6 absorbed into adjacent classes |

---

## Composite Admissibility Score

For a compact summary, define:

```
Φ(S → S') = w₁ · (1 - RCD/N) + w₂ · (1 - TBS_norm/0.5) + w₃ · PCI + w₄ · (1 - SDI/SDI_max)
```

with weights w₁ + w₂ + w₃ + w₄ = 1, and TBS_norm as defined above.
For same-axis transfers TBS_norm = TBS_raw / max_range is used automatically.

This produces a single admissibility score in [0, 1]:
- Φ = 1: perfectly admissible reduction
- Φ < 0.7: substantial distortion — scope transition should be treated as inadmissible

**Calibration:**
Weights are to be set based on the Kuramoto calibration experiment,
where the theoretical admissibility threshold is known analytically.

---

## Using the Metrics Together

The four metrics measure different aspects of distortion:

| Metric | What it captures | Blind to |
|---|---|---|
| RCD | Class count change | Boundary shift within same count |
| TBS | Boundary location shift | Structural changes not at boundaries |
| PCI | Per-state classification accuracy | Topology changes that preserve class membership |
| SDI | Transition topology change | Fine-grained boundary effects |

A complete distortion analysis requires all four.
A reduction can have RCD = 0, TBS ≈ 0, PCI ≈ 1, but SDI > 0
(same classes, same boundaries, different transition structure).

---

*For the experimental protocol that develops these metrics, see [experiments/aggregation_meanfield.md](../../experiments/aggregation_meanfield.md).*
*For the admissibility criterion these metrics quantify, see [docs/core/arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md).*
