---
status: working-definition
layer: docs/advanced/
last_updated: 2026-05-30
depends_on:
  - docs/advanced/observable_space_cover_height.md
  - docs/advanced/bc_signature_persistence_and_dominance.md
  - docs/bc_taxonomy/bc_failure_signatures.md
  - docs/advanced/bc_operator_signatures_arw.md
related:
  - docs/advanced/bc_extraction_method.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
open_questions:
  - Q-EXT-01: Can operator signatures be reliably distinguished in cover height profiles without model equations?
  - Q-EXT-02: Minimum data requirements for stable Σ extraction (sweep density, observable count)
  - Q-EXT-03: Σ stability under observable choice — does a different observable yield the same Σ?
---

# BC Signature Extraction from Observables

## Overview

This document defines a procedure for extracting a generator's BC signature Σ
directly from observable data — without access to governing equations, operator
vocabularies, or qualitative domain knowledge.

This is the bottom-up complement to `bc_extraction_method.md`, which reads Σ
top-down from model equations and qualitative observations. Top-down extraction
is sufficient when a complete model is available. For cross-system transfer,
a model is often available for the source system but not the target, or for
neither. Transfer claims must be groundable in observable behaviour alone —
otherwise they are only possible between systems that are already well-understood,
which is precisely where transfer is least needed.

**Relation to transfer.** Σ-based transfer (defined in
`bc_signature_persistence_and_dominance.md` §6) compares generators by their
persistence profiles. This comparison is only well-defined if Σ can be extracted
independently for each system. The present document provides that extraction
procedure.

---

## The Extraction Problem

Given:
- A sweep dataset for system A: BC-space points {b_i} with observable values {π(b_i)}
- No access to the equations of motion or operator structure

Produce:
- Σ_A: the generator signature of A — the persistence measure
  p_A : 2^{BC} → ℝ≥0 over active BC configurations

The challenge is that BC classes are not directly visible in observable data.
What is visible is the *projection* of BC structure into observable space:
the cover height profile, the shape of the regime partition, and the failure
signatures at transition boundaries. Σ must be read from these projections.

---

## The Extraction Chain

The procedure proceeds in four steps, each of which produces a stable intermediate
artifact.

```
Observable sweep data
        ↓  Step 1
Cover height profile h(b) in BC space
        ↓  Step 2
Operator signature identification at each η level
        ↓  Step 3
BC class assignment and persistence interval construction
        ↓  Step 4
Σ: persistence measure p(σ) over BC configurations
```

---

## Step 1 — Cover Height Profile

Construct the observable-space cover height h(b_i) following the procedure in
`observable_space_cover_height.md`:

1. Sort sweep points by observable value π(b_i)
2. Build maximal interval covers across the full ε range (log-spaced)
3. Accumulate weighted height h(b_i) = Σ_ε Σ_{C ∋ b_i} (|C| − 1)
4. Map h back to BC-space coordinates

**Output:** A height field h : B → ℝ≥0 over the swept BC space.

**Interpretation for extraction purposes.** The cover height profile encodes
the η-stratified structure of the regime: high-h regions are deep inside stable
regimes, low-h regions are near transition boundaries. The *gradient structure*
of h — where transitions are sharp vs. gradual, unidirectional vs. symmetric —
carries the operator signature of the underlying BC class.

---

## Step 2 — Operator Signature Identification

At each resolution level η (read from the ε-axis of the cover height
construction), identify which operator signature (S1–S5) is dominant in the
structure of h.

Each BC class leaves a characteristic imprint on h:

| BC class | Operator signature | Characteristic h-profile feature |
|---|---|---|
| Restriction | S1 — projection | Sharp h-boundary; ε-independent transition; Z(π) appears as hard exclusion zone |
| Coupling | S2 — product ∘ composition | Gradual h-transition with ε-dependent width; Z_shared signature near θ*; F-gradient steepens approaching critical coupling |
| Dissipation | S4 — scaling ∘ composition | Monotone h-decay toward attractor region; transition asymmetric in θ-direction (contraction vs. expansion differ) |
| Forcing | S3 — time-coupled product | Periodic or directional h-structure; θ* shifts with forcing frequency/amplitude; asymmetric approach from above vs. below |
| Symmetry Breaking | — | Bifurcation in h: single high-h basin splits into two below θ*; h-contours develop saddle point |
| Aggregation | S1 (quotient) | Step-wise h-structure at coarsening boundaries; N-dependent transition shift (σ_within/σ_between signature) |

