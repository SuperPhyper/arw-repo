# LLM Contribution Charter

This document defines how language models (LLMs) should interact with this repository.

The repository serves as a **structured persistent memory** for the development of the ARW/ART research program.
LLM contributions should therefore prioritize **traceability, conceptual clarity, and structural consistency** over stylistic improvements.

---

# Core Principles

## 1. Traceability over novelty

LLM contributions must make their reasoning transparent.

Whenever a change or suggestion is made, it should include:

- the **motivation**
- the **location within the repository structure**
- the **relation to existing concepts**

Prefer explicit reasoning over stylistic rewrites.

---

## 2. Respect the ARW / ART separation

The repository distinguishes between:

### ARW — Allgemeine Regime-Wissenschaft

The formal meta-framework that defines:

- scopes
- operators
- admissibility
- regime partitions
- transfer conditions

ARW statements should remain **domain-neutral and formal**.

### ART — Allgemeine Regime-Theorie

ART describes **domain-specific instantiations** of ARW.

Examples include:

- physical systems
- social systems
- computational systems
- experimental pipelines

LLM contributions must **not mix these levels**.

---

## 3. Preserve scope-based reasoning

ARW analysis is structured around the concept of a **scope**:

```text
S = (B, Π, Δ, ε)
```

Where:

- **B** — boundary constraints selecting admissible states (X_B ⊆ X)
- **Π** — admissible descriptions or projections (observables); each π ∈ Π maps states to a descriptive space
- **Δ** — admissible perturbations; defines the robustness conditions under which regime distinctions must remain stable
- **ε** — resolution threshold; d_Π(x, y) ≤ ε means x and y are indistinguishable under scope S

These definitions are canonical. Do not reinterpret them.
The authoritative source is `docs/glossary/scope.md`.

LLM contributions should express structural claims in relation to these elements whenever possible.

---

## 4. Maintain layered documentation

The repository uses layered documentation.

LLMs should place contributions into the correct layer.

Layers and their purposes:

| Layer | Path | Purpose |
|---|---|---|
| overview | `docs/overview/` | Entry points, conceptual orientation, operator definition |
| glossary | `docs/glossary/` | Atomic definitions — one concept per file |
| core | `docs/core/` | Central ARW formalism: scope reduction, regime stability, transitions |
| advanced | `docs/advanced/` | Deeper theoretical elaboration: ε, emergence, engineering |
| art_instantiations | `docs/art_instantiations/` | Domain-specific ARW/ART realizations |
| bc_taxonomy | `docs/bc_taxonomy/` | Boundary condition classification, partition types, transfer metrics |
| context_navigation | `docs/context_navigation/` | Cognitive architecture application of ARW |
| cognitive_architecture | `docs/cognitive_architecture/` | ARW/ART instantiation for cognition |
| related_fields | `docs/related_fields/` | Connections to existing literature |
| pipelines | `docs/pipelines/` | Pipeline design documentation |
| figures | `docs/figures/` | Figure descriptions and visual support |
| notes | `docs/notes/` | Exploratory, provisional, or reflective material |
| experiments | `experiments/` | Executable workflows and simulation designs |
| cases | `cases/` | Pipeline outputs, datasets, experiment cases |
| meta | `docs/meta/` | LLM contribution rules, navigation aids, repo design |

---

## 5. Use explicit status markers

Every contribution should signal its epistemic status using a YAML front-matter block:

```yaml
---
status: working-definition
---
```

Recommended labels:

```text
definition
working-definition
claim
hypothesis
experiment-proposal
interpretation
open-question
note
```

This allows readers to distinguish:

- formal structure
- empirical claims
- speculation

---

## 6. Prefer atomic conceptual units

Concepts should be modular.

Avoid large documents that mix:

- definitions
- interpretations
- applications
- speculation

Instead prefer:

```text
one concept -> one document
```

---

## 7. Avoid hidden conceptual drift

LLMs must **not silently change definitions**.

If a definition changes:

- explicitly mark the change
- explain the motivation
- reference the previous definition

This rule applies to the scope tuple components in particular.
The canonical definitions of B, Π, Δ, ε are stable and must not be reinterpreted without explicit revision of `docs/glossary/scope.md`.

---

# Suggested Contribution Format

When proposing new material, use the following structure:

```md
# Title

## Status
definition | draft | hypothesis | experiment-proposal

## Purpose
Why this concept or document exists.

## Relation to ARW
How it relates to:

- scope structure (B, Π, Δ, ε)
- regime partitions
- transfer conditions
- observables

## Core Statement
The central definition or claim.

## Formal Structure
If applicable:

B =
Π =
Δ =
ε =

## Implications
Possible interpretations or consequences.

## Limits
Known limitations.

## Open Questions
Outstanding research questions.

## Suggested Placement
Recommended repository location.
```

---

# Role of the Repository

This repository is intended to function as a **long-term conceptual memory system** for the ARW research program.

Its purpose is to support:

- reproducible research
- concept evolution
- cross-domain comparison of regime structures
- transparent theoretical development

LLMs interacting with the repository should therefore behave less like editors and more like **research collaborators preserving conceptual integrity**.
