---
status: hypothesis
layer: docs/context_navigation/
title: "Scope-Constructing Agent Architecture — Context Navigation as Description Reorganization"
created: 2026-07-26
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/context_navigation/modal_cognition.md
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/agent_sleep_scope.md
related:
  - docs/context_navigation/context_navigation_model_spec.md
  - docs/context_navigation/agent_architecture_mode_ecology.md
  - docs/context_navigation/salience_mode_ecology.md
  - docs/context_navigation/admissibility_and_mode_selection.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/sleep_as_perturbative_description_consolidation.md
  - docs/context_navigation/transfer_semantics_context_navigation.md
  - docs/art_instantiations/kht_resonance_dialectic.md
  - docs/notes/scope_component_conflict_typology.md
open_questions:
  - Q-SCA-01
  - Q-SCA-02
  - Q-SCA-03
  - Q-SCA-04
  - Q-SCA-05
---

# Scope-Constructing Agent Architecture — Context Navigation as Description Reorganization

> **Status.** Hypothesis. This document proposes an *alternative* formulation of the
> Context Navigation architecture. It does not replace
> [`context_navigation_model_spec.md`](context_navigation_model_spec.md), which remains
> the working-definition of the architecture, nor
> [`agent_online_scope.md`](agent_online_scope.md) /
> [`agent_sleep_scope.md`](agent_sleep_scope.md), which remain the operational
> specifications. It makes a **superiority claim** against the mode-selection framing
> (§1.2) and is promotable only if the discriminating experiment of §14 returns in its
> favour. Same posture as
> [`sleep_as_perturbative_description_consolidation.md`](sleep_as_perturbative_description_consolidation.md),
> which proposes the alternative consolidation criterion this architecture assumes.

---

## 0. Relation to the existing specification

This is not a summary of the existing Context Navigation documents and does not
restate them. The following is already specified elsewhere and is **used, not
redefined**, here:

| Element | Canonical home |
|---|---|
| Observable/perception set, observable vector | `agent_online_scope.md` §2 |
| Weight field w, update rule, clipping/normalization | `agent_online_scope.md` §4 |
| `w_in` / `w_out` as first-class encounter fields | `agent_online_scope.md` §5.1 |
| Saliency triggers, strength, saliency record | `agent_online_scope.md` §3 |
| Encounter protocol record, buffer management | `agent_online_scope.md` §5.2 |
| Archetype library structure and matching rule | `agent_sleep_scope.md` §3, §4.1–4.2 |
| Modes as reduced scopes | `modal_cognition.md` |
| Salience as a property of mode ecology, not of stimuli | `salience_mode_ecology.md` §5 |
| Mode selection / admissibility of operations | `admissibility_and_mode_selection.md`; `context_navigation_model_spec.md` §8 |
| Three-layer memory | `context_navigation_model_spec.md` B4 |
| Labyrinth environment, zone types, ARW observation protocol | `context_navigation_emergent_modes_experiment.md` §1–2 |
| σ_Δ measured offline under replay perturbation | `sleep_as_perturbative_description_consolidation.md` §4 |

What this document contributes is in §8, §9.4, §10, §12 and §13. If §8 turns out to
be data augmentation under a different name (§15, cheap negative), the document should
be superseded rather than repaired.

### 0.1 Notation correction (recorded so it does not recur)

The source sketch for this document carried two deviations from the frozen scope
tuple. Both are corrected here and neither is adopted:

1. **Π and Δ were transposed** — Π was glossed as "admissible perturbations" and Δ as
   a stability or time horizon. Canonically Π is the set of admissible descriptions /
   projections (observables) and Δ is the set of admissible perturbations
   (`docs/glossary/scope.md`, frozen). The sketch used the *correct* semantics
   throughout its substantive sections; only the legend was transposed.
2. **An active observable O was listed as a fifth tuple component.** Π *is* the
   observable set; the currently active observable is π_t ∈ Π_t. The tuple stays
   four-place. This is the same guard already applied to ρ in
   `docs/notes/inductive_strengthening_cascade_closure.md` (ρ is canonical ε, not a
   fifth component).

