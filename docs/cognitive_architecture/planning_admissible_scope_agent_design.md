---
status: experiment-proposal
layer: docs/cognitive_architecture/
title: "Planning-Admissible Scope Agent — Persistence as a Carried State Variable"
created: 2026-07-29
revised: 2026-07-29
revision: 3
depends_on:
  - docs/cognitive_architecture/agent_context_navigation_project_brief_v2.md
  - docs/context_navigation/scope_constructing_agent_architecture.md
  - docs/core/scope_transition.md
  - docs/advanced/observable_space_cover_height.md
  - docs/notes/conflict_navigation_nested_calibration.md
  - docs/notes/kht_reconciliation_scope_constructing.md
  - docs/glossary/scope.md
related:
  - docs/context_navigation/switch_minimization_criterion.md
  - docs/notes/scope_constructing_agent_implementability.md
  - docs/core/cover_stability_criterion.md
  - Simulationen/labyrinth_scope_constructing/ (external — simulation code, not in repo)
  - Simulationen/kontextnavigation_minimal/ (external — simulation code, not in repo)
---

# Planning-Admissible Scope Agent

**One-line claim.** The architecture measures description *failure* well and
estimates description *survival* not at all. Those are mathematically opposite —
failure is retrospective, survival is prospective — and only the second supports
planning, commitment, or any long-horizon agency. This document adds survival as a
carried state variable, separates it strictly from the external quantity that
validates it, and makes selection lexicographic so that survival-maximisation
cannot collapse into describing nothing.

Revision 2 replaced the "rollout horizon as a measured property" formulation of
revision 1: that version let one quantity be both the agent's internal decision
variable and the external evidence for its quality, and it cannot be both.
Revision 3 records the first measurement of both quantities (§8.1–8.3). It went
against the design on the point the design named as its cheapest falsifier, and it
converts the failure into a quantified requirement on the next world rather than
into a repair of the estimator.

---

# Part I — ARW level

## 1. The persistence layer

A scope is S = (B, Π, Δ, ε): boundary constraints B selecting X_B ⊆ X, admissible
descriptions or projections Π, admissible perturbations Δ, and resolution
threshold ε under which d_Π(x, y) ≤ ε makes x and y indistinguishable.

Each description D ∈ Π carries and is validated against three quantities, and the
separation between the first and the other two is the point of this section:

| | what it is | where it lives |
|---|---|---|
| ĥ_t(D) | estimated instantaneous failure hazard | **inside** the agent, updated each step, enters selection |
| H_off(D) | rollout horizon on controlled material, in steps | **outside** the selection mechanics, validation only |
| V_Δ(D) | perturbation survival volume | **outside**, second validation reference |

### 1.1 ĥ_t — the internal state variable

The naive internal quantity would be expected remaining lifetime estimated from
past usage durations. It must not be used, because an observed usage duration is
not a sample from the description's survival distribution. A description's period
of use ends for four different reasons — the world changed (the event of
interest), the agent switched for another reason (competing risk), the run ended
(right censoring), or **the agent's own actions moved it into a different regime**
(informative censoring by a treatment the subject chooses). Usage duration is a
property of (D, X_t, the selection rule, the action sequence, the audit logic),
not of D.

Instead the description tracks its current **margin** to its own failure
threshold,

    m_t(D) = ε − r_t(D)

where r_t is the current residual, and estimates the hazard from it:

    ĥ_t(D) = P( r_{t+1} > ε | r_t, Δr_t, D )

or equivalently from an estimated residual profile,
ĥ_t(D) = 1 − F̂_D(ε | r_t, Δ_t), with any monotone g decreasing in the margin.
This is computable at every step from data the agent already has, and it requires
no death event.

**The hazard itself is the decision variable, not its reciprocal.** Converting to
expected remaining lifetime as 1/ĥ presumes an approximately constant hazard and
inflates the uncertainty exactly in the low-hazard region that matters. Remaining
lifetime may be carried as an interpretive derivative; selection uses ĥ.

### 1.2 Survival over a plan is not a product of step hazards

Planning needs the survival function over L steps, and it is **not** (1 − ĥ)^L.
Residuals are autocorrelated: in the minimal world the measured coherence length
is five steps (§7.4). A product over steps therefore underestimates survival
systematically. The survival function must be estimated at the **coherence-length
grain**, not the step grain — the same granularity that makes the partition
recoverable at all. The coherence length is one quantity serving two layers.

### 1.3 H_off — the external reference, and why it stays in time units

For the separation to hold, H_off must not be "how long was this description used
later". That is the same censored, selection-contaminated quantity under a
different name.

