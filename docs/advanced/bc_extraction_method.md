---
status: experiment-proposal
layer: docs/advanced/
related:
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/cross_domain_signature_matrix.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
  - docs/notes/social_bc_extraction_method.md
derived_from: docs/notes/social_bc_extraction_method.md
              + blocker analysis CASE-20260315-SOC1
---

# BC Extraction Method

This document describes a domain-neutral method for identifying boundary conditions
(BCs) in systems where the BC structure is not given explicitly — i.e. where no
governing equations, no natural sweep parameter, and no pre-defined observables exist.

This situation arises in social systems, cognitive systems, ecological systems with
event-driven dynamics, and any domain where the primary data is behavioral,
narrative, or categorical rather than quantitative.

**Level:** ARW (domain-neutral). The method is a formal procedure; its
instantiations for specific domains belong in `docs/notes/` or
`docs/art_instantiations/`.

---

## The Core Problem

The standard ARW pipeline assumes:

```
control parameter θ  →  sweep  →  observable Π  →  regime partition  →  BC label
```

This works cleanly when θ is a physically defined scalar (e.g. coupling strength κ),
Π is a smooth measurable quantity (e.g. order parameter r_ss), and the BC is
suggested by domain theory.

**In many domains, none of these are given.** The system presents as:

- a set of qualitative states or behaviors
- event-driven transitions rather than continuous dynamics
- multiple plausible BC candidates with no natural ranking
- observables that measure inputs or consequences, not regime structure directly

The BC Extraction Method addresses this gap. It provides a structured path from
qualitative observation to a pipeline-admissible case — or to an explicit diagnosis
of why a case is not yet pipeline-admissible.

---

## Two Operating Modes

The method separates two distinct goals that are often conflated:

| Mode | Goal | Input | Output |
|---|---|---|---|
| **Exploration** | Identify BC candidates; map operator signatures | Qualitative observations, behavioral categories, domain knowledge | BC candidate set + operator signature mapping |
| **Formalization** | Construct a pipeline-admissible case | BC candidate set + Pre-Screening result | ScopeSpec + sweep design + observable Π |

**These modes must not be conflated.** Exploration can succeed even when
Formalization is blocked. A complete Exploration result is a valid repo artifact
at `status: hypothesis`. Formalization is only attempted after Pre-Screening
confirms the three pipeline prerequisites are satisfiable.

---

## Pipeline Prerequisites (Pre-Screening)

Before attempting Formalization (Step E), three prerequisites must be assessed.
If any prerequisite is unsatisfied, the case stays in Exploration mode and the
blocker is documented explicitly.

### P1 — Continuous Control Parameter

**Requirement:** A scalar θ ∈ ℝ (or an ordered discrete approximation) must exist
that modulates the BC effect continuously and is not defined only within a single
episode or event.

**Test questions:**
- Does the parameter exist independently of whether the event occurs?
- Can it be varied experimentally or across observations?
- Is it comparable across different instances of the same system?

**Blocker pattern:** Parameter candidates are event-contextual (only defined during
an episode), norm-relative (not comparable across norms), or culturally indexed
(not measurable on a common scale).

**Resolution options:**
- Restrict to a single-context setup where θ is well-defined within that context
- Adopt a proxy parameter that modulates the BC effect indirectly (document the
  approximation explicitly)
- Accept Exploration-only status until a measurement protocol is designed

### P2 — Span-Capable Observable

**Requirement:** At least one observable Π must exist such that `span(Π) ≥ 2ε`
across the regime partition, and Π must measure the BC-induced regime structure —
not the inputs to the BC operators, and not downstream behavioral consequences.

**Test questions:**
- Does the observable change value across the expected regime transition?
- Is it measuring the structural effect of the BC, or something upstream/downstream?
- Can it be operationalized without a belief-elicitation protocol or unmeasurable
  internal states?

**Blocker pattern — three observable failure types:**

| Type | Description | Example |
|---|---|---|
| Input observable | Measures the BC operator's input, not its output | Observer activation (measures G, not E[·\|G]) |
| Consequence observable | Measures downstream behavioral effects | Reputation change (measures outcome, not regime) |
| Internal-state observable | Requires direct access to unobservable beliefs or expectations | Anticipated shame (not externally measurable) |

**Resolution options:**
- Find an observable that correlates with regime structure under the chosen θ-sweep
- Accept a consequence observable as a proxy with explicit documentation of the
  approximation and its limits
- Design a measurement protocol (experiment or dataset) that operationalizes Π

### P3 — Identifiable Primary BC

**Requirement:** One BC class must be identifiable as primary — the one whose
operator signature most directly generates the regime partition under the chosen θ.
Secondary BCs are permitted but must not be co-equal with the primary.

