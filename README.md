# ARW / ART Framework
*A structural framework for analyzing regime partitions under boundary conditions*

Author: Rico Felder

---

## What This Is

The ARW/ART framework studies how **descriptive choices shape the structures that appear stable in a system**.

Rather than asking whether a model is *true*, ARW analyzes:

- which descriptions produce stable regime structures
- when those descriptions lose validity
- how new descriptive regimes emerge

Every scientific description implicitly defines a **scope** S = (B, Π, Δ, ε).
The ARW operator maps a scope to a **regime partition** of the admissible state space:

```
A(S) = R_S
```

Different scopes applied to the same system produce different regime structures.
The framework develops tools to measure when these structures transfer across scopes — and when they distort.

---

## Reading Path

The repository is organized into four levels. Follow this path for a structured introduction.

### Level 0 — Entry Point

Start here regardless of background.

| Document | Purpose |
|---|---|
| [docs/overview/ARW_in_one_page.md](docs/overview/ARW_in_one_page.md) | Complete framework in compact form |
| [docs/overview/arw-operator.md](docs/overview/arw-operator.md) | Formal definition of the ARW operator |

---

### Level 1 — Formal Foundation

The core scope concepts in depth.

| Document | Purpose |
|---|---|
| [docs/glossary/scope.md](docs/glossary/scope.md) | S = (B, Π, Δ, ε) defined |
| [docs/glossary/boundary_conditions.md](docs/glossary/boundary_conditions.md) | B: structural filters on admissible states |
| [docs/glossary/admissibility.md](docs/glossary/admissibility.md) | When a scope remains structurally valid |
| [docs/core/scope_dominance.md](docs/core/scope_dominance.md) | When a scope maintains ordering authority |
| [docs/core/scope_transition.md](docs/core/scope_transition.md) | How and why descriptive regimes shift |
| [docs/core/scope_resolution.md](docs/core/scope_resolution.md) | How ε determines partition granularity |

---

### Level 2 — Conceptual Depth

Extended documents developing the framework's analytical structure.

| Document | Purpose |
|---|---|
| [docs/core/bc_classes_and_regime_generation.md](docs/core/bc_classes_and_regime_generation.md) | How BC classes generate characteristic regime structures |
| [docs/core/regime_stability_regions.md](docs/core/regime_stability_regions.md) | Regimes as robust stability regions |
| [docs/core/basins_as_scope_partitions.md](docs/core/basins_as_scope_partitions.md) | Basins reinterpreted as scope partitions |
| [docs/core/arw_scope_reduction_partition_criterion.md](docs/core/arw_scope_reduction_partition_criterion.md) | Admissible reduction as partition coarsening |
| [docs/advanced/](docs/advanced/README.md) | Emergence, ε in depth, engineering applications |

---

### Level 3 — Application Domains

ARW/ART instantiated in concrete domains.

| Folder | Domain |
|---|---|
| [docs/context_navigation/](docs/context_navigation/README.md) | Cognitive architecture: modes as reduced scopes, anchor memory, mode ecology |
| [docs/bc_taxonomy/](docs/bc_taxonomy/README.md) | Boundary condition taxonomy and distortion metrics |
| [docs/art_instantiations/](docs/art_instantiations/) | Concrete ART scope examples |

---

### Level 4 — Experiments

Concrete ART instantiations and experimental designs.

| Document | Purpose |
|---|---|
| [experiments/kuramoto_oscillators.md](experiments/kuramoto_oscillators.md) | Coupled oscillator calibration system |
| [experiments/multi_link_pendulum.md](experiments/multi_link_pendulum.md) | Pendulum scope reduction |
| [experiments/agent_consensus_models.md](experiments/agent_consensus_models.md) | Consensus / polarization / fragmentation regimes |
| [experiments/aggregation_meanfield.md](experiments/aggregation_meanfield.md) | Agent ↔ mean-field scope comparison |
| [experiments/labyrinth_experiment_agenda.md](experiments/labyrinth_experiment_agenda.md) | Context-navigation agent experiment |
| [experiments/labyrinth_experiment_extended_design.md](experiments/labyrinth_experiment_extended_design.md) | Extended regime-forcing environment |

---

### Reference (consult anytime)

| Resource | Purpose |
|---|---|
| [docs/glossary/](docs/glossary/README.md) | All atomic concept definitions |
| [docs/glossary/glossary_map.md](docs/glossary/glossary_map.md) | Visual map of concept relationships |
| [docs/related_fields/](docs/related_fields/related_fields_and_methodological_connections.md) | Connections to physics, AI, philosophy, cognitive science |
| [docs/overview/novelty_and_projected_value.md](docs/overview/novelty_and_projected_value.md) | What makes ARW distinctive |
| [docs/overview/limitations_and_open_questions.md](docs/overview/limitations_and_open_questions.md) | Honest assessment of open problems |
| [docs/overview/roadmap.md](docs/overview/roadmap.md) | Research phases and planned development |
| [docs/notes/](docs/notes/) | Research journal and open questions |

---

## Repository Structure

```
ARW / ART Framework
│
├── docs/
│   ├── overview/               ← Start here (Level 0)
│   ├── glossary/               ← Atomic definitions (reference)
│   ├── core/                   ← Extended framework documents (Level 1–2)
│   ├── advanced/               ← Emergence, ε, engineering (Level 2+)
│   ├── context_navigation/     ← Cognitive architecture, theory + components (Level 3)
│   ├── bc_taxonomy/            ← Boundary condition classification (Level 3)
│   ├── art_instantiations/     ← Concrete ART scope examples (Level 3)
│   ├── related_fields/         ← Connections to existing literature
│   └── notes/                  ← Research journal, open questions
│
├── experiments/                ← ART experimental designs (Level 4)
├── figures/                    ← Diagrams and visualizations
└── README.md                   ← This file
```

---

## Research Questions

- Do boundary-condition classes generate characteristic regime partition types?
- Are these partition types transferable across modeling levels (e.g., agent ↔ mean-field)?
- Can transfer failure be quantified using structural distortion metrics?

---

## Status

Active research workspace. Concepts, experiments, and documentation evolve over time.

---

## License

MIT License
