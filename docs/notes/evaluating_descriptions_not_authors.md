---
status: note
layer: docs/notes/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
  - docs/notes/ews_discriminator_test_protocol.md
---

# From Evaluating Authors to Evaluating Descriptions

**Status: concept note.** This is a programmatic note, not a definition. It proposes a
shift in what scientific evaluation takes as its object, and records how far ARW already
operationalizes the proposed dimensions. Registered questions: Q-EVAL-01, Q-EVAL-02.

---

## 1. Motivation

Artificial intelligence fundamentally changes the economics of scientific work.

For centuries, the limiting factor was the production of scholarly material. Writing,
programming, literature review, mathematical derivation, and figure preparation required
substantial human effort. Scientific institutions therefore evolved mechanisms that
largely evaluated people and publications as proxies for underlying quality.

AI changes this balance. Generating polished text, code, figures, or literature summaries
is becoming progressively cheaper. Consequently, the bottleneck shifts from production to
evaluation. The scientific question is no longer:

> Can someone produce a convincing paper?

Instead, it becomes:

> Does this work increase humanity's reliable descriptive capability?

This distinction may prove fundamental.

## 2. The Wrong Question

A growing temptation is to classify research according to the amount of AI involved.
However, AI usage is not itself a scientific property. Two identical manuscripts possess
identical scientific content regardless of whether one author used AI to improve clarity
or structure.

The scientifically relevant object is therefore not the writing process, but the
description itself.

## 3. Descriptions as the Unit of Evaluation

If descriptions become the primary object of study, research evaluation shifts from
author-centric metrics toward descriptive metrics. A description may be evaluated by
asking:

- What new distinctions does it make possible?
- Which previously separate observations does it unify?
- Under which scope conditions is it valid?
- Can independent observers operationalize it?
- Does it survive transfer into different domains?
- What predictions, experiments, or engineering methods emerge from it?
- Under which perturbations does it fail?

These questions are largely independent of institutional affiliation, publication venue,
citation count, or AI assistance. They evaluate the description directly.

## 4. Dimensions of Descriptive Quality

The following dimensions illustrate a possible descriptive evaluation framework.

1. **Descriptive Gain** — does the description distinguish phenomena that previous
   descriptions merged?
2. **Compression** — does it explain more using fewer assumptions or independent rules?
3. **Explicit Scope** — are validity conditions clearly stated?
4. **Operationality** — can another researcher determine whether the description applies?
5. **Falsifiability** — does the description specify observable failure conditions?
6. **Transferability** — does the structural description remain admissible across
   heterogeneous contexts?
7. **Generativity** — does it enable new experiments, technologies, explanations, or
   successful adaptations?
8. **Robustness** — does it remain stable under reasonable perturbations?

## 5. Why AI Makes This Necessary

When producing text becomes inexpensive, polished language ceases to be a meaningful
quality signal. Scientific value therefore migrates toward characteristics that are
considerably harder to automate: reproducibility, operational precision, transfer,
validation, and stable explanatory power.

The evaluation problem shifts from "Who wrote this?" to "What does this description
reliably accomplish?"

## 6. Relation to ARW — Operationalization Map

Although motivated independently, this perspective aligns with the ARW research
programme: ARW treats descriptions as measurable objects whose quality depends on
properties such as admissibility, stability, transfer, and observable structure rather
than rhetorical elegance.

The alignment is not merely thematic. For several of the dimensions in §4, ARW already
provides partial operationalizations:

| Dimension | ARW operationalization | Status |
|---|---|---|
| 1. Descriptive Gain | Regime partition refinement; a description that resolves regimes a coarser one merges (RCD, cover structure) | partial |
| 2. Compression | No dedicated machinery; related to signature-based BC inference (operator structure → cover geometry) | absent/indirect |
| 3. Explicit Scope | The scope tuple S = (B, Π, Δ, ε) is exactly a declaration of validity conditions ([scope](../glossary/scope.md)) | direct |
| 4. Operationality | ScopeSpec/BCManifest/CaseRecord schemas + pipeline reproducibility; independent observers can re-run a case | direct |
| 5. Falsifiability | The F-category schema (F0–F4, F-gradient, Z_shared) specifies observable failure conditions per description ([observable_range](../glossary/observable_range.md)) | direct |
| 6. Transferability | transfer_v2 metrics (Φ, TBS_norm, RCD, SDI) — with the standing caveat that Φ measures observable transfer, not system transfer, and Q-REL-05 is open ([transfer metrics](../bc_taxonomy/transfer_distortion_metrics.md)) | partial |
| 7. Generativity | Not operationalized; observable only retrospectively | absent |
| 8. Robustness | σ_Δ(x) and Δ-stability of the partition; ε-plateau width | direct |

That five of eight dimensions have direct or partial ARW operationalizations is what
lifts this note above a manifesto: the proposal is not "evaluate descriptions somehow"
but "the machinery for a first subset already exists and has been run on cases."

This note suggests extending that philosophy beyond ARW itself. Such an approach does
not replace peer review; it proposes shifting peer review toward explicit evaluation of
descriptive quality.

## 7. Self-Application (Guard)

This note's standard applies to ARW first. The current evidence status of ARW's own
central claims is "plausible but insufficiently supported" (external assessment,
2026-08-01, recorded in the DOC_INDEX entry for the EWS discriminator protocol). Under its own framework, ARW does not get to
claim descriptive quality by declaration — it must score on the dimensions of §4 with
public artifacts: the repository itself (dimension 4), the falsification schema
(dimension 5), the preregistered EWS discriminator test
([protocol](ews_discriminator_test_protocol.md)) as a live instance of dimensions 5
and 8, and the transfer pipeline (dimension 6).

Two failure modes must be named explicitly:

1. **Self-serving bypass.** A description-centric evaluation framework proposed from
   outside academia, by an author without a practical peer-review route, is structurally
   at risk of functioning as a substitute for the validation it claims to improve. The
   guard is symmetry: the framework carries weight only insofar as ARW itself submits to
   it and publishes the resulting scores — including failures.
2. **Dimension gaming.** Any fixed dimension list invites optimization of the scores
   rather than the descriptions (Goodhart-type proxy failure; cf. the delimitation in
   `scale_gap_ambiguity_audit_stability.md` §5 against proxy failure). The dimensions in
   §4 are therefore illustrative, not canonical.

## 8. Relation to Existing Literature (unverified)

The proposal has obvious neighbours: the reproducibility/registered-reports movement
(dimension 4/5 institutionalized), minimum-description-length approaches (dimension 2),
Popperian falsificationism (dimension 5), and "hard to vary" explanation criteria
(dimension 2/8). Whether any existing metascience programme evaluates *descriptions as
objects* — rather than papers, authors, or claims — is not verified against the
literature in this note. Registered as Q-EVAL-02.

## 9. Long-Term Vision

If AI continues lowering the cost of producing scientific artifacts, the limiting
resource of science will increasingly become high-quality descriptions rather than
publications themselves. A mature science of descriptions would ask not merely whether
a theory is true, but whether its descriptive structure represents a measurable
improvement over competing alternatives.

In this view, scientific progress becomes the systematic improvement of humanity's
descriptive repertoire. The central question of future research may therefore become:

> How can we objectively measure whether one description constitutes a genuine advance
> over another?

Registered as Q-EVAL-01. This question may itself become a legitimate scientific
discipline — and within ARW it is not rhetorical: for the subset of dimensions in §6
marked "direct," it is already a measurement task.
