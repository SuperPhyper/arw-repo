---
status: working-definition
layer: docs/meta/context_map/
version: 0.1
task: 2/4 — Falsification + BC Taxonomy
schema: context_map_framework.md §Schema
---

# ARW Context Map — Falsification + BC Taxonomy

Agent-optimised reference. Schema defined in context_map_framework.md.
Read that file first if schema notation is unfamiliar.

---

## Falsification Entries

```
F0: failure∈falsification | Z(π)≠∅∩X_B | A0-A6_violation | →observable_replacement | ¬F-gradient
    diagnostic: substrate_analysis(A0-A6) | empirical: σ_Δ↑@failure_region
    note: ε-independent — no ε choice recovers F0 region
    ¬F-gradient: if_A0-A6_all_pass→not_F0 | high_σ_Δ_alone_is_insufficient_for_F0
    ¬F1: F0_is_structural(substrate_fails) | F1_is_resolution(span<2ε) — independent_axes

F1: failure∈falsification | |C_ε|=1@ε_working | span(π)<2ε OR ε≥ε* | →observable_replacement
    diagnostic: check_span_vs_2ε then check_topology | cf.F1_BC
    note: reduce_ε only if ε_new>sup(σ_Δ), else triggers Δ-instability
    ¬F1_BC: F1=single_observable_insufficient | F1_BC=ALL_observables_insufficient→scope_rejection
    ¬F0: F1_is_resolution_failure(span) | F0_is_substrate_failure(A0-A6) — check_substrate_first

F1_BC: failure∈falsification | F1_for_all_π∈Π | BC_param_has_no_observable_effect | →scope_rejection
    diagnostic: F1_confirmed_across_full_Π | cf.F1
    note: only failure type triggering scope_rejection from observable_insufficiency
    ¬F1: F1_BC_requires_F1_for_EVERY_π∈Π | single_F1_→_F1_not_F1_BC
    ¬F3: F1_BC=observables_have_no_spread | F3=observables_have_spread_but_no_stable_plateau

F2: failure∈falsification | θ*_unstable_under_Δ | cross-run_θ*_shift>tolerance | →scope_rejection
    diagnostic: repeat_runs_within_Δ | compare_θ*_distribution
    ¬F3: F2=plateau_exists_but_θ*_shifts_across_runs | F3=no_plateau_at_all
    ¬F4: F2=θ*_unstable_under_Δ(perturbation) | F4=θ*_at_B_edge(sweep_extent) — different_causes

F3: failure∈falsification | no_plateau_in_N(ε)_for_all_π∈Π | I_ε=∅ | →scope_rejection
    diagnostic: check_sup(σ_Δ)_vs_ε* | if_sup(σ_Δ)≥ε*→no_valid_ε_exists
    note: collective failure — not resolvable by observable swap alone
    ¬F2: F3=no_plateau_in_N(ε)_curve | F2=plateau_exists_but_θ*_drifts_under_Δ
    ¬F1: F3=N(ε)_never_stabilises(for_any_π) | F1=N(ε)=1(cover_trivial_for_one_π)

F4: failure∈falsification | θ*@sweep_boundary | true_transition_outside_B | →sweep_refinement
    diagnostic: θ*_proximity_to_B_edge | not_a_scope_failure
    note: scope may be entirely valid — extend_sweep before interpreting θ*
    ¬F2: F4=θ*_at_B_boundary(artifact_of_sweep_range) | F2=θ*_unstable_under_Δ(within_B)
    ¬scope_failure: F4_is_only_sweep_refinement | no_scope_rejection_from_F4_alone

F-gradient: failure∈falsification | ¬F0∩Z_cover≠∅ | cause=high_|∇O|@x | →scope_refinement OR observable_replacement
    diagnostic: A0-A6_all_pass? yes→F-gradient | stability_mask(σ_Δ_field)
    ε-direction: ↑ INCREASE ε above sup_x(σ_Δ) to satisfy I_ε lower bound | ¬decrease
    ε-contradiction-check: if_you_wrote_decrease_ε AND sup(σ_Δ)<ε in_same_block → CONTRADICTION | re-read ε-direction above | correct to ε↑
    actions_ranked: [stability_mask_exclusion, ε↑, r↓, observable_replacement]
    actions_ranked_note: stability_mask=primary | ε↑=secondary | r↓=tertiary | observable_replacement=last_resort
    note: ε-dependent — Z_cover shrinks as ε↑ | F-gradient∩A_i_fail→reclassify_as_F0
```

### Falsification Decision Tree (compressed)

