---
status: working-definition
layer: docs/notes/
updated: 2026-03-29
---

# Repository Weak Points — Systematic Assessment

This document identifies underdeveloped entries, structural gaps,
and missing components across the repository.
Entries are ordered by priority: how much analytical damage the gap causes
and how tractable it is to fill.

Last full review: 2026-03-29.

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
| `docs/notes/open_questions.md` | Empty | Q1–Q18 + Q_NEW_1–18 = 36 questions, updated through session 2026-03-28 |
| `docs/notes/research_journal.md` | Empty | Full session logs through 2026-03-28 (II) |
| `docs/notes/literature_links.md` | Empty | 36 lines; references across 6 fields |
| Glossary entries (scope_transition, scope_dominance, regime_partition, admissible_reduction) | Missing | All present, 44–65 lines each, with status frontmatter |
| All glossary entries: status tags | 12 entries untagged | All entries now have `status: working-definition` frontmatter |
| `docs/advanced/epsilon_*.md` overlap | Two overlapping documents | Consolidated; `epsilon_and_scope_resolution.md` is canonical; `epsilon_resolution_window_arw.md` remains as redirect stub (see below — still unresolved) |
| `docs/core/basins_as_scope_partitions.md` | Stopped before key analytical move | 219 lines; formal relationship stated (§4), four divergence cases, admissibility connection |
| `docs/advanced/emergence_overview.md` | No formal emergence condition | Formal condition now present |
| `docs/overview/roadmap.md` | High-level phase list without milestones | 159 lines; 5 phases with milestones, go/no-go decision points |
| Observable decomposition framework | Did not exist | Session 2026-03-18: `docs/advanced/observable_decomposition.md`, `docs/glossary/observable_range.md`, `docs/advanced/observable_consequences.md`, `docs/advanced/latent_degrees_of_freedom.md` all created; R(π), Z(π), F0 formalized |
| DOC_INDEX.md | Did not exist / incomplete | Created and maintained; full sweep 2026-03-29 resolved I-01 through I-05 |
| CASE-0004 (Stuart-Landau emergence) | Did not exist | In-progress; first empirical emergence case with emergence window documented |
| Observable-space cover height method | Did not exist | Session 2026-03-27/28: `docs/advanced/observable_space_cover_height.md`, 14 figures, cross-case analysis across CASE-0001–0004 |
| README.md | 6 weeks stale (missing sessions 2026-03-18/27/28) | Updated 2026-03-29: Observable Decomposition, Emergence Case, Cover Height, full pipeline table, all cases, Research Questions |
| F0 not in `schemas/ScopeSpec.yaml` | `observable_replacement` unrecognized severity value | Added F0/observable_replacement to falsification block with full semantics (2026-03-29) |
| CASE-0004 pipeline artifacts | PartitionResult, Invariants, EpsilonSweep, TransferReport pending | Full pipeline run 2026-03-29: N=4, I_ε=[0.039,0.184], go_nogo: go |
| CASE-0004 ↔ CASE-0001 transfer | Not executed; first same-BC cross-system comparison pending | Executed 2026-03-29: Φ=0.9 (highly_admissible), RCD=0, PCI=1.0 |
| CASE-0001 go_nogo interpretation | Only F4/sweep_refinement path documented | Two-path interpretation (PATH A: sweep_refinement, PATH B: F0 closure at κ_c) documented in CaseRecord; PATH B preferred (2026-03-29) |
| Resonance bridge missing | `resonance_dialectic_context_navigation.md` used resonance informally without ARW link | Added Section 13 with explicit formal/informal distinction and bridge via modal_cognition (2026-03-29) |
| `epsilon_resolution_window_arw.md` dead stub | 13-line redirect stub, no content | Deleted 2026-03-29; DOC_INDEX entry superseded (I-06) |
| `README_session_2026-03-18.md` at root | Unarchived session artifact at repo root | Moved to `archive/sessions/` (2026-03-29, I-07) |

---

## Category 1 — Active Gaps (Blocking or Distorting)

### `Simulationen/` code not integrated into pipeline

**Status:** Sessions 2026-03-27/28 produced working Python scripts for the 2D BC sweep and
observable-space cover height analysis. These live in `Simulationen/` (separate from `pipeline/`)
and have no pipeline interface (no CLI, no CaseRecord integration, no schema outputs).

The cover height method is now cited in open questions (Q_NEW_13–18) and in the research journal,
but it cannot be run as part of the standard ARW pipeline workflow.

**What is missing:**
- A `pipeline/cover_height.py` module (or equivalent) that reads sweep data and produces
  cover height profiles as structured output
- Integration with `CaseRecord.yaml` (artifact registry entry for cover height outputs)
- A schema or output format for cover height results (analogous to `PartitionResult.json`)

**Priority:** 1 (the method is now a first-class research tool; isolation causes drift)

---

### CASE-0001 — F0 closure pending (CASE-0001-ext not yet created)

**Status:** CASE-20260311-0001 (Kuramoto κ-sweep) has `go_nogo: pending`. The PATH B
interpretation (F0 closure: θ*=1.475 is a scope transition at Z(r_ss), not a regime boundary)
is now documented in the CaseRecord (2026-03-29). The next required step is creating
CASE-0001-ext with χ = ∂r_ss/∂κ as primary observable, which diverges at κ_c rather than
collapsing (R(χ) ∋ κ_c). This is the highest-priority remaining experimental item for
the Kuramoto case.

