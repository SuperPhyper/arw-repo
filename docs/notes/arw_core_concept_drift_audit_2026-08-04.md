---
status: note
layer: docs/notes/
date: 2026-08-04
related_docs:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/glossary/observable_range.md
  - docs/advanced/epsilon_and_scope_resolution.md
  - docs/core/cover_stability_criterion.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
  - docs/meta/context_map/context_map_pipeline.md
  - docs/notes/arw_theory_audit_2026-06-10.md
  - docs/notes/arw_audit_repair_plan_2026-06-10.md
  - docs/notes/ews_stage1_review_epsilon_vs_delta.md
---

# ARW Core-Concept Drift Audit — 2026-08-04

**Mandate.** One pass per ARW core concept, checking the canonical documents against
(a) each other, (b) the pipeline code, (c) the case artifacts, and (d) the newest
findings in `research_journal.md` and `open_questions.md`. This audit asks a narrower
question than `arw_theory_audit_2026-06-10.md`: not "is the theory defensible" but
"does the repo still say one thing about each concept, and is that thing current".

**Scope of the pass.** Scope tuple, falsification schema, σ_Δ / ε resolution regime,
observable analysis (R(π), Z, observable information), BC taxonomy, transfer metrics,
pipeline DAG, and the post-June conceptual clusters. Monograph drafts are outside this
repo and were not audited.

**Severity legend.** **D1** — doc contradicts code or another canonical doc; an agent
following canon does the wrong thing. **D2** — canon is behind a finding that is
already on record. **D3** — housekeeping / ambiguity that has not yet produced an error.

**Disposition legend.** ✅ fixed in this pass · ⚑ flagged, needs Rico's decision ·
◻ recorded as theory work.

---

## 0. Headline

The repo is in substantially better shape than its own maintenance snapshot suggests.
Front-matter compliance is 100% (242 non-README docs), `DOC_INDEX.md` has an entry for
every file including all twelve uncommitted ones, supersession chains are recorded with
reasons, and the June 2026 repair plan's repo-side work packages (WP-B1, WP-B2, WP-A4)
are genuinely executed rather than merely marked done.

Drift is concentrated in three places, in descending order of consequence: **the
doc→code interface** (canon points at a module that does not exist while the function it
describes lives elsewhere), **the machine-readable context maps** (v0.1, never resynced
after the 2026-06-02 transfer and σ_Δ work), and **the skill layer** (`arw-repo-pulse` is
three weeks stale and `arw-repo-context` still carries a metric definition the repo
formally rejected). Findings D-04 and D-13 are the two an agent would actually trip over.

---

## 1. Scope tuple S = (B, Π, Δ, ε)

Canon is coherent. `docs/glossary/scope.md` carries the INC-01 Čech upgrade (2026-06-10)
plus the 2026-07-17 operative-form clarification distinguishing the three readings of
"cover", and it states the open status of the X-structure question rather than silently
deciding it. No competing definition of the tuple was found in any layer.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-01 | `epsilon_and_scope_resolution.md` and `perturbation_spread.md` treat **both** ε and Δ only in their simulation-native forms. The 2026-08-04 EWS session established a three-way separation (ε_instr ≠ ε_operational ≠ Δ) and that Δ is undeclarable from metadata *in principle*, not accidentally. Q-EWS-04/05 registered; canon unchanged. | D2 | ◻ largest open theory update; see §8 |
| D-02 | The four formal gaps in the tuple (Q_NEW_1 X-structure, Q2 state-dependent ε, Q3 ε-vector, Q_NEW_18 joint-BC separation) are individually registered but nowhere collected. A reader of `scope.md` alone sees a complete tuple with one caveat. | D3 | ⚑ suggest a "known extensions" section in `scope.md` |

---

## 2. Falsification schema (F0–F4, F-gradient, Z_shared)

