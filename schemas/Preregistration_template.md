---
status: note
layer: schemas/
---

# Preregistration — STUDY-YYYYMMDD-####

<!-- Template v0.1 (Q-VAL-01). Copy to studies/STUDY-YYYYMMDD-####/Preregistration.md,
     fill in, then FREEZE: compute SHA-256, write it into StudySpec.preregistration,
     create the git tag, set StudySpec.frozen_at. Nothing below this line may change
     after the freeze; corrections go into StudyRecord.deviations.

     Freeze procedure (per the Cascade practice, ews_discriminator_test_protocol.md):
       1. sha256sum Preregistration.md → StudySpec.preregistration.sha256
       2. git tag study_<id>_prereg_v1
       3. StudySpec.frozen_before_run: true, frozen_at: <date>
       4. Only then: run. -->

## 1. Question and tier

One sentence. Tier T1 | T2 | T3. Target Q-IDs.

## 2. Predictions

Numbered, falsifiable, each with its criterion:

- **C1** — Prediction: … Success iff: … Failure iff: …
- **C2** — …

Every criterion must be decidable from the declared artifacts alone. If a
criterion needs judgement, name the judge and the rubric now.

## 3. Analysis plan

Exact procedure: construction to be run, with which declarations (reference the
StudySpec blocks — do not restate them, they are frozen there), what is computed,
in what order. Any threshold, window, or seed used anywhere is fixed here.

## 4. What would make this study worthless

Named in advance: degenerate outcomes, confounds, and the conditions under which
the result must be reported as `inconclusive` rather than interpreted. (T2
studies: state explicitly what "no surplus over the 1D form" looks like for this
artifact, so it cannot be argued around after the fact.)

## 5. Blinding (T3 only)

What is blinded, how, and what is knowable before unblinding. Forced prediction
sheet if applicable.

## 6. Freeze block

- SHA-256: `<filled at freeze>`
- Git tag: `<filled at freeze>`
- Frozen by / date: `<filled at freeze>`
