# ARW / ART Framework

*A structural framework for analyzing regime partitions under boundary conditions*

Author: Rico Felder · License: MIT · Status: active research program

---

## At a Glance

**What problem does this solve?**
Complex systems are described differently at different levels — agent vs. mean-field,
microscopic vs. macroscopic, detailed vs. coarse. There is no systematic way to ask:
*when does a simpler description remain faithful to the original, and when does it
silently destroy structural information?* ARW proposes a methodology for that question.

**ARW in one sentence.**
ARW (Allgemeine Regime-Wissenschaft) maps descriptive choices — observables, boundary
constraints, admissible perturbations, resolution — to regime partitions, and analyzes
when those partitions survive a change of description and when they distort.

**ART in one sentence.**
ART (Allgemeine Regime-Theorie) is the application layer: it instantiates ARW by
declaring concrete scopes for real systems, which makes experiments and measurements
possible.

**Where to start.**

→ [docs/overview/why_arw.md](docs/overview/why_arw.md) — the problem, via two concrete cases (5 min)
→ [docs/overview/arw_concepts.md](docs/overview/arw_concepts.md) — the four scope components with examples (10 min)
→ [docs/overview/ARW_in_one_page.md](docs/overview/ARW_in_one_page.md) — the framework compactly
→ [papers/](papers/) — Felder 2026, *Epistemic Geometry of Descriptions: Cover Stability as a Criterion for Observable Validity* (PDF + interactive HTML companion)

---

## Core Concept

Every description of a system implicitly declares a **scope**:

```
S = (B, Π, Δ, ε)
```

| Symbol | Meaning |
|---|---|
| B | boundary constraints — which states are admissible |
| Π | observables — what is measured |
| Δ | admissible perturbations — which variations count as the same state |
| ε | resolution — which differences do not count |

The **ARW operator** maps a scope to a regime partition of the admissible state space:

```
A(S) = R_S
```

Δ and ε are **declared parameters of the description**, not properties of a subject.
They are free coordinates, not in the image of the generator map — so no observer enters
the formal construction at ARW level. ("Observer" remains an ART-level term for a
*modelled* describing system; level rule recorded 2026-08-04.)

Different scopes produce different regime structures. The framework develops tools to
measure when those structures transfer across scopes — and when they distort.

---

## Current State (2026-09)

The programme has two phases, and the second one reframes the first.

**Phase 1 (2026-03 → 2026-06) — the case programme.** Seven systems were run end to end
through a partition-extraction pipeline: 1D boundary-condition sweep → observable
extraction → ε-sweep → partition invariants → cross-case transfer metrics. Four of six BC
classes now have a pipeline-run anchor (Coupling, Restriction, Dissipation, Aggregation).
See [Empirical Results](docs/overview/empirical_results.md).

**Phase 2 (2026-08 → ) — two structural findings.**

1. **The regime construction is dimension-free; the 1D sweep is a degenerate case.**
   Adjacency belongs in the scope tuple, as **Δ-reachability** (x ⌢ y iff y ∈ x + Δ), not
   in the sweep protocol. "Consecutive in the sweep" was an undeclared adjacency relation
   operating outside the tuple. Consequence: a 1D sweep is generically blind to structure
   of codimension ≥ 2, θ* becomes a boundary *set* rather than a scalar, and TBS_norm — a
   component of the transfer metric Φ — has no general form.
   → [docs/notes/general_regime_construction.md](docs/notes/general_regime_construction.md)

2. **ε is a declared family, not a scalar.** Three multiplicities were conflated: across
   resolution (sound), across observables (ε_i), and across the domain (ε_i(x)). Scopes
   with several observables need per-observable ε plus a declared composition rule —
   Rule A (joint graph) or Rule B (common refinement), which coincide in 1D and diverge in
   general — and a declared commensurability normalisation.
   → [docs/notes/general_regime_construction.md](docs/notes/general_regime_construction.md) §2.2–2.4

**Consequence: validation strategy v2** ([docs/notes/validation_strategy_v2.md](docs/notes/validation_strategy_v2.md)).
The 1D cases are **retired as the focus of validation** and frozen as a regression suite:
the general construction with Δ = one grid step must reproduce their registered
partitions, and failure falsifies the construction, not the cases. The new unit is the
**study** — a declared question at one tier, with a preregistration frozen (SHA-256 +
git tag) before any results exist. Three tiers: T1 coherence (prerequisite), T2
distinctiveness (artifacts the 1D schema cannot hold in principle), T3 discrimination
(external, blinded data). Ordering decided: **distinctiveness first**.

**Honest status.** Study schemas exist at v0.1; `pipeline/validate_study.py` is planned
and not built; **no study has run yet**. Until T2 delivers, the validation column is
empty and the Phase-1 evidence counts as a consistency constraint, not as validation of
the general construction. The strategy note states this rather than bridging it.

---

## Cases

Values below are read from each case's `results/partition/Invariants.json` and
`ScopeSpec.yaml`.

