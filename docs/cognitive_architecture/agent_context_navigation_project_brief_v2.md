---
status: experiment-proposal
layer: docs/cognitive_architecture/
title: "Agent Context Navigation — Existence Test for Emergent Modulator Structure (Project Brief, v2)"
created: 2026-06-11
revised: 2026-06-11
revision: 2
supersedes: agent_context_navigation_project_brief.md (v1, same date)
depends_on:
  - docs/cognitive_architecture/context_navigation_ai.md
  - docs/cognitive_architecture/modal_cognition.md
  - docs/cognitive_architecture/anchor_memory.md
  - docs/cognitive_architecture/bc_taxonomy_cognitive_modes.md
  - docs/cognitive_architecture/simulation_revision_design_notes.md
related:
  - docs/art_instantiations/kht_architecture_layer1.md (axis hypothesis under comparison)
  - docs/art_instantiations/kht_architecture_layer2.md (biological BC grounding)
  - docs/art_instantiations/kht_arw_analysis.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md (Φ, RCD, TBS_norm — for §4.4 outcome 2)
revision_note: >
  v2 (2026-06-11) corrects an inference-direction error in v1. The agent and
  the human are different scopes with different boundary constraints B. The
  agent tests BC_agent → mode geometry; KHT claims BC_human → mode geometry.
  v1 short-circuited these two statements via the three-outcome table (§4.4)
  and the standing commitment "run so that KHT can lose" (§9). v2 confines
  every conclusion to the agent scope, introduces the inference levels A/B/C
  (§1.2), reinterprets the "different geometry" outcome as a controlled
  BC-contrast (an ARW transfer analysis), and adds a mandatory axis-wise
  pre-classification of KHT axes by BC-dependence to the pre-registration
  (§4.3, WP3). Design sections (§2, §3, §6) are unchanged — the correction
  affects what outcomes mean, not how the experiment is built.
note: >
  This brief consolidates the conclusions of an extended design discussion
  (2026-06-11). It reframes the agent rerun from a confirmation test into an
  existence test for emergent low-dimensional mode structure, and derives the
  design constraints, pre-registered evaluation criteria, and downstream role
  (O3 derivation) that follow from that reframing.
---

# Agent Context Navigation — Project Brief v2: The Existence Test

## 1. Purpose and Epistemic Role

KHT's core structural hypothesis — that cognition is organized by a small set
of axes (operator pairs + binary modulators) whose combinations form discrete
stable modes — currently rests on inherited typological tradition and on
internal coherence, not on independent evidence. The axes are *assumed*, not
*derived* (open: Q-L1-2, Q-L2-2).

The agent experiment is a setting in which one specific subclaim can be
tested outside its context of origin: an artificial agent carries no MBTI
heritage as a confounder. Its role is therefore not application but
foundation — within strict scope limits (§1.2):

> **Primary question:** Does salience-aggregated experiential learning, in a
> sufficiently structured environment, produce a low-dimensional mode
> organization *by itself* — under the agent's own boundary constraints?

Whether the emergent organization resembles the hypothesized KHT axes is a
**secondary, downstream comparison question** (§4.3), not part of the primary
question and not a success criterion. This is an **existence test, not a
confirmation test**, and the distinction is binding for every design decision
below.

### 1.1 The fork (decided)

| Option | Build | Can show | Cannot show |
|---|---|---|---|
| Confirmation test | Axes built into agent | A KHT-structured agent outperforms a monolithic one | That the axes are the *right* ones (circular) |
| **Existence test (chosen)** | No axes built in; structure must emerge | Whether and which low-dimensional structure emerges | — |

A confirmation run may follow later; it is meaningless before the existence
question is answered.

### 1.2 Scope discipline: the BC-mismatch clause (new in v2)

The agent and the human are **different scopes with different B**. The agent
lacks the biological boundary constraints — sensing, embodiment, social
coordination, language, cultural evolution — that in KHT's own Layer-2 model
break the symmetry of the operator-modulator space in the first place
(Restriction: genetic connectivity; Dissipation: Hebbian consolidation under
biological conditions). Those BCs are, in KHT, the *generating cause* of the
16 types. An agent without them cannot reproduce the geometry that follows
from them — not because KHT would be wrong, but because the input is absent.

The agent tests `BC_agent → mode geometry A`. KHT claims
`BC_human → mode geometry KHT`. These are different statements; no outcome of
one decides the other.

Three inference levels, fixed for the rest of this document:

| Level | Statement | Agent can address? |
|---|---|---|
| **A** | Which mode geometry emerges under BC_agent | Yes — this is what the experiment directly measures |
| **B** | Which structural features are learning-mechanism-general (BC-independent) | Partially — only for axes pre-classified as plausibly BC-independent (§4.3) |
| **C** | Human mode geometry under BC_human | No — out of the agent's reach; cross-scope claims only via explicit transfer analysis |

