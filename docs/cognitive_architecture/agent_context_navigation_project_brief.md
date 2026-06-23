---
status: experiment-proposal
layer: docs/cognitive_architecture/
title: "Agent Context Navigation — Existence Test for Emergent Modulator Structure (Project Brief)"
created: 2026-06-11
depends_on:
  - docs/cognitive_architecture/context_navigation_ai.md
  - docs/cognitive_architecture/modal_cognition.md
  - docs/cognitive_architecture/anchor_memory.md
  - docs/cognitive_architecture/bc_taxonomy_cognitive_modes.md
  - docs/cognitive_architecture/simulation_revision_design_notes.md
related:
  - docs/art_instantiations/kht_architecture_layer1.md (axis hypothesis under test)
  - docs/art_instantiations/kht_arw_analysis.md
note: >
  This brief consolidates the conclusions of an extended design discussion
  (2026-06-11). It reframes the agent rerun from a confirmation test into an
  existence test for emergent low-dimensional mode structure, and derives the
  design constraints, pre-registered evaluation criteria, and downstream role
  (O3 derivation) that follow from that reframing.
---

# Agent Context Navigation — Project Brief: The Existence Test

## 1. Purpose and Epistemic Role

KHT's core structural hypothesis — that cognition is organized by a small set
of axes (operator pairs + binary modulators) whose combinations form discrete
stable modes — currently rests on inherited typological tradition and on
internal coherence, not on independent evidence. The axes are *assumed*, not
*derived* (open: Q-L1-2, Q-L2-2).

The agent experiment is the only available setting in which this assumption
can be tested **outside its context of origin**: an artificial agent carries
no MBTI heritage as a confounder. Its role is therefore not application but
foundation:

> **Primary question:** Does salience-aggregated experiential learning, in a
> sufficiently structured environment, produce a low-dimensional mode
> organization *by itself* — and if so, does that organization resemble the
> hypothesized KHT axes?

This is an **existence test, not a confirmation test**. The distinction is
binding for every design decision below.

### 1.1 The fork (decided)

| Option | Build | Can show | Cannot show |
|---|---|---|---|
| Confirmation test | Axes built into agent | A KHT-structured agent outperforms a monolithic one | That the axes are the *right* ones (circular) |
| **Existence test (chosen)** | No axes built in; structure must emerge | Whether and which low-dimensional structure emerges | — |

A confirmation run may follow later; it is meaningless before the existence
question is answered.

---

## 2. Central Design Change: Unlabeled Salience

### 2.1 The problem in the previous design

In the prior run, salience events were assigned to **predefined categories**
(`saliency_type ∈ {cost_shift, visibility_drop, stagnation}`) before archetype
formation. This builds the categorical structure into the agent: archetypes
can only organize along categories the designer supplied. The dimensionality
of the resulting mode ecology is an input, not a finding.

### 2.2 The correction

Separate two things that were previously fused:

- **Salience as trigger** — must be a metric the agent can use. Keep it.
  Defined as a *scalar, category-free* admissibility-loss signal: the
  magnitude of deviation between what the active mode predicts and what is
  observed (ARW: a σ_Δ-type quantity relative to the active regime cell).
- **Salience categorization as structure** — must NOT be given to the agent.
  *Which kinds* of salience exist, *how many* modes form, *along which
  dimensions* they differ: this is the experimental outcome.

**Implementation rule:** remove `saliency_type` from archetype formation.
Archetypes form from similarity of learned weight profiles (w_in/w_out) and
context embeddings alone. A new archetype is instantiated when the scalar
salience signal indicates that no existing archetype covers the current
context adequately — not when a labeled event type fires.

**Richer fallback (preferred if pure scalar starves learning):** provide the
agent the *raw, unlabeled* deviation vector (full prediction–observation
difference, in native dimensionality). Then the experimental question becomes
directly: onto how few dimensions does the agent compress this raw salience
space, and are they interpretable? Emergent dimensionality reduction *is* the
answer to the structure question.

Accepted trade-off: unlabeled salience makes training slower and possibly
unstable. This is informative, not a bug — an agent that forms stable modes
*only* when categories are supplied has answered the existence question
negatively (structure must be imposed, does not emerge).

---

## 3. Degrees-of-Freedom Surplus (anti-circularity constraints)

Removing the salience label is necessary but not sufficient. The hypothesis
can re-enter through three other doors. Governing principle:

> **Everywhere, give the agent more freedom than the hypothesis needs, and
> observe whether it collapses onto the hypothesized number.**

