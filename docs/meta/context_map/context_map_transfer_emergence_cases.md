---
status: working-definition
layer: docs/meta/context_map/
version: 0.2
task: 4/4 — Transfer + Emergence + Cases (exemplary) + YAML assembly
schema: context_map_framework.md §Schema
updated: 2026-05-10
changes_from_v0.1: >
  Fixed SIR BC class (FORCING→AGGREGATION). Fixed all pending case IDs
  (20260429→20260315). Added CASE-20260329-0011, CASE-20260330-0012,
  CASE-20260430-0013 (spring-mass chain). Fixed CASE-0003 BC class
  (was erroneously listed as COUPLING+RESTRICTION; correct is RESTRICTION only).
  YAML assembly updated to match corrected case list. Task 4 YAML remains
  exemplary (not a full assembly of all 13 cases).
---

# ARW Context Map — Transfer + Emergence + Cases

Agent-optimised reference. Schema defined in context_map_framework.md.

---

## Transfer Metric Entries

```
Φ: metric∈transfer | weighted_composite(RCD,TBS_norm,PCI,SDI)
    ≥0.8→highly_admissible | 0.5-0.8→partially_admissible | <0.5→inadmissible
    measures=observable_transfer_not_system_transfer
    ε_mismatch: report_Φ_raw+Φ_matched_ε_both
    guard: TransferReport_must_include_BC_structure_both_scopes

RCD: metric∈transfer | |N*_A - N*_B|
    =0→necessary_not_sufficient_for_admissibility
    >0→regime_count_mismatch→Φ_penalty

TBS_norm: metric∈transfer | |θ*_A/range_A - θ*_B/range_B|
    normalized_transition_shift | requires=sweep_range_in_both_Invariants.json
    missing_sweep_range→TBS_norm=undefined+flag | cf.GUARD-5,GUARD-8

PCI: metric∈transfer | |overlap(R_A,R_B)|/|union(R_A,R_B)|
    Jaccard_overlap_of_partition_regions | requires=aligned_regime_labels
    requires=shared_BC_parameterization_or_mapping

SDI: metric∈transfer | 1 - |w_A-w_B|/max(w_A,w_B)
    w=plateau_width(log_scale) | measures=resolution_robustness_similarity
    SDI=1→identical_plateau_width | SDI→0→very_different_robustness

admissibility_verdict: concept∈transfer | Φ→{highly_admissible,partially_admissible,inadmissible}
    written_to=TransferMetrics.json | closed_enum
```

### Transfer Interpretation Rules

```
high_Φ + different_systems:  observables_project_similar_regime_structure | dynamics_may_differ
low_Φ  + same_BC_class:      check_observable_BC_structures_first | Φ=observable_not_system_transfer
RCD=0  + low_Φ:              transitions_at_different_normalized_positions(high_TBS_norm)
                              OR partitions_incompatible(low_PCI)
```

### Known Transfer Results

```
CASE-0001↔CASE-0002: Φ=0.675 | partially_admissible | RCD=1,TBS_norm=0.167
CASE-0001↔CASE-0003: Φ_raw=0.40,Φ_matched_ε≈0.95 | ε_mismatch_drives_divergence
CASE-0001↔CASE-0004: Φ=pending | same_BC_class(Coupling) | first_same-class_cross-system
CASE-0002↔CASE-0003: Φ=computed | see_transfer/pendulum_vs_kuramoto/
```

---

## Emergence Analysis Entries

