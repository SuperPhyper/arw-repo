---
status: working-definition
layer: docs/meta/context_map/
version: 0.1
task: 3/4 — Pipeline + Artifacts
schema: context_map_framework.md §Schema
---

# ARW Context Map — Pipeline + Artifacts

Agent-optimised reference. Schema defined in context_map_framework.md.

---

## Pipeline DAG (compressed)

```
sweep.py | sweep_behavioral.py → epsilon_sweep.py → epsilon_kappa_map.py [σ_Δ direct + proxy]
                                                 → epsilon_multi_observable.py [if |Π|>1]
                                                         ↓
                                               extract_partition.py
                                                         ↓
                                                   invariants.py
                                                         ↓
                               transfer_v2.py [CANONICAL; requires Invariants.json + annotated_results from BOTH cases]
                                                         ↓
                                              validate.py + audit.py
```
*(DAG corrected 2026-08-04, core-concept drift audit: `stability_mask.py` removed
from the chain — it is not implemented and its function lives inside
`epsilon_kappa_map.py`; `transfer.py` (v1) replaced by `transfer_v2.py` as the
canonical transfer stage.)*

**Blocking relations:**
```
sweep.py         blocks=ALL_downstream
invariants.py    blocks=transfer.py (sweep_range mandatory)
validate.py      blocks=commit (non-zero exit on schema violation)
```

---

## Pipeline Module Entries

```
sweep.py: module∈pipeline | in=BCManifest+ScopeSpec(observable_keys)
    out=results/sweep/sweep_data.json | computes=O(b_i)_for_all_grid_points
    blocks=ALL_downstream | —

sweep_behavioral.py: module∈pipeline | in=BCManifest+ScopeSpec | out=results/sweep/sweep_data.json
    role=behavioural/agent_kernels(cf.pipeline/kernels/labyrinth_agent.py,labyrinth_env.py) | cases=0011,0012

stability_mask.py: module∉pipeline [PLANNED — action_item=E-1/E-2; NOT_IMPLEMENTED — do_not_cite_as_source_of_values]
    intended_out=σ_Δ_field+binary_mask+stability_mask_summary.json
    CURRENT_LOCATION_OF_THIS_FUNCTION=epsilon_kappa_map.py::compute_sigma_delta_windowed(field=sigma_delta_windowed)
    trigger: σ_Δ≥ε@any_point → run_substrate_analysis(F0_vs_F-gradient)

epsilon_sweep.py: module∈pipeline | in=sweep_data+ε_range(auto_from_span)
    out=N(ε)_curve+plateau[ε_lo,ε_hi]+N*+ε_working_recommended
    trigger: no_plateau→F3 | plateau_width_narrow→flag
    computes=|connected_components(G_ε)|_per_ε

epsilon_kappa_map.py: module∈pipeline | in=sweep_data+ε_range
    out=gradient_field_|∂O/∂κ|_over_(κ,ε)_space + sigma_delta_windowed{sigma_delta,proxy_pointwise,proxy_localmax,pointwise_underestimates}
    computes_BOTH: direct_σ_Δ(windowed_max_abs_difference,USE_THIS) AND pointwise_proxy(Corollary1_exact_only_for_local-max_L)
    caveat: pointwise_under-reports_σ_Δ@θ*[C1_2026-06-02:one-sided_FN,optimistic]
    trigger: high_gradient_region → candidate_F-gradient | confirm_with=field:sigma_delta_windowed(¬proxy_pointwise@θ*)

epsilon_multi_observable.py: module∈pipeline | in=sweep_data_all_π+ε_range
    out=per_π_N(ε)_curves+agreement_rate+consensus_plateau
    condition: run_only_if_|Π|>1
    trigger: no_consensus_plateau→F3 | partial_agreement→flag_insufficient_observables

extract_partition.py: module∈pipeline | in=sweep_data+ε_working+stability_mask(optional)
    out=results/partition/PartitionResult.json(regime_assignment_per_grid_point)
    note: unstable_points_flagged_not_assigned | θ*_detected_here

invariants.py: module∈pipeline | in=PartitionResult+ScopeSpec
    out=results/partition/Invariants.json
    mandatory_fields: N*,θ*,ε_working,ε_plateau,sweep_range
    blocks=transfer.py | sweep_range_missing→TBS_norm_undefined

transfer_v2.py: module∈pipeline [CANONICAL_since_2026-06-02] | in=Invariants.json(both)+PartitionResult.annotated_results(both)
    out=transfer_v2/<A>_vs_<B>/TransferMetrics_v2.json+TransferReport_v2.md
    computes=Φ_v2(W_PCI=0.55,W_TOPO=0.25,W_TBS=0.20;weights_provisional)+PCI_real_overlap(+ARI)+RCD+TBS_band
    guards: VOID(empty_annotated_results|missing_sweep_range|undocumented_ε_mismatch) | TRIVIAL_PARTITION(N≤1) → Φ_UNDEFINED_¬low
    epistemic: Φ=decision_score∈partition_compatibility(necessary_¬sufficient) | ¬BC-class_evidence[Q-REL-05]
    SDI: w₄=0_default(collinear_with_RCD_in_1D-sweep_tier)[WP-A4_amendment_2026-07-17]

transfer.py: module∈pipeline [v1 — DEPRECATED_for_BC-class-distance_claims]
    out=transfer/<comparison>/TransferMetrics.json
    defect_2026-06-02: PCI_never_read_per-point_labels→collinear_with_RCD/SDI(~90%_of_Φ_tracked_N)
    disposition: v1_Φ/PCI_values_withdrawn_as_BC-class_evidence | check_producing_module_before_citing_any_Φ

validate.py: module∈pipeline | in=ALL_case_artifacts
    out=validation_report | exit_nonzero_on_schema_violation
    blocks=commit | run_before_every_commit

audit.py: module∈pipeline | in=PartitionResult+Invariants+ScopeSpec+stability_mask_summary
    out=audits/FailureAudit_Phase{N}.md
    runs=falsification_checklist(F0-F4,F-gradient)_against_partition_results
    trigger: unexpected_result_at_any_phase → generate_audit_entry

new_case.py: module∈pipeline | in=--system+--bc-class+--date(CLI_args)
    out=cases/CASE-YYYYMMDD-####/(ScopeSpec_template+BCManifest_template+CaseRecord_template)
    usage: python pipeline/new_case.py --system Kuramoto --bc-class Coupling --date 20260429
```