**Where the weight field lives.** w_t is not a tuple component either. It is a
*structure over* Π — a weighting of the admissible descriptions that selects which
one is active and how the rest are ranked. The scope tuple has no slot for structure
over Π, which is the same gap recorded at ARW level as **Q_NEW_E**
(`docs/notes/scope_component_conflict_typology.md` §8.1). This architecture is
therefore a candidate ART instantiation of that open question: here the structure over
Π is *learned*, where in the controversy setting it is a generator hypothesis. Whether
the two are the same object is Q-SCA-05.

---

## 1. The reframing

### 1.1 The learning target

The existing specification's core hypothesis is that the system *maintains a set of
processing modes* and that cognition is navigation between them by context detection
and mode selection (`context_navigation_model_spec.md` §1).

The reframing proposed here moves the learning target one level down. The agent does
not primarily learn a policy mapping states to actions, nor a selector over a
maintained mode set. It learns **under which descriptions a situation becomes
tractable**, which processing regimes are stable under those descriptions, and when a
switch is required. The action is not the object of learning; it is a product of
whichever context organization is currently stabilized.

```
Encounter → description → scope → mode formation → action → consequences → reorganization
```

Modes are not components installed in the agent. They are the recurring solutions the
system finds to the problem of constructing an actionable world under changing
boundary conditions.

### 1.2 The superiority claim (stated as a claim)

> **C-SCA.** An agent whose architecture is description construction, with modes as a
> derived result, will produce behavioural regimes that transfer to environments with
> a preserved BC signature better than either (a) an agent with a prescribed mode
> library and a gating selector, or (b) an unstructured policy analysed post hoc.

This is a claim, not a result. It is stated so that it can lose. §14 gives the
experiment, §15 the conditions under which the claim is withdrawn.

Note what C-SCA does *not* assert: that the existing formulation is wrong. Mode
selection is a correct description of the *steady state* of this architecture — once
modes have consolidated, the agent does select among them. The claim concerns where
the modes come from and how they are revised, which is what determines transfer.

---

## 2. Encounter and description construction

The agent receives no fully specified state. It receives an encounter field

```
X_t = { x_t^(1), …, x_t^(n) }
```

of potential observations — spatial relations, contact events, energy, remaining time,
movement cost, progress, uncertainty, internal activations, signals from other agents,
traces of past actions. Not all of these are admissible or relevant simultaneously; an
actionable description has to be *constructed* from the encounter, not read off it.

Construction uses the weight field of `agent_online_scope.md` §4:

```
π_t = π(X_t ; w_t),    w_t a weighting over Π_t
```

The weights are not attention in the usual sense. They co-determine what appears as an
object at all, which differences survive, which past episodes become comparable, and
which action possibilities are visible. The same physical situation is therefore
workable under several descriptions — spatial, resource, hazard, temporal, social —
and these are not specified in advance. They are expected to appear as recurring
stable weighting-and-processing structures.

---

## 3. The active scope

Each processing step constructs a temporary scope

```
S_t = (B_t, Π_t, Δ_t, ε_t),    with active description π_t ∈ Π_t
```

- **B_t** — currently assumed boundary constraints
- **Π_t** — admissible descriptions available for construction
- **Δ_t** — perturbations under which the current description must survive
- **ε_t** — the distinctions that currently count

The scope is not a bag of context information. It is the operative frame within which
the agent settles which differences count, what is treated as stable, which experiences
are comparable, which operations are examined, and — critically — when the description
has failed.

The agent's internal state is then

```
z_t = (S_t, m_t, μ_t)
```

with active scope, current mode, and memory state.

---

## 4. Modes as emergent stability regimes

A mode is not a programmed subpolicy and not a policy head. It is a metastable
organizational regime

```
m = (W_m, Π_m, M_m, A_m, F_m)
```

— characteristic weighting, typical description set, activated memory accesses, locally
admissible operations, known failure signatures. A mode exists when this configuration
recurs with sufficient stability across a family of similar encounters:

```
m(X + δX) ≈ m(X)    for δ ∈ Δ
```

A mode is therefore defined by the perturbation range under which it keeps processing
stable, not by having been given a name. Labelling is downstream of function. This is
`modal_cognition.md`'s "modes are reduced scopes" read from the construction side
rather than the selection side.

---

## 5. Salience as an indicator of scope failure

Salience is not a conspicuous stimulus. It is the signal that the active description is
losing stability — prediction breakdown, absent progress, resource collapse, unexpected
contact, a critical time bound, two observables generating incompatible action impulses,
a previously ignored parameter becoming effective.

