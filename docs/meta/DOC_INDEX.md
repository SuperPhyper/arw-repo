---
status: working-definition
layer: docs/meta/
last_updated: 2026-08-04
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
| I-10 | 5 orphan docs not in index (`bc_signature_extraction_observables`, `bc_signature_persistence_and_dominance`, `CASE-20260329-0011`, `CASE-20260330-0012`, `audit_report_2026-06-02`) | Files on disk with no DOC_INDEX entry | Registered all five in their layer tables | 2026-06-24 |
| I-11 | `docs/meta/DOC_INDEX.md` itself | DUPLICATED SECTION — the closing "Navigation Index" block appeared twice, verbatim | Second copy removed | 2026-07-26 |
| I-16 | `cases/CASE-20260318-0004/cases/…` and `cases/CASE-20260315-0007/cases/…` | NESTED PATH ARTIFACT — byte-identical v1 transfer output written to a doubled path `cases/<id>/cases/<id>/transfer/` on 2026-06-02; the CASE-0004 copy held an unstamped duplicate of the withdrawn Φ = 0.9983 result | Files moved to `archive/cases/*_nested_path_artifact/`; emptied directories still need a manual `rm -r` | 2026-08-04 |
| I-15 | `cases/*/transfer/<comparison>/` (6 dirs) | UNMARKED SUPERSEDED OUTPUT — v1 transfer results sat beside v2 output with nothing indicating the v1 PCI defect | `SUPERSEDED_v1.md` stamp added to each, naming the defect, the superseding v2 run and the v1 values; withdrawal notice added to `archive/README.md` | 2026-08-04 |
| I-14 | `cases/CASE-20260315-0005/`, `cases/CASE-20260315-0007/` | DIVERGENT DUPLICATE ARTIFACTS — bare-name and `CASE-<id>_`-prefixed copies of ScopeSpec/BCManifest/CaseRecord, 111–297 diff lines apart, with nothing marking canonical status | March triples archived to `archive/cases/CASE-20260315-{0005,0007}_march_drafts/`; one-copy rule recorded in `archive/README.md` | 2026-08-04 |
| I-13 | `docs/meta/context_map/context_map_falsification_bc.md` | LAYER INVERSION — a derived `meta`-layer artifact was the fullest statement of the falsification schema, incl. Part VII V3.2 revisions reachable from nowhere else | Promoted `docs/core/falsification_schema.md` as source of truth; map marked `derived_from` it (v0.2) with a precedence banner | 2026-08-04 |
| I-12 | `Q-SL-*` (agent_sleep_scope.md) vs `Q-SLP-*` (sleep_as_perturbative_description_consolidation.md) | NEAR-COLLISION — two distinct question series on the sleep scope differing by one character; a prefix-level grep for `Q-SL` matches both | Not renamed (Q-SL-01–04 are cited elsewhere); recorded so a future ID sweep does not treat them as one series. If a third sleep-related series is ever needed, rename rather than extend. | 2026-07-26 |

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
| docs/glossary/observable_range.md | working-definition | observable range R(π), exclusion zone Z(π), F0, F-gradient, Z_cover, descriptive crossover, F1 topology-corrected | — | **Key doc for F0/F-gradient falsification**; updated 2026-04-29 |
| docs/glossary/perturbation_spread.md | definition | perturbation spread σ_Δ(x), pointwise stability, Lipschitz bound | — | Felder 2026 Def 4; formally names ε–Δ consistency condition; added 2026-04-29 |
| docs/glossary/partition.md | working-definition | partition, regime partition | — | — |
| docs/glossary/regime.md | working-definition | regime | — | — |
| docs/glossary/regime_partition.md | working-definition | regime partition (formal) | — | — |
| docs/glossary/resonance.md | working-definition | resonance (ARW definition) | — | Provisional term; note historical naming issues |
| docs/glossary/resonance_field.md | working-definition | resonance field | — | Provisional |
| docs/glossary/scope_dominance.md | working-definition | scope dominance | — | See also docs/core/scope_dominance.md |
| docs/glossary/scope_transition.md | working-definition | scope transition (glossary entry) | — | See also docs/core/scope_transition.md |
| docs/glossary/stability.md | working-definition | stability, regime stability | — | — |
| docs/glossary/state_space.md | working-definition | state space X | — | — |
| docs/glossary/scope_extended_definition.md | working-definition | scope as stable descriptive regime (not truth claim), observable admissibility as stability-grounded, time as observable, three foundational clarifications extending scope.md | — | Added 2026-05-01; extends but does not alter scope.md; depends on multi_scale_observables_and_latent_regime_formation.md |

---