---

## Artifact Entries

```
ScopeSpec.yaml: artifact∈case | defines_S=(B,Π,Δ,ε)
    mandatory_blocks: B,Pi(primary:true_exactly_once),Delta,epsilon,
                      epsilon_choice_note,observable_sufficiency,falsification
    falsification_ids: F0|F1|F1_BC|F2|F3|F4|F-gradient (closed_enum)
    severity_ids: observable_replacement|scope_rejection|sweep_refinement|
                  scope_refinement|universal_exclusion (closed_enum)
    guard: observable_insufficiency≠scope_rejection | F0→observable_replacement_not_scope_rejection
    path: cases/CASE-YYYYMMDD-####/ScopeSpec.yaml

ScopeSpec_signature_first.md: artifact∈case | pre-pipeline_BC_inference
    mandatory_sections: [system_id,state_spaces,primitive_ops(∘×π⊗E[·|G]),
                         BC_signatures,BC_class_assignment,expected_partition,
                         observable_selection,draft_scope_tuple]
    status: note | layer: cases/...
    role: pre-registered_prediction | deviations_are_scientifically_informative
    path: cases/CASE-YYYYMMDD-####/ScopeSpec_signature_first.md

BCManifest.yaml: artifact∈case | documents_BC_class+sweep_program
    mandatory_fields: bc_class,sweep_parameter,sweep_range,sweep_points,fixed_parameters
    sweep_range→copied_to_Invariants.json(for_TBS_norm)
    path: cases/CASE-YYYYMMDD-####/BCManifest.yaml

CaseRecord.yaml: artifact∈case | case_envelope+status_tracker
    mandatory_fields: case_id,system,status,go_nogo,artifacts,scientific_value
    status_values: open|in_progress|complete|failed|archived
    go_nogo_values: go|pending|no_go(+date+reason)
    optional: related_cases,emergence_docs
    guard: go_nogo=pending_until_validate.py+audit.py_pass
    path: cases/CASE-YYYYMMDD-####/CaseRecord.yaml

PartitionResult.json: artifact∈case | regime_assignment_per_grid_point
    produced_by=extract_partition.py | consumed_by=invariants.py+transfer.py+audit.py
    contains: regime_label_per_b_i+θ*+unstable_point_flags
    path: cases/CASE-YYYYMMDD-####/results/partition/PartitionResult.json

Invariants.json: artifact∈case | core_partition_invariants
    mandatory_fields: N_regimes(=N*),theta_star,epsilon_working,epsilon_plateau,sweep_range,go_nogo
    sweep_range_missing→TBS_norm=undefined+flag
    produced_by=invariants.py | consumed_by=transfer.py+validate.py+audit.py
    path: cases/CASE-YYYYMMDD-####/results/partition/Invariants.json

TransferMetrics.json: artifact∈case | transfer_analysis_between_two_cases
    mandatory_fields: Φ,RCD,TBS_norm,PCI,SDI,admissibility_verdict
    admissibility_verdict: highly_admissible|partially_admissible|inadmissible
    ε_mismatch: report_raw_Φ+matched_ε_Φ
    must_include: observable_BC_structures_of_both_scopes
    produced_by=transfer.py
    path: cases/CASE-YYYYMMDD-####/transfer/<comparison>/TransferMetrics.json

FailureAudit.md: artifact∈case | falsification_checklist_per_pipeline_phase
    mandatory_per_entry: failed_check(F-id)+evidence+classification+recommended_action
    produced_by=audit.py | one_file_per_phase_with_unexpected_result
    path: cases/CASE-YYYYMMDD-####/audits/FailureAudit_Phase{N}.md
```

