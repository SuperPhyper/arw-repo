---
status: note
layer: docs/notes/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md            # σ_Δ, pointwise stability (used in §8.1)
  - docs/advanced/epsilon_and_scope_resolution.md   # ε, I_ε, ε-plateau (used in §8.1)
---

# Scope-Component Typology of Scientific Controversies

> **Status note.** Exploratory. Originated in a Kaffeehaus session (2026-07-04) on
> economic-school disagreement. Nothing here is settled; the note exists to keep
> several threads traceable. Candidate for promotion to `hypothesis` once the
> typology survives one worked controversy analysis.

## 1. Core conjecture (ARW level, domain-neutral)

Scientific and normative controversies can be classified by **which component of
the scope tuple S = (B, Π, Δ, ε) the disputing parties vary** while sharing the
others. The conjecture: the varied component predicts the *phenomenology* of the
dispute (how it feels, whether it is resolvable, and by what means).

| Conflict type | Varied component | Dispute structure | Resolution behavior |
|---|---|---|---|
| **ε-conflict** | Resolution threshold | Parties use the same nominal observable at different resolutions / aggregation levels and thereby refer to structurally different objects. The dispute is an **equivocation**, not a disagreement. | Dissolves under disambiguation: once both parties see they describe different aggregation groups, the apparent contradiction disappears or converts into an honest scale-transfer problem. |
| **Δ-conflict** | Admissible perturbations | Parties demonstrably refer to the same object at the same resolution but disagree on the window of variation that counts as absorbable vs. regime-violating. | Survives disambiguation completely. This is the genuinely normative dispute. *(Caveat 2026-07-26: this row is suspected of absorbing a second, non-normative conflict type — see §8.1, Q_NEW_F.)* |
| **Π-conflict** | Admissible descriptions / projections (observables) | "You are measuring the wrong thing." Dispute over relevance of observables, not over their values. | Not resolvable by measurement; requires argument about projective richness of competing Π choices. |
| **B-conflict** | Boundary constraints (selection of X_B ⊆ X) | "We are talking about different systems." Parties select different state subsets as structurally relevant. | Deepest and empirically least decidable type. |

**Key asymmetry:** only the ε-conflict produces *fallacies* in the logical sense
(equivocation). The other three types are legitimate disagreements. A diagnostic
that filters ε-components out of a controversy does not settle the dispute — it
exposes what the dispute is actually about.

## 2. The ε-conflict mechanism in more detail

Claim to be examined: an observable that is used and compared across different
scales results in fallacious inference, because the parties are structurally
talking about **different aggregation groups** under the same name. The
observable label is shared; the object it projects from is not.

Candidate everyday instances (untested, illustrative only):

- Paradox of thrift: individually rational saving vs. aggregate contraction —
  same nominal observable ("saving"), different aggregation level.
- "The economy is doing well / my situation is worse": GDP-level aggregate vs.
  household-level observable under the same label ("economic condition").

**Open formal question — status: partially resolved (2026-07-04 continuation).**
Original question: whether "aggregation level" maps cleanly onto ε (resolution
threshold, d_Π(x,y) ≤ ε → indistinguishable) or whether it partially implicates
Π (a different projection altogether) or B (a different state selection), i.e.
whether scale-equivocation is a *compound* conflict rather than a pure ε-conflict.

A worked case (capital growth vs. productivity, see §6) suggests the answer is
case-dependent along a specific pattern rather than a single fixed decomposition:

- If rising aggregation only changes *resolution* on a fixed projection, the
  conflict is pure ε.
- If rising aggregation admits *new codetermining variables into the projection
  itself* (the observable is now computed from a different variable set), the
  conflict is Π, not ε — resolution language was overloaded to describe a
  projection change.
- If rising aggregation exposes a *different generator entirely* producing the
  same observable label, with no shared causal link to the low-aggregation
  generator, the conflict is B, not Π or ε.

Working conclusion: "scale-equivocation" is not a single row of the typology.
It is a family of conflicts that *look* like ε-conflicts from the outside
(same label, different scale) but must be individually diagnosed against Π and
B before being filed as ε. Pure ε-conflicts (same projection, same generator,
only resolution differs) may be the narrow case, not the default. This still
needs a second independent worked case before the typology row for ε can be
considered well-defined — one confirmed case is not sufficient.

## 3. Predicted diagnostic signature (falsifiable direction)

If the typology holds, the following should be observable in real controversies:

