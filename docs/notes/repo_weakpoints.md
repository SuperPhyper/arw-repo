---
last_reviewed: 2026-03
purpose: consistency audit with current repository state
status: draft
---

# Repository Weak Points (Consistency-Checked)

This document lists **actual remaining weak points** in the repository
after checking the current state of all major directories.

It distinguishes three categories:

1.  **Already implemented but fragmented**
2.  **Working definition present but not operationalized**
3.  **Genuinely missing components**

The goal is to prevent misidentifying solved problems as open gaps.

------------------------------------------------------------------------

# Category 1 --- Implemented but Needs Consolidation

These components already exist in the repository but are **spread across
multiple files or not yet canonicalized**.

## Distortion Metrics

Location: - `docs/bc_taxonomy/transfer_distortion_metrics.md` -
references in experiments (e.g. aggregation mean-field)

Current state: - four conceptual metrics defined - admissible reduction
condition present

Remaining issue: - experiments do not yet consistently reference these
metrics - no unified computation pipeline for metrics across experiments

Needed improvement: - central metric definitions with equations -
cross-reference from all experiments - example calculations

Priority: **medium**

------------------------------------------------------------------------

## Glossary Canonicalization

Location: - `docs/reference/` - `docs/reference/glossary_map.md` -
definitions distributed across core documents

Current state: - glossary structure exists - core terms already defined

Remaining issue: - some definitions appear in multiple files - glossary
entries not always atomic

Needed improvement: - single canonical glossary entries - cross-links
from all documents

Priority: **medium**

------------------------------------------------------------------------

## ε Formalization

Location: - `docs/advanced/epsilon_and_scope_resolution.md` -
`docs/advanced/epsilon_resolution_window_arw.md`

Current state: - ε defined as scope resolution parameter - used
operationally in experiments

Remaining issue: - two documents overlap conceptually - advanced cases
(vector ε, state-dependent ε) unresolved

Needed improvement: - merge into single canonical ε document - clarify
relationship with Δ (perturbations)

Priority: **medium**

------------------------------------------------------------------------

# Category 2 --- Working Definitions but Not Fully Operational

These components exist conceptually but require **formal or experimental
completion**.

## Emergence Criterion

Location: - `docs/advanced/emergence_overview.md`

Current state: - conceptual explanation present

Missing: - formal ARW condition for emergence - clear distinction
between:

coarsening (admissible reduction) vs partition reorganization

Needed improvement: - formal criterion expressed in partition relations

Priority: **medium**

------------------------------------------------------------------------

## Basins vs Scope Partitions

Location: - `docs/core/basins_as_scope_partitions.md`

Current state: - conceptual mapping between dynamical basins and ARW
regimes

Missing: - formal condition for equivalence - explicit counterexamples
where Π or ε hide basin structure

Priority: **medium**

------------------------------------------------------------------------

## Context Navigation Integration

Location: - `docs/context_navigation/`

Current state: - architecture components documented: - anchor memory -
modal cognition - mode ecology - agent architecture

Remaining issue: - integration overview (`context_navigation_ai.md`) is
brief - relationship between architecture and ARW analysis not yet fully
synthesized

Needed improvement: - single integration overview diagram - explicit
mapping between architecture components and ARW scopes

Priority: **medium**

------------------------------------------------------------------------

# Category 3 --- Areas Still Missing

These elements are not yet present in the repository.

## ART Instantiation Coverage

Location: - `docs/art_instantiations/`

Current state: - template exists - geopolitical example present

Missing instantiation cards for:

-   pendulum system
-   Kuramoto oscillators
-   consensus model
-   labyrinth navigation

Needed improvement: - minimal scope cards using

S = (B, Π, Δ, ε)

Priority: **low**

------------------------------------------------------------------------

## Roadmap Operationalization

Location: - `docs/overview/roadmap.md`

Current state: - conceptual roadmap present - core framework elements
marked completed

Missing: - milestones - success criteria - decision gates

Example structure:

Phase 1 Partition extraction calibration (Kuramoto)

Phase 2 Scope reduction validation (Pendulum)

Phase 3 Agent → mean-field distortion analysis

Phase 4 Cross-domain validation

Priority: **low**

------------------------------------------------------------------------

# Category 4 --- Notes Section

Location: `docs/notes/`

Current state: - `open_questions.md` - `literature_links.md` -
`research_journal.md` - `repo_weakpoints.md`

All files contain content.

Remaining improvement: - decide whether research journal should remain
public - or become internal working notes

Priority: **low**

------------------------------------------------------------------------

# Overall Diagnosis

After reviewing the entire repository:

Most previously identified weak points were **outdated**.

The framework already contains:

-   BC taxonomy
-   partition typology
-   distortion metrics
-   ART template
-   context navigation architecture
-   scope formalism

Remaining work is primarily:

-   consolidation
-   operationalization
-   experiment integration

rather than invention of missing concepts.

The repository has largely transitioned from **concept construction** to
**method consolidation**.
