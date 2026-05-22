---
status: note
layer: docs/art_instantiations/
title: "Session Document Index — KHT Architecture, ARW Analysis, and Extended Theory"
created: 2026-05-14
note: >
  This document indexes all files produced in this working session and maps
  their dependency structure, repo layer assignments, and conceptual roles.
  It serves as the entry point for navigating the full document set.
  Documents marked [superseded] should be replaced by their revision in
  the repo; the original is retained for reference only.
---

# Session Document Index

## Overview

This session produced 14 documents across four conceptual clusters:

```
Cluster A: KHT Unified Architecture (Layers 1–4)
Cluster B: KHT Applied Theory (ARW analysis, notation, applications)
Cluster C: ARW Methodology (aggregation limits, partition stability)
Cluster D: Labyrinth Experiment (operator/modulator patch)
```

The dependency graph runs bottom-up: Cluster A must be read before Cluster B;
Cluster C is domain-independent and can be read standalone; Cluster D depends
on the KHT Layer 4 architecture for its theoretical motivation.

---

## Cluster A — KHT Unified Architecture

These documents define the four-layer KHT architecture and constitute the
theoretical foundation for all downstream documents.

**Reading order:** Layer 1 → Layer 2 → Layer 3 → Layer 4 → Index

---

### A1 — `kht_architecture_layer1.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** The primitive operator–modulator space. Four trajectory-free
operators (Ni, Si, Ne, Se) × eight modulator clusters (from T/F, I/E, J/P)
yield 32 fully symmetric combinations. Defines the Layer 1 distance metric
d = d_op + Hamming(M), the duality map D, and the coupled-oscillator substrate
(§3.5–3.6) that grounds the discrete structure in continuous dynamics.

**Key results:**
- 32-element symmetric O×M space as formal null model
- Layer 1 distance metric (range 0–5)
- Duality operator D: (O, M) → (O*, M*), involution D² = 1
- Modulators as coupled oscillators in double-well potentials
- Operators as independent transformation axes (not coupling topologies)
- Continuous substrate → discrete clusters as stable synchronization attractors

**Depends on:** None (foundational)
**Required by:** All other KHT documents

---

### A2 — `kht_architecture_layer2.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** Emergence of 16 persistent profiles from the Layer 1 space via
two sequential biological boundary conditions: Restriction (genetic connectivity
bias) and Dissipation (Hebbian consolidation). The coverage criterion as the
formal selection condition for valid profiles.

**Key results:**
- Two-phase BC mechanism: Restriction (Phase 1) → Dissipation (Phase 2)
- Coverage criterion: minimal complete modulator-axis and operator-family coverage
- 16 profiles as structural consequence of coverage + duality geometry
- Profile structure: Ego-block + Shadow-block = D-conjugate pair
- Appendix function hierarchy as activation weighting w (dynamic property,
  not primitive postulate)
- Falsifiable prediction: coverage-violating profiles exhibit higher regime instability
- SD/UD developmental subtypes as Shadow-block accessibility difference

**Depends on:** A1
**Required by:** A3, A4, B1, B2, B3, B4, B5

---

### A3 — `kht_architecture_layer3.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** Dynamic regime transitions driven by control parameters τ (temporal
pressure), σ (stress/invalidation), and ξ (exploration opportunity). Four regimes
characterized by Layer 1 distances from R1. Social-level dynamics and the
Resonance Mechanism as a structured C-R3 activation protocol.

**Key results:**
- Four regimes: R1 (Ego), R2 (Subconscious), R3 (Unconscious), R4 (Superego)
- Regime distances: d(R1,R2)=3; d(R1,R3)=d(R1,R4)=4
- R1→R2 is modulator-only (shallow); R1→R3 is operator-shift; R1→R4 is full dual
- R4 as scope transition (Z_shared): all R1-calibrated observables fail there
- Observable sufficiency table: O3 (modulator cluster) has widest cross-regime coverage
- Resonance Mechanism as Layer 3 protocol: structured R3 induction in subgroups
- Social coupling: faction formation as Kuramoto-analog synchronization

**Depends on:** A1, A2
**Required by:** A4, B1, B2, B3, B4, B5, D1

---

### A4 — `kht_architecture_layer4.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** Computational instantiation of Layers 1–3 as a behavioral proxy
for a KHT-typed agent. Three-component architecture: Context Parser (estimates
τ, σ, ξ) → Regime Engine (maintains R, applies transition logic) → Response
Generator (produces (O, M)-consistent outputs). Design constraints C1–C8.

**Key results:**
- Three-component simulation architecture
- Operator/modulator translation tables for response generation
- Design constraints derived from lower layers (violations require
  lower-layer revision)