1. Parties in an ε-conflict change their stated disagreement (or drop it) once
   aggregation groups are made explicit; parties in a Δ-conflict do not.
2. The hardest disagreements between schools sharing many observables should
   concentrate where the same observable carries different admissible-perturbation
   windows (Δ), not where observables differ (Π).
3. Controversies classified as B-conflicts should show resistance to *any*
   empirical adjudication, since no shared X_B exists to measure within.

Prediction 2 is the sharpest and most testable of the three.

## 4. Instance sketch: economic schools (ART-flavored, illustrative)

Not a case; no pipeline artifacts. Recorded only to preserve the originating
material. Hypothesis: economic schools may differ systematically in *which*
tuple component they primarily vary —

- structural/Marxian analysis: primarily B (which states count as structurally
  relevant: e.g. reproduction of labor power inside X_B);
- monetarist/investment analysis: primarily Δ (which dynamics count as normal
  fluctuation vs. regime-relevant);
- institutional analysis: primarily Π (which observables are decisive);
- with ε shifting as a *consequence* of these choices rather than as the
  primary carrier of difference.

Shared observables such as profit rate, wage share, inflation, unemployment
would then carry different admissible windows (Δ) or different aggregation
referents (ε) across schools. Original conjecture from the session: "capitalist
disputes are Δ-conflicts over shared observables," with ε-conflicts contributing
a separable equivocation component.

Possible connection (not yet worked out): the diagnostic coupling indicator
Q = K/G from the ARW economic-regime hypothesis presupposes a fixed aggregation
level; an ε-conflict analysis may be a precondition for comparing Q across
schools at all.

## 5. Relation to existing ARW work

- **Conflict-navigation model** (`conflict_navigation_nested_calibration.md`):
  the upper calibration loop (scope calibration) is where Δ- and B-conflicts
  live; the typology refines what "constructing the shared question" means —
  it means identifying the varied tuple component. ε-conflicts are the special
  case where constructing the shared question fully dissolves the dispute.
- **Scope tuple semantics** (`docs/glossary/scope.md`): the typology is a direct
  consumer of the canonical component definitions and adds no new primitives.
- **Terminological discipline:** the originating discussion initially framed
  Δ-conflicts as "ε-conflicts." The corrected assignment (admissible-window
  disputes → Δ; resolution/aggregation disputes → ε) follows the canonical
  table and parallels the τ vs. ε separation established for H2'.

## 6. Worked case: capital growth vs. productivity across aggregation (added 2026-07-04)

At low aggregation, productivity and capital growth coincide observationally —
more produce, more capital, no independent role for wages or financing terms.
This is **coincidental alignment**, not a shared generator: on this scale, Π is
effectively near one-dimensional (production quantity → capital), so ε-level
resolution differences look like the whole story.

At higher aggregation (company-spanning gross/net description), the projection
itself expands: wages, currency rates, and legislation enter as codetermining
variables that factor into "growth" but do not factor into micro-level
productivity at all. This is a **Π-conflict**, not an ε-conflict — the label
"growth" is computed from a different variable set, not merely viewed at a
coarser grain of the same map. Aggregated metrics carry no meaning at the micro
level, and micro-level productivity gains do not by themselves explain
aggregate capital growth once these other variables are active.

A sharper case still: capital growth on the stock/valuation scale can occur
with **no productivity increase at all** — investor trust in increased future
capability is sufficient to grow capital with no causal link to current
production. Here the generator is not an expanded version of the productivity
generator; it is a **different generator** (expectation dynamics) that happens
to output the same observable label. Candidate **B-conflict**: not the same
system described more coarsely, but a different part of the state space
producing an observable that shares a name with the low-aggregation one.

**Diagnostic implication.** The three regimes above (coincidental low-aggregation
alignment / Π-expansion at mid-aggregation / generator swap at the
valuation scale) cannot be told apart by inspecting the observable "growth"
itself — a scalar output is many-to-one over its generators. Distinguishing
them requires looking at what is invariant across the shift, i.e. an
operator-signature-level (Σ) analysis rather than a partition-level metric
comparison. This is the same diagnostic move underwriting WP-A5 and the
expected negative resolution of Q-REL-05 (partition-level metrics cannot in
principle recover which generator produced them). Candidate invariant to test
first: productive capability (capacity independent of realized output) as a
Σ-component that should behave differently across the three regimes above.

## 7. Π-monopolization: a fifth, orthogonal conflict mode (added 2026-07-04)