**H_off(D) is the rollout horizon measured on controlled material**: stored raw
windows, each description rolled forward without new observation, the step
recorded at which deviation first exceeds ε. Equal exposure budgets across
descriptions, no selection effect from the description under test, no possibility
for it to avoid the context it is tested on. The censoring problems are removed by
the *controlled material*, not by changing what is measured.

Keeping the unit as steps is not incidental. Planning admissibility (§3) compares
H to a plan length L, and a quantity that is not in steps cannot enter that
comparison.

### 1.4 V_Δ — the second reference, and an open question

The perturbation survival volume

    V_Δ(D) = ∫₀^{η_max} R_D(η) dη,    R_D(η) = P_{δ∼Δ_η}[ r(D, e+δ) < ε ]

is censoring-free by construction and closer to the ARW notion of stability than
any temporal quantity. It is *not* interchangeable with H_off: it has no time
unit and answers a different question.

Both are kept, and their relation becomes an empirical question (Q-SCA-09):
**does perturbation robustness predict rollout persistence?** The machinery
already exists — the offline stability profile over an η-grid in the existing
recapitulation phase is R_D(η) up to the integration.

## 2. Selection is lexicographic

Selecting for lowest hazard alone has a degenerate maximiser: a maximally coarse
description never fails because nothing violates it. This is the F1 condition one
level up, and it is not hypothetical — it was measured (§7.5). Selection is
therefore ordered, not scalarised:

    admissibility  ≻  prediction competence  ≻  hazard  ≻  switch cost

1. **Admissibility.** Exclude degenerate descriptions — those that make no
   distinctions, or fail to carry the distinctions the situation requires.
2. **Prediction competence.** Exclude descriptions whose error exceeds a fixed
   level (§2.1).
3. **Hazard.** Among the remainder, take the lowest ĥ_t.
4. **Switch cost.** Only at practically equal hazard, prefer the incumbent.

Level 4 makes switch minimisation an **inertia principle and tie-break** rather
than a primary objective. That is a demotion of the criterion as currently stated
in `docs/context_navigation/switch_minimization_criterion.md`, and it is raised
here as a request to that document's owner, not adopted silently.

### 2.1 The competence floor must be external and stratified

Level 2 requires E_pred(D) ≤ E_floor + δ, and E_floor may not come from the
agent's own history — otherwise the constraint drifts with the agent and stops
constraining. It is measured on a reference arm with fixed environment and regime,
identical sensory equipment, identical predictor model, no scope reorganisation,
and identical training and evaluation budget.

E_floor is not a scalar. It is stratified:

    E_floor( B, developmental stage, Π-capacity )

Without stratification an agent that has just acquired a new sense, or a larger
description capacity, is judged against a floor established for equipment it no
longer has.

**Consequence to state explicitly rather than discover as a bug:** because the
floor moves with capacity, a description admissible at capacity m can become
inadmissible at capacity m′. The ordering is capacity-relative.

## 3. Planning admissibility

Reacting requires a description to hold at the present instant. Planning requires
that it hold **under iteration**: an action sequence is evaluated by rolling the
description forward without new observation, so the rolled-forward description
must remain a valid argument of the map that produced it.

`docs/core/scope_transition.md` names the failure mode:

> Scope transition occurs when a descriptive regime (scope) loses its ordering
> dominance because the degrees of freedom it suppresses become dynamically
> relevant.

A projection suppresses degrees of freedom by construction; under iteration the
suppressed ones accumulate influence. H_off is therefore the time to scope
transition under iteration, and it is finite for any proper projection.

**Claim.** A plan of length L formed under S is admissible only if the survival
function of the active description, evaluated at the coherence-length grain,
exceeds the required confidence at horizon L. Beyond that the plan is not wrong in
detail — it lies outside the scope in which it was formed, which is a distinct
failure and needs its own place in the falsification taxonomy (§8.2).

Plan length is thus not a free parameter of the agent but a certified quantity.

## 4. The two loops

`docs/notes/conflict_navigation_nested_calibration.md` establishes the structure:
a lower loop calibrates observables within a fixed scope, an upper loop calibrates
the scope itself, and the two run on separated timescales.

A plan is neither loop's output. It is a trajectory proposed *inside* a scope and
evaluated against B. It sits at the lower loop but presupposes what only the upper
loop can supply.

**In a planning agent the upper loop certifies that the active description will
carry the plan's length.** In a purely reactive agent it need only select a scope
that holds now. This is what makes the two loops non-redundant and gives context
navigation a function beyond mode selection.

It is also the correct home for ĥ. The internal estimate is maintained in the
lower loop; whether it is any good is decided in the upper loop, on the timescale
of repeated regime exposures — which is precisely the separation that a
single-timescale self-set resolution failed to achieve (§7.5).

