---
status: working-definition
updated: 2026-03-11
---

# Repository Weak Points — Systematic Assessment

This document identifies underdeveloped entries, structural gaps,
and missing components across the repository.
Entries are ordered by priority: how much analytical damage the gap causes
and how tractable it is to fill.

Last full review: 2026-03-11.

---

## Resolved Items (Previously Critical)

The following items were identified as critical gaps in the initial assessment
and have since been substantively developed. They are listed here for audit
trail purposes and are no longer blocking.

| File | Previous state | Current state |
|---|---|---|
| `docs/bc_taxonomy/boundary_condition_classes.md` | 6-item list, no definitions | 289 lines; all 6 classes with formal definitions, regime consequences, cross-system instantiations |
| `docs/bc_taxonomy/partition_types.md` | 3-item list | 256 lines; 5 types formally defined with properties and scope-transition behavior |
| `docs/bc_taxonomy/transfer_distortion_metrics.md` | 4-item list | 229 lines; RCD, TBS, PCI, SDI with mathematical definitions + composite Φ score |
| `docs/bc_taxonomy/bc_class_to_regime_type_map.md` | Did not exist | 131 lines; mapping table, cross-system verification, failure cases, regime graph topology |
| `docs/context_navigation/anchor_memory.md` | 1 sentence | 159 lines; definition, formation, retrieval, stability score, decay, cross-episode transfer |
| `docs/context_navigation/modal_cognition.md` | 1 sentence | 121 lines; modes as reduced scopes, mode identity, mode ecology, switching as scope transition |
| `docs/context_navigation/bc_taxonomy_cognitive_modes.md` | 1 sentence | 170 lines; BC class → mode mapping with detail per class |
| `docs/context_navigation/context_navigation_ai.md` | 4-item list | 116 lines; system map with component → ARW mapping, scope transitions in operation |
| `docs/notes/open_questions.md` | Empty | 105 lines; 14 questions across formalization, empirical, conceptual, methodological |
| `docs/notes/research_journal.md` | Empty | 36 lines; current focus, pending decisions, notes on resonance |
| `docs/notes/literature_links.md` | Empty | 36 lines; references across 6 fields |
| Glossary entries (scope_transition, scope_dominance, regime_partition, admissible_reduction) | Missing | All present, 44–65 lines each, with status frontmatter |
| All glossary entries: status tags | 12 entries untagged | All entries now have `status: working-definition` frontmatter |
| `docs/advanced/epsilon_*.md` overlap | Two overlapping documents | Consolidated; `epsilon_and_scope_resolution.md` (180 lines, 7 sections) is the canonical document; `epsilon_resolution_window_arw.md` is a redirect stub |
| `docs/core/basins_as_scope_partitions.md` | Stopped before key analytical move | 219 lines; formal relationship stated (§4), four divergence cases, admissibility connection |
| `docs/advanced/emergence_overview.md` | No formal emergence condition | Formal condition now present: admissible reduction ([x]_S ⊆ [x]_S') vs. emergence (∃x: [x]_S ⊄ [x]_S') |
| `docs/overview/roadmap.md` | High-level phase list without milestones | 159 lines; 5 phases with milestones, go/no-go decision points, OSV fellowship connection |

---

## Category 1 — Active Gaps (Blocking or Distorting)

### Resonance: informal usage in context_navigation documents

**Status:** Partially addressed. The glossary entries (`resonance.md`: 125 lines,
`resonance_field.md`: 99 lines) provide formal definitions.
`boundary_conditions_as_resonance_filters.md` (176 lines) develops the concept
in the architecture context.

**What remains:** `resonance_dialectic_context_navigation.md` (216 lines) uses
"resonance" 12 times but does not consistently distinguish between formal usage
(coherent coupling under compatible BCs) and informal/metaphorical usage.
The research journal notes this explicitly and proposes that resonance is the
*mechanism* by which coupling BC generates regime structure. This tentative
answer needs to be formalized and reflected back into the document.

**Recommended action:** Add a short paragraph to `resonance_dialectic_context_navigation.md`
that explicitly marks which uses of "resonance" are formal (as defined in the glossary)
and which are informal, or formalize the informal uses by connecting them to the
coupling BC class.

**Priority:** 2 (does not block experiments but affects conceptual consistency)

---

### `epsilon_resolution_window_arw.md` — dead redirect stub

**Status:** 13 lines. Redirects to `epsilon_and_scope_resolution.md` (which is
now the canonical ε document at 180 lines). The stub adds no content.

**Recommended action:** Delete the file. Remove the reference from
`docs/advanced/README.md`. Any links pointing to it should be updated to
point directly to `epsilon_and_scope_resolution.md`.

