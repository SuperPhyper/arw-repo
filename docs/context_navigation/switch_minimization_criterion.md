---
status: hypothesis
layer: docs/context_navigation/
title: "Switch Minimization as Description Criterion — Salience Rate as an Online Persistence Estimate"
created: 2026-07-26
depends_on:
  - docs/context_navigation/scope_constructing_agent_architecture.md
  - docs/context_navigation/sleep_as_perturbative_description_consolidation.md
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/admissibility_and_mode_selection.md
  - docs/glossary/perturbation_spread.md
  - docs/advanced/epsilon_and_scope_resolution.md
related:
  - docs/notes/scope_constructing_agent_implementability.md
  - docs/cognitive_architecture/agent_context_navigation_project_brief_v2.md
  - existence_test_preregistration_wp3.md (external — not in repo; unfrozen, import is part of its own freeze protocol)
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/salience_mode_ecology.md
open_questions:
  - Q-PAR-01
  - Q-PAR-02
  - Q-PAR-03
  - Q-PAR-04
  - Q-PAR-05
---

# Switch Minimization as Description Criterion

> **Status.** Hypothesis. Proposes an objective for the scope-constructing agent of
> [`scope_constructing_agent_architecture.md`](scope_constructing_agent_architecture.md):
> the agent should minimize the number of mode switches it needs, subject to remaining
> able to navigate. The claim of this document is not that this is a good heuristic but
> that it is **the same criterion** as the offline persistence criterion of
> [`sleep_as_perturbative_description_consolidation.md`](sleep_as_perturbative_description_consolidation.md)
> §4, measured on a different axis — and that it supplies the first *mechanism* in this
> programme that predicts a mode count rather than hoping for one (§6).
>
> **Provenance.** Rico's formulation, 2026-07-26: *only structurally strongly different
> contexts should make a mode switch necessary; minimizing salience events is more or
> less the goal, because that is what raises general efficiency.* This document works out
> what has to hold for that statement to be implementable, and names the three routes by
> which it degenerates if the constraint is dropped (§3).

---

## 1. The principle, stated so it can fail

> **C-PAR.** Among descriptions that keep navigation admissible, the agent should prefer
> those that require the fewest mode switches. A context should force a switch only when
> it is structurally different enough that no admissible description covers both it and
> the incumbent context.

Two things this is *not*:

- Not "salience is bad". Salience is the only channel through which new modes form at
  all (`scope_constructing_agent_architecture.md` §5, fourth branch). An agent that
  suppresses salience from step 1 never builds a mode ecology — see §8.
- Not an action-reward term. Putting a switch penalty into the PPO reward makes the agent
  avoid switch-*producing contexts* rather than describe better; that route is excluded
  in §5 and it is excluded for a measurement reason, not a taste reason.

---

## 2. The identification: a salience event is an ε-exceedance

This is the load-bearing step. In the implemented agent
(`Simulationen/labyrinth_existence_wp1/s_online.py`) salience is

```
ŝ(t) = ‖obs_ema(t) − c_active‖₂ / √D
```

the deviation between what the active archetype's context centroid "predicts" and what
is observed. Project brief v2 §2.2 and the WP1 module docstring both name this correctly
as **a σ_Δ-type quantity relative to the active regime cell**. The trigger is
`ŝ(t) > THETA_SAL`, debounced over `SAL_K` consecutive steps with a refractory window.

Therefore:

```
THETA_SAL  =  ε_agent
```

The agent-side resolution threshold **already exists in the code**. It was calibrated
(random-walk 75–90th percentile → 6–12 events/episode) rather than derived, and it is
frozen as a hyperparameter in `existence_test_preregistration_wp3.md` §1. And a salience
event is exactly the event

```
{ t : σ̂_Δ(t) > ε_agent }   (debounced)
```

so the **switch count is the empirical count of ε-exceedances of the perturbation-spread
proxy under the active description.** Three formulations that looked distinct are one:

| Formulation | Reading |
|---|---|
| minimize mode switches | fewest ε-exceedances |
| maximize description persistence | the active description survives more of the Δ the environment delivers |
| operate as high in I_ε as admissibility allows | approach the upper end of `sup_x σ_Δ(x) < ε < ε*(O,X)` |

