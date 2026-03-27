---
status: note
layer: docs/cognitive_architecture/
---

# Cognitive Architecture

**Canonical location** for the ARW/ART instantiation of context-dependent cognition.
Documents here treat processing modes as reduced scopes S_mode = (B_mode, Π_mode, Δ_mode, ε_mode),
mode switching as scope transitions, and sleep/consolidation as partition sharpening.

> **Note:** `docs/context_navigation/` also references these documents via redirect stubs.
> The full architecture (agent components, salience, model spec) lives in `docs/context_navigation/`.

---

## Documents

| Document | ARW concept | Purpose |
|---|---|---|
| [context_navigation_ai.md](context_navigation_ai.md) | System integration | How all components connect; ARW mapping summary for the full architecture |
| [modal_cognition.md](modal_cognition.md) | Modes as reduced scopes | Definition of cognitive modes; mode ecology; mode switching as scope transition |
| [anchor_memory.md](anchor_memory.md) | Stored scope-partition associations | Anchor formation, retrieval, decay; stability score; cross-episode transfer |
| [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md) | BC classes → mode types | Design principle: each BC class generates a characteristic cognitive mode type |

## Reading Order

1. [modal_cognition.md](modal_cognition.md) — understand what a mode is in ARW terms
2. [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md) — understand which BC class generates which mode
3. [anchor_memory.md](anchor_memory.md) — understand how the agent stores and retrieves mode assignments
4. [context_navigation_ai.md](context_navigation_ai.md) — see how all components integrate

## Related

- Full architecture spec: [docs/context_navigation/context_navigation_model_spec.md](../context_navigation/context_navigation_model_spec.md)
- Experimental design: [experiments/labyrinth_experiment_agenda.md](../../experiments/labyrinth_experiment_agenda.md)
- BC class definitions: [docs/bc_taxonomy/boundary_condition_classes.md](../bc_taxonomy/boundary_condition_classes.md)
