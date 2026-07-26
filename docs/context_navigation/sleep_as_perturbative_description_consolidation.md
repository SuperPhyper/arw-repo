---
status: hypothesis
layer: docs/context_navigation/
depends_on:
  - docs/context_navigation/agent_sleep_scope.md
  - docs/context_navigation/agent_online_scope.md
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/advanced/invariance_as_scope_persistence.md
related:
  - docs/context_navigation/anchor_memory.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
open_questions:
  - Q-SLP-01
  - Q-SLP-02
  - Q-SLP-03
---

# Sleep as Perturbative Description Consolidation

> **Provenance.** Drafted offline in German (2026-07-26), translated on import
> 2026-07-26. Exploratory: this note proposes an *alternative* consolidation
> mechanism for the sleep scope. It does not replace
> [`agent_sleep_scope.md`](agent_sleep_scope.md), which remains the
> working-definition of S_sleep. Promotion beyond `hypothesis` requires the
> discriminating experiment named in §9.

## 1. Starting point

The context-navigation architecture currently treats the sleep phase as
*optimization of existing archetypes against their observed effectiveness*.
`agent_sleep_scope.md` §2 makes this explicit: `progress_rate` is the sole
effectiveness criterion for archetype revision.

This note develops an alternative reading of the same phase:

> Sleep optimizes no preferences and no rewards. Sleep tests the persistence of
> descriptions.

## 2. The weak link in the effectiveness reading

Under the current design, consolidation is driven by an optimization metric:

```
successful encounter → higher effectiveness → archetype reinforced or replaced
```

This accounts only partially for three things the architecture expects of it:

- why *stable* archetypes form at all rather than a drifting effectiveness ranking,
- why archetypes transfer to contexts not represented in the protocol buffer,
- why biological replay varies its content strongly rather than repeating stored
  episodes faithfully.

The third point is the sharpest: under an effectiveness reading, variation during
replay is noise to be minimized. Under the reading below it is the mechanism.

## 3. Persistence as an existence condition

The move is to stop treating persistence as a *property* a description may or may
not have, and treat it as its *existence condition* — which is the position
[`invariance_as_scope_persistence.md`](../advanced/invariance_as_scope_persistence.md)
already takes at the ARW level. A description does not exist because it succeeded;
it exists only insofar as it survives the admissible perturbations Δ.

Applied to the agent: an archetype is not a summary of what worked. It is a
description that has repeatedly survived internal perturbation.

### 3.1 The ordering axis

Persistence always requires an ordering relation, but not necessarily time.
Depending on domain the axis may be encounters, evolutionary generations,
parameter sweep points, experiments, or consolidation cycles. The concrete axis
is interchangeable; the invariant question is not:

> What remains invariant along this ordering axis?

This is the same structure as the ε-induced scope family flow in
[`scope_family_flow_and_kuramoto_limit_audit.md`](../notes/scope_family_flow_and_kuramoto_limit_audit.md)
§2, with the family indexed by consolidation cycle rather than by ε. Whether that
is more than a formal resemblance is Q-SLP-03.

## 4. Replay as perturbation

The proposed inversion:

> Replay does not reconstruct an encounter. Replay perturbs it.

The agent generates variations of a stored encounter — different resources,
different entry points, altered salience weighting, alternative successor states —
and then asks whether the *same description* remains admissible under them.

In scope terms this is a σ_Δ measurement performed offline. Writing D for the
description under test and δ for a generated variation,

```
σ_Δ(D) = sup_{δ ∈ Δ_replay} d_Π( D(e), D(e + δ) )
```

with Δ_replay the agent's internal perturbation set over the encounter buffer.
The consolidation criterion becomes σ_Δ(D) < ε rather than `progress_rate(e)` high.
Note that this makes the admissibility of Δ_replay itself load-bearing — see
Q-SLP-01.

### 4.1 Dreams

