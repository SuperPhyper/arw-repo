---
status: note
layer: cases/CASE-20260315-SOC1/
related:
  - docs/notes/social_bc_extraction_method.md
  - docs/advanced/operator_signature_catalog.md
  - docs/cases/CASE_TEMPLATE_signature_first.md
---

# ScopeSpec — Signature First: Shame Interaction Regime
# CASE-20260315-SOC1

> **Purpose of this document:** First attempt to run the Shame scenario from
> `social_bc_extraction_method.md` through `CASE_TEMPLATE_signature_first.md`.
> Explicit `[BLOCKED]` markers indicate where the template resists — these are
> the methodological friction points, not failures to fill in a field.

---

## 1. System Identification

```
Case ID:       CASE-20260315-SOC1
System name:   Shame interaction regime (norm violation + observer network)
Domain:        EPI / SOC  (social systems)
ARW level:     ART  (concrete social scenario)
```

---

## 2. State Space(s)

The system involves three co-evolving components. Each needs its own space
before any reduction is applied.

```
X_actor:       discrete action space A of the actor
               A = {admissible actions} ⊆ A_full
               Before violation: A = A_full
               After violation:  A = A_restricted ⊂ A_full

X_observer:    observer network state
               O ∈ {0,1}^n  (n = group size; 1 = observing, 0 = not observing)
               or continuous O ∈ [0,1]^n (attention / salience weight)

X_reputation:  reputation variable r ∈ ℝ  (or [0,1] normalized)
               r encodes current social standing of actor in group

Joint state:   X = A × O × ℝ
               (action space × observer activation × reputation scalar)
```

**Immediate problem — state space is partially discrete, partially continuous:**
A is discrete (action set), O is mixed, r is continuous. This is not a standard
smooth dynamical system. The sweep pipeline expects a continuous control parameter
and continuous observables. The discrete action set A is a structural mismatch.

```
[BLOCKED — B.1]
The action space A is discrete and norm-defined. It cannot be directly embedded
in a smooth state space without a choice of representation (e.g. indicator
functions, graph of admissible actions). This choice is not determined by the
system — it requires a modeling decision that is itself a BC (Restriction).
Circular: the BC we want to infer is presupposed in the state space definition.
```

---

## 3. Primitive Operators Present

| Primitive | Present? | Instantiation in this system |
|---|---|---|
| Composition `∘` | ✅ yes | Norm application followed by reputation update: `r ← f(r, violation_event) ∘ g(A, norm)` |
| Product `×` | ✅ yes | Joint state `A × O × ℝ`; actor state couples to observer state |
| Projection `π` | ✅ yes | Norm reduces `A_full → A_restricted`; reputation aggregates observer judgments to scalar |
| Tensor product `⊗` | ☐ N/A | Classical setting; no QM structure |
| Conditional expectation `E[·\|G]` | ✅ yes | Actor's anticipation of group evaluation: `E[group response \| visibility, norm violation]` |

**Note on composition:** The ordering `g` then `f` (norm check → reputation update)
is causally motivated but not formally derived. Two alternative orderings are plausible:
simultaneous update, or feedback loop. This ambiguity affects which BC is primary.

---

## 4. Derived Signatures

### S1 — Projection / Selection

```
Present:       ✅ yes
Form:          π_norm : A_full → A_restricted
               "norm violation event activates projection onto reduced action space"
Sub-signature: admissibility projection (not idempotent in the strict sense — see below)
Idempotent?:   ⚠ partial
```

**Idempotency problem:**
A standard projection satisfies `p ∘ p = p`. Here, applying the norm restriction twice
should return the same restricted set — which holds if the norm is stable. But:
- Norms can escalate: repeated violation may further restrict A
- Norms can relax: time or restitution may restore A toward A_full

The projection is therefore **only conditionally idempotent** — it holds within a
fixed regime but not across regime transitions. This is consistent with S1 as a
signature, but means the BC is regime-dependent, not globally fixed.

```
[BLOCKED — S1.1]
Idempotence holds only within a regime, not across the shame episode.
The projection is better described as a regime-indexed family {π_k} than a
single operator. This needs a richer state representation or an explicit
regime-switching model.
```

### S2 — Product ∘ Composition (Coupling)

```
Present:       ✅ yes
Form:          F(actor_state, observer_state) = (f(a, o), g(o, a))
               — actor behavior changes observer activation;
               — observer activation changes actor's admissible actions
Sub-signature: Cartesian coupling with feedback (bidirectional cross terms)
Cross terms?:  ✅ yes — bidirectional
```

This is the most structurally clean signature in this case. The actor-observer
coupling is a genuine product-space dynamic with cross terms in both directions.
Structurally equivalent to a two-population Lotka-Volterra with asymmetric coupling.

