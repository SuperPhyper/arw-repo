---
status: note
layer: docs/notes/
companion: arw_theory_audit_2026-06-10.md
---

# ARW Audit Repair Plan — 2026-06-10

**Purpose:** Convert the audit findings (arw_theory_audit_2026-06-10.md) into executable
work packages. Each package names its audit finding(s), deliverable, acceptance
criterion, effort (S ≤ 1 session, M = 1–2 sessions, L = several), and who decides.

**Three principles govern the plan:**

1. **Repair before new prose.** No drafting of Part VI §§6.4–6.5 or Part VII until the
   sections they depend on are corrected (gates G1–G3 below).
2. **Convert weaknesses into results.** Where the audit found overclaiming, the repair
   is usually not deletion but conversion: the separatrix correction becomes a
   falsification-in-action narrative; the Φ defect becomes the motivation for
   signature-level transfer; the reflexivity rhetoric becomes a worked self-application.
3. **Evidence-status discipline.** Every empirical claim in the book gets one of three
   visible statuses: *pipeline-validated (case ID)*, *theoretically derived*, or
   *conjectured/stylized*. Introduced once (WP-C1), applied everywhere.

---

## Workstream A — Evidence corrections in existing drafts (S1 findings)

### WP-A1 — Rewrite Part III §3.3 + Executive Summary (audit A1) — **M**
Replace the E_sep = 2ω₀² / secondary-ridge narrative with the corrected single-ridge
account: separatrix at E_sep = ω₀², self-similarity in u = E/ω₀² (CV < 1%), σ_Δ/ε = 2.0,
one energy scale. Add a short boxed passage telling the correction itself: the framework's
own re-analysis eliminated a spurious structure (falsification-in-action — fits the
book's stance). The regime-boundary vs. descriptive-crossover distinction stays, but as
a theoretical distinction; its empirical showcase moves (→ WP-D2 may supply a new one).
- Touches: §3.3 both boxes, FIG comments (Fig 3/4), Exec Summary ¶3, §4.2/§5.2 spot-check.
- Acceptance: no occurrence of `2ω₀²`/secondary ridge in any draft; numbers match
  kuramoto_pendulum_cover_pipeline_v2 metadata.
- Lead: Claude drafts, Rico reviews.

### WP-A2 — σ_Δ-first rewrite of Part III §3.2 boxes (audit A3, D5) — **S**
Recast the Kuramoto boxes with perturbation spread σ_Δ as the primary instability
quantity; demote the gradient to a bulk proxy with an explicit caveat at θ* (C1/C2).
Resolve the 1.49 vs 1.60 figure tension: decide which dataset the figure shows and add
one finite-N reconciliation sentence.
- Acceptance: no diagnostic recipe in Part III that C1/C2 invalidated; both κ_c numbers
  either reconciled in text or one removed.
- Lead: Claude drafts, Rico reviews.

### WP-A3 — Decide and execute the Part VI reframing (audit A2) — **M, decision required**
Decision for Rico (pick one before any §6.4–6.5 drafting):
- **(a) Necessary-condition framing (recommended):** §6.3 metrics measure partition
  compatibility — necessary, not sufficient, for structural transfer; §6.4 presents the
  2026-06-02 finding as the result that *forces* transfer to be grounded in Σ; §6.5
  universality discussion builds on signatures. Strongest fit with existing §6.2.
- **(b) Metric-minimal framing:** strip §6.3 to RCD/TBS_norm + directional containment,
  treat Φ as historical; transfer chapter becomes purely structural.
Then: rewrite the end of §6.3 (Φ paragraph), add directional-containment result
(0.833, admissible coarsening) as the one robust partition-level signal, replace the
stylized TBS example with the real CASE-0001↔0003 value (0.356) or mark it stylized.
- Acceptance: nothing in Part VI claims Φ detects shared BC structure; Q-REL-05 named.
- Lead: Rico decides framing; Claude executes.

### WP-A4 — SDI canon decision (audit A4) — **S, decision required**
Decide what SDI names: graph edit distance (canonical doc, Part VI usage) or
plateau-width similarity (context map, skill). Recommendation: SDI keeps the graph
definition; the plateau-width quantity gets a new symbol (e.g. RSI, robustness
similarity). Then fix the losing documents (context_map_transfer_emergence_cases.md
or transfer_distortion_metrics.md), check what `pipeline/transfer.py` / `transfer_v2.py`
actually compute, and stage the skill patch (skills are read-only — patch via the
established *_SKILL_patched.md workflow in Simulationen).
- Acceptance: one definition per symbol across repo docs, context maps, pipeline, book.
- Lead: Rico decides; Claude executes repo+book side, stages skill patch.

> **AMENDMENT 2026-07-17 (from monograph Part VII external revision).** SDI
> keeps the graph-edit-distance definition, but is now proven **trivially
> collinear with RCD in the 1D-sweep tier**: the sweep-form transition graph
> is forced to a path on N nodes (regimes are contiguous runs of an ordered
> sweep), so SDI = f(N_A, N_B) deterministically — by construction, not
> empirically. Disposition: w₄ = 0 in Φ by default; SDI reported unnormalised
> as a diagnostic; enabled only against an attributed transition graph (edges
> carrying ε_merge / hysteresis / α / signature type / BC label) or the
> Δ-induced transition graph, whose construction is open (Q_NEW_25).
> **Acceptance criterion extended:** not one-definition-per-symbol only, but
> a per-metric *independent-information* requirement — each metric in a
> comparison set must be justified by information it carries independent of
> regime count, membership, and transition order; a metric that is a
> deterministic function of the others is a diagnostic, not a dimension.
> Executed in `transfer_distortion_metrics.md` (SDI + Φ sections) and
> monograph Part VII V4.2/V4.3 same day.

---

## Workstream B — Repo canon consistency (blocks Part VII)

### WP-B1 — open_questions.md cleanup (audit D4) — **S**
Merge the two contradictory Q-REL-04 entries into one (status: answered — structural
break, with the duplicate's useful formal content folded in); update Q-NEW-CROSS-1
(remove refuted secondary-ridge reference; the question survives in general form).
- Acceptance: one Q-REL-04; no stale ridge references in open_questions.md.

### WP-B2 — Close INC-01 + epsilon doc update (audit B3, D6) — **M**
Upgrade `docs/glossary/scope.md` ε-indistinguishability to the Čech-cover construction;
update `docs/advanced/epsilon_and_scope_resolution.md` to formally name σ_Δ and ε*(O,X).
Both flagged "still open" since 2026-04-29/05-20. Run arw-meta-guard + doc-consistency
checks; register in DOC_INDEX.
- Acceptance: Part VII can be drafted from these two docs without importing stale canon.

### WP-B3 — Q_NEW_1 placement decision (audit B3) — **S, decision required**
Where does the structure of X live: B, a meta-layer below S, or ART? Any consistent
choice works; the book needs the decision, not the solution. Recommendation: ART layer
(domain instantiation carries X-structure; ARW-core stays clean) — but this is Rico's
call. Document in glossary + one sentence in Part VII V1 plan.

### WP-B4 — Plan status sync (audit D1) — **S**
Update action plan v3 (or issue v3.1): Part VI marked 🟡 (6.1–6.3 drafted, 6.4–6.5
open), Phase 0d (K4) reopened pending WP-C3, audit + this repair plan referenced.

---

## Workstream C — Claim-strength alignment in drafts (S2/S3, small edits)

Each is ≤ 1 paragraph; bundle as one editing session (**M total**), order as listed.

- **WP-C1 — Evidence-status convention (audit B2, C6):** one footnote/notation
  convention introduced early (Introduction or Part II): *pipeline-validated (case ID)*
  / *theoretically derived* / *stylized example*. Apply to pandemic numbers, BMI
  passage (soften or cite), §6.3 example.
- **WP-C2 — Part III §3.1 taxonomy claim (audit B1):** "the formal answer" → candidate
  structural answer, developed in Part IX (align with Part V's correct phrasing).
- **WP-C3 — K4 pointer sweep (audit D2):** Part II CITE targets "Part VI, V1/V2/V3/V6"
  → Part VII; "Part VII (Error Forms)" → Part VIII; Part III §3.5 "developed in Part VI"
  → Part VII. Grep-verifiable.
- **WP-C4 — Part II ε honesty paragraph (audit B4):** name the chain/sorites defect of
  naive "same below ε"; working picture = zones that hold together at resolution ε
  (cover components), formal in Part VII. Map metaphor survives.
- **WP-C5 — Part IV emergence scaling (audit B7):** "the mechanism" → ARW's structural
  account; one-case status (CASE-0004) stated.
- **WP-C6 — Part IV/VI BC-class property flag (audit B5):** explicit statement that
  system-BC vs observable-BC decomposition is open (Q_NEW_9), with the designed test
  named (→ WP-D3).
- **WP-C7 — Introduction ex-ante demarcation (audit B8):** ARW specifies the
  *conditions* of failure in advance, not the *moment*; one clause in the Introduction,
  one sentence in Part V.
- **WP-C8 — Epistemic stance passage (audit C5):** late Part II, ~1 paragraph from
  bc_bedrock_working_definition.md: claims are about the organization of descriptions,
  empirically constrained by the systems described; boundary question deliberately open
  (→ 9.2.2).
- **WP-C9 — Citation label separation (audit C3):** every box distinguishes
  "Felder 2026" (paper) from pipeline/case IDs; one pass over Parts III–IV.
- **WP-C10 — Part V duplicate paragraph (audit D3):** merge the two "BC failure is not
  the end of description…" closings in the Exec Summary.

---

## Workstream D — Experiments (close the evidence gaps)

Priority order; each feeds a specific book section.

### WP-D1 — Run CASE-0005 (damped multi-pendulum, Dissipation) — **M**
Most complete pending YAML triple. First pipeline validation of any Dissipation claim
in Part V §5.2. Acceptance: go/no-go + Invariants with sweep_range; failure-direction
observations compared against Part V's two-direction prediction (basins flattening vs
deepening).

### WP-D2 — Run CASE-0008 (pitchfork normal form, Symmetry Breaking) — **M**
Cheap to run; validates the hysteresis/topology-change signature — and is the natural
candidate to supply the missing empirical showcase for regime boundary vs. descriptive
crossover (WP-A1's vacated slot): the pitchfork has both a true bifurcation point and
steep-gradient flanks.

### WP-D3 — Φ_obs test: same system, two observables (audit B5; Q_NEW_9/Q_NEW_11) — **M**
CASE-0001 with r_ss vs σ²(θ) (or χ): the single most valuable experiment for the
book's core claims. Outcome either grounds the Φ_obs × Φ_sys decomposition or shows
observable-BC dominates — both publishable in Part VI/VII.
- Note: use transfer_v2 (overlap PCI) only; v1 results inadmissible.

### WP-D4 — Run CASE-0007 (SIR, Aggregation) — **M, optional before book**
Second emergence/aggregation anchor (WP-C5's one-case caveat); also the SIR
mini-decision from plan v3 §2 resolves itself once real data exist.

After D1+D2: update Part V with an epistemic-status table (which signatures
validated/derived/conjectured) — the audit's B2 solution 1.

---

## Workstream E — New material that converts attack surfaces into content

### WP-E1 — Meta-falsification conditions (audit C1) — **M**
Draft Part IX §9.4 material now: (a) BC classes indistinguishable under all
constructions incl. operator signatures → taxonomy loses content (Q-REL-05);
(b) within-class partition-type transfer fails under controlled conditions → central
hypothesis falls (Q5); (c) taxonomy classifications unstable after careful analysis →
framework at its own scope boundary, framed as risk not just diagnostic.
Written early, this disciplines all intermediate drafting.

### WP-E2 — Self-application page (audit C4) — **M**
One worked page: the taxonomy's own scope tuple (B = finite class inventory,
Π = structural-mode classification, ε = class-resolution, Δ = invariance under
re-description), and what its F1/F2 failures would look like. Placement: end of
Part III (replacing the rhetorical paragraph) or Part IX; recommend Part III for
maximum effect.

### WP-E3 — Σ-comparison / forward-derivation section (audit B6) — **L**
The α = 1/(β−1) theorem (bc_signature_forward_derivation.md, verified) is the strongest
unused material in the programme: operator structure → cover geometry. Build §6.4–6.5
around it (per WP-A3 framing): partition metrics as necessary condition, signatures as
the locus of the structural claim, with the honest statement that a general Σ-comparison
metric is the open frontier (Q-REL-05). Gate: requires WP-A3 decision.

### WP-E4 — Related-fields comparison (audit C2) — **L**
Begin Part IX §9.3 as a working document now (not prose): per field — early warning
signals, RG/coarse-graining, bifurcation theory & universality, DSGRN (Q16), TDA (Q4),
Kuhn, distribution shift — one paragraph: what they claim, what ARW shares, what ARW
adds. Output feeds two places: §9.3 and the Introduction's novelty sentence
("nobody's question" → "nobody's general question" or better, informed by the table).
Claude can draft the comparison table from literature_links.md + web research; Rico
arbitrates the "what ARW adds" column.

---

## Workstream F — External read-through findings (added 2026-06-11)

Source: external critical read-through of all seven drafts (Introduction–Part VI),
2026-06-11. The read confirms the audit's repairs are landing (θ* discipline,
evidence-status markers, R(π)/Z(π) first-definition all noted as working; the
Part III correction box and the §6.3 Φ-as-filter turn singled out as the
manuscript's strongest pieces). Five new items, in plan style:

### WP-F1 — Intro part-count drift ✅ *(fixed 2026-06-11)* — **S**
Introduction said "the argument develops across eight parts" while Parts II, III
and V reference Part IX; plan v3 has nine parts (I–IX). Fixed: "eight" → "nine".

### WP-F2 — Intro reading paths: VI/VII swapped ✅ *(fixed 2026-06-11)* — **S**
Introduction had "Parts I through V and Part VII are narrative … Part VI deepens
concepts formally and is optional" — inverted relative to plan v3 and the drafts
(VI = Transfer, narrative; VII = formal deepening, optional). Fixed by minimal swap:
"Parts I through VI are narrative … Part VII deepens concepts formally and is
optional." (Part VIII deliberately not added to the no-prerequisites list: per
plan v3 it builds on V *and* VII; how VIII routes for the narrative path is a
4c/4d question.)

### WP-F3 — 5+1 structure: canonical first-mention ✅ *(executed 2026-07-14)* — **S–M**
The 5+1 structure (Restriction as meta-operator) is introduced with slightly
different claim levels in Part III §3.1, Part III §3.3 closing, Part V Exec
Summary, and again in V §5.1/§5.4 — by the third occurrence it reads as
established although it is officially open (Part IX §9.1). Fix: declare
**Part III §3.1 the canonical first-mention** (now correctly hedged after WP-C2);
reduce the Part V Exec Summary paragraph and the §5.1/§5.4 restatements to brief
back-references ("the 5+1 reading introduced in Part III §3.1, developed in
Part IX"). Add to the K-conventions as **K7: the 5+1 structure has one canonical
introduction; all other mentions are back-references with uniform hedging.**

### WP-F4 — Style variation pass (anaphora fatigue) — **M, revision-phase task**
The "Not X. Not Y. What changed is Z" construction and the "This is what the
framework calls…"-introduction formula are individually effective but cumulatively
predictable across Parts III–V. Target: vary roughly a third of the instances.
Schedule: with the Phase 4 revision (plan v3 4c/4d), not before — content edits
first, prose rhythm last. Grep-able starting inventory: "This is what the
framework calls", "What changed is", "Not because".

### WP-F5 — Part V: condensed signature schema after §5.2 ✅ *(executed 2026-07-14)* — **M**
Twelve worked scenarios (six classes × two directions) plus masking patterns
produce example fatigue even though each is individually good. Fix: add a
compact signature table at the end of §5.2 — per class × direction: onset
trajectory, observable footprint, formal failure mode, successor scope —
so the diagnostics condense into one retainable schema and the scenarios
become optional depth rather than required reading. (This also gives Part VIII
and the concept register a reusable artifact.) Source for the table:
`docs/bc_taxonomy/bc_failure_signatures.md` + the §5.2 text itself.

### Reinforcements of existing packages (no new WPs)
- **WP-E4 (related fields)** — upgraded from "begin early" to **load-bearing**.
  The read names the occupied neighbourhood precisely (critical transitions /
  early-warning signals, model validation & domain of applicability, Cartwright,
  Pearl/Bareinboim transportability for Part VI, Kuhn/Wittgenstein) and supplies
  the differentiation answer the book should state frontally rather than in CITE
  comments: (a) the unification itself is the contribution — no neighbouring
  field treats description validity cross-domain as its own object (the Intro's
  "nobody's question" diagnosis, properly qualified); (b) ARW is **falsifiably
  instrumented** — σ_Δ/ε conditions, F-categories and transfer metrics run
  through a pipeline that has already killed its own claims (E_sep, v1-Φ
  ordering), which separates it categorially from purely philosophical frame
  theories. Both arguments go into WP-E4's deliverable (Part IX §9.3 + Intro
  novelty sentence).
- **WP-D1/D2/D3 (experiments)** — reconfirmed as *book defense*, not just
  research: the gap between two pipeline-validated systems and the narrative
  reach (schools, markets, constitutions, wards) is the named target for
  critique; every additional BC-class case narrows it.

---

## Sequencing and gates

| Phase | Packages | Gate |
|---|---|---|
| **R1 — Stop the bleeding** | WP-A1, WP-A2, WP-B1, WP-C10 | — |
| **R2 — Decisions** | WP-A3, WP-A4, WP-B3 (Rico) | **G1:** No §6.4–6.5 drafting before WP-A3 decided |
| **R3 — Consistency pass** | WP-A4 exec, WP-B2, WP-B4, WP-C1–C9 | **G2:** No Part VII drafting before WP-B2 + WP-B3 done |
| **R4 — Evidence build** | WP-D1, WP-D2, WP-D3 (parallel to R3 possible) | **G3:** Part V epistemic-status table requires D1+D2 |
| **R3b — Read-through patch** | WP-F1 ✅, WP-F2 ✅, WP-F3 ✅ (2026-07-14: Part V Exec Summary + §5.1 + §5.4 reduced to hedged back-references to III §3.1 per K7), WP-F5 ✅ (2026-07-14: 12-row class×direction schema — onset, footprint, formal mode, successor scope — added at end of §5.2 with diagnostic reading order; feeds Part VIII + register) — **R3b complete** | — |
| **R5 — Conversion writing** | WP-E1, WP-E2, WP-E3, WP-E4 (now load-bearing); then §6.4–6.5, VII, VIII, IX per plan v3 phases 3–4 | — |
| **Phase-4 carry-over** | WP-F4 (style variation pass) with plan v3 4c/4d | — |

**Decision points for Rico — SETTLED 2026-06-10:**
1. WP-A3: Part VI framing → **(a)** (partition compatibility as necessary condition;
   Σ grounds the structural claim). Executed: §6.3 ending rewritten. *Canonical record:
   `decision_note_WP-A3_transfer_reframing_2026-07-02.md` (restatement of this settlement,
   confirmed one decision event 2026-07-14).*
2. WP-A4: SDI → **graph edit distance** (canonical doc + pipeline confirmed identical;
   context-map plateau-width entry was drift). Executed: context map corrected,
   skill patch staged (Simulationen/arw-repo-context_SKILL_patched.md).
3. WP-B3: X-structure → **ART layer**. Executed: Q_NEW_1 answered by decision;
   canonization rides with WP-B2 (scope.md note) and Part VII V1.
4. (Carry-over from plan v3) SIR running-example mini-decision — defer until WP-D4.

**Phase status:** R1 ✅ (2026-06-10) · R2 ✅ (2026-06-10) · R3 next
(WP-B2 INC-01 + epsilon doc, WP-B4 plan sync, WP-C1–C9 bundle) · gates G1 open,
G2 closed until WP-B2+B3-canonization, G3 awaiting D1+D2.

**Suggested session plan:**
- Session 1: decisions (1–4 above) + WP-A1 draft review.
- Session 2: WP-A2, WP-B1, WP-C10 + repo pass start (WP-A4 exec, WP-B4).
- Session 3: WP-C1–C9 bundle review.
- Session 4+: experiments (D1–D3) interleaved with E1/E2 drafting.

---

*Companion to: arw_theory_audit_2026-06-10.md. Supersedes nothing; plan v3 remains the
master book plan — this document inserts as its repair phase between Phases 2 and 3
(WP-B4 records the linkage).*

---

## Maintenance Note (2026-07-11 import)

Imported into `arw-repo` from `To-REPO/` alongside its companion audit. Verified against
current repo state:

- **WP-B1** (Q-REL-04 duplicate merge) — confirmed executed; `open_questions.md` carries
  the 2026-06-10 removal note.
- **WP-B2** (INC-01, σ_Δ/ε* naming) — confirmed executed; both `docs/glossary/scope.md`
  and `docs/advanced/epsilon_and_scope_resolution.md` carry the corrected canonical content.
- **WP-A4** (SDI canon decision) — decision (graph edit distance) confirmed executed in
  `docs/bc_taxonomy/transfer_distortion_metrics.md` and
  `docs/meta/context_map/context_map_transfer_emergence_cases.md`. **The staged skill patch
  (`Simulationen/arw-repo-context_SKILL_patched.md`) was never actually merged into the live
  `arw-repo-context` skill** — this import session found the pre-patch, stale SDI definition
  still active in a skill file that had itself been revised as recently as this same week
  (2026-07-11 skill-maintenance pass), and fixed it directly in that skill rather than via
  the Simulationen staging file (which this session had no access to). If the Simulationen
  patch file still exists, it is now redundant with the fix applied directly.
- **WP-A3** — this repair plan records it "SETTLED 2026-06-10... Executed: §6.3 ending
  rewritten," but a separate, more detailed `decision_note_WP-A3_transfer_reframing_2026-07-02.md`
  restates the same decision three weeks later with additional rationale (WP-A5 proposal,
  D-CTRL specifics) and its own `decided_by`/`decision_date` front-matter. **Not reconciled
  by this import** — unclear whether the July note formalizes/supersedes the June settlement
  or is an independent second pass. Flagged for Rico rather than resolved here.
  **RESOLVED 2026-07-14 (Rico): restatement — one decision event (2026-06-10); the July
  note is its canonical, more detailed record. For WP-A3 substance cite
  `decision_note_WP-A3_transfer_reframing_2026-07-02.md`, not this plan's one-line entry.**
- Everything else in this plan (Workstreams C, D, E, F) concerns monograph drafts and
  pipeline experiments outside this repo's current visibility (no monograph source, no
  `framework_validation.md`, no `SignatureTransfer.json` found) — status of those items is
  unverified from the repo side.
