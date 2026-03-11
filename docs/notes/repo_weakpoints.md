---
status: draft
---

# Repository Weak Points — Systematic Assessment

This document identifies underdeveloped entries, structural gaps,
and missing components across the repository.
Entries are ordered by priority: how much analytical damage the gap causes
and how tractable it is to fill.

---

## Category 1 — Critical Placeholders (Stubs with No Content)

These files are referenced from multiple other documents but contain
almost nothing. They are the highest-priority gaps.

### `docs/bc_taxonomy/boundary_condition_classes.md`

Current state: 6-item list (restriction, coupling, symmetry breaking,
dissipation, forcing, aggregation). No definitions, no examples,
no regime consequences for any class.

What is missing:
- Formal definition of each BC class
- The characteristic regime structure each class generates
- Concrete instantiation in at least two systems per class
  (e.g., coupling BC in Kuramoto and in opinion dynamics)
- Relationship between BC classes: can they combine? Do some dominate?

Why this matters: the entire research program's central hypothesis is
"BC classes generate characteristic regime partition structures".
Without defined classes, this hypothesis is untestable.

---

### `docs/bc_taxonomy/partition_types.md`

Current state: 3-item list. No definitions.

What is missing:
- Formal typology: what distinguishes binary from multi-stable from clustered?
- Mapping from BC classes to partition types (the core claim of the taxonomy)
- Stability properties of each partition type
- Whether partition types are universal or system-dependent

Why this matters: the cross-experiment comparison (Kuramoto, pendulum,
consensus models) depends on comparing partition types. Without a typology,
there is nothing to compare.

---

### `docs/bc_taxonomy/transfer_distortion_metrics.md`

Current state: 4-item list. No definitions.

What is missing: The metrics are already fully defined in
`experiments/aggregation_meanfield.md` (TBS, RCD, PCI, SDI).
This file should consolidate them formally, add the mathematical
definitions, and specify how each metric behaves under different
distortion regimes.

Why this matters: this is the canonical reference for the metrics.
Currently, the definitions live only in an experiment file.

---

### `docs/context_navigation/anchor_memory.md`

Current state: 1 sentence.

What is missing:
- Formal definition: what is an anchor? (context_embedding, mode, outcome_statistics, stability_score)
- Formation: when does an anchor form? (stability threshold after consolidation)
- Retrieval: what triggers retrieval? (context similarity above threshold)
- Decay: do anchors expire? Under what conditions?
- Relationship to ARW partition: anchors are stored scope-partition associations —
  this connection should be explicit

---

### `docs/context_navigation/modal_cognition.md`
### `docs/context_navigation/bc_taxonomy_cognitive_modes.md`

Current state: 1 sentence each.

These two files are closely related and could be merged or made
complementary. Both gesture at the same claim: cognitive processing modes
correspond to reduced scopes (different Π_B). Neither develops it.

What is missing for `modal_cognition.md`:
- How does a "mode" formally instantiate a scope S_mode = (B_mode, Π_mode, Δ_mode, ε_mode)?
- What makes two behavioral trajectories belong to the same mode?
- How is mode identity preserved across episodes?

What is missing for `bc_taxonomy_cognitive_modes.md`:
- The mapping from BC classes (restriction, coupling, etc.) to cognitive mode types
- Concrete correspondence table: which BC class generates which mode?
- Whether this mapping is unique or many-to-many

---

### `docs/context_navigation/context_navigation_ai.md`

Current state: 4-item list.

What is missing: the architecture already exists in detail in
`context_navigation_architecture_notes.md` and
`agent_architecture_mode_ecology.md`.
This file should be a concise integration document — not a new design,
but a clear statement of how the architecture pieces connect to each other
and to ARW concepts. A single-page map of the system.

---

### `docs/notes/open_questions.md`
### `docs/notes/research_journal.md`
### `docs/notes/literature_links.md`

All three are empty. These signal scientific immaturity to external readers.

`open_questions.md` in particular is important — a well-written list of
genuinely open questions signals that the framework knows its own limits.
The content already exists scattered across `limitations_and_open_questions.md`
and the falsification sections of experiment files — it just needs to be
extracted and sharpened.

---

## Category 2 — Underdeveloped Documents with Existing Content

These files have a structure but are missing the analytical core.

### `docs/advanced/epsilon_and_scope_resolution.md` and `epsilon_resolution_window_arw.md`

Current state: both documents circle the same question (what is ε?)
without resolving it. There is significant conceptual overlap.

Problem: ε is the least formally developed component of S = (B, Π, Δ, ε).
In the experiment files, ε appears as a concrete number (0.05 rad, cosine distance < 0.1).
In the theory files, it remains a "resolution threshold" without formal treatment.

What is missing:
- When is ε a scalar? When is it a function of state? When is it a metric?
- How does ε interact with Δ? (A perturbation that is within Δ but crosses ε
  produces a regime change — this is a critical interaction that is not documented)
- How is ε estimated empirically? (For the labyrinth, it is a hyperparameter —
  but how should it be chosen?)
- The two files should be merged and resolved, not left as parallel fragments.

---

### `docs/core/basins_as_scope_partitions.md`

Current state: 64 lines, correct direction, but stops before making
the key analytical move.

