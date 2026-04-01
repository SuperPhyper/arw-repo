---
status: working-definition
layer: docs/meta/
last_updated: 2026-03-29
---

# DOC_INDEX — ARW/ART Documentation Index

Anti-pile-up spine for all conceptual documents in `docs/`.
Every `.md` file in `docs/` (except README.md files) must have an entry here.
See `arw-doc-consistency` skill for usage rules.

**Rules:**
- Before creating a new doc: check this index for existing coverage.
- After creating a doc: add its row in the same session.
- Superseded files: update status to `superseded` and fill the Supersedes column.
- Index is append-only: entries are never deleted, only marked `superseded`.

---

## Known Issues

| ID | File | Issue | Resolution | Date |
|---|---|---|---|---|
| I-01 | `docs/advanced/emergence/epsilon_induced_relational_emergence.md` | DUPLICATE — identical to `docs/advanced/epsilon_induced_relational_emergence.md` | Deleted `docs/advanced/emergence/` subdirectory | 2026-03-29 |
| I-02 | `docs/context_navigation/` (4 files) vs `docs/cognitive_architecture/` | Apparent diverged copies | Confirmed as intentional redirect stubs (`redirects_to:` front-matter); not a real issue | 2026-03-29 |
| I-03 | `docs/notes/operator_signatures_cross_domain.md` | LAYER MISMATCH — front-matter said `layer: advanced` | Moved to `docs/advanced/operator_signatures_cross_domain.md` | 2026-03-29 |
| I-04 | `docs/notes/open_questions_2026-03-18.md` + `open_questions_session_2026-03-18.md` | ARCHIVED STUBS in active notes/ | Moved both to `archive/sessions/` | 2026-03-29 |
| I-05 | `kuramoto_arw_notes.md`, `kuramoto_bc_coupled_eps_comparison_report.md`, `methodological_lessons.md` | MISSING FRONT-MATTER | Added `status: note` + `layer: docs/notes/` to all three | 2026-03-29 |
| I-06 | `docs/advanced/epsilon_resolution_window_arw.md` | DEAD STUB — redirected to epsilon_and_scope_resolution.md with no content | Deleted; entry superseded in DOC_INDEX | 2026-03-29 |
| I-07 | `README_session_2026-03-18.md` at repo root | UNARCHIVED SESSION ARTIFACT | Moved to `archive/sessions/` | 2026-03-29 |
| I-08 | `docs/context_navigation/resonance_dialectic_context_navigation.md` | INFORMAL RESONANCE USAGE — 12 informal uses without formal ARW distinction | Added Section 13 (formal vs. informal resonance note) | 2026-03-29 |
| I-09 | `schemas/ScopeSpec.yaml` — falsification severity field | F0 (`observable_replacement`) missing as valid severity value | Added F0 documentation to falsification block | 2026-03-29 |

---

## Layer: overview

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/overview/why_arw.md | working-definition | problem motivation, regime identification, observable failure, resolution dependence | — | Narrative entry point; uses double pendulum + Kuramoto as motivating cases |
| docs/overview/arw_concepts.md | working-definition | scope components B, Π, Δ, ε — conceptual intro with examples | — | Bridge between why_arw.md and formal docs; covers F0/F1, BC classes overview |
| docs/overview/ARW_in_one_page.md | working-definition | ARW one-page summary, entry point | — | Primary human-facing intro |
| docs/overview/arw-operator.md | working-definition | ARW operator, formal definition | — | Key entry point for LLMs |
| docs/overview/conceptual_outlook.md | hypothesis | ARW in social systems, conceptual extension | — | Provisional; social scope |
| docs/overview/limitations_and_open_questions.md | working-definition | Known limitations, open research questions | — | Links to open_questions.md |
| docs/overview/minimal_example.md | hypothesis | Two-Link Pendulum minimal ARW example | — | ART-level illustration |
| docs/overview/novelty_and_projected_value.md | working-definition | ARW novelty, projected research value | — | — |
| docs/overview/roadmap.md | working-definition | Research roadmap | — | Subject to revision |

---