Salience does not trigger an action. It triggers a **scope audit**:

```
salience → scope audit → { adjust mode | switch mode | form new mode | mark encounter unresolved }
```

The fourth branch matters and has no counterpart in the existing selection mechanism:
an encounter may be recorded as *not currently describable*, which makes it a
high-priority candidate for recapitulation (§9.1) rather than a failure to be averaged
away. Trigger taxonomy and strength grading are `agent_online_scope.md` §3.

---

## 6. Local action construction

The agent needs action selection but does not need it organized as a global policy.
Instead of π(a | s):

```
a_t = argmax_{a ∈ A(S_t, m_t)}  Q_local(a ; S_t, m_t, μ_t)
```

`A(S_t, m_t)` is not a constant action set but the operations that are meaningful under
the current scope. The question the agent answers is not "which action is optimal in
this state" but "which operation preserves or improves the admissibility of my
continued navigation under the present description".

A minimal local evaluation:

```
J(a) = α·P(a) − β·C(a) − γ·R(a) + η·I(a)
```

with expected progress, cost, risk of regime loss, and expected information gain. The
weighting may itself be mode-dependent; an exploratory and an escape mode need not
share it.

---

## 7. Memory

Working memory (`μ_work = (S_t, m_t, σ_t, h_{t−k:t})`) and the encounter protocol are
specified in `agent_online_scope.md` §5.2 and `context_navigation_model_spec.md` B4.
One extension is required here: the protocol record must retain the **entry and exit
scope**, not only the entry and exit weights.

```
e_i = ( X_i, S_i^entry, m_i^entry, T_i, S_i^exit, m_i^exit, r_i, F_i )
```

with T_i the internal transformations traversed and F_i the observed failure signature.
The reason is §8: recapitulation varies the scope of a stored encounter, which is
impossible if only w_in/w_out were kept. Two physically similar episodes described
differently carry different learning content, and the current protocol cannot
distinguish them.

The consolidated regime memory (`agent_sleep_scope.md` §3, archetype library) gains the
same extension: an entry is

```
c_j = (Σ_j, W_j, F_j, T_j, ρ_j)
```

— BC signature, typical weighting, known failure signatures, successful transformations,
empirical stability. An entry then reads: *under this boundary-condition signature, this
descriptive organization has repeatedly permitted stable navigation.*

---

## 8. Recapitulation, not replay

This is the core of the proposal and the part with no predecessor in the repository.

The existing sleep phase does **not** replay at all: `agent_sleep_scope.md` §4 compares
*recorded* protocols against archetypes by `progress_rate` and applies a
winner-takes-place revision. `sleep_as_perturbative_description_consolidation.md` §4
does replay, under δ ∈ Δ_replay, but in order to measure σ_Δ of a description against a
consolidation criterion. Neither varies the **scope** of the stored encounter.

Classical experience replay repeats stored transitions (s_t, a_t, r_t, s_{t+1}).
Recapitulation instead re-organizes a complete encounter under controlled variation of
its scope:

```
e_i′ = ℛ( e_i ; δB, δΠ, δε, δw )
```

varying boundary conditions, the admissible description set, the resolution threshold,
and the weighting — while the perturbation set Δ remains the axis along which stability
is *measured*, per §10.

The questions the offline phase asks are correspondingly different from "what was the
return":

- What would I have seen under a different weighting of Π?
- Which boundary condition was actually causally relevant, and which features were
  merely correlated?
- Under which perturbation does the mode break?
- Would a different scope have made the same encounter navigable?
- Which episodes share a signature despite different surfaces?

The purpose is not to reproduce an episode but to expose its invariants and its failure
boundaries. That is the same move the ARW pipeline makes on physical systems — an
ε-sweep is a controlled variation of the description, not of the system — applied to
stored experience.

---

## 9. The consolidation cycle

### 9.1 Encounter selection

Not all episodes are recapitulated equally often. Priority goes to high salience,
contradictory outcomes, surprising failure, successful new mode formation, low
confidence, mode transitions, and cases with high expected generalizability:

```
p(e_i) ∝ λ₁·|σ_i| + λ₂·U_i + λ₃·N_i + λ₄·T_i
```

with uncertainty U, novelty N, transfer potential T. Encounters marked *unresolved* by
the fourth branch of §5 enter at maximum priority.