What is missing:
- The formal statement: under what conditions is a dynamical basin
  identical to an ARW regime class?
- The condition under which they diverge: when does a basin
  exist in the dynamics but not appear in the regime partition under S?
  (Answer: when the basin-distinguishing observable is below ε, or
  outside Π — this is the crucial ARW contribution to basin theory)
- Connection to the Kuramoto experiment: the order parameter r
  is not itself a basin indicator, but it induces a regime partition
  that *correlates* with the basin structure. When does this correlation fail?

---

### `docs/overview/roadmap.md`

Current state: high-level phase list without timelines, milestones,
or decision points.

What is missing:
- What constitutes "done" for each phase? (Phase 1 is done when what?)
- What are the go/no-go decisions between phases?
- How do the calibration results (Kuramoto, pendulum) gate Phase 2?
- The OSV fellowship timeline exists in the 1-pager but is not connected here.

---

## Category 3 — Structural Gaps (Missing Files That Are Referenced)

These are documents that other files link to or logically require,
but that do not yet exist.

### `docs/bc_taxonomy/bc_class_to_regime_type_map.md` (does not exist)

`bc_classes_and_regime_generation.md` in `docs/core/` describes the relationship
between BC classes and regime structures in prose.
The bc_taxonomy folder should contain a formal mapping table:

```
BC class       →   characteristic partition type   →   example systems
coupling       →   synchronization regimes          →   Kuramoto, pendulum R_P4
restriction    →   bounded-state regimes            →   opinion dynamics, BC-constrained agents
symmetry-break →   bifurcated partitions            →   polarization in R_Op2
dissipation    →   contracted state space           →   damped oscillators, energy-bounded systems
forcing        →   driven multi-stability           →   pendulum with driving Ω
aggregation    →   mean-field collapse              →   S_MF in all mean-field scopes
```

---

### `docs/glossary/scope_transition.md` (does not exist as glossary entry)

`scope_transition.md` exists in `docs/core/` as a full document.
There is no glossary-level atomic definition — a 10-line entry
with the formal definition and links to the core document.
This breaks the glossary's role as the canonical first reference.

Same issue for: `scope_dominance`, `regime_partition`, `admissible_reduction`.
These are central ARW terms with full core documents but no glossary entries.

---

### `docs/art_instantiations/art_labyrinth_scope.md` (does not exist)

The labyrinth has a full ART instantiation in `experiments/`.
The `docs/art_instantiations/` folder should contain a condensed
scope-tuple summary for each ART instantiation — not the full experiment
design, but the formal S = (B, Π, Δ, ε) specification as a reference card.

Currently only the geopolitical scope has a file in `art_instantiations/`.
The physical and agent scopes are only in `experiments/`.

---

## Category 4 — Content That Exists But Lacks Formal Sharpness

These documents have good content but contain passages that should
be made more precise.

### `docs/context_navigation/resonance_dialectic_context_navigation.md`

216 lines, but uses "resonance" in a largely informal sense without
connecting it to the formal definition in `docs/glossary/resonance.md`.
The document would gain significantly from making explicit when
"resonance" is used informally (as a metaphor) versus formally
(as coherent coupling under compatible BCs).

### `docs/advanced/emergence_overview.md`

206 lines, good coverage. Missing: a formal statement of the ARW
emergence condition. Currently: "emergence occurs when a scope loses
admissibility." This should be stated as: "emergence is a scope transition
S → S' such that R_S' ⊄ R_S — the new partition is not a coarsening
of the old one, but a reorganization." This distinction between
coarsening (admissible reduction) and reorganization (emergence) is
analytically important and currently blurred.

### `docs/glossary/` — untagged entries

Twelve glossary entries have no status frontmatter. They appear to be
working definitions but are formally unverified. Adding `status: working-definition`
or `status: needs-formalization` would clarify which entries are stable
and which are provisional.

---

## Summary Table

| File / Gap | Type | Priority |
|---|---|---|
| `bc_taxonomy/boundary_condition_classes.md` | Critical placeholder | 1 |
| `bc_taxonomy/transfer_distortion_metrics.md` | Critical placeholder (content exists in experiments/) | 1 |
| `bc_taxonomy/partition_types.md` | Critical placeholder | 2 |
| `context_navigation/anchor_memory.md` | Critical placeholder | 2 |
| Missing glossary entries (scope_transition, scope_dominance, regime_partition) | Structural gap | 2 |
| `bc_taxonomy/bc_class_to_regime_type_map.md` (missing file) | Structural gap | 2 |
| `notes/open_questions.md` | Empty file | 3 |
| `advanced/epsilon_*.md` — merge and resolve | Underdeveloped + overlap | 3 |
| `core/basins_as_scope_partitions.md` | Stops before key move | 3 |
| `context_navigation/modal_cognition.md` + `bc_taxonomy_cognitive_modes.md` | Critical placeholders | 3 |
| `art_instantiations/` — missing scope cards for physical/agent systems | Structural gap | 3 |
| `overview/roadmap.md` | Underdeveloped | 4 |
| `advanced/emergence_overview.md` — formal emergence condition | Sharpness gap | 4 |
| Untagged glossary entries | Housekeeping | 5 |
