---
status: note
layer: schemas/
---

# Schemas

YAML and JSON schemas that define the structure of pipeline artifacts.
Each schema is the canonical reference for its artifact type.
When a new case is created via `pipeline.new_case`, copies of these schemas
are stamped with the case ID and placed in the case directory.

---

## Schema Files

| Schema | Format | Purpose |
|---|---|---|
| [ScopeSpec.yaml](ScopeSpec.yaml) | YAML | ART scope instantiation: state space X, boundary constraints B, observables Π, perturbations Δ, resolution ε, expected partition |
| [BCManifest.yaml](BCManifest.yaml) | YAML | BC classification, sweep program, distortion metrics plan |
| [CaseRecord.yaml](CaseRecord.yaml) | YAML | Case envelope: artifact registry, phase, status, go/no-go criteria, agent assignments |
| [RegimeGraph.schema.json](RegimeGraph.schema.json) | JSON Schema | Regime transition graph structure G_S |
| [TransitionTrials.schema.json](TransitionTrials.schema.json) | JSON Schema | Transition trial data format |
| [StudySpec.yaml](StudySpec.yaml) | YAML | **Study** declaration (validation strategy v2, Q-VAL-01): tier, question, sampled domain (no `sweep_range`), ε-family block, Δ-reachability rule, composition rule, preregistration binding. Draft v0.1 |
| [Preregistration_template.md](Preregistration_template.md) | Markdown | Frozen-before-run predictions, criteria, analysis plan; SHA-256 + git-tag freeze procedure. Draft v0.1 |
| [StudyRecord.yaml](StudyRecord.yaml) | YAML | Study outcome envelope: verdict against preregistered criteria only, mandatory deviations list, surplus-over-1D honesty field, no Φ across the 1D/general break. Draft v0.1 |

The three study schemas are consumed by `pipeline/validate_study.py` — **planned,
does not exist yet**; until then the `[MC]` checks in the StudySpec header are
performed by hand. Case schemas (ScopeSpec/BCManifest/CaseRecord) remain valid
for the frozen regression suite; new validation work uses the study unit
(`docs/notes/validation_strategy_v2.md`).

---

## Usage

Schemas are consumed by the pipeline modules (primarily `pipeline.validate`)
and referenced in the [PartitionPipeline design document](../pipeline/PartitionPipeline.md).

For the formal connection between these schemas and the ARW scope tuple
S = (B, Π, Δ, ε), see [docs/glossary/scope.md](../docs/glossary/scope.md).