Note that `agent_sleep_scope.md` §4.1 currently *filters* protocols (excluding short or
resource-depleted ones) but does not *prioritize* them. Prioritized selection is an
extension, not a replacement.

### 9.2 Counterfactual reconstruction

The episode is re-run under changed scopes. Full high-fidelity world simulation is not
required; four levels are available and differ in cost and fidelity: actual environment
simulation, a learned world model, symbolic or relational reconstruction, and internal
activation reconstruction. Which level suffices for signature extraction is Q-SCA-02.

### 9.3 Signature extraction

From the variants: which boundary conditions determine the regime, which parameters may
vary, which observables are interchangeable, which combination triggers the transition,
and which failure signature announces the breakdown. The result is a BC signature

```
Σ_i = (relevant, irrelevant, critical, coupled)
```

which is the same object the physical cases carry as an operator signature
(`docs/advanced/bc_operator_signatures_arw.md`), derived here from experience rather
than from a known generator.

### 9.4 Mode formation and revision

The system may stabilize an existing mode, **merge** two apparently distinct modes,
**split** an over-broad one, mark a special case as a boundary zone, create a new mode,
or **prune** a redundant one.

This is the deferred gap. `agent_sleep_scope.md` §4.3 states explicitly: *"Whether two
archetypes represent the same latent subscope is not decided here — that is
S_observer's analysis after experiment end."* The present proposal moves that decision
into the consolidation phase and gives it a criterion: two archetypes merge when their
stability profiles (§10) overlap above threshold under a shared BC signature; one splits
when its profile is bimodal over Δ.

This is a clustering problem, but not in the space of external states. What is clustered
is *successful organizational forms under similar BC signatures*.

### 9.5 Compression

Not every recapitulation is retained. What is condensed: stable signatures, critical
transitions, minimal descriptions, successful reorganization paths, typical failure
signals. The cycle therefore serves generalization, mode formation, error correction,
forgetting, and transfer checking at once.

---

## 10. The stability profile of a mode

Perturbation is not only a robustness device here. It defines what may count as the
*same* mode. For a mode m:

```
𝒫_m = { δ ∈ Δ : m(S + δ) remains functionally stable }
R_m(δ) = Pr( admissible navigation | m, δ )
```

From R_m one reads a core region, a tolerance region, a transition zone, a failure
boundary, and the neighbouring modes.

**Relation to σ_Δ.** This is the perturbation spread of
`docs/glossary/perturbation_spread.md` applied one level up: σ_Δ^π is defined per
observable, R_m per mode. The construction is the same one used at ARW level for
co-stability of observables —
`docs/notes/scope_component_conflict_typology.md` §8.1 defines
X_stab(π) = {x ∈ X_B : σ_Δ^π(x) < ε}; R_m is its mode-level analogue, and 𝒫_m is the
mode's stability domain in Δ rather than in X_B. Whether the two constructions are
formally the same object at different levels, or merely analogous, is Q-SCA-03.

The system thereby learns a **morphology of its own descriptive capacities** — which is
the object the existing architecture has no representation for, because a maintained
mode library records what the modes are but not where they end.

---

## 11. Four levels of learning

The architecture separates processes that are usually conflated:

| Level | What is learned |
|---|---|
| 1 — operative | better actions within a stable mode |
| 2 — modal | formation and revision of processing regimes |
| 3 — contextual | when which mode or mode combination is admissible |
| 4 — metadescriptive | which observables, thresholds and scope structures should be constructed at all |

Standard RL addresses level 1 and partly level 3. The claim of §1.2 is located at levels
2–4. This table is a framing device, not a mechanism; it is included because the
existing documents do not separate these and the discriminating experiment needs the
distinction to attribute an effect.

---

## 12. Mode transitions as weight displacement

A transition should not be modelled as a switch between discrete controllers. The agent
shifts weights, the description changes, and another regime becomes stable:

```
w_t → w_{t+1}    inducing    m_A → m_{A/B} → m_B
```

The intermediate configuration m_{A/B} is not a transient to be minimized. It may carry
exploration, uncertainty management, conflict resolution, social coordination, and
recalibration. Some situations may require no mode selection at all but a temporary
*coupling* of several modes.

