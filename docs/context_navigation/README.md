---
status: note
layer: docs/context_navigation/
---

# Context Navigation

Application of ARW/ART concepts to the context-navigation cognitive architecture.

Processing modes are reduced scopes S_mode = (B_mode, Π_mode, Δ_mode, ε_mode).
Salience is the admissibility-loss signal at scope boundaries.
Mode switching is the operational form of scope transition.
Sleep / consolidation sharpens regime partition boundaries.

---

## Theory — ARW Translation

Documents that translate ARW scope concepts into the agent architecture.

| Document | Purpose |
|---|---|
| [context_navigation_model_spec.md](context_navigation_model_spec.md) | Full architecture specification with ARW mapping |
| [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md) | Admissibility → mode selection; when a mode becomes active |
| [salience_mode_ecology.md](salience_mode_ecology.md) | Salience as scope-competition / admissibility-loss signal |
| [modal_cognition.md](modal_cognition.md) | Modes as reduced scopes; mode identity via partition membership |
| [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md) | BC classes → cognitive mode types; design principle for mode ecology |
| [boundary_conditions_as_resonance_filters.md](boundary_conditions_as_resonance_filters.md) | BCs as resonance filters in the architecture |
| [resonance_dialectic_context_navigation.md](resonance_dialectic_context_navigation.md) | Resonance and context navigation |

## Architecture — Components

Documents describing the concrete architectural components and their ARW roles.

| Document | ARW role | Purpose |
|---|---|---|
| [agent_architecture_mode_ecology.md](agent_architecture_mode_ecology.md) | Full architecture | Mode ecology structure and component interactions |
| [anchor_memory.md](anchor_memory.md) | Stored scope-partition associations | Formation, retrieval, decay, cross-maze transfer |
| [context_navigation_ai.md](context_navigation_ai.md) | System integration | How components connect; ARW mapping summary |
| [context_navigation_architecture_notes.md](context_navigation_architecture_notes.md) | Working notes | Mode optimization and consolidation details |

## Connection to Experiments

The context-navigation architecture is operationalized in:

- [experiments/labyrinth_experiment_agenda.md](../../experiments/labyrinth_experiment_agenda.md) — ART scope, hypotheses, distortion metrics
- [experiments/labyrinth_experiment_extended_design.md](../../experiments/labyrinth_experiment_extended_design.md) — zone scopes as explicit BC classes

## Connection to BC Taxonomy

The cognitive mode design is grounded in the BC taxonomy:

- [docs/bc_taxonomy/boundary_condition_classes.md](../bc_taxonomy/boundary_condition_classes.md) — BC class definitions with labyrinth instantiations
- [docs/bc_taxonomy/bc_class_to_regime_type_map.md](../bc_taxonomy/bc_class_to_regime_type_map.md) — which BC class generates which mode type