**However:** The coupling strength is norm-dependent. Outside a norm-violation
event, observer activation `o` may be near zero and the coupling effectively
vanishes. This means S2 is **event-triggered**, not continuously active.

```
[BLOCKED — S2.1]
The coupling is conditionally present — it activates on a norm-violation event.
A standard ARW Coupling case (CASE-0001 Kuramoto) has coupling that is
continuously present and modulated by a scalar κ. Here the coupling switches
on/off discretely. This is closer to S3 (Forcing) than S2 (Coupling) in structure.
The boundary between S2 and S3 is unclear in this case.
```

### S3 — Time-Coupled Product (Forcing)

```
Present:       ✅ partial
Form:          The norm violation event acts as a discrete time-indexed forcing:
               X ↦ X × T_event,  T_event = {pre-violation, violation, post-violation}
T structure:   T = {0, 1, 2}  discrete, ordered, non-repeating (single episode)
               or T = ℤ if repeated norm violations are modeled
Exogenous?:    ✅ partially — the violation event is endogenous to actor behavior
               but the norm itself is exogenous (socially imposed)
```

**Endogeneity problem:**
S3 requires that T is exogenous — not determined by X. Here, the violation event
is triggered by the actor's own action, which is part of X. The norm is exogenous,
but its activation depends on X. This is intermediate between S2 (endogenous
coupling) and S3 (exogenous forcing).

```
[BLOCKED — S3.1]
The "forcing" here is norm-triggered, not externally clocked. The norm is
exogenous but its activation is endogenous. No clean S3 instantiation is possible
without either (a) treating the norm as a fully external clock (simplification),
or (b) modeling norm + actor as a joint system (which collapses into S2).
This is a genuine structural ambiguity, not a data gap.
```

### S4 — Scaling ∘ Composition (Dissipation)

```
Present:       ✅ partial — reputation dynamics only
Form:          r(t+1) = (1−λ) · r(t) + λ · judgment(t)
               — exponential decay of reputation toward group judgment
               — λ ∈ (0,1) is the update rate (contraction parameter)
Contraction?:  ✅ exponential decay toward attractor (group judgment average)
Rate c:        c = (1−λ),  0 < c < 1
```

This is the cleanest S4 instantiation: reputation as a leaky integrator over
group judgments, structurally identical to LIF leak term in neuroscience.

**But:** The attractor is not fixed — it tracks the (time-varying) group judgment.
This makes S4 a **tracking dissipation**, not convergence to a static fixed point.
Whether this qualifies as a clean Dissipation BC depends on whether the group
judgment can be treated as a slowly varying external signal (→ S3) or as a
co-evolving state (→ S2).

```
[BLOCKED — S4.1]
The dissipation attractor is itself dynamic (group judgment evolves).
Clean S4 requires a fixed or slowly varying attractor.
Here S4, S2, and S3 are entangled in the reputation dynamics.
```

### S5 — Expectation / Conditional Expectation as Projection

```
Present:       ✅ yes — most naturally
Form:          E[group_response | visibility v, violation severity s]
               Actor forms an expectation over possible group reactions
               conditioned on observable features of the situation
Sub-signature: discrete conditional expectation over observer response distribution
Idempotent?:   ✅ yes — in the L²-projection sense, given fixed G
```

S5 is arguably the most natural signature for shame specifically: shame is
precisely the anticipation of negative group evaluation, i.e. `E[judgment | G]`
where G encodes the observer network state and the norm context.

**Observable problem (Q-SOC-03):** To use S5 as a pipeline observable Π, we need
a measurable proxy for `E[group_response | ...]`. Candidates:

| Candidate Π | Operationalization | Problem |
|---|---|---|
| Self-reported shame intensity | Survey / behavioral rating | Conflates expectation with affective response |
| Behavioral withdrawal rate | Frequency of avoidance behavior | Indirect; many confounds |
| Reputation score change | Pre/post social standing measure | Measures outcome, not anticipation |
| Observer network activation | Fraction of group aware of violation | Measures input G, not E[·\|G] |

```
[BLOCKED — S5.1]  ← Q-SOC-03 confirmed as hard blocker
No candidate Π directly measures E[group_response | G].
All candidates either measure inputs to the expectation (G) or outputs of it
(behavioral consequences). The expectation itself is not directly observable
without a belief-elicitation protocol (e.g. incentivized prediction tasks).
This is a fundamental measurement problem, not a data availability problem.
```

---

## 5. BC Class Labels