This also answers D-1 of
[`scope_constructing_agent_implementability.md`](scope_constructing_agent_implementability.md)
§9 — but with a twist that §3 makes essential: ε *is* agent-side, and it must **not** be
agent-optimized.

### 2.1 Two ε's, kept strictly apart

Repo rule: no silent redefinition of ε. There are now two, and they must never be
conflated in a report:

| Symbol | Where | Space | What it gates |
|---|---|---|---|
| ε_agent | `s_online.THETA_SAL` (0.18) | 10-dim observation space, L2/√D | when a deviation counts as a scope failure → encounter closure |
| ε_observer | `s_observer.EPS_MIN…EPS_MAX` sweep | 4-dim `action_dist` (L1) and 10-dim `obs_mean` (L1) | when two behavioural windows count as the same regime → the partition |

Whether the agent's own context partition under ε_agent coincides with the observer's
behavioural partition under ε_observer is an open question and the agent-level analogue
of Q-SCA-03 → **Q-PAR-01**.

---

## 3. The degeneracy, and why the constraint is not decoration

Raw switch minimization has a trivial optimum: *stop distinguishing*. Three concrete
routes exist, one of them already implemented as a fallback:

1. **Reference tracking.** `s_online.py` sets `_active_ref = obs_ema` on coverage failure
   (and in `'vector'` mode always). That zeroes the deviation by construction. An agent
   rewarded for low salience learns to pull the reference onto the observation, not to
   describe better. The current architecture's fallback *is* the degenerate minimizer.
2. **Raising ε_agent.** Trivially reduces the event count. At ε_agent ≥ ε*_agent the
   context cover collapses to one cell — one mode, no distinctions, no navigation.
3. **Uninformative weighting.** Only bites if ŝ becomes description-relative (measured in
   the active weighted description, which §5 of the architecture document arguably wants):
   then concentrating w on a near-constant observable minimizes deviation. The simplex
   constraint (clip at 0.01 before normalization, Σw = 1) prevents collapse to zero but
   not concentration.

All three are the same failure, and it already has a name. With

```
ε*(O, X_B) := inf { ε > 0 : |C_ε| = 1 }
```

(`docs/advanced/epsilon_and_scope_resolution.md`, Felder 2026 Prop 1), the agent-level
collapse threshold ε*_agent is the resolution at which the agent's context cover becomes
trivial. Every degenerate route drives the agent to ε_agent ≥ ε*_agent, i.e. **F1 —
observable insufficiency**. The failure mode of C-PAR is a named ARW falsification
category, which is the reason to take the principle seriously and the reason it needs a
hard constraint.

### 3.1 The resolution: three knobs, one job each

| Knob | Role | Who sets it |
|---|---|---|
| **ε_agent** (`THETA_SAL`) | resolution at which a deviation counts | **fixed exogenously** (0.18, from WP1 calibration). Never optimized by the agent. Reported at ±1 step as a robustness check. |
| **λ** (parsimony pressure in consolidation) | how strongly few-switch descriptions are preferred *at fixed ε* | swept — this is the graded BC axis κ (§6.2) |
| **η** (observation-noise magnitude) | magnitude axis of Δ | swept independently, only for R_m / 𝒫_m estimation |

With ε_agent held fixed, the only remaining route to a lower switch rate is **a better
description**, which is precisely the intended target. Routes 1 and 3 are then blocked by
§8's structural rule; route 2 is blocked by construction.

---

## 4. The criterion

> **One-sided — qualification added 2026-07-27.** Everything below is an *upper* bound
> on the failure rate. A description that never breaks carries no partition at all, so the
> criterion needs a lower bound as well:
>
> ```
> 0  <  failure rate  <  parsimony bound
> ```
>
> structurally the same two-sided form as `sup_x σ_Δ(x) < ε < ε*(O,X)`. §3 below finds
> three ways the agent could *cheat* the count to zero and closes them; it does not ask
> what happens when the count reaches zero legitimately, which is the same destination by
> an honest route.
>
> Two caveats, both measured 2026-07-27. The floor is **necessary but not sufficient**:
> descriptions fail at ordinary rates (median failure rate 0.27 over evaluated variants),
> so a non-zero floor removes a degenerate corner without making a description
> BC-responsive. And the separation figures that motivated this box were subsequently
> found defective in three successive versions (circular, saturated, wrong grain), so no
> separation verdict is claimed here in either direction; the agent in fact navigates
> ~10× better than chance. What survives independently of that ratio is the measured
> cause: every selection criterion here is a *within-window* statistic while BC
> information sits in *levels across* contexts. See
> [`../notes/observable_information_and_bc_responsiveness.md`](../notes/observable_information_and_bc_responsiveness.md)
> §7 and Q_NEW_G. Nothing below is retracted; it is incomplete.

