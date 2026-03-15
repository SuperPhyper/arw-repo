---
status: experiment-proposal
layer: docs/notes/
related:
  - docs/advanced/bc_extraction_method.md
  - docs/advanced/operator_signature_catalog.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
  - cases/CASE-20260315-SOC1/
instantiates: docs/advanced/bc_extraction_method.md
---

# Social BC Extraction — ART Instantiation

This document is the social-domain instantiation of the general
`bc_extraction_method.md`. It applies Steps A–F of that method to social systems
using historically stabilized behavioral categories as regime indicators.

For the general method, prerequisites, blocker taxonomy, and Pre-Screening
procedure, see `docs/advanced/bc_extraction_method.md`.

---

## ART Context: Why Social Systems

Social systems are a high-value application domain for BC extraction because
standard pipeline entry is almost always blocked (B.2, B.3, B.4), yet the domain
provides unusually rich qualitative structure:

**Cultural stabilization:** Behavioral categories (shame, guilt, defiance, pride,
indignation, envy, loyalty) persist across centuries and cultures. This persistence
suggests they encode **compressed empirical knowledge of recurrent regime structures**
— not arbitrary semantic conventions. They are the social domain's equivalent of
historically validated physical observables.

**High variation:** Large diversity of interaction patterns across cultures and
historical periods provides a broad empirical base for cross-instance comparison
(→ Pre-Screening P3: cross-cultural invariance as BC-level evidence).

**Data abundance:** Ethnography, psychology, history, literature, and social science
datasets provide accessible material without specialized measurement infrastructure.

---

## Step A — Behavioral Category Collection

### Pilot set

`shame, guilt, defiance, pride, indignation, envy, loyalty`

### Sources