**Cross-reference, not duplication.** This is structurally the R3-mediation pathway of
`docs/art_instantiations/kht_resonance_dialectic.md` §4 on the agent side: a
non-destructive route through an exploratory regime rather than a collapse into the
dual. That document owns the dialectical form; this one records only that the agent
architecture requires a functional intermediate state. Whether they are the same
mechanism is Q-SCA-04.

---

## 13. Multi-agent: description packages and migration

Nothing in `docs/context_navigation/` or `docs/cognitive_architecture/` currently
addresses more than one agent (checked 2026-07-26). This section is therefore new
territory rather than a reframing.

Several agents may span different scopes over the same situation:

```
S_t^(1), S_t^(2), …, S_t^(N)
```

The question is then not only which action is aggregated but **which descriptions are
compatible**. Communication is an exchange of observables, relevance assignments, BC
signatures, failure signatures, regime proposals and uncertainties — not of conclusions.
An agent can report *"under my description the bottleneck is not distance but remaining
energy"*; the receiver need not adopt the conclusion and can instead attempt to
instantiate the proposed scope itself. That is description migration:

```
S^(A)  --τ-->  S^(B)
```

where τ is a transformation preserving the relevant signatures, not a message transfer.

For an aggregable system, agents should not have to synchronize full internal models.
What is exchanged is a compact package

```
D = (Σ, Π_required, F, T, c)
```

— recognized BC signature, required observable structure, expected failure signature,
proposed transformation, and confidence or validity range. Other agents test packages
locally. No central global policy forms; instead a population of context navigators
produces, tests, adopts, modifies and discards regime descriptions.

**Why this is the most load-bearing section.** It is the first setting in which the
robustness reading of the maximin criterion (`kht_resonance_dialectic.md` §5, Q-RD-6)
becomes operational. Two agents holding different generator hypotheses over a shared Π
is exactly the configuration of Q_NEW_E — but here, unlike in discourse, a hypothesis
commits to predictions that the environment resolves within an episode. The
prediction-commitment discriminator proposed at ARW level (Q_NEW_F) is checkable in
simulation. If it fails here, it will not work in discourse either.

---

## 14. Minimal setup and the discriminating experiment

The environment, zone structure and ARW observation protocol are taken unchanged from
`context_navigation_emergent_modes_experiment.md` §1–2 — the labyrinth with zone types
R, C, F, behavioural observable π_action, ε-sweep, partition comparison against zone
topology. Reusing it is deliberate: the comparison below is only meaningful if all arms
are analysed by the same pipeline.

**Three architecture arms:**

| Arm | Agent |
|---|---|
| A | prescribed mode library + gating selector (`agent_architecture_mode_ecology.md`) |
| B | single unstructured policy, regimes read out post hoc (`..._emergent_modes_experiment.md` §1.2) |
| C | scope-constructing agent: weight field, recapitulation, mode consolidation (this document) |

**Two ablation arms within C**, which carry the actual discriminating power:

| Arm | Offline phase |
|---|---|
| C0 | no offline phase |
| C1 | identical episodic replay |
| C2 | scope-varied recapitulation (§8) |

Primary measure: transfer Φ to unseen labyrinth instances with preserved zone topology,
per `transfer_semantics_context_navigation.md` §2.1. Secondary: number of stable modes
against zone-type count, and the width of 𝒫_m relative to the perturbation range seen in
training.

**The sharp prediction.** Scope-varied recapitulation should produce modes whose
stability domain 𝒫_m is *wider than the perturbation envelope encountered during
training* — extrapolative rather than interpolative robustness. C1 should not show this;
identical replay cannot expose a boundary the episode never approached.

---

## 15. What would withdraw the claim

Named first, because it is the cheap outcome:

**Cheap negative — recapitulation is data augmentation.** If C2's advantage over C1 is
entirely accounted for by the additional effective sample count, and 𝒫_m tracks the
training perturbation envelope rather than exceeding it, then §8 is augmentation with
extra vocabulary. The document should then be superseded, not repaired. The measurement
that decides this is the 𝒫_m width comparison in §14, and it must be run with C1 and C2
matched on gradient steps, not on episode count.

**Further falsification conditions:**

- C-SCA fails if arm C does not exceed arms A and B on transfer Φ with preserved BC
  signature. Note this is survivable in one direction: if C matches A but reaches it
  without a prescribed mode library, that is a weaker but real result about where mode
  structure has to be put in.