| BC Class | Assigned? | Justifying signature | Notes |
|---|---|---|---|
| Restriction | ✅ yes | S1: norm projection `A_full → A_restricted` | Conditionally idempotent only; regime-indexed |
| Coupling | ✅ yes | S2: actor-observer bidirectional cross terms | Event-triggered, not continuously active |
| Aggregation | ✅ yes | S1: reputation aggregates observer judgments to scalar r | Lossy; not invertible |
| Symmetry Breaking | ⚠ partial | S1+S2: norm violation breaks symmetry between actor and observers | Needs formalization |
| Forcing | ⚠ partial | S3: norm as exogenous constraint, event-triggered | Endogeneity ambiguity — see BLOCKED S3.1 |
| Dissipation | ✅ yes | S4: reputation leaky integrator toward group judgment | Attractor is dynamic, not fixed |

**Primary BC class:** `[BLOCKED — B.2]`

```
[BLOCKED — B.2]
Three BC classes are plausible as primary: Restriction, Coupling, Dissipation.
The choice depends on which aspect of shame is modeled:
- If the action space contraction is primary → Restriction
- If the actor-observer activation is primary → Coupling
- If the reputation dynamics is primary → Dissipation

In CASE-0001 (Kuramoto), the primary BC was determined by what the sweep
parameter modulates. Here, no single continuous sweep parameter naturally
emerges that modulates all three signatures simultaneously.
This is the deepest structural blocker in this case.
```

---

## 6. Regime Partition

```
Control parameter θ:   [BLOCKED — B.3]
Sweep range:           [BLOCKED — B.3]
Expected regimes N:    Qualitative proposal: N = 3
                       R1: pre-violation (full action space, low observer activation)
                       R2: violation episode (restricted actions, high observer activation,
                           reputation declining)
                       R3: post-episode (partial restoration or permanent reputation loss)
Transition boundary θ*: [BLOCKED — B.3]
Regime boundaries:      [BLOCKED — B.3]
```

```
[BLOCKED — B.3]
No continuous scalar control parameter has been identified.
Candidates considered and rejected:

  - visibility v ∈ [0,1]:  fraction of group that observes the violation
    → plausible; modulates coupling strength and S5 conditioning
    → problem: violation event must occur for v to be meaningful;
      v is only defined within an episode, not as a global sweep parameter

  - norm salience s ∈ [0,1]: how strongly the norm applies in context
    → plausible; modulates the projection strength in S1
    → problem: norm salience is culturally defined, not measurable on a
      common scale across scenarios

  - violation severity ρ ∈ [0,1]: degree of norm transgression
    → plausible for a single-norm model
    → problem: severity is relative to norm; not comparable across norms

The fundamental difficulty: in physical cases, the control parameter is a
property of the system dynamics (κ in Kuramoto). In social cases, the control
parameter candidates are properties of the norm context, which is exogenous.
A sweep over visibility v is the most tractable candidate — but requires
designing a specific protocol or dataset.
```

---

## 7. Observables Π, Perturbations Δ, Resolution ε

### Observables Π

| Observable key | Formula / description | Primary? | Span estimate | Sufficient? |
|---|---|---|---|---|
| `withdrawal_rate` | Frequency of avoidance / withdrawal behavior in episode | ☐ candidate | [UNKNOWN] | [UNKNOWN] |
| `reputation_delta` | Change in reputation score r pre/post episode | ☐ candidate | [UNKNOWN] | [UNKNOWN] |
| `observer_activation` | Fraction of group actively monitoring actor | ☐ candidate | [UNKNOWN] | [UNKNOWN] |
| `action_space_size` | Cardinality of A_restricted / A_full | ☐ candidate | [UNKNOWN] | [UNKNOWN] |

```
[BLOCKED — B.4]
No observable can be marked primary: true yet.
- withdrawal_rate: indirect; conflates shame with other avoidance triggers
- reputation_delta: measures outcome, not regime structure
- observer_activation: measures input (G), not the BC effect
- action_space_size: A is discrete; ratio is not a smooth observable

The core problem: all candidates measure either inputs to BC operators
or downstream behavioral consequences, not the BC-induced regime structure
directly. This maps exactly onto Q-SOC-03.

Possible resolution: design a measurement protocol that operationalizes
visibility v as the sweep parameter, and uses withdrawal_rate or
reputation_delta as observable Π. Then span(Π) can be estimated empirically.
This requires data — either a behavioral experiment or a social science dataset.
```

### Perturbations Δ

```
Perturbation type:    Variation in observer group composition
                      (different subsets of n observers; same violation event)
Robustness check:     [UNKNOWN — requires empirical data or simulation]
```

### Resolution ε

```
Working ε:            [BLOCKED — no observable defined yet]
Plateau location:     [BLOCKED]
Plateau width w:      [BLOCKED]
Choice justification: [BLOCKED — depends on observable choice]
```

---

## 8. Failure Modes