## Layer: glossary

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/glossary/scope.md | working-definition | scope tuple S=(B,Π,Δ,ε), canonical definitions | — | **Source of truth for B,Π,Δ,ε. Frozen.** |
| docs/glossary/admissibility.md | working-definition | admissibility, admissibility condition | — | — |
| docs/glossary/admissible_reduction.md | working-definition | admissible reduction | — | — |
| docs/glossary/attractor.md | working-definition | attractor | — | — |
| docs/glossary/basin.md | working-definition | basin of attraction | — | — |
| docs/glossary/boundary_conditions.md | working-definition | boundary conditions (general) | — | Distinct from BC classes |
| docs/glossary/canonical_vocabulary.md | hypothesis | canonical vocabulary mapping | — | Not yet a definition |
| docs/glossary/chaos.md | working-definition | chaos, Lyapunov exponent in ARW context | — | — |
| docs/glossary/coarse_graining.md | working-definition | coarse-graining, ε-equivalence | — | — |
| docs/glossary/coupling.md | working-definition | coupling (BC class) | — | See also bc_taxonomy/ |
| docs/glossary/emergence.md | working-definition | emergence (ARW definition) | — | See advanced/emergence_overview.md for full treatment |
| docs/glossary/emergent_solution_space.md | working-definition | emergent solution space | — | Links to advanced/emergent_solution_space.md |
| docs/glossary/glossary_index.md | working-definition | glossary navigation index | — | Meta-navigation within glossary |
| docs/glossary/glossary_map.md | working-definition | glossary concept map | — | Visual/structural companion to glossary_index |
| docs/glossary/independent_violation_axes.md | working-definition | independent violation axes (IVA), Z(π) geometry | — | See advanced/iva_z_geometry.md for full treatment |
| docs/glossary/latent_degrees_of_freedom.md | working-definition | latent degrees of freedom | — | See advanced/latent_degrees_of_freedom.md |
| docs/glossary/observable.md | working-definition | observable, π: X → D | — | — |
| docs/glossary/observable_range.md | working-definition | observable range R(π), exclusion zone Z(π), F0 | — | **Key doc for F0 falsification** |
| docs/glossary/partition.md | working-definition | partition, regime partition | — | — |
| docs/glossary/regime.md | working-definition | regime | — | — |
| docs/glossary/regime_partition.md | working-definition | regime partition (formal) | — | — |
| docs/glossary/resonance.md | working-definition | resonance (ARW definition) | — | Provisional term; note historical naming issues |
| docs/glossary/resonance_field.md | working-definition | resonance field | — | Provisional |
| docs/glossary/scope_dominance.md | working-definition | scope dominance | — | See also docs/core/scope_dominance.md |
| docs/glossary/scope_transition.md | working-definition | scope transition (glossary entry) | — | See also docs/core/scope_transition.md |
| docs/glossary/stability.md | working-definition | stability, regime stability | — | — |
| docs/glossary/state_space.md | working-definition | state space X | — | — |

---

## Layer: core

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/core/arw_scope_reduction_partition_criterion.md | working-definition | scope transition, admissible reduction, partition criterion | — | — |
| docs/core/basins_as_scope_partitions.md | working-definition | basins as scope partitions | — | — |
| docs/core/bc_classes_and_regime_generation.md | working-definition | BC classes and regime generation | — | Connects to bc_taxonomy/ |
| docs/core/regime_stability_regions.md | working-definition | regime stability regions | — | — |
| docs/core/scope_dominance.md | working-definition | scope dominance (formal) | — | See also docs/glossary/scope_dominance.md |
| docs/core/scope_resolution.md | working-definition | scope resolution | — | — |
| docs/core/scope_transition.md | working-definition | scope transition (formal) | — | See also docs/glossary/scope_transition.md |

---