## 5. What selects a projection

Three pressures act on the choice of D ∈ Π and do not agree:

| Pressure | Pushes the projection |
|---|---|
| closure under iteration (large H_off) | **wider** — fewer suppressed degrees of freedom |
| expressibility of B | onto the *particular* components in which B is stated |
| rollout search cost | **narrower** — search is exponential in horizon and dimension |

No projection is simultaneously wide, B-expressive and narrow across all regimes.
**Different regimes resolve the tension differently, and that is the proposed
generator of mode structure** — modes as solutions of a three-way constraint
rather than as a by-product of a capacity limit. One quantity per pressure, each
measurable without the agent in the loop: H_off, expressible(D, B) as a binary,
and |D| as the active-component count.

## 6. Resolution without committing to ε

`docs/advanced/observable_space_cover_height.md` probes scope granularity across
all resolution scales at once, over the **BC index** — a sweep of points with BC
coordinates. An agent has no BC sweep; it has its own sensor history.

**Transposition to the time index.** The same construction over the stream's
one-step residuals: contiguous covers at each ε — contiguous grouping, not a ball
cover, transitivity not applied, exactly as in the BC-space method — accumulated
across ε levels. The plateau gives the number of descriptions needed with no ε
selected. Two additions the time index requires:

- **Coherence length.** Cover membership is assigned over contiguous segments, not
  per sample. Per-sample assignment recovers the right *number* and the wrong
  *partition* (§7.4). This is the same grain the survival function needs (§1.2).
- **Null by control condition, not surrogate.** A stationary stream under the
  identical procedure supplies the comparison. Permutation does not: permuting
  segments preserves the regime structure, permuting samples destroys the state's
  autocorrelation along with it. Temporal structure and regime structure are not
  separable by permuting the stream.

---

# Part II — ART level

## 7. Measurements this design rests on

From the simulation series 2026-07-22 to 2026-07-29
(`Simulationen/labyrinth_scope_constructing/`, `Simulationen/kontextnavigation_minimal/`,
external to this repo). Negative results included; three are load-bearing.

### 7.1 A regime distinction must not be locally readable

`two_band` gave its substrates a distinguishing *feature*. The feature was present
(AUC 0.89 for the best candidate observable against a median of 0.013; 39 of 109
candidates above |AUC−0.5| > 0.10) and selection recruited it (ranks 0 and 1 of
109). No partition formed: NMI(mode × substrate) 0.052, separation ratio at its
permutation null (mean excess −0.016 over five seeds).

**Reading.** The distinction was absorbed into the shared vocabulary instead of
partitioning the library. If every description can already tell the regimes apart,
specialising is redundant. A regime distinction is a scope boundary only when it
cannot be read off the description's inputs.

### 7.2 The forward map must predict the change

Fitted on an absolute target with the persistence block initialised to identity,
surviving forward maps carried **97.2 %** of their weight in the persistence block
and **2.2 %** in the action block. Such a map cannot register a regime acting only
on the action→effect relation: the measured error ratio across an unannounced
action inversion was 0.84–1.14 — the agent did not notice.

Predicting the change instead raised the action share to 8.6 % (17×). Navigation
competence collapsed in the same move (near-miss rate 0.075 → 0.000), including at
a stable library, so the two effects are separate and the second is unexplained.

### 7.3 Cost structure

Offline, no agent in the loop: building a description from nothing costs 99–110
steps to reach its error plateau; identifying which of two converged descriptions
applies costs 5 steps. Ratio ≈ 20. The *realised* advantage of holding a library
was 1.4. The missing factor is detection latency, not identifiability — the agent
checks alternatives only when its salience monitor fires, on a fixed window, after
a threshold is crossed.

This is the quantitative reason for §4: certification belongs in a loop with its
own timescale, not in the reactive path.

### 7.4 What worked

Minimal world, latent regimes differing only in which action produces which
effect, no policy and no reward — prediction is the payoff:

| | value |
|---|---|
| descriptions at end of life vs. number of regimes | 2.8 vs 2 |
| share of recoveries landing on a pre-existing description | 0.88 |
| partition agreement, per-sample assignment | 0.508 |
| partition agreement, contiguous segments ≥ 5 samples | **1.000** |
| gain over one description, two regimes / stationary control | 0.357 / 0.131 |

The coherence length at which agreement becomes exact (5 samples) equals the
independently measured identifiability limit from §7.3. The coherence length the
partition needs and the identifiability limit are the same quantity — which is why
§1.2 uses it for the survival function as well.