There is **no single canonical document for the falsification schema**. It is assembled
from `docs/glossary/observable_range.md` (F0, F-gradient, Z, Z_cover),
`docs/bc_taxonomy/bc_failure_signatures.md` (per-class table),
`schemas/ScopeSpec.yaml` (ids + severities) and
`docs/meta/context_map/context_map_falsification_bc.md` (the most complete single
statement, and the only place the F-category discriminations are written out). The
context map is doing source-of-truth work from the `meta` layer.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-03 | The corrected F1 criterion is `ε ≥ ε*(O,X)`; the shorthand `span(π) < 2ε` is valid only for connected O(X). The shorthand still appears without caveat in ~10 documents (`admissible_resolution_lower_bound.md`, `bc_extraction_method.md`, `observable_decomposition.md` §closing, `arw_for_ml.md`, `arw_for_neuroscience.md`, `arw_for_statistical_physics.md`, `arw_observer_scope.md`, `CASE_TEMPLATE_signature_first.md`, `research_report_CASE-20260328-0010.md`) and in the `observable_sufficiency` example comment of `schemas/ScopeSpec.yaml`. `bc_failure_signatures.md` and `observable_space_cover_height.md` have the corrected form — so the repo says both. | D1 | ⚑ blanket-correct vs. add one caveat line to the template + schema; decision needed (see §9) |
| D-04 | No canonical home for the F-schema. The most complete statement lives in a v0.1 context map whose header declares it a derived artifact. | D2 | ⚑ candidate: promote a `docs/core/falsification_schema.md` as source of truth, with the context map derived from it |

---

## 3. σ_Δ and the ε resolution regime

This is where the audit found its most consequential defect.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-05 | `pipeline/stability_mask.py` **does not exist** (planned, action item E-1/E-2), yet `epsilon_and_scope_resolution.md` §"binary stability mask" claimed the mask is computed "(exactly) in `pipeline/stability_mask.py`", and `perturbation_spread.md` §"Pipeline Computation" attributed the direct σ_Δ computation to it while describing `epsilon_kappa_map.py` as proxy-only. In fact `epsilon_kappa_map.py::compute_sigma_delta_windowed` has computed direct σ_Δ since 2026-06-02 (fields `sigma_delta_windowed`, `proxy_pointwise`, `proxy_localmax`, `pointwise_underestimates`). An agent following canon would look for a missing module and fall back on exactly the pointwise proxy that C1 invalidated at θ* — the one-sided false-negative failure mode. | **D1** | ✅ both documents corrected; `cover_stability_criterion.md` §6 table row corrected |
| D-06 | The same stale routing persists in `context_map_framework.md` and `context_map_falsification_bc.md` "Notes for Next Tasks" module lists (11 modules incl. `stability_mask.py`, excl. `sweep_behavioral.py`, `transfer_v2.py`, kernels). These are planning residue rather than canon. | D3 | ⚑ low priority; delete or refresh the two note blocks |
| D-07 | `cover_stability_criterion.md` was already current on the σ_Δ implementation (it names `compute_sigma_delta_windowed` explicitly) while the two glossary/advanced documents were not — the divergence sat inside the same concept cluster for two months. | D2 | ✅ resolved by D-05 fix |

---

## 4. Observable analysis (R(π), Z(π), Z_cover, observable information)

Coherent. `observable_range.md` carries the corrected single-ridge separatrix
(E_sep = ω₀²) with the correction history attached; `cover_stability_criterion.md` and
`framework_validation.md` retain the buggy value only inside explicit correction notes,
which is the right pattern. `observable_information.md` (Felder Def 6) is consistent with
`scope.md` and the cover criterion. Z(π) vs Z_cover discrimination is stated in three
places without divergence.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-08 | `observable_decomposition.md` (1054 lines, `status: claim`) closes with the uncaveated `span(π) < 2ε` form — see D-03. It is also the canonical home of the A0–A6 substrate inventory that F0 depends on, so the mismatch sits in a load-bearing document. | D1 | ⚑ part of the D-03 decision |

---

## 5. BC taxonomy