**Test questions:**
- Which BC class is most directly modulated by θ?
- Which BC class generates the transition boundary θ* most directly?
- If multiple BCs are present, do they operate at different timescales or levels
  (allowing one to be primary)?

**Blocker pattern:** Multiple BC classes are simultaneously and equally activated
by the same event, with no natural ranking. This typically occurs when the system
has no single dominant structural mechanism.

**Resolution options:**
- Fix a modeling focus (e.g. "reputation dynamics" → Dissipation as primary)
  and treat other BCs as secondary; document the choice explicitly
- Decompose into sub-cases, each with a single primary BC
- Accept Exploration-only status if no principled ranking is possible

---

## The Method: Steps A–F

### Step A — Behavioral / Qualitative Category Collection

Compile the set of qualitative states, behavioral categories, or transition
indicators that characterize the system.

**Sources (domain-general):**
- empirical observation records
- domain-expert classifications
- historical or cross-cultural stabilized categories
- literature, narrative, or case study descriptions

**Output:** A list of candidate regime indicators with brief descriptions.

**Key criterion:** Prefer categories that are **historically or cross-contextually
stable** — these are more likely to encode compressed structural knowledge rather
than context-specific artifacts.

---

### Step B — Interaction / Transition Scenario Reconstruction

For each category, reconstruct the typical scenario in which it occurs.

**Questions to answer for each category:**

| Question | Purpose |
|---|---|
| What event or condition triggers this state? | Identifies the BC activation mechanism |
| Which components / agents / variables are involved? | Identifies the state space components |
| Which relations between components are relevant? | Identifies coupling structure |
| What constraint or norm is invoked? | Identifies Restriction or Forcing candidates |
| What changes in the available actions or states? | Identifies the BC effect on X |
| What is the temporal structure (instantaneous / sustained / cyclic)? | Identifies S1/S2/S3 distinction |

**Output:** One scenario description per category, structured around the questions above.

---

### Step C — Structural Variable Identification

Translate the scenario into structural components using the four BC identification axes.

| Axis | Structural question | Candidate BC class | Candidate signature |
|---|---|---|---|
| Admissibility | Which states or actions become disallowed? | Restriction | S1: projection onto X_B ⊆ X |
| Coupling | Which components become dynamically linked? | Coupling | S2: product ∘ composition |
| Forcing | Does an external or institutional constraint impose itself? | Forcing | S3: X × T |
| Reduction | Is the state space collapsed to coarser categories? | Aggregation | S1: quotient projection |
| Contraction | Does the system converge toward a target state? | Dissipation | S4: scaling ∘ composition |
| Belief / inference | Does anticipation or expectation of others matter? | Stochastic BC | S5: E[·\|G] |

**Output:** A structural variable table mapping scenario components to axes and
BC candidates.

---

### Step D — Operator Signature Identification

Map the BC candidates from Step C onto ARW primitive operators. Produce a
**BC candidate set** with operator justification for each entry.

**For each BC candidate:**

```
BC class:          [name]
Operator form:     [formal expression using ∘, ×, π, E[·|G]]
Signature:         [S1 / S2 / S3 / S4 / S5]
Activation:        [continuous / event-triggered / episodic]
Idempotent?:       [yes / no / conditional / asymptotic]
Ambiguity:         [note any S_i / S_j ambiguity and its source]
```

**Critical constraints from the operator catalog:**

- A behavioral label is **never** itself a BC — it is an indicator of BC-induced
  regime change
- BC candidate sets may contain multiple entries — do not force a single label
  at this stage
- Idempotence failures and S2/S3 ambiguities are **expected** in systems without
  natural physical dynamics — document them, do not suppress them
- Dissipation → Restriction is only asymptotically valid — never treat S4 as
  implying S1 in finite time

**Output:** BC candidate set with operator justification. This is the final output
of Exploration mode and a valid repo artifact in its own right.

---

### Step E — Pre-Screening

Assess the three pipeline prerequisites P1, P2, P3 against the BC candidate set.

**Pre-Screening decision table:**

| P1 (control param) | P2 (observable) | P3 (primary BC) | Decision |
|---|---|---|---|
| ✅ | ✅ | ✅ | Proceed to Step F (Formalization) |
| ✅ | ✅ | ❌ | Fix modeling focus first; re-assess P3 |
| ✅ | ❌ | ✅ | Design measurement protocol; re-assess P2 |
| ❌ | any | any | Stop; Exploration-only; document blocker B.3 |
| any | ❌ (all types) | any | Stop; Exploration-only; document blocker B.4 |
| ✅ | ✅ | ✅ (after fixing) | Proceed with documented simplification |

**For each failed prerequisite, document:**