## Layer: core

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/core/arw_scope_reduction_partition_criterion.md | working-definition | scope transition, admissible reduction, partition criterion | — | — |
| docs/core/basins_as_scope_partitions.md | working-definition | basins as scope partitions | — | — |
| docs/core/bc_classes_and_regime_generation.md | working-definition | BC classes and regime generation | — | Connects to bc_taxonomy/ |
| docs/core/cover_stability_criterion.md | working-definition | cover stability, ε-adjacency graph G_ε(O), observable cover C_ε, admissible resolution regime, Corollary 1 (Lipschitz), perturbation-stable cover | — | Felder 2026 foundational layer; added 2026-04-29 |
| docs/core/falsification_schema.md | working-definition | **falsification categories F0, F1, F1_BC, F2, F3, F4, F-gradient; Z_shared vs Z(π) vs Z_cover; decision order; pairwise discriminations; severity enum; ScopeSpec binding** | — | **Source of truth for the falsification schema.** Created 2026-08-04 (core-concept drift audit D-04): the fullest statement previously lived in `docs/meta/context_map/context_map_falsification_bc.md`, a derived artifact, which is now marked derived (v0.2) and re-rendered from this file. Carries the Part VII V3.2 revisions that existed only in the map: decision order F0→F4→F1→F3→F2→F-gradient, A6 split (invalid→F0 / unresolving→F1), claim-relative F1, χ mass criterion with τ_∂, and the "never lower ε" convention caveat. F1 stated as `ε ≥ ε*(O,X_B)` with the span shorthand scoped to connected images; F0 recorded as Π-relative. Open: Q_NEW_26 (χ computed nowhere) |
| docs/core/observable_information.md | working-definition | observable information (necessary condition), non-trivial Δ-stable cover, scope validity precondition | — | Closes Q4 (partial); added 2026-04-29 |
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
| docs/advanced/bc_signature_forward_derivation.md | claim | forward map operator structure → cover geometry; α=1/(β−1) theorem; β-exponent calculus (S5 lift +1, moment ×2); resolves Q-NEW-CROSS-2 (forward) | — | Forward complement of bc_signature_extraction_observables.md; keystone + β-rules numerically verified 2026-06-03 |
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
| docs/advanced/extended_z_observable_necessity.md | working-definition | extended Z(π), observable class necessity, multi-BC systems | — | Open questions renumbered Q-EXT-01–06 → Q-ZOBS-01–06 (2026-07-14, prefix collision with bc_signature_extraction_observables.md) |
| docs/advanced/h2_prime_theorem.md | working-definition | Theorem H2' — IVA dimensionality principle | — | — |
| docs/advanced/iva_z_geometry.md | working-definition | IVA, Z(π) geometry | — | — |
| docs/advanced/latent_degrees_of_freedom.md | claim | latent degrees of freedom, BC mapping, observable hierarchy | — | Still claim-level |
| docs/advanced/mathematical_scope_boundary.md | working-definition | mathematical scope boundaries, primitive operator bases | — | — |
| docs/advanced/minimal_operator_basis_arw.md | working-definition | minimal operator basis | — | — |
| docs/advanced/observable_consequences.md | claim | consequences of observable decomposition | — | Still claim-level |
| docs/advanced/observable_decomposition.md | claim | observable decomposition, pre-scopal substrates, BC mapping | — | Still claim-level; key for F0 |
| docs/advanced/observable_space_cover_height.md | working-definition | observable-space cover height, three-pattern diagnostic, Čech cover relationship | — | Promoted from hypothesis 2026-04-29; Felder 2026 relationship section added |
| docs/advanced/operator_signature_catalog.md | working-definition | operator signature catalog S1–S5 | — | — |
| docs/advanced/primitive_operator_time_coupling.md | working-definition | primitive operators, time coupling, emergent dynamic BCs | — | — |
| docs/advanced/quantum_operator_extension.md | open-question | quantum operator extension | — | Open question; speculative |
| docs/advanced/report_chi_observable.md | claim | χ = ∂r_ss/∂κ as fluctuation observable | — | Empirical; links CASE-0001 |
| docs/advanced/scope_completeness.md | working-definition | scope completeness, observable agreement | — | — |
| docs/advanced/arw_observable_complexity_landscape.md | note | observable complexity landscape, subscope density | — | MOVED from figures/ 2026-03-29 |
| docs/advanced/regime_graphs_arw.md | note | regime graphs, partition adjacency structure | — | MOVED from figures/ 2026-03-29 |
| docs/advanced/operator_signatures_cross_domain.md | hypothesis | operator signatures across domains | — | MOVED from docs/notes/ 2026-03-29 (I-03) |
| ~~docs/advanced/emergence/epsilon_induced_relational_emergence.md~~ | — | — | — | **DELETED 2026-03-29 (was duplicate of docs/advanced/epsilon_induced_relational_emergence.md — I-01)** |
| docs/advanced/multi_scale_observables_and_latent_regime_formation.md | hypothesis | multi-scale observables (micro/meso/macro), latent regime formation, aggregation as information loss, Z_cover inter-group variation, cover-collapse sequence | — | Added 2026-05-01; extends arw_emergence_bc_relative.md from 2-level to multi-scale; scientific basis for CASE-20260430-0013 |
| docs/advanced/multi_scale_sweep_protocol.md | note | multi-scale sweep protocol, single-pass sweep, grid density from G_max/ε, nesting hypothesis testability, cover height ordering | — | Added 2026-05-01; operational companion to multi_scale_observables_and_latent_regime_formation.md; depends on cover_height.md |
| docs/advanced/causality_as_directed_observable_structure.md | working-definition | causality as scope-relative directed observable coupling, asymmetric induction, Δ-stable causal structure, causal admissibility conditions | — | Added 2026-05-01; extends scope_extended_definition.md; causality as descriptive property, not primitive system feature |
| docs/advanced/invariance_as_scope_persistence.md | working-definition | invariance as scope-persistence, Noether/Einstein invariance in ARW context, Δ-stable partition, generalized invariance, scope-relative conservation | — | Added 2026-05-01; connects classical invariance theory to ARW; depends on causality_as_directed_observable_structure.md |
| docs/advanced/epistemic_ceilings_as_scope_saturation.md | working-definition | epistemic ceilings as scope saturation, cover exhaustion C_ε, three structural causes (Π-narrowness, ε-mismatch, Δ-excess), ceiling diagnosis and resolution | — | Added 2026-05-01; depends on invariance_as_scope_persistence.md + causality_as_directed_observable_structure.md |
| docs/advanced/arw_aggregation_limits_typological_observables.md | note | aggregation limits of typological observables, variance crossover problem, N* (crossover point), F1 at aggregation limit, Z_shared (heterogeneous scope), Aggregation Stability Measure (ASM), Variance Ratio Profile V(A), ecological fallacy as cross-level scope violation | — | General result; KHT used as illustration; applies to any discrete-type observable (MBTI, Big Five, institutional categories); added 2026-05-20 |
| docs/advanced/bc_signature_persistence_and_dominance.md | working-definition | generator signature (Σ̄_G, P_G^max) on observed family K_G, η = −log(ε/ε₀), persistence interval η_i, BC dominance, signature distance d_Σ (mean over K_A∪K_B) | — | Registered 2026-06-24 (was orphan, I-10); created 2026-05-30; §1/§6 updated 2026-07-17 (η↔ε₀ fixed, old d(Σ,Σ') similarity superseded by d_Σ per monograph VII V4.5/V4.7); Q-SIG-02–05 registered in open_questions 2026-07-17 |
| docs/advanced/bc_signature_extraction_observables.md | working-definition | bottom-up BC signature Σ extraction from observable data without model equations, complement to bc_extraction_method.md | — | Registered 2026-06-24 (was orphan, I-10); created 2026-05-30 |
| docs/advanced/qualitative_scope_signature_abstraction.md | hypothesis | QSA: qualitative BC-signature abstraction from prose descriptions (no sweep data), Ŝ tuple, signature-string matching as ε̂, label-matching trap, three-tier extraction ladder | — | Imported 2026-07-14 from Kaffeehaus session 2026-07-11; explicitly lowest evidentiary tier (hypothesis generation, not validation); registers Q-QSC-01/02; worked example: passive water management (R·D cluster vs Forcing fog harvesting); monograph home: Part VIII + VII V4.5 tier note |
| docs/advanced/framework_validation.md | superseded | hardness ladder (Weak/Medium/Strong validation grading), evidence ledger §2.1–2.6, hierarchical signature factorisation hypothesis (BC-class distance as coarsest transfer coordinate) | — | Imported 2026-07-11 (found by Rico in another chat, suspected stale); confirmed superseded: its §2.6/§3 "Strong (confirmed)" result for CASE-0004↔CASE-0001 (Φ=0.9983) contradicted by the repo's own transfer_v2 recomputation of the same pair (Φ=0.7794, `ambiguous_requires_inspection`, N_CONFOUND flag) — see warning banner in file; kept in full for historical record only; was an orphan (not in DOC_INDEX) before this import |

---

## Layer: bc_taxonomy

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/bc_taxonomy/bc_class_to_regime_type_map.md | working-definition | BC class → regime type mapping | — | — |
| docs/bc_taxonomy/boundary_condition_classes.md | working-definition | BC classes 1–6 (Coupling, Restriction, Forcing, Dissipation, Aggregation, Symmetry Breaking) | — | **Primary BC taxonomy reference** |
| docs/bc_taxonomy/partition_types.md | working-definition | partition types | — | — |
| docs/bc_taxonomy/transfer_distortion_metrics.md | working-definition | Φ (v2 decision score, clamped, w₄=0 default), θ̂*/TBS_norm, RCD, PCI (max-overlap directed), SDI (trivially collinear with RCD in 1D-sweep tier, WP-A4 amendment) | — | **Source of truth for transfer metrics**; v2 sync 2026-07-17 (TBS notation, PCI correspondence rule, SDI triviality, Φ rewritten, transfer_v2.py mapping); limitations: Q-REL-08 (TBS range), Q_NEW_25 (Δ-induced graph) |
| docs/bc_taxonomy/bc_failure_signatures.md | note | BC failure signatures, onset trajectories, F0/F-gradient/Z_shared by class, multi-BC masking | — | Informs Part V (monograph; Fehlermodi = Part V since plan v3 renumbering — fixed 2026-07-14); complements boundary_condition_classes.md |
| docs/bc_taxonomy/bc_relational_structure.md | hypothesis | BC classes as relation types, Restriction as meta-relation, Dissipation as temporal distinguishability, Forcing as inter-regime coupling, 5+1 taxonomy structure | — | Created 2026-05-30; formal companion to bc_bedrock_working_definition.md; informs Part IX §9.1 |
| docs/notes/c_components_derivation_attempt.md | note | derivation attempt: C components from embedded Restrictions, mapping analysis, gap identification | — | Created 2026-05-30; addresses Q-GEN-06; depends on bc_relational_structure.md + epistemic_context_and_functional_admissibility.md |

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
| docs/art_instantiations/generator_admissibility_taxonomy.md | art_instantiations | hypothesis | generator admissibility taxonomy, G=(Λ,Σ,φ,C), A(G), A_f(G\|C), A_h(G\|C), failure types I–III (domain-boundary / branch-selection / joint-constraint; formerly "Type I/II/III collapse", renamed 2026-07-17), signature-first generator inference | — | Core ART-layer generator formalism; depends on epistemic_context doc; Q-GEN-01–07 (05/06 registered late, 07 added 2026-07-17) |
| docs/art_instantiations/epistemic_context_and_functional_admissibility.md | art_instantiations | hypothesis | epistemic-operational context C, seven A_f criteria, compression viability κ, science as stability filter, time as compression axis | — | Formalizes C in G=(Λ,Σ,φ,C); Q-EPO-01–03 |
| docs/art_instantiations/example_unification_theories_as_generators.md | art_instantiations | note | quadratic gravity as generator, A_h vs A_f in unification theories, structural homologies with QG literature | — | Illustrative; literature-anchored (Stelle, Buccio et al., Piva, Edelstein et al.); not a physics claim |
| docs/art_instantiations/kht_architecture_index.md | working-definition | KHT Unified Architecture index, four-layer overview, layer summaries, causal direction | — | Entry point for KHT series; added 2026-05-20 |
| docs/art_instantiations/kht_architecture_layer1.md | working-definition | KHT Layer 1: Operator–Modulator space, 32 symmetric O×M combinations, Layer 1 distance metric, formal null model | — | Part of kht_unified_architecture; added 2026-05-20 |
| docs/art_instantiations/kht_architecture_layer2.md | working-definition | KHT Layer 2: Persistent profiles, biological BCs (Restriction + Dissipation), coverage criterion, 16 valid profiles, Ego/Shadow duality | — | Part of kht_unified_architecture; added 2026-05-20 |
| docs/art_instantiations/kht_architecture_layer3.md | working-definition | KHT Layer 3: Dynamic regime transitions, four regimes (R1–R4), control parameters (τ,σ,ξ), social dynamics, Layer 1 distance between regimes | — | Part of kht_unified_architecture; added 2026-05-20 |
| docs/art_instantiations/kht_architecture_layer4.md | working-definition | KHT Layer 4: AI context navigation simulation, computational instantiation of Layers 1–3, archetype library, regime simulator | — | Part of kht_unified_architecture; added 2026-05-20 |
| docs/art_instantiations/kht_arw_analysis.md | note | ARW analysis of KHT, BC class diagnosis (Restriction+Dissipation+Coupling+Forcing), observable candidates O1–O4, scope tuple S_KHT_L3, F-gradient/F1/F0 conditions, tractability assessment | — | Prerequisite for any KHT-based ART case; relates to CASE-SOC1 and CASE-0010; added 2026-05-20 |
| docs/art_instantiations/kht_operator_modulator_scope_signatures.md | note | KHT operators as observables (Π; GF(2)² over τ*/aperture, duality as parity), O3/O4 blindness → F0/F1/F-gradient, modulators as sequenced scope-operations (J/P→ε, I/E→Δ, T/F=permutation invariance), scope reconstruction S=(B,Π,Δ,ε) from KHT primitives | — | Bridge doc; consolidates external H2/H3 drafts; depends on kht_operator_modulator_design_refinement (pending import); measurability open; added 2026-06-27 |
| docs/art_instantiations/kht_state_notation.md | working-definition | KHT state notation |O,M,R,w,θ⟩, symmetry operators (D full dual, M̃ modulator inversion, P_op operator swap), Klein four-group V₄=Z₂×Z₂, four regimes as orbit of R1 under V₄, selection rules, scope-layered latent DoF, profile as symmetry-broken attractor, MBTI correspondence table | — | Part of kht_unified_architecture extended theory; depends on kht_architecture_layer1–3 + arw_quantization_partition_stability; added 2026-05-22 |
| docs/art_instantiations/kht_group_dynamics.md | hypothesis | KHT group dynamics, collective regime manifold Φ_G={(R_k,α_k)}, four collective regimes C-R1–C-R4, four stabilization mechanisms M1–M4 (Kuramoto coupling/external forcing/resonance/parameter shift), social phenomena as regime dynamics (polarization/groupthink/rigidity/innovation), κ_c as group-level N*, connection to CASE-20260328-0010 | — | Classical metastability only — explicitly NOT a quantum claim; depends on kht_state_notation + kht_arw_analysis; added 2026-05-22 |
| docs/art_instantiations/kht_applications_clinical_cognitive.md | hypothesis | KHT clinical/cognitive hypotheses H-A through H-E: attractor binding strength → regime stability, creativity as threshold-gated R3, masking as operator-stable modulator shift, therapeutic change as threshold recalibration (T1–T4 mechanisms), developmental trajectory → profile stability; cross-hypothesis dependency ordering; shared measurement prerequisites | — | No diagnostic claims; no pathologization; hypotheses are falsifiable, not validated; depends on kht_state_notation + kht_architecture_layer2–3; added 2026-05-22 |
| docs/art_instantiations/kht_doc_index.md | note | Session index for 14-doc KHT working cluster (Clusters A–D), reading order, key results per doc, dependency graph, repo layer assignments; companion to kht_architecture_index.md with broader scope | — | Covers extended set (state_notation, group_dynamics, applications, prescopal, ARW methodology) beyond 4-layer architecture index; added 2026-05-22 |
| docs/art_instantiations/kht_resonance_dialectic.md | hypothesis | KHT Resonance Dialectic, unification of three resonance senses (formal/admissibility/procedural), duality (V₄) as thesis–antithesis form, R3 mediation vs R4 collapse, maximin joint-admissibility criterion m*=argmax min(R(m,x_A),R(m,x_B)), discursive level (§6.3: ambiguity node as realization class, drift as structural cost, linkage over membership) | — | Synthesis node integrating glossary/resonance + resonance_dialectic_context_navigation + kht_architecture_layer3 §5.4; depends on kht_architecture_layer1/3, kht_state_notation, kht_group_dynamics; Q-RD-1–5; added 2026-06-29. **Extended 2026-07-25** with §6.3 from the Resonanzdialektik working thesis (uploaded by Rico), folded in as an extension rather than a new doc at Rico's direction — the name is established in KHT. Level discipline enforced in §6.3: its ARW-level claims are owned by scope_component_conflict_typology.md §8 (Q_NEW_E) and scale_gap_ambiguity_audit_stability.md §5, not by this file. Q-RD-1–4 were never registered in open_questions.md despite this row citing them since 2026-06-29 — corrected 2026-07-25, Q-RD-5 added. **Extended 2026-07-26**: §5 gains a two-readings table for the min (fairness over parties vs. robustness over generator hypotheses, Wald-type minimax under model uncertainty); §6.3 gains a sharpening box on claim (c) plus the argument why the discursive level splits the criterion — no facilitator exists there to verify a claimed inadmissibility; Q-RD-5 narrowed to the fairness axis, Q-RD-6 added for the robustness axis, orthogonal to Q-RD-1. The ARW-level part of this revision is owned by scope_component_conflict_typology.md §8.1 (Q_NEW_E, Q_NEW_F) |
| docs/art_instantiations/art_instantiation_lcc_nested_calibration.md | hypothesis | nested calibration (two-loop: lower=observables within fixed scope, upper=scope itself), calibration-obstruction typology, kinematics/dynamics factorization (ARW-level), cost-landscape topology, goal-metric construction, cooperation-will as boundary condition; low-carbon concrete (LCC) standard-update as worked instance | — | Imported 2026-06-24 from To-REPO; ART instantiation with one ARW-level contribution (§3); anchors to docs/notes/conflict_navigation_nested_calibration.md |

---

## Layer: cognitive_architecture

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/cognitive_architecture/anchor_memory.md | working-definition | anchor memory (cognitive arch.) | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/bc_taxonomy_cognitive_modes.md | working-definition | BC taxonomy and cognitive modes | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/context_navigation_ai.md | working-definition | context navigation AI system map | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/modal_cognition.md | working-definition | modal cognition | — | ⚠ See I-02: diverged copy also in context_navigation/ |
| docs/cognitive_architecture/agent_context_navigation_project_brief.md | superseded | existence test (vs confirmation test) for emergent low-dimensional mode structure, unlabeled salience, degrees-of-freedom surplus (anti-circularity), pre-registered evaluation, O3 read off from emergent geometry | — | Imported 2026-06-24 from To-REPO. **Superseded 2026-07-27** by `agent_context_navigation_project_brief_v2.md` (inference-direction correction); kept for the record, cite v2 |

---

## Layer: context_navigation

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/context_navigation/scope_constructing_agent_architecture.md | hypothesis | scope-constructing agent, learning target as description construction rather than mode selection, recapitulation operator e′ = ℛ(e; δB, δΠ, δε, δw) as distinct from experience replay, mode merge/split/prune in-phase, mode stability profile R_m(δ) and 𝒫_m, four levels of learning, intermediate modes m_{A/B}, multi-agent description packages D = (Σ, Π_required, F, T, c) and description migration τ | — | Added 2026-07-26 from a session sketch by Rico, filed at his direction as a **standing alternative formulation** rather than distributed as extensions — the reframing is held superior in its core idea. Does **not** supersede context_navigation_model_spec.md (working-definition) or agent_online_scope/agent_sleep_scope (operational specs); same alternative-formulation posture as sleep_as_perturbative_description_consolidation.md, with which it largely stands or falls. Carries an explicit superiority claim C-SCA (§1.2) and a three-arm + C0/C1/C2-ablation discriminating experiment (§14) reusing the emergent-modes labyrinth unchanged. §0 delimits against nine existing context-navigation files after a section-by-section comparison; §0.1 records two notation drift corrections from the sketch (Π/Δ transposed; an active observable O listed as a fifth tuple component) so they are not reintroduced. Cheap negative named first (§15): recapitulation is data augmentation, decided by the 𝒫_m width comparison with C1/C2 matched on gradient steps. Q-SCA-01–05 registered (prefix was unused). Multi-agent (§13) is new territory — no prior multi-agent material existed in context_navigation/ or cognitive_architecture/ |
| docs/cognitive_architecture/agent_context_navigation_project_brief_v2.md | experiment-proposal | existence test for emergent mode structure, BC-mismatch clause (agent and human are different scopes with different B), inference levels A/B/C, the inversion (a different geometry is a controlled BC-contrast, not a threat), unlabeled salience, degrees-of-freedom surplus incl. the interpretation door, axis-wise BC pre-classification | agent_context_navigation_project_brief.md (v1) | Imported 2026-07-27. The repo previously held only v1, which v2 supersedes — v1 short-circuited `BC_agent → geometry` and `BC_human → geometry KHT` via its three-outcome table and the commitment "run so that KHT can lose". Design sections unchanged; what changed is what the outcomes mean. The companion pre-registration (WP3) is deliberately **not** imported: its own freeze protocol makes import the act of freezing, and it is still `frozen: false` |
| docs/cognitive_architecture/planning_admissible_scope_agent_design.md | experiment-proposal | persistence layer (h_hat carried inside the agent, H_off and V_delta strictly outside), failure retrospective vs survival prospective, lexicographic selection (admissibility > prediction competence > hazard > switch cost), planning admissibility as a certified horizon, cover height transposed to the time index, coherence length as one quantity serving partition and survival, three-way projection tension as mode generator | — | Added 2026-07-29 from the 2026-07-22..29 simulation series (`Simulationen/labyrinth_scope_constructing/`, `Simulationen/kontextnavigation_minimal/`, both external). Revises the agent side of `agent_context_navigation_project_brief_v2.md`; does **not** supersede it — the existence test is untouched. Revision 3 already records the first measurement against its own named falsifier and it came back **negative**: rollout horizon 2–6 steps against an oracle-calibrated floor, and the hazard estimate adds nothing over the present residual (§8.1–8.2). §8.3 converts that into a quantified requirement on the next world rather than a repair of the estimator. Q-SCA-06a/b/c, 07, 08, 09, 10 registered. **Open request to a doc owner:** §2 level 4 demotes switch minimisation from a criterion to a tie-break — `docs/context_navigation/switch_minimization_criterion.md` must decide, and this doc is to be corrected if the demotion is refused |
| docs/notes/scope_constructing_agent_implementability.md | note | section-by-section confrontation of the scope-constructing architecture with the running labyrinth code; passive vs active recapitulation; δΠ bounded to masking a fixed observable set; failure signature must stay vector-valued; Φ not computable on an ε-axis behavioural sweep; §15's gradient-step matching does not apply to a library-only offline phase; D-1..D-7 build decisions | — | Imported 2026-07-27. Verdict: the agent side of the §14 arms is buildable, the *measurement* side is the blocker — neither Φ nor 𝒫_m width was computable in the WP1 setup, for the same reason (no graded BC axis). Also records that §0 of the architecture document cites spec sections (agent_online_scope §3, §4.1) that WP1 deliberately superseded |
| docs/context_navigation/switch_minimization_criterion.md | hypothesis | C-PAR: prefer descriptions requiring the fewest mode switches among those keeping navigation admissible; identification THETA_SAL = ε_agent, hence salience event = ε-exceedance of the σ_Δ proxy; three degenerate routes and their common name F1; lexicographic form (admissibility as hard filter) to avoid a fittable λ; the reward route excluded on measurement grounds; λ as agent-side BC sweep axis; parsimony belongs to consolidation, not to triggering | — | Imported 2026-07-27 from a session formulation by Rico. Claims the criterion is the *same* criterion as the offline persistence criterion of sleep_as_perturbative_description_consolidation.md §4, measured on a different axis (Q-PAR-02). Supplies the first mechanism in this programme that *predicts* the H1 mode count rather than hoping for it, on condition that λ is swept and N(λ) reported as a curve. Q-PAR-01–05 registered |
| docs/notes/kht_reconciliation_scope_constructing.md | note | how the scope-constructing build relates to KHT; contamination-route comparison (the old observation space contained three mode-shaped distance observables, the new one none); which WP3 criteria survive (E1 reformulable, E2/E3 not computable); axis-by-axis re-examination in which A1–A4 gain directness and A5/A9 move; operator/modulator correspondence and the limit it implies | — | Imported 2026-07-27. Central finding: the agent's ε, selector and λ are the structural analogues of KHT's modulators and are **exogenous**, so the current build runs one modulator cluster per run and can only find operator-side structure. Also records that under WP3's gates with substituted quantities the current data is Gate 0/1 — instrument changed, no reading. K-1..K-5 decisions |
| docs/notes/observable_information_and_bc_responsiveness.md | claim | C1: observable information is necessary but does not entail BC-responsiveness (self-reading observable as a counterexample class, demonstrated by construction); C2: stability-based selection *could* bias toward self-description — measured and found unsupported, retained as conjecture; C3 (measured): within-window selection criteria are structurally blind to between-BC level differences; the class of self-confirming selection criteria; F1_BC as a construction constraint and why an agent cannot apply it; failure-rate floor as necessary-not-sufficient lower bound, cross-encounter level contrast as the proxy the measurement calls for | — | Created 2026-07-27 after the scope-constructing agent's substrate-separation gate failed at r ≈ 1.0, **and substantially corrected the same day**: the original attribution to self-directed descriptions did not survive measurement (self-share 0.20–0.58 across conditions against a 0.31 chance level; the mixed condition where the gate is measured is 67% exteroceptive and fails identically). C2 downgraded, C3 added and measured (median composition separability |d| = 0.23; `cost_here`, the most diagnostic channel, absent because constant *within* each substrate). **Corrected a second time the same day**: the separation ratio the note was built around was found defective in three successive versions (circular / saturated / wrong grain); an audit banner now marks every separation figure in it as not load-bearing, and the agent turns out to navigate ~10× better than a random walker. C1, the composition-separability measurement behind C3, and the channel counts are independent of the ratio and untouched. All three versions kept visible. Filed as `claim` in notes rather than promoted to core/advanced. Cross-reference added to `docs/core/observable_information.md` (definition unchanged). Q_NEW_G registered — first ARW-level question to come out of the agent strand rather than the physical cases |
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
| docs/context_navigation/mode_scope_regime_audit.md | note | mode-scope-regime audit, terminological corrections post-audit, χ_mode (§2.6, added 2026-07-11) | — | Post-audit clarifications: modes as regimes, salience as fluctuation observable, consolidation as asymptotic process; §2.6 adds formal χ_mode derivation (R⁴·A·Approx) + local-max estimator χ_mode^LM (Q-CNS-06 partial resolution, distinct from the 2026-03-29 mode-switch-rate candidate) |
| docs/context_navigation/transfer_semantics_context_navigation.md | working-definition | Φ as observable transfer (not system transfer), three transfer experiment types for labyrinth | — | Transfer protocol for context navigation; Φ reporting requirements |
| docs/context_navigation/context_navigation_emergent_modes_experiment.md | experiment-proposal | emergent modes experiment, ARW as observation instrument, unstructured policy regime analysis | — | Complementary to designed modes experiment; H1–H4; references experiments/labyrinth_experiment_agenda.md |
| docs/context_navigation/context_navigation_scope_spec_emergent.md | working-definition | S_emergent scope, action_dist observable, emergent regime partition, R(action_dist), Z(action_dist) | — | Scope companion to context_navigation_emergent_modes_experiment.md; distinct from context_navigation_scope_spec.md |
| docs/context_navigation/agent_online_scope.md | working-definition | S_online scope, perception observable set (7 observables), hard-gate archetype matching (partitioned by saliency type, no fallback), w_in/w_out first-class protocol fields, gradient_pct saliency strength, ε_stab | — | One of three scopes in three-scope architecture; S_online ≠ S_emergent; ε_stab ≠ ARW ε; contact_onset deferred from minimal saliency set |
| docs/context_navigation/agent_sleep_scope.md | working-definition | S_sleep scope, archetype library (partitioned by saliency type), winner-takes-place revision, unconditional promotion for no-match, progress_rate as sole evaluation observable, Π_evaluation | — | Agent-internal offline phase; no EMA, no capacity limit in minimal version; complements S_online; distinct from S_observer |
| docs/context_navigation/arw_observer_scope.md | working-definition | S_observer scope, saliency-bounded encounter windows (not zone windows), Π_behavior (action_dist Layer 1; saliency_type_dist/progress_rate_obs/regime_persistence Layer 2), Z_shared(S_observer), subscope reconstruction from archetype w_in, ε-sweep with N as finding | — | External ARW measurement scope; refines S_emergent (see §5); N is a finding not a target; zone alignment explicitly secondary |

---

## Layer: experiments

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| experiments/labyrinth_three_scope_minimal_setup.md | experiment-proposal | minimal three-scope experiment, 9×9 labyrinth, encounter-window segmentation, Python pseudocode for S_online/S_sleep/S_observer, winner-takes-place revision, 5-step correspondence analysis, hyperparameter table | — | Execution-oriented; covers Phase 0–2 (3-phase checklist); starting position randomized in Zone R; zone structure is scaffold not object of study |
| experiments/labyrinth_patch_op_mod_split.md | proposal | S_online operator/modulator weight split, w_op (5-dim content observables), w_mod (2-dim context observables), saliency-trigger-driven modulator update, archetype library as content-attention profiles | — | Patch to labyrinth_three_scope_minimal_setup.md; motivated by KHT Layer 4 operator/modulator distinction; scope: S_online internals only; added 2026-05-20 |
| experiments/sigma_extraction_kuramoto_noise.md | experiment-proposal | Σ extraction under noise, K1 noisy-Kuramoto scenario, discriminant robustness predictions | — | Registered 2026-07-14 (was orphan); addresses Q-EXT-01/02, Q-SIG-02 |
| experiments/sigma_extraction_bc_signatures.md | working-draft | first empirical Σ-extraction results, three discriminants (profile type, ε_merge/span, h_asym), Coupling vs Restriction separation | — | Imported 2026-07-14 from monograph workspace (was book-side orphan); addresses Q-EXT-01/02; results feed monograph Part VI §6.4 material |
| experiments/sigma_extraction_validation_plan.md | working-plan | 4-level Σ-extraction validation programme (intra-class consistency, observable dependence, noise, blind test) | — | Imported 2026-07-14 from monograph workspace; Level-1 expectations to be re-derived against bc_signature_forward_derivation.md β-calculus (cross-ref added on import) |
| experiments/spring_mass_chain/ (scripts) | — | spring_mass_sweep.py + spring_mass_cover.py — simulation and cover analysis for CASE-20260430-0013 | — | Python scripts; not indexed as docs. See experiments/spring_mass_chain/README.md and cases/CASE-20260430-0013/ |
| experiments/labyrinth_calibration/ (scripts) | — | calibrate_scope.py — scope calibration (Q1) and training convergence (Q2) for CASE-20260330-0012 labyrinth | — | Python script; not indexed as docs. See experiments/labyrinth_calibration/README.md |

**Case: CASE-20260430-0013** (Vertical Spring-Mass Chain, multi-scale observable scope; pre-pipeline)
- `cases/CASE-20260430-0013/ScopeSpec_signature_first.md` — active ScopeSpec v3 (supersedes pendulum drafts v1/v2)
- `cases/CASE-20260430-0013/consistency_check.md` — pre-ScopeSpec physical model verification
- `archive/cases/CASE-20260430-0013_pendulum_drafts/` — v1 and v2 pendulum ScopeSpec drafts (superseded)

---

## Layer: related_fields

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/related_fields/related_fields_and_methodological_connections.md | working-definition | related fields, methodological connections | — | — |
| docs/related_fields/j_space_arw_signature_hypothesis.md | note | J-Space (Anthropic, July 2026) as regime-occupancy signature p(R_i\|context), not static representation geometry; χ_mode^J prediction | — | Imported 2026-07-11 from To-REPO; depends on mode_scope_regime_audit.md §2.6; registers Q-REL-06/07 (renumbered from a Q-REL-01/02 collision with bc_relational_structure.md) |

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
| docs/cases/CASE-20260329-0011.md | working-definition | case motivation — Labyrinth agent Phase 1 (mode emergence, uniform Zone A) | — | Registered 2026-06-24 (was orphan, I-10); links cases/CASE-20260329-0011/ |
| docs/cases/CASE-20260330-0012.md | experiment-proposal | case motivation — Labyrinth agent emergent modes (unstructured policy, ARW as observer) | — | Registered 2026-06-24 (was orphan, I-10); links cases/CASE-20260330-0012/ |

---

## Layer: meta

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/meta/LLM_CONTRIBUTION_CHARTER.md | working-definition | LLM contribution rules, repo governance | — | **Mandatory reading for LLM contributors** |
| docs/meta/audit_report_2026-03-15.md | note | audit findings 2026-03-15 | — | Historical; not updated after that date |
| docs/meta/audit_report_2026-06-02.md | note | audit findings 2026-06-02 (E_sep bug-fix propagation, gradient-proxy scope correction) | — | Registered 2026-06-24 (was orphan, I-10); historical |
| docs/meta/llm_memory_map.md | note | LLM memory map | — | — |
| docs/meta/maintenance_checklist.md | working-definition | periodic repo maintenance checklist | — | Created 2026-03-29 |
| docs/meta/repo_design.md | working-definition | repository design principles | — | — |
| docs/meta/context_map/context_map_framework.md | working-definition | context map schema, scope tuple objects, cover objects, observable objects, partition objects, differential diagnosis index | — | Agent-optimised navigation; machine-readable notation; read before other context_map files |
| docs/meta/context_map/context_map_falsification_bc.md | working-definition | falsification entries (F0–F4, F-gradient, Z_shared), falsification decision tree, BC taxonomy (6 classes), operator signatures S1–S5, observable BC structure notation | — | Agent-optimised; companion to context_map_framework.md |
| docs/meta/context_map/context_map_pipeline.md | working-definition | pipeline DAG, all 11 pipeline modules (incl. stability_mask.py as planned), all 7 artifact types, case directory anatomy, guard rules GUARD-1–9 | — | Agent-optimised; stability_mask.py marked PLANNED (action E-1) |
| docs/meta/context_map/context_map_transfer_emergence_cases.md | working-definition | transfer metrics (Phi, RCD, TBS_norm, PCI, SDI), emergence window analysis, all 14 case entries (4 active + 10 pending), assembled context_map.yaml (exemplary) | — | Agent-optimised; corrected from v0.1 (SIR BC class, case IDs, missing cases 0011/0012/0013); v0.2 2026-05-10 |

---

## Layer: notes

| File path | Status | Canonical concept(s) | Supersedes | Notes |
|---|---|---|---|---|
| docs/notes/aggregated_bc_structures.md | hypothesis | aggregated BC structures | — | — |
| docs/notes/scope_component_conflict_typology.md | note | scope-tuple conflict typology (ε/Δ/Π/B-conflict classification of controversies), Π-monopolization as fifth orthogonal conflict mode, linkage-over-shared-Π as a case the typology cannot place (§8) | — | Imported 2026-07-11 from To-REPO (Kaffeehaus session 2026-07-04); used the more complete of two offline-reconstructed variants (base duplicate discarded, see maintenance note in file); registers Q_NEW_A–E. **§8 added 2026-07-25** from the Resonanzdialektik thesis: same B/Π/Δ/ε, no monopolization, difference located in the linkage over Π — invisible to a tuple-component typology by construction, since S has no slot for relational structure among observables. Candidate homes Σ (generator) or the Q_NEW_25 transition graph; cheap negative outcome (B-conflict in disguise) named first. Bears on Q_NEW_C. **§8.1 added 2026-07-26** (stability revision, on Rico's correction that varying background assumptions yield differently *stable* projections independent of factual correctness): linkage = co-stability profile induced by a generator hypothesis, since σ_Δ is tuple-internal only for pure state functions and the repo's observables are asymptotic; computable as a graph over Π weighted by overlap of X_stab(π) = {x : σ_Δ^π(x) < ε}; selects Σ over the Q_NEW_25 graph without routing through S1–S5. Sharper claim: the typology does not fail to place such a case, it misplaces it in the Δ-conflict row — registered as Q_NEW_F, with the §1 Δ-row given a caveat. Revised cheap negative: Δ-conflict in disguise, not B-conflict. Same-day reconciliation with the three notes imported 2026-07-26: §8.1 gains a Downstream paragraph (consumed by communicative_branching_points_nuclear_discourse.md §5 / Q-COM-02, previously a one-way reference) and an Adjacent paragraph recording that §8.1, the aesthetics note §3 and the sleep note §4 identify three independent sources of σ_Δ variation (Δ, environment, generator) of which only the third is tuple-invisible — kept here rather than spun out as a fourth note |
| docs/notes/cross_scope_causal_construction.md | note | cross-scope causal construction, level-shift detector (4 markers), three-part construction for legitimate cross-scope causal claims, undecidability of generator identity | — | Imported 2026-07-11 from To-REPO; depends on scope_component_conflict_typology.md |
| docs/notes/shared_term_reflex_check.md | note | shared-term reflex check (same-B/same-Π two-question heuristic), lightweight front-end to the conflict typology and causal-construction note | — | Imported 2026-07-11 from To-REPO; depends on both preceding notes |
| docs/notes/conflict_navigation_nested_calibration.md | note | conflict navigation as nested scope/observable calibration, two calibration loops on separated timescales (lower=observables, upper=scope), incentive erosion / fall-out precursor | — | Imported 2026-06-24 from To-REPO; exploratory generalization from calibration case toward conflict case; anchor for art_instantiation_lcc_nested_calibration.md |
| docs/notes/facilitation_toolkit_tuning_or_framing.md | note | tuning vs framing distinction for multi-stakeholder sessions, two-loops/two-clocks (inner live calibration vs outer reframing), shared-frame vs shared-will diagnosis, participation incentive (locally negotiable for each), path-step sizing, full facilitator toolkit (checklists/templates) | — | Imported 2026-06-24 from To-REPO; expanded 2026-06-29 to merged field-guide-and-toolkit (Part I/II/III), superseding earlier 164-line v2 in place; design-guide/in-room-guide split of same spine subsumed, not imported separately; informal practitioner companion (not a formal definition) |
| docs/notes/facilitation_between_the_sessions.md | note | the slow loop (outer-loop) work for multi-stakeholder facilitation, three-pass branch structure (A stayed Tuning / B became Framing / C hit the wall), loop separation discipline, representation gate, handoff hinge | — | Imported 2026-06-29 from To-REPO; companion to facilitation_toolkit_tuning_or_framing.md (operationalizes its §2/§5 between-session references) |
| docs/notes/facilitation_crystallize_the_friction.md | note | friction-surfacing for contested frames, collide-not-cluster, naming oppositions both sides own, friction diagnosis typology (missing piece / uneven leverage / no overlap), local compromise at the friction point, structural-opposition as second output | — | Imported 2026-06-29 from To-REPO; companion to facilitation_toolkit_tuning_or_framing.md (operationalizes its §5 "build the shared question"); invoked by Branch B of facilitation_between_the_sessions.md |
| docs/notes/kht_operator_modulator_design_refinement.md | note | constituting basis τ*(=S/N)+aperture(=data class), GF(2)² with perception duality as parity, sequenced modulators, I/E=Bezug vs aperture=Datentyp, Type as context-local aggregation limit (WTA local / distribution global), branched-flow arm generation, V₄ as medium symmetry | — | Imported 2026-06-24 from To-REPO; consolidated design pass v4 over kht_architecture_layer1.md; Q-KHT-OM-1..9 |
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
| docs/notes/scope_failure_and_ontological_projection.md | note | scope failure as ontological projection, projection error at admissibility boundary, ARW as projection filter, implicit boundary enabling model overreach | — | Added 2026-05-09; depends on F-schema, A_f/A_h, epistemic_ceilings, causality docs; Q-PROJ-01 registered |
| docs/notes/arw_economic_regime_hypothesis.md | hypothesis | labor-capital coupling, Q indicator (K/G), economic regime stability, Q* threshold, H-ECON-01, automation as Dissipation BC, deregulation as Restriction BC removal, collective bargaining as Coupling BC | — | Added 2026-05-13; qualitative grounding 2026-05-08; candidate for ART instantiation; falsification conditions F-ECON-01–04; path to formalization in §8 |
| docs/cognitive_architecture/simulation_revision_design_notes.md | note | labyrinth simulation revision, archetype library, local admissible policies, environment classes as substrate filters, scope-admissibility, F0-type transitions in RL context, policy separation requirement | — | Added 2026-05-13; design notes for CASE-0011/0012 simulation revision; environments as admissibility filters; archetype as persistent local admissibility structure |
| docs/notes/arw_quantization_partition_stability.md | note | quantization as scope-relative partition stability, discrete descriptions as stable partitions under Δ at ε, four conditions for quantization, condensed/dilute matter phase transition analogy (Ω order parameter, N* as T_c), formal embedding of QM via spectral theorem + cover height, superposition as F-gradient, entanglement as Z_shared, latent degrees of freedom (L1 Δ-averaging, L2 ε-blindness, L3 B-inadmissibility), descriptive collapse X→π(X_B), EFT as systematic latency management, SSB as latency inversion, unification across physics/biology/psychology | — | Domain-neutral; §3.4 adds phase-transition framing (order parameter Ω, coupling density); §3.5 adds formal QM embedding (spectral theorem, Born rule/unitarity/linearity outside embedding); §3.6 adds latent DoF framework + descriptive collapse (974 lines); updated 2026-05-22 to 974-line canonical version |
| docs/notes/kht_prescopal_substrate_hypotheses.md | hypothesis | KHT pre-scopal biological substrate hypotheses, operator independence (Ni/Si/Ne/Se), candidate neural substrates, dissociation evidence, reverse inference caveat, H1–H5 testable hypotheses | — | Part of kht_unified_architecture; explicitly hypothesis-grade; generates empirical questions, does not assert neurobiological facts; added 2026-05-20 |
| docs/notes/scope_family_flow_and_kuramoto_limit_audit.md | note | ε-induced scope family flow structure (𝒮_α(b) directed/net limit, Q-INV-03 resolved), δ-collapse vs. N→∞ Emergent-Aggregation limit identity (Q-INV-04, open), RG-universality parked as external discussion anchor | — | Imported 2026-07-11 from To-REPO; fixed a depends_on path error (aggregated_bc_structures.md is at docs/notes/, not docs/advanced/); annotates Q-INV-02 in invariance_as_scope_persistence.md |
| docs/notes/arw_theory_audit_2026-06-10.md | note | Adversarial audit of ARW theory + monograph drafts: refuted separatrix/secondary-ridge narrative (A1), defective v1 transfer metric (A2), invalidated gradient-peak method (A3), SDI definition drift (A4), plus Tier 2–4 findings (taxonomy-completeness overclaim, BC-class discriminability, scope-tuple gaps, falsifiability/novelty attack surfaces) | — | Imported 2026-07-11 (uploaded by Rico); companion to arw_audit_repair_plan_2026-06-10.md; monograph content itself (Parts I–IX) not present in this repo |
| docs/notes/arw_audit_repair_plan_2026-06-10.md | note | Work-package plan (WP-A1–A4, B1–B4, C1–C10, D1–D4, E1–E4, F1–F5) converting the audit into executable repairs; sequencing/gates R1–R5 | — | Imported 2026-07-11 (uploaded by Rico); companion to arw_theory_audit_2026-06-10.md; on import, confirmed WP-B1/B2 executed and WP-A4's decision executed in repo docs but its staged skill-patch was never merged (fixed directly in arw-repo-context skill this session instead); flags an unreconciled duplicate WP-A3 decision record (this plan says settled 2026-06-10, a separate decision note restates it 2026-07-02) |
| docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md | note | WP-A3 decision: partition-level transfer metrics (Φ, RCD, TBS_norm, PCI, SDI) are a necessary-not-sufficient filter, not a verdict; structural transfer must be grounded in Σ (operator signatures S1–S5); proposes WP-A5 (SignatureTransfer.json, two-stage transfer workflow) | — | Imported 2026-07-11 from To-REPO (decided 2026-07-02); companions arw_theory_audit_2026-06-10.md / arw_audit_repair_plan_2026-06-10.md located and imported same session (uploaded by Rico); framework_validation.md / monograph Part VI–IX still not found in this repo or Simulationen; triggered the Q-REL-05 reformulation below; possible duplicate of the "SETTLED 2026-06-10" WP-A3 record in arw_audit_repair_plan_2026-06-10.md — unreconciled, flagged for Rico |
| docs/notes/transfer_deflation_and_abstraction_chains.md | note | transfer deflation, coarse-graining as relation between two descriptions, abstraction chain, domain-agnosticism as consequence, necessity locus (Q_NEW_27) | — | Imported 2026-07-18 from monograph workspace (written 2026-07-02); feeds monograph Part IX §9.2.5/§9.4; §6 registration executed on import (Q_NEW_27) |
| docs/notes/inductive_strengthening_cascade_closure.md | note | inductive strengthening, cascade closure, ε-cascade as scope family {S_ρ}, vertical (resolution-axis) transfer as distinct from horizontal Φ-transfer, strengthening as third repair move beside scope reduction and observable replacement, projective-load cost | — | Imported 2026-07-25 (drafted offline, uploaded by Rico); import as a pair with scale_gap_ambiguity_audit_stability.md; Kakeya/Wang–Zahl cited as literature anchor only, not an ART case; Q-STR-01–03 registered on import (prefix was unused); notation guard added — ρ is canonical ε, not a fifth tuple component |
| docs/notes/scale_gap_ambiguity_audit_stability.md | note | scale-gap ambiguity, realization class Real(C; ρ₁→ρ₂), ambiguity measure Amb as d_Π-diameter, audit stability, strengthening refusal as costly signal, distinction from Goodhart-type proxy failure, shared-term instance (§5, added same day) | — | Imported 2026-07-25 (drafted offline, uploaded by Rico); companion to inductive_strengthening_cascade_closure.md, consumes its definitions; Q-STR-04–06 registered on import; checked against arw_aggregation_limits_typological_observables.md — N* is a variance crossover, not a realization-class diameter, so the conjectured bound is recorded in Q-STR-06 rather than cross-referenced as settled |
| docs/context_navigation/sleep_as_perturbative_description_consolidation.md | context_navigation | hypothesis | sleep as falsification rather than optimization, replay as Δ-perturbation, persistence as existence condition of a description, preference as online persistence estimate, consolidation-cycle ordering axis, σ_Δ(D) < ε as consolidation criterion | — | Imported 2026-07-26 from To-REPO (drafted offline in German, translated on import); companion to agent_sleep_scope.md, does **not** supersede it — the two consolidation rules are experimentally separable (§9); Q-SLP-01–03 registered on import (distinct from the pre-existing Q-SL-01–04 in agent_sleep_scope.md — near-collision, see I-12) |
| docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md | notes | note | scope-relative beauty, environment as Δ-constraint, architecture as externalized description system, aesthetic preference feedback loop, monumentality as visible persistent cooperation | — | Imported 2026-07-26 from To-REPO (drafted offline, already English); kept at `note` deliberately — §9 records why the claim is not yet falsifiable (post-hoc scope attribution; competing fluency/familiarity accounts not excluded); Q-AES-01–02 registered on import |
| docs/notes/communicative_branching_points_nuclear_discourse.md | notes | note | communicative branching point, communication as cartography (orientation vs. persuasion), discourse displacement as effect observable, latent-assumption-network risk at the discursive level | — | Imported 2026-07-26 from To-REPO (drafted offline in German, translated on import; byte-identical `-2` duplicate not separately imported); renamed from repo_note_kommunikationsstrategie_nuklearia_2026-07-26.md; **not** a second home for the branching-point claim — §0 delimits it against kht_resonance_dialectic.md §6.3 and scope_component_conflict_typology.md §8/§8.1 (Q_NEW_E/F), and Q-COM-01 is the check that would merge it back; §6 literature-gap claim is unverified session recollection |
| docs/notes/minds_generalization_beyond_facilitation.md | note | MINDS as viability-preserving scope-navigation protocol for coupled systems with partial descriptions, facilitation as first instantiation (not the toolkit itself), non-human parties (models/datasets/services/goals/institutions/time horizons/motifs), 5 transfer conditions + negative condition (classical optimization suffices), 10 candidate instantiations (multi-agent meta-controller, ontology merging, software architecture, production systems, model integration, legislation, knowledge retention, ecology [modular only], personal time horizons, artistic synthesis), Synthesis Test as maximin over worst-represented necessary component | — | Added 2026-07-31 from Kaffeehaus session; abstraction over the facilitation cluster (facilitation_toolkit_tuning_or_framing.md and companions — does **not** supersede them); maximin criterion remains owned by kht_resonance_dialectic.md, this note only extends its candidate reference class (Q-RD-6 territory); registers Q-MINDS-01–04 (prefix collision-checked, free); source toolkit: MINDS v0.8 draft, art-of-resonance.org |

| docs/notes/total_description_space.md | notes | superseded | total description space D(S), scope parameter space, cover construction as one construction over four directions (state/sweep-path/resolution/Δ), falsification categories as degeneracy types, no-complete-invariant anchor (Carlsson–Zomorodian 2009) | superseded by docs/notes/scope_fibration.md | Added 2026-08-01 from monograph exploration session (intro strong-claims gap); extends partially-resolved Q4 (ARW↔TDA, observable_information.md); delimited against semantic description-spaces cluster (Q_NEW_E/F, Q-RD-5/6); preserves Part VII V1 graph-vs-cover precision; registers Q-DSP-01–04 (prefix collision-checked, free); candidate rename if collision emerges: scope fibration  Superseded same day (2026-08-01) after external review — see successor row. |

| docs/notes/scope_fibration.md | notes | hypothesis | scope fibration D(S), four morphism types (ε-coarsening, Δ-stability action, π-observable change, B-restriction), path vs candidate-comparison-functor distinction for transfer (functor = target status, current: structure-preserving translation), five-level architectural hierarchy (cover construction fundamental; category language and persistence theory explicitly non-foundational), falsification categories as obstructions to local triviality, 2σ̄-interleaving / exact commutativity on ε-plateaus (Q-DSP-01 paper part), no-complete-invariant anchor (Carlsson–Zomorodian 2009) | docs/notes/total_description_space.md | Added 2026-08-01; rename + extension after external review; categorical vocabulary adopted as language only (conservativity = Q-DSP-05); go_nogo ε-plateau criterion identified as local-triviality condition of the (ε,Δ)-plane; Q-DSP-01 partially answered, Q-DSP-05 registered; promoted note→hypothesis 2026-08-01 after 4 empirical runs (plateau-interior strictness 20/20 on declared-Δ 1D rerun; blind reconstruction works; diagnostic surplus over σ_Δ NOT shown — instrumental claim bounded) |

| docs/notes/evaluating_descriptions_not_authors.md | notes | note | description-centric evaluation, eight dimensions of descriptive quality (gain, compression, explicit scope, operationality, falsifiability, transferability, generativity, robustness), production→evaluation bottleneck shift under AI, dimension→ARW operationalization map (5 of 8 direct/partial), self-application guard (symmetry; Goodhart-type dimension gaming) | — | Added 2026-08-03 from Rico's concept note; programmatic, not a definition; §7 guard makes the note conditional on ARW scoring itself publicly (links ews_discriminator_test_protocol.md); §8 literature delimitation unverified; registers Q-EVAL-01–02 (prefix collision-checked, free); monograph integration deliberately deferred (Part IX revision) |

| docs/notes/ews_discriminator_test_protocol.md | notes | experiment-proposal | EWS discriminator test, observable-relative alarm classification (F0/F-gradient vs genuine transition), cross-observable coherence rule, preregistered criteria with labelled positive+negative from one apparatus (Cascade Peter/Paul lakes 2008–2011), baselines B1–B4 incl. plain σ_Δ and multivariate EWS; partial time blinding (common random offset, limits stated); structured observable admission table; forced pre-unblinding prediction sheet; audit trail + SHA-256 freeze + git tag cascade_prereg_v1 | — | Added 2026-08-01 in response to the 'claims plausible but insufficiently supported' assessment; written before data access so criteria cannot drift; delimited against multivariate EWS (aggregation increases power, ARW reads disagreement); carries the run-4 lesson forward (H2 exists to catch 'localises correctly but adds nothing'); Q-EWS-01–03 to be registered on execution (prefix collision-checked, free) |

| docs/notes/ews_stage1_review_epsilon_vs_delta.md | notes | note | three-way separation ε_instr ≠ ε_operational ≠ Δ; manufacturer specs constrain the instrument component of ε only (mapping rule required: truth-referenced vs pairwise, reading-dependent ε(x)); pH standardization circularity (raw units only); Δ as modelling commitment with declared family Δ_min⊆…⊆Δ_max and required verdict stability; bias direction conditional on inclusion-monotone σ_Δ (canonical sup-form qualifies); chlorophyll F0 for Π_abs only, Π_rel conceptually admissible with ε unresolved; power: degeneration to pairwise unanimity + DO/pH share measurement infrastructure (not independent error channels) | — | Added 2026-08-04, revised same day after review round 5. Upholds the Stage-1 stop, replaces its reason. Registers Q-EWS-04, Q-EWS-05. Flags epsilon_and_scope_resolution.md + perturbation_spread.md as simulation-native for BOTH ε and Δ. Blinded CSVs not opened. |

| docs/notes/arw_core_concept_drift_audit_2026-08-04.md | notes | note | core-concept drift audit (D-01–D-15) across scope tuple, falsification schema, σ_Δ/ε regime, observable analysis, BC taxonomy, transfer metrics, pipeline; doc↔code interface as the main drift locus; five corrections applied in-place; five decisions requested (F1 shorthand, F-schema home, duplicate case YAMLs, v1 transfer output, skill refresh) | — | Added 2026-08-04. Narrower mandate than arw_theory_audit_2026-06-10.md (one-thing-per-concept + currency, not defensibility); confirms WP-A4/B1/B2 executed. Key findings: D-05 canon pointed at the unimplemented `pipeline/stability_mask.py` while `epsilon_kappa_map.py::compute_sigma_delta_windowed` has computed direct σ_Δ since 2026-06-02 (fixed); D-11 `transfer_distortion_metrics.md` self-contradiction on SDI (fixed); D-13 `arw-repo-context` skill still carries the WP-A4-rejected SDI definition (skill layer, not fixed here); D-09 CASE-0005/0007 are pipeline-run `go` cases, so audit-B2's "zero validated cases" for Dissipation/Aggregation is superseded; D-10 divergent duplicate YAML triples in both cases. Monograph drafts not in this repo, not audited. **All five decisions settled by Rico 2026-08-04 and executed the same day** (§9 execution notes): F1 shorthand option (b), falsification schema promoted to `docs/core/`, March triples archived, v1 transfer dirs stamped, both skills refreshed. Execution surfaced D-16 (nested-path duplicate transfer output, I-16). |

| docs/notes/description_atlas_programme.md | notes | experiment-proposal | description atlas as the form of the Vollraum (charts + transition data + obstructions, forced by the no-complete-invariant argument); chart = parameter region with constant fiber = validity condition as the sciences already state it; payoff in transition data not chart reproduction; registered prediction P-ATLAS (no surplus inside charts, surplus only at boundaries — inside half already fired via run 4); obstruction types M/T/R with T (monodromy) and R (no common refinement) absent from the schema; preregistered 8-case chart list (Knudsen, Born–Oppenheimer/conical intersections, ensemble inequivalence, Ginzburg, harmonic, geometrical optics, Markov, rigid-body) | — | Added 2026-08-04. Reframes the correspondence strategy as atlas construction, not validation-by-borrowing. Intra-system (paths, not functors) — hence Q-REL-05 does not bite. Guards: derivation before literature lookup, mandatory surplus prediction per case, full reporting, ARW/ART level discipline. Registers Q-DSP-06/07 plus §9 end conditions. |

| docs/notes/general_regime_construction.md | notes | hypothesis | general (dimension-free) regime construction with Δ-reachability as the admissible-transition relation; 1D sweep as degenerate special case; two defects of the 1D operative form (cover degenerates to increment thresholding — sorites/transitivity argument vacuous on a path graph; adjacency 'consecutive in sweep' is undeclared, outside the scope tuple); codimension argument (1D generically blind to structure of codim ≥ 2, hence to conical-intersection-type point defects); table of what becomes definable at dim ≥ 2; schema breakage (θ* scalar → boundary set, sweep_range, TBS_norm has no general form); **ε as a declared family** (§2.2–2.4): three multiplicities separated (per-observable ε_i, per-point ε_i(x), resolution family — only the last was sound), Rule A joint graph vs Rule B common refinement (coincide in 1D, diverge in general — Rule-B classes need not be connected), commensurability/normalisation requirement, and the finding that epsilon_multi_observable.py sweeps only the diagonal ε₁=ε₂ and leaves its own docstring question unanswered while its CASE-0003 output already records agreement_rate 0.367 | — | Added 2026-08-04 on Rico's directive to argue and later test beyond 1D. Partially answers Q_NEW_25; prerequisite for Q-DSP-07 (type-T); sharpens Q-REL-05/08; registers Q-EPS-01/02/03. Notes doc↔code divergence: cover_stability_criterion.md defines G_ε over ALL pairs, scope.md operative form over consecutive samples only. Existing 2D assets in Simulationen are grid-derived, not Δ-derived. CASE-20260430-0013 registered 2D, never run. |

| docs/notes/validation_strategy_v2.md | notes | experiment-proposal | successor validation strategy (v1 = implicit case/1D-sweep/go_nogo/Φ practice, never declared); role change of 1D cases from evidence to frozen regression suite (recovery obligation: general construction with Δ = one grid step must reproduce registered partitions, failure falsifies the construction); three tiers T1 coherence / T2 distinctiveness / T3 discrimination with per-tier success and failure conditions; distinctiveness-first ordering (decided with Rico 2026-08-05); **study** as the new unit of validation (StudySpec with ε-family block + declared Δ-reachability rule + composition rule, Preregistration as first-class frozen artifact, boundary sets instead of θ* scalars, StudyRecord); no Φ across the 1D/general break — cross-study comparison goes to Σ level (WP-A3, revives WP-A5 as companion artifact); T2 candidate list ((ε₁,ε₂) joint region for CASE-20260311-0003, Rule A/B divergence on a ≥2D field, boundary set for CASE-20260430-0013 or Kuramoto (κ,σ), codim-2 detection vs 1D-sweep family) | — | Added 2026-08-05. Operationalises general_regime_construction.md §7; validates nothing itself (§5 states the empty validation column and the no-continuity-metric cost explicitly); guard against indefinitely deferred external contact: Cascade T3 resumes as soon as T1 ε-family scaffolding exists. Registers Q-VAL-01–03 (prefix collision-checked, free). framework_validation.md already superseded; validation_program_signatures.md orthogonal, untouched. |

---

## Navigation Index

The existing `docs/INDEX.md` serves as human-facing navigation.
This file (DOC_INDEX.md) serves as the anti-pile-up registry — tracking canonical ownership
of concepts, supersession chains, and open issues. Both should be maintained together.