| Door | Risk | Constraint |
|---|---|---|
| State representation | Observations pre-encoded along hypothesized axes → axes trivially recovered | Observation space richer than (and not aligned with) the hypothesized axes |
| Policy architecture | Mode-slot count = expected type count → only that count can emerge | More mode/archetype slots than expected modes; no fixed mode count |
| Environment design | Substrates mapped 1:1 onto hypothesized axes → emergence is tautological | More substrate variation than hypothesized dimensions; substrates defined by *physical* admissibility differences, never by axis labels |

Environment principle (from `simulation_revision_design_notes.md`, retained):
each environment class is an **admissibility filter** — it preserves at least
one policy substrate and invalidates at least one competing substrate (OPEN,
CORRIDOR, HALFWALL, COSTPATH, QUICKSAND, OCCLUSION). The agent *feels* these
differences only through the scalar salience signal (its policy degrades);
it is never *told* the class. The environment is structured; the structure is
not named.

Pretraining protocol retained: train each environment class in isolation
first to allow local policy differentiation, then mix (policy separation
requirement: a policy successful in one regime must become measurably
suboptimal in another).

---

## 4. Pre-Registered Evaluation (fix BEFORE the run)

Post-hoc pattern recognition is the main interpretive risk: a typologically
trained observer will see his axes in any three- or four-dimensional result.
All criteria below are therefore fixed before training starts.

### 4.1 Separation check (precondition)

Cross-substrate effectiveness matrix: effectiveness of each archetype on each
substrate class. **Requirement: clear diagonal dominance.** Without measurable
archetype separation, the run cannot address the existence question (this is
the diagnosed failure of the previous run, see §6) and must be treated as a
design iteration, not a result.

### 4.2 Dimensionality measure

Intrinsic dimensionality of the emergent archetype library (PCA /
participation ratio / ML intrinsic-dimension estimator on the set of
w_in/w_out vectors and/or archetype context embeddings — estimator chosen and
fixed in advance).

- Low effective dimension (order of the hypothesized axis count) → candidate
  emergent structure exists.
- High / unstructured dimension → no emergent low-dimensional organization.

### 4.3 Interpretability criterion (what counts as "resembles KHT axes")

"Three dimensions" are not *the* three dimensions merely by count. Required:

1. Each emergent principal axis maps onto an identifiable substrate property
   or processing distinction, with a unique best interpretation (no two
   equally good readings).
2. Blind labeling: a rater given the emergent axes *without* KHT vocabulary
   produces descriptions that match the KHT axis semantics (pre-write the
   matching rubric).
3. Stability: the emergent axes reproduce across seeds and across
   environment-mixture orders (axis identity, not just axis count).

### 4.4 Three outcomes — all informative

| Outcome | Reading | Consequence |
|---|---|---|
| Low-dim structure emerges and passes 4.3 | Strongest evidence to date that the axes are learning-induced necessities, not inherited convention | Axis hypothesis upgraded from assumption to supported claim; proceed to O3 derivation (§5) |
| Low-dim structure emerges but differs from KHT axes | Empirically motivated axis revision — more valuable than confirmation | Revise Layer 1 around the emergent geometry |
| No low-dim structure emerges | Discreteness must be imposed; does not self-organize under salience-aggregated learning | Foundational revision of KHT's Layer 1/2 claim; the "necessary vs. posited" question answered negatively |

A well-posed experiment has no uninformative outcome. The commitment to
accept outcome 3 is a precondition of running the experiment honestly; if
outcome 3 is unaffordable, the design will drift back into a confirmation
machine through unexamined choices.

---

## 5. Downstream: O3 Is Read Off, Not Invented

The structure observable for KHT (working name **O3**) is currently blocked:
an instrument cannot be designed for a structure whose existence is
unestablished — it would project its assumed axes into every measurement
(the standard failure of personality instruments).

If the existence test yields structure, the emergent geometry *is* the
specification of O3: the dimensions along which the agent's archetypes
organize are the quantities a human-facing instrument must track.

Design requirements for O3 carried over from the discussion (for later
cross-referencing, not for immediate build):

- **Structure, not content.** O3 must measure *how* processing is organized,
  never *what* is chosen/preferred/answered. Content is the policy layer —
  culturally trained, calibration-bound; the entire class of
  "do you prefer X or Y" items is excluded by construction.
- **Within-subject and relational.** Compare a person's transitions with
  their own other transitions; no norm group.
