---
status: working-definition
layer: docs/cognitive_architecture/
---

# Anchor Memory

## Definition

An anchor is a stored association between a context embedding,
a behavioral mode, and the stability properties of that association.

```
anchor = (context_embedding, mode_id, outcome_statistics, stability_score)
```

Anchor memory is the agent's collection of stored anchors,
built up through experience and sharpened during consolidation.

---

## Formal Role in ARW

In ARW terms, an anchor is a stored scope-partition association:

```
anchor ≡ (context_embedding ↔ regime class Rᵢ under S_context)
```

The context embedding is a point in the projection space Π_B.
The mode is the behavioral regime that was dominant when this
context was previously encountered.

Anchor memory is therefore a **stored approximation of the local partition**
around previously visited states — a cache of prior scope assignments.

---

## Formation

An anchor forms when:

1. The agent has occupied a context region for sufficient episodes
2. The mode active in that region has remained stable across episodes
   (stability_score exceeds formation threshold τ_form)
3. A consolidation phase (sleep) confirms the association

```
formation condition:
  context_embedding stable across k episodes
  AND mode_id constant across those episodes
  AND stability_score(context, mode) > τ_form
  → anchor formed during next consolidation
```

Anchors do **not** form mid-episode from single observations.
They require consolidation — the offline phase that stabilizes
episodic experience into durable associations.

This is the ARW interpretation of why sleep matters:
consolidation sharpens the partition boundary around the anchor,
increasing stability_score by reducing within-class variance.

---

## Retrieval

Anchor retrieval is triggered when the current context embedding
is sufficiently similar to a stored anchor:

```
retrieval condition:
  sim(current_context, anchor.context_embedding) > τ_retrieve
  → activate anchor.mode_id
```

Retrieval is the agent performing a **scope lookup** rather than
re-deriving the appropriate regime from scratch.
It is fast (constant-time relative to learning) precisely because
it bypasses the partition derivation step.

**Salience and retrieval:**
When multiple anchors are sufficiently similar to the current context,
they compete. Salience is the competition signal —
high salience = ambiguous scope assignment = multiple candidate regimes.

---

## Stability Score

```
stability_score(context, mode) ∈ [0, 1]
```

Updated after each episode:
- Increases when mode_id is consistent with prior activations in this context
- Decreases when mode switches occur within the context region
- Reset toward 0 if the context-mode association becomes inconsistent

High stability_score: this anchor is a reliable scope assignment.
Low stability_score: the context-mode mapping is unstable — the partition
boundary may be running through this region.

**ARW interpretation:**
A low stability_score at a context location indicates that the scope
is near a partition boundary — the state is ambiguous between regime classes.
This is directly analogous to states near the boundary of R_S
where [x]_S is unstable under small perturbations.

---

## Decay and Pruning

Anchors are pruned when:
- stability_score falls below a minimum threshold across multiple episodes
- The context region is not visited for a long time (temporal decay)
- A consolidation phase identifies the anchor as inconsistent with
  surrounding anchors (structural pruning)

This prevents the anchor memory from accumulating stale scope assignments
after the environment has changed — i.e., after a scope transition
has rendered old partition associations inadmissible.

---

## Cross-Episode Transfer

Anchors formed in Maze 1 are available in Maze 2.
Transfer is admissible when the structural context (zone type, motif)
is preserved across mazes, even if visual appearance changes.

Formally: transfer is admissible if the partition compatibility condition holds
between the old maze's scope S_maze1 and the new maze's scope S_maze2:

```
[x]_maze1 ⊆ [x]_maze2   for contexts x in structurally similar zones
```

Anchor retrieval rate in new mazes is therefore a direct empirical
test of cross-scope partition compatibility.
High retrieval rate → high compatibility → admissible transfer.

---

## Relation to Sleep / Consolidation

| Phase | Anchor effect |
|---|---|
| During episode | Anchors retrieved; stability scores updated |
| Post-episode (consolidation) | Stable associations formalized; unstable anchors pruned |
| Between mazes | Anchors available for retrieval; compatibility untested until encounter |

Sleep does not create new knowledge — it stabilizes existing associations
into more robust partition structures. This is the ARW account of
memory consolidation as partition sharpening.

---

*For the full agent architecture, see [agent_architecture_mode_ecology.md](agent_architecture_mode_ecology.md).*
*For the experimental protocol testing anchor transfer, see [experiments/labyrinth_experiment_agenda.md](../../experiments/labyrinth_experiment_agenda.md).*
