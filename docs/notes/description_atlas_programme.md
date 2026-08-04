---
status: experiment-proposal
layer: docs/notes/
created: 2026-08-04
depends_on:
  - docs/notes/scope_fibration.md
  - docs/notes/ews_stage1_review_epsilon_vs_delta.md
  - docs/core/falsification_schema.md
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
---

# The Description Atlas — the Vollraum as charts plus obstructions

**Purpose.** This note fixes the target of the D(S) programme and specifies the
route to it. The target is unchanged: a description of the **full space** of
scope-induced descriptions of a system. What changes is the claim about what such
a description can *be*, and where the work has to happen.

**Status.** Programme note with one registered falsification condition (§4) and a
preregistered case list (§6). Not a result.

---

## 1. Why the Vollraum can only be an atlas

`scope_fibration.md` §4 records the structural constraint: adding any second
direction to the ε-filtration makes D(S) a multi-filtration, and multidimensional
persistence admits no complete discrete invariant (Carlsson & Zomorodian 2009).
Any faithful record of D(S) therefore requires declaring a slice.

Taken seriously, that is not a caveat but a **specification of form**. A space
with no global summary but well-behaved local pieces is described by an atlas:
charts on which the structure is trivial, plus the transition data between them.
If the no-complete-invariant reading survives (Q-DSP-02), then

> the Vollraum description of a system **is** the atlas of its validity charts
> together with the obstructions to gluing them.

Nothing else is available. This is a stronger and more useful statement than
"D(S) is hard to summarise": it says what a completed description would look like
and what its parts are.

## 2. Chart

A **chart** is a region of scope parameter space on which the fiber is locally
constant — a declared parameter region together with the observable family and
the declared indifference (ε, Δ) under which the regime assignment does not
change.

> Chart c = (R ⊆ P, Π_c, ε_c, Δ_c) with the fiber constant on R.

This is exactly the content of a validity condition as the sciences already state
them. "Navier–Stokes holds for Kn < 0.01" is the assertion that on that parameter
region the continuum description's assignment is stable under the perturbations
that region admits. "The harmonic approximation holds for small amplitude" is the
same shape. So is v ≪ c, N → ∞, m_e/M ≪ 1, λ ≪ L.

**The charts already exist.** A century of physics has mapped validity regions
with quantitative boundaries, and validated them far beyond anything ARW can
produce. What has not been done is to collect them as charts **of one object**.
That collection is the programme.

## 3. The payoff is the transition data, not the charts

Reproducing a chart is the trivial half, and the run-4 lesson applies to it
without mercy: re-description is not an achievement
(`Simulationen/qdsp01_check_results/README_qdsp01_check.md`, run 4 — the
fibration violation set was beaten on localisation by a cheaper local finite
difference).

The non-trivial half is what happens **between** charts:

- where two validated descriptions overlap and disagree;
- where no continuous passage from one to the other exists;
- where a region belongs to no chart at all.

Fibrations are the tool for exactly this — not for the local pieces, but for the
gluing. The known hard regions of the sciences are, on this reading, the
obstructions: the Knudsen transition regime (Kn ≈ 0.1–10), where neither the
continuum nor the free-molecular description holds, is not a chart but a gap
between charts; ensemble inequivalence in long-range interacting systems is a
failed transition function between two descriptions of one system; a conical
intersection carries non-trivial monodromy in the adiabatic state assignment.

**Intra-system, therefore well-posed.** In the language of `scope_fibration.md`
§2b, an atlas is built from **paths**, not functors: all charts describe the same
system. This is why the transfer machinery's known defect does not bite here.
Q-REL-05 (Φ carries no clear BC-class-distance signal) was found on *cross-system*
comparisons, where the charts belong to different objects. Comparing two charts of
one system on their overlap is the well-posed application of the same machinery,
and it is the one the fibration reading already identified as the tractable side.

## 4. The registered falsification condition

The atlas reading makes a prediction sharp enough to kill the instrumental claim,
and it is stated here **before** the boundary tests are run:

> **P-ATLAS.** Inside a chart, ARW's constructions add nothing over local
> analytic tools. Any diagnostic surplus can appear only at chart boundaries and
> in inter-chart regions.

The first half is not a concession extracted after a failure — it follows from the
definition. Inside a chart the fiber is constant and the structure locally
trivial; there is nothing for a stability diagnostic to find that a gradient does
not find first. The second half is the whole instrumental claim.

Status of the two halves:

- **Inside-chart half: already fired, in the predicted direction.** Run 4 tested a
  smooth 2D field with a single transition — a chart interior — and the
  finite-difference baselines won. Under P-ATLAS that is the expected outcome.
- **Boundary half: untested.** If a properly designed inter-chart test also shows
  no surplus, the instrumental claim is **finished**, not deferred again. The
  architectural claim (charts, obstructions, the ε–Δ interleaving of §5a) would
  survive as a descriptive framework with no diagnostic value — which is a
  legitimate and reportable end state.

This is the guard against goalpost-moving: the condition is registered now, the
inside-chart half is already on record, and the boundary half has a stated
failure outcome.

## 5. Obstruction types