**What is needed:**
- Create `cases/CASE-20260311-0001-ext/` with ScopeSpec.yaml for χ as primary observable
- Run sweep and pipeline on CASE-0001-ext to confirm partition at κ_c
- Formally close CASE-0001 (decision: F0 via r_ss at κ_c)

**Priority:** 1 (see Q_NEW_12 in open_questions.md; CASE-0001 is the only go-pending case)

---

## Category 2 — Structural Housekeeping

### ART instantiation catalog incomplete

**Status:** `docs/art_instantiations/` contains: the geopolitical scope example, the blank
template, five domain hypotheses (ecology, game theory, ML, neuroscience, social science),
statistical physics, synergetics, Littman-Metcalf optics, and the CASE-0010 research report.
The physical systems (Kuramoto, pendulum, Stuart-Landau) still lack standalone ART scope
cards in this folder; their specifications live in `experiments/` and `cases/`.

**Priority:** 3

---

### `cases/.templates/` is empty

**Status:** `pipeline/new_case.py` references templates; directory still empty as of 2026-03-29.

**Priority:** 4

---

### `docs/pipelines/` contains minimal stubs

**Status:** `docs/pipelines/PartitionPipeline.md` (5 lines) and `RegimeGraphPipeline.md` (5 lines)
remain stubs. The actual pipeline documentation is in `pipeline/PartitionPipeline.md` (~170 lines).

**Priority:** 4

---

### Empty top-level directories

| Directory | Status |
|---|---|
| `agents/` | Still empty; role descriptions live in `pipeline/PartitionPipeline.md`. Remove until agent configs become artifacts. |
| `analysis/` | Placeholder; will be needed in Phase 2+. Keep. |
| `papers/` | Placeholder for Phase 4. Keep. |
| `simulations/` | Placeholder; actual simulation code is in `pipeline/sweep.py` and `Simulationen/`. Keep until factored out. |

**Priority:** 4

---

## Category 3 — Content Depth (Not Blocking, But Worth Tracking)

### Cover height open questions (Q_NEW_13–18) — no experimental plan

Six new open questions were raised in sessions 2026-03-27/28 around the observable-space
cover height method. None yet have a designated next-action experimental plan in the research
journal or in `open_questions.md`. Q_NEW_13 (cover-height maxima vs. ε-plateau correspondence)
is directly testable against CASE-0001 data.

**Status:** Track. Priority candidate for next Simulationen session.

---

### BC class: system vs. scope property (Q_NEW_9)

The question of whether BC class belongs to the system or the scope (Q_NEW_9 in
`open_questions.md`) is identified as foundational for the BC taxonomy program.
No dedicated working document exists yet. If the BC class is a scope property, BCManifest
would need separate `system_bc` and `observable_bc` fields, and Φ would decompose into
Φ_obs × Φ_sys. This is a significant potential schema change.

**Status:** Track. Addressed if/when Φ decomposition is implemented (Q_NEW_11).

---

### ε estimation procedure: adaptive refinement not implemented

Three pipeline modules implement ε-sweep, 2D robustness map, and per-observable ε.
Adaptive step refinement near critical ε-values is not yet implemented.
State-dependent ε formalization (Q2) remains open.

**Status:** Track, not blocking current case runs.

---

### Pending cases (CASE-0005 through CASE-0009, SOC1): pipeline not yet run

All six pending cases have pre-pipeline artifacts (ScopeSpec, BCManifest, CaseRecord);
none have been run through the pipeline. CASE-0005 is the most complete (full YAML triple).

**Status:** Queued. Not blocking but represents the next major experimental frontier.

---

## Summary Table

| Gap | Type | Priority | Status |
|---|---|---|---|
| CASE-0001-ext (χ observable) not yet created | Experimental | 1 | PATH B documented; CASE-0001-ext needed |
| `Simulationen/` not in pipeline | Structural | 1 | No pipeline module; isolated analysis code |
| ART instantiation catalog incomplete | Structural | 3 | Scope specs in experiments/, not centralized |
| `cases/.templates/` empty | Housekeeping | 4 | Verify or remove |
| `docs/pipelines/` stubs | Structural | 4 | Redirect or expand |
| Empty dirs (`agents/`) | Housekeeping | 4 | Consider removing |
| Cover height Q_NEW_13–18 no plan | Depth | — | Track; Q_NEW_13 most tractable |
| BC class: system vs. scope (Q_NEW_9) | Depth / Schema | — | Track; foundational question |
| ε adaptive refinement | Depth | — | Track, not blocking |
| Pending cases pipeline not run | Experimental | — | Queued; CASE-0005 most ready |
| ~~README.md stale~~ | Documentation | ~~1~~ | **Resolved 2026-03-29** |
| ~~F0 not in ScopeSpec schema~~ | Schema | ~~1~~ | **Resolved 2026-03-29** |
| ~~CASE-0004 pipeline missing~~ | Experimental | ~~1~~ | **Resolved 2026-03-29** — go; Φ=0.9 |
| ~~CASE-0004↔0001 transfer not run~~ | Experimental | ~~1~~ | **Resolved 2026-03-29** |
| ~~Resonance bridge~~ | Conceptual | ~~2~~ | **Resolved 2026-03-29** — Section 13 added |
| ~~epsilon_resolution_window_arw.md stub~~ | Housekeeping | ~~3~~ | **Resolved 2026-03-29** — deleted |
| ~~README_session_2026-03-18.md at root~~ | Housekeeping | ~~3~~ | **Resolved 2026-03-29** — archived |
