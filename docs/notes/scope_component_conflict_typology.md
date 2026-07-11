---
status: note
layer: docs/notes/
depends_on:
  - docs/glossary/scope.md
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
| **Δ-conflict** | Admissible perturbations | Parties demonstrably refer to the same object at the same resolution but disagree on the window of variation that counts as absorbable vs. regime-violating. | Survives disambiguation completely. This is the genuinely normative dispute. |
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

See `docs/notes/open_questions.md` for the canonical entries.

## Non-goals

This note does not claim that economic schools *are* distinguished by single
tuple components; it records the question. No case, no metrics, no transfer
claims are made here.