## Layer: advanced

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/advanced/admissible_resolution_lower_bound.md | working-definition | admissible resolution lower bound | — | — |
| docs/advanced/arw_emergence_bc_relative.md | working-definition | emergence as BC-relative observable collapse, emergence window, ε-width | — | Links CASE-20260318-0004 (first empirical emergence case) |
| docs/advanced/arw_hypothesis_structure_diagram.md | note | ARW hypothesis structure, diagram | — | Provisional diagram reference |
| docs/advanced/axiom_a_empirical_validation.md | working-definition | Axiom A empirical validation | — | — |
| docs/advanced/bc_extraction_method.md | experiment-proposal | BC extraction method | — | — |
| docs/advanced/bc_operator_signatures_arw.md | working-definition | BC classes, operator signatures S1–S5, regime partitions | — | Full treatment; extends bc_taxonomy/ |
| docs/advanced/bc_relative_observable_indistinguishability.md | working-definition | BC-relative observable indistinguishability | — | — |
| docs/advanced/bc_stratification_dynamic_subscopes.md | hypothesis | BC stratification, dynamic subscopes | — | — |
| docs/advanced/cross_domain_signature_matrix.md | working-definition | cross-domain signature matrix | — | — |
| docs/advanced/emergence_and_latent_degrees_of_freedom.md | working-definition | emergence and latent DoF | — | — |
| docs/advanced/emergence_overview.md | working-definition | emergence overview | — | Entry point for emergence cluster |
| docs/advanced/emergence_scope_transition.md | working-definition | emergence as scope transition | — | — |
| docs/advanced/emergent_solution_space.md | working-definition | emergent solution space (advanced) | — | — |
| docs/advanced/engineering_scope_reduction_and_regime_shift.md | hypothesis | engineering scope reduction, regime shift | — | — |
| docs/advanced/epsilon_and_scope_resolution.md | working-definition | ε and scope resolution | — | — |
| docs/advanced/epsilon_induced_relational_emergence.md | working-definition | ε-induced relational emergence | — | **Canonical copy.** Duplicate at docs/advanced/emergence/ — see I-01 |
| docs/advanced/epsilon_induced_scope_family.md | working-definition | ε-induced scope families | — | — |
| ~~docs/advanced/epsilon_resolution_window_arw.md~~ | — | — | docs/advanced/epsilon_and_scope_resolution.md | **DELETED 2026-03-29** — dead redirect stub; canonical doc is epsilon_and_scope_resolution.md |
| docs/advanced/extended_z_observable_necessity.md | working-definition | extended Z(π), observable class necessity, multi-BC systems | — | — |
| docs/advanced/h2_prime_theorem.md | working-definition | Theorem H2' — IVA dimensionality principle | — | — |
| docs/advanced/iva_z_geometry.md | working-definition | IVA, Z(π) geometry | — | — |
| docs/advanced/latent_degrees_of_freedom.md | claim | latent degrees of freedom, BC mapping, observable hierarchy | — | Still claim-level |
| docs/advanced/mathematical_scope_boundary.md | working-definition | mathematical scope boundaries, primitive operator bases | — | — |
| docs/advanced/minimal_operator_basis_arw.md | working-definition | minimal operator basis | — | — |
| docs/advanced/observable_consequences.md | claim | consequences of observable decomposition | — | Still claim-level |
| docs/advanced/observable_decomposition.md | claim | observable decomposition, pre-scopal substrates, BC mapping | — | Still claim-level; key for F0 |
| docs/advanced/observable_space_cover_height.md | hypothesis | observable-space cover height | — | — |
| docs/advanced/operator_signature_catalog.md | working-definition | operator signature catalog S1–S5 | — | — |
| docs/advanced/primitive_operator_time_coupling.md | working-definition | primitive operators, time coupling, emergent dynamic BCs | — | — |
| docs/advanced/quantum_operator_extension.md | open-question | quantum operator extension | — | Open question; speculative |
| docs/advanced/report_chi_observable.md | claim | χ = ∂r_ss/∂κ as fluctuation observable | — | Empirical; links CASE-0001 |
| docs/advanced/scope_completeness.md | working-definition | scope completeness, observable agreement | — | — |
| docs/advanced/arw_observable_complexity_landscape.md | note | observable complexity landscape, subscope density | — | MOVED from figures/ 2026-03-29 |
| docs/advanced/regime_graphs_arw.md | note | regime graphs, partition adjacency structure | — | MOVED from figures/ 2026-03-29 |
| docs/advanced/operator_signatures_cross_domain.md | hypothesis | operator signatures across domains | — | MOVED from docs/notes/ 2026-03-29 (I-03) |
| ~~docs/advanced/emergence/epsilon_induced_relational_emergence.md~~ | — | — | — | **DELETED 2026-03-29 (was duplicate of docs/advanced/epsilon_induced_relational_emergence.md — I-01)** |

---

## Layer: bc_taxonomy

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/bc_taxonomy/bc_class_to_regime_type_map.md | working-definition | BC class → regime type mapping | — | — |
| docs/bc_taxonomy/boundary_condition_classes.md | working-definition | BC classes 1–6 (Coupling, Restriction, Forcing, Dissipation, Aggregation, Symmetry Breaking) | — | **Primary BC taxonomy reference** |
| docs/bc_taxonomy/partition_types.md | working-definition | partition types | — | — |
| docs/bc_taxonomy/transfer_distortion_metrics.md | working-definition | Φ, TBS_norm, RCD, PCI, SDI | — | **Source of truth for transfer metrics** |

