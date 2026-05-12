---
status: note
layer: docs/cognitive_architecture/
created: 2026-05-09
depends_on:
  - cases/CASE-20260329-0011/
  - cases/CASE-20260330-0012/
  - docs/glossary/scope.md
  - docs/cognitive_architecture/context_navigation_ai.md
  - docs/advanced/observable_decomposition.md
---

## Core Shift

The current environment system produces observable variation, but not yet sufficiently strong policy separation.

The revision goal is therefore:

> Environments should not merely look different — they should selectively preserve or invalidate specific policy substrates.

The central design object becomes:

- scope admissibility
- observable validity
- substrate failure
- local policy emergence

rather than global reward optimization alone.

---

# 1. Central Architectural Principle

The system should move away from:

- global policy aggregation
- monolithic generalized navigation
- averaged latent representations

toward:

- local admissible policies
- persistent archetype libraries
- scope-relative policy selection
- regime-dependent navigation

The intended architecture is therefore:

```text
environment encounter
→ substrate classification
→ archetype selection
→ local policy execution
→ admissibility monitoring
→ scope transition if necessary
```

Global intelligence is not defined as:
> “one policy solving all environments”

but as:
> “stable navigation between locally admissible policies.”

---

# 2. Core Environment Design Philosophy

## Previous issue

The previous environments differ structurally, but many still allow:

```text
generalized “move toward exit” behavior
```

As a result:

- policy specialization remains weak
- archetypes overlap excessively
- local policies fail to stabilize clearly
- emergent scope separation remains weak

---

# 3. New Design Goal

Each environment/cell type should:

1. preserve at least one substrate
2. invalidate at least one competing substrate
3. force a different admissible local policy

A successful environment is therefore an:
> admissibility filter

rather than merely a different map layout.

---

# 4. Environment Classes as Substrate Filters

## OPEN

### Preserved
- d_nav
- v_sight
- long-range visibility
- gradient following

### Invalidated
- wall-following
- edge-contact heuristics

### Intended policy
- cost-field navigation
- direct path optimization

---

## CORRIDOR

### Preserved
- e_edge
- c_contact
- topological path memory

### Invalidated
- direct-line navigation
- naive distance heuristics

### Intended policy
- wall-following
- dead-end avoidance
- corridor topology reasoning

---

## HALFWALL

### Preserved
- v_sight remains high

### Invalidated
- visibility ≠ traversability assumption

### Intended policy
- decoupled perception/action reasoning
- movement verification

---

## COSTPATH

### Preserved
- m_cost
- long-term path optimization

### Invalidated
- shortest geometric path assumption

### Intended policy
- low-cost corridor tracking
- delayed reward acceptance

---

## QUICKSAND

### Preserved
- r_resource
- trajectory memory
- local history dependence

### Invalidated
- static local-cost assumptions

### Intended policy
- cumulative-cost avoidance
- revisitation suppression

---

## OCCLUSION

### Preserved
- memory
- progress estimation
- historical inference

### Invalidated
- local visual guidance

### Intended policy
- memory-guided exploration
- uncertainty navigation

---

# 5. Policy Separation Requirement

A new design criterion:

> A policy successful in one regime should become measurably suboptimal in another regime.

If the same generalized strategy succeeds everywhere, then:

- archetypes cannot separate cleanly
- admissibility boundaries remain weak
- scope transitions remain non-operative

The system therefore requires:
- genuine regime incompatibility
- local optimality conflicts
- substrate-dependent failure modes

---

# 6. Archetype Library Concept

## Key shift

Archetypes are not:
- compressed summaries of a global policy

Instead they are:
- persistent local admissibility structures

Each archetype should contain:

```text
- local policy
- dominant observables
- saliency profile
- admissible substrate assumptions
- failure signatures
- transition triggers
- effectiveness metrics
- scope boundary indicators
```

---

# 7. Environment Pretraining

## Goal

Each environment type should first be trained independently.

Purpose:
- produce strongly differentiated local policies
- stabilize substrate-specific strategies
- produce measurable archetype separation

Only after this phase should environments be mixed.

---

# 8. Persistent Archetype Library

The archetype library should persist across:
- runs
- seeds
- environments
- training cycles

This enables:
- transfer analysis
- admissibility tracking
- scope-transition experiments
- archetype evolution studies

Important:
The library is not a memory cache.
It is a structural repository of admissible local policies.

---

# 9. Scope-Admissibility Interpretation

The simulation should increasingly be interpreted as:

```text
synthetic scope landscape generation
```

rather than:
```text
maze-solving benchmark optimization
```

The maze exists primarily to generate:
- observable collapse
- substrate failure
- regime transitions
- admissibility boundaries
- archetype emergence

---

# 10. F0 / Substrate Failure Interpretation

A key distinction:

Not every saliency spike means:
- uncertainty
- policy competition

Some spikes instead indicate:
> observable invalidation

Examples:
- visibility loses navigational reliability
- local distance heuristic collapses
- wall-following becomes meaningless
- static cost assumptions fail

These correspond to:
- substrate failures
- inadmissible scopes
- F0-type transitions

---

# 11. Intended Long-Term Research Direction

The simulation is not primarily intended to prove a maze architecture.

It is intended as a controlled experimental space for studying:

- scope admissibility
- local policy regimes
- observable validity
- regime transitions
- latent observables
- substrate failure
- archetype persistence
- transfer boundaries
- emergent context navigation

The maze becomes:
> a synthetic laboratory for regime and scope analysis.
