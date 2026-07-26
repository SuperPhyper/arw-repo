---
status: superseded
layer: docs/advanced/
date: 2026-06-02
related_cases:
  - CASE-20260311-0001
  - CASE-20260311-0002
  - CASE-20260311-0003
  - CASE-20260318-0004
related_docs:
  - docs/glossary/observable_range.md
  - docs/bc_taxonomy/transfer_distortion_metrics.md
  - docs/advanced/observable_decomposition.md
  - docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md
  - docs/notes/arw_theory_audit_2026-06-10.md
---

> **⚠ SUPERSEDED — imported 2026-07-11 for the historical record only.** This document's
> central claim (§2.6/§3: a "Strong (confirmed, pre-registered)" result for
> CASE-0004 ↔ CASE-0001, Φ = 0.9983) is contradicted by the repo's own `transfer_v2`
> recomputation of the identical pair, generated the same day (2026-06-02) this document
> is dated:
>
> `cases/CASE-20260318-0004/transfer_v2/CASE-0004_vs_CASE-0001/TransferReport_v2.md`:
> **Φ (v2) = 0.7794 → `ambiguous_requires_inspection`** (not `highly_admissible`); real
> overlap PCI = 0.659 (`partial_compatibility`), not ≈1; explicit flag on record:
> *"N_CONFOUND: regime counts equal → legacy v1 Phi was inflated by count match; trust
> PCI_real for true overlap"* and *"COMPONENT_DISAGREEMENT: real-overlap PCI and topology
> term diverge by >0.3 — single Phi is not a faithful summary."*
>
> In other words: the "Strong" confirmation this document reports was an artifact of the
> v1 PCI defect (structural proxy collinear with regime count) that the 2026-06-02
> transfer-metric rigour pass identified and fixed elsewhere the same day. §3.5 of this
> document itself flags the adjacent tension (CASE-0001↔CASE-0003, a *different* BC class,
> already showing high Φ) as "the most interesting part" of an open puzzle — the later
> Q-REL-05 finding resolves that puzzle negatively: Φ does not reliably discriminate
> BC-class distance at all (same-class vs. cross-class pairs statistically tied on real
> overlap PCI). See `docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md`
> ("Pending" section) for the explicit requalification/downgrade instruction this
> document was already flagged for before it was located and imported.
>
> Kept in full below, unedited, for the historical record — this is what the framework
> validation chapter claimed before the metric defect was understood. Do not cite the
> §2.6/§3 "Strong" result, the Φ=0.9983 figure, or the pre-registration falsifier logic
> in §3.4 as current evidence. The hardness-ladder methodology in §1 and most of the
> Medium-level ledger entries in §2 (2.1–2.5) are not directly affected by the PCI defect
> and may still be useful framing — but were not independently re-verified on import.

---

# Framework Validation: What ARW Has Risked, and What It Has Confirmed

This chapter does two things. First, it audits the evidence ARW has already
produced and sorts it by *epistemic hardness* — distinguishing mere coherence
from retrodiction from genuine prediction. Second, it reports one pre-registered
strong test (CASE-0004 ↔ CASE-0001) whose prediction was locked before
measurement and whose outcome confirmed a central structural claim of the
framework — together with the one further test (a different-BC-class control)
still needed before that claim hardens from a confirmed endpoint into an
established metric.

The organising principle is deliberately conservative: a framework is not
validated by running its pipeline to completion, nor by describing many cases
without contradiction. It is validated when it is forced to commit to a
statement that could have come out otherwise, and the statement holds.

> **Note on levels (ARW vs ART).** §1–§2 make ARW-level claims about scope
> structure, observable range, and transfer. The supporting evidence is drawn
> from ART-level case instantiations (CASE-0001 through CASE-0004). The two
> levels are kept in separate subsections; case data is cited by Case ID, not
> inlined as if it were framework-level fact. The strong result in §3 is an
> ART-level measurement (CASE-0004 ↔ CASE-0001 transfer) confirming an ARW-level
> prediction (hierarchical signature factorisation); the two are kept distinct.

---

## 1. The Hardness Ladder

Validation claims are not interchangeable. We grade every result against three
levels, and we label each result in the ledger with the level it actually
reaches — not the level we would like it to reach.

| Level | What it requires | Failure mode it rules out |
|---|---|---|
| **Weak — Coherence** | The framework describes the case consistently, without internal contradiction. | Internal incoherence. |
| **Medium — Retrodiction** | The framework explains an *already known* phenomenon more sparsely or more precisely than the standard account. | Redundancy (the framework adds nothing). |
| **Strong — Prediction** | The framework commits, *before measurement*, to an outcome that was not already known, and the outcome occurs. | Post-hoc fitting (the framework only ever explains what already happened). |

