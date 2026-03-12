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

### ARW — Allgemeine Resonanzwissenschaft

The formal meta-framework that defines:

- scopes
- operators
- admissibility
- regime partitions
- transfer conditions

ARW statements should remain **domain-neutral and formal**.

### ART — Applied Resonance Theory

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

- **B** — boundary conditions
- **Π** — partition structure
- **Δ** — admissibility rules
- **ε** — resolution / tolerance

LLM contributions should express structural claims in relation to these elements whenever possible.

---

## 4. Maintain layered documentation

The repository uses layered documentation.

LLMs should place contributions into the correct layer.

Typical layers include:

```text
docs/overview
docs/glossary
docs/core
docs/advanced
docs/art_instantiations
docs/notes
experiments
cases
```

Guideline:

| Layer | Purpose |
|------|--------|
| overview | entry points and conceptual overview |
| glossary | atomic definitions |
| core | core ARW structure |
| advanced | deeper theoretical work |
| art_instantiations | domain-specific applications |
| notes | exploratory or interpretative work |
| experiments / cases | empirical implementations |

---

## 5. Use explicit status markers

Every contribution should signal its epistemic status.

Recommended labels:

```text
definition
working-definition
claim
hypothesis
experiment-proposal
interpretation
open-question
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

---

# Suggested Contribution Format

When proposing new material, use the following structure.

```md
# Title

## Status
definition | draft | hypothesis | experiment-proposal

## Purpose
Why this concept or document exists.

## Relation to ARW
How it relates to:

- scope structure
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