No definitional drift. Six classes, 5+1 relational reading, hedged consistently
(`bc_relational_structure.md` explicitly keeps "why exactly six" open as Q-REL-03).
The empirical picture, however, has moved and the repo's own commentary has not.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-09 | The 2026-06-10 audit's finding B2 states that "Dissipation, Forcing, Symmetry Breaking and Aggregation have zero pipeline-validated cases" and that CASE-0005–0008 are open. On disk, **CASE-20260315-0005 (Dissipation, `pendulum_gamma`) and CASE-20260315-0007 (Aggregation, `sir_epidemic`) both carry `decision: "go"`, full `results/partition/` output and transfer runs** (0007 is `status: complete`). Four of six classes now have at least one pipeline-run anchor. This strengthens the framework's position and should be reflected wherever B2 is cited. | D2 | ⚑ B2 is a note in `docs/notes/`; recommend an amendment line rather than an edit to the historical audit |
| D-10 | CASE-0005 and CASE-0007 each hold **two divergent copies** of ScopeSpec/BCManifest/CaseRecord: bare-name files (June 2026, used by the pipeline) and `CASE-<id>_*.yaml` prefixed files (March 2026, superseded, 111–297 diff lines). Nothing marks which is canonical. `validate.py` is not currently protected against reading the stale pair. | D1 | ⚑ needs Rico's call: archive the March triples under `archive/`, or add a `superseded:` front-matter marker |

---

## 6. Transfer metrics