The four conflict types in §1 all share an assumption: both parties treat the
other's scope as a legitimate description, and dispute its accuracy, relevance,
or boundary. There is a distinct pattern that does not vary a tuple component
at all, but instead **denies the legitimacy of the competing Π itself**, usually
via moral rather than epistemic disqualification.

**Π-monopolization**: a party does not defend its chosen projection against a
competing one on grounds of projective richness (which would make it an
ordinary Π-conflict, §1) — it instead treats the competing projection as
illegitimate prior to any such argument, typically by recasting it as
complicity, evasion, or bad faith rather than as an alternative description
with its own (possibly narrower) usage range.

**Diagnostic distinction from an ordinary Π-conflict:**

| | Π-conflict | Π-monopolization |
|---|---|---|
| Competing description | Stands as a description; disputed on relevance/richness | Stripped of description-status itself ("that's not an explanation, that's an excuse") |
| Resolution path | Argument about which Π explains more | Not resolvable by argument — the other party is not conceded a position to argue from |
| What can be checked | Projective richness, predictive reach | Whether the disqualification is epistemic (this Π explains less) or moral (this Π excuses/is complicit) |

**Reconciliation rule (the antidote to monopolization):** a non-monopolizing
treatment names, for each competing Π, its B (which slice of states/cases it is
drawn from), its usage range (what it is good for), and its limitation (what it
structurally cannot do) — instead of replacing one Π with the other. Two
distinct failure modes should be told apart rather than conflated:

1. **Omission**: a relevant Π is simply not mentioned, though clearly germane
   (e.g. a structural/aggregate account left out where it bears directly on the
   case). This is a completeness objection, not a monopolization charge, and is
   often the legitimate core of a monopolization complaint.
2. **Monopolization proper**: a competing Π is mentioned only to be
   delegitimized, rather than acknowledged as limited-but-valid within its own
   usage range.

**Illustrative instance (not a case; no pipeline artifacts).** Media coverage of
a violent incident: an individual-case Π (immediate legal/procedural trigger)
and a structural Π (documented population-level pattern) are both applicable to
the same event. Coverage that omits the structural Π entirely commits omission
(1); framing invoking the structural Π to declare the individual-case Π an
"excuse" or complicity commits monopolization (2). A reconciled formulation
states both: the immediate trigger per the individual-case account, and the
event's place within the documented structural pattern — without either
description doing duty for the other. Note that naming both Π's does not by
itself license a causal claim connecting them; see
`docs/notes/cross_scope_causal_construction.md` for why that additional step
(the bridge claim) needs independent support.

---

## 8. Shared terms, different linkage: a candidate the typology cannot place (added 2026-07-25)

The five modes above sort a controversy by *which* tuple component the parties
vary (§1) or by refusal to grant the other a component at all (§7). A case
brought in from the Resonanzdialektik working thesis
(see `docs/art_instantiations/kht_resonance_dialectic.md` §6.3) fits neither,
and is recorded here because it bears directly on Q_NEW_C.

Two parties use the same terms, drawn from the same population of cases, at the
same resolution, each granting the other's description the status of a
description. Same B, same Π, same ε, and no monopolization. They nevertheless
hold different positions, and the difference is reconstructible: the terms are
*linked* differently. The thesis's example:

```
supply security → base load    → nuclear      → diversity
supply security → grid stability → storage    → renewables
```

The nodes are shared. What differs is which term is treated as constraining
which — the relational structure over Π, not its membership.

**Why this is a gap rather than a fifth-and-a-half mode.** The scope tuple has
no slot for relational structure among observables. Π is a *set* of admissible
projections; nothing in S = (B, Π, Δ, ε) records how they constrain one another.
A disagreement located entirely in that structure is therefore invisible to a
tuple-component typology by construction — which is a stronger statement than
"the typology is incomplete," and a checkable one.

**Two candidate homes, both speculative:**

1. **Generator level.** Σ (operator signatures S1–S5) is where structure over a
   scope family lives rather than within a scope. If linkage differences are
   signature differences, the parties instantiate different generators over a
   shared Π, and the existing generator-admissibility machinery applies without
   extension. This is the conservative reading.
2. **Transition graph.** The general regime construction that Q_NEW_25 declares
   missing carries a graph whose edges record *how* regimes meet. Linkage
   differences might be differences in that attributed structure. This reading
   is blocked until Q_NEW_25 is discharged, and is noted so the dependency is on
   record rather than rediscovered later.

