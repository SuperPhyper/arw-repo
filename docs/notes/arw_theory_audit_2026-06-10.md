---
status: note
layer: docs/notes/
---

# ARW Theory & Monograph Audit — 2026-06-10

**Mandate:** Adversarial review of (a) the theoretical foundations of ARW as documented
in the arw-repo, and (b) their presentation in the monograph drafts (Introduction,
Parts I–VI). Each finding states evidence, why it matters, and solution options.

**Severity legend:**
- **S1** — contradicts current evidence; must be fixed before any further writing on the affected section
- **S2** — theoretical gap in the core; affects what the book may legitimately claim
- **S3** — external attack surface; a hostile reviewer will raise it
- **S4** — internal consistency / housekeeping

---

## Tier 1 — Findings that contradict current evidence (S1)

### A1. Part III contains the refuted separatrix and secondary-ridge narrative

**Evidence:** Part III §3.3 boxes state E_sep = 2ω₀² ("E_sep = 2.0 J confirmed
analytically") and build an extended argument on a "secondary band at E ≈ ω₀²"
as a descriptive crossover distinct from the separatrix. The Executive Summary
repeats it ("distinguishes it from a secondary descriptive crossover at lower energy").
The 2026-06-02 re-run (kuramoto_pendulum_cover_pipeline_v2) established: **E_sep = ω₀²**
(the 2ω₀² value was a pipeline bug), and **no secondary ridge exists** — the "secondary"
band *was* the true separatrix under the wrong convention.

**Why it matters:** This is not a detail. Part III uses the two-band structure as the
flagship demonstration that the framework can *distinguish* a regime boundary from a
descriptive crossover (F-gradient). With one ridge, that demonstration collapses for
the pendulum case. The distinction itself remains valid (F-gradient is independently
grounded), but it currently has **no clean empirical showcase** in the book.

**Solution options:**
1. Rewrite §3.3 around the corrected single-ridge structure: separatrix at E_sep = ω₀²,
   self-similarity in u = E/ω₀² (CV < 1%), σ_Δ/ε = 2.0 at the separatrix. The corrected
   story is *stronger* as a Restriction example (one energy scale, not two).
2. Move the regime-boundary-vs-descriptive-crossover demonstration to a system where
   both genuinely occur, or present it honestly as a theoretical distinction with the
   refutation as a *methodological success story*: the framework's own re-analysis
   eliminated a spurious structure. That is a falsification-in-action narrative that
   fits the book's stance better than the original claim.
3. Audit all dependent text: Part III Exec Summary, §3.3 both boxes, FIG comments
   (Fig 4), Part V §5.2 Restriction (uses ω/E_sep without value — currently safe),
   Q-NEW-CROSS-1 in open_questions.md (stale reference).

### A2. Part VI's quantitative transfer apparatus rests on a metric now known to be defective

**Evidence:** Research journal 2026-06-02: v1 PCI never read per-point regime labels
and was collinear with RCD and SDI; ~90% of Φ's weight tracked regime count N.
Recomputed with real overlap: same-class PCI=0.659 vs cross-class PCI=0.650 —
statistically tied. The Φ=1.0 dissipation result was withdrawn (placeholder data +
F1-insufficient observable). Conclusion on record: "Φ is a normalised-axis
partition-overlap filter, not a BC-class metric." Part VI §6.3 presents the
four-metric composite Φ as the instrument that "summarises how admissible a scope
comparison is," and §6.1 claims failure modes across domains are "structurally
identical" — claims the current metric cannot support.

**Why it matters:** Part VI is the book's declared Alleinstellungsmerkmal. Its central
quantitative promise — transfer is *measurable* — currently outruns the evidence.
Worse, the repo's own decoupling controls (D-CTRL-1: different BC class, Φ=0.729 — not
low) actively undercut the claim that Φ detects shared BC structure. A reviewer with
repo access would consider this the single most damaging inconsistency.

