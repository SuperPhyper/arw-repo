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
| [docs/advanced/](docs/advanced/README.md) | Emergence, ε in depth, engineering applications |

### Level 3 — Application Domains

| Folder | Domain |
|---|---|
| [docs/context_navigation/](docs/context_navigation/README.md) | Cognitive architecture: modes as reduced scopes |
| [docs/cognitive_architecture/](docs/cognitive_architecture/README.md) | ARW/ART instantiation for context-dependent cognition |
| [docs/bc_taxonomy/](docs/bc_taxonomy/README.md) | BC classes, partition types, BC→partition mapping, distortion metrics |
| [docs/art_instantiations/](docs/art_instantiations/README.md) | Scope template + geopolitical instantiation (Persian Gulf system) |

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
| [docs/notes/open_questions.md](docs/notes/open_questions.md) | 14 open research questions across formalization, empirics, method |
| [docs/notes/](docs/notes/README.md) | Research journal and literature links |

---

## Repository Structure

```
ARW / ART Framework
│
├── docs/                           ← Framework documentation
│   ├── overview/                   ← Start here (15-min intro + operator)
│   ├── glossary/                   ← Canonical vocabulary + atomic definitions
│   ├── core/                       ← Extended framework documents (Level 1–2)
│   ├── advanced/                   ← Emergence, ε, engineering (Level 2+)
│   ├── context_navigation/         ← Cognitive architecture application (Level 3)
│   ├── cognitive_architecture/     ← ARW/ART instantiation for cognition (Level 3)
│   ├── bc_taxonomy/                ← Boundary condition classification (Level 3)
│   ├── art_instantiations/         ← Concrete ART scope examples (Level 3)
│   ├── related_fields/             ← Connections to existing literature
│   ├── notes/                      ← Research journal, open questions
│   ├── pipelines/                  ← Pipeline design stubs (PartitionPipeline, RegimeGraphPipeline)
│   └── figures/                    ← Figure description files (linking to figures/)
│
├── experiments/                    ← ART experimental designs (Level 4)
├── figures/                        ← Diagrams and visualizations (PNG + Mermaid/description sources)
│
├── pipeline/                       ← Python implementation of the partition extraction pipeline
│   ├── validate.py                 ← Structural completeness check
│   ├── sweep.py                    ← BC parameter sweep (Kuramoto kernel implemented)
│   ├── extract_partition.py        ← Observable extraction + ε-regime assignment
│   ├── invariants.py               ← Regime count, adjacency graph, persistence, θ*
│   ├── transfer.py                 ← Cross-scope distortion metrics (RCD, TBS, PCI, SDI)
│   ├── audit_helpers.py            ← A5 failure audit
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
│   ├── CASE-20260311-0001/         ← Kuramoto Phase 1 (end-to-end complete)
│   └── CASE-20260311-0002/         ← Pendulum Phase 1
│
├── data/                           ← Data storage (blobs/)
├── analysis/                       ← Analysis outputs (placeholder)
├── papers/                         ← Paper drafts (placeholder)
├── simulations/                    ← Simulation code (placeholder)
│
├── LICENSE                         ← MIT License
└── README.md                       ← This file
```

---

## Pipeline

The partition extraction pipeline is the computational backbone of the framework.
It implements the full workflow from scope specification to cross-scope transfer analysis.

See [pipeline/README.md](pipeline/README.md) for architecture, CLI reference, and implementation status.

Current state: end-to-end validated on Kuramoto Phase 1 (`CASE-20260311-0001`).
Pendulum kernel is stubbed; consensus, mean-field, and labyrinth are planned.

---

## Research Questions

- Do boundary-condition classes generate characteristic regime partition types?
- Are these partition types transferable across modeling levels (e.g., agent ↔ mean-field)?
- Can transfer failure be quantified using structural distortion metrics?

---

## Status

Active research workspace — concepts, experiments, and documentation evolve over time.
See [docs/overview/limitations_and_open_questions.md](docs/overview/limitations_and_open_questions.md) for current open problems.
See [docs/notes/repo_weakpoints.md](docs/notes/repo_weakpoints.md) for a systematic gap assessment.

---

## License

MIT License
