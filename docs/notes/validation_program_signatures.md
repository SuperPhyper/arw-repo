---
status: experiment-proposal
source: derived from "Gleiche Operator-Signaturen in vielen Domänen" (2026-03-14)
layer: docs/notes/
related: operator_signature_catalog.md, cross_domain_signature_matrix.md, quantum_operator_extension.md
---

# Validation Program: Operator Signatures Across Domains

This document specifies six concrete research actions to make the hypothesis
"identical operator signatures appear across domains" testable within the ARW repo.

**Core hypothesis:** BC classes (Restriction, Coupling, Aggregation, Symmetry Breaking,
Forcing, Dissipation) are semantic labels for recurring operator signatures (S1–S5).
These signatures arise from a primitive basis of composition `∘`, product `×`, and
projection `π`.

**Acceptance standard:** A signature is considered "demonstrated in a domain" when
a case artifact exists that (a) names the signature explicitly, (b) gives the
system-specific operator form, and (c) shows the BC label follows from it — not
just from empirical regime structure.

---

## Action 1 — Signature Catalog as Reference Object

**Goal:** Establish S1–S5 as a stable, citable reference within the repo.

**Artifact:** `docs/advanced/operator_signature_catalog.md`

**Status:** ✅ Complete (2026-03-14)

**Acceptance criteria:**
- [ ] Each signature has a formal definition, invariants, and ≥3 cross-domain examples
- [ ] Each signature names its primary BC class
- [ ] Document carries `status: working-definition`
- [ ] Open questions (Q-DISS-01, Q-SIG-01, Q-TENSOR-01) are registered

---

## Action 2 — Cross-Domain Case Triads

**Goal:** For each signature, demonstrate it concretely in three different domains
using a shared template. This tests whether the signature label is truly domain-neutral
or domain-specific.

**Artifact per triad:** `docs/art_instantiations/triad_S{N}_{domain_A}_{domain_B}_{domain_C}.md`

**Proposed triads:**

| Signature | Domain A | Domain B | Domain C |
|---|---|---|---|
| S1 (Projection) | DS: Poincaré section | SP: Zwanzig projection | ML: PCA |
| S2 (Coupling) | DS: Lotka-Volterra | CT: Feedback interconnection | NEURO: E/I network |
| S3 (Forcing) | DS: Forced pendulum | EPI: Term-time SEIR | QM: TDSE with H(t) |
| S4 (Dissipation) | DS: Damped oscillator | NEURO: LIF leak term | QM: Lindblad dynamics |
| S5 (Expectation) | CT: Kalman / MMSE | SP: Mori-Zwanzig | ML: Attention |

**Status:** ❌ Not started

**Acceptance criteria:**
- [ ] For each triad: three case stubs exist with `CASE_TEMPLATE_signature_first.md` filled in
- [ ] Each stub names the same signature S_N in Section 4
- [ ] BC labels are consistent across the three domains
- [ ] At least one triad is promoted to a full pipeline case (ScopeSpec + BCManifest + results)

---

## Action 3 — Invertibility Experiment (ARW-Q15)

**Goal:** Operationalize the question: given observed regimes and observable data,
can the signature and BC label be uniquely inferred? Or is there irreducible overlap?

**Background:** ARW-Q15 asks whether the map Signature → BC label is injective.
The cross-domain matrix shows that S1 (Projection) maps to Restriction, Aggregation,
*and* Symmetry Breaking. This non-uniqueness needs to be quantified.

**Proposed experiment:**

1. Take three existing cases with known BC labels (CASE-0001: Coupling,
   CASE-0002: Coupling, CASE-0003: Restriction)
2. For each, extract the operator structure without looking at the BC label
3. Apply signature identification (S1–S5) mechanically
4. Check: does the signature assignment recover the BC label?
5. Identify cases where multiple BC labels are consistent with the observed signatures

**Artifact:** `docs/notes/experiment_Q15_invertibility.md`

**Status:** ❌ Not started

**Acceptance criteria:**
- [ ] Experiment protocol written and reviewed
- [ ] Applied to all three existing cases
- [ ] Overlap cases documented with explicit disambiguation rule proposed
- [ ] Result feeds back into `docs/notes/open_questions.md` (Q-SIG-01)

---

## Action 4 — Quantum Stress Test for the Primitives

**Goal:** Implement a QM case study covering projective measurement (S1), tensorial
composition (S2), and Lindblad dissipation (S4). Check whether the current ARW
primitive set is sufficient or whether `×` must be generalized to `⊗`.

**Background:** Documented in `docs/advanced/quantum_operator_extension.md`.
The QM column is the primary stress test for the Cartesian product primitive.

**Proposed case:** A two-qubit open system:
- State space: `H = ℂ² ⊗ ℂ²` (S2 — tensor coupling)
- Measurement: projective onto computational basis (S1)
- Dynamics: Lindblad with dephasing channel (S4)

**Questions to answer:**

| Question | Expected answer | Confidence |
|---|---|---|
| Is `×` as Cartesian sufficient for S2? | No — must use `⊗` | High |
| Does S1 (Restriction) apply to QM measurement? | Yes, with non-classical reading | High |
| Does S4 (Dissipation) apply to Lindblad? | Yes — CP semigroup matches signature | High |
| Which BC labels survive? | Coupling, Restriction, Dissipation | Medium |
| Must "product" be monoidal in ARW? | Yes, for QM-native coverage | Medium |