**Failure signatures as discriminants.** The failure signature at θ* (from
`bc_failure_signatures.md`) provides the sharpest discrimination between
BC classes at the same η level:

- F-gradient + Z_shared → Coupling
- F0 (observable exits R(π) sharply) → Restriction or Forcing
- Gradual indistinguishability → Dissipation (increasing) or Aggregation (N-dependent)
- Bifurcation of h-basins → Symmetry Breaking

**Multi-BC situations.** When multiple operator signatures appear at different
η levels, record each signature with its η range. Do not force a single label.
The η-stratified signature list is the input to Step 3.

**Output:** A list of (operator signature, η interval) pairs, one per identifiable
signature layer.

---

## Step 3 — BC Class Assignment and Persistence Intervals

Map each (operator signature, η interval) pair to a BC class using the
signature-to-class correspondence in Step 2.

For each BC class C_i identified:
- η_birth,i = upper bound of its η interval (coarsest resolution at which C_i's
  signature is non-trivially present in h)
- η_death,i = lower bound of its η interval (finest resolution before C_i's
  signature becomes subsumed or indistinguishable)
- Individual persistence: p({C_i}) = η_birth,i − η_death,i

For overlapping η intervals (multi-BC configurations):
- Identify the η range of coherent joint presence
- Check for conflict signature (one class suppressing the other's h-structure)
  vs. reinforcement (joint h-structure more stable than either alone)
- Joint persistence p({C_i, C_j}) = length of coherent joint interval

**Output:** Persistence intervals {(C_i, I_i)} and joint persistence estimates
{(σ, p(σ))} for identified multi-BC configurations.

---

## Step 4 — Σ Assembly

Assemble the persistence measure:

```
Σ : 2^{BC_active} → ℝ≥0,    σ ↦ p(σ)
```

where BC_active = {C_i : p({C_i}) > 0}.

Normalise p(σ) by max_{σ} p(σ) to obtain a scale-invariant profile
comparable across systems with different η ranges.

**Output:** Σ — the generator signature of the system, extracted from
observables alone. This Σ is directly comparable with Σ extracted from
other systems (same or different domain) using the transfer compatibility
measure d(Σ, Σ') defined in `bc_signature_persistence_and_dominance.md` §6.

---

## Scope and Limitations

**What this procedure can establish:**

- Which BC classes are structurally active in a system's regime architecture
- The relative robustness (persistence) of each class and their joint configurations
- A Σ that supports transfer comparison with other systems

**What it cannot establish:**

- The bedrock-level identity of BC classes — Σ is read in projected space
  (operator signature level), not from the abstract relational types
  (see `bc_signature_persistence_and_dominance.md` §Overview)
- Whether a shared Σ reflects shared generative structure or coincident
  projection — this remains an interpretive claim requiring additional evidence
- Σ for systems where no sweep data is available (the procedure requires
  variation across BC space)

**Observable dependence.** Σ may in principle depend on which observable π
is used for the cover height construction. If two observables yield different
Σ for the same system, this is itself diagnostic: the system's regime
architecture is not fully captured by any single observable, and the true Σ
is the union of what each observable reveals. This is open question Q-EXT-03.

**Minimum data requirements.** The η-stratification in Step 2 requires
sufficient sweep density across the relevant BC range, and sufficient ε
resolution to distinguish signature layers. Minimum requirements for stable
Σ extraction are open (→ Q-EXT-02).

---

## Relation to bc_extraction_method.md

| Dimension | bc_extraction_method.md | This document |
|---|---|---|
| Direction | Top-down: model/qualitative → pipeline case | Bottom-up: observable data → Σ |
| Primary output | ScopeSpec + BCManifest (pipeline case) | Σ (transfer-comparable signature) |
| Requires model? | Preferred; has fallback for no-equation domains | No — data only |
| Use case | Case construction for new system | Transfer comparison across systems |
| Prerequisite | Qualitative understanding of system | Sweep data with observable |

The two procedures are complementary. For systems where both apply, the
resulting BC candidate set (bc_extraction_method.md Step D) and the extracted
Σ (this document Step 4) should be compared as a consistency check.

---

*Establishes the extraction procedure presupposed by transfer claims in Part VI §6.3–6.4.*
*For the formal Σ definition: `bc_signature_persistence_and_dominance.md`.*
*For top-down BC identification: `bc_extraction_method.md`.*
