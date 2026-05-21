# To-REPO → arw-repo: Action Plan (2026-05-20)

Audit of `To-REPO/` against current `arw-repo/` state.
All 12 files in `To-REPO/` are **new to the repository** — no existing file is superseded.

---

## Overview of To-REPO Contents

| File | Type | Target Layer | Status |
|---|---|---|---|
| `EpistemicGeometry_Interactive.html` | HTML companion to Felder 2026 paper | `papers/` | New |
| `arw_aggregation_limits_typological_observables-1.md` | Advanced conceptual doc (complete version, 655 lines) | `docs/advanced/` | New |
| `arw_aggregation_limits_typological_observables.md` | Earlier draft of the above (399 lines, no §10) | — | Drop / archive |
| `arw_quantization_partition_stability.md` | Conceptual note | `docs/notes/` | New |
| `kht_architecture_index.md` | KHT series entry point | `docs/art_instantiations/` | New |
| `kht_architecture_layer1.md` | KHT Layer 1: Operator–Modulator Space | `docs/art_instantiations/` | New |
| `kht_architecture_layer2.md` | KHT Layer 2: Persistent Profiles | `docs/art_instantiations/` | New |
| `kht_architecture_layer3.md` | KHT Layer 3: Dynamic Regime Transitions | `docs/art_instantiations/` | New |
| `kht_architecture_layer4.md` | KHT Layer 4: AI Context Navigation Simulation | `docs/art_instantiations/` | New |
| `kht_arw_analysis_revised.md` | ARW Analysis of KHT (conceptual bridge doc) | `docs/art_instantiations/` | New |
| `kht_prescopal_substrate_hypotheses.md` | KHT biological substrate hypotheses | `docs/notes/` | New |
| `labyrinth_patch_op_mod_split.md` | Labyrinth S_online patch proposal | `experiments/` | New |

---

## Action Groups

### Group A — KHT Unified Architecture Series (highest priority, internally coupled)

Six files form a single coherent cluster. They reference each other via `part_of`,
`previous:`, `next:`, and `related:` frontmatter fields. They must be contributed
together or in layer order (1 → 2 → 3 → 4 → index → analysis).

**Files:**
- `kht_architecture_layer1.md` → `docs/art_instantiations/kht_architecture_layer1.md`
- `kht_architecture_layer2.md` → `docs/art_instantiations/kht_architecture_layer2.md`
- `kht_architecture_layer3.md` → `docs/art_instantiations/kht_architecture_layer3.md`
- `kht_architecture_layer4.md` → `docs/art_instantiations/kht_architecture_layer4.md`
- `kht_architecture_index.md` → `docs/art_instantiations/kht_architecture_index.md`
- `kht_arw_analysis_revised.md` → `docs/art_instantiations/kht_arw_analysis_revised.md`

**Pre-commit actions required:**
1. **Filename fix for analysis doc:** `kht_arw_analysis_revised.md` contains a
   `related: kht_arw_analysis.md` reference in its frontmatter. Since there is no
   prior version in the repo, this self-reference is a dangling pointer. Either:
   - Rename the file to `kht_arw_analysis.md` and remove the `related:` self-reference, OR
   - Keep the name and update frontmatter: replace `related: - kht_arw_analysis.md`
     with `revision_of: private draft (not in repo)`.
   **Recommendation:** rename to `kht_arw_analysis.md` (clean entry, no prior version).

2. **DOC_INDEX registration:** All six files must be registered in
   `docs/meta/DOC_INDEX.md` under the `art_instantiations` section.

3. **arw-meta-guard check** before finalizing each file.

**What these docs contribute:**
KHT (Kognitive Hierarchie Theorie) is a four-layer cognitive architecture:
- Layer 1: a fully symmetric 32-combination Operator × Modulator space (null model)
- Layer 2: 16 persistent profiles emerging via biological BCs (Restriction + Dissipation)
- Layer 3: four cognitive regimes with control-parameter-driven transitions
- Layer 4: computational instantiation as an AI context-navigation simulation

The ARW analysis (`kht_arw_analysis_revised.md`) maps all layers to ARW BC classes,
identifies admissible observables, and derives a candidate scope tuple. It is the
prerequisite for any future KHT-based ART case (related cases: CASE-20260315-SOC1,
CASE-20260328-0010).

---

### Group B — Advanced/Notes Conceptual Docs

Three standalone conceptual documents. Each is independently usable.

#### B1: Aggregation Limits of Typological Observables

**Source:** `arw_aggregation_limits_typological_observables-1.md` (655 lines — the complete version)
**Target:** `docs/advanced/arw_aggregation_limits_typological_observables.md`

**Important:** Two versions exist in To-REPO:
- `arw_aggregation_limits_typological_observables.md` (399 lines, ends at §9 Summary)
- `arw_aggregation_limits_typological_observables-1.md` (655 lines, extends with §10 ASM)

The `-1` version is **more complete**: it adds §10 "Toward an Aggregation Stability
Measure (ASM)" — a concrete quantitative framework (Variance Ratio Profile, N*
estimation, ICC equivalence). The shorter version is a prior draft.

**Action:** Copy `-1` version to repo as the canonical file (drop the `-1` suffix).
Archive or discard the 399-line version.

**Content summary:** Formalizes the "variance crossover problem" for typological
observables: every discrete-type observable (KHT, MBTI, Big Five, institutional
categories) has an aggregation level N* beyond which within-class variance exceeds
between-class variance, making the observable structurally uninformative. Maps to
ARW failure modes F1 and Z_shared. General claim; KHT used only as example.
Layer designation: `docs/advanced/` (correct per frontmatter).

**DOC_INDEX registration required.**

#### B2: Quantization as Scope-Relative Partition Stability

