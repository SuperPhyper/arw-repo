---
status: note
layer: docs/notes/
created: 2026-08-04
revised: 2026-08-04 (external review round 5 — five precisions incorporated)
depends_on:
  - docs/notes/ews_discriminator_test_protocol.md
  - docs/core/falsification_schema.md
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/advanced/epsilon_and_scope_resolution.md
---

# Stage-1 Review — manufacturer specifications constrain ε; Δ remains a modelling commitment

Review of the Stage-1 feasibility stop recorded in the analyst handoff v2
(`Simulationen/ews_cascade/_handoff_v2/`). The stop is upheld. What follows adds
one retrieved fact, one three-way conceptual distinction, and one power
assessment that together change *why* the study stops and what a replacement
would have to look like.

**Analyst-side blinding status:** the blinded CSVs were not opened. Nothing below
uses measurement values.

**Core result of this review, in one line:**

> instrument specifications → ε_instr ≠ ε_operational ≠ Δ

Three distinct objects, previously collapsed into one in both the protocol and
the Stage-1 record.

---

## 1. The retrieved fact: manufacturer specifications do exist

The Stage-1 record states that numerical precision is unavailable. That is
correct for the EML and the Supporting Information, but not for the instrument.
The EML declares the exact configuration — YSI 6600 V2-4 sondes with optical DO
(6150 ROX) and optical Chl-a (6025) — and the manufacturer datasheet for that
configuration publishes a specification table:

| Parameter | Range | Resolution | Accuracy |
|---|---|---|---|
| ROX optical DO, % saturation | 0–500% | 0.1% | 0–200%: ±1% of reading or 1% air saturation, whichever is greater |
| ROX optical DO, mg/L | 0–50 mg/L | 0.01 mg/L | 0–20 mg/L: ±0.1 mg/L or 1% of reading, whichever is greater |
| pH (6561) | 0–14 units | 0.01 unit | ±0.2 unit |
| Temperature (6560) | −5…+50 °C | 0.01 °C | ±0.15 °C |
| Chlorophyll (6025) | ~0–400 µg/L | 0.1 µg/L; 0.1% RFU | **no accuracy stated**; detection limit ~0.1 µg/L; linearity R² > 0.9999 |

*(Source: YSI 6600 V2 sensor specification sheet, E52-02, ©2010.)*

This is route 1 of the three exits the Stage-1 record lists, and it is partially
open. It does not reopen the study, for the reasons in §2 and §4.

## 2. The conceptual correction: three objects, not two

### 2.1 What the specifications do and do not give

The Stage-1 record — and the protocol it was written against — treated
"numerical instrument precision" as the missing basis for **Δ**. That conflates
components of the scope tuple. But the correction must not overshoot in the
other direction: a datasheet does not hand over ε either. Resolution, accuracy
and ε are three different things.

- **Resolution** is the smallest digitally representable difference.
- **Accuracy** bounds the deviation of a reading from a reference value.
- **ε** is the equivalence/adjacency threshold used *in a given scope* for
  regime construction.

> Manufacturer specifications provide an external, pre-data constraint on the
> **instrument contribution** to ε. They do not by themselves determine the
> complete operational ε used for regime construction.

A **preregistered mapping rule** is still required between them, and the rule is
not unique. For pH at ±0.2 units, at least two constructions are defensible:

- ε_truth = 0.2 — reading compared against a hypothetical true value;
- ε_pair = 0.4 — two *readings* declared mutually compatible under a worst-case
  interval interpretation.

Which one is correct depends on what the cover construction compares, and the
choice must be declared, not inherited silently from the datasheet.