---

## Layer: art_instantiations

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/art_instantiations/art_geopolitical_scope_example.md | working-definition | ART geopolitical scope instantiation | — | — |
| docs/art_instantiations/art_scope_template.md | working-definition | ART scope template | — | Reusable template |
| docs/art_instantiations/arw_for_ecology.md | hypothesis | ARW for ecology | — | — |
| docs/art_instantiations/arw_for_game_theory.md | hypothesis | ARW for game theory | — | — |
| docs/art_instantiations/arw_for_ml.md | hypothesis | ARW for ML | — | — |
| docs/art_instantiations/arw_for_neuroscience.md | hypothesis | ARW for neuroscience | — | — |
| docs/art_instantiations/arw_for_social_science.md | hypothesis | ARW for social science | — | — |
| docs/art_instantiations/arw_for_statistical_physics.md | hypothesis | ARW for statistical physics | — | — |
| docs/art_instantiations/arw_for_synergetics.md | hypothesis | ARW for synergetics | — | — |
| docs/art_instantiations/arw_littman_bc_analysis.md | interpretation | BC structure in Littman–Metcalf method | — | ART instantiation for optics/photonics |
| docs/art_instantiations/research_report_CASE-20260328-0010.md | working-definition | structural observable failure in social scopes | — | Links CASE-20260328-0010 |

---

## Layer: cognitive_architecture

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/cognitive_architecture/anchor_memory.md | working-definition | anchor memory (cognitive arch.) | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/bc_taxonomy_cognitive_modes.md | working-definition | BC taxonomy and cognitive modes | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/context_navigation_ai.md | working-definition | context navigation AI system map | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/modal_cognition.md | working-definition | modal cognition | — | ⚠ See I-02: diverged copy also in context_navigation/ |

---

## Layer: context_navigation

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/context_navigation/admissibility_and_mode_selection.md | working-definition | admissibility in context-navigating architectures, mode selection | — | — |
| docs/context_navigation/agent_architecture_mode_ecology.md | hypothesis | agent architecture, mode ecology | — | — |
| docs/context_navigation/anchor_memory.md | note | redirect → docs/cognitive_architecture/anchor_memory.md | — | Intentional redirect stub (redirects_to: front-matter) |
| docs/context_navigation/bc_taxonomy_cognitive_modes.md | note | redirect → docs/cognitive_architecture/bc_taxonomy_cognitive_modes.md | — | Intentional redirect stub |
| docs/context_navigation/boundary_conditions_as_resonance_filters.md | hypothesis | BC as resonance filters | — | — |
| docs/context_navigation/context_navigation_ai.md | note | redirect → docs/cognitive_architecture/context_navigation_ai.md | — | Intentional redirect stub |
| docs/context_navigation/context_navigation_architecture_notes.md | hypothesis | context navigation architecture, mode optimization | — | — |
| docs/context_navigation/context_navigation_model_spec.md | working-definition | context navigation model specification | — | — |
| docs/context_navigation/modal_cognition.md | note | redirect → docs/cognitive_architecture/modal_cognition.md | — | Intentional redirect stub |
| docs/context_navigation/resonance_dialectic_context_navigation.md | hypothesis | resonance–dialectic context navigation | — | — |
| docs/context_navigation/salience_mode_ecology.md | hypothesis | salience as emergent property of mode ecology | — | — |
| docs/context_navigation/context_navigation_scope_spec.md | working-definition | S_global scope (designed modes experiment), mode_dist primary observable, zone sub-scopes, agent ARW role mapping | — | Scope companion to context_navigation_model_spec.md; covers S_global, Π_global, Z(mode_dist), F0–F4 |
| docs/context_navigation/mode_scope_regime_audit.md | note | mode-scope-regime audit, terminological corrections post-audit | — | Post-audit clarifications: modes as regimes, salience as fluctuation observable, consolidation as asymptotic process |
| docs/context_navigation/transfer_semantics_context_navigation.md | working-definition | Φ as observable transfer (not system transfer), three transfer experiment types for labyrinth | — | Transfer protocol for context navigation; Φ reporting requirements |
| docs/context_navigation/context_navigation_emergent_modes_experiment.md | experiment-proposal | emergent modes experiment, ARW as observation instrument, unstructured policy regime analysis | — | Complementary to designed modes experiment; H1–H4; references experiments/labyrinth_experiment_agenda.md |
| docs/context_navigation/context_navigation_scope_spec_emergent.md | working-definition | S_emergent scope, action_dist observable, emergent regime partition, R(action_dist), Z(action_dist) | — | Scope companion to context_navigation_emergent_modes_experiment.md; distinct from context_navigation_scope_spec.md |
| docs/context_navigation/agent_online_scope.md | working-definition | S_online scope, perception observable set (7 observables), weight dynamics, encounter protocol, saliency events, ε_stab | — | One of three scopes in three-scope architecture; S_online ≠ S_emergent; ε_stab ≠ ARW ε |
| docs/context_navigation/agent_sleep_scope.md | working-definition | S_sleep scope, archetype library, archetype revision protocol, eff_norm, effectiveness evaluation, Π_evaluation | — | Agent-internal offline phase; complements S_online; distinct from S_observer |
| docs/context_navigation/arw_observer_scope.md | working-definition | S_observer scope, Π_behavior (Layer 1 + Layer 2), Z_shared(S_observer), regime detection protocol, salience_freq, action_switching_rate | — | External ARW measurement scope; refines S_emergent; behavioral fluctuation observable analog of χ = ∂r_ss/∂κ |