- Candidate measurement channels (complementary, for cross-referencing):
  1. **Transition geometry / anisotropy** — perturb along control parameters
     (τ, σ, ξ analogs); measure which mode transitions are easy, which
     resist, return dynamics, hysteresis. The shape of this transition field
     is the type fingerprint; predicted invariant under cultural policy
     training.
  2. **Instability as signal** — locate where processing consistency breaks
     under small perturbation (cognitive cover-stability analysis; the
     F-gradient zones of type assignment). Reinterprets the known
     near-midline test-retest instability of MBTI-style instruments as
     *correct measurement of a boundary region*, not noise.
  3. **Relational coupling** — measure coupling structure between axes
     (mutual damping, switching cost, sequencing) rather than absolute axis
     levels; absolute levels are policy-shifted, coupling structure is the
     scope-level claim.
- **Cost honesty:** structure observables are slow (perturbation +
  repetition). Speed of content tests is precisely what makes them
  calibration-bound. Slowness is the price of calibration-freedom and is to
  be stated in the design, not apologized for.

Method dry-run available now: run the §4.2 dimensionality pipeline on the
existing 20-archetype library from the previous run. Statistically near-void
(n=20, poorly separated substrates), but it validates the evaluation
tooling before the rerun.

---

## 6. Diagnosis of the Previous Run (baseline)

2720 episodes, combined log. Quartile trends:

| Metric | Q1 | Q4 | Reading |
|---|---|---|---|
| goal_rate | 0.168 | 0.135 | competence declining |
| ep_reward | −30.1 | −34.1 | declining |
| n_saliency | 12.7 | 18.3 | rising admissibility stress, unresolved |
| mean_w_eff | 0.61 | 0.86 (→0.99) | consolidation rising monotonically |

**Core finding: consolidation–competence decoupling.** The archetype
mechanism works (stable structure forms and deepens) but deepens around a
suboptimal configuration — pathological dissipation: basins discretize
without competence gain. Library: 20 archetypes in only 3 pre-given salience
categories (cost_shift 9, visibility_drop 9, stagnation 2 — the last a
degenerate); near-identical effectiveness (0.999) and similar weight profiles
across categories → **archetypes did not separate**. Cause: (a) salience
categories pre-labeled (§2), (b) environment did not enforce policy
separation (only two real substrates). Conclusion: prior run demonstrates the
*mechanism*, decides nothing about *structure*. Both defects are addressed by
§2 and §3.

---

## 7. ARW Framing (level discipline)

- ARW level: salience = scalar admissibility-loss signal relative to the
  active regime cell; modes = regime cells in the partition of S_global (not
  independent scope tuples — see `modal_cognition.md` revision note);
  archetypes = persistent local admissibility structures; distinguish
  uncertainty spikes from observable-invalidation (F0-type) spikes.
- ART level: this experiment, its environments, logs, and metrics. A future
  CaseRecord should document both system-level BC class (zone type) and
  observable-level BC class per Q_NEW_9 handling in
  `bc_taxonomy_cognitive_modes.md`.
- The KHT axis hypothesis enters **only** in §4.3 (interpretation rubric) and
  nowhere in agent, environment, or training code. This separation is the
  operational definition of "ergebnisoffen" for this project.

---

## 8. Work Packages

1. **WP1 — Salience refactor:** remove `saliency_type` from archetype
   formation; implement scalar (and optional raw-vector) salience; archetype
   instantiation via coverage failure, similarity-based merging.
2. **WP2 — Environment build:** six admissibility-filter classes per revision
   notes; physical substrate differences, no class labels in agent inputs;
   isolation pretraining then mixing; verify policy separation requirement.
3. **WP3 — Pre-registration:** fix dimensionality estimator, separation
   threshold (diagonal dominance), interpretability rubric, seed/stability
   protocol. Freeze before first training run.
4. **WP4 — Evaluation pipeline:** cross-substrate effectiveness matrix,
   dimensionality analysis, axis-interpretation tooling. Dry-run on old
   20-archetype library.
5. **WP5 — Run + analysis:** multi-seed existence-test runs; report against
   §4.4 outcome table.
6. **WP6 (conditional on outcome 1 or 2):** derive O3 specification from
   emergent geometry; draft `ScopeSpec_signature_first.md` for a first
   human-side structure measurement.

---

## 9. Standing Commitments

- Existence test before confirmation test; no axis labels anywhere in the
  agent-facing stack.
- Degrees-of-freedom surplus at every design door (§3).
- Evaluation criteria frozen before training (§4); deviations documented,
  never silent.
- All three outcomes are acceptable results. The experiment is run so that
  KHT can lose.
