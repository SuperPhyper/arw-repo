# LLM Memory Map

This file provides a lightweight navigation map for LLMs and human collaborators.
Its purpose is to identify the most important conceptual anchors of the repository and to indicate how new contributions should orient themselves.

---

# 1. Canonical Orientation

When interacting with this repository, prefer the following reading order:

1. `README.md`
2. `docs/overview/ARW_in_one_page.md`
3. `docs/glossary/scope.md`
4. `docs/core/arw-operator.md`
5. neighboring glossary/core files relevant to the current task
6. only then: `docs/notes/`, `experiments/`, `cases/`

This order helps preserve the distinction between canonical structure and exploratory material.

---

# 2. Conceptual Priority Map

The following concepts should be treated as high-priority anchors.
New contributions should relate themselves to these concepts whenever relevant.

## Scope

Primary formal unit of analysis.
Canonical form:

```text
S = (B, Π, Δ, ε)
```

Use when discussing admissibility, partitioning, or the structural conditions under which a description holds.

## Boundary Conditions (B)

Defines the constraints, couplings, restrictions, or framing conditions under which a system is considered.

## Partition Structure (Π)

Defines how regimes, states, or admissible distinctions are separated or grouped.

## Admissibility (Δ)

Defines what counts as structurally valid, representable, or permissible inside the selected scope.

## Resolution / Tolerance (ε)

Defines granularity, tolerance, or the operational threshold at which distinctions are maintained or collapsed.

## ARW Operator

Formal transformation principle acting on scope structure and regime description.
Use for formal claims, transfer questions, or regime-generation logic.

## Regime / Regime Partition

Use when discussing emergent stable patterns, distinct classes of behavior, or structure induced by boundary conditions.

## Transfer / Scope Transfer

Use when asking whether conclusions or regime structures remain valid across different descriptions, systems, or abstraction levels.

## Observables

Use when linking a formal structure to what can actually be measured, tracked, or compared in an instantiation.

---

# 3. Repository Layer Map

Use this section to decide where new content belongs.

## `docs/overview`

Use for entry points, orientation texts, short conceptual overviews, and first-contact explanations.

## `docs/glossary`

Use for atomic concepts and short definitional files.
One concept per file whenever possible.

## `docs/core`

Use for central ARW formalism.
Place foundational operator logic, admissibility structure, and essential framework relations here.

## `docs/advanced`

Use for more difficult, extended, or theoretically richer elaborations that presuppose the core material.

## `docs/art_instantiations`

Use for domain-specific realizations of ARW or ART.
Examples: physical, social, computational, or organizational cases.

## `docs/notes`

Use for exploratory, provisional, reflective, or interpretive material.
Do not treat notes as automatically canonical.

## `experiments`

Use for executable workflows, pipeline logic, evaluation setups, or simulation-related structures.

## `cases`

Use for datasets, pipeline outputs, example runs, and generated result collections.

---

# 4. Content Status Map

When adding or revising a file, signal which type of content it is.
Recommended labels:

- `definition`
- `working-definition`
- `claim`
- `hypothesis`
- `interpretation`
- `experiment-proposal`
- `open-question`
- `note`

This prevents canonical definitions from becoming confused with exploratory speculation.

---

# 5. LLM Contribution Rules of Thumb

## Prefer this

- explicit placement
- explicit status
- explicit ARW/ART distinction
- modular concept files
- traceable revisions
- structure before interpretation

## Avoid this

- silently redefining terms
- mixing ARW formalism with ART examples in one undifferentiated passage
- treating notes as final doctrine
- adding broad speculative claims without placement or status markers
- duplicating concepts under new names without explanation

---

# 6. Suggested Prompting Heuristic for LLM Use

When working with the repository, an LLM should implicitly ask:

1. What layer of the repository am I in?
2. Is this ARW or ART?
3. Which canonical concept does this connect to?
4. Is this a definition, claim, note, or proposal?
5. Where should this contribution live so that future readers can find and reuse it?

---

# 7. Functional Role of This File

This file is not itself a source of new theory.
It is a navigation and memory aid.
Its role is to reduce drift, improve consistency, and help future contributors orient themselves inside the repository as a long-term conceptual memory system.
