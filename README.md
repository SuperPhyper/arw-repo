# ARW / ART Framework

*A structural framework for analyzing regime partitions under boundary conditions*

Author: Rico Felder

---

## At a Glance

**What problem does this solve?**
Complex systems are described differently at different levels — agent vs. mean-field, microscopic vs. macroscopic, detailed vs. coarse. There is no systematic way to ask: *when does a simpler description remain faithful to the original, and when does it silently destroy structural information?* ARW provides that methodology.

**What is ARW in one sentence?**
ARW (Allgemeine Regime-Wissenschaft) is a formal framework that maps descriptive choices — observables, boundary conditions, resolution — to regime partitions, and analyzes when those partitions transfer or distort across modeling levels.

**What is ART in one sentence?**
ART (Allgemeine Regime-Theorie) is the application layer: it instantiates ARW by specifying concrete scopes for real systems, enabling experiments and measurements.

**What can a new reader cover in 15 minutes?**
→ [docs/overview/ARW_in_one_page.md](docs/overview/ARW_in_one_page.md) — the complete framework compactly
→ [docs/overview/minimal_example.md](docs/overview/minimal_example.md) — a concrete walkthrough with a two-link pendulum

---

## Core Concept

Every description of a system implicitly defines a **scope**:

```
S = (B, Π, Δ, ε)
```

| Symbol | Meaning |
|---|---|
| B | boundary constraints — which states are admissible |
| Π | observables — what is being measured |
| Δ | admissible perturbations — robustness conditions |
| ε | resolution threshold — smallest distinguishable difference |

The **ARW operator** maps a scope to a regime partition of the admissible state space:

```
A(S) = R_S
```

Different scopes produce different regime structures. The framework develops tools to measure when these structures transfer across scopes — and when they distort.

---

## Theorem H2' — IVA Dimensionality Principle

*(see [docs/advanced/h2_prime_theorem.md](docs/advanced/h2_prime_theorem.md) — second revised draft, 2026-03-28)*

The most structurally important recent result in the framework:

> **dim_eff(Z(π)) = rank(IVA_ext(π))**

The **effective dimension of an observable's exclusion zone** in parameter space equals the **rank of its extended independent violation axes** — the number of linearly independent directions along which the observable's pre-scopal substrate fails.