---

## Layer: experiments

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| experiments/labyrinth_three_scope_minimal_setup.md | experiment-proposal | minimal three-scope experiment, 9×9 labyrinth, PPO+S_online+S_sleep, action_dist ε-sweep, hyperparameter table | — | Execution-oriented; covers Phase 0–2; all hyperparameters consolidated in §9 |

---

## Layer: related_fields

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/related_fields/related_fields_and_methodological_connections.md | working-definition | related fields, methodological connections | — | — |

---

## Layer: pipelines

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/pipelines/epsilon_algorithm.md | working-definition | ε-filtration algorithm | — | — |
| docs/pipelines/epsilon_filtration.md | working-definition | ε-filtration pipeline | — | — |
| docs/pipelines/PartitionPipeline.md | note | partition pipeline design | — | — |
| docs/pipelines/RegimeGraphPipeline.md | note | regime graph pipeline design | — | — |

---

## Layer: figures

See `docs/figures/FIGURES_INDEX.md` for the complete registry of all 57 figure files
and their description documents. Summary of description `.md` files:

| File path | Status | Figures covered | Notes |
|---|---|---|---|
| docs/figures/FIGURES_INDEX.md | note | All 57 figures (registry) | Created 2026-03-29 |
| docs/figures/boundary_shift.md | note | boundary_shift.png | — |
| docs/figures/cover_2d_all_cases.md | note | cover2d_* (14 files, CASE-0002/0003/0004) | — |
| docs/figures/cover_height_analysis.md | note | cover_height_*, cover_cp_*, fiber_* (13 files) | Stubs; description pending |
| docs/figures/epsilon_figures.md | note | ε-filtration figures | — |
| docs/figures/epsilon_kappa_robustness.md | note | epsilon_kappa_robustness.png | — |
| docs/figures/epsilon_sweep_kuramoto.md | note | epsilon_sweep_kuramoto.png | — |
| docs/figures/iva_h2prime_figures.md | note | fig_iva1–3 (3 files) | Stubs; description pending |
| docs/figures/kuramoto_2d_cover_height.md | note | kuramoto_2d_observable_heatmap.png | — |
| docs/figures/kuramoto_observables.md | note | r_ss_vs_kappa, chi_vs_kappa, bc_sweep_lambda | Stubs; description pending |
| docs/figures/kuramoto_paper_figures.md | note | fig1–4, time_series_*, metrics_vs_coupling, epsilon_window | Stubs; description pending |
| docs/figures/kuramoto_sync_transition.md | note | kuramoto_sync_transition.png | — |
| docs/figures/multi_observable_agreement.md | note | multi_observable_agreement.png | — |
| docs/figures/observable_decomposition_figures.md | note | fig_emp1–3, fig_ext1–4 (7 files) | Stubs; description pending |
| docs/figures/pci_scaling.md | note | pci_scaling.png | — |
| docs/figures/scope_completeness.md | note | scope_completeness.png, obs_* (3 files) | — |
| docs/figures/structural_diagrams.md | note | arw_signature_graph.mmd | Stub; description pending |
| docs/figures/epsilon_figures.md | working-definition | ε-filtration figures | — | — |
| docs/figures/epsilon_kappa_robustness.md | note | scope robustness I_ε(κ) figure | — | — |
| docs/figures/epsilon_sweep_kuramoto.md | note | ε-sweep partition invariant (Kuramoto) | — | — |
| docs/figures/kuramoto_2d_cover_height.md | note | Kuramoto 2D BC sweep cover height | — | — |
| docs/figures/kuramoto_sync_transition.md | note | Kuramoto synchronization transition figure | — | — |
| docs/figures/multi_observable_agreement.md | note | multi-observable agreement (Double Pendulum) | — | — |
| docs/figures/pci_scaling.md | note | PCI scaling figure | — | — |
| docs/figures/scope_completeness.md | note | scope completeness figure | — | — |

