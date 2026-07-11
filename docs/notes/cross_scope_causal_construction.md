---
status: note
layer: docs/notes/
depends_on:
  - docs/glossary/scope.md
  - docs/notes/scope_component_conflict_typology.md
---

# Cross-Scope Causal Construction: Generator Matching vs. Label Matching

> **Status note.** Exploratory. Originated in a Kaffeehaus session (2026-07-04),
> following on from the scope-component conflict typology. Triggered by a media
> case (patriarchal-violence framing) but the claim is domain-neutral. Candidate
> for promotion to `hypothesis` once a second independent instance is worked.

## 0. Scope of this note (important delimitation)

**This note is not a claim that causal inference is generally problematic.**
Within a fixed scope — same B, same Π, one generator — causal inference is the
ordinary, unproblematic business of the sciences: interventional data,
counterfactual structure, controlled comparison all work there without
anything in this note applying. A study showing "intervention X lowers rate Y"
*within* an aggregate population is a normal causal claim; it needs none of the
machinery below.

The problem addressed here is narrow and specific: **causal claims that are
established at one scope and then silently carried across a scope boundary**
to license a claim at a different scope (aggregate → instance, or instance →
aggregate), where the generator may — or may not — be the same on both sides.
Causal inference in general is not in question; causal *transport* across a
possible generator boundary is.

## 1. The problem

The conflict typology (`scope_component_conflict_typology.md`) diagnoses *what
kind of disagreement* two parties are having when they vary different scope
components. It does not address a related but distinct question: **how a causal
claim can legitimately be carried across a scope boundary at all** — e.g. from
an aggregate/structural scope to a single-instance scope, or vice versa.

This matters wherever a single observable label (e.g. "growth", or a case
classification such as "custody dispute" / "patriarchal violence") is shared
across scopes with different B (which states are selected) and possibly
different generators, and one party wants to use evidence gathered at one
scope to support a causal claim at the other.

## 2. Core claim

An observable label is a **many-to-one output of its generator** (cf. the
capital-growth/productivity worked case in the conflict typology, §6, and the
expected negative resolution of Q-REL-05: partition-level metrics cannot in
principle recover which generator produced them). Constructing causality across
scopes by matching the *label* rather than the *generator* produces two
symmetric fallacies:

- **Aggregate → instance**: attributing a structural/population-level mechanism
  to a specific case because the case's label matches the aggregate category
  (ecological fallacy). Example: citing a population-level rate of
  post-separation violence to explain *this* individual's motive.
- **Instance → aggregate**: using a single case (or a small, salient set) to
  confirm or deny a structural mechanism because the case carries the same
  label (hasty generalization). Example: treating one case's official
  classification ("custody dispute") as evidence against the existence of a
  broader structural pattern.

Both are instances of the same underlying error: treating label co-occurrence
as generator identity.

**Important asymmetry (2026-07-04 addendum).** Whether the generators actually
differ is, in general, **undecidable from the label alone** — this follows from
the same many-to-one principle, and mirrors why Q-REL-05 is expected to resolve
negatively. No instrument can reliably confirm or refute generator identity in
general. What *is* observable is something weaker and more useful: whether an
aggregation-level shift is occurring in the argument at all, and whether it has
been marked as such. §3 addresses this narrower, tractable question; §4's
three-part construction addresses what to do once a shift has been flagged.

## 3. Level-shift detection (precedes the bridge construction)

Because generator identity is undecidable in general, the useful instrument is
not a generator-difference detector but a **level-shift detector**: something
that flags *when and how* an argument moves between aggregation levels, so that
the move is forced into the open rather than passing silently on label
continuity. This does not establish admissibility — it establishes that an
admissibility question exists and has not yet been answered.

Candidate structural markers (surface-observable, independent of domain
content):

1. **Quantifier shift**: population quantifiers ("in X% of cases", "typically",
   a rate) transition to singular definite reference ("he", "this case") within
   the same causal chain, without an explicit transition marker.
2. **Evidence-type mismatch**: a claim about subject-level A is supported with
   an evidence class that properly belongs to level B (statistics cited as
   evidence for an individual's motive, or a single case cited as evidence
   against a population-level statistic).
3. **Predicate continuity without referent respecification**: the same causal
   predicate ("caused by", "driven by") is reused across the shift without
   re-specifying what it now refers to.