```
Blocker ID:        [B.1 / B.2 / B.3 / B.4 / system-specific]
Prerequisite:      [P1 / P2 / P3]
Root cause:        [why the prerequisite cannot be met as-is]
Resolution path:   [what would need to change to unblock]
Scope impact:      [does this invalidate the BC hypothesis, or only the pipeline step?]
```

**A failed Pre-Screening is not a failure of the method.** It is a precise
diagnosis of what the system requires before a pipeline case is possible.
The BC candidate set from Step D remains valid regardless.

---

### Step F — Formalization (only if Pre-Screening passes)

Construct the minimal pipeline-admissible case using `CASE_TEMPLATE_signature_first.md`.

**Minimality principle:** The first formalization attempt should use the simplest
possible setup that passes Pre-Screening:

- Single primary BC
- Single control parameter θ
- Single primary observable Π
- Fewest possible state space components
- Smallest sweep range that captures at least one regime transition

Complexity can be added in subsequent iterations once the minimal case produces
a stable regime partition.

**Formalization checklist:**

- [ ] State space defined with continuous embedding (document any discretization choices)
- [ ] Primary BC and its operator form entered in BCManifest.yaml
- [ ] θ defined, sweep range specified, sweep design documented
- [ ] Primary observable Π operationalized; span estimate provided
- [ ] Perturbations Δ defined
- [ ] ε pre-estimate from expected span(Π)
- [ ] Failure modes F1–F4 documented
- [ ] `go_nogo: pending` set in CaseRecord.yaml

---

## Blocker Taxonomy

The Shame case (CASE-20260315-SOC1) produced a canonical set of blockers.
These recur across domains and are listed here as a reference taxonomy.

| Blocker | Prerequisite | Typical domain context | Resolution class |
|---|---|---|---|
| **B.1** State space partially discrete | P1, P2 | Social, cognitive, linguistic systems | Modeling choice: choose continuous embedding |
| **B.2** No identifiable primary BC | P3 | Event-driven systems; multi-mechanism scenarios | Focus decision: fix modeling target |
| **B.3** No continuous control parameter | P1 | Social norms, cognitive states, cultural categories | Protocol design or proxy parameter |
| **B.4** No span-capable observable | P2 | Belief states, internal expectations, latent variables | Measurement protocol or consequence proxy |
| **B.5** Idempotence only conditional | P3 | Regime-switching systems; norm-dependent projections | Accept regime-indexed family {π_k} |
| **B.6** S2/S3 structural ambiguity | P3 | Endogenous activation of exogenous constraints | Explicit modeling choice: fix as S2 or S3 |
| **B.7** Attractor is dynamic (S4) | P3 | Tracking dissipation; reputation-like variables | Treat attractor as slowly-varying S3 signal |

---

## Domain Applicability

The method is designed to apply wherever standard pipeline entry is blocked.
Known applicable domain contexts:

| Domain | Typical blocker | Typical resolution |
|---|---|---|
| Social systems | B.2, B.3, B.4 | Visibility / salience as proxy θ; behavioral proxy Π |
| Cognitive / neural (high-level) | B.3, B.4 | Task condition as θ; response rate or accuracy as Π |
| Ecology (event-driven) | B.1, B.6 | Continuous population density as state; disturbance rate as θ |
| ML latent spaces | B.4 | Probe classifier output as Π; layer depth or regularization as θ |
| Historical / archival systems | B.3, B.4 | Document frequency or institutional index as proxy θ and Π |
| Clinical / psychiatric | B.3, B.4 | Symptom severity scale as θ; behavioral frequency as Π |

---

## Relation to Existing ARW Artifacts

| Artifact | Role in this method |
|---|---|
| `operator_signature_catalog.md` | Reference for Step D operator mapping |
| `cross_domain_signature_matrix.md` | Reference for known domain instantiations of each signature |
| `CASE_TEMPLATE_signature_first.md` | Used in Step F formalization |
| `validation_program_signatures.md` | Actions 2 and 3 are direct applications of this method |
| `social_bc_extraction_method.md` | ART-level instantiation for social domains |

---

## Output Artifacts by Mode

### Exploration output (Steps A–E, Pre-Screening fails or not yet attempted)

```
docs/notes/<domain>_bc_extraction_<system>.md
  status: hypothesis
  contains: Steps A–D results + Pre-Screening blockers
```

### Formalization output (Step F, Pre-Screening passes)

```
cases/CASE-YYYYMMDD-####/
  ScopeSpec_signature_first.md   ← Step F output
  BCManifest.yaml
  CaseRecord.yaml  (go_nogo: pending)
```

---

*Derived from: social_bc_extraction_method.md + blocker analysis CASE-20260315-SOC1*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