Write for a description (archetype) *a*: `dur(a)` = mean encounter duration under *a*,
`ρ(a)` = mean `progress_rate` under *a*. Both quantities are **already recorded per
encounter** (`duration`, `progress_rate` in the protocol record); the only bookkeeping
addition is a running mean of `duration` on the archetype, alongside the running context
centroid it already maintains.

Note first that at fixed ε_agent,

```
switch rate under a  ≈  1 / dur(a)
```

so minimizing switches is maximizing mean encounter duration. No new instrumentation is
required to state the criterion — only a changed revision rule.

**Lexicographic form (recommended):**

```
admissible(a)  :⟺  ρ(a) ≥ ρ_min
revision rule:  among descriptions covering the same context region,
                keep the admissible one with the largest dur(a);
                if none is admissible, keep the one with the largest ρ(a)
                and mark the region unresolved
```

**Why lexicographic and not a weighted sum** `J(a) = ρ(a) − λ/dur(a)`: a weighted sum has
a free coefficient that can be tuned until the library holds about three archetypes. That
is the interpretation door of project brief v2 §3 reopening from the objective side. The
lexicographic form has no such coefficient. λ then enters *only* as a swept parameter
(§6.2), never as a fitted one.

**Why duration alone is not enough**: long encounters that go nowhere maximize `dur`
perfectly. Hence admissibility is a hard filter, not a term. `ρ_min` must be set from a
non-hypothesis reference — proposal: the random-walk baseline `progress_rate` used for the
WP1 `THETA_SAL` calibration, so that "admissible" means "better than not describing at
all".

**Code-level attachment points** (both in the fork, both small):

- `s_sleep.py`, revision rule (currently: `proto['progress_rate'] > match['effectiveness']`
  → winner-takes-place): replace the scalar comparison with the lexicographic rule.
- `s_online.py`, `_close_encounter_and_update`: `w_target` selection currently follows the
  matched archetype's `w_out` with effectiveness-annealed exploration. `confidence` should
  read the new criterion, not raw `progress_rate`.
- `s_online.py`, reference handling: `_active_ref` must come from a stored archetype
  context, never from the live EMA (§8).

---

## 5. Why the objective must not enter the reward

PPO controls actions; the description is controlled by the weight field and the archetype
library. A switch penalty in the reward is therefore optimized by the wrong actuator: the
agent learns to **avoid contexts that produce switches** — route around zone boundaries,
stay in the substrate it already describes well — instead of learning descriptions that
survive those contexts.

That is not merely suboptimal, it destroys the measurement. The primary observable of the
whole programme is `π_action`, the action distribution within an encounter window
(`..._emergent_modes_experiment.md` §2.1). An objective that reshapes trajectories to
avoid boundary crossings changes the observable and the zone-correspondence analysis at
once, and the resulting partition would report the *avoidance* structure, not the
description structure.

This settles D-4 of the implementability analysis in favour of library-only
recapitulation and library-only parsimony: **the offline phase and the effectiveness
criterion are the only admissible attachment points.**

---

## 6. Consequence 1: a mechanism for the mode count

### 6.1 Why N should converge

Under parsimony pressure at fixed ε_agent and a hard admissibility filter, the library is
driven toward the **minimal number of descriptions sufficient to keep navigation
admissible across the encountered substrates**. If each substrate class is an
admissibility filter in the sense of `simulation_revision_design_notes.md` — it preserves
at least one policy substrate and invalidates at least one competing one — then the
minimal sufficient count is the number of *structurally distinct* filters encountered.

