---
status: note
layer: docs/context_navigation/
---

# Context Navigation

Application of ARW/ART concepts to the context-navigation cognitive architecture.

**Post-audit summary (see `mode_scope_regime_audit.md`):**
Processing modes are **regimes in S_global** — stable partition cells, not independent
scope tuples. Salience is a **fluctuation observable** maximal at Z_shared; it is not
a class-E admissibility-variance signal at zone boundaries. Mode switching is a
**regime transition within S_global**, not a scope transition (scope transitions require
S_global itself to become invalid). Consolidation is an **asymptotic dissipation process**
that tends toward sharper partition boundaries — it is a limit process, not a mechanism
that immediately sharpens them.

---

## Theory — ARW Translation

Documents that translate ARW scope concepts into the agent architecture.

| Document | Purpose |
|---|---|
| [context_navigation_model_spec.md](context_navigation_model_spec.md) | Full architecture specification with ARW mapping |
| [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md) | Admissibility → mode selection; F0/Z(π) for salience observable; scope transition window |
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

## Formal Scope Specification and Transfer

Documents providing the formal ARW scope structure for the labyrinth system.

| Document | Purpose |
|---|---|
| [context_navigation_scope_spec.md](context_navigation_scope_spec.md) | System-level S=(B,Π,Δ,ε) for the labyrinth; zone-level scopes as scope transitions S→S'; observable R(π)/Z(π) for mode_dist and salience_mean |
| [transfer_semantics_context_navigation.md](transfer_semantics_context_navigation.md) | Φ as observable transfer (not system transfer); three transfer experiment types; reporting requirements |

## Connection to Experiments

The context-navigation architecture is operationalized in:

- [experiments/labyrinth_experiment_agenda.md](../../experiments/labyrinth_experiment_agenda.md) — ART scope, hypotheses, distortion metrics
- [experiments/labyrinth_experiment_extended_design.md](../../experiments/labyrinth_experiment_extended_design.md) — zone scopes as explicit BC classes

## Connection to BC Taxonomy

The cognitive mode design is grounded in the BC taxonomy:

- [docs/bc_taxonomy/boundary_condition_classes.md](../bc_taxonomy/boundary_condition_classes.md) — BC class definitions with labyrinth instantiations
- [docs/bc_taxonomy/bc_class_to_regime_type_map.md](../bc_taxonomy/bc_class_to_regime_type_map.md) — which BC class generates which mode type

## Open Questions

Active questions specific to the context-navigation architecture:

| ID | Question | Source |
|---|---|---|
| Q7 | Can scope transitions be detected without ground truth? | open_questions.md |
| Q8 | Does the mode ecology stabilize or keep growing? | open_questions.md |
| Q-CNS-01 | Empirically optimal ε_global for the labyrinth partition? | context_navigation_scope_spec.md |
| Q-CNS-02 | Does salience_mean show Z(π) peak at zone transitions analogous to χ at K_c? | context_navigation_scope_spec.md |
| Q-CNS-03 | Is the consolidation phase necessary for regime stability? (ablation test) | context_navigation_scope_spec.md |
| Q-CNS-04 | Φ for structurally similar vs. dissimilar labyrinths? | context_navigation_scope_spec.md |
| Q-CNS-05 | Do BC classes of zone types produce the mode types predicted by bc_taxonomy_cognitive_modes? | context_navigation_scope_spec.md |