**Solution options:**
1. Reframe §6.3 honestly: the metrics measure **partition compatibility**, which is a
   *necessary but not sufficient* condition for structural transfer. The discovery that
   partition-level metrics do not resolve BC class is itself a finding the book can use:
   it forces the claim (already in §6.2) that transfer is grounded in Σ (signature
   structure), not in partition resemblance. The 2026-06-02 result then *supports* the
   generator chapter instead of contradicting the metrics chapter.
2. The one robust structural signal found — directional containment 0.833 for admissible
   coarsening (D-CTRL-2) — deserves promotion: it distinguishes coarsening from genuine
   mismatch and is currently absent from the book.
3. Do not publish numeric Φ values from v1 runs (Part VI currently has none — keep it
   that way; the §6.3 TBS_norm physicist/sociologist example uses invented numbers,
   mark as stylized or replace with the real CASE-0001↔0003 value, TBS_norm=0.356).
4. Open question Q-REL-05 (does any partition-level construction recover BC-class
   distance, or must it be measured on operator signatures S1–S5?) should appear in
   Part IX as a named limitation.

### A3. Part III's Kuramoto box describes the gradient-peak method that C1/C2 invalidated at θ*

**Evidence:** Part III §3.2: instability band "identified as the peak of the observable
gradient |∂r_ss/∂κ|"; the cover-stability box reasons from gradient magnitude to
perturbation behaviour. C1 (2026-06-02) showed the pointwise gradient proxy
systematically **under-reports σ_Δ at θ*** (one-sided false negatives, up to 4.3× at a
separatrix); C2 showed it is a biased discriminant. The canonical method near
transitions is direct σ_Δ or the local-max Lipschitz bound.

**Why it matters:** The book teaches a diagnostic method in its flagship example that
the research programme has since restricted. If a reader applies the gradient-peak
recipe at a transition, they get exactly the false-stable error the C1 finding warns of.

**Solution:** Rephrase the boxes in terms of σ_Δ (perturbation spread) as the primary
quantity, with the gradient as a *bulk* proxy that is unreliable precisely at θ*. This
is also a pedagogical gain: it motivates why σ_Δ needed to be a named formal quantity.

### A4. Two incompatible canonical definitions of SDI circulate in the repo

**Evidence:** `docs/bc_taxonomy/transfer_distortion_metrics.md` (canonical layer):
SDI = graph edit distance between regime transition graphs.
`docs/meta/context_map/context_map_transfer_emergence_cases.md` and the
arw-repo-context skill: SDI = 1 − |w_A − w_B| / max(w_A, w_B) (ε-plateau-width
similarity). Part VI §6.3 follows the graph-edit-distance version.

**Why it matters:** Whatever the pipeline actually computes, one of the two documents
is wrong, and the book is anchoring prose to a contested symbol. Doc drift at exactly
the layer (transfer metrics) where Tier-1 finding A2 already lives.

**Solution:** Decide which quantity SDI names (the plateau-width quantity arguably
deserves its own symbol — it measures robustness similarity, not topology distortion);
fix the losing document; verify `pipeline/transfer.py` / `transfer_v2.py` against the
decision; then re-check Part VI wording.

---

## Tier 2 — Theoretical gaps in the core (S2)

### B1. The 5+1 taxonomy derivation is presented as settled in Part III but is a working hypothesis