```
unexpected_result OR plateau_failure
  → σ_Δ(x)≥ε anywhere?
      YES → substrate_analysis:
              A0-A6_fail? → F0→observable_replacement
              A0-A6_pass? → F-gradient→scope_refinement
      NO  → |C_ε|=1? → F1(check_all_Π→F1_BC?)→observable_replacement
          → θ*_unstable_under_Δ? → F2→scope_rejection
          → no_plateau_any_π? → F3→scope_rejection
          → θ*@B_edge? → F4→sweep_refinement
```

AMENDMENT-2026-07-18: decision_order_revised(monograph VII V3.2) |
    new_order: F0 → F4 → F1 → F3 → F2 → F-gradient |
    rationale: θ*@edge_has_no_reliable_estimate ⇒ F2_uninterpretable_before_F4 |
    F1_generalized: claim_relative(ε-partition_fails_to_refine_R_claim) |
        total_collapse(ε≥ε*)=special_case(pipeline_tests_this_form) |
    F-gradient_mass: fraction μ(χ=1)/μ(X_B)>τ_∂ (χ=assignment_instability,
        σ=proxy; χ_not_computed→Q_NEW_26) |
    A6_split: invalidity→F0 | valid_but_unresolving@ε→F1 |
    F2_tests: Var>τ_var OR range>τ_range (not_equivalent; case_declares) |
    AMENDMENT-2026-07-18b: χ_sweep_form(component_identity: C_ε^δ(x_j)≢C_ε(x_j),
        NOT r_ε(T_δx) — undefined off sweep nodes) |
        σ↔χ_error_relation=uncharacterised(both directions possible; C1
        one-sidedness concerns gradient→σ only) → Q_NEW_26 |
        never_lower_ε = proxy-based_pipeline_convention, NOT χ-theorem
        (ε changes partition ⇒ χ-effect not guaranteed monotone;
        ε-repairs within selected plateau + verify by recomputation) |
        λ_T_typing: finite-time Lyapunov = own observable (referent=λ_T@T,
        A6 tests λ_T stability → can pass → F1 for claimed structure;
        read as λ_∞ estimator without passing convergence test → F0) |
    tree_above=historical_until_next_map_regeneration

### Severity Cross-Reference

```
observable_replacement : F0 | F1 | F1_BC(partial) | F-gradient(secondary)
scope_rejection        : F1_BC | F2 | F3
sweep_refinement       : F4
scope_refinement       : F-gradient(primary)
universal_exclusion    : Z_shared
```

---

## BC Taxonomy Entries

### Six BC Classes

```
COUPLING: bc_class∈bc_taxonomy | operator=∘⊗ | param=κ(Kuramoto),K(SL),coupling_const
    signature: interaction_between_components | partition=sync_transition
    observable_target: order_params(r_ss),sync_indices | Z(π)@transition
    cases: CASE-0001(Kuramoto),CASE-0002(MultiPendulum),CASE-0004(SL)

RESTRICTION: bc_class∈bc_taxonomy | operator=π(projection,object-level)+Adm(meta-level) | param=E(pendulum),amplitude_limits
    signature: constraint_on_admissible_subspace | partition=energy_regime_boundary
    meta_role: admissibility_condition_for_all_other_relations (see bc_relational_structure.md §3)
    observable_target: energy_based,frequency_content | Z(π)@constraint_boundary
    cases: CASE-0003(DoublePendulum)
    updated: 2026-05-30 — added meta-relational character

DISSIPATION: bc_class∈bc_taxonomy | operator=ordered_continuation(R_D⊆X×X_≤) | param=τ(ordering_scale),sequence_horizon
    signature: ordered_distinguishability_preservation | partition=attractor_basin_boundary
    note: ordering ≤ is primary (time is most common case); energy_loss and attractor depth are secondary
    failure_directions: weakening(→indistinguishability) | deepening(→single_attractor)
    observable_target: recovery_time,zone_sharpness,basin_depth | Z(π)@attractor_disappears
    cases: CASE-0005(pending)
    updated: 2026-05-30 — reformulated as ordered-continuation relation; energy_loss demoted to secondary

FORCING: bc_class∈bc_taxonomy | operator=R_F(Regime_A→Adm(Regime_B),directional) | param=regime_compatibility,organiser_scale
    signature: inter_regime_admissibility_relation | partition=compatibility_boundary
    note: frequency/resonance is a special case; general form is directional inter-regime coupling
    failure_directions: decoupling(organiser_loses_reach) | absorption(organised_loses_autonomy)
    observable_target: regime_coherence,cross_regime_correlation | Z(π)@incommensurability_zone
    cases: CASE-0006(pending)
    updated: 2026-05-30 — reformulated as directional inter-regime coupling; external_energy_injection demoted to special case

AGGREGATION: bc_class∈bc_taxonomy | operator=E[·|G](population) | param=σ(freq_spread),pop_variance
    signature: statistical_aggregation_of_units | partition=collective_onset
    observable_target: population_stats,var_rel | Z(π)@critical_fluctuations
    cases: CASE-0007(SIR,pending)

SYMMETRY_BREAKING: bc_class∈bc_taxonomy | operator=symmetry_perturb(equivariant) | param=μ(pitchfork)
    signature: breaks_structural_symmetry | partition=bifurcation_point
    observable_target: asymmetry_order_params(PLV) | Z(π)@bifurcation
    cases: CASE-0008(pitchfork,pending)
```