- §9.4 fails if merge/split decisions driven by R_m overlap produce a mode count that
  diverges from, rather than converges to, the zone-type count.
- §10 fails if R_m is not reliably estimable from the number of recapitulations a
  practical offline budget allows — a sampling problem rather than a conceptual one, but
  fatal in the same way.
- §13 fails if locally tested description packages are adopted at a rate indistinguishable
  from random, i.e. if τ transfers no usable structure.

---

## 16. Open questions

Registered in [`../notes/open_questions.md`](../notes/open_questions.md).

| ID | Question | Priority |
|---|---|---|
| Q-SCA-01 | Does scope-varied recapitulation (§8) produce modes with a stability domain 𝒫_m wider than the training perturbation envelope, or does it reduce to data augmentation once C1 and C2 are matched on gradient steps? This is the primary question; §15 names it as the cheap negative. | high |
| Q-SCA-02 | Which reconstruction level (§9.2 — environment simulation, learned world model, symbolic reconstruction, internal activation reconstruction) is sufficient for signature extraction? Full simulation is assumed to be unnecessary but this is untested. | medium |
| Q-SCA-03 | Is the mode stability profile R_m (§10) formally the same construction as the observable co-stability domain X_stab(π) of `scope_component_conflict_typology.md` §8.1 at a different level, or only analogous? Bears on whether the ART result transfers back to ARW. | medium |
| Q-SCA-04 | Is the intermediate mode m_{A/B} (§12) the same mechanism as R3 mediation in `kht_resonance_dialectic.md` §4, or a distinct agent-level phenomenon that merely resembles it? | medium |
| Q-SCA-05 | The weight field w is a learned structure over Π; a generator hypothesis (Q_NEW_E) is an assumed one. Are these the same object, such that a multi-agent population (§13) is an ART instantiation of the linkage question — or does the learned case lack the property that makes the ARW case tuple-invisible? | high |

---

## 17. Relationship to existing documents

| Document | Relationship |
|---|---|
| `context_navigation_model_spec.md` | Working-definition of the architecture. This document proposes an alternative *core hypothesis* (construction rather than selection) and does not replace it. |
| `agent_online_scope.md` | Operational spec for perception, weights, salience, encounter protocol. Used unchanged except for the scope-retention extension in §7. |
| `agent_sleep_scope.md` | Operational spec for the archetype library and revision. §9.1 (prioritization) and §9.4 (merge/split/prune) extend it; the extension fills a gap that document explicitly defers. |
| `sleep_as_perturbative_description_consolidation.md` | Proposes the σ_Δ consolidation criterion this architecture assumes. Same alternative-formulation posture; the two stand or fall largely together. |
| `agent_architecture_mode_ecology.md` | The prescribed-mode-library architecture. Arm A of §14. |
| `context_navigation_emergent_modes_experiment.md` | Environment, observation protocol and arm B of §14; H4 there is the ancestor of the C0/C1/C2 ablation. |
| `modal_cognition.md` | Modes as reduced scopes — the definition this document reads from the construction side. |
| `salience_mode_ecology.md` | Salience as a property of mode ecology; §5 here adds only the *unresolved-encounter* branch. |
| `transfer_semantics_context_navigation.md` | Supplies the Φ reporting requirements for §14. |
| `scope_component_conflict_typology.md` §8.1 | ARW-level source of the "structure over Π is not in the tuple" claim (Q_NEW_E). §0.1 and §10 connect to it; Q-SCA-03/05 carry the question. |
| `kht_resonance_dialectic.md` | §5/§6.3 supply the maximin readings that §13 would operationalize (Q-RD-6); §4 supplies the R3 pathway that §12 resembles (Q-SCA-04). |

---

## Maintenance History

- **2026-07-26**: Created from a session sketch (drafted by Rico, same day). Filed as a
  standing alternative formulation at Rico's direction — the reframing is held to be
  superior in its core idea, and the formal deviations in the sketch were drift errors
  to be corrected rather than positions to be preserved. Notation corrections recorded
  in §0.1 (Π/Δ transposition; O as a fifth tuple component) so they are not
  reintroduced. §0 delimits the document against the nine existing context-navigation
  files after a section-by-section comparison; material already specified elsewhere is
  referenced, not restated. Q-SCA-01–05 registered (prefix was unused).