The dividing line does **not** run cleanly between "agent can do B" and
"agent cannot do C" — it runs *within KHT's axes*: some are plausibly generic
properties of any resource-bounded learning system (candidates: the J/P
convergence/divergence axis, the latent/transient distinction); others are
explicitly biologically grounded (Restriction- and Dissipation-carried
structure). The agent is informative about the former and silent about the
latter. This forces the axis-wise pre-classification in §4.3.

**The inversion (new in v2).** If the agent finds robust modes that do *not*
resemble KHT, that is not a threat but a measurement: same learning
mechanism, different BC set, different geometry — the first controlled
contrast of its kind in this project. The difference between agent geometry
and claimed human geometry is then informative *about the BCs themselves*:
it allows asking which parts of KHT structure are learning-general and which
are specifically human. The agent becomes a contrast medium — it isolates
what is due to the learning mechanism, so that what is due to the BCs becomes
visible by subtraction. Formally this is an ARW transfer analysis between two
scopes with documented different B (metrics: Φ, RCD, TBS_norm; with the
standing caveat that Φ measures observable transfer, not system transfer).

---

## 2. Central Design Change: Unlabeled Salience

*(unchanged from v1; implemented 2026-06-11 in
`Simulationen/labyrinth_existence_wp1/`)*

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
negatively (structure must be imposed, does not emerge — at level A).

---

## 3. Degrees-of-Freedom Surplus (anti-circularity constraints)

*(unchanged from v1)*

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

v2 note: the axis-wise pre-classification (§4.3) closes a fourth door — the
*interpretation* door. Without it, any emergent axis could be declared
post hoc to have been "one of the BC-independent ones."

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

Tooling status: the estimator pipeline was dry-run on the old 20-archetype
library (2026-06-11, `Simulationen/wp4_dimensionality_dryrun/`). All four
candidate estimators agree on that library (intrinsic dim ≈ 7–9 of 20, no
separation) — estimator choice appears robust; participation ratio is the
most assumption-free candidate. The choice is frozen in WP3.

### 4.3 Comparison criterion (downstream of the primary question)

"Three dimensions" are not *the* three dimensions merely by count. The KHT
comparison is a secondary analysis and enters only here. Required:

0. **Axis-wise BC pre-classification (new in v2, frozen before the run):**
   every KHT axis is classified in advance as either
   (i) *plausibly BC-independent* — interpretable as a generic property of
   resource-bounded learning systems; candidate for learning-emergence; the
   agent is informative about it (level B), or
   (ii) *explicitly biologically grounded* — generated by BC_human per
   KHT Layer 2; the agent is silent about it (level C).
   The comparison in steps 1–3 is run **only against class (i) axes**.
   Emergence or non-emergence of class (ii) structure in the agent carries
   no evidential weight either way.
1. Each emergent principal axis maps onto an identifiable substrate property
   or processing distinction, with a unique best interpretation (no two
   equally good readings).
2. Blind labeling: a rater given the emergent axes *without* KHT vocabulary
   produces descriptions that match the axis semantics of class (i) axes
   (pre-write the matching rubric).
3. Stability: the emergent axes reproduce across seeds and across
   environment-mixture orders (axis identity, not just axis count).

### 4.4 Three outcomes — all informative, all level-A statements (revised in v2)

Every row below is a statement about `BC_agent → geometry`. None of them is a
statement about KHT's validity for humans (level C).

| Outcome | Reading (within agent scope) | Consequence |
|---|---|---|
| Low-dim structure emerges and passes 4.3 against class (i) axes | Those specific axes are learning-induced under BC_agent — evidence at level B that they are learning-mechanism-general, not biologically contingent | The class (i) subset of the axis hypothesis is upgraded from assumption to supported claim; class (ii) axes untouched; proceed to O3 derivation (§5) for the supported subset |
| Low-dim structure emerges but differs from class (i) axes | **The inversion (§1.2):** controlled BC-contrast — same learning mechanism, different B, different geometry. Evidence *for* the structuring role of the missing biological BCs | Run the ARW transfer analysis (agent partition vs claimed KHT partition; Φ, RCD, TBS_norm with documented B-difference); the geometry *difference* becomes the object of study. No automatic Layer-1 revision |
| No low-dim structure emerges | Discreteness does not self-organize under salience-aggregated learning *from BC_agent alone* | Constrains only the subclaim "axes derivable from general learning principles" (for class (i) axes). Fully compatible with emergence under BC_human. Not a foundational KHT revision |

A well-posed experiment has no uninformative outcome. The commitment to
accept outcome 3 *as a level-A result* is a precondition of running the
experiment honestly; if outcome 3 is unaffordable, the design will drift back
into a confirmation machine through unexamined choices.

---

## 5. Downstream: O3 Is Read Off, Not Invented

The structure observable for KHT (working name **O3**) is currently blocked:
an instrument cannot be designed for a structure whose existence is
unestablished — it would project its assumed axes into every measurement
(the standard failure of personality instruments).