The WP-A4 decision (SDI keeps graph-edit-distance; plateau-width similarity does not get
the name) and the 2026-07-17 amendment (SDI constructively collinear with RCD in the
1D-sweep tier, w₄ = 0, independent-information requirement) are executed in
`transfer_distortion_metrics.md`. Φ v2 in the document is channel-mapped to
`transfer_v2.py` including the actual weights (0.55 / 0.25 / 0.20) and both guards
(VOID, TRIVIAL_PARTITION) — verified against the code, matches.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-11 | `transfer_distortion_metrics.md` contradicted **itself**: the closing "Using the Metrics Together" section still required "all four" metrics and asserted "RCD = 0, TBS ≈ 0, PCI ≈ 1, but SDI > 0" — a configuration the same document's SDI section proves impossible in the sweep tier. | D1 | ✅ section reconciled; tier column and independent-information requirement added |
| D-12 | v1 Φ/PCI values are withdrawn as BC-class evidence, but v1 `transfer/<comparison>/` directories still sit beside v2 output in CASE-0001, 0002, 0003, 0004, 0005, 0007, 0013 with no in-directory marker. Only CASE-0007's transfer output is v1-only. | D2 | ⚑ suggest a one-line `README` stamp in each v1 transfer dir, or a `superseded: true` key in the JSON |
| D-13 | The `arw-repo-context` **skill** still defines `SDI = 1 − \|w_A − w_B\| / max(w_A, w_B)` — the plateau-width quantity that WP-A4 explicitly ruled *not* to be SDI — and gives the superseded four-term Φ. The skill is loaded at the start of every session, so this is the highest-traffic stale definition in the system. | **D1** | ⚑ skill refresh (out of this pass's remit; see §9) |

---

## 7. Pipeline

Code is ahead of its documentation, consistently in the same direction: the modules
implement the post-C1/C2 methods, the maps still describe the pre-June state.

| ID | Finding | Sev | Disposition |
|---|---|---|---|
| D-14 | `context_map_pipeline.md` (v0.1) put `stability_mask.py` in the DAG chain, named `transfer.py` as the transfer stage, and omitted `sweep_behavioral.py`, `transfer_v2.py` and `pipeline/kernels/`. | D1 | ✅ DAG, module entries and transfer stage corrected in place |
| D-15 | The pipeline map is versioned `0.1` with no `last_updated`; the transfer/cases map is at `0.3` with an internal `version: "0.2"` block. Version discipline across the four maps is inconsistent, which is why D-14 was invisible. | D3 | ⚑ suggest `last_updated` in all four map headers |

---

## 8. Newest clusters and the theory-update queue

Everything registered since 2026-06-02 is indexed and cross-referenced; no orphans, no
ID collisions (the apparent `Q-CNS-06` / `Q-SCA-06` duplicates are parent/sub-question
pairs, not collisions). The Q-prefix space has grown from 9 to **22 active prefixes**;
`open_questions.md` records collision checks per import, which is why the growth has been
safe, but there is no single prefix registry table in the repo — the only one that existed
is in a skill and lists 9.

The substantive theory-update queue, in the order the repo's own records rank it:

1. **ε/Δ on observational data (Q-EWS-04/05).** Journal 2026-08-04 calls this "the largest
   framework gain of the whole EWS episode". Needs: the specification → ε_operational
   mapping rule, and the Δ-as-declared-family form Δ_min ⊆ … ⊆ Δ_max with verdict
   stability required across it. Target documents named explicitly in the journal:
   `epsilon_and_scope_resolution.md`, `perturbation_spread.md`.
2. **F-schema source of truth (D-04)** and the F1 shorthand decision (D-03).
3. **Case-canon hygiene (D-10)**, which blocks any clean re-run of CASE-0005/0007.
4. **Σ-comparison procedure** — still the open frontier that Φ's demotion (WP-A3) left
   exposed; `bc_signature_forward_derivation.md` is the strongest available material and
   is not yet wired into the transfer workflow (WP-A5 / `SignatureTransfer.json` proposed
   2026-07-02, not built).

---

## 9. Decisions — all settled 2026-08-04 (Rico)

| # | Decision | Resolution | Executed |
|---|---|---|---|
| 1 | F1 shorthand (D-03, D-08) | **Option (b)** — correct the canonical/schema documents; leave instantiation documents with the shorthand plus a pointer | ✅ |
| 2 | F-schema home (D-04) | **Promote** `docs/core/falsification_schema.md` as source of truth; context map becomes a derived rendering | ✅ |
| 3 | Duplicate case YAMLs (D-10) | **Archive** the March triples | ✅ |
| 4 | v1 transfer output (D-12) | **Stamp** the directories | ✅ |
| 5 | Skill refresh (D-13) | Regenerate `arw-repo-pulse` wholesale, patch `arw-repo-context` | ✅ |

### Execution notes

**1 — F1 shorthand.** `schemas/ScopeSpec.yaml` example comments now state ε* and require
the connectedness claim whenever span is reported as supporting evidence;
`docs/cases/CASE_TEMPLATE_signature_first.md` and `docs/advanced/observable_decomposition.md`
carry the general criterion. Seven instantiation documents
(`admissible_resolution_lower_bound.md`, `bc_extraction_method.md`, `arw_for_ml.md`,
`arw_for_neuroscience.md`, `arw_for_statistical_physics.md`, `arw_observer_scope.md`,
`research_report_CASE-20260328-0010.md`) received a one-block **F1 notation** pointer
after their H1, scoping the shorthand to connected images and linking the canonical
schema. The shorthand itself was deliberately not rewritten in those files.

**2 — F-schema promotion.** `docs/core/falsification_schema.md` created. Beyond
consolidating F0–F4 / F1_BC / F-gradient / Z_shared, the pairwise discriminations and the
severity enum, it captures the **Part VII V3.2 revisions that existed only inside the
context map**: the revised decision order F0 → F4 → F1 → F3 → F2 → F-gradient (F2 is
uninterpretable while F4 is live), the A6 split (invalid → F0 / valid-but-unresolving →
F1), claim-relative F1 with total collapse as the pipeline-tested special case, the
F-gradient mass criterion μ(χ=1)/μ(X_B) > τ_∂, and the caveat that "never lower ε" is a
proxy-based pipeline convention rather than a χ-theorem. `context_map_falsification_bc.md`
bumped to v0.2 with a `derived_from` key and a banner stating that the core document wins.

**3 — Archive.** Six files moved to `archive/cases/CASE-20260315-{0005,0007}_march_drafts/`
with per-directory READMEs recording which values the surviving bare-name files produced.
`archive/README.md` gained both entries and a rule: a case directory holds exactly one
copy of each artifact; bare name is canonical where both exist. Cases 0006/0008/0009/SOC1
carry only prefixed filenames — a naming inconsistency, not a duplication, left as is.

**4 — Stamps.** `SUPERSEDED_v1.md` written into all six legacy `transfer/<comparison>/`
directories, each naming the v1 PCI defect, the superseding v2 run (or its absence), and
the v1 values for provenance. `archive/README.md`'s transfer index carries the same
withdrawal notice.

**New finding during execution — D-16.** Two cases contained a **doubled output path**,
`cases/<id>/cases/<id>/transfer/`, holding byte-identical copies of their v1 transfer
output (0007 and 0004, both written 2026-06-02 from a run invoked with the case root
already in the path argument). The CASE-0004 copy held an unstamped second instance of
the **Φ = 0.9983 `highly_admissible`** result that `framework_validation.md` was built on
and that the v2 recomputation replaced with Φ = 0.7794 `ambiguous_requires_inspection` —
a live miscitation surface that stamping the outer directory alone would have missed.
Files moved to `archive/cases/*_nested_path_artifact/`; the emptied nested directories
could not be removed from the audit workspace and need a manual `rm -r`.

---

## Changes applied in this pass

| File | Change |
|---|---|
| `docs/advanced/epsilon_and_scope_resolution.md` | stability-mask computation re-attributed to `epsilon_kappa_map.py::compute_sigma_delta_windowed`; `stability_mask.py` marked not implemented |
| `docs/glossary/perturbation_spread.md` | "Pipeline Computation" section rewritten to the implemented windowed estimator, with the C1 caveat and the correct output fields |
| `docs/core/cover_stability_criterion.md` | §6 concept-map row for M_stable re-pointed to the implemented module |
| `docs/bc_taxonomy/transfer_distortion_metrics.md` | "Using the Metrics Together" reconciled with the 2026-07-17 SDI amendment; tier column + independent-information requirement added |
| `docs/meta/context_map/context_map_pipeline.md` | DAG corrected; `stability_mask.py` entry demoted to not-implemented with a pointer to the real location; `epsilon_kappa_map.py` entry records both estimators; `transfer_v2.py` added as canonical, `transfer.py` marked deprecated with its defect |

All five are corrections of statements the repo elsewhere already contradicts — no new
claims, no reinterpretation of B, Π, Δ or ε.

### Second pass (after the decisions of §9)

| File | Change |
|---|---|
| `docs/core/falsification_schema.md` | **new** — canonical falsification schema (decision 2) |
| `docs/meta/context_map/context_map_falsification_bc.md` | marked derived, v0.1 → v0.2, `derived_from` key + precedence banner |
| `schemas/ScopeSpec.yaml` | `observable_sufficiency` example comments restated in ε* terms (decision 1) |
| `docs/cases/CASE_TEMPLATE_signature_first.md` · `docs/advanced/observable_decomposition.md` | F1 stated as `ε ≥ ε*(O, X_B)` with the shorthand scoped and linked |
| 7 instantiation documents | F1-notation pointer block added (decision 1, option b) |
| `archive/cases/CASE-20260315-{0005,0007}_march_drafts/` | **new** — 6 archived YAMLs + READMEs (decision 3) |
| `archive/cases/CASE-2026{0315-0007,0318-0004}_nested_path_artifact/` | **new** — 4 archived duplicates + READMEs (D-16) |
| `archive/README.md` | case index extended; one-copy rule stated; v1-Φ withdrawal notice added to the transfer index |
| 6 × `cases/*/transfer/<comparison>/SUPERSEDED_v1.md` | **new** — v1 stamps (decision 4) |
| `docs/meta/DOC_INDEX.md` | `falsification_schema.md` registered; audit entry updated |
| skills `arw-repo-pulse`, `arw-repo-context` | regenerated / patched (decision 5) |

### Still open after this pass

- The emptied nested directories `cases/CASE-20260315-0007/cases/` and
  `cases/CASE-20260318-0004/cases/` need a manual `rm -r`.
- D-02 (collect the four scope-tuple gaps in `scope.md`), D-06 (stale module lists in the
  "Notes for Next Tasks" blocks of two context maps), D-15 (`last_updated` discipline
  across the four maps) — all D3, deliberately not executed.
- The theory-update queue in §8 is unchanged: Q-EWS-04/05 remains the top item.