- Fidelity limits: simulation is behavioral proxy, not biological instantiation;
  R4 cannot be genuinely reproduced
- Layer 4 as synthetic data generator for empirical testing
- Multi-agent extension: faction formation and Resonance Mechanism as
  coupled LLM protocol

**Depends on:** A1, A2, A3
**Required by:** D1

---

### A5 — `kht_architecture_index.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** Entry point for the four-layer architecture. Architecture diagram,
layer summaries, source reconciliation (Appendix vs. Gesamtausgabe), relationship
to ARW analysis, cross-layer open questions Q-CL-1 through Q-CL-5.

**Depends on:** A1, A2, A3, A4
**Required by:** Navigation only

---

## Cluster B — KHT Applied Theory

These documents apply the unified architecture to ARW analysis, formal notation,
empirical hypotheses, and domain extensions.

---

### B1 — `kht_arw_analysis_revised.md`
**Layer:** `docs/art_instantiations/` | **Status:** `note`

**Content:** Full ARW analysis of KHT grounded in the four-layer architecture.
BC class assignments at specific architectural layers. Observable candidates with
substrate analysis. Scope tuple S_KHT_L3. Falsification conditions. Open questions
with resolution status.

**Key results:**
- BC assignments grounded by layer: Restriction (L2 Ph1), Dissipation (L2 Ph2),
  Coupling (L2+L3), Forcing (L3)
- Candidate metric on X: d = d_op + Hamming(M) — resolves Q-KHT-1
- O3 (modulator cluster) as primary cross-regime observable
- O1+O3 pairing resolves OCEAN side-blindness problem
- S_KHT_L3 scope tuple with explicit B, Π, Δ, ε
- Q-KHT-5 and Q-KHT-7 resolved; Q-KHT-9, Q-KHT-10 newly opened
- R1→R4 as Z_shared (scope transition, not regime boundary)

**Supersedes:** `kht_arw_analysis.md` [retain for reference, do not promote]
**Depends on:** A1, A2, A3
**Required by:** B3, B4, B5, C1

---

### B2 — `kht_prescopal_substrate_hypotheses.md`
**Layer:** `docs/notes/` | **Status:** `hypothesis`

**Content:** Neurobiological substrate hypotheses for the KHT architecture.
Five hypotheses (H1–H5) about operator dissociability, modulator global reach,
operator agnosticism, developmental sequence, and biological BC mechanism.
Revised Si/Ne candidate substrates with confidence levels and reverse-inference
caveat. Nativism/interactionism question explicitly left open.

**Key results:**
- H1: Operators on anatomically dissociable substrates
  (Si → perirhinal; Ne → lateral/anterior temporal — revised from original)
- H2: Modulators on globally-reaching systems
  (I/E → DMN/TPN; T/F → DLPFC/VMPFC; J/P → basal ganglia/ACC)
- Confidence levels for all candidate substrates
- Reverse inference problem explicitly noted
- Eight empirical questions EQ-1 through EQ-8 ordered by tractability

**Depends on:** A1, A2
**Required by:** B4 (indirectly)

---

### B3 — `kht_state_notation.md`
**Layer:** `docs/art_instantiations/` | **Status:** `working-definition`

**Content:** Compact state notation |O, M, R, w, θ⟩ for KHT cognitive states,
analogous to quantum number notation. Symmetry operators D, M̃, P_op and their
Klein four-group structure V₄. Selection rules for regime transitions. Latent
degrees of freedom at each scope level. Profile as symmetry-broken dominant
attractor configuration.

**Key results:**
- Full state vector |O, M, R, w, θ⟩ with layered scope structure
- Symmetry operators: D (full dual), M̃ (modulator inversion), P_op (operator swap)
- Klein four-group: {1, M̃, P_op, D} = V₄ = Z₂ × Z₂
- Four regimes as orbit of R1 under V₄: {R1, R2, R3, R4} = {1·R1, M̃·R1, P_op·R1, D·R1}
- Selection rules with distances and transition conditions
- Scope-layered latency: w latent at L1, θ latent at L2, w partial-latent at L3
- Shadow-block as D-conjugate stabilized attractor configuration
- INFJ/ENFJ ambiguity: same compact label |Ni, FEP, R1⟩, different w

**Depends on:** A1, A2, A3, C2
**Required by:** B4, B5

---

### B4 — `kht_applications_clinical_cognitive.md`
**Layer:** `docs/art_instantiations/` | **Status:** `hypothesis`

**Content:** Five empirically tractable hypotheses derived from the state notation,
each with formal derivation, empirical prediction, minimal test design, and
scope limitations.

