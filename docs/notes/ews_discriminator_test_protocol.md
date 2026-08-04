---
status: experiment-proposal
layer: docs/notes/
created: 2026-08-01
execution_status: "Stage-1 feasibility STOP, 2026-08-01/04 — see docs/notes/ews_stage1_review_epsilon_vs_delta.md. Cascade instantiation not viable (observable set too small for H1); protocol design itself unchanged and reusable on a dataset meeting the §5 requirements of the review note."
depends_on:
  - docs/glossary/observable_range.md
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
  - docs/art_instantiations/arw_for_ecology.md
  - docs/bc_taxonomy/bc_failure_signatures.md
---

# A Preregistered Discrimination Study of Observable-Specific versus System-Level Early Warning Signals

*(Internal working title: the EWS discriminator test.)*

**Framing (fixed 2026-08-01, review round 4).** This study is **not** posed as
"ARW versus EWS". The question it asks stands on its own and is of interest
independently of ARW: *when an early-warning indicator rises, is that a property
of the system or of the particular observable it was computed on — and can the
two be told apart on data with labelled positives and negatives?* ARW supplies
one candidate discriminator (the F0 / F-gradient taxonomy and a cross-observable
coherence rule); the EWS toolkit and plain perturbation-spread thresholding
supply the competitors. A negative result is then a publishable finding about
early-warning methodology rather than an internal disappointment, and the study
is usable by researchers with no stake in ARW at all. Every claim below is to be
written in that register.

**Purpose.** ARW's claims are currently supported by self-generated simulation
data of one system family and by illustrative examples. This document specifies
the cheapest test that could change that: a preregistered comparison against the
early-warning-signals (EWS) literature on public data with labelled positives
*and* negatives. It is written before any data is touched, so that the criteria
cannot drift toward whatever the data happens to show.

**Why this test and not another.** EWS is the closest existing programme to ARW's
ambition (predicting regime transitions across domains from generic indicators),
it has an established benchmark culture, and its central practical problem — false
alarms — is exactly where ARW claims a structural distinction the EWS toolkit does
not make. If ARW cannot add anything here, the general claim of the monograph is
in doubt; if it can, one such result carries more weight than the entire
simulation corpus.

---

## 1. The distinctive claim, stated so it can fail

EWS indicators (rising variance, rising lag-1 autocorrelation, critical slowing
down) are computed **on one observable at a time** and interpreted as properties
**of the system**: the system is approaching a bifurcation. The known failure mode
is the false alarm — indicators rise without a transition following.

ARW's F-taxonomy makes a distinction EWS has no slot for: an indicator rise may be
a property of the **description** rather than the system.

- **F0 / observable-range failure** — the observable leaves the zone where it is
  well-defined; its "signal" is a projection artifact.
- **F-gradient / cover-instability** — the observable is sound but too steep at
  this resolution: σ_Δ ≥ ε locally, so component membership is not stable under
  admissible perturbation.
- **Genuine regime transition** — the partition boundary is stable under Δ and
  reproduces across admissible observables.

This yields a prediction EWS does not make, because it is *observable-relative*
by construction where EWS is observable-blind:

> **H1 (discrimination).** For a genuine system transition, alarms from
> independent admissible observables of the same system agree in normalised
> sweep/time position. For a descriptive artifact (F0 / F-gradient), the alarm is
> **idiosyncratic to the observable** and co-located with that observable's own
> instability diagnostics.

> **H2 (added value).** Requiring cross-observable coherence reduces the
> false-alarm rate on labelled negatives at equal or lower cost in detection
> power on labelled positives, relative to single-observable EWS.

**Explicit delimitation against multivariate EWS.** Multivariate/spatial EWS
already combines variables — but to *increase detection power* by aggregation.
The ARW proposal uses **disagreement between observables as diagnostic
information about which failure type occurred**. Aggregation destroys exactly the
signal ARW reads. If the test succeeds only in a form that a simple multivariate
EWS also achieves, H2 counts as failed (see §5, baseline B4).

---

## 2. Data (labelled positives and negatives from one apparatus)

**Primary dataset — Cascade whole-lake experiment (Carpenter et al. 2011).**
Peter Lake was manipulated (stepwise largemouth-bass addition, 2008–2011) into a
food-web regime shift; Paul Lake was the unmanipulated reference over the same
period, with the same instruments and the same weather. This gives what benchmark
studies usually lack: **a labelled positive and a labelled negative recorded by
the same apparatus.**

- Daily key variables, Paul and Peter, 2008–2011 —
  EDI, DOI 10.6073/pasta/c08b808fe0ca65ae30b65b7d780f037f
