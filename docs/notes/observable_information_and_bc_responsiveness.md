---
status: claim
layer: docs/notes/
title: "Observable Information Does Not Entail BC-Responsiveness — Self-Reading Observables and Self-Confirming Selection Criteria"
created: 2026-07-27
depends_on:
  - docs/core/observable_information.md
  - docs/glossary/observable_range.md
  - docs/glossary/perturbation_spread.md
  - docs/glossary/scope.md
related:
  - docs/context_navigation/scope_constructing_agent_architecture.md
  - docs/context_navigation/switch_minimization_criterion.md
  - docs/context_navigation/sleep_as_perturbative_description_consolidation.md
  - docs/notes/kht_reconciliation_scope_constructing.md
  - docs/notes/scope_component_conflict_typology.md
  - docs/meta/context_map/context_map_falsification_bc.md
open_questions:
  - Q_NEW_G
---

# Observable Information Does Not Entail BC-Responsiveness

> **Two claims, of different strength.**
>
> **C1 (demonstrated by construction).** Observable information — non-trivial cover
> plus Δ-stability, `docs/core/observable_information.md` — does not entail that the
> observable responds to B at all. The two conditions are independent. An observable
> can satisfy observable information in full and still produce an identical image on
> every admissible boundary condition, in which case it supports no regime partition
> over B whatsoever.
>
> **C2 (proposed; measured and found unsupported in this instance — see §2.1).** The
> conjecture was that any procedure selecting descriptions by their own stability has an
> intrinsic bias toward self-directed observables, the most stable thing available. C1
> shows such a bias is *possible*; the measurements show it is not *operative* here — the
> self-share across four conditions is 0.20–0.58 against a chance level of 0.31 — two
> conditions below chance, two above, no clear bias. (An earlier version of this sentence
> also cited the separation ratio; that ratio was defective, see the audit banner. The
> self-share numbers do not depend on it and carry the downgrade on their own.) C2 is
> retained as a conjecture without support, not as a finding.
>
> **C3 (measured, §2.2–2.3).** What does hold: every selection criterion in the
> implementation computes a statistic *within* a context, and a boundary-condition
> difference presents itself as a difference of *levels across* contexts. Such criteria are
> therefore structurally blind to BC-responsiveness — measured as median substrate
> separability |d| = 0.23 over the selected compositions, 14 of 32 negligible, and the
> single most substrate-diagnostic channel absent from every surviving description because
> it is *constant* within each substrate.
>
> C1 does not contradict the framework: `observable_information.md` calls its
> condition *necessary* for scope validity, not sufficient, and F1_BC already makes
> BC-unresponsiveness fatal. What is new is that nothing in the necessary condition
> *excludes* it — so a construction procedure guided by observable information or by
> persistence can converge on descriptions that F1_BC would reject.

---