**Priority:** 3 (housekeeping, low analytical impact)

---

### ART instantiation catalog incomplete

**Status:** `docs/art_instantiations/` contains only the geopolitical scope example
(317 lines) and the blank template (132 lines). The physical systems (Kuramoto,
pendulum) and the agent system (labyrinth) have their ART scope specifications
embedded in their respective experiment files under `experiments/`, but not as
standalone scope cards in `art_instantiations/`.

**Recommended action:** Either:
(a) Extract condensed scope-tuple reference cards for Kuramoto, pendulum, and
labyrinth from the experiment files and place them in `art_instantiations/`, or
(b) Accept that `art_instantiations/` is an example collection (not a complete catalog)
and document this explicitly in the folder's README.

**Priority:** 3 (does not block work; the scope specifications exist, they are
just not centralized)

---

## Category 2 — Structural Housekeeping

### Empty top-level directories

Four directories contain zero files:

| Directory | Intended purpose | Recommendation |
|---|---|---|
| `agents/` | Agent role definitions | Roles are documented in `pipeline/PartitionPipeline.md` § Agent Role Mapping. The directory should either be populated when agent configs are implemented, or removed until needed. |
| `analysis/` | Cross-case analysis outputs | Will be needed in Phase 2+. Keep as placeholder. |
| `papers/` | Paper drafts | Keep as placeholder; will be populated during Phase 4 (consolidation). |
| `simulations/` | Standalone simulation code | Simulation kernels currently live in `pipeline/sweep.py`. Factor out when systems mature beyond the sweep interface. |

**Recommended action:** Keep `analysis/`, `papers/`, `simulations/` as placeholders
(they align with roadmap phases). Consider removing `agents/` until agent
configurations become artifacts rather than just documentation — the role
descriptions already live in `PartitionPipeline.md`.

**Priority:** 4 (cosmetic; no analytical impact)

---

### `cases/.templates/` is empty

`pipeline.new_case` references templates, but the `.templates/` directory
contains no files. Either the templates are generated programmatically
(in which case the directory is unnecessary), or template files were
planned but not created.

**Recommended action:** Verify whether `new_case.py` uses this directory.
If not, remove it. If yes, populate it with the schema stubs that `new_case`
would stamp.

**Priority:** 4

---

### `docs/pipelines/` contains minimal stubs

`PartitionPipeline.md` (5 lines) and `RegimeGraphPipeline.md` (5 lines) are
conceptual stubs. The actual implemented pipeline documentation lives in
`pipeline/PartitionPipeline.md` (full design document, ~170 lines).

**Recommended action:** Either:
(a) Expand the stubs in `docs/pipelines/` to be the conceptual design documents
and keep `pipeline/PartitionPipeline.md` as the implementation reference, or
(b) Redirect the stubs to the implementation document and note the distinction.

**Priority:** 4 (the information exists, it is just split awkwardly)

---

## Category 3 — Content Depth (Not Blocking, But Worth Tracking)

These items are not gaps in the sense of missing content — the relevant
documents exist and have substance. They are tracked here as directions
where further formalization would strengthen the framework.

### ε estimation procedure

`epsilon_and_scope_resolution.md` § 7 lists open questions including
"How is ε estimated empirically?" The Kuramoto case uses ε = 0.05 as a
concrete number; the labyrinth uses cosine distance < 0.1. There is no
general procedure for choosing ε. This matters for reproducibility
as soon as new systems are added.

### Resonance ↔ coupling BC: formal relationship

The research journal tentatively proposes that resonance is the mechanism
by which coupling BC generates regime structure. This is an interesting
analytical claim that could sharpen the BC taxonomy if formalized.

### ART scope cards for physical/agent systems

See Category 1. The scope specifications exist in experiment files
but are not available as quick-reference cards.

---

## Summary Table

| Gap | Type | Priority | Status |
|---|---|---|---|
| Resonance formalization in context_navigation | Conceptual consistency | 2 | Partially addressed; glossary entries exist, bridge to architecture usage missing |
| `epsilon_resolution_window_arw.md` dead stub | Housekeeping | 3 | Delete file, update links |
| ART instantiation catalog incomplete | Structural | 3 | Scope specs exist in experiments/, not centralized |
| Empty dirs (agents/) | Housekeeping | 4 | Consider removing until populated |
| `cases/.templates/` empty | Housekeeping | 4 | Verify if used by new_case.py |
| `docs/pipelines/` minimal stubs | Structural | 4 | Redirect or expand |
| ε estimation procedure | Depth | — | Tracked, not blocking |
| Resonance ↔ coupling formalization | Depth | — | Tracked, not blocking |