```
emergence_window: concept∈emergence | ε∈[ε_local_collapse,ε_relational_collapse]
    width=ε_relational_collapse-ε_local_collapse | wide→robust_emergence
    condition: local_cover_trivial ∩ relational_cover_nontrivial+Δ-stable
    requires=Π_contains_both_local+relational_observables

local_observable: concept∈emergence | BC_structure_dominated_by=RESTRICTION|DISSIPATION
    captures=individual_unit_behavior | computable_without_reference_to_others
    role: defines_emergence_window_lower_bound_via_F1
    example: amp_asym(amplitude_asymmetry_single_oscillator)

relational_observable: concept∈emergence | BC_structure_dominated_by=COUPLING|AGGREGATION
    captures=collective_structure | requires_ensemble_or_interaction_reference
    role: defines_emergence_window_upper_bound_via_relational_collapse
    example: PLV(Phase_Locking_Value_across_all_oscillators)

local_collapse: concept∈emergence | ε_at_which_local_cover_becomes_trivial
    =lower_bound_of_emergence_window | often_F1_by_design_in_emergence_cases

relational_collapse: concept∈emergence | ε_at_which_relational_cover_becomes_trivial
    =upper_bound_of_emergence_window | Z_cover(relational_π,ε)→nontrivial

collapse_ordering: concept∈emergence | which_observable_loses_nontriviality_first
    local<relational → standard_bottom-up_emergence(canonical)
    relational<local → reverse_ordering → suspect_observable_choice
    diagnostic: compare_ε_collapse_values_from_epsilon_sweep.py_per_observable

Λ_robustness: concept∈emergence | stability_of_emergence_window_under_system_param_variation
    example_CASE-0004: window_stable_for_λ∈[0.4,1.3] | collapses_for_λ>1.3@weak_K
```

### Emergence ScopeSpec Rules

```
emergence_case_ScopeSpec:
  Pi: local_observable(primary:false) + relational_observable(primary:true)
  falsification: F1_for_local_observable(note=intentionally_insufficient_by_design)
  CaseRecord: emergence_docs field required
  guard: F1_local≠scope_failure — it_defines_the_window_lower_bound
```

---

## Case Entries (Active — pipeline run or complete)

```
CASE-20260311-0001: case∈cases | Kuramoto_N=400 | BC=COUPLING | status=complete | go_nogo=go
    S=(B={κ∈[0,3],σ=1.0},Π={r_ss},Δ=IC±0.05,ε=0.09)
    N*=2(incoherent/synchronized) | θ*≈1.475 | plateau=[0.06,0.12]
    F0@κ≈κ_c(r_ss:A2+A4+A5_fail→scope_transition_not_boundary)
    F4@θ*≈κ_max=1.5(extend_sweep_to_κ=2.5)
    gap_θ*_vs_κ_c: 8%_finite-N_effect(N→∞→κ_c=√(8/π)·σ≈1.596)
    transfer: paired_with=CASE-0002,CASE-0003

CASE-20260311-0002: case∈cases | Multi-Link-Pendel | BC=COUPLING | status=complete | go_nogo=go
    S=(B={κ∈[0,10]},Π={var_rel(primary)},Δ=IC,ε=0.023)
    N*=3 | θ*≈3.25 | observable=var_rel(sufficient),lambda_proxy(insufficient_by_construction)
    transfer: paired_with=CASE-0001,CASE-0003

CASE-20260311-0003: case∈cases | DoublePendulum | BC=RESTRICTION | status=complete | go_nogo=go
    S=(B={E∈[0.5,30J]},Π={var_rel(primary)},Δ=energy-norm,ε=0.015)
    N*=2_primary | secondary_ridge@E≈ω₀²
    F-gradient@E≈ω₀²: E_rel∈R(π)_everywhere,A0-A6_all_pass
        cause=high_|∂E_rel/∂κ|→Z_cover(E_rel,ε_working)≠∅
        resolution=ε↓15%_eliminates_ridge | classified=scope_refinement
        initially_suspected_F0→substrate_analysis_ruled_out(canonical_F-gradient_example)
    transfer: paired_with=CASE-0001,CASE-0002

CASE-20260318-0004: case∈cases | StuartLandau_2osc | BC=COUPLING | status=complete | go_nogo=go
    S=(B={K∈[0,0.3],λ=0.7},Π={PLV(primary),amp_asym},Δ=IC±0.01,ε=0.12)
    N*=2(phase-incoherent/phase-locked) | θ*≈K*=0.055 | plateau=[0.082,0.805]
    emergence_window=[0.082,0.805],width=0.723(wide→robust)
    local_obs=amp_asym(F1_by_design,span<<2ε,BC_structure=R·D)
    relational_obs=PLV(sufficient,Z(PLV)=∅,BC_structure=C·A)
    Λ_robustness: stable_λ∈[0.4,1.3] | collapses_λ>1.3@weak_K
    first_ARW_emergence_case | collapse_ordering=local<relational(canonical)
    transfer: paired_with=CASE-0001(same_BC_class_Coupling)
```