This is not a heuristic. It is a proved theorem (Regular Value Theorem + Rank Theorem, with generic transversality established by Lemma G; Sard's theorem ensures measure-zero exceptions are negligible). It means the *geometry* of where an observable breaks down is structurally determined by the observable's construction, not by the system.

**Why this matters:**

Before Theorem H2', the exclusion zone Z(π) was defined but its geometry was left open. Could a Coupling-BC observable fail along a 2D surface in parameter space? A 1D curve? A fractal? The theorem answers this via the BC class alone:

| BC class | rank(IVA_ext) | Shape of Z(π) |
|---|---|---|
| Coupling | 0 | Isolated point (κ_c) — failure is a scope singularity, not a region |
| Symmetry Breaking | ≥ 1 | At least a half-line or surface |
| k independent BCs | k | k-dimensional manifold |

**Empirical validation across three cases:**

| Case | System | dim_eff | Z(π) shape | Outcome |
|---|---|---|---|---|
| CASE-0001 | Kuramoto | 0 | point at κ_c ≈ 1.49 | θ* = 1.475 is a scope singularity, not a regime boundary ✓ |
| CASE-0008 | Pitchfork normal form | 1 | half-line along μ ≥ 0 | Exclusion zone is a ray in μ-space ✓ |
| CASE-0010 | German School System | 2 | 2D surface in joint BC space | Two independent failure axes confirmed ✓ |

**Corollary C4 (Observable Class Necessity):** Two observables with different rank(IVA_ext) cannot be substituted within the same scope — they belong to structurally distinct observable classes. This makes observable selection principled rather than ad hoc, and connects directly to the F0 falsification category.

---

## Reading Path

### 15-Minute Introduction

| Document | Purpose |
|---|---|
| [docs/overview/ARW_in_one_page.md](docs/overview/ARW_in_one_page.md) | Complete framework in compact form |
| [docs/overview/minimal_example.md](docs/overview/minimal_example.md) | Concrete walkthrough: pendulum, scope, partition, transition |

### Level 1 — Formal Foundation

| Document | Purpose |
|---|---|
| [docs/overview/arw-operator.md](docs/overview/arw-operator.md) | Formal definition of the ARW operator |
| [docs/glossary/scope.md](docs/glossary/scope.md) | S = (B, Π, Δ, ε) in full detail |
| [docs/glossary/boundary_conditions.md](docs/glossary/boundary_conditions.md) | B: structural filters on admissible states |
| [docs/glossary/admissibility.md](docs/glossary/admissibility.md) | When a scope remains structurally valid |
| [docs/core/scope_dominance.md](docs/core/scope_dominance.md) | When a scope maintains ordering authority |
| [docs/core/scope_transition.md](docs/core/scope_transition.md) | How and why descriptive regimes shift |
| [docs/core/scope_resolution.md](docs/core/scope_resolution.md) | How ε determines partition granularity |

### Level 2 — Conceptual Depth

| Document | Purpose |
|---|---|
| [docs/core/bc_classes_and_regime_generation.md](docs/core/bc_classes_and_regime_generation.md) | How BC classes generate characteristic regime structures |
| [docs/core/regime_stability_regions.md](docs/core/regime_stability_regions.md) | Regimes as robust stability regions |
| [docs/core/basins_as_scope_partitions.md](docs/core/basins_as_scope_partitions.md) | Basins reinterpreted as scope partitions |
| [docs/core/arw_scope_reduction_partition_criterion.md](docs/core/arw_scope_reduction_partition_criterion.md) | Admissible reduction as partition coarsening |
| [docs/advanced/epsilon_and_scope_resolution.md](docs/advanced/epsilon_and_scope_resolution.md) | ε in depth: admissible ε-interval, ε-sweep, multi-observable ε, I_ε(κ) robustness |
| [docs/advanced/scope_completeness.md](docs/advanced/scope_completeness.md) | Observable agreement as scope completeness diagnostic; latent degrees of freedom |
| [docs/advanced/observable_decomposition.md](docs/advanced/observable_decomposition.md) | Observables as compositions of basis operators; pre-scopal substrate; R(π) and Z(π) |
| [docs/glossary/observable_range.md](docs/glossary/observable_range.md) | Observable range R(π), exclusion zone Z(π), F0 falsification category |
| [docs/advanced/h2_prime_theorem.md](docs/advanced/h2_prime_theorem.md) | **Theorem H2' — IVA Dimensionality Principle:** dim_eff(Z(π)) = rank(IVA_ext(π)); proved, validated on 3 cases |
| [docs/advanced/](docs/advanced/README.md) | Emergence, engineering applications, cover height |

### Level 3 — Application Domains

| Folder | Domain |
|---|---|
| [docs/context_navigation/](docs/context_navigation/README.md) | Cognitive architecture: modes as reduced scopes |
| [docs/cognitive_architecture/](docs/cognitive_architecture/README.md) | ARW/ART instantiation for context-dependent cognition |
| [docs/bc_taxonomy/](docs/bc_taxonomy/README.md) | BC classes, partition types, BC→partition mapping, distortion metrics |
| [docs/art_instantiations/](docs/art_instantiations/README.md) | Scope template + domain instantiations (geopolitical, ecology, ML, neuroscience, social systems) |

### Level 4 — Experiments

| Document | Purpose |
|---|---|
| [experiments/kuramoto_oscillators.md](experiments/kuramoto_oscillators.md) | Coupled oscillator calibration system |
| [experiments/multi_link_pendulum.md](experiments/multi_link_pendulum.md) | Pendulum scope reduction |
| [experiments/agent_consensus_models.md](experiments/agent_consensus_models.md) | Consensus / polarization / fragmentation regimes |
| [experiments/aggregation_meanfield.md](experiments/aggregation_meanfield.md) | Agent ↔ mean-field scope comparison |
| [experiments/labyrinth_experiment_agenda.md](experiments/labyrinth_experiment_agenda.md) | Context-navigation agent experiment |
| [experiments/labyrinth_experiment_extended_design.md](experiments/labyrinth_experiment_extended_design.md) | Extended regime-forcing environment |

### Reference

| Resource | Purpose |
|---|---|
| [docs/glossary/canonical_vocabulary.md](docs/glossary/canonical_vocabulary.md) | Term definitions with adjacent-field distinctions |
| [docs/glossary/](docs/glossary/README.md) | All atomic concept definitions |
| [docs/glossary/glossary_map.md](docs/glossary/glossary_map.md) | Visual map of concept relationships |
| [docs/related_fields/](docs/related_fields/README.md) | Connections to dynamical systems, RL, philosophy, cognitive science |
| [docs/overview/novelty_and_projected_value.md](docs/overview/novelty_and_projected_value.md) | What makes ARW distinctive |
| [docs/overview/limitations_and_open_questions.md](docs/overview/limitations_and_open_questions.md) | Honest assessment of open problems |
| [docs/overview/roadmap.md](docs/overview/roadmap.md) | Research phases and planned development |
| [docs/notes/open_questions.md](docs/notes/open_questions.md) | Open research questions (Q1–Q16 + Q_NEW_1–18) |
| [docs/notes/research_journal.md](docs/notes/research_journal.md) | Research journal (sessions 2026-03-12 through 2026-03-28) |
| [docs/meta/DOC_INDEX.md](docs/meta/DOC_INDEX.md) | Anti-pile-up spine: canonical ownership of all conceptual docs |
| [docs/INDEX.md](docs/INDEX.md) | Human-facing searchable index of all documentation |

---

## Repository Structure

```
ARW / ART Framework
│
├── docs/                           ← Framework documentation
│   ├── overview/                   ← Start here (15-min intro + operator)
│   ├── glossary/                   ← Canonical vocabulary + atomic definitions
│   ├── core/                       ← Extended framework documents (Level 1–2)
│   ├── advanced/                   ← Emergence, ε, observable decomposition, cover height (Level 2+)
│   ├── context_navigation/         ← Cognitive architecture application (Level 3)
│   ├── cognitive_architecture/     ← ARW/ART instantiation for cognition (Level 3)
│   ├── bc_taxonomy/                ← Boundary condition classification (Level 3)
│   ├── art_instantiations/         ← Concrete ART scope examples (Level 3)
│   ├── related_fields/             ← Connections to existing literature
│   ├── notes/                      ← Research journal, open questions, weakpoints
│   ├── meta/                       ← DOC_INDEX, LLM charter, maintenance checklist
│   ├── pipelines/                  ← Pipeline design stubs (PartitionPipeline, RegimeGraphPipeline)
│   └── figures/                    ← Figure description files (linking to figures/)
│
├── experiments/                    ← ART experimental designs (Level 4)
├── figures/                        ← Diagrams and visualizations (57 files: PNG + Mermaid sources)
│
├── pipeline/                       ← Python implementation of the partition extraction pipeline
│   ├── validate.py                 ← Structural completeness check
│   ├── sweep.py                    ← BC parameter sweep
│   ├── epsilon_sweep.py            ← ε → N regime count sweep
│   ├── epsilon_kappa_map.py        ← 2D (κ, ε) robustness map
│   ├── epsilon_multi_observable.py ← Per-observable ε agreement analysis
│   ├── extract_partition.py        ← Observable extraction + ε-regime assignment
│   ├── invariants.py               ← Regime count, adjacency graph, persistence, θ*, sweep_range
│   ├── transfer.py                 ← Cross-scope distortion metrics (RCD, TBS_norm, PCI, SDI, Φ)
│   ├── audit.py                    ← Failure audit runner
│   ├── audit_helpers.py            ← A5 failure audit helpers
│   └── new_case.py                 ← Case scaffolding generator
│
├── schemas/                        ← YAML/JSON schemas for pipeline artifacts
│   ├── ScopeSpec.yaml              ← ART scope instantiation schema
│   ├── BCManifest.yaml             ← BC classification + sweep program schema
│   ├── CaseRecord.yaml             ← Case envelope schema
│   ├── RegimeGraph.schema.json     ← Regime transition graph schema
│   └── TransitionTrials.schema.json
│
├── cases/                          ← One directory per experiment instance
│   │
│   ├── ── Active (pipeline run) ──
│   ├── CASE-20260311-0001/         ← Kuramoto κ-sweep [Coupling] (go_nogo: pending / F1 + Z(r_ss) at κ_c)
│   ├── CASE-20260311-0002/         ← Multi-Link-Pendel κ-sweep [Coupling] (go_nogo: go)
│   ├── CASE-20260311-0003/         ← Doppelpendel E-sweep [Restriction] (go_nogo: go)
│   ├── CASE-20260318-0004/         ← Coupled Stuart-Landau K-sweep [Coupling] (in_progress; first emergence case)
│   │
│   ├── ── Pending (signature-first, pipeline not yet run) ──
│   ├── CASE-20260315-0005/         ← Multi-Pendel + damping γ-sweep [Dissipation]
│   ├── CASE-20260315-0006/         ← Multi-Pendel + forcing Ω-sweep [Forcing]
│   ├── CASE-20260315-0007/         ← SIR epidemic model β-sweep [Aggregation]
│   ├── CASE-20260315-0008/         ← Pitchfork normal form μ-sweep [Symmetry Breaking]
│   ├── CASE-20260315-0009/         ← Stochastic Kuramoto σ-sweep [Coupling + Noise]
│   ├── CASE-20260315-SOC1/         ← Shame interaction regime [Restriction (social)]
│   └── CASE-20260328-0010/         ← German School System [Coupling + Restriction + Forcing + Dissipation]
│                                     (first multi-BC-class case; ScopeSpec.yaml present)
│
├── Simulationen/                   ← Extended simulation and analysis scripts (cover height, 2D BC sweeps)
│   ├── kuramoto_2d_sweep.py        ← 2D (κ, σ) BC sweep (1120 points)
│   ├── sweep_2d_all_cases.py       ← RK4 2D sweeps for CASE-0002/0003/0004
│   ├── cover_observable_space.py   ← Observable-space interval cover computation
│   ├── cover_multi_case.py         ← Cross-case cover height analysis (CASE-0001–0004)
│   └── cover_2d_all_cases.py       ← 2D cover height analysis and visualization
│
├── data/                           ← Data storage (blobs/)
├── analysis/                       ← Analysis outputs (placeholder)
├── papers/                         ← Paper drafts (placeholder)
├── simulations/                    ← Simulation code (placeholder; kernels in pipeline/sweep.py)
│
├── archive/                        ← Superseded/completed artifacts (read-only)
│   ├── sessions/                   ← Session working docs (merged into canonical files)
│   └── transfers/                  ← Completed transfer analysis index
│
├── LICENSE                         ← MIT License
└── README.md                       ← This file
```

---

## Pipeline

The partition extraction pipeline is the computational backbone of the framework.
It implements the full workflow from scope specification to cross-scope transfer analysis.

See [pipeline/README.md](pipeline/README.md) for architecture, CLI reference, and implementation status.

Current state: end-to-end validated on Kuramoto (`CASE-20260311-0001`) and
classical double pendulum (`CASE-20260311-0003`). Includes ε-sweep,
2D (κ, ε) robustness mapping, per-observable ε-analysis, and failure audit.

---

## Empirical Results

### ε-Analysis and Scope Resolution
*(see [docs/advanced/epsilon_and_scope_resolution.md](docs/advanced/epsilon_and_scope_resolution.md))*

- **Admissible ε-interval:** The partition structure is stable across a range of ε values (plateaus). The ε-sweep identifies these plateaus empirically, replacing the need to guess ε.
- **Scope fragility at phase transitions:** The admissible ε-interval narrows where the system changes fastest (Kuramoto: r = −0.77 correlation between plateau width and observable gradient). See [figures/epsilon_kappa_robustness.png](figures/epsilon_kappa_robustness.png).
- **Multi-observable scopes need per-observable ε:** On the double pendulum, λ_proxy and Var_rel agree on the regime count at only 28% of ε-values. A single shared ε is insufficient. See [figures/multi_observable_agreement.png](figures/multi_observable_agreement.png).
- **Observable agreement as scope completeness diagnostic:** Where observables disagree, latent degrees of freedom are active. See [docs/advanced/scope_completeness.md](docs/advanced/scope_completeness.md).

### Observable Decomposition and Pre-Scopal Structure
*(Session 2026-03-18; see [docs/advanced/observable_decomposition.md](docs/advanced/observable_decomposition.md))*

- **Observables carry pre-scopal substrates:** Every non-trivial observable π is a composition of basis operations (Restriction, Aggregation, Symmetry, Discretization, Approximation). For r_ss, ~25 assumptions span levels A0–A6; only one is a scope decision.
- **Observable range R(π) and exclusion zone Z(π):** Each observable is structurally valid only in R(π) ⊆ B. When B overlaps Z(π) (the exclusion zone), the observable fails not from insufficient span (F1) but from structural substrate failure (F0). See [docs/glossary/observable_range.md](docs/glossary/observable_range.md).
- **θ* in CASE-0001 is a scope transition, not a regime boundary:** κ_c lies in Z(r_ss), where five substrate assumptions fail simultaneously. CASE-0001 documents a scope transition; a new observable (e.g. χ = ∂r_ss/∂κ) is needed to resolve the partition at κ_c (Q_NEW_12).
- **Φ measures observable transfer, not system transfer:** Φ = f(S_A, S_B), not f(System_A, System_B). Two physically identical systems with different observables may show low Φ.
- **lambda_proxy is structurally insufficient by construction:** Assumptions A6.1 and A6.2 (finite T, finite δθ(0)) are violated by definition, explaining the empirical insufficiency in CASE-0002/0003 from first principles.

### First Empirical Emergence Case (CASE-0004)
*(see [docs/advanced/arw_emergence_bc_relative.md](docs/advanced/arw_emergence_bc_relative.md))*

- **Coupled Stuart-Landau oscillators** provide the first empirical ARW emergence case.
- **Emergence window:** ε ∈ [0.082, 0.805], width = 0.723. Local observable (amp_asym) collapses before relational observable (PLV) — the local precursor preceding the relational transition is now documented.
- **Lambda-robustness:** Δ-stable for λ ∈ [0.4, 1.3]; breaks at λ > 1.3 for weak K.

### Observable-Space Cover Height
*(Sessions 2026-03-27/28; see [docs/advanced/observable_space_cover_height.md](docs/advanced/observable_space_cover_height.md))*

- **Cover height as ε-marginalisation:** Instead of committing to a single ε, the observable-space cover height h integrates partition structure across all ε-scales simultaneously. For the Kuramoto 2D sweep (1120 points), this yields 57% dynamic range across BC space.
- **Cover height maps regime depth, not identity:** High h → interior of a flat regime (many BC points produce nearly identical observable values); low h → transition zone (each point isolated in observable space). Height contours run parallel to the regime boundary.
- **Profile shape discriminates observable failure type:** Smooth/monotone → sufficient or gradual transition; jagged/non-monotone → F0 structural failure (noisy observable); flat → F1 span failure. CASE-0004 (PLV vs. amp_asym: 136% DR vs. 14% DR, 10× ratio) provides the cleanest discrimination.
- **2D BC sweeps reveal BC interaction structure:** In CASE-0002 (κ × γ), cover-height contours are diagonal in (κ, γ) space — the regime boundary is a joint function of both BCs, invisible in either 1D sweep. This implies Δ must permit joint BC conditions (Q_NEW_18). See [figures/cover2d_0002_varrel_overlay.png](figures/cover2d_0002_varrel_overlay.png).
- **DR alone is not a reliable sufficiency indicator:** In CASE-0002/0003, the insufficient observable (lambda_proxy) has higher DR than the sufficient one (var_rel). DR must be combined with profile shape analysis.

---

## Research Questions

### Formalization
- **Q1** — Can admissibility be quantified as a continuous measure rather than a binary condition?
- **Q2** — Should ε be state-dependent? What is the consistent formulation near regime boundaries?
- **Q3** — When Π = {π₁, π₂, ...}, what is the joint admissibility condition? Is ε a vector, matrix, or function on product space? *(Empirically motivated by CASE-0003: only 37% ε-agreement between observables.)*
- **Q_NEW_1** — Does the topological/algebraic structure of X belong to B, an independent meta-layer, or the ART layer?
- **Q_NEW_2** — Should F0 (R(π) ∩ B ≠ B) be a required entry in ScopeSpec.yaml? *(Open; F0 is defined in the glossary but not yet in the schema.)*

### Empirical
- **Q5** — Do BC classes generate partition types universally? *(First positive data: Coupling BC produces sequential partitions in Kuramoto and Multi-Link-Pendel. Unexpected: Coupling and Restriction produce topologically equivalent sequential partitions at matched ε — BC-class signal appears in transition position and sharpness, not in topology.)*
- **Q_NEW_12** — Does χ = ∂r_ss/∂κ (diverges at κ_c rather than collapsing) yield a different partition for CASE-0001? *(High priority; first candidate of a fluctuation-observable class.)*
- **Q_NEW_11** — Can Φ be decomposed into Φ_obs × Φ_sys? *(Requires a new scope on the same system with a different observable.)*
- **Q_NEW_13** — Do cover-height maxima in BC space correspond systematically to stable ε-plateaus in N(ε)? *(Directly testable against CASE-0001.)*
- **Q_NEW_18** — Do non-axis-aligned regime boundaries (CASE-0002 2D sweep) require extending Δ to permit joint BC conditions?

### Conceptual
- **Q9** — Are scope transitions and phase transitions formally related? Under what conditions do they coincide?
- **Q10** — Is emergence in ARW ontological or epistemic? Where is the boundary between "the description changes" and "something new comes into existence"?
- **Q_NEW_9** — Is BC class a property of the system or of the scope? *(Foundational for BC taxonomy; would require BCManifest to carry separate system_bc and observable_bc fields.)*
- **Q_NEW_10** — Does ARW need formal definitions distinguishing θ* (regime boundary within R(π)) from a scope transition at Z(π)?

### Methodological
- **Q12** — Is there a principled procedure for deriving ε from data, consistent with the ε–Δ consistency condition?
- **Q13** — What is the general pipeline for partition extraction from trajectory data without known equations of motion?
- **Q_NEW_16** — Can profile shape smoothness (total variation, autocorrelation along BC axis) serve as an automated pre-screening step for observable selection?
- **Q_NEW_17** — Is there a formal relationship between cover-height dynamic range and observable span/ε?

See [docs/notes/open_questions.md](docs/notes/open_questions.md) for the complete list (Q1–Q16 + Q_NEW_1–18).

---

## Status

Active research workspace — concepts, experiments, and documentation evolve over time.

**Active cases:** CASE-0001 (go_nogo: pending — PATH B preferred: F0 closure at κ_c; CASE-0001-ext with χ=∂r_ss/∂κ planned), CASE-0002 (go), CASE-0003 (go), CASE-0004 (go — first empirical emergence case; Φ=0.9 transfer to CASE-0001 confirmed 2026-03-29).

**Pending cases:** CASE-0005 through CASE-0009, SOC1, CASE-0010 (German School System — first multi-BC-class case) — all have pre-pipeline artifacts; none have been run through the pipeline yet.

**Next priorities:** (1) Create CASE-0001-ext with χ=∂r_ss/∂κ as primary observable and run pipeline (closes CASE-0001 F0 formally). (2) Integrate `Simulationen/` cover height scripts into pipeline infrastructure as a first-class module. (3) Run pipeline on CASE-0005 (most complete pending case: Dissipation BC).

See [docs/overview/limitations_and_open_questions.md](docs/overview/limitations_and_open_questions.md) for current open problems.
See [docs/notes/repo_weakpoints.md](docs/notes/repo_weakpoints.md) for a systematic gap assessment (last reviewed: 2026-03-29).
See [docs/notes/research_journal.md](docs/notes/research_journal.md) for session-by-session findings.

---

## License

MIT License