A monograph that stops at Weak is a vocabulary. One that reaches Medium is an
explanation. Only Strong-level results make ARW a *theory* in the sense that
matters to a critic — something that took a risk and survived.

---

## 2. Evidence Ledger (existing results)

Each entry states the result, its hardness level, and — critically — the honest
limitation that a reviewer would raise.

### 2.1 lambda_proxy insufficiency — *Medium, approaching Strong*

**Result.** lambda_proxy was derived to be *structurally* insufficient as an
observable from first principles: pre-scopal assumptions A6.1 and A6.2 (finite
integration time, finite initial separation) are violated by the proxy's own
construction, independent of any data. This derivation was made, and *then*
empirical insufficiency was found independently in **two** systems
(CASE-0002 and CASE-0003).

**Why it is strong.** The order matters: derivation preceded the two-system
confirmation. This is the closest existing result to a genuine prediction —
the framework said "this observable must fail for reasons internal to its
definition," and the data agreed in systems of different BC structure.

**Reviewer's objection.** The empirical insufficiency in CASE-0002/0003 was
observed in the same research programme that produced the derivation; a sceptic
will ask whether the derivation was reverse-engineered from the observation.
The defence is the first-principles character of the A6.1/A6.2 argument, which
does not reference any sweep data. This defence is strong but should be made
explicit in the text, not assumed.

### 2.2 F0 at θ* in CASE-0001 — *Medium*

**Result.** The collapse at θ* ≈ 1.475 in CASE-0001 was diagnosed as an
*observable-range* failure (F0), not a physical regime boundary: r_ss
simultaneously violates five pre-scopal assumptions in the exclusion zone
Z(r_ss). The framework forced a distinction — "the partition reflects observable
collapse, not a regime in the system" — that the naive reading (a regime
boundary at θ*) would have missed.

**Why it is medium, not strong.** This is retrodiction of high quality: it
re-explains an already-visible feature more correctly than the default reading.
It does not predict a *new* feature. Its value is parsimony and correctness, not
surprise.

### 2.3 F-gradient at the pendulum separatrix — *Medium*

**Result.** After the E_sep convention bugfix (2026-06-02), the conservative
pendulum exhibits a single Restriction boundary at E_sep = ω₀², carrying an
F-gradient signature (σ_Δ/ε ≈ 2.0): the observable is within its range R(π)
everywhere, but its gradient is too steep for the chosen ε at the separatrix.
This is correctly classified F-gradient, not F0 (the substrate A0–A6 is sound)
and not Z_shared.

**Why it is medium.** The framework's falsification taxonomy correctly *placed*
a real feature in the right category, distinguishing three failure modes that a
coarser account would conflate. Diagnostic precision, not prediction.

### 2.4 The bugfix self-similarity check — *Medium, with a caveat that must be stated*

**Result.** The corrected pendulum model predicts that frequency is a function
of the single reduced variable u = E/ω₀² (one energy scale, not two). The
measurement confirmed this: f/ω₀ at fixed u varies by CV < 5 % across
ω₀ ∈ [0.6, 1.8] up to u = 0.9, and cover_height_p2_ratio fell from 33.5
(buggy) to 5.1 (corrected). The field is now nearly self-similar in ω₀.

**The caveat — this is the Class A / Class B distinction.** The vanished
"secondary ridge" must not be sold as evidence that *legitimate* descriptions
collapse onto simpler classes under Δ-stabilisation. The secondary ridge was a
**Class A artefact** — a hard-coded physical constant was wrong (E_sep = 2ω₀²
instead of ω₀²). Removing it corrected the physics; it did not demonstrate a
description-attractor. The self-similarity *prediction* of the corrected model
is sound Medium-level evidence. But the disappearance of the ridge is a
bugfix, not a validation of the epistemic-attractor thesis. Conflating the two
invites exactly the objection "you fixed a typo and called it a theorem."

> **Class A (artefact):** structure that never existed — wrong physics or wrong
> code. Its removal is a correction.
>
> **Class B (description attractor):** redundant structure in a *legitimate*
> description that disappears under Δ-stabilisation, collapsing to a simpler
> admissible class. Its removal is evidence for the epistemic reading of BC
> classes.
>
> The pendulum case is Class A. The epistemic-attractor thesis needs a Class B
> demonstration — see §3.