---

## Case Entries (Pending — signature-first, pipeline not yet run)

```
CASE-20260315-0005: case∈cases | Multi-Pendel+damping | BC=DISSIPATION | status=open | go_nogo=pending
    sweep=γ(damping_coefficient) | ScopeSpec_signature_first=present

CASE-20260315-0006: case∈cases | Multi-Pendel+forcing | BC=FORCING | status=open | go_nogo=pending
    sweep=Ω(forcing_frequency) | ScopeSpec_signature_first=present

CASE-20260315-0007: case∈cases | SIR_epidemic | BC=AGGREGATION | status=open | go_nogo=pending
    sweep=β(transmission_rate) | ScopeSpec_signature_first=present
    note: BC=AGGREGATION(population_level_expectation_operator) | ¬FORCING

CASE-20260315-0008: case∈cases | Pitchfork_normal_form | BC=SYMMETRY_BREAKING | status=open | go_nogo=pending
    sweep=μ(bifurcation_param) | ScopeSpec_signature_first=present

CASE-20260315-0009: case∈cases | Stochastic_Kuramoto | BC=COUPLING+NOISE | status=open | go_nogo=pending
    sweep=σ(noise_amplitude) | ScopeSpec_signature_first=present

CASE-20260315-SOC1: case∈cases | Shame_interaction_regime | BC=RESTRICTION(social) | status=open | go_nogo=pending
    domain=social | ScopeSpec_signature_first=present | methodological_friction_documented

CASE-20260328-0010: case∈cases | German_school_system | BC=COUPLING+RESTRICTION+FORCING+DISSIPATION | status=open | go_nogo=pending
    first_multi-BC_case | ScopeSpec.yaml=present | BCManifest+CaseRecord=not_yet_created

CASE-20260329-0011: case∈cases | Labyrinth_agent_Phase1 | BC=COUPLING+RESTRICTION(cognitive) | status=open | go_nogo=pending
    domain=context_navigation(ART) | system=labyrinth_10x10_uniform_ZoneA
    question=does_discrete_regime_partition_emerge_from_behavioral_space?
    ScopeSpec_companion=context_navigation_scope_spec.md

CASE-20260330-0012: case∈cases | Labyrinth_EmergentModes | BC=COUPLING+RESTRICTION(cognitive) | status=open | go_nogo=pending
    domain=context_navigation(ART) | system=labyrinth_multi-zone_unstructured_policy
    ARW_as_post-hoc_observation_instrument | ScopeSpec_companion=context_navigation_scope_spec_emergent.md

CASE-20260430-0013: case∈cases | Spring-Mass_Chain_1D | BC=FORCING+RESTRICTION | status=open | go_nogo=pending
    domain=mechanical | multi-scale_observable_scope
    sweep=2D(A=forcing_amplitude,Ω=forcing_freq) | conditioned_param=N(chain_length,1..5)
    Pi={π_micro(spring_extension_var),π_meso(COM_var),π_macro(end_mass_var)}
    ScopeSpec_signature_first=v3_present | consistency_check=present
    first_multi-scale_observable_case
```

---

## YAML Assembly — context_map.yaml (exemplary)

This file demonstrates the machine-readable format for agent context injection.
Full version merges all four task files. Values below are representative;
pending cases listed as status-only entries.