| ID | Condition | Severity | Action |
|---|---|---|---|
| F1 | `span(ALL π_i) < ε` | `scope_rejection` | Replace observable; see BLOCKED B.4 |
| F2 | Regime partition unstable under observer group variation | `scope_rejection` | Formalize Δ more precisely |
| F3 | No plateau found for any candidate observable | `scope_rejection` | Revisit control parameter choice |
| F4 | Regime transition at boundary of visibility sweep | `sweep_refinement` | Extend v range |
| F5-SOC | BC inference inconsistent across cultural instances of shame | `scope_rejection` | Signals that "shame" encodes multiple distinct BCs across cultures — split into sub-cases |
| F6-SOC | Action space A cannot be embedded in continuous state space | `modeling_block` | Requires alternative state space representation before pipeline can proceed |

---

## 9. Transfer Pre-Assessment

| Target case | Expected RCD | Expected TBS_norm | Expected Φ | Rationale |
|---|---|---|---|---|
| CASE-20260311-0003 (Doppelpendel / Restriction) | 0–2 | [UNKNOWN] | partially_admissible (estimate) | Both cases involve Restriction; but control parameter and observable are incommensurable |
| CASE-20260311-0001 (Kuramoto / Coupling) | 1–3 | [UNKNOWN] | inadmissible (estimate) | Coupling present in both but structural form very different; no common observable scale |

```
[NOTE — transfer]
TBS_norm cannot be computed without sweep_range in both Invariants.json files.
For this case, sweep_range is blocked pending control parameter identification.
Transfer assessment is therefore qualitative only at this stage.
```

---

## 10. Checklist — Pipeline Readiness

- [x] Template sections filled or explicitly blocked with reasons
- [ ] All `[FILL]` markers resolved — **NOT MET: 6 active BLOCKED markers**
- [ ] Primary BC class determined — **NOT MET: B.2**
- [ ] Primary observable identified — **NOT MET: B.4**
- [ ] Control parameter defined — **NOT MET: B.3**
- [ ] ε value inside stable plateau — **NOT MET: depends on B.3 + B.4**
- [ ] `sweep_range` available for Invariants.json — **NOT MET**
- [ ] `go_nogo` in CaseRecord.yaml — **NOT MET: set to `no_go` pending resolution**

**Pipeline readiness: NOT READY**

---

## Summary of Blockers

| ID | Block | Root cause | Proposed resolution path |
|---|---|---|---|
| B.1 | State space partially discrete | Action space A is norm-defined; continuous embedding requires modeling decision | Choose representation (e.g. indicator functions on A); accept modeling choice as ART-level decision |
| B.2 | No single primary BC class | Three BC classes plausible; selection depends on which aspect of shame is modeled | Fix a modeling focus (e.g. "reputation dynamics" → Dissipation as primary) and treat others as secondary |
| B.3 | No continuous control parameter | Social control parameters are norm-contextual and not comparable across scenarios | Adopt visibility v ∈ [0,1] as sweep parameter; constrain to single-norm, single-group setup |
| B.4 | No primary observable | All candidates measure inputs or consequences, not BC-induced regime structure | Design measurement protocol; use withdrawal_rate or reputation_delta as Π under fixed v-sweep |
| S1.1 | Idempotence only conditional | Projection is regime-indexed, not globally fixed | Model as regime-indexed family {π_k}; accept S1 as locally valid |
| S3.1 | S2/S3 structural ambiguity | Norm activation is endogenous | Simplify: treat norm as external clock (pure S3) or as coupled co-state (pure S2); document choice |

---

## Interpretation

This attempt confirms the diagnosis from the `social_bc_extraction_method.md` review:
the template resists most strongly at **Section 6 (control parameter)** and
**Section 7 (observables)** — exactly where the physical cases have the most
traction (a continuous sweep parameter and a clean scalar observable).

The blockers are not all equal in depth:

- **B.1, S1.1, S3.1** are *modeling choices* — they can be resolved by making an
  explicit simplifying assumption. This is acceptable at ART level.
- **B.2** is a *focus decision* — also resolvable by fixing a modeling target.
- **B.3 and B.4** are *measurement problems* — they require either empirical data
  or a designed protocol. They cannot be resolved by assumption alone.

**Recommended next step:** Fix B.2 (Dissipation as primary BC, reputation dynamics
as modeling focus) and B.3 (visibility v as sweep parameter), then assess whether
`reputation_delta` has sufficient span to serve as a primary observable Π.
That reduces the case to a tractable minimal setup:

```
System:      n-agent group; one actor; single norm; visibility sweep v ∈ [0,1]
Observable:  reputation_delta = r(post) − r(pre)
BC:          Dissipation (reputation leaky integrator) with S2 coupling secondary
Expected:    R1 (low v, no reputation effect) / R2 (high v, reputation loss)
             with transition at some v* ∈ (0,1)
```

This is a testable two-regime case — small, but pipeline-admissible in principle.

---

*First attempt: 2026-03-15*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
