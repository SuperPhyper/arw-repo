---
status: working-definition
---

# ART Instantiation: Labyrinth Extended Design
## Regime-Forcing Environment — Constraint Zones as Explicit BC Classes

This document extends [labyrinth_experiment_agenda.md](labyrinth_experiment_agenda.md)
with the full multi-zone environment design. Each constraint zone is formalized
as a distinct BC tuple, producing a spatial regime partition in the environment
itself. The agent must perform intra-episode scope transitions as it traverses zones.

---

## 1 Core Design Principle

A single smooth policy cannot optimally solve an environment whose
regions impose structurally incompatible constraints.

In ARW terms: the environment is designed so that a single scope S_B
cannot remain admissible across all zones. The agent must perform
scope transitions S_B(zone_i) → S_B(zone_j) at zone boundaries.

This makes scope transitions **observable from the outside** —
they manifest as mode switches, salience spikes, and behavioral discontinuities
that can be measured with the metrics defined in the agenda.

---

## 2 Zone Scopes

Each zone imposes a distinct BC tuple. These are not arbitrary constraints
but carefully chosen to force **qualitatively different regime classes**.

### Zone A — Exploration Scope S_A

```
S_A = (B_A, Π_B, Δ_B, ε_B)
```

**B_A:**
- Action cost: low (c = 0.05 per step)
- Visibility radius: large (r = 5 cells)
- Error penalty: minimal
- No traps or irreversible states

**Admissible regime under S_A:** R_B1 (Exploration)

Exploration is admissible because:
- low cost makes coverage cheap
- large visibility enables map construction
- no traps make errors recoverable

Deliberative planning (R_B2) is *inadmissible* — it wastes planning budget
on a zone where exploration dominates.
Reactive mode (R_B4) is *inadmissible* — large visibility makes local-only sensing
suboptimal.

**Scope boundary trigger:**
Entering a corridor with reduced visibility drops r below S_A admissibility.
Salience spike expected at this boundary.

---

### Zone B — Deliberative Scope S_D

```
S_D = (B_D, Π_B, Δ_B, ε_B)
```

**B_D:**
- Action cost: high (c = 0.5 per step)
- Narrow corridors with traps
- Wrong-turn penalty: severe
- Planning budget: required for safe navigation

**Admissible regime under S_D:** R_B2 (Deliberative)

High action cost makes exploration expensive.
Traps make reactive behavior (R_B4) catastrophic.
Only deliberative planning — which minimizes wrong turns — is structurally admissible.

**Key ARW property:**
B_D does not merely *reward* deliberative behavior.
It makes exploration and reactive behavior *inadmissible* —
the expected return under those regimes falls below the scope threshold.

**Scope boundary trigger:**
Exiting to a low-cost zone — action cost drops below the threshold
that makes deliberation worth its computational cost.
This is a **BC relaxation** that allows re-entry into R_B1.

---

### Zone C — Anchor Retrieval Scope S_C

```
S_C = (B_C, Π_B, Δ_B, ε_B)
```

**B_C:**
- Repeated structural motifs (T-junctions, right-angle corridors)
- Identifiable landmarks at fixed positions
- Memory capacity: required (m ≥ 3 anchors)
- Motif recurrence: same substructure appears 3–5 times per maze

**Admissible regime under S_C:** R_B3 (Anchor retrieval)

When the current context matches a stored anchor, retrieval dominates:
it is faster than planning and more reliable than exploration.
Without memory (m = 0), anchor retrieval is *inadmissible by definition* —
the BC suppresses the mode.

**Key ARW property of this zone:**
Zone C is the primary test of the cross-maze transfer hypothesis.
The structural motifs in Zone C are preserved across maze instances —
only their spatial arrangement changes.

This means: anchors formed in Zone C of Maze 1 should be compatible
with Zone C of Maze 2. This compatibility is the formal admissibility
of the prior partition applied to the new maze.

**Transfer admissibility prediction:**

```
R_B(maze_1, Zone C) compatible with R_B(maze_2, Zone C)
↔ structural motifs are preserved across maze instances
```

This is directly measurable: anchor retrieval rate in new mazes
should be high in Zone C and low in structurally dissimilar zones.

---

### Zone D — Reactive Scope S_R

```
S_R = (B_R, Π_B, Δ_B, ε_B)
```

**B_R:**
- Visibility radius: minimal (r = 1 cell)
- Partial observability: agent cannot see around corners
- Ambiguous intersections: multiple paths look identical
- Planning budget: ineffective (no useful lookahead under r=1)

**Admissible regime under S_R:** R_B4 (Reactive)

Global planning is *inadmissible* — the agent cannot build a reliable
internal map with r=1 visibility. Anchor retrieval is *inadmissible* —
ambiguous intersections cannot be reliably matched to stored contexts.

Only local reactive behavior — responding to immediately visible information —
remains admissible.

**Scope boundary trigger:**
Visibility restoration (exit to Zone A) immediately makes R_B4 suboptimal.
Transition S_R → S_A is expected to be fast — R_B4 loses admissibility
as soon as global information becomes available.

---

## 3 Spatial Scope Partition

The full maze induces a **spatial regime partition** — a partition of
the maze cells by zone type:

```
A(S_environment) = { Zone A cells, Zone B cells, Zone C cells, Zone D cells }
```

This is an environmental regime partition independent of the agent.

The ARW prediction is that the **agent's behavioral partition**
aligns with the **environmental partition**:

```
A(S_B) aligned with A(S_environment)
↔ behavioral modes track structural BC classes
```