**Hypotheses:**
- **H-A** (Attractor Binding Strength → Regime Stability): weaker consolidation →
  more frequent transitions, slower recovery. Structural analog to emotion
  dysregulation and identity instability.
- **H-B** (Creativity as Threshold-Gated Operator Shift): creative production =
  R3 activation (ξ > θξ); R3 creativity structurally different from R4 creativity.
- **H-C** (Masking as Operator-Stable Modulator Shift): O stable, M forced
  off-attractor under social forcing → systematic fatigue.
- **H-D** (Therapeutic Change as Threshold Recalibration): four mechanistically
  distinct therapeutic targets T1–T4 (θσ↑, hysteresis↑, forcing↓, Shadow integration).
- **H-E** (Developmental Trajectory → Profile Stability): stability increases
  monotonically from adolescence through early adulthood as Dissipation converges.

**Logical ordering:** H-E → H-A → H-D; H-B and H-C independent but share basis.

**Depends on:** A2, A3, B1, B3
**Required by:** B5 (indirectly)

---

### B5 — `kht_group_dynamics.md`
**Layer:** `docs/art_instantiations/` | **Status:** `hypothesis`

**Content:** Group-level extension of the KHT regime framework. Central concept:
the collective regime manifold Φ_G = {(R_k, α_k)} — the set of simultaneously
admissible collective attractor tendencies before regime stabilization. Four
stabilization mechanisms M1–M4. Social phenomena as collective regime dynamics.

**Key results:**
- Collective regime manifold: classical metastability description, not QM
- Four collective regime types: C-R1 through C-R4
- Four stabilization mechanisms: M1 (coupling/Kuramoto), M2 (external forcing),
  M3 (resonance-driven), M4 (parameter shift)
- Social phenomena reframed: polarization as bifurcation, groupthink as
  premature collapse, institutional rigidity as attractor deepening,
  innovation as near-critical manifold state
- Connection to variance crossover: κ_c as group-level N*
- Connection to CASE-0010: institutional regime manifold grounding

**Depends on:** A2, A3, B1, B3, C1
**Required by:** Nothing (terminal)

---

## Cluster C — ARW Methodology

These documents extend the ARW framework itself, independent of KHT. They apply
to any system using typological observables or scope-relative descriptions.

---

### C1 — `arw_aggregation_limits_typological_observables.md`
**Layer:** `docs/advanced/` | **Status:** `note`

**Content:** Formal characterization of aggregation limits for typological
observables. The variance crossover problem: N* as the aggregation level where
σ²_W = σ²_B. Two failure modes: F1 (cover too coarse) and Z_shared (scope
heterogeneous). Aggregation Stability Measure (ASM) with Variance Ratio Profile
V(A), bootstrap N* estimation, context-heterogeneity adjustment, and ICC connection.

**Key results:**
- Variance crossover N* as scope parameter (not statistical artifact)
- F1 vs. Z_shared: distinct failure modes requiring distinct remedies
- Monotone decrease of V(A) as null hypothesis (not structural law)
- "Uninformative" formulation corrected: marginal contribution collapses,
  not absolute information
- ASM tuple: {V(A), N*_median, N*_CI, N*_IQR, V_slope, N*_adjusted}
- ICC connection: N* = aggregation level where ICC drops below 0.5
  → computable with standard multilevel modeling packages
- Ecological fallacy and atomistic fallacy as symmetric scope violations

**Depends on:** ARW core docs (glossary, observable_decomposition)
**Required by:** B1, B5, C2

---

### C2 — `arw_quantization_partition_stability.md`
**Layer:** `docs/notes/` | **Status:** `note`

**Content:** Structural unification of quantized descriptions across domains.
Central thesis: a description appears quantized iff its partition is invariant
under (B, Δ, ε). Physical quantization is a formal special case (§3.5).
Condensed vs. dilute matter as collective order analog (§3.4). Latent degrees
of freedom and descriptive collapse (§3.6).

**Key results:**
- Four-condition framework: (X, B, Δ, ε) → stable partition π(X_B)
- Physical quantization as ARW special case via spectral theorem (§3.5)
- Superposition → F-gradient under Ô; Interference → B-excluded states;
  Entanglement → Z_shared at joint scope; Uncertainty principle →
  incompatible partitions under non-commuting observables
- Three features beyond embedding: linearity of ℋ, Born rule, unitarity
- Condensed/dilute matter: order parameter Ω(A) = σ²_B(A) − σ²_W(A);
  N* as typological T_c; V(A) as decoherence curve (§3.4)
- Three latency mechanisms: Δ-averaging, ε-blindness, B-inadmissibility (§3.6)
- EFT as systematic latency management; renormalization as scope-map sequence
- Spontaneous symmetry breaking as latency inversion