**Evidence:** Part III §3.1: "This 5+1 structure is **the formal answer** to why there
are exactly six, not more and not fewer." The bedrock document
(`bc_bedrock_working_definition.md`) says the taxonomy "**may be** five fundamental
relation types plus the meta-condition," explicitly open to revision; Q11 (taxonomy
completeness) is open; the planned derivation (can Θ be derived as a boundary operator
over the five relations?) is Part IX §9.1 *future work*. Part V's Exec Summary handles
this correctly ("Whether this structure grounds a formal derivation … is the question
Part IX §9.1 takes up") — Part III does not.

**Why it matters:** "Why exactly six?" is the question every reviewer of a taxonomy
asks first. Overclaiming the answer in §3.1 and hedging it in Part V/IX gives a hostile
reader an internal contradiction to quote.

**Solution:** Align Part III §3.1 with Part V's phrasing: the 5+1 structure is the
*candidate* structural answer, developed in Part IX. One sentence fix.

### B2. The empirical discriminability of BC classes is weaker than the book implies

**Evidence:** Q5 data: at matched ε, Coupling (CASE-0001) and Restriction (CASE-0003)
produce **structurally equivalent sequential partitions** (Φ≈0.95) — "the sequential
topology appears universal for monotone observables." Q-REL-05: same-class and
cross-class pairs statistically indistinguishable in PCI once regime count is
controlled. Meanwhile only 2 of 6 classes (Coupling, Restriction) have pipeline-run
go-cases; **Dissipation, Forcing, Symmetry Breaking, and Aggregation have zero
pipeline-validated cases** (CASE-0005–0008 open). Part V presents six detailed,
two-directional failure signatures with onset-trajectory diagnostics as established
structure.

**Why it matters:** Part V's failure-signature taxonomy — the diagnostic heart of the
book — is currently supported by: two physics cases, theory, and narrative anecdotes
(research cluster, hospital ward, school district). The signatures for four of six
classes are predictions, not findings. The book's stance ("makes visible what the
reader has already encountered") partially protects the narrative claims, but the
diagnostic tables (§5.3 onset discriminants) read as validated method.

**Solution options:**
1. Add an explicit epistemic-status paragraph to Part V (and later VII/V3): which
   signatures are pipeline-validated, which are theoretically derived, which are
   conjectured. This costs little and buys credibility — it converts a hidden weakness
   into a visible research programme.
2. Prioritize running CASE-0005 (Dissipation, most complete YAML triple) and CASE-0008
   (Symmetry Breaking / pitchfork — cheap to run) before Part VII is written, so at
   least four classes have at least one empirical anchor.
3. Where Part V claims class-specific signatures, the honest formulation after Q5 is:
   classes differ in **transition position, sharpness, plateau width, and failure
   direction** — not (on current evidence) in partition topology.

### B3. The scope tuple S = (B, Π, Δ, ε) is presented as complete; four formal gaps are on record

**Evidence (all open in open_questions.md):**
- Q_NEW_1: the algebraic/topological structure of X is a precondition for observables
  but appears nowhere in the tuple.
- Q2: ε is a global scalar; σ_Δ(x) makes the *effective* requirement state-dependent;
  formal extension ε: X_B → ℝ₊ open.
- Q3: multi-observable scopes need an ε-vector — empirically forced (CASE-0003: 37%
  agreement across ε; no shared ε satisfies var_rel and lambda_proxy). The admissible
  region in ℝᵏ is box-approximated; cross-observable constraints open (Q-NEW-COVER-2).
- Q_NEW_18: joint-BC separation conditions (diagonal cover contours in CASE-0002 κ×γ)
  are not expressible as product conditions Δ₁ × Δ₂; whether the formalism permits
  joint constraints is open.

Additionally, Part II's identification of the *frame* with the sub-tuple (B, Π, ε) —
excluding Δ — is asserted, not argued.

**Why it matters:** Part VII (V1) will be written from `docs/glossary/scope.md`, which
itself still awaits the Čech-cover upgrade (INC-01, open since 2026-04-29). Writing the
formal chapter from a lagging canonical doc bakes the drift into the book.

**Solution:** Before Part VII: (1) close INC-01 in the repo; (2) decide and document
whether X-structure lives in B, a meta-layer, or ART (Q_NEW_1 needs a *decision*, not
a solution — any consistent choice works); (3) Part VII should present ε-vector and
state-dependence as scoped extensions with the empirical motivation from CASE-0003;
(4) either justify Δ's exclusion from the frame sub-tuple (Δ is the *test* of the
frame, not part of what makes descriptions accessible — that argument is available)
or drop the sub-tuple claim.