| Case | System (sweep) | BC class | ε | N | θ* | go/no-go |
|---|---|---|---|---|---|---|
| CASE-20260311-0001 | Kuramoto (κ) | Coupling | 0.09 | 4 | 1.475 | pending — F1 sweep refinement |
| CASE-20260311-0002 | Multi-link pendulum (κ) | Coupling (+Dissipation) | 0.023 | 3 | 3.25 | go |
| CASE-20260311-0003 | Double pendulum (E) | Restriction | 0.015 | 2 | 8.5 J | go |
| CASE-20260318-0004 | Coupled Stuart–Landau (K) | Coupling (+Restriction) | 0.09 | 4 | 0.055 | go — first emergence case |
| CASE-20260315-0005 | Multi-link pendulum, damping (γ) | Dissipation | 0.05 | 8 | 0.1 | go |
| CASE-20260315-0007 | SIR epidemic (β) | Aggregation | 0.10 | 2 | 0.2 | go — complete |
| CASE-20260602-0014 | Growing-population SIR (ρ) | Dissipation (growing) | 0.05 | 1 | — | **no_go** — trivial partition at working ε |
| CASE-20260430-0013 | Vertical spring-mass chain (2D) | Forcing (+Restriction) | — | — | — | partial output, no CaseRecord |

Registered but not yet run (signature-first or open): CASE-0006, 0008, 0009, SOC1, 0010
(German school system, first multi-BC-class case), 0011 and 0012 (labyrinth /
behavioural, ε to be fixed by ε-sweep).

**Transfer.** `pipeline/transfer_v2.py` is canonical; v1 output is stamped
`SUPERSEDED_v1.md` (its PCI never read per-point labels, so ~90 % of Φ tracked regime
count). Current runs, including two decoupling controls:

| Comparison | Φ | Verdict |
|---|---|---|
| CASE-0001 vs CASE-0007 | 0.625 | partially_admissible |
| CASE-0004 vs CASE-0001 | 0.7794 | ambiguous_requires_inspection |
| Control, cross-class: 0003 vs 0007 | 0.7285 | ambiguous_requires_inspection |
| Control, same-class: 0001 vs 0002 | 0.6954 | partially_admissible |

The cross-class control scores *above* the same-class control. **Φ carries no clear
BC-class-distance signal** (Q-REL-05, expected-negative) and must never be presented as
BC-class evidence. Under v2, Φ is also barred across the 1D/general break; cross-study
structural comparison is routed to the Σ level (WP-A5, not yet built).

---

## Reading Path

### Formal foundation

| Document | Purpose |
|---|---|
| [docs/glossary/scope.md](docs/glossary/scope.md) | S = (B, Π, Δ, ε) — **source of truth, frozen** |
| [docs/overview/arw-operator.md](docs/overview/arw-operator.md) | Formal definition of the ARW operator |
| [docs/core/falsification_schema.md](docs/core/falsification_schema.md) | **F0–F4, F1_BC, F-gradient, decision order** — canonical since 2026-08-04 |
| [docs/core/cover_stability_criterion.md](docs/core/cover_stability_criterion.md) | Cover stability; basis of the 2026 paper |
| [docs/core/](docs/core/README.md) | Scope reduction, transitions, stability regions |

### Conceptual depth

| Document | Purpose |
|---|---|
| [docs/advanced/observable_decomposition.md](docs/advanced/observable_decomposition.md) | Observables as operator compositions; pre-scopal substrate; R(π), Z(π) |
| [docs/advanced/epsilon_and_scope_resolution.md](docs/advanced/epsilon_and_scope_resolution.md) | ε in depth (flagged simulation-native — see the ε ≠ Δ finding below) |
| [docs/advanced/h2_prime_theorem.md](docs/advanced/h2_prime_theorem.md) | Theorem H2′: dim_eff(Z(π)) = rank(IVA_ext(π)) |
| [docs/advanced/observable_space_cover_height.md](docs/advanced/observable_space_cover_height.md) | Cover height as ε-marginalisation |
| [docs/bc_taxonomy/](docs/bc_taxonomy/README.md) | BC classes, partition types, transfer distortion metrics |
| [docs/notes/scope_fibration.md](docs/notes/scope_fibration.md) | D(S) as a fibration; falsification categories as obstructions (hypothesis) |
| [docs/notes/ews_stage1_review_epsilon_vs_delta.md](docs/notes/ews_stage1_review_epsilon_vs_delta.md) | ε ≠ Δ on observational data; Δ is undeclarable from instrument metadata |
| [docs/notes/description_atlas_programme.md](docs/notes/description_atlas_programme.md) | Charts, transition data, obstructions; prediction P-ATLAS |

### Applications (ART)