4. **Missing hedge at the seam**: no explicit qualifier ("this may, but need
   not, be an instance of X") at the exact point where the level changes.

None of these markers prove that the generators differ. They only show that a
level shift is occurring at that point in the argument. That is sufficient for
the intended purpose — **forcing admissibility review, not adjudicating
truth**. Once a shift is flagged, it must either go through the three-part
construction (§4) or be explicitly marked as undecided; it must not be allowed
to pass silently on label continuity alone.

This mirrors the missing-H0 pattern found in the H2' coherence review: not a
claim that the theorem was wrong, but that an admissibility precondition was
implicit and unmarked, and needed to be made explicit before further use.

## 4. Three-part construction required for a legitimate cross-scope causal claim

Applies once a level shift has been flagged (§3). A causal claim that
legitimately crosses a scope boundary needs three independently-supported
parts, not one:

1. **Mechanism claim at the source scope**, stated with a counterfactual /
   interventionist structure (a real Δ, not just a correlation): e.g. "if
   protective measures during the post-separation risk phase are strengthened,
   the rate should fall." This is what makes it a causal claim at that scope at
   all, rather than a described pattern.
2. **Instance-level signature evidence**, independent of the label, and fixed
   *before* the instance is inspected (to avoid circularity — see §5 open
   question on ex-ante specification): case-specific evidence that the
   *mechanism itself* — not just the label — is present (e.g. documented
   control/entitlement dynamics, escalation pattern, prior threats), not mere
   co-occurrence of surface features ("separation" + "violence").
3. **The bridge claim itself** — "this instance is generated by that mechanism"
   — is a third, independently checkable claim, with three admissible outcomes:
   satisfied, not satisfied, or **undecidable**. It is not automatically proven
   by (1) and (2) holding separately; both a real structural mechanism and a
   real individual case can be true without the individual case being an
   instance of that mechanism. "Undecidable" must remain a legitimate,
   first-class outcome — if it is not, the procedure collapses back into label
   matching whenever evidence is thin.

**The characteristic failure mode**: treating (1) as established and then
treating (2) as automatically satisfied by label match alone, skipping (3)
entirely. This is the failure mode observed in the originating case: a
structural mechanism (documented, real) was used to license a causal
classification of a specific instance without instance-level signature
evidence, and the competing instance-level scope (individual case
classification) was treated as illegitimate for declining to make that jump
(see the Π-monopolization pattern noted as a follow-up to the conflict
typology).

## 5. Relation to existing ARW work

- **Σ vs. partition-level metrics**: the same diagnostic move as WP-A5 —
  matching operator signatures rather than partition-level (here: label-level)
  output — applied to a causal-construction question rather than a
  classification question. The undecidability of generator identity (§2
  addendum) is the same principle behind the expected negative resolution of
  Q-REL-05.
- **H2' coherence review / missing H0**: §3's level-shift detector plays the
  same structural role as the missing admissibility precondition found for
  H2' — not a truth claim, an explicit precondition that was previously
  implicit and unmarked.
- **Scope-component conflict typology**: this note's problem is downstream of
  Π-monopolization (a party refusing to name the other scope's assumptions and
  limits at all) but is not solved by naming scopes alone. Reconciliation
  (naming B, usage range, and limitation per scope) is necessary but not
  sufficient — it prevents the *illegitimacy* framing but does not by itself
  license or block the causal bridge in either direction.
- **Conflict-navigation model** (`conflict_navigation_nested_calibration.md`):
  the bridge claim (§4.3 above) is exactly the kind of claim the upper
  calibration loop should isolate as a separate, explicitly contested item,
  rather than letting it ride silently on the other two.

## 6. Open questions

- Can §3's four markers be operationalized as a checklist applicable to text
  (e.g. for use alongside `arw-meta-guard`-style review), or do they require
  domain judgment that resists formalization?
- How is instance-level signature evidence (§4.2) specified *before* inspecting
  the instance, in practice, without either being so generic it is trivially
  satisfied or so specific it is circularly reverse-engineered from the case at
  hand?
- Does the strength of the source-scope mechanism claim (§4.1) trade off
  against the amount of instance-level signature evidence (§4.2) required —
  i.e. a stronger population-level effect size lowering the evidentiary bar for
  individual attribution — or are these strictly independent axes?
- Untested: does this three-part structure generalize to non-adversarial
  cross-scope inference (e.g. scientific transfer between aggregate and
  individual-system models), or is the label/generator conflation specific to
  contested, socially-loaded classifications?

## 7. Illustrative instance (not a case; no pipeline artifacts)

Media framing dispute over a violent incident (Stade, 2026-07-04 news cycle):
one side classifies the incident by its immediate legal/procedural trigger
("custody dispute"), the other by its structural category ("patriarchal
violence" / post-separation violence pattern). Both labels can be simultaneously
true of the same event without either licensing the causal claim the respective
side wants to draw from it, absent instance-level mechanism evidence per §4.2.
Recorded only to preserve the originating material; not a worked ARW/ART case.