### B4. Part II teaches the naive ε-equivalence that Felder 2026 corrected

**Evidence:** Part II §2.3: "Below the threshold ε, two states are treated as the same."
Pairwise ε-indistinguishability is not transitive (sorites): chains of sub-ε steps
connect arbitrarily distant states, so "treated as the same" does not yield a
well-defined partition. The Čech-cover construction (path-connected components of the
observable cover) is precisely the repair — and is the formal basis of the empirical
boxes Part III already cites (cover counts, cover stability).

**Why it matters:** The book's narrative definition of its most important parameter is,
strictly read, the version the research programme already falsified. A mathematically
literate reader hits this in Part II and discounts everything after.

**Solution:** Part II does not need the formalism, but needs one honest paragraph:
the naive "same below ε" picture has a known defect (chains), and the working
definition is "zones that hold together at resolution ε" (cover components), formally
developed in Part VII. The map-scale metaphor survives intact.

### B5. Whether BC class is a system property or a scope property is unresolved — and Part IV builds on the unresolved reading

**Evidence:** Q_NEW_9 (open, flagged "foundational for the BC taxonomy program"):
r_ss is Restriction-dominated regardless of system; if BC class is a scope property,
BCManifest needs separate system_bc/observable_bc and Φ decomposes into Φ_obs × Φ_sys
(Q_NEW_11, unimplemented; the one data point — Φ=0.9 across different systems *and*
observables — motivates but does not resolve). Part IV §4.4 asserts the observable-BC
construction "is not a metaphor" and Part VI's generator chapter quietly assumes the
system side (Σ as property of the generator).

**Why it matters:** If BC classification is scope-relative all the way down, then
"two systems share BC class" — the foundation of the transfer claim — is not yet a
well-defined predicate. This is the deepest open conceptual issue in the framework.

**Solution:** The book can survive this by *placing* the question rather than hiding
it: Part IV already has the material (observable BC structure ≠ system BC structure);
add the explicit statement that the decomposition is an open research question with a
designed test (same system, two observables: r_ss vs σ²(θ) on CASE-0001). Running that
test is also the single most valuable experiment for the book's core claims.

### B6. The generator formalism (Part VI §6.2) is presented with more confidence than its formal status supports

**Evidence:** G = (Λ, Σ, φ, C) is partially formalized: topology conditions on Λ per
collapse type open (Q-GEN-03); exhaustiveness of the three collapse types open
(Q-GEN-01: non-autonomous generators may produce uncaptured geometries); no
signature-first protocol for Type III (Q-GEN-02); minimal C for non-empty A_f open
(Q-GEN-04). There is no defined procedure for *comparing* Σ across two generators —
yet Σ-sharing is declared "what grounds the transfer claim" (§6.2 closing).

**Why it matters:** After A2, Σ carries the entire weight of the transfer argument.
A reviewer will ask: how do I determine Σ for a given system, and how do I check two
Σ are "the same"? The current answer (operator signatures S1–S5, signature-first
documents) exists in the repo but is not yet a defined comparison procedure — and
Q-REL-05 explicitly asks whether BC-class distance must be measured on S1–S5 because
partitions won't do it.

**Solution:** Either (1) Part VI §6.4/6.5 (unwritten) deliver the Σ-comparison story —
the forward-derivation result (α = 1/(β−1) theorem, bc_signature_forward_derivation.md)
is the strongest available material: operator structure → cover geometry is a real,
verified derivation and currently appears nowhere in the book; or (2) §6.2 downgrades
to "Σ is the structural locus of the transfer claim; its comparison metric is the open
frontier" — and Part IX owns it.

### B7. The emergence account rests on a single empirical case

