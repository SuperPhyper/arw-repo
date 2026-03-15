---
status: working-definition
layer: docs/meta/
---

# Repository Design Principles

This document summarizes the guiding design choices of the ARW repository.
It is intended both for human contributors and for LLM-based collaborators.

---

# Purpose

The repository is not merely a storage space for notes.
It is a **structured research environment** designed to preserve conceptual consistency,
enable traceable development, and support cross-domain ARW/ART work over time.

The repository should therefore be treated as:

- a conceptual memory system
- a documentation architecture
- a research scaffold
- a place where formal structure and empirical instantiation remain distinguishable

---

# Design Principles

## 1. Consistency over accumulation

New material should fit the existing architecture.
The goal is not to collect as much content as possible, but to preserve conceptual coherence.

Questions to ask before adding content:

- Does this belong to ARW or ART?
- Is this a definition, a claim, a note, or an experiment?
- Does this introduce conceptual drift?
- Does this duplicate an existing concept?

---

## 2. Traceability over convenience

Changes should be explainable.
A contribution should not only say *what* is being added, but also *why* and *where it belongs*.

Traceable contributions typically specify:

- motivation
- relation to neighboring concepts
- suggested placement
- epistemic status

---

## 3. Formal first, interpretation second

The repository distinguishes between formal structure and interpretive extension.
Whenever possible, contributions should first clarify the structural role of a concept
before expanding into implications.

This is especially important for ARW-level content.

---

## 4. ARW and ART are distinct layers

### ARW — Allgemeine Regime-Wissenschaft

ARW contains the formal meta-structure.
This includes:

- scope definitions
- operators
- admissibility structures
- regime partitions
- transfer relations

### ART — Allgemeine Regime-Theorie

ART contains concrete instantiations of ARW in a domain.
This includes:

- physical realizations
- social or organizational cases
- computational pipelines
- empirical studies

A clean repository contribution should make explicit which layer it addresses.

---

## 5. Scope structure is foundational

Reasoning in the repository is organized around the scope tuple:

```text
S = (B, Π, Δ, ε)
```

The canonical definitions are stable and must not be silently reinterpreted:

| Component | Canonical meaning | Source |
|---|---|---|
| **B** | Boundary constraints — select admissible states X_B ⊆ X | `docs/glossary/scope.md` |
| **Π** | Admissible descriptions or projections (observables) — each π ∈ Π maps states to a descriptive space | `docs/glossary/scope.md` |
| **Δ** | Admissible perturbations — robustness conditions; distinctions must hold under all δ ∈ Δ | `docs/glossary/scope.md` |
| **ε** | Resolution threshold — d_Π(x, y) ≤ ε means x ~_S y | `docs/glossary/scope.md` |

Contributions that affect structural claims should indicate how they relate to
one or more of these components.

---

## 6. Documentation is layered

The repository is designed in documentation layers rather than as one monolithic manuscript.
This makes navigation easier and reduces conceptual mixing.

```text
docs/overview/           entry points, orientation, ARW operator definition
docs/glossary/           atomic concepts — one file per concept
docs/core/               central ARW formalism: scope reduction, regime stability, transitions
docs/advanced/           advanced theoretical elaboration: ε, emergence, engineering
docs/art_instantiations/ domain-specific ARW/ART realizations
docs/bc_taxonomy/        BC classification, partition types, transfer metrics
docs/context_navigation/ cognitive architecture application of ARW
docs/cognitive_architecture/ ARW/ART instantiation for cognition
docs/related_fields/     connections to existing literature
docs/pipelines/          pipeline design documentation
docs/figures/            figure descriptions
docs/notes/              exploratory, provisional, or reflective material
docs/meta/               LLM contribution rules, navigation aids, repo design
experiments/             computational and empirical workflows
cases/                   generated outputs, datasets, pipeline cases
figures/                 image files (PNG, SVG)
pipeline/                Python implementation of the partition pipeline
schemas/                 YAML/JSON schemas for pipeline artifacts
```

Contributors should prefer placing content into the narrowest fitting layer.

---

## 7. Atomic concepts beat overloaded documents

A concept that carries independent explanatory weight should generally have its
own dedicated file.
This improves reuse, linking, and long-term maintainability.

Preferred pattern:

```text
one concept -> one file
one file -> one main purpose
```

Avoid mixing definitions, speculative outlooks, experimental proposals,
and retrospective notes in a single undifferentiated document.

---

## 8. Status should always be legible

A reader should quickly be able to recognize what kind of content they are dealing with.

Use YAML front-matter at the top of every non-README document:

```yaml
---
status: working-definition
---
```

Possible status labels:

- `definition`
- `working-definition`
- `claim`
- `hypothesis`
- `interpretation`
- `experiment-proposal`
- `open-question`
- `note`

This helps preserve the distinction between canonized structure and exploratory material.

---

## 9. Changes should preserve conceptual lineage

Definitions may evolve, but this evolution should be visible.
Contributors should avoid silent redefinition.

When revising a concept, document:

- what changed
- why it changed
- what problem the revision solves
- whether older wording remains useful in a narrower context

---

## 10. The meta layer describes, not prescribes theory

The `docs/meta/` layer contains navigation and contribution rules.
It is not a source of ARW theory.

Files in `docs/meta/` must themselves be consistent with the canonical definitions
in `docs/glossary/` and `docs/overview/`.
If a conflict exists between `docs/meta/` and `docs/glossary/scope.md`,
the glossary takes precedence.

---

# Practical Contribution Heuristic

Before adding or revising material, check the following:

1. **Layer** — Where does this belong?
2. **Level** — ARW or ART?
3. **Status** — Definition, claim, note, or proposal?
4. **Structure** — Does it relate to B, Π, Δ, ε? Are those terms used canonically?
5. **Traceability** — Can a future reader understand why it was added?
6. **Non-duplication** — Does this already exist elsewhere?

---

# Intended Contributor Behavior

Contributors, including LLMs, should behave as **caretakers of conceptual integrity**.
The task is not merely to produce text, but to preserve a research architecture in which
concepts remain navigable, comparable, and revisable without collapsing into confusion.