---

## Layer: cases (docs/cases/)

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/cases/CASE_TEMPLATE_signature_first.md | note | case template for signature-first pre-pipeline docs | — | Template; see docs/cases/README.md for TODO on motivational docs |

---

## Layer: meta

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/meta/LLM_CONTRIBUTION_CHARTER.md | working-definition | LLM contribution rules, repo governance | — | **Mandatory reading for LLM contributors** |
| docs/meta/audit_report_2026-03-15.md | note | audit findings 2026-03-15 | — | Historical; not updated after that date |
| docs/meta/llm_memory_map.md | note | LLM memory map | — | — |
| docs/meta/maintenance_checklist.md | working-definition | periodic repo maintenance checklist | — | Created 2026-03-29 |
| docs/meta/repo_design.md | working-definition | repository design principles | — | — |

---

## Layer: notes

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/notes/aggregated_bc_structures.md | hypothesis | aggregated BC structures | — | — |
| docs/notes/arw_dsgrn_dialogue_plan.md | note | ARW ↔ DSGRN dialogue plan | — | See Q16 in open_questions.md |
| docs/notes/arw_extended_Z_research_assignment.md | note | extended Z(π) research assignment | — | Links to advanced/extended_z_observable_necessity.md |
| docs/notes/arw_iva_research_assignment.md | note | IVA research assignment | — | Links to advanced/iva_z_geometry.md |
| docs/notes/arw_research_assignment.md | note | observable superiority validation assignment | — | — |
| docs/notes/arw_social_scope_research_assignment.md | note | social scope research assignment | — | Links CASE-20260315-SOC1 |
| docs/notes/bc_extraction_littman_metcalf.md | hypothesis | BC extraction — Littman-Metcalf method | — | Links to art_instantiations/arw_littman_bc_analysis.md |
| docs/notes/kuramoto_arw_notes.md | note | Kuramoto BC-perturbation study notes | — | — |
| docs/notes/kuramoto_bc_coupled_eps_comparison_report.md | note | BC-coupled epsilon comparison (Kuramoto) | — | — |
| docs/notes/literature_links.md | working-definition | literature links | — | — |
| docs/notes/methodological_lessons.md | note | methodological lessons (Kuramoto study) | — | — |
| docs/notes/open_questions.md | working-definition | active open research questions (Q1–Q16+) | — | **Canonical; add new questions here** |
| ~~docs/notes/open_questions_2026-03-18.md~~ | — | — | — | MOVED to archive/sessions/ 2026-03-29 (I-04) |
| ~~docs/notes/open_questions_session_2026-03-18.md~~ | — | — | — | MOVED to archive/sessions/ 2026-03-29 (I-04) |
| docs/advanced/operator_signatures_cross_domain.md | hypothesis | operator signatures across domains | — | MOVED from docs/notes/ 2026-03-29 (I-03) |
| docs/notes/repo_weakpoints.md | working-definition | repository weak points, systematic assessment | — | — |
| docs/notes/research_journal.md | working-definition | research journal (all sessions) | — | **Canonical; add new session findings here** |
| docs/notes/research_journal_session_2026-03-18.md | note | session 2026-03-18 research journal | — | Archived; merged into research_journal.md |
| docs/notes/social_bc_extraction_method.md | experiment-proposal | social BC extraction method | — | ART instantiation |
| docs/notes/validation_program_signatures.md | experiment-proposal | operator signatures validation program | — | — |

---

## Navigation Index

The existing `docs/INDEX.md` serves as human-facing navigation.
This file (DOC_INDEX.md) serves as the anti-pile-up registry — tracking canonical ownership
of concepts, supersession chains, and open issues. Both should be maintained together.
