---
status: note
layer: docs/notes/
title: "Scale-Gap Ambiguity: Cascade Closure as Audit Stability"
created: 2026-07-25
imported: 2026-07-25
depends_on:
  - docs/glossary/scope.md
  - docs/notes/inductive_strengthening_cascade_closure.md
open_questions:
  - Q-STR-04
  - Q-STR-05
  - Q-STR-06
---

# Scale-Gap Ambiguity: Cascade Closure as Audit Stability

**Status: note (exploratory).** Companion to
`inductive_strengthening_cascade_closure.md`; the formal core below consumes its
definitions. Neither document is an ART instantiation and no case artifacts are
implied.

## 1. Motivation

A recurring vector for exploitation-through-ambiguity is not vagueness within a
single description but a *gap between scales of description*: a claim that is true
and verifiable at a coarse resolution while leaving its fine-resolution realization
unconstrained. The statistic is honest; the individual case it licenses is not. The
contract clause is precise at document level; its application to a concrete situation
is chosen adversarially. In each instance the coarse claim functions as a compliance
shield for a fine-scale choice the counterparty never had to disclose.

This note proposes that the phenomenon has an exact ARW formulation via the
ε-cascade, that cascade-closed descriptions are precisely the ones immune to it
(**audit stability**), and that — because inductive strengthening is *costly* —
refusal to adopt an available strengthening is itself descriptive information about
the refusing party (**strengthening refusal as signal**).

## 2. Formal core: the realization class

Setting as in the companion note: a scope family {S_ρ = (B, Π_ρ, Δ, ρ)} over a
resolution range, with a claim C asserted and verified at coarse resolution ρ₁. The
notation guard of that note applies here unchanged: ρ is the canonical resolution
threshold ε, not an additional tuple component.

**Realization class.** For a finer resolution ρ₂ < ρ₁, define

    Real(C; ρ₁→ρ₂) = { fine-scale configurations x admissible under B
                       whose coarse-graining to ρ₁ satisfies C }

**Scale-gap ambiguity.** The ambiguity of C over the gap [ρ₂, ρ₁] is the diameter of
the realization class under the fine-scale descriptive metric:

    Amb(C; ρ₁→ρ₂) = diam_{d_Π, ρ₂} Real(C; ρ₁→ρ₂)

If Amb ≤ ε at ρ₂, verifying C at the coarse scale already pins the fine-scale
situation up to indistinguishability: nothing exploitable remains in the gap. If
Amb ≫ ε, the coarse claim is compatible with fine-scale configurations that are
descriptively far apart — and an interested party may select among them.

**Exploitation, structurally.** Scale-gap exploitation is adversarial selection
within Real(C; ρ₁→ρ₂): choosing the realization that maximizes the selector's
utility while preserving coarse compliance. No falsehood is uttered at ρ₁; the harm
lives entirely in the unconstrained degrees of freedom the coarse description never
bound. This is why fact-checking the coarse claim cannot detect it — a special case
of "more information at the same scale does not help."

**Distinction from Goodhart.** Goodhart-type failure is optimization *of* a proxy
that degrades the proxy's validity. Scale-gap exploitation keeps the coarse claim
fully valid; the selection happens in the claim's fiber, not against the claim. The
two can co-occur but have different repairs (proxy redesign vs. cascade closure).

## 3. Audit stability

**Definition sketch.** A description is **audit-stable** over [ρ₂, ρ₁] if for every
intermediate resolution ρ in the range, Amb(C; ρ₁→ρ) ≤ ε. Equivalently: zooming in
at any level yields verdicts consistent with the coarse verdict — verification
commutes with resolution change.

**Connection to cascade closure.** A cascade-closed strengthening C′ (companion
note) is exactly a device for shrinking realization classes scale by scale: the
induction step that carries C′ downward is, read contrapositively, a bound on what
fine-scale configurations coarse compliance can hide. Conjecture (Q-STR-04): audit
stability over a range is equivalent to the existence of a cascade-closed
strengthening whose per-scale content is verifiable within Π_ρ.

**Cost restated.** Audit stability is therefore not free: it inherits the projective
load of the strengthening. A maximally lean coarse description is maximally
gap-ambiguous; binding the gap requires carrying auxiliary structure at every scale
(disaggregations, worked applications, selection rules) that a parsimony-optimal
reporter would omit.

## 4. Strengthening refusal as signal

Because the load is real, adopting a strengthening is a **costly self-binding**:
the party volunteering it forfeits the option value of the realization class. This
supports a signaling reading:

- If an audit-stable formulation is (a) known to exist, (b) available at bounded
  cost to the describing party, and (c) refused, the refusal is evidence that the
  option value of Real(C; ρ₁→ρ₂) is positive for that party — i.e., that the gap is
  load-bearing for them.
- The inference is probabilistic, not verdictive. Legitimate refusal grounds exist:
  the load may be genuinely unaffordable, the fine-scale observables may be
  privacy-protected, or the strengthening may leak competitively relevant structure.
  The signal is the *unexplained* refusal — refusal without a declared, checkable
  ground.