### 2.5 Matched-ε transfer, CASE-0001 ↔ CASE-0003 — *Medium*

**Result.** Raw Φ = 0.40 rises to Φ ≈ 0.95 once ε is matched between the two
scopes. This supports the framework's claim (session 2026-03-18) that Φ measures
*observable* transfer, not *system* transfer: the apparent low compatibility was
a resolution-coordinate artefact, not a structural mismatch.

**Why it is medium.** It confirms an interpretive claim about what Φ measures.
It is also the conceptual seed of the strong test in §3: it shows that
class-level compatibility can be masked by an ε-coordinate difference, which is
precisely what the factorisation hypothesis predicts.

### 2.6 Same-BC-class cross-system transfer, CASE-0004 ↔ CASE-0001 — *Strong (confirmed, pre-registered)*

**Result.** A prediction was registered on 2026-06-02 — *before* CASE-0004's
transfer artefacts were finalised — that two same-BC-class systems (Kuramoto and
coupled Stuart-Landau, both Coupling) would show Φ_matched ≥ 0.85 at matched ε,
with a falsifier at Φ_matched < 0.60. The measured result was Φ = 0.9983
(highly_admissible): identical regime count (N=4), identical linear adjacency
(3 edges), TBS_norm = 0.008, ε matched at 0.09 in both scopes (so Φ_raw =
Φ_matched). **Prediction confirmed.**

**Why it is genuinely strong — and why the strength is not the high Φ.** The
load-bearing fact is *where* the homology survives. The two scopes use observables
with **opposite primary BC structure**: PLV on CASE-0004 is Coupling-dominated
and relational (C·A·R); r_ss on CASE-0001 is Restriction-dominated and collective
(R³·A·D). These are not merely "different observables" — they diverge maximally at
the observable layer. Yet the partition is conserved: same N, same adjacency
topology, near-zero normalised transition shift. The classical reading (transfer
works because the *systems* are similar) predicts the observable divergence should
propagate; it does not explain conservation across the layer where the two
descriptions are least alike. The ARW reading (transfer tracks *partition*
homology, not system similarity) predicts exactly this. The result therefore moves
weight onto the ARW reading in a way a high Φ between similar observables could not.

**The three caveats that must travel with this result.**

1. *One endpoint is not a metric.* The hierarchical factorisation claims a
   *monotonicity* — d_BC increases ⇒ Φ decreases. This result is a single point
   at d_BC = 0. It confirms the endpoint; it does not establish the slope. A
   different-BC-class control (d_BC > 0 with measurably lower Φ) is required before
   "signature distance predicts transfer" is a metric rather than a confirmed
   special case. Two distinct d_BC values would be better still, to show the fall
   is graded, not binary. This is the open follow-up in §3.4.
2. *PCI is a structural approximation, and it carries the most weight.* The
   TransferMetrics report flags PCI as a structural approximation reconstructed
   from N and adjacency, not from label-aligned annotated regimes — and PCI has the
   largest weight in Φ (0.4). The registered threshold (0.85) is comfortably clear
   even under a more conservative PCI, so the *confirmation* stands. But the
   monograph must not present Φ = 0.9983 as a precision figure. The honest claim is:
   Φ ≈ 1 under a structural PCI approximation; a label-aligned PCI computation is
   outstanding.
3. *The transition points sit in a shared exclusion zone.* Both observables have
   A3 (ergodicity) failing at the critical coupling (Z_shared applies at the
   transition). The conserved homology is therefore a statement about the partition
   *away from* θ*. This does not weaken the result — it sharpens its scope: the
   claim is partition-structure conservation across the regime layout, not
   identical behaviour at the critical point itself.

### 2.7 Ledger summary

| # | Result | Level | Load-bearing limitation |
|---|---|---|---|
| 2.1 | lambda_proxy insufficiency | Medium→Strong | order-of-discovery must be shown explicit |
| 2.2 | F0 at θ* | Medium | retrodiction, no new feature |
| 2.3 | F-gradient at separatrix | Medium | diagnostic placement only |
| 2.4 | self-similarity (corrected pendulum) | Medium | ridge removal is Class A, not Class B |
| 2.5 | matched-ε transfer 0001↔0003 | Medium | confirms interpretation of Φ |
| 2.6 | same-BC transfer 0004↔0001 | **Strong (confirmed)** | single endpoint d_BC=0; PCI approximate; θ* in Z_shared |

**Honest bottom line.** ARW now has solid Medium-level validation, one
Medium-approaching-Strong result (2.1), and **one clean Strong-level result
(2.6): a pre-registered prediction that committed before measurement and was
confirmed.** What remains open is not whether ARW can produce a strong result —
it has — but whether the confirmed endpoint generalises into a *metric*. That
requires the monotonicity control in §3.4.

