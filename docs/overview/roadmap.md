---
status: working-definition
---

# Research Roadmap

This roadmap describes the research phases, milestones, and go/no-go decisions
for the ARW/ART framework development.

The OSV fellowship timeline (12 months, full-time) maps onto Phases 1–4.
Phase 0 is conceptual groundwork already completed.

---

## Phase 0 — Formal Backbone *(completed)*

**Goal:** Establish the core formal vocabulary and analytical structure.

**Completed:**
- ARW scope tuple S = (B, Π, Δ, ε) defined
- ARW operator A(S) = R_S formalized
- Admissible reduction criterion [x]_S ⊆ [x]_S' established
- ART scope template defined
- BC taxonomy: six classes with regime consequences
- Partition type typology: five types with BC mappings
- Distortion metrics: RCD, TBS, PCI, SDI defined

**What "done" meant:** The formal vocabulary is sufficient to write
a complete ART instantiation for any new system without ambiguity.
Demonstrated by the geopolitical scope example, which uses the framework
to generate non-trivial structural claims.

---

## Phase 1 — Mechanical Calibration *(Months 1–3)*

**Goal:** Validate the partition extraction pipeline on systems with
analytically known regime structure.

**Systems:** Kuramoto oscillators, two/three-link pendulum.

**Key deliverables:**
- Partition extraction pipeline implemented and tested
- K_c recovery in Kuramoto within analytical error bounds
- Admissibility boundary κ*(N) measured for pendulum scope reduction
- TBS(N) scaling exponent calibrated

**Go/No-Go criterion:**
Pipeline recovers K_c to within 5% across N ∈ {100, 500, 2000}.
If it does not: the partition extraction method requires revision
before Phase 2 can produce interpretable results.

**Why this gates Phase 2:**
The social and cognitive systems in Phase 2 have no analytical ground truth.
The pipeline's reliability must be established here, where ground truth exists.

---

## Phase 2 — Core Investigation *(Months 4–8)*

**Goal:** Test the central hypothesis across social and cognitive domains.
Three parallel workstreams.

### 2a — Opinion Dynamics (Months 4–6)

Agent-based consensus/polarization/fragmentation regimes.

**Key deliverables:**
- Regime partition extracted under S_agent and S_MF
- TBS(N), RCD, PCI, SDI measured across ε_bc × N parameter space
- Network topology variation: scale-free and lattice BC comparisons
- First cross-domain BC taxonomy test: coupling BC → sequential partition

**Go/No-Go criterion:**
PCI(S_agent → S_MF) < 1 for small N and near transition boundaries.
If PCI = 1 everywhere: distortion metrics are insensitive — methodology is flawed.

### 2b — Context-Navigation Agent (Months 5–8)

Labyrinth agent with mode ecology, anchor memory, sleep consolidation.

**Key deliverables:**
- Policy embedding cluster count ≥ 3 under mixed-zone environment
- Zone–mode alignment score > 0.7
- Sleep sharpening index: cluster separation increases post-consolidation
- Transfer PCI > 0.6 in structurally similar new mazes

**Go/No-Go criterion:**
Discrete policy clusters emerge (count ≥ 2 in Phase 1 of labyrinth experiment).
If only one cluster: modal cognition hypothesis fails — single smooth policy dominates.

### 2c — Mean-Field Aggregation (Months 6–8)

Formal cross-scope comparison for opinion dynamics system.

**Key deliverables:**
- Admissibility boundary mapped in (N, ε_bc) parameter space
- TBS(N) ~ N^{-α}: exponent α measured
- Composite admissibility score Φ calibrated against analytical cases from Phase 1

---

## Phase 3 — Abstraction *(Months 9–10)*

**Goal:** Generalize findings into a portable BC taxonomy and transfer methodology.

**Key deliverables:**
- BC taxonomy validated: which class → partition type mappings held across domains?
- Failure cases documented: where did the prediction break down and why?
- Transfer distortion metrics refined based on Phase 2 empirical results
- First draft of cross-domain comparison methodology

**Go/No-Go criterion:**
At least 3 of the 6 BC class → partition type predictions confirmed across
two or more independent systems. If fewer: the taxonomy is domain-specific,
not universal — the scope of the research claim must be narrowed.

---

## Phase 4 — Consolidation *(Months 11–12)*

**Goal:** Package findings as a reusable research artifact.

**Key deliverables:**
- Open-source Python toolkit: partition extraction, distortion metrics, scope comparison
- Publication-ready manuscript: core framework + two cross-domain case studies
- Repository finalized: all docs at `working-definition` or above
- v1.0 release tag

**What "publication-ready" means:**
The manuscript presents one confirmed cross-domain BC → partition type case,
one partial or failed case with analysis of why, and the distortion metric
methodology with calibration results from Phase 1.
A negative result in Phase 2 is publishable if the failure mode is informative.

---

## Decision Points

| Point | Condition | If yes | If no |
|---|---|---|---|
| After Phase 1 | Pipeline recovers K_c within 5% | Proceed to Phase 2 | Revise extraction method; delay Phase 2 by 4–6 weeks |
| After Phase 2a | PCI < 1 near boundaries | Proceed to Phase 2c | Revisit metric sensitivity before cross-scope comparison |
| After Phase 2b | Policy clusters emerge | Proceed to transfer tests | Investigate architecture; may require mode count or gating revision |
| After Phase 3 | ≥ 3 BC predictions confirmed | Full Phase 4 | Narrow manuscript scope to confirmed cases only |

---

## Relation to OSV Fellowship Application

The fellowship covers Months 1–12 (Phases 1–4).
Phase 0 is presented as completed groundwork demonstrating feasibility.

The fellowship application foregrounds the context-navigation agent (2b)
as the narrative anchor — biologically motivated, empirically concrete.
ARW/ART is the scientific substrate that makes the agent results interpretable
across domains.

See the 1-pager at `osv_1pager.pdf` for the condensed version.
