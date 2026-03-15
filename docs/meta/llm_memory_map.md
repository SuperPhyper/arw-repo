---
status: note
layer: docs/meta/
---

# LLM Memory Map

This file provides a lightweight navigation map for LLMs and human collaborators.
Its purpose is to identify the most important conceptual anchors of the repository
and to indicate how new contributions should orient themselves.

---

# 1. Canonical Orientation

When interacting with this repository, prefer the following reading order:

1. `README.md`
2. `docs/overview/ARW_in_one_page.md`
3. `docs/glossary/scope.md`
4. `docs/overview/arw-operator.md`
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

Canonical source: `docs/glossary/scope.md`

The components are defined as follows — **do not reinterpret these**:

| Component | Meaning |
|---|---|
| **B** | Boundary constraints — select admissible states X_B ⊆ X |
| **Π** | Admissible descriptions or projections (observables) — each π ∈ Π maps states to a descriptive space |
| **Δ** | Admissible perturbations — define robustness conditions; distinctions must remain stable under δ ∈ Δ |
| **ε** | Resolution threshold — d_Π(x, y) ≤ ε means x ~_S y (indistinguishable under scope S) |

Use when discussing admissibility, partitioning, or the structural conditions under which a description holds.

## Boundary Conditions (B)

Defines the constraints, couplings, restrictions, or framing conditions under which a system is considered.
Canonical source: `docs/glossary/boundary_conditions.md`, `docs/bc_taxonomy/boundary_condition_classes.md`

## Descriptions / Projections (Π)

Defines which aspects of the system are visible within the scope.
Each observable π ∈ Π maps states to a descriptive space where differences can be evaluated.
Canonical source: `docs/glossary/observable.md`, `docs/glossary/scope.md § Π`

## Admissible Perturbations (Δ)

Defines what perturbations regime distinctions must withstand.
Robust partitions must remain stable under all δ ∈ Δ.
Canonical source: `docs/glossary/scope.md § Δ`

## Resolution / Tolerance (ε)

Defines the operational threshold at which distinctions are maintained or collapsed.
An admissible ε-interval I_ε = [ε_min, ε_max] exists for each scope — empirically determined via ε-sweep.
Canonical source: `docs/glossary/scope.md § ε`, `docs/advanced/epsilon_and_scope_resolution.md`

## ARW Operator

Formal mapping A(S) = R_S: scope → regime partition.
Use for formal claims, transfer questions, or regime-generation logic.
Canonical source: `docs/overview/arw-operator.md`

## Regime / Regime Partition

Equivalence classes of states under robust indistinguishability: R_S = X_B / ~_S
Use when discussing emergent stable patterns, distinct classes of behavior, or structure induced by boundary conditions.
Canonical source: `docs/glossary/regime.md`, `docs/glossary/regime_partition.md`

## Transfer / Scope Transfer

Whether regime structures remain valid across different descriptions, systems, or abstraction levels.
Quantified by RCD, TBS_norm, PCI, SDI, Φ.
Canonical source: `docs/bc_taxonomy/transfer_distortion_metrics.md`

## Observables

Link formal structure to what can actually be measured, tracked, or compared.
Canonical source: `docs/glossary/observable.md`

---

# 3. Repository Layer Map

Use this section to decide where new content belongs.

## `docs/overview/`

Entry points, orientation texts, short conceptual overviews, first-contact explanations, and the ARW operator definition.
Key files: `ARW_in_one_page.md`, `arw-operator.md`, `minimal_example.md`

## `docs/glossary/`

Atomic concepts and short definitional files.
One concept per file whenever possible.
Key files: `scope.md`, `boundary_conditions.md`, `admissibility.md`, `regime.md`, `observable.md`

## `docs/core/`

Central ARW formalism: scope reduction, regime stability regions, scope transitions, scope dominance, basins.
Key files: `arw_scope_reduction_partition_criterion.md`, `regime_stability_regions.md`, `scope_transition.md`

## `docs/advanced/`

More difficult, extended, or theoretically richer elaborations that presuppose the core material.
Key files: `epsilon_and_scope_resolution.md`, `scope_completeness.md`, `emergence_overview.md`

## `docs/art_instantiations/`

Domain-specific realizations of ARW or ART: physical, social, computational, organizational cases.
Key files: `art_scope_template.md`, `art_geopolitical_scope_example.md`

## `docs/bc_taxonomy/`

Boundary condition classification system: BC classes, partition types, BC→partition mapping, transfer distortion metrics.
Key files: `boundary_condition_classes.md`, `transfer_distortion_metrics.md`, `bc_class_to_regime_type_map.md`

## `docs/context_navigation/`

Application of ARW to cognitive architecture: context-dependent modes, salience, admissibility-based selection.
Key files: `bc_taxonomy_cognitive_modes.md`, `admissibility_and_mode_selection.md`

## `docs/cognitive_architecture/`

ARW/ART instantiation for cognition as a research domain.

## `docs/related_fields/`

Connections to dynamical systems, RL, philosophy of science, cognitive science.
Key files: `related_fields_and_methodological_connections.md`

## `docs/pipelines/`

Pipeline design documentation: partition extraction, regime graph construction.
Key files: `PartitionPipeline.md` (also maintained at `pipeline/PartitionPipeline.md`)

## `docs/figures/`

Figure descriptions and captions. Actual image files are in `figures/`.

## `docs/notes/`

Exploratory, provisional, reflective, or interpretive material.
Do not treat notes as automatically canonical.
Key files: `research_journal.md`, `open_questions.md`, `repo_weakpoints.md`

## `docs/meta/`

LLM contribution rules, navigation aids, and repository design documentation.
These files are meta-level: they describe how to interact with the repository, not ARW theory itself.
Key files: `LLM_CONTRIBUTION_CHARTER.md`, `llm_memory_map.md`, `repo_design.md`

## `experiments/`

Executable workflows, pipeline logic, evaluation setups, simulation-related structures.

## `cases/`

Pipeline outputs, example runs, datasets, generated result collections.
One subdirectory per experiment instance.

---

# 4. Content Status Map

When adding or revising a file, signal which type of content it is using YAML front-matter:

```yaml
---
status: working-definition
---
```

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
- scope-relative claims (relate to B, Π, Δ, ε)

## Avoid this

- silently redefining terms (especially scope tuple components)
- mixing ARW formalism with ART examples in one undifferentiated passage
- treating notes as final doctrine
- adding broad speculative claims without placement or status markers
- duplicating concepts under new names without explanation
- using "Resonanzwissenschaft" or "Applied Resonance Theory" — the canonical names are "Regime-Wissenschaft" and "Regime-Theorie"

---

# 6. Suggested Prompting Heuristic for LLM Use

When working with the repository, an LLM should implicitly ask:

1. What layer of the repository am I in?
2. Is this ARW or ART?
3. Which canonical concept does this connect to?
4. Is this a definition, claim, note, or proposal?
5. Where should this contribution live so that future readers can find and reuse it?
6. Am I using B, Π, Δ, ε with their canonical meanings?

---

# 7. Functional Role of This File

This file is not itself a source of new theory.
It is a navigation and memory aid.
Its role is to reduce drift, improve consistency, and help future contributors orient themselves inside the repository as a long-term conceptual memory system.