**Artifact:** `cases/CASE-YYYYMMDD-QM01/` + `docs/art_instantiations/qm_stress_test.md`

**Status:** ❌ Not started

**Acceptance criteria:**
- [ ] QM case filled with `CASE_TEMPLATE_signature_first.md`
- [ ] Each of S1, S2, S4 explicitly instantiated in QM terms
- [ ] BC label stability assessed for each signature
- [ ] Result documented in `docs/advanced/quantum_operator_extension.md`
  (Q-TENSOR-01, Q-TENSOR-03 updated)

---

## Action 5 — F5 Test Case: Model Failure through Operator Vocabulary

**Goal:** Find a case where a classical ARW model collectively fails and the cause
is plausibly "operator basis insufficient" — i.e. the observable structure cannot
be expressed from `{∘, ×, π}`.

**Background:** ARW-F5 (Scope Exhaustion) is the hypothesis that some regime
structures are inexpressible from the current primitive closure. Candidates:

| Candidate | Failure mode | Required primitive |
|---|---|---|
| Non-Markovian dynamics | Memory kernel not expressible as `∘` chain | Memory operator `M[x](t) = ∫ K(t−s) x(s) ds` |
| QM measurement chains | Non-commuting projections; order matters | Non-commutative composition |
| Renormalization group | Coarse-graining + rescaling as irreducible step | Scale operator |
| Chaotic mixing | Sensitive dependence not captured by smooth `π` | Symbolic dynamics / generating partition |

**Proposed experiment:**

1. Take a known failure case (e.g. CASE-0001, F1 flag at `sweep_refinement`)
2. Check whether the failure is attributable to observable insufficiency (standard)
   or to operator vocabulary exhaustion (F5)
3. If F5: document which operator is missing and what its formal definition would be

**Artifact:** `docs/notes/experiment_F5_scope_exhaustion.md`

**Status:** ❌ Not started

**Acceptance criteria:**
- [ ] At least one candidate case analyzed for F5
- [ ] Clear distinction between observable insufficiency and operator-vocabulary failure
- [ ] If F5 confirmed: proposed new primitive formally defined (even if not yet adopted)
- [ ] Result feeds into `docs/notes/open_questions.md`

---

## Action 6 — Empirical Bridge: Projection-Operator Methods in Neuro/EEG

**Goal:** Use the Mori-Zwanzig methodology — which has been explicitly applied to
EEG macro-dynamics — as a bridge case to test signature transferability from
Statistical Physics to Neuroscience.

**Background:** Mori-Zwanzig in StatPhys and EEG macro-modeling both use S1
(Projection / Zwanzig operator `P`) and S5 (Conditional expectation / memory kernel).
If the same signatures produce the same regime structure in both domains, this is
direct empirical evidence for domain-neutral signature semantics.

**Transfer pair:**

| Case A | Case B | Expected overlap |
|---|---|---|
| StatPhys: Mori-Zwanzig on Lennard-Jones fluid | NEURO: Mori-Zwanzig on EEG macro-modes | S1, S5 shared; BC labels Restriction + Stochastic |

**Proposed experiment:**

1. Identify an existing EEG / neural mass model using Mori-Zwanzig reduction
2. Fill `CASE_TEMPLATE_signature_first.md` for both the StatPhys and Neuro instances
3. Run transfer metrics (RCD, TBS_norm, Φ) between the two cases
4. Check: does matched-ε transfer score Φ improve relative to raw Φ?

**Artifact:** `cases/CASE-YYYYMMDD-NEURO01/` + `docs/art_instantiations/mz_neuro_bridge.md`

**Status:** ❌ Not started

**Acceptance criteria:**
- [ ] Both cases have filled `CASE_TEMPLATE_signature_first.md`
- [ ] Transfer metrics computed (requires `sweep_range` in both `Invariants.json`)
- [ ] Both raw Φ and matched-ε Φ reported (ε-mismatch expected)
- [ ] Signature overlap (S1, S5) documented as the structural basis for transfer

---

## Progress Tracker

| Action | Artifact | Status | Blocker |
|---|---|---|---|
| 1 — Signature catalog | `docs/advanced/operator_signature_catalog.md` | ✅ complete | — |
| 2 — Case triads | `docs/art_instantiations/triad_S{N}_*.md` | ❌ not started | Needs case stubs |
| 3 — Invertibility (Q15) | `docs/notes/experiment_Q15_invertibility.md` | ❌ not started | Needs protocol |
| 4 — QM stress test | `cases/CASE-…-QM01/` | ❌ not started | Needs QM case setup |
| 5 — F5 test case | `docs/notes/experiment_F5_scope_exhaustion.md` | ❌ not started | Needs candidate case |
| 6 — Neuro/EEG bridge | `cases/CASE-…-NEURO01/` | ❌ not started | Needs EEG model reference |

---

*Generated from: "Gleiche Operator-Signaturen in vielen Domänen" (project resource, 2026-03-14)*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