If the existence test yields structure, the emergent geometry specifies O3
candidates — **for the class (i) axes only** (v2). The dimensions along which
the agent's archetypes organize are the quantities a human-facing instrument
must track *insofar as they are learning-general*; class (ii) axes need their
own, human-side existence evidence and cannot inherit support from the agent.
Under outcome 2, the transfer analysis output (which geometry components
differ, by how much) additionally specifies *where* a human instrument must
be sensitive to BC-generated structure the agent lacks.

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

Method dry-run: completed 2026-06-11 on the existing 20-archetype library
(`Simulationen/wp4_dimensionality_dryrun/`). Statistically near-void (n=20,
poorly separated substrates) as expected; the evaluation tooling is validated
for the rerun.

---

## 6. Diagnosis of the Previous Run (baseline)

*(unchanged from v1, one correction)*

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
degenerate). *Correction (v2, from dry-run data): effectiveness is not
uniformly 0.999 but quantized at {0.3, 0.5, 0.8, 0.999} — and these levels
cut across all three categories, which strengthens the non-separation
diagnosis (cross/within distance ratio 0.96, silhouette −0.07).*
→ **archetypes did not separate**. Cause: (a) salience categories
pre-labeled (§2), (b) environment did not enforce policy separation (only
two real substrates). Conclusion: prior run demonstrates the *mechanism*,
decides nothing about *structure*. Both defects are addressed by §2 and §3.

---

## 7. ARW Framing (level discipline)

- ARW level: salience = scalar admissibility-loss signal relative to the
  active regime cell; modes = regime cells in the partition of S_global (not
  independent scope tuples — see `modal_cognition.md` revision note);
  archetypes = persistent local admissibility structures; distinguish
  uncertainty spikes from observable-invalidation (F0-type) spikes.
- **Scope discipline (new in v2):** S_agent and S_human are distinct scopes
  with different B. Conclusions stay inside the scope they were measured in;
  cross-scope statements are made only through explicit transfer analysis
  (Φ, RCD, TBS_norm), never by direct attribution. Φ measures observable
  transfer, not system transfer — transfer reports must document the
  observable BC structures of both scopes.
- ART level: this experiment, its environments, logs, and metrics. A future
  CaseRecord should document both system-level BC class (zone type) and
  observable-level BC class per Q_NEW_9 handling in
  `bc_taxonomy_cognitive_modes.md`.
- The KHT axis hypothesis enters **only** in §4.3 (comparison rubric, class
  (i) axes) and nowhere in agent, environment, or training code. This
  separation is the operational definition of "ergebnisoffen" for this
  project.

---

## 8. Work Packages

1. **WP1 — Salience refactor:** remove `saliency_type` from archetype
   formation; implement scalar (and optional raw-vector) salience; archetype
   instantiation via coverage failure, similarity-based merging.
   *Status: implemented 2026-06-11 (`Simulationen/labyrinth_existence_wp1/`);
   strength buckets and priority_mode/dist-gate also removed (decision
   2026-06-11: all categorical matching keys out).*
2. **WP2 — Environment build:** six admissibility-filter classes per revision
   notes; physical substrate differences, no class labels in agent inputs;
   isolation pretraining then mixing; verify policy separation requirement.
   *Status: open. quicksand/occlusion cell types exist in `env_cells.py` but
   are not wired into the curriculum.*
3. **WP3 — Pre-registration:** fix dimensionality estimator, separation
   threshold (diagonal dominance), interpretability rubric, seed/stability
   protocol, **and the axis-wise BC pre-classification of KHT axes
   (§4.3 step 0)**. Freeze before first training run.
4. **WP4 — Evaluation pipeline:** cross-substrate effectiveness matrix,
   dimensionality analysis, axis-interpretation tooling.
   *Status: dimensionality dry-run done 2026-06-11; effectiveness matrix and
   interpretation tooling open.*
5. **WP5 — Run + analysis:** multi-seed existence-test runs; report against
   §4.4 outcome table (level-A statements only).
6. **WP6 (conditional on outcome 1 or 2):** outcome 1 — derive O3
   specification from emergent geometry for the supported class (i) axes;
   outcome 2 — run the agent↔KHT transfer analysis (§1.2 inversion) and
   document the geometry difference as BC-evidence. In either case draft
   `ScopeSpec_signature_first.md` for a first human-side structure
   measurement.

---

## 9. Standing Commitments (revised in v2)

- Existence test before confirmation test; no axis labels anywhere in the
  agent-facing stack.
- Degrees-of-freedom surplus at every design door (§3), including the
  interpretation door (axis-wise pre-classification, §4.3 step 0).
- Evaluation criteria frozen before training (§4); deviations documented,
  never silent.
- All three outcomes are acceptable results — *as level-A statements*.
- **Inference direction stays within the agent scope.** The agent does not
  test KHT and cannot make KHT lose; it tests whether one subclaim — axes
  derivable from general learning principles — holds for the pre-registered
  class (i) axes under BC_agent. Cross-scope claims about human cognition
  are made only via explicit transfer analysis, never by direct attribution.
  *(Replaces v1's "the experiment is run so that KHT can lose", which
  asserted an inference the agent cannot carry.)*