Under a capacity cap of two active components the two descriptions' component sets
become **disjoint** (overlap 1.00 → 0.00) while agreement stays at 1.000. The cap
does not improve detection; it makes the absorption of §7.1 structurally
impossible. It does not distinguish modes from regimes on its own — a stationary
world under the same cap also produces distinct projections — so it composes with
the control-condition null rather than replacing it.

### 7.5 The degenerate maximiser is not hypothetical

A single-timescale self-set resolution fails. Each description setting its own ε
from the robust tail of its own working error, swept over the one free constant:

| constant | descriptions, stationary world | descriptions, two regimes | switches |
|---|---|---|---|
| 4 | 4.50 | 6.50 | 2.75 |
| 8 | 1.00 | 1.50 | 0.00 |
| 16 | 1.00 | 1.00 | 0.00 |

No value passes both conditions: the agent either invents descriptions in a world
that never changes, or stops noticing the real change. At the constant that
silences the false alarms it also has **zero** detections — a stable library, no
novelty, no switches, and no discrimination. That is the degenerate maximiser of
§2 in measured form, and it is why the joint signature of §9 needs its competence
constraint.

**Retraction carried from revision 1.** This was reported as showing that a
modulator cannot be set from operator-side experience at all. Too strong. What is
shown is that a **single-timescale** self-set resolution fails — the description
set its own ε from its own recent error while that same ε governed whether the
error counted. The nested construction with a slow upper loop is a different
architecture and is untouched by this measurement. §4 adopts it.

---

## 8. Falsification

### 8.1 The cheapest available falsifier — run, and it went against the design

Measured 2026-07-29 (`Simulationen/kontextnavigation_minimal/persistence.py`), six
seeds, descriptions recovered by the chunked mixture of §6:

| H_off measured against | median, per seed |
|---|---|
| a fixed one-step ε | 1 – 3 steps |
| the oracle accumulation floor | 2 – 6 steps |

The second row is the honest one. Comparing a *cumulative* rollout deviation
against a *one-step* ε measures noise accumulation — after k steps the irreducible
deviation alone grows like √k — so the threshold is calibrated against the true
generating map rolled forward over the same actions, and the horizon is the first
step at which the description exceeds that floor by more than ε.

The short horizon survives the correction. **The descriptions are one-step
predictors.** Planning admissibility H ≥ L is satisfiable only for plans of length
two to four, which is not planning in any useful sense. §5's capacity cap is not
the culprit — the horizon is this short before any cap is applied.

### 8.2 Q-SCA-06b answered, and underdetermined

Same runs. ĥ against the oracle-calibrated H_off, pooled over 690 (description,
time) pairs:

| | Spearman ρ |
|---|---|
| ĥ vs H_off | **−0.688** |
| current residual r_t vs H_off (the control) | −0.665 |
| ĥ vs H_off, rank of r_t regressed out of both | **−0.26, +0.03, −0.10, −0.18, −0.06** per seed |

ĥ predicts the horizon in the right direction — and so does the present error, and
almost as well. With the residual's rank removed the partial correlation is small
and inconsistent in sign. **In this world ĥ is a monotone recoding of the present
error**: prospective in name, retrospective in content. The control that caught
this was built into the test before it was run, for exactly this reason.

**The conclusion must not be over-drawn.** Finding 8.2 is underdetermined by
finding 8.1: where H_off ranges only over 1–6 steps and its variance is dominated
by the starting residual, there is no room for a prospective signal to become
visible. What is shown is that hazard estimation contributes nothing *where the
horizon has no dynamic range* — not that it is impossible. The same over-reach was
made about ε_m and had to be retracted (§7.5); it is not repeated here.

### 8.3 The resulting requirement on the next world

The persistence layer cannot be tested in a world whose descriptions have no
horizon. The minimal world is an action-driven random walk: beyond the next few
steps there is nothing to be right about.

**Requirement, quantified:** H_off must have at least an order of magnitude of
dynamic range across descriptions and situations before Q-SCA-06 is answerable.
Worlds with deterministic multi-step structure — the generator families already in
use in this repository — meet this by construction, and a world's H_off
distribution should be measured *before* an agent is run in it, exactly as the
salience check now precedes every transfer sweep.

### 8.4 Out-of-horizon plan failure needs a category

A plan failing beyond the certified horizon is a different failure from one
failing inside it. The falsification enum is closed (GUARD-2: F0, F1, F1_BC, F2,
F3, F4, F-gradient), so this document assigns no id and flags the gap for the
taxonomy owner.

### 8.5 What would retire the persistence layer

