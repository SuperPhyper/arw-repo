# To-REPO → ARW Repository: Action Plan (2026-05-22, Session 3)

**Files in To-REPO:** 9 (4 new since this morning's session, old carry-overs cleaned up)
**New content:** 3 neue KHT-Docs + 1 meta-Index + 1 weiteres Update am Quantization-Doc
**No-action files:** 4 (already imported or superseded by current version)

---

## Delta Summary

| File | Bytes | Lines | Status |
|---|---|---|---|
| `kht_state_notation.md` | 19 940 | 550 | **NEW** → `docs/art_instantiations/` |
| `kht_group_dynamics.md` | 21 618 | 447 | **NEW** → `docs/art_instantiations/` |
| `kht_applications_clinical_cognitive.md` | 26 589 | 590 | **NEW** → `docs/art_instantiations/` |
| `kht_doc_index.md` | 18 298 | 419 | **NEW** → `docs/art_instantiations/` (frontmatter fix needed) |
| `arw_quantization_partition_stability.md` | 47 632 | 974 | **UPDATE** → supersedes today's 748-line import (+226 lines, §3.6 new) |
| `arw_quantization_partition_stability-1.md` | 30 317 | 748 | Already in repo (today's session) — no action |
| `arw_aggregation_limits_typological_observables.md` | 28 615 | 631 | Already handled — repo (655 lines) is more complete |
| `arw_aggregation_limits_typological_observables-1.md` | 30 317 | 655 | Already in repo — exact match |

---

## Group A — New KHT Applied Theory (3 files)

### A1: kht_state_notation.md → docs/art_instantiations/kht_state_notation.md

**Content:** KHT State Notation — a quantum-number-analogous formalism for encoding
cognitive state-space positions. Notation `|O, M, R, w, θ⟩` encodes operator, modulator
cluster, current regime, function weight, and regime distance parameter. Defines symmetry
operations (duality D, regime transitions), compatibility conditions, and scope limitations.

**Status/Layer:** `working-definition` / `docs/art_instantiations/` ✓ (already in frontmatter)
**Depends on:** kht_architecture_layer1–3, arw_quantization_partition_stability
**Meta-guard:** Frontmatter complete; ARW level is ART (KHT-specific); GUARD-9 English ✓
**DOC_INDEX:** New entry needed

---

### A2: kht_group_dynamics.md → docs/art_instantiations/kht_group_dynamics.md

**Content:** KHT Group Dynamics — collective regime structure and metastable attractor
ensembles. The central concept is the **collective regime manifold**: the set of
simultaneously admissible collective attractor tendencies before a dominant regime
stabilizes. Explicitly *not* a quantum claim — classical metastability description
grounded in KHT coupling structure. Covers regime lock-in dynamics, scope boundary
conditions for groups vs. individuals, and falsifiable predictions for team composition.

**Status/Layer:** `hypothesis` / `docs/art_instantiations/` ✓ (already in frontmatter)
**Depends on:** kht_architecture_layer3, kht_state_notation, kht_arw_analysis (in repo as kht_arw_analysis.md)
**Cross-reference:** CASE-20260328-0010
**Meta-guard:** Frontmatter complete; explicitly disclaims quantum ontology; GUARD-9 English ✓
**DOC_INDEX:** New entry needed

---

### A3: kht_applications_clinical_cognitive.md → docs/art_instantiations/kht_applications_clinical_cognitive.md

**Content:** KHT Applications — clinical and cognitive research hypotheses. Five
empirically tractable hypotheses derived from the state notation and four-layer
architecture: profile stability as a measurable variable, regime transitions as
predictable events, SD/UD developmental subtypes as scope-dependent phenomena,
therapeutic implications of Shadow-block accessibility, cognitive load as regime
destabilization. Each hypothesis has formal derivation + empirical prediction +
minimal test design + explicit scope limits.

**Status/Layer:** `hypothesis` / `docs/art_instantiations/` ✓ (already in frontmatter)
**Depends on:** kht_state_notation, kht_architecture_layer2–3, kht_prescopal_substrate_hypotheses
**Meta-guard:** Explicit "no diagnostic claims" caveat; hypotheses marked falsifiable; GUARD-9 English ✓
**DOC_INDEX:** New entry needed

---

## Group B — kht_doc_index.md (meta question)

**Content:** Session-level navigation index covering all 14 documents produced in this
working cluster (Clusters A–D). Provides reading order, key results summaries per doc,
dependency graph, and repo layer assignments. More detailed than the existing
`kht_architecture_index.md` — that covers the 4-layer architecture only; this covers
the full extended set including state_notation, group_dynamics, applications, etc.

**Decision: Import as** `docs/art_instantiations/kht_doc_index.md`

Rationale: The doc-consistency anti-pattern "creating a summary doc that repeats other
docs → create a navigation entry in docs/meta/ instead" applies to *redundant* content.
This index has genuine added value: compact key-results summaries and dependency
structure not available elsewhere. The existing `kht_architecture_index.md` companion
precedent supports this placement.

**Frontmatter fix required:**
- `status: index` → `status: note` (non-standard; closest valid value is `note`)
- `layer: docs/` → `layer: docs/art_instantiations/`
- Remove `title:` field if desired (optional — keep for clarity)

**DOC_INDEX:** New entry needed

---

## Group C — arw_quantization_partition_stability update

**Current repo version:** 748 lines (imported this morning)
**New version:** 974 lines (+226 lines, adds §3.6)

### New §3.6: Latent Degrees of Freedom and the Descriptive Collapse (L485–711)

Six sub-sections:
- **§3.6.1** Quantum Numbers as Reduced Coordinates — quantum numbers as coordinates
  on π(X_B), not full state descriptors; latent DoF as present-but-unstably-distinguishable
- **§3.6.2** The Structure of Latency — formal definition: f is latent in S ⟺ variation
  in f does not produce stably distinguishable changes under Π; three mechanisms
- **§3.6.3** Descriptive Collapse: X → π(X_B) — the compression from full state space
  to partition-labeled classes; information lost vs. made reliable
- **§3.6.4** Effective Field Theory as Systematic Latency Management — EFT as the
  physics of selective latency: integrating out high-energy DoF = making them latent
  at the low-energy scope
- **§3.6.5** Spontaneous Symmetry Breaking as Latency Inversion — SSB as the emergence
  of a new stable partition class from a previously latent DoF
- **§3.6.6** The Central Thesis, Restated — quantization = selective latency + stable
  partition; the observable description is the residue after latency compression

**Target:** Same path `docs/notes/arw_quantization_partition_stability.md` (overwrite)
**Frontmatter:** unchanged (`status: note`, `layer: docs/notes/`)
**DOC_INDEX:** Update note field (add §3.6 description)

---

## Execution Checklist

### Group A (3 new KHT docs)
- [ ] Copy kht_state_notation.md → docs/art_instantiations/kht_state_notation.md
- [ ] Copy kht_group_dynamics.md → docs/art_instantiations/kht_group_dynamics.md
- [ ] Copy kht_applications_clinical_cognitive.md → docs/art_instantiations/kht_applications_clinical_cognitive.md
- [ ] Add DOC_INDEX entries for all 3

### Group B (kht_doc_index)
- [ ] Fix frontmatter: status → note, layer → docs/art_instantiations/
- [ ] Copy to docs/art_instantiations/kht_doc_index.md
- [ ] Add DOC_INDEX entry

### Group C (quantization update)
- [ ] Overwrite docs/notes/arw_quantization_partition_stability.md with 974-line version
- [ ] Update DOC_INDEX note field (add §3.6)

### Final
- [ ] Run meta-guard verification on all 5 modified files
- [ ] Verify DOC_INDEX consistency