Registered as **Q_NEW_E**. Note what it does *not* claim: that the linkage
difference is irreducible. If every such case turns out to be a B-conflict in
disguise — the parties silently drawing on different case populations, with the
linkage difference a symptom — the typology stands unamended and Q_NEW_E closes
negatively. That is the outcome to try for first, because it is the cheap one.

### 8.1 Revision (2026-07-26): the linkage is an induced stability profile

§8 left the *content* of a linkage edge undetermined — "which term is treated as
constraining which" admits a semantic reading (π_j is part of what π_i means), an
inferential one, and a stability one. The three are not equivalent, and only the
third stays inside existing ARW machinery. This revision commits to it, on the
grounds given below, and states the resulting claim more strongly than §8 does.

**Where the differing assumptions actually enter.** The relevant quantity is the
perturbation spread σ_Δ(x) = sup_{δ∈Δ} |O(x+δ) − O(x)|
(`docs/glossary/perturbation_spread.md`; Felder 2026 Def 4). It *looks* tuple-
internal: given Π, Δ and a state, it appears determined. That holds only when O is
a pure state function. The observables this repository actually works with — r_ss,
var_rel, lambda_proxy — are steady-state or asymptotic quantities: O is defined
through the dynamics, not merely on the state space. **σ_Δ therefore requires the
tuple *plus* a generator.**

The consequence is the mechanism §8 was missing. Two parties holding B, Π, Δ and ε
fixed, and differing only in what they assume about the dynamics, obtain different
σ_Δ-profiles over X_B — hence different verdicts about which projections carry a
robust ε-plateau — without either party miscomputing anything, and without either
being refuted at the time of the dispute. A world-model, on this reading, is not a
structure over Π at all: it is a **generator hypothesis**, and the linkage structure
of §8 is its observable shadow.

This selects candidate home 1 (Σ) over candidate home 2, but on a different argument
than §8 gives. §8 offered the conditional "*if* linkage differences are signature
differences". The claim here is stronger and does not route through S1–S5: linkage
differences are *generator* differences, which manifest as stability differences,
and operator signatures are one — not the only — vocabulary for describing them.
The dependency on Q_NEW_25 recorded in §8 is not needed for this reading.

**A construction that makes the graph computable.** For a scope S and a generator G,
define for each π ∈ Π its stability domain

```
X_stab(π) = { x ∈ X_B : σ_Δ^π(x) < ε },   σ_Δ^π(x) = sup_{δ∈Δ} |π(x+δ) − π(x)|
```

(σ_Δ^π is the canonical σ_Δ of `docs/glossary/perturbation_spread.md` with the observable
it is taken over written explicitly, since the construction ranges over Π. X_stab(π) is
the pointwise-stable set of that document, indexed by observable.)

and take the linkage graph over Π to have edges weighted by the overlap of
X_stab(π_i) and X_stab(π_j) — the observables that stand or fall together under Δ.
Two generators over one tuple yield two graphs with identical vertex sets and
different edge structure, which is exactly the "same nodes, different topology"
formulation of §8, now as a derived rather than postulated object. Nothing new is
required to measure it: ε-plateaus per observable are already a pipeline output, and
the caveat of `docs/glossary/perturbation_spread.md` §4 applies unchanged — near θ* the
mask must come from direct σ_Δ or the local-max Lipschitz bound, not the pointwise
gradient proxy (C1/C2, 2026-06-02), or the edges will be spuriously present.

**The sharper claim: misclassification, not absence.** §8 says the typology "cannot
place" such a case. On the stability reading it *does* place it — wrongly, and
systematically, in the **Δ-conflict** row. Both conflict types issue the same verdict
("this perturbation is absorbable / regime-violating"); the Δ-conflict produces it by
stipulating the input, the generator conflict by hypothesising the map. The
phenomenology is identical, so the diagnostic cannot separate them, and the Δ-row's
resolution column — *"survives disambiguation completely. This is the genuinely
normative dispute"* — is then wrong about the case. A generator conflict is not
normative. It is **underdetermined**: decidable by evidence, but only after the
perturbation in question has occurred.

That yields a discriminator the typology can carry:

> Does the party's position commit it to a prediction that an observed perturbation
> could contradict? Yes → generator conflict (underdetermined, later decidable).
> No → Δ-conflict (normative, not evidence-decidable).

Registered as **Q_NEW_F**, separately from Q_NEW_E because it is a claim about an
existing table row rather than about the completeness of the table.