If ĥ_t ranks descriptions no better than the present residual does against H_off
measured on controlled material (Q-SCA-06b), in a world that satisfies §8.3, the
internal state variable knows nothing about its own remaining load-bearing
capacity and is repeating its own past. That is an answer about the architecture,
not a cue to re-tune the estimator. The 2026-07-29 run produced that pattern but
in a world that does *not* satisfy §8.3, so it does not discharge this test.

---

## 9. Open questions

Continuing the Q-SCA series (01–05 in use before this document; grep-checked
2026-07-29 — 06–09 free, as are the prefixes Q-PLAN, Q-HOR, Q-CVH).

**Q-SCA-06 (open) — does the agent know its own remaining load-bearing capacity?**
Split into three, because the three answers have different consequences:

- **06a Calibration.** Does a predicted hazard of 0.2 correspond to an observed
  failure rate near 0.2 under the controlled offline test?
- **06b Ranking — measured 2026-07-29, underdetermined (§8.2).** Does ĥ order
  descriptions correctly by their later measured H_off, *beyond what the present
  residual already orders*? First measurement: ρ = −0.688 for ĥ, −0.665 for the
  residual control, partial correlation small and sign-inconsistent. Not evidence
  against the layer, because the world used had H_off ∈ [1, 6] and cannot resolve
  the question (§8.3). Re-open in a world meeting the dynamic-range requirement.
  *Ranking alone is sufficient for selection;* calibration is required only for
  the stronger theoretical claim.
- **06c Generalisation.** Does the prediction hold under new regimes, other
  perturbation magnitudes, and BC-preserving transfer — or is it in-sample only?

**Q-SCA-07 (open).** Can an upper calibration loop on a slower timescale set ε
where a single loop provably cannot (§7.5)? Candidate information source:
cross-description contrast, the gap between the active description's error and the
best alternative's, which exists only because a library exists.

**Q-SCA-08 (open).** Does the three-way tension of §5 generate mode structure, or
does one pressure dominate and reduce it to a capacity limit? Requires all three
quantities on the same runs, added one at a time with a measured delta.

**Q-SCA-09 (open).** Does the perturbation survival volume V_Δ predict the rollout
horizon H_off? If yes, one offline reference suffices and the existing
recapitulation stability profile is already most of it. If no, robustness under Δ
and persistence under iteration are distinct properties of a description and both
must be carried.

**Q-SCA-10 (open) — the world requirement, from §8.3.** How much dynamic range must
H_off have before Q-SCA-06 is answerable at all? The measured lower bound is: more
than the 1–6 steps an action-driven random walk provides. Which generator families
meet an order-of-magnitude range, and should a world's horizon distribution be
measured before an agent is run in it, as the salience check now precedes every
transfer sweep?

### 9.1 The joint signature, and its necessary constraint

Over training, the following would be evidence that the system maintains
descriptions rather than continually reconstructing them: library novelty falling,
description lifespan rising, transfer improving, switch frequency falling.

**All four are produced trivially by an agent that stops distinguishing.** A single
coarse description has zero novelty, unbounded lifespan and zero switches — see
§7.5 for this in measured form. The signature is evidence only under the explicit
side condition E_pred(D) ≤ E_floor + δ with E_floor external and stratified per
§2.1. Without it the signature measures rigidity, not learning.

---

## 10. Discipline and outstanding items

The predecessor build reached roughly fifteen interacting mechanisms with no
ablation ladder, and six measurement criteria were retired in one week. Two rules
carried forward:

1. **Every criterion ships with a null construction and a degenerate arm on which
   the null must be exactly recovered.** The one-description arm returning excess
   0.000 on all seeds is the template. A criterion without a passing null
   calibration is not reportable.
2. **Every mechanism enters singly, with a measured delta.** Anti-circularity per
   brief v2 §3 applies to each: the offered space must exceed what the hypothesis
   needs. For §5 the component pool must include components that could *not* serve
   the hypothesis, so that a projection choosing them is a finding.

**Registrations completed 2026-07-29:** row in `docs/meta/DOC_INDEX.md`; session
entry in `docs/notes/research_journal.md`; Q-SCA-06a/06b/06c, 07, 08, 09, 10 in
`docs/notes/open_questions.md`, with the ID-collision check run against
`open_questions.md` and all of `docs/` before assignment (06–10 unused in the Q-SCA
prefix; the candidate prefixes Q-PLAN, Q-HOR, Q-CVH also free and not taken).

**Raised for a document owner, not adopted here:** §2 level 4 demotes switch
minimisation from a criterion to a tie-break. `docs/context_navigation/switch_minimization_criterion.md`
states it as a criterion. That document should decide whether the demotion is
accepted, and this one should be corrected if it is not.