**Depends on:** C1, ARW core docs
**Required by:** B3

---

## Cluster D — Labyrinth Experiment

---

### D1 — `labyrinth_patch_op_mod_split.md`
**Layer:** `experiments/` | **Status:** `proposal`

**Content:** Concrete implementation patch for the labyrinth context-navigation
experiment. Splits the 7-dimensional weight vector w into w_op (5-dim, content
observables) and w_mod (2-dim, context observables), motivated by the KHT
Layer 4 operator/modulator separation.

**Key results:**
- Observable classification: IDX_OP = [0,1,2,3,6]; IDX_MOD = [4,5]
- w_mod updated via direct saliency-type mapping with inertia α = 0.3
  (soft update, not hard switch)
- w_op updated via existing archetype library (unchanged logic, 5-dim)
- Policy Network input shape unchanged (7-dim reconstructed by build_o_weighted)
- S_sleep operates on w_op_in/w_op_out (5-dim); S_observer unchanged
- Phase 2 ablation candidate: W_MOD_PROFILES → uniform (α = 0 effectively)
- H1 and falsification structure unchanged by patch

**Depends on:** A4 (theoretical motivation), labyrinth_three_scope_minimal_setup.md
**Required by:** Nothing (terminal)

---

## Superseded Documents

### [superseded] `kht_arw_analysis.md`
First version of the ARW analysis, based on Appendix source only. Superseded
by `kht_arw_analysis_revised.md` (B1). Retain for reference; do not promote
to canonical status in the repo.

---

## Dependency Graph

```
A1 (Layer 1)
 └─── A2 (Layer 2)
       └─── A3 (Layer 3)
             └─── A4 (Layer 4) ─────────────────── D1 (Labyrinth patch)
             └─── B1 (ARW analysis revised)
             └─── B3 (State notation) ──────────── C2 (Partition stability)
                   └─── B4 (Clinical hypotheses)
                   └─── B5 (Group dynamics) ─────── C1 (Aggregation limits)
 └─── B2 (Prescopal substrate)

C1 (Aggregation limits) [standalone entry, feeds B1, B5, C2]
C2 (Partition stability) [feeds B3]

A5 (Architecture index) [navigation; depends on A1–A4]
```

---

## Suggested Repo Placement

| File | Suggested repo path |
|---|---|
| `kht_architecture_layer1.md` | `docs/art_instantiations/kht/` |
| `kht_architecture_layer2.md` | `docs/art_instantiations/kht/` |
| `kht_architecture_layer3.md` | `docs/art_instantiations/kht/` |
| `kht_architecture_layer4.md` | `docs/art_instantiations/kht/` |
| `kht_architecture_index.md` | `docs/art_instantiations/kht/` |
| `kht_arw_analysis_revised.md` | `docs/art_instantiations/kht/` |
| `kht_prescopal_substrate_hypotheses.md` | `docs/notes/kht/` |
| `kht_state_notation.md` | `docs/art_instantiations/kht/` |
| `kht_applications_clinical_cognitive.md` | `docs/art_instantiations/kht/` |
| `kht_group_dynamics.md` | `docs/art_instantiations/kht/` |
| `arw_aggregation_limits_typological_observables.md` | `docs/advanced/` |
| `arw_quantization_partition_stability.md` | `docs/notes/` |
| `labyrinth_patch_op_mod_split.md` | `experiments/labyrinth/` |
| `kht_arw_analysis.md` [superseded] | `docs/archive/` |

---

## Open Questions Spanning Multiple Documents

| ID | Question | Documents involved |
|---|---|---|
| Q-CROSS-1 | What is the complete correspondence table between |O,M,R⟩ compact labels and the 16 standard KHT profiles? Requires derivation of all Ego-block cell assignments. | B3, A2 |
| Q-CROSS-2 | Can Layer 4 simulation outputs serve as synthetic validation data for Hypotheses H-A through H-E? What fidelity is required? | A4, B4 |
| Q-CROSS-3 | Is the Labyrinth experiment's emergent archetype structure (if H1 is confirmed) interpretable as a Layer 2 Dissipation output? What would the mapping look like? | D1, A2 |
| Q-CROSS-4 | The collective κ_c (group coupling threshold for C-R1 formation) is the group-level analog of N* (aggregation crossover). Can they be formally unified into a single parameter? | B5, C1 |
| Q-CROSS-5 | The quantization framework (C2) grounds the KHT state notation (B3). Can the three latency mechanisms (Δ-averaging, ε-blindness, B-inadmissibility) be mapped to specific observational failure modes in the clinical hypotheses (B4)? | C2, B3, B4 |