> **Measurement audit, 2026-07-27 (III) — read before any separation number below.**
> The substrate-separation ratio was measured three different ways and all three were
> defective: mean prediction error (**circular** — it is what the switch criterion
> selects on), displacement rate (**saturated** — blocked cells are ~9 % of the grid, so
> mature modes sit at 0.92–0.96 everywhere and the ratio is 1.0 by arithmetic), and
> per-step progress (**wrong grain** — dominated by the long tail of milling steps).
> Every `r ≈ 1.0` in this document was produced by one of those, and none of them means
> "the descriptions do not separate".
>
> Two things were established by the audit and are not in doubt. The agent navigates
> about **ten times better than chance** — goal rate 0.050–0.073 against a random
> walker's 0.007 in the same substrates, closest-approach-within-5-cells 0.29–0.36
> against 0.030. And at **episode grain** (per episode: the mode that carried it, and
> that episode's closest approach) the values are no longer pinned near 1.0 — they range
> 0.73–1.86 across three seeds, one pass and two fails, with only 2–5 modes clearing the
> minimum sample. That measurement is real but badly underpowered at 180 episodes.
>
> Consequently: **this document makes no claim about whether the separation gate passes.**
> What survives untouched is everything that does not use that ratio — the construction
> in §1, the composition-separability measurement in §2.2 (Cohen's d over substrates
> under a fixed random walker, independent of the gate), and the channel counts in §2.1.


---

## 1. The construction

Let the system be observed by π and let the describing system also have access to its
own state — its own last operation, its own elapsed clock. Take

```
π_self : (history) → (the operation just performed)
```

Then, for any admissible B:

- **non-trivial cover.** π_self takes several values as the operation varies, so
  |C_ε| > 1. Condition (i) of observable information holds.
- **Δ-stable.** σ_Δ(π_self) is whatever the perturbation channel does to the
  self-report; under any Δ that perturbs the *system* and not the describing system's
  own record, σ_Δ = 0 exactly. Condition (ii) holds, and holds maximally.
- **BC-unresponsive.** O(X_B) is the same set for every B, because π_self never reads
  X at all. So `span(ALL π_i) < ε` in the sense that matters — the BC parameter has no
  observable effect (`context_map_falsification_bc.md`: *F1_BC: BC_param_has_no_
  observable_effect → scope_rejection*).

The observable is therefore perfectly valid by the necessary condition and useless for
the purpose the necessary condition is a precondition *for*. One line, no subtlety.

**Why this has not shown up before in this repository.** In every physical case —
Kuramoto, Doppelpendel, Stuart-Landau, SIR, pitchfork — the observable is applied to
the system. There is no proprioception in Kuramoto; there is no π that could read the
observer. The gap between necessary and sufficient is invisible as long as observables
cannot be self-directed. It becomes visible the moment the describing system is *in*
the world it describes — which is the first structural difference between the
cognitive-architecture strand and the physics cases that has consequences for the ARW
apparatus rather than only for interpretation.

---

## 2. Where it became visible — and a correction to the first reading

> **Correction, same day.** The first version of this note claimed that the agent's
> descriptions are predominantly self-directed (11 of 20 slots) and that this is *why*
> substrate separation fails. Both halves needed correction. The share is strongly
> condition-dependent, and in the condition where the gate is actually measured the
> descriptions are predominantly *exteroceptive*. (This correction originally added "while
> separation fails just the same" — that ratio was itself defective, see the audit banner
> above; the correction does not need it and does not rest on it.)
> The causal story was wrong. What replaced it (§2.2) is better founded and sharper.
> C1 is untouched: it is a construction and does not depend on any of this.

### 2.1 The self-share is condition-dependent, and the causal claim does not survive

`Simulationen/labyrinth_scope_constructing/` selects four observables per mode out of a
pool of 109 compositions over 16 primitive channels, on intrinsic criteria only.
Counting the channels behind the surviving descriptions, strictly (`act_*` and
`time_left` only — `displaced` is an interaction variable and counted separately):

| Condition | slots | self-only share | separation median r *(defective — see audit)* |
|---|---|---|---|
| 120 ep, single substrate, ε-greedy, seed 42 | 52 | 0.58 | 1.031 |
| 120 ep, single substrate, ε-greedy, seed 1337 | 36 | 0.47 | 1.023 |
| 200 ep, single substrate, run-and-tumble | 28 | 0.32 | 0.922 |
| 200 ep, **four substrates mixed**, run-and-tumble | 40 | **0.20** | 1.013 |

Two things follow. First, the figure quoted in the first version (≈ 0.55–0.70, depending
on whether `displaced` is lumped in) was from the top row and was presented as a general
property; it is not. Second, and decisively: in the mixed condition — the only one in
which the separation ratio is even meaningful, since a single-substrate run cannot show
substrate separation — descriptions are **67 % exteroceptive**, i.e. the self-share is at
its *lowest* exactly where the original claim needed it highest. Self-description is
therefore not what distinguishes that condition. (The first version added "and separation
still fails at r ≈ 1.0"; that ratio was defective and the sentence does not need it.)

For calibration: purely self-reading channels are 5 of 16 in the pool, so uniform
selection would give a share of 0.31. Two of the four measured conditions sit below that
and two above. There is no clear bias in these numbers at all.

### 2.2 What the measurement actually shows

The right question is not which *channels* the descriptions rest on but whether the
selected *compositions* distinguish the substrates. Measured directly: take the 32
distinct compositions the surviving descriptions use, and evaluate each one under a fixed
random walker in all four substrates, so the environment and not the policy drives any
difference. Separability per composition as Cohen's d over substrate pairs:

- **14 of 32 have max |d| < 0.2** — negligible.
- median max |d| = **0.23** — small by convention.
- Every `DIFF` composition sits at |d| ≈ 0.00–0.06: a difference over a window is a
  symmetric random-walk artifact and carries no substrate information whatsoever, yet
  several were selected.
- The best separators reach |d| ≈ 0.99 (`RATE12`/`MEAN12` of radius-2 passability), so
  the pool *does* contain substrate-diagnostic compositions.
- **`cost_here` does not appear in the surviving descriptions at all** — and it is the
  most substrate-diagnostic channel in the environment by construction: uniform 0.4 in
  one substrate, uniform 0.3 in another, a 0.1–0.65 gradient in a third, and 0.05/1.0
  barriers in the fourth.

That last point is the whole finding, and it is not about proprioception.

### 2.3 The correct diagnosis: within-window criteria cannot see between-BC differences

`cost_here` is *constant* within a run in three of the four substrates. Its spread inside
any window is therefore near zero, and every selection criterion in the implementation —
spread relative to own range, peak spread, failure-association, contingency — computes a
**within-window** statistic and discards it. But the substrate information sits in the
channel's *level*, not in its variation: 0.4 versus 0.3 versus a gradient versus
barriers.

Generalized:

> A criterion computed from statistics *within* a context is structurally blind to
> differences *between* contexts, because a boundary-condition difference presents itself
> as a difference of levels across contexts the describing system never sees side by side.

This is why nothing helped. Heavy-tailed exploration, receptor adaptation, critical
periods, value replay and four different selection criteria were all tried against the
separation failure; every one of them is a within-window criterion, so all of them were
blind in the same way. The failure was not underpowered — it was the same failure
repeated five times.

## 3. Why stability-based selection *could* have this bias (C2, unsupported)

The description criterion of `scope_constructing_agent_architecture.md` §4 is
persistence: a mode exists as long as its description keeps holding under δ ∈ Δ. The
consolidation criterion of `sleep_as_perturbative_description_consolidation.md` §4 is
the same thing offline: σ_Δ(D) < ε.

Both are criteria on the description's *own* behaviour. Neither mentions what the
description is about. And the ranking they induce is, in general,

```
own operations  >  own resource state  >  interaction variables  >  environment
```

because each step to the right adds a source of variation the describing system does
not control. A criterion that rewards holding will therefore rank self-description
first, and it will do so more strongly the better the criterion works.

This is the sense in which persistence is necessary but not sufficient for a
description to be *about* something.

**Held as a conjecture only.** §2.1 measured the ranking and did not find it: the
self-only share sits at 0.20–0.58 against a chance level of 0.31, and the run in which
separation is measurable has the *lowest* share. The argument above says why such a bias
would arise if the ranking held; the data do not show it holding. Two ways to read that:
the ranking may be dominated by the predictability term (a wall is highly predictable
too, once you are next to it), or the effect may exist but be small next to C3. Not
resolved here.

---

## 4. The class: self-confirming selection criteria

Three instances are now on record, and they are the same failure in different
vocabularies:

| Instance | The criterion | What it selects for | Where recorded |
|---|---|---|---|
| Δ_replay admissibility | a description is kept if it persists under internally generated perturbations | an arbitrarily narrow Δ_replay makes *every* description persistent | Q-SLP-01 |
| habitual variability | an observable is recruited if it varies enough to be informative | channels that vary *often*, hence blindness to rarely-but-decisively informative ones | `switch_minimization_criterion.md` §9; simulation, 2026-07-26 |
| persistence / stability | a description is kept if it holds | the most stable thing available, which is the describing system itself | this note |

The general form: **a criterion evaluated on the description's own behaviour will
select descriptions of whatever the criterion finds easiest, and "easiest" is a
property of the describing system, not of the world.** Naming the class matters
because the fixes are not interchangeable — each instance needs an opposing condition
of its own, and in each case the opposing condition is what carries the empirical
content.

---

## 5. What this does *not* claim

- Not that observable information is wrong or should be weakened. It is a necessary
  condition and it does necessary work; the exclusion-zone reinterpretation in
  `observable_information.md` stands untouched.
- Not that persistence should be dropped as a mode criterion. Without it there is no
  mode identity at all.
- Not that the agent's separation failure is *explained* by C1. It is not — §2 measured
  that and the explanation is C3 instead. C1 remains a statement about what the necessary
  condition does and does not entail, demonstrated by construction and independent of
  whether any particular selection procedure falls into it.
- Not that the physical cases are affected. C1 requires a self-directed observable,
  and the physics cases have none. Whether an analogue exists there — an observable
  that reads the *measurement apparatus* rather than the system — is worth asking but
  is not claimed here.

---

## 6. The prescriptive move, and why it cannot be applied literally

The obvious repair is to promote BC-responsiveness from a falsification verdict to a
construction constraint: admit a description only if it discriminates between boundary
conditions. F1_BC already supplies the semantics; it is simply used as a judgement on
finished scopes rather than as a filter during their construction.

**But an agent cannot apply it.** BC-responsiveness is defined by comparing O(X_B)
across B, and an agent does not observe its own boundary conditions — it does not know
which substrate it is in, and in this experiment series it must not be told (that is
the anti-circularity commitment of the project brief). The constraint is computable by
the observer and not by the agent. Stating it as an agent-side rule would be a category
error of the same kind as putting the resolution threshold under the agent's own
control.

---

## 7. What an agent *can* compute

Two proxies, and after §2.2 they are not equally good.

### 7.1 A description must fail somewhere (necessary, not sufficient)

A description that holds everywhere carries no partition. If prediction never breaks, no
encounter boundary is ever drawn and the description is compatible with every situation
the agent will ever be in. So:

```
admit a description only if its failure rate is bounded away from zero
```

— a **lower** bound on the switch rate, alongside the upper bound parsimony supplies:

```
0  <  failure rate  <  parsimony bound
```

structurally the same two-sided form as `sup_x σ_Δ(x) < ε < ε*(O,X)`, and for the same
reason: the lower bound rules out blindness, the upper rules out noise, neither alone is
a criterion. Implemented as `--fail-floor` / `--cluster-floor`, off by default so its
effect stays attributable. Measured distribution of failure rates over evaluated
variants: 13 % sit below 0.01 — those are the never-failing descriptions the floor is
meant to exclude — with p25 = 0.07 and a median of 0.27.

This also patches a hole in C-PAR's own degeneracy analysis
(`switch_minimization_criterion.md` §3), which found three ways the agent could *cheat*
the switch count to zero and closed all three, but did not ask what happens when the
count reaches zero legitimately. Same destination, honest route.

**But it is not sufficient**, and §2.2 says why: the descriptions in the failing runs do
fail, at ordinary rates. A non-zero failure rate does not make a description
BC-responsive. The floor removes a degenerate corner; it does not create separation.

**Measured, 2026-07-27.** One run with the floor at 0.10 (200 episodes, four substrates
mixed, otherwise identical to the baseline): median r 1.029 against 1.013 without it
— both from the defective per-step measure, so the comparison says nothing about
separation — and the self-directed share *rose*, 0.20 → 0.40. The floor
also rejected every proposed variant in 335 cases, falling back to the unfiltered pool,
so it was largely inoperative and what remains may be stochastic. Read conservatively:
the floor did not help, it may have hurt, and the implementation needs a fallback that is
something better than "ignore the constraint" before the result is worth much. Either way
it is not the mechanism, which is what §7.2 was already expected to be.

### 7.2 Cross-encounter level comparison (the proxy C3 actually calls for)

If BC information sits in a channel's *level across contexts* rather than its variation
within one, then the agent-computable form of BC-responsiveness is a comparison *between*
stored encounters:

> A candidate observable is BC-informative to the extent that its level differs between
> stored encounters that could not be covered by one description.

Everything this needs is already in the protocol buffer. Each record holds a raw window
and the identity of the mode that was active; encounters marked *unresolved* are exactly
the ones no description covered. So the offline phase can compute, per candidate, a
between-encounter contrast — and it currently does not: `fit_and_score` evaluates every
window **independently**, which is precisely the within-context restriction C3 identifies.

This is a one-function change in the offline phase, and unlike §7.1 it addresses the
measured cause rather than a corner case. It is the concrete next step and it is
untested — noted here so the claim is not confused with a result.

**Open:** whether "could not be covered by one description" is the right pairing
criterion, or whether the contrast should be computed across *all* encounter pairs and
the pairing left to emerge. The first presupposes the mode structure the contrast is
supposed to help build.

## 8. Open question

Registered in [`open_questions.md`](open_questions.md).

| ID | Question | Level | Priority |
|---|---|---|---|
| Q_NEW_G | Observable information is necessary but does not entail BC-responsiveness (C1, demonstrated). What is the minimal *additional* condition that does — and is there a formulation computable by a system that cannot observe its own boundary conditions? Two candidates: a non-zero clustered failure rate (§7.1 — measured to be necessary but demonstrably not sufficient), and a cross-encounter level contrast (§7.2 — addresses the measured cause, untested). The open part is whether any *within-context* statistic can suffice at all, or whether BC-responsiveness is only ever computable by comparison across contexts. | ARW | high |

Level note: Q_NEW_G is ARW-level and stays in the Q_NEW_* series with the other
ARW-level questions (Q_NEW_E, Q_NEW_F). The ART-level consequences live with the agent
documents as Q-PAR-* and Q-SCA-*.

---

## 9. Relationship to existing documents

| Document | Relationship |
|---|---|
| `docs/core/observable_information.md` | C1 qualifies it: the condition is necessary and does not exclude BC-unresponsiveness. A cross-reference has been added there. No change to the definition. |
| `context_map_falsification_bc.md` / F1_BC | supplies the semantics of BC-unresponsiveness. §6 proposes promoting it from verdict to construction constraint; §6 also explains why an agent cannot apply it directly. |
| `switch_minimization_criterion.md` | C-PAR is an upper bound on the failure rate. §7 supplies the missing lower bound; without it C-PAR pushes toward exactly the descriptions C1 identifies. |
| `sleep_as_perturbative_description_consolidation.md` | its σ_Δ(D) < ε criterion is the offline form of the biased criterion; Q-SLP-01 is the first instance of the class in §4. |
| `scope_constructing_agent_architecture.md` | §4's mode definition (stability under δ ∈ Δ) is underdetermined in the sense of §3 here. This is a gap in the architecture, not in its implementation. |
| `scope_component_conflict_typology.md` | X_stab(π) is the observable-level stability domain; the question of whether a *stable* description is also a *contentful* one is the same distinction one level down. |
| `kht_reconciliation_scope_constructing.md` | records the channel counts that made this visible. Its separation figures are subject to the same audit. |

---

## Maintenance History

- **2026-07-27 (II)**: Substantially corrected within hours of creation. The measured
  instance in §2 did not survive a proper measurement: the self-directed share is
  condition-dependent (0.20–0.58 across four conditions, chance level 0.31), and in the
  mixed-substrate condition — the only one where the separation ratio means anything —
  descriptions are 67 % exteroceptive — the self-share is lowest exactly where the claim
  needed it highest. (The separation figures cited alongside were themselves defective;
  see the 2026-07-27 (III) entry.) C2 downgraded
  from proposed mechanism to unsupported conjecture. C3 added and measured: every
  selection criterion in the implementation computes a *within-window* statistic, while a
  BC difference presents as a difference of *levels across* contexts — median substrate
  separability |d| = 0.23 over the selected compositions, 14 of 32 negligible, all `DIFF`
  compositions at |d| ≈ 0, and `cost_here`, the most substrate-diagnostic channel in the
  environment, absent from every surviving description *because it is constant within each
  substrate*. §7 split accordingly: the failure-rate floor is necessary but not
  sufficient, and the cross-encounter level contrast is the proxy the measurement actually
  calls for. C1 untouched throughout.
- **2026-07-27 (III)**: Measurement audit. Three per-step quantities for the separation
  ratio found defective in sequence — circular, saturated, wrong grain. The third invited
  the reading that the agent does not navigate; checked against a random walker and
  reversed: it navigates ~10× better than chance. At episode grain the ratio ranges
  0.73–1.86 over three seeds (1 pass, 2 fails, 2–5 modes in the matrix) — real but
  underpowered. Audit banner added; every separation figure in this document is now marked
  as not load-bearing. C1, the §2.2 composition-separability measurement and the §2.1
  channel counts are independent of the ratio and untouched.
- **2026-07-27**: Created after the substrate-separation gate of the scope-constructing
  agent failed at r ≈ 1.0 with 11 of 20 description slots held by BC-unresponsive
  channels, and the failure survived every mechanism tried against it. Filed as `claim`
  rather than promoted into `docs/core/` or `docs/advanced/`: C1 is demonstrated by
  construction and could be promoted, but C2 and the §7 proposal rest on one agent case,
  and the clustering question in Q_NEW_G is unresolved. Promotion should wait for either
  a formalization of the lower bound or a second instance outside the agent setting.