---

## 3. The Strong Test, Confirmed — and the Control That Turns It Into a Metric

> **Status of this section: claim (confirmed) + experiment-proposal (§3.5).**
> The prediction in §3.2 was registered on 2026-06-02 *before* CASE-0004's
> transfer artefacts were finalised, and is recorded in
> `transfer_test_0004_0001_coupling/prediction_registration.md`. It was confirmed
> (Φ = 0.9983 ≥ 0.85). §3.5 specifies the further control — a different-BC-class
> transfer with d_BC > 0 — that is still outstanding and that converts the
> confirmed endpoint into a monotonic metric.

### 3.1 The hypothesis under test — hierarchical signature factorisation

We claim that transfer confidence is a monotonically decreasing function of a
**signature distance** d(Σ_A, Σ_B), and that this distance *factorises
hierarchically* into coordinates of decreasing coarseness:

1. **BC-class distance** (discrete, coarsest coordinate)
2. **normalised transition location** TBS_norm
3. **ε-stability similarity** SDI

Hierarchical means: a large BC-class distance dominates; *within the same BC
class*, the finer coordinates decide. The existing transfer metrics (Φ,
TBS_norm, SDI) are then not separate quantities but successive coordinates of a
single signature distance, with the BC class as its zeroth coordinate.

### 3.2 The prediction (registered before measurement)

> CASE-0001 (Kuramoto, Coupling) and CASE-0004 (coupled Stuart-Landau, Coupling)
> are the same BC class but different dynamics and different primary observables
> (r_ss vs PLV). The factorisation hypothesis predicts that, **at matched ε**,
> their transfer admissibility Φ is high (operationally: Φ_matched ≥ 0.85,
> admissibility verdict `highly_admissible` or `partially_admissible`), because
> the coarsest coordinate — BC-class distance — is zero, leaving only the finer
> coordinates to differ.

### 3.3 Outcome — confirmed

Measured: Φ = 0.9983 (`highly_admissible`); RCD = 0 (N=4 both); SDI = 0
(identical 4-node, 3-edge linear adjacency); TBS_norm = 0.008; ε = 0.09 matched
in both scopes, so Φ_raw = Φ_matched. The result clears the registered
threshold and falls far from the falsifier (Φ < 0.60). The factorisation's
endpoint prediction at d_BC = 0 holds.

The substantive content, restated from §2.6: the homology is conserved across an
**opposite-primary-BC observable pairing** (PLV: C·A·R, relational; r_ss: R³·A·D,
collective). Conservation precisely where the two descriptions diverge most is
the discriminating evidence between the classical reading (system similarity
drives transfer) and the ARW reading (partition homology drives transfer). The
result favours the ARW reading.

The falsifier below is retained for the record; it was the live falsifier at
registration time and did not trigger.

### 3.4 The falsifier (what would have refuted the framework)

> If, at matched ε with both observables confirmed sufficient on their own
> scopes, Φ_matched had remained low (Φ_matched < 0.6, `inadmissible`), the
> hierarchical factorisation would be **refuted**: same BC class failing to
> secure transfer once resolution was controlled. A low Φ_matched could not be
> rescued by re-matching ε, because ε was matched by construction. This branch
> did not occur.

### 3.5 The outstanding control — different BC class (d_BC > 0)

> **Status: experiment-proposal.** This is the test that converts §3.3 from a
> confirmed endpoint into an established metric.

A single point at d_BC = 0 confirms one end of the claimed monotonicity. It does
not show that Φ *falls* as d_BC grows — the homology could, for all this result
proves, be high across *unrelated* BC classes too, in which case BC-class
distance would carry no information and the "metric" would be vacuous. The
necessary control:

> **Prediction (to register before running):** a transfer between two systems of
> *different* BC class (d_BC > 0) — e.g. a Coupling case (CASE-0001) against a
> Restriction case (CASE-0003) or an Aggregation case (CASE-0007, SIR) — yields,
> at matched ε with both observables confirmed sufficient, a Φ *measurably lower*
> than the d_BC = 0 result of §3.3. Ideally two different-class pairs at distinct
> d_BC values, to show the fall is graded rather than binary.

