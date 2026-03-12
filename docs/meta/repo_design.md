# Repository Design Principles

This document summarizes the guiding design choices of the ARW repository.
It is intended both for human contributors and for LLM-based collaborators.

---

# Purpose

The repository is not merely a storage space for notes.
It is a **structured research environment** designed to preserve conceptual consistency, enable traceable development, and support cross-domain ARW/ART work over time.

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
Whenever possible, contributions should first clarify the structural role of a concept before expanding into implications.

This is especially important for ARW-level content.

---

## 4. ARW and ART are distinct layers

### ARW

ARW contains the formal meta-structure.
This includes:

- scope definitions
- operators
- admissibility structures
- regime partitions
- transfer relations

### ART

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

Where:

- **B** defines the boundary conditions
- **Π** defines the partition structure
- **Δ** defines admissibility
- **ε** defines tolerance / resolution

Contributions that affect structural claims should, where appropriate, indicate how they relate to one or more of these components.

---

## 6. Documentation is layered

The repository is designed in documentation layers rather than as one monolithic manuscript.
This makes navigation easier and reduces conceptual mixing.

Typical layers:

```text
docs/overview            entry points and orientation
docs/glossary            atomic concepts
docs/core                formal ARW structure
docs/advanced            advanced theoretical elaboration
docs/art_instantiations  domain-specific realizations
docs/notes               exploratory, provisional, or reflective material
experiments              computational and empirical workflows
cases                    generated outputs, datasets, or pipeline cases
figures                  visual support material
```

Contributors should prefer placing content into the narrowest fitting layer.

---

## 7. Atomic concepts beat overloaded documents

A concept that carries independent explanatory weight should generally have its own dedicated file.
This improves reuse, linking, and long-term maintainability.

Preferred pattern:

```text
one concept -> one file
one file -> one main purpose
```

Avoid mixing definitions, speculative outlooks, experimental proposals, and retrospective notes in a single undifferentiated document.

---

## 8. Status should always be legible

A reader should quickly be able to recognize what kind of content they are dealing with.
Possible status labels include:

- definition
- working-definition
- claim
- hypothesis
- interpretation
- experiment-proposal
- open-question
- note

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

# Practical Contribution Heuristic

Before adding or revising material, check the following:

1. **Layer** — Where does this belong?
2. **Level** — ARW or ART?
3. **Status** — Definition, claim, note, or proposal?
4. **Structure** — Does it relate to B, Π, Δ, ε?
5. **Traceability** — Can a future reader understand why it was added?
6. **Non-duplication** — Does this already exist elsewhere?

---

# Intended Contributor Behavior

Contributors, including LLMs, should behave as **caretakers of conceptual integrity**.
The task is not merely to produce text, but to preserve a research architecture in which concepts remain navigable, comparable, and revisable without collapsing into confusion.