Further, **DO accuracy is reading-dependent** ("±1% of reading or 1% air
saturation, whichever is greater"). The instrument contribution is therefore
initially a *function* ε(x), not a scalar; collapsing it to a constant is a
second declared modelling step.

Beyond the instrument, further contributions to observational indistinguishability
remain unaccounted: calibration drift between the weekly instrument rotations,
temporal aggregation, and the published preprocessing (outlier removal, missing-day
rule, mean-shift correction across instrument changes).

### 2.2 The pH standardization trap

The published analysis standardized pH within each year to mean 0 and SD 1, to
absorb between-lake buffering differences. An accuracy declared in pH units can
therefore be applied **only to the raw pH series**. After standardization the
corresponding ε would be ±0.2 divided by an annual SD that is itself estimated
*from the measurements* — i.e. the ε would become data-derived, which is exactly
the circularity the preregistration exists to prevent. Any use of pH in this
study must therefore be on raw units, and the protocol must say so.

### 2.3 Δ is a different kind of object

Δ is the class of admissible perturbations: which variations of the system must
leave regime assignment intact. That is not a property of the instrument at all.
No datasheet can supply it, because it encodes a *modelling commitment* about
which changes count as "the same lake state".

In simulation this distinction is invisible: Δ is whatever we inject, and σ_Δ
follows. On observational data the objects come apart completely, and the Cascade
stop is the first place the framework has been forced to notice it.

Consequences:

1. **ε_instr is declarable here** for raw DO and raw pH — external, pre-data,
   defensible. This part of the Stage-1 verdict is revised.
2. **ε_operational is not thereby fixed** — it requires the declared mapping rule
   (§2.1) plus an accounting of drift, aggregation and preprocessing.
3. **Δ remains undeclarable from metadata — necessarily, not accidentally.** No
   further metadata retrieval would fix it. A revised protocol must declare Δ as
   an explicit modelling commitment (e.g. "rotation between the two deployed
   sondes, plus within-season weather variation at fixed season phase, count as
   the same state"), preregistered and defended as such.
4. **The empirical route through the two-sonde rotation stays blocked**, as the
   Stage-1 record found: without instrument IDs the paired disagreement is not
   recoverable, and recovering it from step changes at rotation boundaries would
   require looking at the measurements.

### 2.4 Direction of bias — conditional on the σ_Δ definition

> If perturbation spread is defined **inclusion-monotonically** — as a supremum
> observable radius, diameter, or worst-case span over Δ — then narrowing Δ can
> only reduce or preserve σ_Δ,π. Under the present classifier this makes
> stability easier to obtain, and an underestimated Δ is therefore
> **anti-conservative for H1**.

The repo's canonical definition, σ_Δ(x) := sup_{δ∈Δ} |O(x+δ) − O(x)|
(`docs/glossary/perturbation_spread.md`), is of exactly this form, so the
corollary holds as stated *here*. It would **not** transfer automatically to a
distributional variant (σ_Δ as a standard deviation over a measure on Δ), where
narrowing the class can change the weighting and need not reduce the spread. Any
future σ_Δ variant must re-derive the bias direction rather than inherit it.

"Err upward" is likewise bounded: an arbitrarily wide Δ eventually tests a
different claim, not a more conservative version of the same one. The clean form
is the preregistered plausible family

> Δ_min ⊆ … ⊆ Δ_max

with the upper end chosen deliberately conservative, and the H1/H2 verdict
required to be stable across the whole family. A verdict that flips inside the
family is the reportable finding, not an invitation to select a member.

## 3. Chlorophyll: F0 for the absolute-concentration projection only

Chlorophyll has resolution and detection limit but **no stated accuracy**, and
the 6-Series manual states that a single-point calibration essentially sets the
zero and yields readings that are "only semiquantitative with regard to
chlorophyll" — reflecting change rather than concentration; defensible absolute
concentrations normally require post-calibration against extracted water samples,
which is not recoverable here.

The earlier draft of this note concluded "chlorophyll is F0" and thereby broke
ARW's own rule that **F0 is Π-relative, not sensor-relative**. The correct
classification separates two projections:

- **Π_abs = absolute Chl-a concentration** — *not supported* under the available
  calibration record. F0: the observable is used outside its declared valid range.
- **Π_rel = relative chlorophyll fluorescence / change** — *potentially
  admissible in principle*. An alarm location need not depend on absolute
  concentration, only on the stability of relative temporal change; the Supporting
  Information does treat sensor chlorophyll as a direct measured series, and
  reports the clearer EWS signals in the direct sensor variables rather than in
  the model-derived metabolism quantities.

This does not rescue chlorophyll for the present test: for Π_rel there is still
no external rule giving ε (the RFU scale carries no accuracy figure), and drift
plus instrument exchange remain unquantified. The honest verdict is therefore:

> F0 for absolute chlorophyll concentration under the available calibration
> record; potentially admissible under a separately declared relative-fluorescence
> projection, for which ε remains unresolved.

The instructive part is that the fault lies not in the sensor alone but in the
mismatch between sensor validity and the chosen Π — which is precisely what the
F-taxonomy is supposed to make visible, and what the first draft failed to apply
to itself.

## 4. Power: the coherence discriminator degenerates and its channels are not independent

Granting the revision of §2.3.1, the admissible response set is **raw DO %
saturation and raw pH**. Temperature is admissible only as a forcing-variable
control (see §5). Model-derived GPP/R/NEP are correctly excluded for carrying
process error on top of observation error.

The earlier draft claimed "no configuration of k carries information". That
overstates it: k = 2 of n = 2 does test concordance. What it loses is the
structure that makes H1 interesting:

> With two response observables, the intended **graded** coherence discriminator
> degenerates into pairwise unanimity. It remains logically testable, but loses
> the redundancy and partial-coherence structure needed to distinguish a
> system-level transition from an observable-specific success or failure.

There is a second, stronger objection independent of counting. DO and pH are not
independent measurement-error channels: they come from the same multiparameter
sondes and share logging, deployment, the weekly instrument rotation, and parts
of the preprocessing (including the documented mean-shift correction across
calibration and instrument changes). Common-mode instrument error therefore
propagates into both, and an apparent "coherence" between them is not evidence of
system-level structure in the way H1 requires. Hence:

> Only two response variables retain externally constrained instrument
> uncertainty, and those two do not constitute independent measurement-error
> channels.

That is the operative reason the confirmatory H1 test is too weakly identified on
this dataset.

## 5. What a viable version would need

- **≥ 3 response observables** is the mathematical minimum for a non-trivial
  majority rule; **≥ 4 is the recommended robust design target**, since k = 3 of 4
  tolerates a single observable failing for an unrelated reason. Four is a design
  recommendation, not a logically forced minimum.
- **Independent measurement channels** — separate instruments or separate
  measurement principles, not several parameters from one sonde package.
- **Published accuracy specifications** for each admitted response observable,
  plus a declared mapping rule from specification to ε_operational.
- **A labelled negative recorded by the same apparatus.** This is the Cascade
  design's real strength and must be preserved. Note the role separation: the
  *reference lake* is the system-side labelled negative; a forcing variable such
  as temperature is a covariate control, **not** a negative response control,
  since temperature and stratification themselves vary between lakes.
- **A declarable Δ as a modelling commitment**, preregistered as the family
  Δ_min ⊆ … ⊆ Δ_max of §2.4, with verdict stability across the family required.

## 6. Registry consequences

- **Q-EWS-01** — answered negative, with the question corrected: Δ is not
  declarable from measurement structure **in principle**, because Δ is not an
  instrument property. What metadata constrains is ε_instr, and even that
  underdetermines ε_operational.
- **Q-EWS-02** — open, untested; power blocker recorded (degeneration to pairwise
  unanimity plus shared measurement infrastructure).
- **Q-EWS-04** — admissible form of a Δ declaration for observational data;
  candidate answer is the declared family with required verdict stability.
- **Q-EWS-05 (new)** — the mapping rule from instrument specification to
  ε_operational: truth-referenced vs pairwise interpretation, reading-dependent
  ε(x) vs scalar collapse, and the additional contributions (drift, aggregation,
  preprocessing) that the specification does not cover.
- The ε_instr / ε_operational / Δ triple is general and belongs in the framework
  documentation, not only in this test's record — flagged for
  `docs/advanced/epsilon_and_scope_resolution.md` and
  `docs/glossary/perturbation_spread.md`, which currently treat both ε and Δ only
  in their simulation-native forms.

## 7. Verdict

The Stage-1 stop stands. Its rationale changes:

> Manufacturer specifications provide external pre-data constraints on the
> instrument component of ε for raw DO and pH; they neither determine the
> complete operational ε nor provide Δ. Δ is necessarily a modelling commitment
> specifying the class of variations under which regime assignment is required to
> persist. Chlorophyll is unsupported as an absolute-concentration observable
> under the available calibration record, although a separately defined
> relative-fluorescence observable remains conceptually possible. Even under the
> favourable admission of DO and pH, the dataset retains only two response
> variables with externally constrained instrument uncertainty, and both share
> substantial measurement infrastructure. The intended graded cross-observable
> coherence discriminator is therefore too weakly identified for the confirmatory
> H1 test.

The discipline behind the stop is the substantive result of this round: the
protocol's stop condition fired and was obeyed rather than renegotiated. DEV-001
and DEV-002 are correctly recorded; the blinded set is correctly demoted to an
infrastructure rehearsal. The framework gain — the three-way separation of
ε_instr, ε_operational and Δ — exceeds what the test itself would have delivered
had it run.
