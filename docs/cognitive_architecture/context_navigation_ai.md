---
status: working-definition
layer: docs/cognitive_architecture/
---

# Context Navigation AI — System Map

This document is a compact integration reference for the context-navigation
architecture. It maps each component to its ARW role and shows how
the components connect.

For full component treatments, follow the links in each section.

---

## The Core Claim

An agent operating across structurally different environments cannot
remain admissible under a single scope. It must maintain a structured
set of reduced scopes — one per BC class present in the environment —
and select among them based on the current context.

This is modal cognition: not policy interpolation, but scope selection.

---

## Component Map

```
Environment BC tuple
        ↓
Constraint zones → local BC configuration
        ↓
Context embedding (Π_B projection)
        ↓
Salience estimator ← admissibility-loss signal
        ↓
Mode selection (gating) → active scope S_mᵢ
        ↓
Policy execution under S_mᵢ
        ↓
Anchor memory update ← if context is stable and novel
        ↓
Sleep / consolidation (every N episodes)
        ↓
Partition sharpening → anchor stability scores updated
```

---

## Component → ARW Mapping

| Component | ARW role | Key document |
|---|---|---|
| Constraint zones | Environmental BC tuple; defines which regime is admissible per zone | [labyrinth_experiment_extended_design.md](../../experiments/labyrinth_experiment_extended_design.md) |
| Context embedding | Projection Π_B: maps current state to observable space | [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md) |
| Learnable modes (k policies) | Candidate regime representatives; each mode ≡ S_mᵢ = (B_mᵢ, Π_mᵢ, Δ_mᵢ, ε_mᵢ) | [modal_cognition.md](modal_cognition.md) |
| Salience estimator | Admissibility-loss signal: detects when current scope S_mᵢ is failing | [salience_mode_ecology.md](salience_mode_ecology.md) |
| Gating mechanism | Mode selection = scope activation; maps context → active regime class | [admissibility_and_mode_selection.md](admissibility_and_mode_selection.md) |
| Anchor memory | Stored scope-partition associations: (context, mode, stability_score) | [anchor_memory.md](anchor_memory.md) |
| Sleep / consolidation | Partition sharpening: stabilizes [x]_S boundaries post-episode | [anchor_memory.md](anchor_memory.md) |

---

## Scope Transitions in Operation

A mode switch is a scope transition S_mᵢ → S_mⱼ.

It is triggered when:

1. Salience exceeds threshold (S_mᵢ loses admissibility)
2. A stored anchor matches the current context above τ_retrieve
3. An external BC change forces the transition (dynamic constraint shift)

After transition, the new mode S_mⱼ becomes dominant.
The agent tracks observables in Π_mⱼ and admits perturbations in Δ_mⱼ.
Observables specific to S_mᵢ fall below ε_mⱼ — they are latent under the new scope.

---

## What Makes This Architecture ARW-Grounded

A standard mixture-of-experts or multi-policy agent selects among policies
based on expected return. The mode is a performance optimization.

In this architecture, the mode is a *scope selection* — it determines
which observables are tracked, which perturbations are admitted, and
what resolution distinguishes behavioral states.

The performance difference is a consequence of selecting the structurally
appropriate scope, not the primary objective.

This distinction is testable: the ARW account predicts that mode switches
correlate with environmental BC changes (zone boundaries), not just
with reward signal changes. A standard mixture-of-experts does not
predict this correlation.

---

## BC Classes Present in the Labyrinth

| Zone | BC class | Required mode |
|---|---|---|
| Zone A (exploration) | Restriction (low cost) | Exploration (R_B1) |
| Zone B (high cost) | Restriction (high cost) | Deliberative (R_B2) |
| Zone C (landmarks) | Coupling (anchor-context) | Anchor retrieval (R_B3) |
| Zone D (low visibility) | Restriction (visibility) | Reactive (R_B4) |

Each BC class requires a distinct scope to remain admissible.
An agent with fewer modes than BC classes will systematically lose
admissibility in some zones — not just perform worse, but become structurally
unable to track the relevant partition.

---

*For the full experimental protocol, see [experiments/labyrinth_experiment_agenda.md](../../experiments/labyrinth_experiment_agenda.md).*
*For the BC → mode mapping derivation, see [bc_taxonomy_cognitive_modes.md](bc_taxonomy_cognitive_modes.md).*
