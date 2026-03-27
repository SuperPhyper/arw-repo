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

---

## Usage

Schemas are consumed by the pipeline modules (primarily `pipeline.validate`)
and referenced in the [PartitionPipeline design document](../pipeline/PartitionPipeline.md).

For the formal connection between these schemas and the ARW scope tuple
S = (B, Π, Δ, ε), see [docs/glossary/scope.md](../docs/glossary/scope.md).
