---
status: working-definition
layer: docs/bc_taxonomy/
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
θ̂*(S)   = (θ*(S) − b_min) / (b_max − b_min)          ∈ [0, 1]
TBS_norm = | θ̂*(S) − θ̂*(S') |                        ∈ [0, 1]
```

where [b_min, b_max] is the sweep range stored in `Invariants.json`.
*(Notation corrected 2026-07-17: the earlier one-line form θ*/range silently
assumed b_min = 0 and divided a scalar by what is typed as an interval; the
two-step min–max form above is what `transfer_v2.py` has computed all along —
`x_norm = (theta − range_min)/(range_max − range_min)`.)* TBS_norm expresses
the transition's **relative position within each scope's declared exploration
window** — not an intrinsic system property (see the Q-REL-08 limitation
below).

`pipeline.transfer` uses TBS_norm automatically when `sweep_range` is present in
both Invariants files; it falls back to TBS_raw otherwise (logged as `method: raw_only`).

**Limitation (registered 2026-07-17, Q-REL-08):** the normalisation inherits
the choice of explored range, which is a case-design decision, not a system
property — widening a sweep moves the same θ* to a smaller fraction with no
structural change. Cross-case TBS_norm comparisons are therefore only
meaningful when the ranges are themselves comparable (matched design, or a
shared natural domain). transfer_v2's sweep-window sensitivity band mitigates
but does not remove this. A canonical reference range (natural domain, first
structural singularity, dimensionless control parameter, …) is an open
question: see Q-REL-08 in `docs/notes/open_questions.md`.

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

Take the finer partition as reference. For each of its regime classes Rᵢ, the
**corresponding** class in the comparison partition is the one sharing the most
member states on the common normalised axis (**maximum-overlap correspondence**
— this rule is part of the definition; without it PCI is not a function). Then

```
pᵢ         = |Rᵢ ∩ corr(Rᵢ)| / |Rᵢ|
PCI(A→B)   = Σᵢ |Rᵢ|·pᵢ / Σᵢ |Rᵢ|        (point-weighted containment)
PCI_scalar = min( PCI(A→B), PCI(B→A) )    (strict, worst direction)
```

computed from the actual per-point labels (`annotated_results`) resampled
onto a common uniform reference grid on [0, 1], never from counts or
adjacency alone (v1 defect, 2026-06-02). *(Aligned 2026-07-18 to the
implementation: `transfer_v2.py` computes point-weighted containment —
acc/total over grid cells, not an unweighted (1/N)Σpᵢ class average — and
reports both directions plus their strict minimum as the scalar; the
directional pair carries the containment/coarsening reading.)* The
**adjusted Rand index** is reported alongside as the label-invariant,
symmetric cross-check.

**Interpretation (sharpened 2026-07-17):** PCI is a **directed overlap
score** — the purity of the finer-to-coarser assignment — not a symmetric
ground truth. The correspondence is not injective: several fine classes can
map to one coarse class, so PCI can be high while fine structure has been
heavily merged; RCD registers that merging by count, and the two are read
together (a coverage check — does every comparison class get meaningfully
hit? — is the natural third quantity). The directionality is what licenses
the arrow in Φ(S → S'): admissible coarsening in the arrow direction,
mismatch against it.
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

**Constructive triviality in the 1D-sweep tier (WP-A4 amendment, 2026-07-17):**
the definition above uses the Δ-induced transition graph (edges = admissible
transitions under Δ) — an object whose general construction does not yet
exist. What the pipeline actually produces is the **sweep-realised adjacency
graph**: regimes are connected components of the consecutive-sample
ε-adjacency graph on an *ordered* sweep, hence contiguous runs, hence the
transition graph is forced to be the path on N nodes — always. In this tier
SDI = GED(path(N_A), path(N_B)) is a deterministic monotone function of
|N_A − N_B|: **collinear with RCD by construction**, carrying no independent
information. Disposition (monograph Part VII V4.2): SDI is held **out of Φ**
(w₄ = 0) and reported unnormalised as a diagnostic, until either (a) it is
computed on an **attributed** transition graph (edges carrying ε_merge,
hysteresis, order of contact α, signature type, or BC label) or (b) the
Δ-induced graph above is actually constructed (open: Q_NEW_25). Where a
normalised value is reported anyway, the normaliser is the size proxy
SDI_max = |V_A| + |V_B| + |E_A| + |E_B| under unit costs — a size reference,
*not* the maximum distance between graphs of these sizes. The interpretation
note above ("PCI = 1 but SDI > 0") applies only to the Δ-induced graph, and
is impossible in the sweep tier.

**Experimental targets:**

| System | Expected SDI | Reason |
|---|---|---|
| Kuramoto S_K → S_MF (large N) | 0 | Same 3-class sequential structure |
| Consensus S_Op → S_MF | 1 | R_Op4 node deleted; its edges lost |
| Geopolitical S_A → S_G | 2–3 | R_A4 and R_A6 absorbed into adjacent classes |

---

## Composite Decision Score Φ

*(Section rewritten 2026-07-17 to the v2 form; the earlier four-term formula
with unclamped TBS term and ambiguous N is superseded — it could leave [0, 1]
for TBS_norm > 0.5 and re-counted N through three components.)*

**Definition (as in monograph Part VII, Def 11):**

```
Φ(S → S') = w₁ · (1 − RCD/N_max)
          + w₂ · max(0, 1 − 2·TBS_norm)
          + w₃ · PCI
          [ + w₄ · (1 − SDI/SDI_max) ]
```

with N_max = max(N, N', 1), w_i ≥ 0, Σ w_i = 1, every term clamped to [0, 1]
(hence Φ ∈ [0, 1] by construction), and **w₄ = 0 by default** in the 1D-sweep
tier (SDI constructive triviality, above); the SDI term is enabled only
against an attributed transition graph.

**Mapping to the reference implementation.** `transfer_v2.py` computes the
same three-channel structure under different term names:
Φ = W_PCI·PCI + W_TOPO·topo + W_TBS·max(0, 1 − TBS/0.5), with
(W_PCI, W_TOPO, W_TBS) = (0.55, 0.25, 0.20) and
topo = ½·count_score + ½·edge_score. On path-forced sweep graphs the edge
score is count-determined, so the code's topology term and Def 11's RCD term
carry the same information; the two forms are channel-equivalent
(PCI + count + TBS), differing in term naming and weight labels only. The
code's weights are the declared calibration; they are documented as
provisional in every report.

**Epistemic status (binding):** Φ is a **decision score**, not an intrinsic
quantity — weights are calibrated, not theory-identified; the arrow is
inherited entirely from the directed PCI (containment reading); N remains a
confounder even in the three-channel core (RCD directly, PCI indirectly).
Verdicts are reported against a three-way decision band (fail / ambiguous /
partition-compatible) rather than a single cut; thresholds are declared
calibration conventions. Guards: VOID (missing labels / sweep_range /
undocumented ε-mismatch) and TRIVIAL_PARTITION (N ≤ 1) make Φ *undefined*,
not low. And per WP-A3: a valid, high Φ evidences **partition
compatibility** — a necessary condition for structural transfer, never
evidence of shared BC-class structure (Q-REL-05, expected-negative).

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
