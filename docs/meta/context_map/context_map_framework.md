---
status: working-definition
layer: docs/meta/context_map/
version: 0.1
task: 1/4 — Schema + Framework Core
---

# ARW Context Map — Framework Core

Agent-optimised reference. Notation is dense by design: each entry encodes identity,
location, core relation, and operational trigger. Not for human reading — for context injection.

---

## Schema

```
<ID>: <type>∈<layer> | <core_relation> | <trigger→action> [| cf.<ID> | ¬<ID>]
```

### Controlled Vocabularies

**type**
```
metric | failure | zone | invariant | bc_class | operator |
artifact | module | concept | interval | graph | set
```

**layer**
```
framework | observable | cover | partition | transfer |
emergence | pipeline | case | falsification
```

**action** (closed enum — use exactly these strings)
```
scope_refinement       # adjust ε or Δ, scope remains usable
observable_replacement # replace observable, scope structure intact
sweep_refinement       # extend or densify sweep range
scope_redesign         # fundamental scope failure, restart
flag                   # document and monitor, no immediate action
—                      # no action triggered (informational entry)
```

**relation operators**
```
∈   member of / lives in
∩   intersection
∪   union
⊆   subset
≠∅  non-empty
→   implies / triggers
¬   negation (used for differential diagnosis)
cf. compare with (similar but distinct)
@   evaluated at / located at
↑   increases
↓   decreases
```

---

## Scope Tuple Objects

```
S: concept∈framework | S=(B,Π,Δ,ε) | all_regime_claims_relative_to_S | —

B: set∈framework | X_B⊆X | defines_admissible_domain | cf.ScopeSpec[BCManifest]

Π: set∈framework | {π:X_B→ℝ} | primary∈Π_required | cf.ScopeSpec[Pi-block]

Δ: set∈framework | admissible_perturbations | enters_via=σ_Δ | cf.ScopeSpec[Delta]

ε: interval∈framework | resolution_threshold | ∉I_ε→scope_invalid | cf.I_ε
```

---

## Cover Objects

```
G_ε: graph∈cover | nodes=X,edges=|O(x)-O(y)|≤ε | structure→C_ε | —

C_ε: set∈cover | connected_components(G_ε) | |C_ε|=1→F1 | |C_ε|=N*→partition_candidate

N(ε): metric∈cover | |C_ε|_as_fn_of_ε | plateau→I_ε | no_plateau→F3

N*: invariant∈partition | stable_|C_ε|_in_plateau | written_to=Invariants.json | —

σ_Δ: metric∈cover | sup_δ|O(x+δ)-O(x)| | >ε@x→Z_cover | bound=L·r[Corollary1]

ε*: metric∈cover | min_ε_s.t.|C_ε|=1 | upper_bound_of_I_ε | connected→ε*=span/2

I_ε: interval∈cover | sup(σ_Δ)<ε<ε* | empty→no_valid_scope | empirical=N(ε)_plateau

Corollary1: concept∈cover | σ_Δ(x)≤L·r | gradient_proxy=|∇O|·r | computed_by=epsilon_kappa_map.py
```

---

## Observable Objects

```
R(π): set∈observable | {x∈X_B:A0-A6_satisfied} | θ*∈Z(π)→scope_transition_not_boundary | cf.Z(π)

Z(π): zone∈observable | X_B\R(π) | A0-A6_violation | →F0 | ¬Z_cover

Z_shared: zone∈observable | system-level∩all_class-E_π | cause=ergodicity|critical_slowing|non-unique_μ | non-class-E_observable_required

Z_cover: zone∈cover | {x:σ_Δ(x)≥ε}∩R(π) | ε-dependent | →F-gradient | ¬Z(π)

A0: concept∈observable | state_space_well-defined+dynamics_integrable | prereq=A1-A6 | —
A1: concept∈observable | π_computable_from_x | prereq_for=A2-A6 | —
A2: concept∈observable | π_converges(time/ensemble_avg) | fails_at=phase_transition | —
A3: concept∈observable | π(x)_finite_everywhere_in_X_B | —
A4: concept∈observable | finite_measurement_variance | fails_at=critical_fluctuations | —
A5: concept∈observable | reproducible_stationary_regime | fails_at=multistability | —
A6: concept∈observable | observable-specific(integration_time,IC_size) | checked_last | —
```

---

## Partition Objects

```
θ*: invariant∈partition | BC_value@regime_boundary | θ*∈Z(π)→scope_transition | F4_risk@sweep_edge

ε_working: invariant∈partition | chosen_ε∈I_ε | center_of_plateau | written_to=Invariants.json

ε_plateau: interval∈partition | [ε_lo,ε_hi]_of_stable_N(ε) | width→robustness | —

Invariants.json: artifact∈case | {N*,θ*,ε_working,ε_plateau,sweep_range} | sweep_range_mandatory_for_TBS_norm | —
```

---

## Differential Diagnosis Index

Fast lookup for concepts that produce similar empirical signatures:

```
Z(π) vs Z_cover:
  Z(π)    — substrate failure (A0-A6), ε-independent, →F0
  Z_cover — gradient excess, ε-dependent, →F-gradient
  diagnostic: substrate_analysis(A0-A6)

F0 vs F-gradient:
  F0        — Z(π)≠∅, substrate broken, →observable_replacement
  F-gradient — ¬F0∩Z_cover≠∅, cause=high_∇O, →scope_refinement
  diagnostic: A0-A6 all satisfied? yes→F-gradient, no→F0

N(ε) trivial vs no plateau:
  trivial(|C_ε|=1) — span<2ε or fragmented, →F1
  no_plateau       — σ_Δ>ε* everywhere, →F3
  diagnostic: check_span_vs_ε then check_σ_Δ_globally

θ* as boundary vs scope_transition:
  boundary         — θ*∈R(π), robust under Δ
  scope_transition — θ*∈Z(π), observable collapses there
  diagnostic: check_Z(π)_at_θ*
```

---

## Notes for Next Tasks

Task 2 entries to produce:
- Falsification: F0, F1, F1_BC, F2, F3, F4, F-gradient, Z_shared (full)
- BC Taxonomy: COUPLING, RESTRICTION, DISSIPATION, FORCING, AGGREGATION, SYMMETRY_BREAKING
- Operator signatures: S1–S5

Task 3 entries to produce:
- Pipeline modules: sweep.py, stability_mask.py, epsilon_sweep.py,
  epsilon_kappa_map.py, epsilon_multi_observable.py, extract_partition.py,
  invariants.py, transfer.py, validate.py, audit.py, new_case.py
- Artifacts: ScopeSpec.yaml, BCManifest.yaml, CaseRecord.yaml,
  PartitionResult.json, TransferMetrics.json, FailureAudit.md

Task 4 entries to produce:
- Transfer metrics: Φ, RCD, TBS_norm, PCI, SDI
- Emergence: emergence_window, local_collapse, relational_collapse, collapse_ordering
- Active cases: CASE-20260311-0001 through CASE-20260330-0012
- Final assembly: context_map.yaml (machine-readable, all tasks merged)