### Operator Signatures S1–S5

```
S1: operator∈bc_taxonomy | ∘(composition) | present_in=COUPLING | —
S2: operator∈bc_taxonomy | ⊗(tensor_product) | present_in=COUPLING | state_space_expansion
S3: operator∈bc_taxonomy | π(projection) | present_in=RESTRICTION | state_space_contraction
S4: operator∈bc_taxonomy | ×(contraction,neg_definite) | present_in=DISSIPATION | energy_removal
S5: operator∈bc_taxonomy | E[·|G](conditional_expectation) | present_in=FORCING+AGGREGATION | external_or_population
```

### Observable BC Structure Notation

```
BC_structure(π): concept∈bc_taxonomy | pattern_of_S1-S5_in_π_functional_form
    ≠ system_BC_class | independent_of_system | determines=observable_sensitivity+Z(π)_shape
    notation: R³·A·D = Restriction_dominant×3,Aggregation,Dissipation
    example: r_ss → BC_structure=R³·A·D | regardless_of_which_system_applied_to
    relevance: Φ_measures_observable_transfer_not_system_transfer
```

### Signature-First Workflow (compressed)

```
new_case_setup:
  1. identify_state_spaces(degrees_of_freedom)
  2. identify_primitive_ops(∘,×,π,⊗,E[·|G])∈governing_equations
  3. which_ops_parameterized_by_sweep_param? → BC_signature
  4. assign_BC_class(COUPLING|RESTRICTION|DISSIPATION|FORCING|AGGREGATION|SYMMETRY_BREAKING)
  5. predict_expected_partition(from_BC_class_table)
  6. select_observables(from_BC_class_observable_targets)
  artifact: ScopeSpec_signature_first.md (pre-registered_before_pipeline_run)
```

### Multi-BC Cases

```
MULTI_BC: concept∈bc_taxonomy | multiple_BC_classes_active_simultaneously
    example: CASE-0010(German_school_system)=COUPLING+RESTRICTION+FORCING+DISSIPATION
    challenge: operator_signatures_overlap | BC_structure_analysis_required_per_observable
    status: first_multi-BC_case_planned | methodology_under_development
```

---

## Cross-Layer Connections

Entries here link falsification and BC taxonomy to framework objects from Task 1:

```
F0 ↔ Z(π):       F0_is_operational_trigger | Z(π)_is_formal_region | same_phenomenon
F-gradient ↔ Z_cover: F-gradient_is_operational_trigger | Z_cover_is_formal_region
Z_shared ↔ F0:    Z_shared⊆Z(π)_for_all_class-E | Z_shared_cannot_be_escaped_within_class-E
BC_class ↔ Π:     BC_class_determines_observable_selection | Π_should_match_BC_class_targets
S1-S5 ↔ σ_Δ:     operator_signatures_predict_where_σ_Δ_will_be_high (transition_boundaries)
```

---

## Notes for Next Tasks

Task 3 entries to produce:
- Pipeline modules (11): sweep.py, stability_mask.py, epsilon_sweep.py,
  epsilon_kappa_map.py, epsilon_multi_observable.py, extract_partition.py,
  invariants.py, transfer.py, validate.py, audit.py, new_case.py
- Artifacts (7): ScopeSpec.yaml, ScopeSpec_signature_first.md, BCManifest.yaml,
  CaseRecord.yaml, PartitionResult.json, TransferMetrics.json, FailureAudit.md

Task 4 entries to produce:
- Transfer metrics: Φ, RCD, TBS_norm, PCI, SDI, admissibility_verdict
- Emergence: emergence_window, local_collapse, relational_collapse, collapse_ordering
- Active cases: CASE-20260311-0001 through CASE-20260330-0012
- Final assembly: context_map.yaml (machine-readable, all tasks merged)