Note that CASE-0001 ↔ CASE-0003 already exists (Φ ≈ 0.95 at matched ε, §2.5),
which is *high* — so the naive "different class ⇒ low Φ" is already under
tension. This is not a problem; it is the most interesting part. It suggests
BC-class distance alone is too coarse, and that what the metric actually tracks
is a finer signature distance in which Coupling and the Restriction-dominated
r_ss observable are closer than their nominal class labels suggest (recall r_ss
is itself R³·A·D — Restriction-dominated — even on a Coupling system). The
control must therefore be designed around *observable* BC structure, not just
*system* BC class. A clean falsifier requires a pair whose signatures are
genuinely far on every coordinate. CASE-0007 (SIR, Aggregation) with a
genuinely Aggregation-dominated observable is the better candidate than a
Restriction case whose observable may alias toward r_ss.

### 3.6 Controls that validated §3.3 (per repo guards)

These were satisfied for the confirmed result (see
`transfer_test_0004_0001_coupling/design/controls_checklist.md` and the
RESULTS folder validity conditions):

- **Observable sufficiency first.** PLV confirmed sufficient on CASE-0004 (and
  amp_asym, insufficient by design as the emergence condition, was *not* used);
  r_ss sufficient on CASE-0001. Confirmed before transfer was computed.
- **Observable BC structures documented** for both scopes in the transfer report
  (GUARD-6): PLV = C·A·R, r_ss = R³·A·D. This is what makes the §3.3 homology
  interpretable rather than a confound — the observable divergence is recorded,
  so the partition conservation is read against it, not in ignorance of it.
- **sweep_range present** in both Invariants.json (GUARD-5/GUARD-8); TBS_norm
  computed in normalised form (0.008), not raw. Both Φ_raw and Φ_matched
  reported (equal here, since ε matched).
- **CASE-0004 go_nogo = go** before transfer ran (GUARD-7), with the primary
  phase-locking transition R2→R3 at K=0.055 meeting the go criterion.

One honest deviation to record in the monograph: PCI was computed as a
*structural* approximation (from N and adjacency), not from label-aligned
annotated regimes, and PCI carries the largest Φ weight (0.4). The confirmation
is robust to this because the margin over threshold is large, but a
label-aligned PCI recomputation should be listed as outstanding work so the
0.9983 figure is not over-read.

---

## 4. How to Present This in the Monograph

1. Lead the validation chapter with the **hardness ladder** (§1) so the reader
   knows the grading rule before seeing any result. This pre-empts the
   "you only ever explain what already happened" objection by showing you share
   the worry.
2. Present the **ledger** (§2) without inflation. Mark every Medium result
   Medium. 2.6 is the one Strong result — present it as such, but lead its
   strength with the *observable-BC-mismatch* fact, not the Φ number; the high Φ
   is the headline a sceptic discounts, the conserved homology across opposite
   observable structures is the part they cannot.
3. State the **Class A / Class B** distinction (§2.4) yourself, before a reviewer
   does. Owning the limitation of the pendulum case is more persuasive than
   having it extracted. Apply the same self-disclosure to 2.6's three caveats
   (single endpoint, approximate PCI, θ* in Z_shared).
4. Frame §3.3 as **confirmed**, then immediately pivot to §3.5 as the **open
   commitment**. The honest arc is: "we registered a prediction, it held, and
   here is the next prediction — different BC class, lower Φ — that we have *not*
   yet run and that would turn this from a confirmed special case into a metric."
   A monograph that ends on a still-live, falsifiable follow-up reads as ongoing
   science, not a closed apologia. The tension noted in §3.5 — that CASE-0003 is
   a *different* class yet already shows high Φ — should be presented as the open
   puzzle it is, not hidden: it is what makes the signature-distance question
   non-trivial.

---

## Maintenance Note (2026-07-11 import)

Imported into `arw-repo` at Rico's request, found via a different chat session and
recognized as old/potentially non-canonical before import. Confirmed superseded on
import: see the warning banner at the top of this file for the specific contradicting
evidence (`transfer_v2` recomputation of the exact same case pair, same date, giving
Φ=0.7794/`ambiguous_requires_inspection` instead of the 0.9983/`highly_admissible`
this document reports as a "Strong (confirmed)" result). Not registered in DOC_INDEX
before this import (orphan). §3.5's own outstanding control (a different-BC-class
transfer with d_BC > 0) was, ironically, informative anyway: CASE-0001↔CASE-0003
already showed high Φ despite differing BC class (§2.5), which this document treats
as an open puzzle rather than a warning sign — the later Q-REL-05 finding resolves
that puzzle by showing Φ doesn't reliably track BC-class distance at all, undermining
the premise of §3.1's factorisation hypothesis, not just the §2.6/§3.3 confirmation.