Misalignment is informative: it identifies regions where the agent's
internal scope does not respond to the environmental BC change.

---

## 4 Intra-Episode Scope Transitions

A single episode traversing all four zones requires three scope transitions:

```
S_A → S_D → S_C → S_R
(or any ordering depending on maze layout)
```

Each transition is a **admissibility failure** of the prior scope
followed by **re-stabilization** under a new scope.

**Transition sequence prediction:**

| Event | ARW account |
|---|---|
| Enter Zone B from Zone A | S_A loses admissibility (B_D not compatible with exploration) |
| Salience spike | Competing modes compete — admissibility signal |
| Mode switch to R_B2 | S_D becomes dominant scope |
| Stable navigation in Zone B | S_D holds admissibility |
| Enter Zone C | S_D loses admissibility (motif recognition outperforms planning) |
| Anchor retrieval event | S_C activated via context match |
| Enter Zone D | S_C loses admissibility (visibility collapses) |
| Mode switch to R_B4 | S_R becomes dominant |

---

## 5 Ambiguous Decision Nodes

Certain junctions are designed to be **scope-transition zones** —
points where two competing scopes are simultaneously partially admissible.

Example: junction between Zone B (high-cost) and Zone C (landmark-rich)

At this junction:
- deliberative planning (R_B2) is marginally admissible
- anchor retrieval (R_B3) is marginally admissible
- neither is clearly dominant

**ARW prediction:**
Salience at this junction reflects genuine scope ambiguity —
not noise, but a state where the system is near a partition boundary.
Salience should be *higher and longer-lasting* at ambiguous junctions
than at clean zone transitions.

This is a directly measurable prediction distinguishing the ARW account
from a pure uncertainty model (which would predict salience proportional
to prediction error, not to scope ambiguity).

---

## 6 Dynamic Constraint Shifts

Mid-episode BC changes test whether the agent can perform
unscheduled scope transitions:

| Perturbation | Expected response |
|---|---|
| Visibility suddenly drops from r=5 to r=1 | S_A → S_R transition, salience spike |
| Action cost suddenly doubles | S_A → S_D transition, mode switch to deliberative |
| Memory capacity temporarily zeroed | S_C → S_A or S_D, anchor retrieval suppressed |
| Time pressure activated | All modes accelerated, planning budget compressed |

These are **Δ_B violations** — perturbations outside the admissible range
of the current scope. They force scope transitions that were not
scheduled by the zone structure.

Measuring salience and mode-switch latency under dynamic shifts
tests whether the agent's admissibility signal is sensitive to
arbitrary BC changes, not only to spatial zone boundaries.

---

## 7 Multi-Level Scope Comparison

The extended environment enables a three-level scope comparison:

```
Level 1 — Cell scope S_cell:     individual grid cells, full local detail
Level 2 — Zone scope S_zone:     zone-level structure, agent tracks zone type
Level 3 — Episode scope S_ep:    full episode trajectory, only outcome visible
```

**Admissibility chain prediction:**

```
S_cell → S_zone: admissible when zone boundaries are sharp
S_zone → S_ep:  admissible when episode outcome depends on zone sequence
```

If zone boundaries are blurred (zones bleed into each other),
S_cell → S_zone becomes inadmissible —
the zone-level description distorts the actual constraint structure.

This is tested by varying zone boundary sharpness as an experimental parameter.

---

## 8 Experimental Phases

| Phase | Environment | Goal |
|---|---|---|
| 1 — Mode Emergence | Single uniform zone (one BC tuple) | Verify that discrete partition emerges at all |
| 2 — Zone Switching | Single maze, all four zones | Measure intra-episode scope transitions |
| 3 — Dynamic Shifts | Add mid-episode BC perturbations | Test unscheduled scope transition sensitivity |
| 4 — Transfer | New maze, same zone structure | Measure cross-maze partition compatibility |
| 5 — Structural Variation | New maze, different zone arrangement | Test limits of transfer admissibility |

---

## 9 Key Observables per Phase

| Phase | Primary observable | ARW interpretation |
|---|---|---|
| 1 | Policy embedding cluster count | Partition cardinality |
| 2 | Salience spike locations | Scope transition boundaries |
| 2 | Zone–mode alignment score | Compatibility of S_B and S_environment |
| 3 | Mode-switch latency after perturbation | Admissibility loss detection speed |
| 4 | Anchor retrieval rate in new maze | Cross-maze partition compatibility |
| 5 | PCI decay as structural similarity decreases | Distortion as function of BC mismatch |

---

## 10 Falsification Conditions

The extended design is **specifically** designed to be falsifiable at each phase:

- Phase 1: no clustering → discrete regime structure does not emerge
- Phase 2: mode switches do not align with zone boundaries → BC does not drive regime structure
- Phase 2: salience is uniform across maze → no scope transition signal
- Phase 3: mode-switch latency is insensitive to BC change magnitude → admissibility signal is not graded
- Phase 4: anchor reuse rate is at chance → prior partition is incompatible with new maze
- Phase 5: PCI does not decay with structural dissimilarity → distortion metric is not sensitive

---

*For the scope definitions used here, see [labyrinth_experiment_agenda.md](labyrinth_experiment_agenda.md).*
*For the cognitive architecture connecting these zones to modes, see [docs/context_navigation/agent_architecture_mode_ecology.md](../docs/context_navigation/agent_architecture_mode_ecology.md).*
*For the transfer distortion metrics, see [docs/bc_taxonomy/transfer_distortion_metrics.md](../docs/bc_taxonomy/transfer_distortion_metrics.md).*