**Source:** `arw_quantization_partition_stability.md`
**Target:** `docs/notes/arw_quantization_partition_stability.md`

**Content summary:** Proposes that the appearance of discrete/quantized descriptions
across domains (quantum mechanics, biological species, psychological types) reflects
a common structural condition: a description is "quantized" iff its partition is
stable under the admissible perturbations Δ at resolution ε. Domain-neutral claim.
Layer designation: `docs/notes/` (per frontmatter, status: note — appropriate).

**Note:** The frontmatter `depends_on` lists
`docs/advanced/arw_aggregation_limits_typological_observables.md` — which only
exists after B1 is added. Contribution order: B1 before B2.

**DOC_INDEX registration required.**

#### B3: KHT Pre-Scopal Biological Substrate Hypotheses

**Source:** `kht_prescopal_substrate_hypotheses.md`
**Target:** `docs/notes/kht_prescopal_substrate_hypotheses.md`

**Content summary:** Lists explicit empirical hypotheses generated by KHT Layer 1's
architectural commitment to operator independence (Ni, Si, Ne, Se as orthogonal
axes). For each hypothesis, lists candidate neural substrates, confidence level, and
the dissociation evidence that would confirm or disconfirm it. Methodologically
careful (reverse inference caveat explicit). Status: hypothesis.

Layer designation: `docs/notes/` (per frontmatter — appropriate for hypothesis-grade
content with neurobiological scope that is not yet ART-pipeline-ready).

**Contribution order:** Should follow Group A (KHT series must exist for internal
references to resolve). Part_of `kht_unified_architecture` cluster.

**DOC_INDEX registration required.**

---

### Group C — Papers Directory

**Source:** `EpistemicGeometry_Interactive.html`
**Target:** `papers/EpistemicGeometry_Interactive.html`

The `papers/` directory already contains:
`Epistemic_Geometry_of_Descriptions__Cover_Stability_as_a_Criterion_for_Observable_Validity.pdf`

This HTML file is an **interactive companion** to that paper — it renders the paper
with live LaTeX (KaTeX), interactive widgets, and navigation. It is a self-contained
single-file HTML document.

**Action:** Copy directly to `papers/`. No frontmatter needed (HTML, not a .md doc).
Update `papers/README.md` to list both the PDF and the interactive HTML version.

**No DOC_INDEX registration needed** (DOC_INDEX covers .md conceptual docs only).

---

### Group D — Experiments

**Source:** `labyrinth_patch_op_mod_split.md`
**Target:** `experiments/labyrinth_patch_op_mod_split.md`

**Content summary:** A concrete patch proposal for the Labyrinth agent's `S_online`
scope. Splits the single weight vector `w` into two sub-vectors:
- `w_op` (5-dim): operator observables (content of situation: `d_exit`, `v_sight`,
  `e_edge`, `c_contact`, `p_progress`)
- `w_mod` (2-dim): modulator observables (processing context: `r_resource`, `m_cost`)

Motivated by KHT Layer 4's operator/modulator distinction. Includes Python code
snippets for the modified initialization and update logic. Scope: S_online internals
only — no changes to Policy Network, S_sleep, or S_observer.

Parent doc: `labyrinth_three_scope_minimal_setup.md` (already in `experiments/`).
Related cases: CASE-20260329-0011, CASE-20260330-0012.
Status: proposal.

**Action:** Copy to `experiments/`. Add to `experiments/README.md` (or the labyrinth
experiment agenda doc) as a pending patch. No DOC_INDEX registration needed
(experiments/ is pipeline/code layer, not docs/).

---

## Contribution Sequence

Respecting internal dependencies:

```
1. Group A: KHT series (layers 1–4 → index → analysis)
   └─ prerequisite for B3 (kht_prescopal_substrate_hypotheses references them)

2. Group B1: arw_aggregation_limits_typological_observables
   └─ prerequisite for B2 (quantization doc depends_on it)

3. Group B2: arw_quantization_partition_stability

4. Group B3: kht_prescopal_substrate_hypotheses

5. Group C: EpistemicGeometry_Interactive.html

6. Group D: labyrinth_patch_op_mod_split.md
```

---

## Housekeeping Items

| Item | Action |
|---|---|
| `arw_aggregation_limits_typological_observables.md` (399-line version) | Do NOT copy to repo. Archive locally or discard. |
| DOC_INDEX (`docs/meta/DOC_INDEX.md`) | Register all new .md docs from Groups A, B1, B2, B3 |
| `papers/README.md` | Add entry for `EpistemicGeometry_Interactive.html` |
| `kht_arw_analysis_revised.md` frontmatter | Fix dangling `related: kht_arw_analysis.md` ref |
| arw-meta-guard | Run for each file before commit |
| arw-doc-consistency | Run after all files are placed, to check for drift |

---

## What This Import Adds to the Repo

- **KHT is fully scaffolded:** The four-layer architecture gives the cognitive-typology
  domain a proper ARW treatment — from the symmetric null model (Layer 1) through
  biological BC-driven profile emergence (Layer 2), regime dynamics (Layer 3), and
  AI instantiation (Layer 4). This enables future `ScopeSpec_signature_first.md`
  documents for KHT-based ART cases.

- **Two new advanced concepts:** The variance crossover / aggregation limits framework
  (B1) and the quantization-as-partition-stability unification (B2) are general ARW
  results — applicable far beyond KHT, to any domain using typological or discrete
  observables.

- **Labyrinth patch:** Brings the operator/modulator split from KHT Layer 4 into the
  Labyrinth experiment design — a concrete KHT→ART transfer in the experimental pipeline.

- **Interactive paper companion:** Makes the Felder 2026 epistemic geometry paper
  explorable without a PDF reader.