- Psychology and behavioral science (emotion research, moral psychology)
- Anthropological emotion vocabularies (cross-cultural affect studies)
- Classical philosophy (Aristotle's *Rhetoric*; Stoic moral psychology)
- Cultural narratives and literature (persistent exemplars of regime transitions)

---

## Step B — Scenario Reconstruction

### Social scenario template

For each behavioral category, the scenario reconstruction answers:

| Question | Social instantiation |
|---|---|
| Trigger event | Which norm is invoked or violated? |
| Components involved | Which actors, roles, and relations are present? |
| Relevant constraint | What social norm, rule, or expectation is activated? |
| State change | What changes in the admissible action space? |
| Temporal structure | Is the constraint instantaneous, sustained, or cyclic? |

### Example — Shame

```
Trigger:            norm violation by actor
Observation:        by socially relevant group (observer network activates)
Components:         actor, observer network, norm, reputation variable
Constraint:         norm defines admissible action space; violation activates sanction
State change:       action space contracts; reputation variable updates negatively
Temporal structure: episodic (discrete event → sustained consequence)
```

### Example — Defiance

```
Trigger:            authority imposes constraint on actor
Observation:        actor resists or violates the constraint publicly
Components:         actor, authority, audience, norm
Constraint:         institutional forcing (S3); actor attempts to reject it
State change:       coupling between actor and authority increases; audience activates
Temporal structure: sustained conflict episode; may be cyclic (repeated defiance)
```

---

## Step C — Structural Variable Identification

### Social structural axes

| Axis | Social instantiation | Candidate BC | Candidate signature |
|---|---|---|---|
| Admissibility | Norm defines permitted actions | Restriction | S1: `π_norm : A_full → A_restricted` |
| Coupling | Observer network activates; social link established | Coupling | S2: actor × observer product state |
| Forcing | Institution or authority imposes external constraint | Forcing | S3: norm as exogenous `X × T` |
| Reduction | Social role or label assigned (e.g. "deviant", "hero") | Aggregation | S1: quotient projection to role label |
| Contraction | Reputation or behavior converges toward group norm | Dissipation | S4: `r(t+1) = (1−λ)r(t) + λ·judgment(t)` |
| Belief / inference | Anticipation of others' evaluation | Stochastic BC | S5: `E[group_response \| G]` |

---

## Step D — Operator Signature Mapping

### Pilot category results

| Category | Primary signatures | BC candidate set | Key ambiguity |
|---|---|---|---|
| Shame | S1, S2, S5 | Restriction, Coupling, Stochastic BC | S2/S3: observer activation is endogenous |
| Guilt | S1, S5 | Restriction, Stochastic BC | S1 idempotence conditional on norm stability |
| Defiance | S2, S3 | Coupling, Forcing | S3 forcing is resisted — partial activation only |
| Pride | S1, S4 | Restriction (inverted), Dissipation | S1 here expands rather than contracts X_B |
| Indignation | S2, S3 | Coupling, Forcing | Directed coupling (actor → authority); asymmetric |
| Envy | S2, S5 | Coupling, Stochastic BC | S5: comparison expectation; S2: rival as coupled state |
| Loyalty | S2, S4 | Coupling, Dissipation | S4: behavior contracts toward in-group norm |

**Note on Pride:** Pride involves an action space that *expands* post-event
(achievement + recognition). S1 is present but inverted relative to the standard
Restriction form. This is a genuine structural variant — not a counterexample,
but a signed projection. Requires explicit note in operator catalog (→ Q-SOC-04).

---

## Step E — Pre-Screening

### Assessment for social domain (general)

**P1 — Continuous control parameter:**

| Candidate θ | Relevant categories | Problem |
|---|---|---|
| Visibility `v ∈ [0,1]` | Shame, indignation | Defined only within episode; needs single-context setup |
| Norm salience `s ∈ [0,1]` | Guilt, shame | Culturally relative; not comparable across norms |
| Authority strength `a ∈ [0,1]` | Defiance, loyalty | Operationalizable in institutional settings |
| Social distance `d ∈ [0,1]` | Envy, pride | Measurable via network data |

**Verdict P1:** Blocked in general; resolvable by fixing single-context,
single-norm setup with a context-internal proxy parameter.

**P2 — Span-capable observable:**

| Candidate Π | Category | Observable type | Limitation |
|---|---|---|---|
| `withdrawal_rate` | Shame, guilt | Behavioral consequence | Indirect; confounded |
| `reputation_delta` | Shame, pride | Outcome measure | Post-hoc; not regime structure |
| `compliance_rate` | Defiance, loyalty | Behavioral proxy | Measures resistance, not BC directly |
| `observer_activation` | Shame, indignation | Input measure | Measures G, not E[·\|G] |

**Verdict P2:** No direct observable available. Consequence observables
(reputation_delta, compliance_rate) are the most tractable under fixed θ-sweep.

**P3 — Identifiable primary BC:**

Blocked for most categories due to simultaneous BC activation. Resolvable by
fixing a modeling focus:

| Category | Recommended primary BC | Modeling focus |
|---|---|---|
| Shame | Dissipation | Reputation dynamics under visibility sweep |
| Guilt | Restriction | Action space contraction under internalized norm |
| Defiance | Forcing | Institutional constraint under authority strength sweep |
| Loyalty | Dissipation | Behavioral contraction toward in-group norm |

**Overall Pre-Screening verdict:** ❌ Blocked in general form.
Resolvable per category by fixing single-context setup, proxy θ, and modeling focus.

---

## Step F — Minimal Formalization Candidates

### Shame — minimal setup

```
System:         n-agent group; one actor; single norm; visibility sweep
θ:              visibility v ∈ [0,1]
Primary BC:     Dissipation  (reputation leaky integrator)
Observable Π:   reputation_delta = r(post) − r(pre)
Expected:       R1 (low v: no reputation effect) /
                R2 (high v: reputation loss)
θ*:             transition at some v* ∈ (0,1)
Data needed:    behavioral experiment or dataset with reputation measure + visibility proxy
```

### Defiance — minimal setup

```
System:         actor + authority + audience; single institutional norm
θ:              authority enforcement strength a ∈ [0,1]
Primary BC:     Forcing  (institutional constraint as S3)
Observable Π:   compliance_rate
Expected:       R1 (low a: defiance regime) /
                R2 (high a: compliance regime)
θ*:             transition at some a* ∈ (0,1)
Data needed:    experimental or observational compliance dataset
```

---

## Open Questions — Social Domain

| ID | Question | Status | Blocks |
|---|---|---|---|
| Q-SOC-01 | Are cross-cultural invariances sufficient evidence for BC-level invariance? | open | P3 cross-instance validation |
| Q-SOC-02 | How is the observer network (S2) formally bounded? | open | B.3 operationalization |
| Q-SOC-03 | Can reputation (S5) be operationalized as a measurable Π? | open | B.4 for Shame case |
| Q-SOC-04 | Does Pride (inverted S1, action space expansion) require a signed projection extension? | open | operator_signature_catalog.md update |
| Q-SOC-05 | Is the S2/S3 ambiguity (endogenous norm activation) resolvable in principle? | open | B.6 resolution |

---

*ART instantiation of: `docs/advanced/bc_extraction_method.md`*
*Derived from: original social_bc_extraction_method.md + blocker analysis CASE-20260315-SOC1*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
