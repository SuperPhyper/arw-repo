---
status: working-definition
layer: docs/cognitive_architecture/
---

# BC Taxonomy and Cognitive Modes

This document maps the ARW boundary condition taxonomy to the
cognitive processing modes in the context-navigation architecture.

The central claim: the same BC classes that generate characteristic
regime structures in physical systems also generate characteristic
cognitive processing modes in the labyrinth agent.

---

## The Mapping

| BC class | Environmental instantiation | Generated cognitive mode | Mode signature |
|---|---|---|---|
| Restriction | Action cost, visibility limit, memory cap | Reactive (R_B4), Deliberative (R_B2) | High cost → deliberative; low visibility → reactive |
| Coupling | Anchor memory links context to mode | Anchor retrieval (R_B3) | Familiar context activates stored mode via coupling |
| Symmetry breaking | Ambiguous junctions, competing paths | Salience spike / mode competition | No single mode is clearly dominant |
| Dissipation | Policy gradient convergence | Mode stabilization (all modes) | Dissipation contracts policy space toward mode attractors |
| Forcing | Dynamic constraint shifts | Forced regime transition | External BC change forces mode switch regardless of context |
| Aggregation | Episode-level view, coarse evaluation | No specific mode (meta-operation) | Aggregation suppresses intra-episode mode structure |

---

## BC Class → Mode in Detail

### Restriction → Reactive and Deliberative Modes

Restriction is the primary BC class that generates mode differentiation
in the labyrinth agent.

**High action cost (C_cost):**
Restricts admissible strategies to those that minimize wrong turns.
Exploration (high action entropy) becomes inadmissible — each step is too costly.
Deliberative mode (low entropy, planned trajectory) is the only admissible strategy.

```
B_restriction: action_cost = high
→ exploration inadmissible
→ deliberative mode (R_B2) generated
```

**Low visibility radius (C_vis):**
Restricts the observable space. Planning (which requires global information)
becomes inadmissible — the agent cannot build a reliable internal map.
Reactive mode (local sensing only) is the only admissible strategy.

```
B_restriction: visibility = r_min
→ planning inadmissible
→ reactive mode (R_B4) generated
```

**Pattern:** Two different restriction BCs generate two different modes.
This demonstrates that restriction alone produces a **sequential partition**
(reactive → deliberative along the resource dimension).

---

### Coupling → Anchor Retrieval Mode

Anchor memory introduces a coupling between the current context
and stored past contexts. This is a form of BC coupling:
the current state is constrained to be influenced by stored associations.

```
B_coupling: current_context coupled to anchor_memory
→ context-mode association activates
→ anchor retrieval mode (R_B3) generated
```

Without this coupling (no memory), anchor retrieval is structurally inadmissible —
the BC that generates it does not exist.

**Cross-system parallel:** The same coupling BC class generates
synchronization regimes in Kuramoto and anchor-retrieval regimes in the agent.
Both are coupling-induced coherence — one between oscillators, one between
context and memory.

---

### Symmetry Breaking → Mode Competition (Salience)

Ambiguous junctions in the labyrinth implement a symmetry-breaking BC:
two paths are equivalent (symmetric), and no intrinsic feature selects between them.

```
B_sym-break: path_cost(A) ≈ path_cost(B)   [symmetric junction]
→ no mode is clearly dominant
→ salience spike (mode competition)
```

Symmetry breaking resolves this competition: a small cost difference,
a landmark, or a prior anchor tips the balance.

**ARW interpretation:** High salience at symmetric junctions is not noise —
it is the structural signal of a symmetry-breaking BC in the environment.
The mode ecology reflects the environmental symmetry structure.

---

### Dissipation → Mode Stabilization

Policy gradient descent (the learning algorithm) is the cognitive analog
of dissipation: it contracts the policy space toward lower-loss regions.

```
B_dissipation: policy_loss decreases over episodes
→ policy space contracts toward mode attractors
→ discrete modes stabilize (multi-stable partition)
```

Without dissipation (no learning), the policy would explore all of policy space.
With dissipation, it converges to a small set of stable modes —
the basins of the policy loss landscape.

**Sleep / consolidation as enhanced dissipation:**
Consolidation amplifies the dissipative effect by replaying
high-stability experiences and penalizing mode inconsistency.
This deepens the mode attractors — post-sleep modes are more robust
to in-episode perturbations.

---

### Forcing → Forced Regime Transition

Dynamic constraint shifts (mid-episode BC changes) implement forcing:
an external signal that overrides the current BC configuration.

```
B_forcing: constraint_shift(t)
→ current regime cell R_mᵢ loses admissibility suddenly
→ forced regime transition within S_global, regardless of context similarity to anchors
```

**Key distinction from normal mode switching:**
In normal operation, mode switches are internally triggered: the agent's
parameter point moves through S_global until it crosses a partition boundary.
Forced transitions are externally triggered by BC changes that shift the
partition boundary itself, evicting the agent from its current regime cell.

This distinction is testable: forced transitions should show
higher mode-switch latency (the agent must re-identify its regime cell
rather than smoothly transitioning to an anchored one)
and lower initial performance in the new mode (no prior anchor applies).

---

## Summary: BC Taxonomy as Cognitive Architecture Design Principle

The BC taxonomy is not just a classification scheme — it is a
**design principle** for the cognitive architecture:

1. Identify the BC classes present in the target environment
2. Each BC class requires a distinct cognitive mode to handle it admissibly
3. The mode ecology is complete when it covers all BC classes present
4. Salience is the admissibility-loss detector at BC class boundaries

An agent with fewer modes than BC classes in its environment will
systematically lose regime admissibility in some regions —
it will be structurally suboptimal, not just quantitatively suboptimal.

---

## Note: BC Classes as Sub-Scope Properties

**Revision note (see `docs/context_navigation/mode_scope_regime_audit.md` §2.5; Q_NEW_9):**
The BC classes assigned to modes in this document characterize the boundary conditions
that dominate within the regime R_m — they are **sub-scope properties of R_m**
as a partition cell of S_global, not properties of the agent substrate independently
of the scope.

Consequence: if the agent is observed with different observables Π', the same
behavioral mode may appear to have a different BC class (because observable BC
structure and system BC structure are distinct — see K5 in
`docs/advanced/observable_consequences.md`). This is the cognitive-architecture
instance of the open question Q_NEW_9, partially addressed by Q-CNS-07.

Until Q_NEW_9 is resolved, BCManifest entries for cognitive-architecture cases
should document both the system-level BC class (zone type) and the observable-level
BC class (notation for mode_dist, salience_mean, etc.).

---

*For the full mode definitions, see [modal_cognition.md](modal_cognition.md).*
*For the BC class definitions, see [docs/bc_taxonomy/boundary_condition_classes.md](../bc_taxonomy/boundary_condition_classes.md).*
*For the experimental test, see [experiments/labyrinth_experiment_extended_design.md](../../experiments/labyrinth_experiment_extended_design.md).*