This is the first mechanism in the programme that **predicts** H1 of
`..._emergent_modes_experiment.md` ("N matches the number of structurally distinct zone
types") rather than hoping for it. In the existing design nothing pushes N toward the zone
count; the old run's library grew to 20 archetypes in 3 pre-given categories while
competence fell. Under C-PAR, that growth is exactly what the criterion forbids.

Note what is *not* prescribed: a number. Parsimony is prescribed; the number comes from
the environment. The anti-circularity doors of brief v2 §3 stay shut, on one condition —
§6.2.

### 6.2 λ as the graded BC axis (and the sweep that keeps it honest)

λ must be **swept and reported as a curve N(λ)**, never fitted. A single λ that yields a
convenient N is a tuned result. What is a result is the *plateau structure* of N(λ):
an interval of λ over which the mode count is stable is the same object as an ε-plateau in
the physics cases — a partition invariant stable over a BC parameter.

This resolves blocker §4.6 of the implementability analysis without touching the
environment:

- λ is an architectural boundary condition (`context_navigation_model_spec.md` §2: B =
  architectural boundary conditions), so a λ-sweep is a legitimate BC sweep at the agent
  scope, structurally analogous to sweeping K in Kuramoto.
- A λ-sweep yields θ*(λ) and a `sweep_range`, which is exactly what `pipeline/transfer_v2.py`
  requires and what an ε-axis behavioural sweep cannot provide
  (`pipeline/sweep_behavioral.py` docstring). **Φ becomes computable, and WP2 stays
  untouched.**
- η remains a separate, independent axis, needed only for R_m / 𝒫_m. Sweeping λ and η
  together would confound parsimony pressure with perturbation magnitude; they are
  orthogonal by design and must be reported orthogonally.

Caveat to record: along a λ-sweep the *agent* varies, not the environment. The partition
is over agent configurations at fixed environment — admissible as a BC sweep, but not the
same object as the categorical zone-topology comparison. Both are run; neither replaces
the other.

---

## 7. Consequence 2: 𝒫_m — and a circularity that must be controlled

The objective directly rewards descriptions that survive more perturbation, so it
directly rewards a wide stability domain 𝒫_m. That is good news for plausibility: §14's
sharp prediction (𝒫_m wider than the training perturbation envelope) acquires a mechanism
instead of being a surprise.

It is also a hazard. Under C-PAR there are now **two** candidate explanations for a wide
𝒫_m: scope-varied recapitulation (the C2 claim) and the parsimony objective itself.
Consequences for the experiment design of `scope_constructing_agent_architecture.md` §14:

1. 𝒫_m width must be measured for **C0 and C1 as well**, not only C2. If C0 already shows
   extrapolative width, the width is the objective's doing and carries no information
   about recapitulation.
2. The C-SCA claim becomes **differential**: C2 − C1 in 𝒫_m width at identical objective,
   identical ε_agent, identical λ. The absolute statement "𝒫_m exceeds the training
   envelope" is no longer attributable to recapitulation on its own.
3. The objective must be held constant across all arms, which also means arm A and arm B
   need a defensible analogue of it or an explicit statement that they lack one.

Registered as **Q-PAR-03**. This is a sharpening of §14/§15, not a refutation — but
without it, C2 would win for a reason that has nothing to do with recapitulation.

---

## 8. Cold start: parsimony belongs to consolidation, not to triggering

Salience is the mode-*formation* channel. A criterion that suppresses salience online
prevents the library from ever forming — premature parsimony, the mirror image of the old
run's pathological proliferation.

**Structural rule (recommended, and it closes two problems at once):**

> Online triggering runs at fixed ε_agent and is never suppressed, penalized, or
> reference-tracked. Parsimony acts **only** on which descriptions survive consolidation.

This blocks the reference-tracking exploit (§3, route 1) and the cold-start problem
simultaneously, because the quantity the agent could game is no longer under the agent's
online control. It also implies a concrete correction to the current code: on coverage
failure `_active_ref` must **not** be reset to `obs_ema`. The encounter is marked
*unresolved* (the fourth branch of the architecture document's §5) and enters
recapitulation at maximum priority, while the reference stays at the last stored archetype
context.

Relation to `scope_constructing_agent_architecture.md` §12: the intermediate mode m_{A/B}
is where an unresolved region is held while it is still being described. Under C-PAR its
cost should be low early and high late — an annealing that follows from the criterion
rather than being added to it. Whether that is the same object as the R3 mediation pathway
remains Q-SCA-04.

---

## 9. Which salience the criterion is defined on

Three salience definitions now coexist in the repository. This matters because C-PAR
minimizes a *count of events*, and the three do not produce the same events:

| Source | Definition | Status |
|---|---|---|
| `salience_mode_ecology.md` §5 | S(c) = Var_m(F_m(c)) — variance of mode fitness across modes | not implemented; would require evaluating *all* modes' fitness per context, which the code never does (it computes nearest-archetype distance only) |
| `agent_online_scope.md` §3 | three named triggers + strength grading | **superseded** by WP1 (brief v2 §2) |
| WP1 code / brief v2 §2.2 | ŝ(t) = ‖obs_ema − c_active‖₂/√D, deviation from the active description | implemented; **C-PAR is defined on this one** |

Minimizing the third does not minimize the first: the third is a property of the active
description alone, the first of the whole ecology. Whether a parsimony pressure on the
third also reduces the first is **Q-PAR-04** — and it is the point where C-PAR touches
`salience_mode_ecology.md`'s claim that salience is a property of the mode ecology rather
than of stimuli.

**Minor consistency note, recorded but not blocking.** `salience_mode_ecology.md` §5 reads
"low variance → one mode clearly dominates → low salience". Under its own formula the
opposite holds: a dominating mode (0.9, 0.1, 0.1) has *high* fitness variance, while
comparable fitnesses (0.5, 0.5, 0.5) have variance zero. Either the formula or the
interpretation needs a sign correction; a doc-consistency pass should settle which.

---

## 10. Consequences for the existing programme

| Item | Resolution |
|---|---|
| D-1 (is ε agent-side?) | Yes, and it already exists as `THETA_SAL`. But it is **exogenous** — fixed, never optimized (§3.1). |
| D-2 (which κ?) | κ = λ (parsimony pressure). η separate, for Δ only. Environment untouched, WP2 unaffected. |
| D-4 (library-only or PPO-coupled?) | Library-only. The reward route is excluded on measurement grounds (§5). |
| D-5 (F vector-valued?) | Unchanged and reinforced: the criterion needs no failure *classes*, only durations and admissibility. |
| D-7 (freeze WP3 first?) | Compatible: C-PAR needs `THETA_SAL` fixed, which is what WP3 freezes. But λ, ρ_min and the revised revision rule are constants WP3 does not cover → the SCA programme needs its own preregistration, as recommended in the gap analysis §7. |

**Cheap retrospective test, available now.** `n_saliency` is logged per episode across all
four labyrinth generations. C-PAR predicts that switch rate and competence move
*together* (fewer switches ↔ higher `goal_rate`) once descriptions are good. Brief v2 §6
reports the old run going the other way: `n_saliency` 12.7 → 18.3 while `goal_rate`
0.168 → 0.135 and consolidation rose monotonically. That is one data point in C-PAR's
favour as a *diagnostic*. The per-run correlation across seeds and substrates can be
computed from the existing `results*.zip` logs before any new code is written, and it is
the first thing that could cheaply embarrass the principle.

---

## 11. What would withdraw C-PAR

- **It is one-sided, and the missing side matters more than expected.** If the
  lower bound of §4 (a non-zero, clustered failure rate) turns out to do all the
  empirical work — i.e. if any description satisfying it performs about as well
  regardless of how far the switch rate is then minimized — then C-PAR is a
  constraint dressed as an objective, and the objective part should be dropped.
- **It is a relabeling.** If the lexicographic rule produces the same library as plain
  `progress_rate` winner-takes-place on the same protocol buffers, C-PAR has added
  vocabulary and nothing else.
- **The rate measures nothing.** If switch rate at fixed ε_agent is uncorrelated with
  transfer Φ to unseen instances across seeds, then few switches is not evidence of a
  better description, and the objective is optimizing an artifact of `THETA_SAL`.
- **No plateau in N(λ).** If N drifts monotonically with λ and never stabilizes, parsimony
  pressure does not produce a discrete mode count and the H1 mechanism claim of §6 fails.
  (A plateau at N = 1 is the F1 outcome of §3, not a success.)
- **Only degenerate routes work.** If, with §8's structural rule in force, the switch rate
  cannot be reduced at all without loss of admissibility, then C-PAR is statable but not
  implementable in this environment — which would itself be a result about the labyrinth's
  descriptive richness rather than about the principle.

---

## 12. Open questions

To be registered in `docs/notes/open_questions.md`. Prefix `Q-PAR` checked free
(2026-07-26; existing prefixes: AES, CNS, COM, CTX, EPO, EXT, GEN, INV, NEW, PROJ, QSC,
RD, REL, SCA, SIG, SLP, STR).

| ID | Question | Priority |
|---|---|---|
| Q-PAR-01 | Does the agent's context partition under ε_agent (`THETA_SAL`) coincide with the observer's behavioural partition under ε_observer? The two thresholds live in different spaces on different observables; if they disagree, "the agent's modes" and "the measured regimes" are different objects and the whole correspondence analysis needs a translation step. Agent-level analogue of Q-SCA-03. | high |
| Q-PAR-02 | Is the online switch rate at fixed ε a consistent estimator of the offline persistence criterion σ_Δ(D) < ε of `sleep_as_perturbative_description_consolidation.md` §4? The online rate samples whatever Δ the environment delivered; the offline criterion perturbs actively. Where they disagree, which one predicts transfer? This sharpens the discriminating experiment of that document's §9. | high |
| Q-PAR-03 | Under C-PAR, wide 𝒫_m has two candidate causes — the parsimony objective and scope-varied recapitulation. Can they be separated by measuring 𝒫_m width in C0/C1/C2 at identical objective, or does the objective saturate the effect and make Q-SCA-01 untestable in this environment? | high |
| Q-PAR-04 | Does parsimony pressure on the active-description deviation ŝ also reduce mode-competition salience S(c) = Var_m(F_m(c)) (`salience_mode_ecology.md` §5)? The two are different quantities; if they move oppositely, "minimizing salience" is ambiguous and the criterion must name its target explicitly in every report. | medium |
| Q-PAR-05 | Is C-PAR a description-length criterion in the MDL sense — mode count plus switch cost traded against residual deviation — and if so, does the λ-plateau correspond to a code-length minimum? If the correspondence holds it supplies an external, non-hypothesis calibration for λ and removes the last free parameter. | medium |

---

## 13. Relationship to existing documents

| Document | Relationship |
|---|---|
| `scope_constructing_agent_architecture.md` | Supplies the objective that document leaves open. §4's mode definition ("stable under δ ∈ Δ") becomes something the agent is actively driven toward rather than a post-hoc property. Sharpens §14/§15 via §7 here. |
| `sleep_as_perturbative_description_consolidation.md` | Same criterion, other axis. §6 there — "preference is an online estimate of the future persistence of a description" — is what C-PAR makes measurable: the switch rate *is* that estimate. Q-PAR-02 carries the discrepancy. |
| `agent_online_scope.md` | `THETA_SAL` = ε_agent is identified here; §3/§4.1 of that document remain superseded by WP1 and are not used. |
| `admissibility_and_mode_selection.md` | Supplies the admissibility notion used as the hard filter; §6.3's F0 condition for salience is the failure mode that must be distinguished from a genuine switch before the count is meaningful. |
| `salience_mode_ecology.md` | §9 here delimits C-PAR against its salience definition and records a sign inconsistency in its §5. |
| `..._emergent_modes_experiment.md` | H1 gets a mechanism (§6.1). The zone-topology comparison is preserved alongside the λ-sweep, not replaced by it. |
| `scope_constructing_agent_implementability.md` | Resolves D-1, D-2, D-4; leaves D-3, D-6, D-7 open. Removes the Φ blocker (§4.6 there) without an environment change. |
| `existence_test_preregistration_wp3.md` | Compatible in that it freezes `THETA_SAL`; insufficient in that λ, ρ_min and the revision rule are new constants. Separate preregistration required. |

---

## Maintenance History

- **2026-07-26**: Created from Rico's formulation the same day (salience minimization as
  the organizing goal). Core contribution: the identification `THETA_SAL = ε_agent` and
  hence *salience event = ε-exceedance of the σ_Δ proxy* (§2), which makes switch
  minimization, description persistence and operating high in I_ε the same criterion; the
  three degenerate routes and their common name F1 (§3); the lexicographic form that
  avoids a fittable λ (§4); the exclusion of the reward route on measurement grounds (§5);
  λ as agent-side BC sweep axis, which removes the Φ blocker recorded in
  `scope_constructing_agent_implementability.md` §4.6 (§6.2); and the circularity control
  that C-PAR forces onto §14 of the architecture document (§7). Q-PAR-01–05 proposed,
  prefix collision-checked against `open_questions.md`.