This supplies a candidate functional reading of biological dreaming. Dreams are
frequently unrealistic — places merge, persons substitute for one another,
causal structure bends — while the same semantic structures persist across the
distortion. That is what one would expect if dreams were perturbation tests of
descriptions rather than memory replay. The claim here is only that the reading is
*consistent* with the phenomenology; it is not evidence, and the note does not
assert a neurobiological fact (compare the reverse-inference caveat in
[`kht_prescopal_substrate_hypotheses.md`](../notes/kht_prescopal_substrate_hypotheses.md)).

## 5. Sleep as falsification rather than optimization

The reframing turns the sleep phase from an optimization process into a
falsification process. The governing question shifts from

> Which description was most successful?

to

> Which description survives the most admissible variations?

This is the same epistemic operation as experimental method: experiments vary
boundary conditions, and theories survive only where their descriptions continue
to carry. The proposal is that sleep performs that operation internally.

## 6. Preference, reinterpreted

Preference need not be learned as a separate object. On this reading:

> Preference is an online estimate of the future persistence of a description.

An agent prefers descriptions that hold across many boundary conditions, remain
admissible in many contexts, and reduce future navigation cost. What is
consolidated during sleep is therefore not preference but descriptions; preference
is the online estimator, not the stored quantity.

## 7. Consequences for the agent architecture

An alternative sleep pipeline, replacing the effectiveness evaluation of
`agent_sleep_scope.md` §2–§3:

1. Select a stored encounter from the protocol buffer.
2. Generate many admissible Δ-perturbations of it.
3. Reconstruct the encounter under each perturbed condition.
4. Test whether the same description remains admissible.
5. Measure Δ-robustness — not the original success.
6. Consolidate those archetypes whose descriptions persist under variation.

Steps 1 and 6 are unchanged from the current design; the substitution is entirely
in 2–5. This is what makes the two readings experimentally separable (§9).

## 8. Relation to existing ARW concepts

The reading connects several terms that are currently handled separately:
Δ-stability, admissibility, archetypes, preference, sleep, and scientific
falsification. All appear as perspectives on one question:

> Which description persists under admissible boundary conditions?

## 9. Discriminating experiment (what would settle this)

The two readings make opposed predictions for archetypes that are *effective but
fragile* — high `progress_rate` on the encounters that produced them, high
σ_Δ under replay perturbation. The effectiveness reading consolidates them; the
persistence reading evicts them. Running both consolidation rules over the same
protocol buffer and comparing transfer performance on held-out labyrinth
topologies is therefore a direct test, and requires no new instrumentation beyond
a Δ_replay generator.

Until that comparison exists, this note stays at `hypothesis`.

## 10. Open questions

Registered in [`open_questions.md`](../notes/open_questions.md).

| ID | Question | Priority |
|---|---|---|
| Q-SLP-01 | By what rule does an agent generate its internal perturbations, and what makes a generated perturbation *admissible*? Δ_replay is currently unspecified, and the persistence criterion is only as meaningful as Δ_replay is principled — an arbitrarily narrow Δ_replay makes every description persistent. | high |
| Q-SLP-02 | How is Δ-robustness operationalized for a symbolic archetype, where d_Π is not given by a metric on a state space? What is the relation between Δ-robustness and admissibility volume? | high |
| Q-SLP-03 | Do archetypes arise from frequency or from survival rate under variation — and is the consolidation-cycle ordering axis (§3.1) a scope family in the sense of `scope_family_flow_and_kuramoto_limit_audit.md`, or only formally analogous? | medium |

## Preliminary core claim

> Descriptions do not become stable because they were successful. They become
> stable because they survive internal and external perturbation along an
> ordering axis.

Sleep would then not be an optimization over past experience but a machine for
estimating future transferability.

---

## Maintenance History

- **2026-07-26**: Imported from `To-REPO/` (drafted offline in German, same day).
  Translated to English per repo language rule. Added §4 σ_Δ formalization, §8
  relation section, §9 discriminating experiment, and Q-SLP-01–03 (prefix was
  unused; distinct from the pre-existing Q-SL-01–04 in `agent_sleep_scope.md`).
  Placed in `docs/context_navigation/` as a companion to `agent_sleep_scope.md`,
  which it does not supersede.