| Folder / document | Domain |
|---|---|
| [docs/art_instantiations/](docs/art_instantiations/README.md) | Domain instantiations + KHT (cognitive hierarchy) architecture layers |
| [docs/context_navigation/](docs/context_navigation/README.md) | Modes as reduced scopes; scope-constructing agent |
| [docs/cognitive_architecture/](docs/cognitive_architecture/README.md) | ARW/ART instantiation for context-dependent cognition |
| [docs/notes/minds_generalization_beyond_facilitation.md](docs/notes/minds_generalization_beyond_facilitation.md) | Facilitation as one instance of a scope-navigation protocol |
| [docs/notes/compromise_as_scope_minimization.md](docs/notes/compromise_as_scope_minimization.md) | Compromise as joint-scope minimisation (2026-09) |
| [experiments/](experiments/README.md) | Experimental designs: Kuramoto, pendulum, labyrinth, Σ-extraction |

### Reference and current state

| Resource | Purpose |
|---|---|
| [docs/overview/empirical_results.md](docs/overview/empirical_results.md) | **Empirical findings to date**, with their tier and limits |
| [docs/notes/open_questions.md](docs/notes/open_questions.md) | Open questions — 28 prefix series here, a few more in their source notes; grep for collisions before assigning an ID |
| [docs/notes/research_journal.md](docs/notes/research_journal.md) | Session-by-session findings (2026-03-12 → 2026-08-05) |
| [docs/meta/DOC_INDEX.md](docs/meta/DOC_INDEX.md) | Anti-pile-up spine: canonical ownership of every conceptual doc |
| [docs/INDEX.md](docs/INDEX.md) | Human-facing searchable index |
| [docs/overview/limitations_and_open_questions.md](docs/overview/limitations_and_open_questions.md) | Honest assessment of what is not settled |
| [docs/notes/repo_weakpoints.md](docs/notes/repo_weakpoints.md) | Systematic gap assessment |
| [docs/meta/LLM_CONTRIBUTION_CHARTER.md](docs/meta/LLM_CONTRIBUTION_CHARTER.md) | Contribution rules — every contribution must pass its pre-commit check |

---

## Repository Structure

```
├── docs/                   Framework documentation
│   ├── overview/           Entry points, empirical results, roadmap, limitations
│   ├── glossary/           Atomic definitions — one concept per file
│   ├── core/               Frozen core: scope reduction, cover stability, falsification schema
│   ├── advanced/           ε, emergence, observable decomposition, BC signatures, cover height
│   ├── bc_taxonomy/        BC classes, partition types, distortion metrics
│   ├── art_instantiations/ Domain scopes + KHT architecture
│   ├── context_navigation/ Cognitive architecture, scope-constructing agent
│   ├── cognitive_architecture/
│   ├── notes/              Research journal, open questions, working notes
│   ├── meta/               DOC_INDEX, context maps, LLM charter, audit reports
│   ├── related_fields/     Connections to existing literature
│   └── figures/            Caption files for figures/
│
├── pipeline/               Partition extraction pipeline (Python)
│   ├── validate.py         Structural completeness check
│   ├── sweep.py            BC parameter sweep (+ sweep_behavioral.py for agent sweeps)
│   ├── extract_partition.py
│   ├── epsilon_sweep.py    ε → N regime-count sweep
│   ├── epsilon_kappa_map.py        2D (κ, ε) map; direct windowed σ_Δ
│   ├── epsilon_multi_observable.py Per-observable ε (diagonal ε₁ = ε₂ only — known limit)
│   ├── invariants.py       Regime count, adjacency graph, persistence, θ*
│   ├── transfer_v2.py      Cross-scope metrics — canonical
│   ├── transfer.py         v1 — deprecated for BC-class-distance claims
│   ├── audit.py / audit_helpers.py / new_case.py
│   └── kernels/            Simulation kernels
│
├── schemas/                ScopeSpec, BCManifest, CaseRecord (cases)
│                           StudySpec, Preregistration, StudyRecord (studies, v0.1)
├── cases/                  One directory per case (16 registered)
├── experiments/            Experimental designs + spring-mass / labyrinth scripts
├── papers/                 Felder 2026 (PDF + interactive HTML)
├── figures/                ~57 diagrams and result plots
├── agents/                 Agent role definitions for the research scaffold
├── archive/                Superseded artifacts, read-only, with supersession stamps
├── data/  analysis/  simulations/   (placeholders)
└── LICENSE
```

---

## What Is Next

1. **T1 coherence** — recovery check of the frozen regression suite under Δ-reachability;
   ε-family scaffolding; a concrete Δ-reachability rule that does not silently become
   "grid neighbours" again.
2. **T2 distinctiveness** — the (ε₁, ε₂) joint region for CASE-20260311-0003 (its own
   output already records `agreement_rate = 0.367`, never drawn as a conclusion);
   Rule A / Rule B divergence on a ≥ 2D field; θ* as a boundary set; codim-2 detection
   against the constructed two-level model H(x, y) = [[x, y], [y, −x]].
3. **WP-A5** — the Σ-level structural comparison artifact, now load-bearing because Φ is
   barred across the break.
4. **Build `validate_study.py`** — until then the `[MC]` checks in `schemas/StudySpec.yaml`
   are performed by hand.

Failure condition, recorded in advance: if T2 yields nothing the 1D form could not hold,
the generalisation is bookkeeping and will be reported as such.

---

## License

MIT License — see [LICENSE](LICENSE).