**Evidence:** Part IV §4.5 presents range-filling as "the mechanism behind what we call
emergence." Empirical basis: CASE-0004 (Stuart-Landau, emergence window ε ∈ [0.082, 0.805])
— one case, one BC class, with Δ-robustness breaking at λ > 1.3 for weak K. Q10
(emergence: ontological or epistemic?) deliberately open.

**Solution:** Keep the account, scale the claim: "the mechanism" → "the structural
account ARW gives" + the one-case status stated. CASE-0007 (SIR, Aggregation) would
provide the needed second instance in a different class.

### B8. The Introduction promises ex-ante detection; no validated ex-ante method exists

**Evidence:** Introduction: the crossing "could, in principle, be identified before it
occurs." Q7 (unsupervised scope-transition detection without ground truth) open;
Q1 (admissibility as continuous measure) open; the pre-failure signatures in Part V
(growing σ_Δ near threshold) are theoretically motivated and demonstrated post-hoc on
known systems only.

**Why it matters:** "In principle" carries the sentence, but the gap between
"classifiable after the fact" and "detectable in advance" is exactly where critical-
transitions research (early warning signals) spent fifteen years and accumulated known
failure modes (false positives, transitions without warning). The book should not
imply it has solved what that literature shows is hard.

**Solution:** Keep "in principle," add the demarcation in Part V or IX: ARW's claim is
that the *conditions* of failure are specifiable in advance (the scope can be audited),
not that the *moment* of failure is predictable. That distinction is defensible and
genuinely differentiating.

---

## Tier 3 — External attack surfaces (S3)

### C1. Falsifiability of ARW itself

The falsification schema (F0–F4, F-gradient, Z_shared) classifies failures *within*
the framework. An adversarial reviewer will note that every predictive failure has a
reclassification available (wrong observable → F0; wrong resolution → F1; too steep →
F-gradient; transition zone → Z_shared) — an immunization structure in Popper's sense.
The framework needs a stated meta-falsification condition: what pattern of outcomes
would count against ARW *as such*? Candidates already exist in the repo and should be
surfaced: (a) if BC classes proved empirically indistinguishable under *all*
constructions including operator signatures (Q-REL-05 fails), the taxonomy loses
content; (b) if predicted partition types failed to transfer within-class under
controlled conditions (Q5 fails), the central hypothesis falls; (c) Part III's own
underdetermination criterion (taxonomy yields unstable classifications after careful
analysis) — currently framed as "diagnostic," it should be framed as *risk*. Part IX
§9.4 is the natural home. The book gains credibility by stating these; it loses
credibility if a reviewer states them first.

### C2. Novelty and demarcation from existing fields

The Introduction's "it is nobody's question" overstates. Adjacent claims exist and the
book currently engages none of them in the drafted parts: critical transitions / early
warning signals (Scheffer, Dakos — cross-domain transition structure with generic
indicators); renormalization and coarse-graining (resolution-dependence of effective
descriptions is the *founding* insight of RG); bifurcation theory and normal forms
(the "same structure across systems" phenomenon has a canonical explanation:
universality classes); DSGRN (Q16 — parameter-space partition into regions of
identical qualitative dynamics, structurally the closest existing object to an ARW
regime partition); TDA/persistent homology (Q4 — the Čech cover *is* their object);
Kuhn (frames becoming visible at failure); model-validity / extrapolation /
distribution-shift literatures in statistics and ML. ARW has genuine differentiators
(the scope tuple as audit object; observable-BC structure; the falsification schema
as engineering practice) — but they only become visible *against* this background.
Part IX §9.3 must be written as a serious comparison, not a courtesy list; the
Introduction's strongest sentence should be weakened from "nobody's question" to
"nobody's *general* question" or equivalent.

### C3. Evidence base and self-citation structure