The current falsification schema (`docs/core/falsification_schema.md`) recognises
only a **metric** mode of Δ-failure: σ_Δ ≥ ε on a set exceeding the mass
tolerance τ_∂. The atlas reading predicts at least two further modes, and their
existence or absence is itself a test.

| Type | Character | Status in the schema | Physical instance |
|---|---|---|---|
| **M — metric** | σ_Δ ≥ ε (mass criterion) — assignment unstable because the observable is too steep for the declared indifference | present (F-gradient) | double-pendulum separatrix, CASE-0003 |
| **T — topological** | assignment not single-valued around a loop; χ ≠ 0 on a circuit on which \|∇O\| stays finite — monodromy, not steepness | **absent** | conical intersection: adiabatic electronic labels do not return after a loop enclosing the intersection (geometric phase) |
| **R — no common refinement** | two charts whose observable families admit no common refinement, so the overlap comparison is undefined rather than negative | **absent** | candidate: descriptions with incompatible coarse-grainings; to be identified |

Type T matters most, for two reasons. It is the mode run 4 could not test — in a
smooth single-transition field, steepness and assignment instability coincide, so
the task had no room for the distinction. And it is textbook physics, not a
construction: the sign change of adiabatic electronic states around a conical
intersection is an assignment instability that no gradient threshold detects.

If type T is confirmed as a distinct obstruction, the atlas programme has
**added a category** to the falsification schema rather than re-described it —
the first case in which the fibration reading yields something not visible without
it. If the T instances turn out to be reducible to M under a suitable observable
choice, that is a real negative result about the fibration's added structure.

## 6. Preregistered case list

Fixed here, before any case is worked. **All are reported, including failures.**
Cherry-picking a subset is the failure mode this list exists to prevent.

| # | Chart family | Boundary parameter | What it contributes |
|---|---|---|---|
| A1 | Continuum ↔ slip ↔ transition ↔ free-molecular flow | Knudsen number | multi-chart axis with published numerical boundaries; the inter-chart gap (Kn ≈ 0.1–10) is a known hard region |
| A2 | Adiabatic (Born–Oppenheimer) electronic states | nuclear configuration; conical intersections | candidate type-T obstruction (geometric phase) |
| A3 | Canonical ↔ microcanonical description | interaction range / N | ensemble inequivalence as a failed transition function |
| A4 | Mean-field ↔ fluctuation-dominated | Ginzburg criterion, dimension | chart boundary derived analytically, not conventionally |
| A5 | Harmonic ↔ anharmonic | amplitude | simplest chart pair; calibration case for the method |
| A6 | Geometrical optics ↔ wave optics | λ/L | second calibration case, different mechanism |
| A7 | Markovian ↔ non-Markovian | timescale separation | tests whether the method transfers off the spatial-parameter pattern |
| A8 | Rigid-body ↔ elastic | stiffness vs forcing | engineering-side chart pair |

A1, A2, A5 are the first three: one multi-chart axis, one candidate type-T case,
one calibration case.

## 7. Guards

The correspondence route has a specific failure mode — the boundaries are already
known, so "recovering" them proves nothing unless the recovery is derived without
using the answer.

1. **Derivation before lookup.** θ* for each chart boundary is derived from the
   ARW construction (ε-plateau on an analytic or simulated observable) and
   recorded *before* the literature value is consulted. Same blinding logic as the
   Cascade protocol; the recorded derivation is the artifact.
2. **Surplus prediction per case.** Each case must state, in advance, one
   consequence that the conventional reading does not make. Without it the case is
   re-description and scores nothing. Example for A1: conventional practice treats
   the Kn thresholds as properties of the flow; ARW requires θ* = θ*(π, ε, Δ), so
   the boundary must shift with the observable and the declared tolerance — hence
   the *spread of thresholds quoted for different quantities* (drag, heat
   transfer, slip) is predicted structure rather than imprecision. This is
   checkable against existing literature and is **not yet verified** — it is the
   case's risk, not its result.
3. **Full reporting.** The §6 list is fixed. Cases that fail, or that turn out not
   to be charts at all, are reported with the same prominence as successes.
4. **Level discipline.** Physical validity conditions are ART-level instantiations;
   the atlas structure is ARW-level. A case that only works because a physical
   detail was imported into the general claim is a failed case.

## 8. Open questions

- **Q-DSP-06** — Is the atlas (charts + transition data + obstructions) an
  adequate form for the Vollraum description, or does it lose structure that the
  no-complete-invariant argument does not force us to lose?
- **Q-DSP-07** — Does a topological obstruction type (T) exist as a category
  distinct from the metric one (M), or is every candidate T instance reducible to
  M under a suitable observable choice?

## 9. What would end the programme

- P-ATLAS's boundary half fails: no surplus at chart boundaries either → the
  instrumental claim is closed, permanently.
- Type T reduces to type M in every candidate → the fibration adds no structure
  beyond the existing schema.
- The charts of established theories cannot be put into the chart form of §2
  without importing case-specific machinery → the atlas is not domain-neutral, and
  the universality claims of the monograph's introduction lose their basis.

Each of these is a real possible outcome and each is reportable as a result.