- High-frequency sonde data, Food Web Resilience Experiment 2008–2011 —
  EDI, DOI 10.6073/pasta/f618d3b51a53d08021563701a211304f

Multiple simultaneous observables are recorded (chlorophyll, dissolved oxygen,
pH, phycocyanin, zooplankton biomass, water temperature) — the precondition for
H1. The original EWS analysis (Carpenter et al. 2011, *Science* 332:1079) is the
published comparison point.

**Secondary (only if the primary is inconclusive):** the `ewstools` benchmark
corpus and the deep-learning EWS test sets (Bury et al. 2021), which provide many
labelled model and empirical series but *not* the paired same-apparatus
positive/negative structure that makes the Cascade data valuable here.

---

## 3. Preregistered analysis protocol

Fixed before data access. Any deviation must be recorded as a deviation, with the
original criterion left visible.

1. **Freeze the observable set — structured, not a bare list.** Declare Π before
   inspecting any measurements, one row per admitted variable, in
   `03_prereg/observable_admission.md`:

   | Family | Variable | Reason for inclusion | Expected mechanism | Admissibility concern |
   |---|---|---|---|---|
   | Oxygen | DO | metabolic integrator | whole-lake metabolism | diel cycle dominates; supersaturation artifacts |
   | Algae | chlorophyll | phytoplankton biomass | grazer release → biomass shift | sonde fluorescence ≠ biomass under photoinhibition |
   | Cyanobacteria | phycocyanin | bloom-forming fraction | community composition shift | low signal outside bloom periods |
   | Physics | water temperature | external forcing | driver, not response | expected to show weather, not regime structure |

   *(The rows above are illustrative of the required format; the actual set is
   fixed in Stage 1 from the metadata and may differ.)* Recording the expected
   mechanism in advance is what makes a later "this observable behaved oddly"
   checkable rather than rhetorical, and the admissibility-concern column is
   where an F0 risk must be named *before* it can be invoked as an explanation.

2. **Blind the labels and the calendar.** Series identity (which lake) is
   withheld under opaque IDs, and the time axis is shifted by a single random
   offset c applied *identically to all series*, so that relative timing, lags,
   window structure and inter-series alignment are preserved exactly while the
   calendar is removed. Reported times are t′ = t + c.

   **Honest limit of the time blinding (do not overstate it).** The calendar is
   only *partially* hidden: ice-free-season gaps, diel cycles and annual periodicity
   remain visible in the data itself, so the phase within a year and the number of
   seasons can be inferred. What the offset removes is the absolute year — hence
   the ability to align a suspected transition with the *published* manipulation
   schedule. That is the leak worth closing; the residual seasonal structure is
   not closable without destroying the dynamics under study. Treat time blinding
   as raising the cost of unconscious alignment, not as a guarantee.
3. **Per-observable EWS layer.** Standard indicators via `ewstools` with the
   literature's default settings; sensitivity across the declared grid of
   detrending bandwidth and window size, since both are known to move results.
4. **Per-observable ARW layer.** For each observable: σ_Δ estimated from the
   declared Δ (measurement-replicate/short-lag resampling — the Δ *must* be
   declared, not chosen to fit), the ε-plateau structure, cover stability, and an
   F-classification per alarm (F0 / F-gradient / candidate transition).
5. **Coherence rule.** An alarm is *coherent* iff ≥ k of the admissible
   observables produce alarms whose normalised positions agree within a declared
   tolerance; k and the tolerance are fixed in step 1.
6. **Commit a prediction, per series, before unblinding.** Not a metrics dump —
   an explicit call, recorded in `03_prereg/prediction_sheet.md`:

   | Series | Prediction (positive / negative) | Confidence (0–1) | Transition location (t′) | Expected reason if wrong |
   |---|---|---|---|---|

   The last column is the load-bearing one: naming in advance *how* the call
   could fail prevents the post-hoc discussion from collapsing into a debate
   about individual indicator values. A prediction sheet with an empty
   "expected reason if wrong" column is not complete.
7. **Unblind once and score** against the manipulation record and the criteria
   table in §4.

**Audit trail.** Each of these steps writes its own timestamped file under
`03_prereg/` (`decision_log.md`, `delta_definition.md`, `observable_admission.md`,
`coherence_rule.md`, `baseline_parameters.md`, `prediction_sheet.md`). The
decision log is append-only: entries are added with a timestamp, never edited or
removed. This is what turns the preregistration from a promise into a record that
a third party can check.

**Freeze before data.** Before any measurement file enters the workspace, the
preregistration is frozen twice over: (i) a SHA-256 manifest of every file under
`03_prereg/` plus this protocol, written to `03_prereg/PREREG_MANIFEST.sha256`;
(ii) a git tag `cascade_prereg_v1` in `arw-repo` on the commit containing this
document. Any later change to the criteria must appear as a *new* file plus a
recorded deviation, never as an edit to a frozen one.