---

## Case Directory + Naming

```
case_id: concept∈case | format=CASE-YYYYMMDD-#### | YYYYMMDD=creation_date,####=zero-padded_seq
path: cases/CASE-YYYYMMDD-####/
scaffold: new_case.py | all_templates_generated_at_creation

dir_structure:
  ScopeSpec.yaml
  BCManifest.yaml
  CaseRecord.yaml
  ScopeSpec_signature_first.md      [newer cases]
  results/partition/
    PartitionResult.json
    Invariants.json
    stability_mask_summary.json
  transfer/<comparison>/
    TransferMetrics.json
    TransferReport.md
  audits/
    FailureAudit_Phase{N}.md
```

---

## Guard Rules (agent-critical)

Rules that must not be violated when creating or editing artifacts:

```
GUARD-1: ScopeSpec.Pi → exactly_one_entry_with_primary:true
GUARD-2: ScopeSpec.falsification.id → closed_enum only (F0|F1|F1_BC|F2|F3|F4|F-gradient)
GUARD-3: ScopeSpec.falsification.severity → closed_enum only
GUARD-4: observable_insufficiency ≠ scope_rejection (F1→observable_replacement, not scope_rejection)
GUARD-5: Invariants.json.sweep_range → mandatory; omission blocks TBS_norm
GUARD-6: TransferMetrics → must note observable BC structures of both scopes
GUARD-7: CaseRecord.go_nogo → pending until validate.py+audit.py both pass
GUARD-8: TBS_norm uses normalized form |θ*_A/range_A − θ*_B/range_B|, not raw TBS
GUARD-9: all repo artifacts in English regardless of conversation language
```

---

## Notes for Task 4

Task 4 entries to produce:
- Transfer metrics: Φ(obs_vs_sys), RCD, TBS_norm, PCI, SDI, admissibility_verdict
- Emergence: emergence_window, local_collapse, relational_collapse, collapse_ordering
- Active cases: CASE-20260311-0001 through CASE-20260330-0012 (status snapshots)
- Final assembly: context_map.yaml merging all four tasks into machine-readable index
