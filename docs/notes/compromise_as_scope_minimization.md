---
status: note
layer: docs/notes/
created: 2026-09-16
depends_on:
  - docs/glossary/scope.md
  - docs/notes/scope_relative_class_dimensionality.md
  - docs/notes/general_regime_construction.md
  - docs/notes/conflict_navigation_nested_calibration.md
  - docs/notes/minds_generalization_beyond_facilitation.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
related:
  - docs/notes/facilitation_toolkit_tuning_or_framing.md
  - docs/notes/facilitation_crystallize_the_friction.md
  - docs/notes/scope_component_conflict_typology.md
  - docs/context_navigation/switch_minimization_criterion.md
  - docs/art_instantiations/kht_group_dynamics.md
  - docs/art_instantiations/kht_resonance_dialectic.md
---

# Compromise as Scope Minimisation

**Level separation.** This file contains statements at two levels and keeps them
apart by construction:

- **Part I (ARW)** — domain-neutral. Minimal sufficient joint scopes, the
  minimisation problem, its failure modes.
- **Part II (ART)** — instantiations in social, organisational and facilitation
  domains. Part II is a candidate for promotion to `docs/art_instantiations/` once
  Part I stabilises; it is kept here to avoid a third orphan document.

**No statement in Part II legislates for the ARW level.** Where Part II needs a
formal claim, it cites Part I.

Notation follows `scope_relative_class_dimensionality.md`. Two symbol clashes from
the earlier draft are repaired here: acceptance regions are written $A_i$ (not $C_i$,
which is a descriptive class), and the reducible-complexity quantity is written
$d_{\mathrm{red}}$ (not $\Delta d_C$ — $\Delta$ is the admissible perturbation family
and is not available as a difference operator).

---

# Part I — ARW level

## I.1 Setting

Actors are indexed $i$. Each declares a scope $S_i = (B, \Pi_i, \Delta_i,
\varepsilon_i)$ and, under it, an **acceptance region** $A_i$: the set of outcomes it
classifies as acceptable.

The conventional picture — two positions on a common axis, compromise at the midpoint —
presupposes (1) a common metric axis, (2) comparable evaluation of displacement on it,
(3) approximately symmetric acceptance structure. When any fails, the midpoint is not
distinguished. If $A_1 = \{x < 7\}$ and $A_2 = \{x > 3\}$, nothing in
$A_1 \cap A_2 = \{3 < x < 7\}$ privileges $x = 5$.

The proposal is to replace distance minimisation with scope minimisation:

$$
\textbf{Find the least joint scope that still preserves the distinctions each acceptance classification requires.}
$$

## I.2 Necessary versus expressed distinctions

For actor $i$, distinguish the expressed set $\Pi_i$ from a subset
$\Pi_i^{\mathrm{req}} \subseteq \Pi_i$ required for its acceptance classification.
A distinction $\pi \in \Pi_i$ is **necessary** if removing it moves an outcome across
the boundary of $A_i$, or destroys a distinction required to locate that boundary.

$$
\text{expressed demand} \neq \text{necessary distinction}.
$$

Necessity is a property of the classification, not of whether a participant voiced the
criterion.

## I.3 What is minimised — and over what order

The earlier draft used three quantities interchangeably: $\operatorname{cdim}(S_J)$,
$K(\Pi_J)$, and $|\Pi|$. They are different objects and are separated here.

- $|\Pi_J|$ — **observation load**: how many distinctions the joint description must
  actually make. This is the object of the constraint problem.
- $\operatorname{cdim}(S_J)$ — **class dimensionality** of the class structure induced
  or declared under $S_J$. This is *reported*, not optimised.

The map $\Pi_J \mapsto \mathcal{C}_{S_J}$ must be declared; $\operatorname{cdim}$ is
defined on $\mathcal{C}$, never on $\Pi$ directly
(`scope_relative_class_dimensionality.md` §2–3).

**Minimal, not minimum.** A joint scope $S_J^\ast$ is **irreducible** if for every
$\pi \in \Pi_J^\ast$, removing $\pi$ causes either loss of a required distinction or
loss of required stability. Irreducibility is $\subseteq$-minimality. It is *not*
least cardinality.

$$
\text{irreducible (}\subseteq\text{-minimal)} \neq \text{minimum-cardinality}.
$$

Generically the irreducible joint scopes form an **antichain**: several mutually
incomparable solutions, of possibly different cardinality, all irreducible. Writing
$\arg\min \operatorname{cdim}$ hides this. Two consequences:

1. The formalism does not select among irreducible joint scopes. That selection is
   itself a decision, and it is not determined by the acceptance constraints.
2. Reporting a single minimal scope as *the* minimal scope is a category error. The
   admissible output is the set of irreducible joint scopes, or an explicitly declared
   selection rule on top of it.