The formal load rests on Felder 2026 (the author's own paper — publication/peer-review
status should be stated somewhere); all empirical results are self-generated
simulations; four go/pending cases total; no external replication. The boxes in
Part III attribute pipeline results to "(Felder 2026)" — blurring what is in the paper
versus what is repo-internal analysis. Recommendations: (1) separate the citation
labels (paper vs. pipeline/case ID) in every box; (2) state the evidence-base scope
once, plainly, in the Introduction or Part IX ("the empirical programme is young; the
cases are chosen for structural diversity, not statistical weight"); (3) the planned
DSGRN dialogue and any external-system case (CASE-0010 school system) are the cheapest
routes to non-self-referential evidence.

### C4. The reflexivity move is currently rhetoric; it could be a result

Part III closes: the framework applying to itself is "the strongest form of internal
consistency the framework could demonstrate." A reviewer will answer: self-application
is only *consistent*, not *demonstrated*, until you actually do it. The fix is to do
it: one worked page — what is the taxonomy's own B (finite class inventory), Π
(structural-mode classification), ε (the resolution at which two organising conditions
count as the same class), Δ (what perturbations of a system description must leave the
classification invariant), and what its F1/F2 failures would look like (Part III
already names the F1 analogue: classifications unstable under careful analysis).
This converts the book's most attackable paragraph into one of its most distinctive.

### C5. Epistemic/ontic wavering in the narrative voice

Part I narrates ontically ("systems jump," "the zone ended"); Part II defines regimes
as properties of descriptions at a resolution; the bedrock document is explicitly
description-relative and anti-constructivist — but that stance statement appears
nowhere in the drafted text. Q9 (scope vs. phase transitions) and Q10 (emergence)
are the formal residue of the same unresolved positioning. The book does not need to
solve the realism question; it needs one explicit passage (late Part II is the natural
place) stating the commitment: ARW makes claims about the organization of descriptions,
including the claim that this organization is empirically constrained by the systems
described — and the boundary question is held open deliberately (→ Part IX 9.2.2).
Without that passage, Part I reads as realism and Part II as constructivism, and
reviewers will choose whichever reading is easier to attack.

### C6. Stylized quantitative detail in narrative examples

The pandemic mortality figures (2% / 0.4% / 8%), the BMI threshold discussion, and the
§6.3 physicist/sociologist TBS numbers are invented or composite. Within the book's
stance this is legitimate *if marked*. A single footnote convention ("numerical values
in narrative examples are stylized unless tied to a case ID") protects every instance
at once. The BMI passage additionally makes empirical claims (variance behaviour
across populations) that should either get a real citation or be softened.

---

## Tier 4 — Internal consistency and housekeeping (S4)

**D1. Part VI is half-drafted but the plan marks it ⬜.** §§6.4–6.5 are announced in
§6.1 and §6.3 but absent. The action plan v3 predates the draft. Update plan status;
note that §6.4's promised content ("Φ measures observable transfer, not system
transfer") is exactly where the A2 reframing must land — write 6.4 *after* deciding A2.

**D2. Pointer drift persists despite Phase 0d being marked ✅.** Verified instances:
Part III §3.5 says the formal account of failure is "developed in Part VI" (should be
VII; narrative is V itself). Part II's CITE comments systematically target
"Part VI, V1/V2/V3/V6" for the formal treatment (lines 77, 80, 285–287, 374, 398–399,
447 — all should be Part VII per K4), and Part II §2.4 points scope-transition
detection to "Part VII (Error Forms)" (Error Forms = Part VIII per the plan).
One full K4 sweep needed before transitions are written.

**D3. Missing apparatus.** Parts VII–IX unwritten; all inter-part transitions are
placeholders; concept register absent; Part V Exec Summary contains two near-duplicate
closing paragraphs ("BC failure is not the end of description…" appears twice) — a
visible editing seam.

**D4. open_questions.md contains two contradictory Q-REL-04 entries** (one "answered —
structural break," one "open") and Q-NEW-CROSS-1 still cites the refuted secondary
ridge. The auto-memory likewise says "Q-REL-04 open" while the journal says answered.
Reconcile in the repo first, then memory.

**D5. Numeric tension between Part III's Kuramoto boxes.** Text box: empirical
instability band at κ/σ ≈ 1.49 (pipeline metadata 1.485); Fig-8 comment: σ̄_Δ peak at
κ_c1/σ ≈ 1.60 with secondary at 1.55. If both figures are produced as commented, the
chapter will display two different "empirical" critical values without explanation.
Decide which dataset the figure shows and add the finite-N reconciliation explicitly.

**D6. Repo canonical docs lag the canon used by the book** (also B3): scope.md
(INC-01, Čech upgrade), epsilon_and_scope_resolution.md (σ_Δ naming, ε*) — both flagged
"still open" since 2026-05-20. Part VII must not be drafted from these until they are
updated, or the book will canonize the stale versions.

---

## Priority repair sequence (proposal)

1. **A1 + A3** — rewrite Part III §3.3 (corrected separatrix) and §3.2 boxes (σ_Δ-first
   method). Self-contained; nothing else depends on the old text.
2. **A2 decision** — choose the Part VI reframing (partition compatibility as necessary
   condition; Σ as locus of the structural claim) *before* writing §§6.4–6.5.
3. **A4 + D4 + D6** — repo consistency pass (SDI, Q-REL-04 duplicate, INC-01,
   epsilon doc). Cheap; blocks Part VII otherwise.
4. **B1, B4, B7, B8** — claim-strength corrections in Parts II–IV (each ≤ 1 paragraph).
5. **B2 experiments** — run CASE-0005 and CASE-0008 before Part VII; run the
   same-system/two-observable Φ_obs test (B5) when feasible.
6. **C1 + C4** — draft the meta-falsification conditions and the self-application page
   as Part IX §9.4 material now, while the points are fresh; they also discipline
   everything written in between.
7. **C2** — begin the related-fields comparison (9.3) early; it will change how the
   Introduction's novelty claim is phrased in revision.

---

*Audit basis: monograph drafts introduction + Parts I–VI (v1, states of 2026-05-28/30),
action plan v3, bc_bedrock_working_definition.md, arw-repo open_questions.md,
repo_weakpoints.md, research_journal.md (through 2026-06-02),
transfer_distortion_metrics.md, context maps, and session memory of the transfer-metric
and separatrix findings.*

---

## Maintenance Note (2026-07-11 import)

Imported into `arw-repo` from `To-REPO/` at Rico's request, as the companion this audit's
sibling repair plan (`arw_audit_repair_plan_2026-06-10.md`) and the later
`decision_note_WP-A3_transfer_reframing_2026-07-02.md` both point to. Cross-checked against
current repo state on import:

- **A1 (separatrix)** — confirmed already fixed at the pipeline/doc level (E_sep = ω₀²,
  no secondary ridge) per `arw-repo-context` skill maintenance history 2026-06-02 and
  `docs/core/cover_stability_criterion.md` §10.2/10.4. Whether the *monograph* text itself
  (Part III) was corrected is outside this repo's visibility — monograph drafts are not
  present in `arw-repo` or connected folders.
- **A2/A4 (Φ framing, SDI)** — A4's SDI finding is confirmed still relevant: this import
  session found the exact same stale SDI definition (`1 − |w_A−w_B|/max(w_A,w_B)`) still
  present in a recently-updated `arw-repo-context` skill file, over a month after the
  context map itself was corrected (2026-06-10). Fixed in that skill on import of this note.
- **D6/B3 (INC-01, σ_Δ naming)** — confirmed **closed**: `docs/glossary/scope.md` already
  has the Čech-cover / observable-cover construction (dated 2026-06-10 in-doc), and
  `docs/advanced/epsilon_and_scope_resolution.md` already formally names σ_Δ and ε*(O,X)
  (Felder 2026 Definition 4). D6/B3 were live concerns at audit time; both are resolved now.
- **D4 (duplicate Q-REL-04)** — confirmed already resolved; `docs/notes/open_questions.md`
  records the merge under a 2026-06-10 removal note.