---

## 4. Success and failure criteria (fixed in advance)

| Outcome | Criterion |
|---|---|
| **H1 supported** | On the reference lake (labelled negative), single-observable EWS alarms are observable-idiosyncratic *and* co-located with that observable's σ_Δ/cover-instability diagnostics; on the manipulated lake, alarms are cross-observable coherent. |
| **H1 refuted** | Alarm coherence does not differ between the manipulated and the reference lake, or coherent alarms appear in the reference lake without a transition. |
| **H2 supported** | The coherence rule strictly dominates single-observable EWS on the (false-alarm rate, detection lead time) pair, and is not matched by baselines B1–B4. |
| **H2 refuted** | Any baseline matches it — in particular B3 (plain σ_Δ threshold) or B4 (multivariate EWS). |
| **Inconclusive** | The data cannot resolve it: too few admissible observables, no declarable Δ, alarms too sparse. Recorded as inconclusive, not retried with adjusted criteria. |

**The run-4 lesson applies here** (see `scope_fibration.md` §5b): a structure can
localise correctly and still add nothing over the quantities it is built from.
H2 exists precisely to catch that, and its refutation is a real possible outcome
that must be reported as prominently as a success.

---

## 5. Baselines (matched cost, run alongside)

- **B1** — single-observable EWS at literature defaults.
- **B2** — single-observable EWS with the best hindsight-tuned parameters
  (upper bound on what the standard toolkit can do).
- **B3** — plain σ_Δ threshold per observable, no cover/fibration machinery.
  *(The baseline that defeated the fibration violation set in run 4.)*
- **B4** — multivariate/aggregated EWS across the same observable set.

---

## 6. What each outcome means for the monograph

- **H1 + H2 supported:** ARW has demonstrated added diagnostic value on external
  real-world data against an established programme. This becomes the empirical
  anchor the book currently lacks, and the Class-C universality claims acquire
  their first non-illustrative support.
- **H1 supported, H2 refuted:** ARW correctly classifies but does not outperform.
  The monograph must then present the F-taxonomy as an interpretive framework
  with verified consequences, not as a superior detection instrument — the same
  restraint already recorded for D(S).
- **H1 refuted:** the observable-relativity claim fails on real data. This is the
  outcome that would require rewriting the strong claims of the introduction, and
  it must be reported rather than absorbed.
- **Inconclusive:** the book states that the distinctive claim has not yet met
  external data, and names this test as the open item.

Any of the four is a gain in seriousness over the current state, in which the
claim has never been exposed to data that could refute it.

---

## 7. Feasibility and first step

Cost is dominated by data handling, not computation: the series are small, and
the ARW layer reuses the existing pipeline's ε-plateau and σ_Δ machinery. The
honest risk is not compute but **declarability of Δ on observational data** —
ARW's perturbation class is native to simulation, and its observational
counterpart (replicate measurements, short-lag resampling, instrument noise
model) is a modelling choice that must be fixed in step 1 and defended, since
choosing it after seeing the alarms would make the whole test circular.

**First step (cheap, decides feasibility before any commitment):** obtain the EML
metadata of both EDI packages *only* — no measurements yet — and answer four
questions from it: which observables have continuous coverage across 2008–2011 in
both lakes; what instrument precision is declared per variable; whether replicate
structure exists (duplicate sondes, calibration repeats, co-located manual
samples); and what the true sampling interval is. These decide whether a
defensible Δ can be declared from measurement structure alone (Q-EWS-01). If not,
this protocol stops here and says so.

**Blinding is externally held.** Rico stages the data and keeps the series-ID →
lake mapping; the analysis side never sees it until a single unblinding event
after all thresholds, the observable admission list, the declared Δ, the alarm
classifications and the baseline results are written down. Operational details:
`Simulationen/ews_cascade/STAGING_GUIDE.md`. What blinding hides is *only* the
mapping — the published facts of the experiment (Peter manipulated, Paul
reference) cannot be and need not be hidden.

## 8. Open questions (to be registered on execution)

- **Q-EWS-01** — Can an admissible Δ be declared for observational time series
  from measurement structure alone, without reference to the alarms it will be
  used to judge?
- **Q-EWS-02** — Does alarm coherence across admissible observables discriminate
  genuine transitions from descriptive artifacts on labelled data (H1)?
- **Q-EWS-03** — Does the coherence rule add value over single-observable EWS,
  plain σ_Δ thresholding, and multivariate EWS (H2)?