This inverts the usual audit posture: instead of hunting for falsehood at the coarse
scale (where there is none), the auditor asks for the strengthening and reads the
response. The demand is cheap to formulate once the concept is named; the asymmetry
between "binds willingly" and "declines without grounds" does diagnostic work that
coarse-scale verification cannot.

## 5. Illustrative instances (not ART cases; no artifacts implied)

- **Aggregate vs. individual**: a population-level statistic used to justify a
  decision about a specific case — the case sits anywhere in a wide realization
  class the statistic never constrained.
- **Contract text vs. application**: clause-level precision with
  application-level discretion retained by the drafting party.
- **Reported metrics vs. operational reality**: compliance reporting whose
  categories are satisfiable by operationally disparate practices.
- **Shared term vs. party-specific elaboration** (added 2026-07-25): a public
  term — *supply security*, *sustainability*, *risk* — functions as the coarse
  level; each party's implicit elaboration is the fine level. Real(term) is the
  set of elaborations compatible with the shared label, and for the terms that
  do the most public work Amb is very large. This instance is structurally
  interesting because it inverts the note's framing: here the large realization
  class is what makes communication possible at all, since parties with
  incompatible fine-scale models can still attach to one coarse label. The same
  quantity is therefore the enabling condition and the failure mode, and
  explication — a cascade-closed strengthening — is refused not (only)
  adversarially but because its projective load is genuinely unaffordable in
  ordinary discourse. This is the *legitimate-refusal* branch of §4 arriving as
  the normal case rather than the exception, and it is the reason §4's signal
  reading must not be applied to public language without an argument about cost.
  Source thesis and the wider treatment:
  `docs/art_instantiations/kht_resonance_dialectic.md` §6.3;
  `docs/notes/scope_component_conflict_typology.md` §8.

Each would need its own scoping before becoming an ART instantiation; they are
listed here only to fix intuition.

**Relation to the aggregation-limits machinery (checked on import).**
`docs/advanced/arw_aggregation_limits_typological_observables.md` defines N* as the
*variance crossover* point — the aggregation level at which within-class and
between-class variance of an outcome exchange magnitude. This is not a
realization-class diameter, and no quantity in that document currently bounds Amb.
The two are plausibly related for aggregate-vs-individual instances (large σ²_W at
fixed class assignment is what makes the class-level claim weakly binding on the
individual case), but the bound is a conjecture, not an inheritance — folded into
Q-STR-06 rather than cross-referenced as settled.

The economic regime hypothesis (`docs/notes/arw_economic_regime_hypothesis.md`,
Q = K/G as extraction proxy) remains a candidate first quantitative testbed:
extraction that preserves coarse-indicator compliance is scale-gap exploitation in
this note's sense.

## 6. Open questions (registered 2026-07-25)

Registered in `docs/notes/open_questions.md` alongside the companion note's
Q-STR-01–03. Prefix collision-grepped 2026-07-25; Q-STR- was unused.

- **Q-STR-04 (open)**: Equivalence — is audit stability over [ρ₂, ρ₁] equivalent to
  the existence of a Π-verifiable cascade-closed strengthening?
- **Q-STR-05 (open)**: Signal conditions — under what assumptions on cost
  distribution and common knowledge does strengthening refusal separate
  gap-exploiting from load-constrained describers? (Likely imports standard
  costly-signaling structure; determine what, if anything, is ARW-specific beyond
  the formulation of the signal's content.)
- **Q-STR-06 (open)**: Measurement — can Amb(C; ρ₁→ρ₂) be estimated in pipeline
  terms (sampling the realization class under B and computing d_Π-diameter at ρ₂),
  and does the aggregation-limits N* machinery bound it?

## 7. Path to promotion (note → hypothesis)

Falsifiable formulation candidate: in a system with a computable realization class,
(i) Amb decreases monotonically as cascade-closed structure is added and (ii) no
same-scale refinement (adding observables at ρ₁ only) reduces Amb below the bound
set by the gap. (ii) is the sharp claim — it predicts that scale-gap ambiguity is
invisible to and irreparable by single-scale effort, which a counterexample could
kill.

## Import record (2026-07-25)

Registration checklist of the offline draft, executed:

- [x] Imported together with `inductive_strengthening_cascade_closure.md`; the
      `depends_on` entry resolves to its final path
- [x] DOC_INDEX grep for *audit stability, realization class, scale gap, ambiguity
      measure, costly signal* — no coverage found; new doc, not an extension
- [x] Aggregation-limits doc checked for a realization-class-like quantity — N* is a
      variance crossover, not a diameter; no duplication, and the conjectured bound
      is recorded in §5 and Q-STR-06 rather than asserted
- [x] No `-N` suffix sibling exists in `docs/notes/`
- [x] Q-STR-04–06 collision-grepped alongside Q-STR-01–03 and registered
- [x] DOC_INDEX row added