**Revised cheap negative outcome.** §8 names "B-conflict in disguise" as the first
thing to try for. Under this revision the more likely — and more damaging — negative
is **Δ-conflict in disguise**: if the discriminator above cannot be applied because
parties adjust their predictions after the fact, then generator conflicts are not
merely hard to distinguish from Δ-conflicts, they are *operationally* Δ-conflicts,
and both Q_NEW_E and Q_NEW_F close negatively together. This is the weakest joint in
the revision and is recorded as such: the discriminator is only sharp where the
prediction is fixed ex ante, which in live controversy it rarely is.

**Downstream (added 2026-07-26, same day).**
`docs/notes/communicative_branching_points_nuclear_discourse.md` §5 consumes this
section: it reads a *communicative branching point* as the place where two generator
hypotheses over a shared tuple begin to produce different σ_Δ-profiles, and asks
whether such a point can be located in live discourse without either party
articulating its generator (Q-COM-02 there). The ex-ante limitation recorded above
applies to that question in full and is the reason it is not already answered.

**Adjacent, and worth not losing.** Two further notes imported the same day make
σ_Δ-variation claims from different sources:
`docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md` §3
has the *environment* fixing part of Δ, thereby lowering σ_Δ for the observables an
active scope runs on; `docs/context_navigation/sleep_as_perturbative_description_consolidation.md`
§4 has σ_Δ measured offline under replay perturbation. Neither conflicts with the
reading here — but taken together the three identify at least three independent
sources of σ_Δ variation outside Π: the admitted perturbation set (Δ, the classical
route), the environment that suppresses perturbations, and the generator through
which an asymptotic observable is defined. Only the third is invisible to the tuple.
That is a distinction the Δ-conflict row will need if Q_NEW_F is pursued, and it is
recorded here rather than in a new document.

**Status of this revision.** Argued, not tested. No case has been run with two
generator variants over a shared tuple; until one has, the co-stability graph is a
construction proposal, not a result.

---

**Note on reconstruction:** this file was rebuilt from session context on
2026-07-04 (mobile session, no direct repo access). §1–§5 reproduce the
originally drafted note; §6 is new. An earlier reconstruction of this same
note (lacking §6 and §7) was also produced in the same window and discarded
in favor of this, more complete, version when both were reconciled on import
(2026-07-11) — see `docs/meta/DOC_INDEX.md` for the registration entry.

## Open Questions Registered (2026-07-11 import)

- **Q_NEW_A** — Does "aggregation level" map onto ε alone, or is
  scale-equivocation a compound (ε + Π) conflict? (Prerequisite for §1 row 1.)
- **Q_NEW_B** — Can prediction 2 (§3) be operationalized on a documented
  controversy with published positions from ≥2 schools sharing ≥2 observables?
- **Q_NEW_C** — Is the four-type classification exhaustive, or do mixed
  conflicts dominate empirically (making the typology a decomposition basis
  rather than a partition of controversies)?
- **Q_NEW_D** — Does the typology transfer outside economics (it is stated at
  ARW level), e.g. to a natural-science priority dispute?
- **Q_NEW_E** (added 2026-07-25, see §8; revised 2026-07-26, see §8.1) — Can a
  disagreement located in the *linkage* over a shared Π, with B, Π, Δ and ε all held
  fixed, be placed by any tuple-component typology? §8.1 sharpens the candidate
  answer: the linkage is the co-stability profile induced by a generator hypothesis,
  which lives at the generator level (Σ) and is computable as a graph over Π weighted
  by overlap of the stability domains X_stab(π) = {x ∈ X_B : σ_Δ^π(x) < ε}. Open
  part: whether two generator variants over one tuple actually produce distinguishable
  graphs on a worked case. Bears on Q_NEW_C: if irreducible, the typology is not a
  partition of controversies but a projection of them.
- **Q_NEW_F** (added 2026-07-26, see §8.1) — Does the Δ-conflict row of §1 conflate
  two types: a normative disagreement over which perturbations count, and an
  underdetermined disagreement over the generator that maps them? Both issue the same
  verdict, so the phenomenology does not separate them; the proposed discriminator is
  whether the position commits to a prediction a later perturbation could contradict.
  Closes negatively together with Q_NEW_E if parties routinely adjust predictions
  post hoc, since the two types would then be operationally identical.

See `docs/notes/open_questions.md` for the canonical entries.

## Non-goals

This note does not claim that economic schools *are* distinguished by single
tuple components; it records the question. No case, no metrics, no transfer
claims are made here.