This follows directly from `scope_relative_class_dimensionality.md` §9: refinement is
a partial order and $\operatorname{cdim}$ is a scalar summary; optimising the summary
linearises an order that is only partial.

## I.4 Commensurability is a precondition, not an assumption

$A_i$ is stated under $S_i$. The joint problem asks whether $A_i$ survives in $S_J$.
That presupposes the actors' descriptive spaces are commensurable — which is exactly
the transfer question, not a side condition.

Concretely, before $\Pi_J \subseteq \bigcup_i \Pi_i$ is even well-formed:

- a **translation** between the $\Pi_i$ must be declared (which $\pi \in \Pi_A$
  corresponds to which $\pi' \in \Pi_B$, and with what loss);
- a **normalisation** across actors must be declared — the analogue of
  `cross_observable.normalisation`, and subject to the same requirement that a scalar
  $\varepsilon$ across differently-scaled distinctions is ill-formed;
- a **composition rule** must be named: Rule A (joint graph) or Rule B (common
  refinement), with a stated reason if Rule B.

Without these, $\min |\Pi_J|$ is not ill-posed in a fixable way — it is undefined.
Transfer admissibility ($\Phi$) is the relevant machinery, with its standing caveat:
$\Phi$ is not evidence of class distance (Q-REL-05 open).

## I.5 The constrained problem

$$
\Pi_J^\ast \in \operatorname{Irr}\big(\Pi_J \subseteq \textstyle\bigcup_i \Pi_i\big)
$$

subject to, for all actors $i$ and all $\delta \in \Delta_J$,

$$
d\big(S_J, \delta\big) \in A_i,
$$

where $d(S_J, \delta)$ is the decision admitted under $S_J$ after perturbation $\delta$.
Note the type: the constraint is on the **decision**, not on the description — an
earlier formulation wrote $D(\Pi_J) \in A_i$, which mismatches a description with an
outcome region.

**$\Delta_J$ is declared as a family.** $\Delta_{\min} \subseteq \cdots \subseteq
\Delta_{\max}$, with acceptance required across the family, not at a single declared
$\Delta$. This matters here more than in simulation: no participant's stated
perturbation set is authoritative, and $\Delta$ is undeclarable from metadata in
principle.

**Bias direction.** Under-declaring $\Delta_J$ shrinks the perturbation spread and
therefore yields *more* stability verdicts — the procedure is **anti-conservative**
under $\Delta$ under-declaration. Since class-label preservation rather than a metric
spread is the operative criterion here, the indicator is $\chi$, not $\sigma_\Delta$
(`scope_relative_class_dimensionality.md` §12).

## I.6 Failure modes

Three, structurally distinct, requiring different interventions.

| Mode | Condition | Reading |
|---|---|---|
| Under-compression | $\Pi_J \supsetneq$ any irreducible $\Pi_J^\ast$ | Too many distinctions treated as mandatory; the admissible solution set shrinks or empties. $\bigcap_i A_i = \varnothing$ does **not** establish incompatible interests — it may only report unnecessary constraints. |
| Over-compression | a necessary $\pi$ has been removed | Agreement exists because a live distinction is no longer representable. Under perturbation the suppressed distinction reappears. |
| Instability | acceptance holds at $\Delta_{\min}$, fails within the declared family | The scope is sufficient only under current conditions. |

**Over-compression is the anti-conservative bias of §I.5 in its social form.** A false
consensus and an under-declared $\Delta$ are not two problems; the second is the
mechanism of the first. Widening $\Delta_J$ is therefore the diagnostic move for
suspected false consensus — not further questioning of positions.

$$
\text{consensus at insufficient resolution} \neq \text{stable compromise}.
$$

## I.7 A candidate quantity

$$
d_{\mathrm{red}} = |\Pi_{\mathrm{conflict}}| - |\Pi_J^\ast|
$$

measures descriptive structure removable without destroying necessary acceptance
distinctions. Given §I.3 it is defined only relative to a *chosen* irreducible
$\Pi_J^\ast$, hence is a set-valued quantity in general (a range over the antichain).

**Status: candidate.** $d_{\mathrm{red}}$ is not a measure of conflict severity, and no
case or study supports an interpretation beyond scope-reducible descriptive
complexity.

## I.8 What the formalism does not deliver

The construction yields **admissibility**, not fairness. It can state that a solution
preserves every actor's necessary distinctions under a declared $\Delta$. It cannot
state that the distribution of concessions is just. The observation that

$$
\text{fair compromise} \not\Rightarrow \text{equal numerical concession}
$$

is a claim about the inadequacy of the midpoint model, not a fairness criterion
supplied by ARW. Any normative reading is imported from outside and must be declared as
such — particularly where the formalism licenses *dropping* a distinction an actor
raised.

---

# Part II — ART level (instantiations)

**Level note.** Actors here are modelled describing systems: legitimate ART-level
objects of study. Nothing in this part asserts an ARW principle.

## II.1 Non-metric social scopes

A social scope may declare classes such as
$\{\text{role}, \text{position}, \text{action}, \text{group}, \text{decision}\}$ and
relational classes such as
$\{\text{cooperates with}, \text{opposes}, \text{trusts}, \text{depends on},
\text{mediates between}\}$.

A resolution rule may state: *differences in wording are not distinguished as long as
the attributed position is unchanged.* No numerical distance between statements is
required — this is the non-numeric $\preceq_E$ of
`scope_relative_class_dimensionality.md` §7.

A perturbation family may contain $\{\text{minor disagreement}, \text{time pressure},
\text{role change}, \text{resource conflict}\}$. The operative question is not whether
"trust" can be assigned a number, but whether a relational classification survives the
declared perturbations: $P_1 \, R_{\mathrm{coop}} \, P_2$ may persist under ordinary
disagreement and fail under resource conflict.

## II.2 Group formation as compression

Stable relational patterns may permit
$\{P_1, P_2, P_3\} \mapsto G_A$, $\{P_4, \ldots, P_7\} \mapsto G_B$, with a relation
$G_A \, R_{\mathrm{conflict}} \, G_B$ at the higher level. If that relation persists
under turnover of individual interactions, it belongs to the higher-level description.

This is the reification case of `scope_relative_class_dimensionality.md` §6: at the
level that reifies it, the stability of the lower-level pattern *is* a class.

## II.3 Scope-relative statements

"The organisation is divided into two camps" reads as
$\operatorname{cdim}^{\mathrm{eff}}_{S_1} = 2$: under the distinctions, perturbations
and resolution of $S_1$, two classes carry the relevant structure. Under $S_2$,
$\operatorname{cdim}^{\mathrm{eff}}_{S_2} = 7$ may be required. No contradiction,
provided $S_1 \neq S_2$ and both are declared. Neither statement establishes an
ontological number of groups.

## II.4 Selection and hiring

`status: claim`

Many candidate properties are observable. The existence of an observable does not place
it in the decision scope; the question is whether it preserves a distinction the
decision requires.

Stated carefully, and with the counter-direction that the earlier draft omitted:

- Adding observables can introduce irrelevant distinctions and permit accidental
  criteria to influence classification.
- Removing observables can also **destroy stability under $\Delta$**. Minimisation
  operates strictly inside the stability constraint (§I.5); "less is better" is false
  outside it.
- Therefore "more information does not necessarily produce a better decision" is a
  claim about scope-irrelevant observables, not a general information claim. It is
  unsupported by any case or study in this repo and is labelled `claim` accordingly.
- Where the removed observables are legally or ethically loaded (age, appearance),
  their removal is licensed by this framework only if they carry no required
  distinction — an *empirical* claim about the specific decision, and a normative
  matter beyond it (§I.8).

## II.5 Facilitation

A conflict presents disagreement points $\{q_1, \ldots, q_n\}$. Mapping asks which of
them determine different acceptance regions. Some are consequences of deeper
distinctions; some dissolve under terminology clarification; some are preferences
rather than constraints; some are structurally necessary.

$$
\text{many expressed differences} \rightarrow \text{few decisive distinctions}.
$$

Three practical consequences carried over from Part I, in order of importance:

1. **Suspected false consensus → widen $\Delta_J$**, do not re-question positions
   (§I.6).
2. **Report the antichain, not a single minimal scope** — and make the selection among
   irreducible scopes an explicit, visible step rather than an artefact of the
   procedure (§I.3).
3. **Declare the translation between participants' vocabularies before minimising**
   (§I.4); an undeclared translation makes the minimisation undefined while looking
   like it succeeded.

General workflow:

$$
\text{decision question} \rightarrow \text{required distinctions} \rightarrow \text{minimal observation} \rightarrow \text{perturbation test} \rightarrow \text{stable decision scope}.
$$

This reverses the common pattern (available information → criteria → weights → score →
decision) by inserting a prior question: *why is this distinction part of the decision
at all?*

---

## Relation to existing repo material

Collision check run against HEAD `e9c20fa` (2026-08-07). This note sits in an already
populated neighbourhood and **supersedes nothing**. The delta must be stated explicitly,
or it reads as a competing typology.

- **[conflict_navigation_nested_calibration.md](conflict_navigation_nested_calibration.md)**
  already owns conflict navigation with an ARW/ART split, the nested-loop construction,
  and the participation-incentive criterion. This note does not restate them. Its delta
  is the *construction of the joint scope itself* — acceptance regions $A_i$,
  irreducibility, and the antichain — which the nested-calibration note presupposes
  rather than builds.
- **[facilitation_toolkit_tuning_or_framing.md](facilitation_toolkit_tuning_or_framing.md)
  §5.3–5.4** already contains the over-compression failure in practitioner form, and
  states it better than Part I does: the test is not *did everyone agree* but *is
  everyone still represented*, and the early-warning sign is a real constraint going
  quiet. **§I.6 adds only the mechanism and the move it implies** — over-compression is
  what an under-declared $\Delta_J$ produces, hence widening the perturbation family is
  the diagnostic, not further questioning of positions. The toolkit's recovery move
  (put the constraint back on the table) stays owned there.
- **Toolkit §7, participation incentive** ("a party stays only when it has a stable
  position that is also negotiable") is a formalisation target for §I.5: the incentive
  fails if $A_i$ is not preserved under $\Delta_J$ *or* if the joint scope has collapsed
  onto $\partial A_i$, leaving nothing adjustable. Stated as a candidate reading only;
  the criterion itself stays owned by the toolkit and
  [kht_resonance_dialectic.md](../art_instantiations/kht_resonance_dialectic.md).
- **[minds_generalization_beyond_facilitation.md](minds_generalization_beyond_facilitation.md)
  §3 and Q-MINDS-03** already own the necessary-versus-preference question, with a
  candidate criterion at the $B$ level (a constraint is non-substitutable iff its
  violation moves the system out of $X_B$). §I.2 offers a different candidate — at the
  boundary of $A_i$ — and is routed through Q-MINDS-03 rather than registering a
  duplicate. Whether the two criteria coincide is Q-CMP-01.
- **[scope_component_conflict_typology.md](scope_component_conflict_typology.md) §1**
  classifies conflicts by *which tuple component the parties vary* ($\varepsilon$-, $\Delta$-,
  $\Pi$-, $B$-conflict). The three failure modes of §I.6 are **orthogonal** to that
  typology: they classify failures of the *joint-scope construction*, and any of them
  can occur within any of the four conflict types. Neither typology refines the other.
- **[kht_group_dynamics.md](../art_instantiations/kht_group_dynamics.md)** owns
  collective regime structure, polarization and groupthink at ART level. §II.2 defers to
  it and contributes only the reification reading (a subgroup counts as a party once its
  stability is reified at the next level).
- **[switch_minimization_criterion.md](../context_navigation/switch_minimization_criterion.md)**
  has the same shape — minimise a count subject to a persistence constraint — in the
  agent-mode domain. The antichain caveat of §I.3 plausibly applies there too; not
  pursued here.

---

## Open questions (Q-CMP, registered here)

*Collision check against HEAD `e9c20fa`: no `Q-CMP` ID exists anywhere in `docs/`.
Prefix allocated here; mirror into `docs/notes/open_questions.md` in the same session.*

**Q-CMP-01 — Do the two non-substitutability criteria coincide?**
Q-MINDS-03 proposes: non-substitutable iff violation moves the system out of $X_B$.
§I.2 proposes: necessary iff removal moves an outcome across $\partial A_i$. Do these
agree, and if not, which is operative? *Routed through Q-MINDS-03; not a duplicate
registration.*

**Q-CMP-02 — Is there a principled selection rule on the antichain?**
Under what conditions is the set of irreducible joint scopes finite, and is selection
among them necessarily exogenous to the formalism? *Why it matters:* if exogenous, every
MINDS-style procedure must expose the selection as a decision with an owner, or it
launders a choice as a result.

**Q-CMP-03 — Is $d_{\mathrm{red}}$ stable under change of the declared translation?**
If not, it reports the translation as much as the conflict, and must never appear in
external material. *Bears on:* Q-REL-05 ($\Phi$ is not evidence of class distance).

**Q-CMP-04 — Does the participation incentive admit the §I.5 reading?**
Is "stable position that is also negotiable" adequately captured by ($A_i$ preserved
under $\Delta_J$) ∧ (joint scope not collapsed onto $\partial A_i$)? *Bears on:*
Q-RD-6, Q-MINDS-02.

---

## Summary

$$
\textbf{Compromise is not the minimisation of distance between positions.}
$$

$$
\textbf{Compromise is the selection of an irreducible joint decision scope preserving the distinctions each acceptance classification requires, under a declared perturbation family.}
$$

Three repairs distinguish this from the "as little as possible, as much as necessary"
slogan: minimisation is over a partial order and yields a set, not a point (§I.3);
commensurability is a precondition, not an assumption (§I.4); and compression that
looks successful is exactly what an under-declared $\Delta$ produces (§I.6).
