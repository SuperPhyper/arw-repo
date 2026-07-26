---
status: note
layer: docs/notes/
companion: arw_theory_audit_2026-06-10.md, arw_audit_repair_plan_2026-06-10.md
decision_date: 2026-07-02
decided_by: Rico Felder
---

# Decision Note — WP-A3: Part VI Transfer Reframing

## Decision

**Framing (a) — necessary-condition framing — is adopted.**

The partition-level metrics (RCD, TBS_norm, PCI, SDI, composite Φ) measure
**partition compatibility**: a *necessary but not sufficient* condition for
structural transfer. Transfer itself is grounded in the signature structure Σ
(operator signatures S1–S5), not in partition resemblance. Φ is a filter, not
a verdict — consistent with the closing paragraphs of Part VI §6.3 as drafted.

Framing (b) (metric-minimal) is rejected: it would discard the pedagogical
value of the metric apparatus without adding evidential strength.

## Rationale (beyond audit A2)

The 2026-06-02 findings read together are an information-theoretic argument,
not a measurement defect:

- Φ (v1) tracked regime count N for ~90% of its weight.
- PCI does not separate same-class from cross-class (0.659 vs. 0.650, tied).
- D-CTRL-1 (same N, different BC class) yields Φ = 0.729 — not low.

**Partitions are many-to-one outputs of their generators.** Distinct BC
structures can produce near-identical partitions on normalised axes; therefore
no partition-level construction can in principle recover BC-class distance.
Q-REL-05 is expected to resolve negatively, and this expectation should be
stated as such in Part VI / Part IX rather than left as a neutral open question.

The repo structure encodes the same conflation: `TransferMetrics.json` compares
partition artifacts, while the signature level (S1–S5 tables in Signature-First
ScopeSpecs) does not feed the transfer pipeline. The data model is
partition-first; the theory (pairwise-local admissibility, Σ as generator) is
signature-first. This mismatch — not the metric weighting — is the root finding.

## Execution consequences (per WP-A3, extended)

1. **Part VI §6.3 rewrite:** end-of-section Φ paragraph aligned to filter
   framing (largely done in draft v1); no claim anywhere that Φ detects shared
   BC structure.
2. **§6.4** presents the 2026-06-02 result as the finding that *forces*
   transfer to be grounded in Σ (weakness-to-result conversion, repair
   principle 2). Write §6.4 only after this note is merged.
3. **Directional containment 0.833** (D-CTRL-2, admissible coarsening) is
   promoted into §6.3 as the one robust partition-level signal; coarsening is
   the transition type partitions can honestly carry.
4. **Stylized TBS example** in §6.3 replaced with the real CASE-0001↔0003
   value (TBS_norm = 0.356) or explicitly marked stylized (WP-C1 convention).
5. **Q-REL-05** named as limitation in Part IX, with the expected-negative
   reading above.

## New work package (proposed): WP-A5 — Signature-level transfer artifact

Extend the repo schema with a signature-comparison object (working name
`SignatureTransfer.json`) that compares S1–S5 operator signatures of two cases
and sits alongside `TransferMetrics.json`. Transfer workflow becomes two-stage:

- **Stage 1 — partition filter:** Φ and companions (necessary condition).
- **Stage 2 — signature comparison:** Σ-level evidence (the structural claim).

Acceptance: Q-REL-05 becomes empirically testable inside the pipeline;
`framework_validation.md` hardness labels reference stage-2 evidence for any
"Strong" transfer claim. Effort: M. Blocks: none; blocked by: SDI canon
decision (WP-A4) only for symbol hygiene.

## Pending (explicitly deferred, do not lose)

**CASE-0004 ↔ CASE-0001 (Φ = 0.9983) requalification.** Under the adopted
framing this result evidences partition compatibility, not structural
transfer. Its "Strong" classification in `framework_validation.md` must be
re-grounded in independent signature evidence (same BC class: Coupling) or
downgraded. To be handled as its own session; touches
`framework_validation.md` and possibly the monograph's use of the case.

---

## Maintenance Note (2026-07-11 import, updated same day)

Imported into `arw-repo` from `To-REPO/` (placed there after the initial
2026-07-11 batch was already processed). Its two named companions were initially
**not found** anywhere in `arw-repo` or `Simulationen`; Rico then uploaded both
directly, and they are now imported as `docs/notes/arw_theory_audit_2026-06-10.md`
and `docs/notes/arw_audit_repair_plan_2026-06-10.md`. `framework_validation.md`
and the "Part VI / Part IX" monograph / `SignatureTransfer.json` remain **not
found** — likely live in an external writing workspace not currently connected;
Rico confirmed he isn't sure where `framework_validation.md` specifically is.
Treat any statement depending on those three as unverified against this repo.

**Possible duplicate decision record, unreconciled.** `arw_audit_repair_plan_2026-06-10.md`
already lists WP-A3 under "Decision points for Rico — SETTLED 2026-06-10" with
"Executed: §6.3 ending rewritten" — three weeks *before* this note's own
2026-07-02 decision date. Both make the same substantive choice (framing (a),
necessary-condition). This note adds detail absent from the June record (the
WP-A5 proposal, D-CTRL specifics) but does not reference the June settlement or
mark itself as a restatement. Left as-is, not merged or deduplicated — flagged
here for Rico to say whether this is a second, more detailed formalization of
the same decision, or two independent decision events that happen to agree.

> **RESOLVED 2026-07-14 (Rico):** this note is a **restatement** — a more
> detailed formalization of the single decision settled 2026-06-10. There was
> one decision event. This note is the **canonical record** of WP-A3 (it carries
> the full rationale, the WP-A5 proposal, and the pending requalification item);
> the repair plan's "SETTLED 2026-06-10" line remains as the settlement record
> and now points here. No content conflict between the two records.

**A real inconsistency found and fixed, not just a documentation gap.** WP-A4
(SDI canon decision, in the repair plan) recorded that the correct SDI
definition (graph edit distance) was applied to the context map on 2026-06-10,
with a skill patch only *staged* in `Simulationen/arw-repo-context_SKILL_patched.md`.
That staged patch was never actually merged: the live `arw-repo-context` skill —
including the version revised just this week during an unrelated skill-maintenance
pass — still carried the stale SDI definition
(`1 − |w_A−w_B|/max(w_A,w_B)`, ε-plateau-width similarity) until this compatibility
check caught it. Fixed directly in `arw-repo-context` on 2026-07-11 (see that
skill's own maintenance history). Also caught and fixed in the same skill: an
"INC-01 still open" claim that was already stale (INC-01 closed 2026-06-10,
per WP-B2).

Cross-check against repo docs imported the same week: `docs/notes/scope_component_conflict_typology.md`
and `docs/notes/cross_scope_causal_construction.md` (both 2026-07-04, i.e. after
this decision) already use the "expected negative resolution of Q-REL-05" framing
and reference WP-A5 by name, consistent with this note — no conflict found.
The canonical Q-REL-05 entry in `docs/notes/open_questions.md` was still neutrally
`open` before this import; updated on import per this note's own instruction
(see that file's entry for the change).