```yaml
# context_map.yaml
# ARW Agent Context Map — machine-readable index
# Generated from: context_map_framework.md + context_map_falsification_bc.md
#                 context_map_pipeline.md + context_map_transfer_emergence_cases.md
# Version: 0.2 (updated 2026-05-10 — case list corrected and extended)

meta:
  version: "0.2"
  status: "working-definition"
  layer: "docs/meta/context_map/"
  description: >
    Scope-relative context injection map for ARW repository agents.
    Each entry is minimally sufficient for agent navigation and decision-making.
    Not a human-readable glossary — use docs/glossary/ for that.

framework:

  S:
    type: concept
    layer: framework
    relation: "S=(B,Pi,Delta,epsilon)"
    trigger: "all_regime_claims_relative_to_S"
    action: "—"

  sigma_delta:
    id: "sigma_Delta"
    type: metric
    layer: cover
    relation: "sup_delta|O(x+delta)-O(x)|"
    trigger: ">epsilon@x->Z_cover"
    action: scope_refinement
    bound: "L*r[Corollary1]"
    computed_by: "stability_mask.py [PLANNED — action E-1]"

  I_epsilon:
    id: "I_epsilon"
    type: interval
    layer: cover
    relation: "sup(sigma_Delta)<epsilon<epsilon*"
    trigger: "empty->no_valid_scope"
    action: scope_redesign
    empirical: "N(epsilon)_plateau"

  R_pi:
    id: "R(pi)"
    type: set
    layer: observable
    relation: "{x in X_B: A0-A6_satisfied}"
    trigger: "theta*_in_Z(pi)->scope_transition_not_boundary"
    action: flag
    cf: "Z(pi)"

  Z_pi:
    id: "Z(pi)"
    type: zone
    layer: observable
    relation: "X_B minus R(pi)"
    trigger: "A0-A6_violation->F0"
    action: observable_replacement
    note: "epsilon-independent — no epsilon resolves Z(pi)"

  Z_cover:
    id: "Z_cover"
    type: zone
    layer: cover
    relation: "{x: sigma_Delta(x)>=epsilon} intersect R(pi)"
    trigger: "nonempty->F-gradient"
    action: scope_refinement
    note: "epsilon-dependent — not Z(pi)"

falsification:

  F0:
    type: failure
    layer: falsification
    relation: "Z(pi) nonempty in X_B | A0-A6_violation"
    trigger: "substrate_failure"
    action: observable_replacement
    diagnostic: "substrate_analysis(A0-A6)"
    note: "epsilon-independent"
    cf: "not F-gradient"

  F_gradient:
    id: "F-gradient"
    type: failure
    layer: falsification
    relation: "not F0 AND Z_cover nonempty | cause=high_grad_O@x"
    trigger: "Z_cover nonempty"
    action: scope_refinement
    diagnostic: "A0-A6_all_pass->F-gradient | stability_mask(sigma_Delta_field)"
    note: "epsilon-dependent"
    cf: "not F0"

  F4:
    type: failure
    layer: falsification
    relation: "theta*@sweep_boundary"
    trigger: "true_transition_outside_B"
    action: sweep_refinement
    note: "not a scope failure — extend sweep before interpreting theta*"

bc_taxonomy:

  COUPLING:
    type: bc_class
    layer: bc_taxonomy
    operator: "composition + tensor_product"
    param: "kappa(Kuramoto), K(SL)"
    observable_target: "order_params, sync_indices"
    cases: ["CASE-20260311-0001", "CASE-20260311-0004"]

  RESTRICTION:
    type: bc_class
    layer: bc_taxonomy
    operator: "projection"
    param: "E(pendulum), amplitude_limits"
    observable_target: "energy_based, frequency_content"
    cases: ["CASE-20260311-0003"]

  AGGREGATION:
    type: bc_class
    layer: bc_taxonomy
    operator: "conditional_expectation_population"
    param: "sigma(freq_spread), beta(SIR)"
    observable_target: "population_stats, var_rel, I_peak"
    cases: ["CASE-20260315-0007"]
    note: "SIR is AGGREGATION not FORCING"

pipeline:

  sweep_py:
    id: "sweep.py"
    type: module
    layer: pipeline
    inputs: ["BCManifest.yaml", "ScopeSpec.yaml"]
    outputs: ["results/sweep/sweep_data.json"]
    blocks: "ALL_downstream"

  stability_mask_py:
    id: "stability_mask.py"
    type: module
    layer: pipeline
    status: "PLANNED — action_item E-1; not yet implemented"
    note: "gradient_proxy in epsilon_kappa_map.py is current approximation"

  invariants_py:
    id: "invariants.py"
    type: module
    layer: pipeline
    inputs: ["PartitionResult.json", "ScopeSpec.yaml"]
    outputs: ["Invariants.json"]
    mandatory_output_fields:
      - N_regimes
      - theta_star
      - epsilon_working
      - epsilon_plateau
      - sweep_range
    blocks: "transfer.py"
    guard: "sweep_range_missing->TBS_norm=undefined"

transfer:

  Phi:
    id: "Phi"
    type: metric
    layer: transfer
    relation: "weighted_composite(RCD, TBS_norm, PCI, SDI)"
    thresholds: ">=0.8->highly_admissible | 0.5-0.8->partially_admissible | <0.5->inadmissible"
    note: "measures observable transfer not system transfer"

  TBS_norm:
    type: metric
    layer: transfer
    relation: "|theta*_A/range_A - theta*_B/range_B|"
    trigger: "missing_sweep_range->undefined"
    action: flag
    guard: "GUARD-5 + GUARD-8"

emergence:

  emergence_window:
    type: concept
    layer: emergence
    relation: "epsilon in [epsilon_local_collapse, epsilon_relational_collapse]"
    trigger: "wide->robust | narrow->marginal"
    action: flag
    requires: "Pi contains local + relational observables"

  collapse_ordering:
    type: concept
    layer: emergence
    relation: "local<relational->canonical | relational<local->suspect_observable"
    trigger: "reverse_ordering->review_observable_choice"
    action: flag

cases_active:

  CASE-20260311-0001:
    system: Kuramoto
    bc_class: COUPLING
    status: complete
    go_nogo: go
    N_star: 2
    theta_star: 1.475
    epsilon_working: 0.09
    failures: ["F0@kappa_c", "F4@sweep_edge"]

  CASE-20260311-0002:
    system: Multi-Link-Pendulum
    bc_class: COUPLING
    status: complete
    go_nogo: go
    N_star: 3
    theta_star: 3.25
    epsilon_working: 0.023

  CASE-20260311-0003:
    system: DoublePendulum
    bc_class: RESTRICTION
    status: complete
    go_nogo: go
    N_star: 2
    epsilon_working: 0.015
    failures: ["F-gradient@secondary_ridge_E_approx_omega0_squared"]

  CASE-20260318-0004:
    system: StuartLandau_2osc
    bc_class: COUPLING
    status: complete
    go_nogo: go
    N_star: 2
    theta_star: 0.055
    epsilon_working: 0.12
    emergence: true
    emergence_window: [0.082, 0.805]
    emergence_width: 0.723

cases_pending:

  CASE-20260315-0005: {system: Multi-Pendulum_damped, bc_class: DISSIPATION, status: open}
  CASE-20260315-0006: {system: Multi-Pendulum_forced, bc_class: FORCING, status: open}
  CASE-20260315-0007: {system: SIR_epidemic, bc_class: AGGREGATION, status: open, note: "not FORCING"}
  CASE-20260315-0008: {system: Pitchfork_normal_form, bc_class: SYMMETRY_BREAKING, status: open}
  CASE-20260315-0009: {system: Stochastic_Kuramoto, bc_class: COUPLING+NOISE, status: open}
  CASE-20260315-SOC1: {system: Shame_interaction, bc_class: RESTRICTION_social, domain: social, status: open}
  CASE-20260328-0010: {system: German_school_system, bc_class: COUPLING+RESTRICTION+FORCING+DISSIPATION, status: open}
  CASE-20260329-0011: {system: Labyrinth_Phase1, bc_class: COUPLING+RESTRICTION, domain: context_navigation, status: open}
  CASE-20260330-0012: {system: Labyrinth_EmergentModes, bc_class: COUPLING+RESTRICTION, domain: context_navigation, status: open}
  CASE-20260430-0013: {system: Spring-Mass_Chain_1D, bc_class: FORCING+RESTRICTION, status: open, note: "first multi-scale observable case"}

guards:
  GUARD-1: "ScopeSpec.Pi: exactly_one primary:true"
  GUARD-2: "falsification.id: closed_enum {F0,F1,F1_BC,F2,F3,F4,F-gradient}"
  GUARD-3: "falsification.severity: closed_enum"
  GUARD-4: "observable_insufficiency != scope_rejection"
  GUARD-5: "Invariants.json.sweep_range: mandatory"
  GUARD-6: "TransferMetrics: must note observable BC structures both scopes"
  GUARD-7: "CaseRecord.go_nogo=pending until validate.py+audit.py pass"
  GUARD-8: "TBS_norm: normalized form only"
  GUARD-9: "all repo artifacts in English"
```
