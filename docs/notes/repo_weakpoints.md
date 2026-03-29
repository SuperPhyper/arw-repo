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

---

## Category 1 — Active Gaps (Blocking or Distorting)

### README.md stale — missing two full research sessions

**Status:** Critical. The main README was last substantively updated before session 2026-03-18.
It is missing:
- Session 2026-03-18: observable decomposition, F0 falsification category, pre-scopal substrates,
  observable BC structure, Φ as observable transfer, χ as fluctuation observable (Q_NEW_12)
- Session 2026-03-27: 2D BC sweep (κ × σ), observable-space cover height method, 57% DR finding
- Session 2026-03-28 (I): cover height cross-case analysis across CASE-0001–0004; Pattern A/B/C
- Session 2026-03-28 (II): 2D cover height on CASE-0002/0003/0004; BC interaction structure (Q_NEW_18)
- CASE-20260328-0010 (German School System multi-BC case) — first multi-BC-class case
- Q_NEW_13–18 (cover height open questions) not reflected in README Research Questions section
- Pipeline modules: `epsilon_kappa_map.py`, `epsilon_multi_observable.py`, `audit.py`, `new_case.py`
  are absent from the README pipeline table (only listed in `pipeline/README.md`)

**Priority:** 1 (first-impression document; severely outdated for any new reader or LLM)

**Recommended action:** Update README Empirical Results, Pipeline, cases/ structure, and Research
Questions sections. *(Being addressed in this session.)*

---

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

### F0 not yet in ScopeSpec.yaml falsification schema

**Status:** F0 (R(π) ∩ B ≠ B, severity: observable_replacement) is formally defined in
`docs/glossary/observable_range.md` and referenced in the skill context, but it is not yet
a recognized `severity:` value in the ScopeSpec.yaml schema (`schemas/ScopeSpec.yaml`).
Existing falsification entries in CASE-0001 and CASE-0002 use only F1–F4 severities.
Q_NEW_2 is still open: should F0 entries be required in ScopeSpec.yaml?

**Priority:** 1 (structural gap between documented theory and schema)

---

### CASE-0001 sweep_refinement pending since 2026-03-12

**Status:** CASE-20260311-0001 (Kuramoto κ-sweep) has `go_nogo: pending` with failure mode
`F1: sweep_refinement` — θ* ≈ 1.475 sits at the sweep boundary. A refined sweep near κ ∈ [1.0, 2.5]
was called for but not executed. This is additionally complicated by the session 2026-03-18 finding
that θ* ≈ 1.475 is more precisely a scope transition (κ_c lies in Z(r_ss)) than a regime boundary.

**What is needed:**
- Either: run sweep refinement with a different observable (e.g., χ = ∂r_ss/∂κ as proposed in Q_NEW_12)
- Or: formally close CASE-0001 with the interpretation that r_ss cannot have a valid regime boundary
  at κ_c (F0 classification), document this in the CaseRecord, and open a new CASE-0001 extension
  with χ as primary observable

**Priority:** 1 (single go-pending case in the four active cases)

---

### CASE-0004 pipeline artifacts pending

**Status:** CASE-20260318-0004 (Stuart-Landau, first emergence case) has `status: in_progress`.
`PartitionResult.json`, `Invariants.json`, and `TransferMetrics.json` (for planned transfer to
CASE-0001) are not yet produced. The theoretical analysis (emergence window, PLV sufficiency,
amp_asym failure) is complete; the pipeline has not been run.

**Priority:** 1 (only after this is done can the first same-BC cross-system transfer be computed)

---

### CASE-0004 ↔ CASE-0001 transfer not yet executed

**Status:** The transfer between CASE-20260318-0004 (Coupling, Stuart-Landau) and
CASE-20260311-0001 (Coupling, Kuramoto) is planned as the first same-BC cross-system comparison.
It requires CASE-0004's pipeline to be complete first (see above).

**Priority:** 1 (depends on CASE-0004 pipeline completion)

---

### Resonance: informal usage persists in architecture documents

**Status:** Partially addressed (glossary entries `resonance.md` 125 lines, `resonance_field.md`
99 lines, `boundary_conditions_as_resonance_filters.md` 176 lines exist).
`resonance_dialectic_context_navigation.md` (216 lines) still uses "resonance" 12 times without
consistently distinguishing formal (coupling BC mechanism) from informal usage.

**Priority:** 2 (does not block experiments but affects conceptual consistency)

---

## Category 2 — Structural Housekeeping

### `epsilon_resolution_window_arw.md` — dead redirect stub

**Status:** 13 lines. Redirects to `epsilon_and_scope_resolution.md` (canonical ε document,
180 lines). The stub adds no content. Still present as of 2026-03-29.

**Recommended action:** Delete the file. Update any links in `docs/advanced/README.md`.

**Priority:** 3

---

### `README_session_2026-03-18.md` at repo root — unarchived session artifact

**Status:** A session working document remains at the root level alongside `README.md`.
It should be in `archive/sessions/`.

**Recommended action:** Move to `archive/sessions/README_session_2026-03-18.md`.

**Priority:** 3

---

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
| README.md 6 weeks stale | Documentation | 1 | Being updated this session |
| `Simulationen/` not in pipeline | Structural | 1 | No pipeline module; isolated analysis code |
| F0 not in ScopeSpec schema | Schema | 1 | Defined in glossary, missing in schema |
| CASE-0001 sweep_refinement pending | Experimental | 1 | 18 days unresolved; F0 / χ path needed |
| CASE-0004 pipeline artifacts missing | Experimental | 1 | First emergence case incomplete |
| CASE-0004 ↔ CASE-0001 transfer not run | Experimental | 1 | Depends on CASE-0004 pipeline |
| Resonance formalization bridge | Conceptual consistency | 2 | Partially addressed; architecture docs lagging |
| `epsilon_resolution_window_arw.md` dead stub | Housekeeping | 3 | Delete |
| `README_session_2026-03-18.md` at root | Housekeeping | 3 | Archive |
| ART instantiation catalog incomplete | Structural | 3 | Scope specs in experiments/, not centralized |
| `cases/.templates/` empty | Housekeeping | 4 | Verify or remove |
| `docs/pipelines/` stubs | Structural | 4 | Redirect or expand |
| Empty dirs (`agents/`) | Housekeeping | 4 | Consider removing |
| Cover height Q_NEW_13–18 no plan | Depth | — | Track; Q_NEW_13 most tractable |
| BC class: system vs. scope (Q_NEW_9) | Depth / Schema | — | Track; foundational question |
| ε adaptive refinement | Depth | — | Track, not blocking |
| Pending cases pipeline not run | Experimental | — | Queued; CASE-0005 most ready |
