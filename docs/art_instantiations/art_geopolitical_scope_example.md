---
status: working-definition
---

# ART Instantiation: Geopolitical Conflict System
## Persian Gulf — Actor-Level and System-Level Scopes

This document is a concrete ART instantiation of the ARW framework.
It demonstrates scope definition, regime partition extraction, scope transition,
and admissibility analysis applied to a geopolitical system.

It is not a predictive political model. It is a demonstration of how
ARW analytical tools apply to a domain outside physics and engineering.

---

## 1 State Space

Let X be the state space of the Persian Gulf conflict system.

A state x ∈ X is a snapshot of the system at a given time, described by:

- military posture of each actor (deployed forces, readiness level)
- active proxy engagements (location, intensity, actor)
- economic pressure indices (sanctions, energy price, trade flows)
- domestic political stability of primary actors
- control status of maritime chokepoints (Strait of Hormuz)
- active diplomatic channels (open / suspended / broken)

X is high-dimensional and only partially observable.
ART does not require full observability — it requires a scope that
specifies which observables are tracked and at what resolution.

---

## 2 Scope Definition

### Actor-Level Scope S_A

The first scope analyzes the system from the perspective of
individual actors and their admissible strategic regimes.

```
S_A = (B_A, Π_A, Δ_A, ε_A)
```

**B_A — Boundary Conditions**

Constraints that determine which states are structurally admissible
for each actor.

| Actor | Key boundary conditions |
|---|---|
| United States | casualty aversion, public accountability, alliance coordination, global economic exposure |
| Iran | sanctions environment, military asymmetry vs. US air power, territorial familiarity, high attritional tolerance |
| Israel | strike distance constraints, second-front exposure, US alliance dependency, domestic political fragility |

These are not preferences. They are structural constraints that
determine which regimes can be sustained over time.

**Π_A — Observables**

```
Π_A = { actor_posture, proxy_activity, chokepoint_status, diplomatic_channel_state }
```

Each observable maps actor behavior to a measurable feature space.
Regime distinctions must be visible in at least one of these projections.

**Δ_A — Admissible Perturbations**

Perturbations that the regime structure must remain stable under:

- tactical incidents (drone strike, ship seizure) without strategic authorization
- domestic political fluctuations within normal variance
- oil price movements within ±30%

Perturbations that exceed Δ_A (e.g., assassination of a head of state,
nuclear threshold crossing) are scope-transition triggers, not noise.

**ε_A — Resolution Threshold**

```
ε_A: tactical-level distinctions are below resolution
```

Individual skirmishes, single missile exchanges, and proxy incidents
below a sustained-engagement threshold are indistinguishable under S_A.
Only sustained behavioral patterns are resolved.

---

### System-Level Scope S_G

The second scope aggregates actor behavior into system-level observables,
analogous to a mean-field description in physics.

```
S_G = (B_G, Π_G, Δ_G, ε_G)
```

**B_G — Boundary Conditions**

System-level constraints:

- global energy market continuity (Hormuz throughput > threshold)
- nuclear non-use norm (active)
- no direct US-Iran conventional ground engagement

**Π_G — Observables**

```
Π_G = { conflict_intensity_index, chokepoint_throughput, regional_escalation_level }
```

Individual actor identities are suppressed. Only aggregate system
behavior is tracked.

**Δ_G — Admissible Perturbations**

Larger perturbations are admissible at this scope:

- actor-level regime changes within existing system structure
- proxy activity surges below systemic escalation threshold
- single chokepoint disruption events under 72 hours

**ε_G — Resolution Threshold**

```
ε_G >> ε_A
```

Actor-level distinctions (which actor struck, which proxy acted)
are below resolution at S_G. Only system-state changes are visible.

---

## 3 Regime Partition under S_A

Applying the ARW operator to the actor-level scope:

```
A(S_A) = R_A
```

States that remain indistinguishable under Π_A and stable under Δ_A
are grouped into equivalence classes.

The induced partition R_A contains the following regime classes:

| Regime | Behavioral signature | Admissibility |
|---|---|---|
| R_A1 — Contained pressure | Sanctions + periodic air/maritime operations, no proxy expansion | High for all actors |
| R_A2 — Proxy escalation | Active proxy engagement, infrastructure targeting, no direct confrontation | High for Iran, constrained for US/Israel |
| R_A3 — Maritime disruption | Sustained Hormuz interference, tanker seizures | High for Iran, forces US into costly response |
| R_A4 — Precision strike campaign | US/Israel air campaign, limited duration | High for US/Israel, depends on Iran response |
| R_A5 — Regional war expansion | Multi-front engagement, proxy network activation across region | Low for all — requires boundary condition violation |
| R_A6 — Internal destabilization | Domestic pressure operations, political fragmentation targeting | Asymmetrically admissible |

**Key structural observation:**

R_A1 and R_A2 are the dominant stability regions under current boundary conditions.
R_A5 is suppressed — not because actors prefer to avoid it, but because
the boundary conditions of all primary actors make it structurally inadmissible
simultaneously.

---

## 4 Regime Partition under S_G

Applying the ARW operator to the system-level scope:

```
A(S_G) = R_G
```

At the coarser resolution of S_G, actor-level distinctions collapse.
The partition R_G contains three regime classes:

| Regime | System-level signature |
|---|---|
| R_G1 — Stable deterrence | Conflict intensity low, Hormuz open, escalation index below threshold |
| R_G2 — Active systemic stress | Conflict intensity elevated, Hormuz throughput reduced, escalation spreading |
| R_G3 — Systemic breakdown | Nuclear norm under pressure, Hormuz closed, direct great-power confrontation |

R_G3 is structurally suppressed under current boundary conditions —
analogous to a high-energy attractor that is inaccessible without
a large-scale perturbation exceeding Δ_G.

---

## 5 Scope Transition: S_A → S_G

Is S_A → S_G an admissible reduction?

The ARW partition compatibility criterion requires:

```
for every x ∈ D: [x]_A ⊆ [x]_G
```

Each actor-level regime class must be fully contained within
a system-level regime class.

**Checking compatibility:**

| Actor-level regime | Maps to system-level regime | Compatible? |
|---|---|---|
| R_A1 (Contained pressure) | R_G1 (Stable deterrence) | ✓ |
| R_A2 (Proxy escalation) | R_G2 (Active systemic stress) | ✓ |
| R_A3 (Maritime disruption) | R_G2 (Active systemic stress) | ✓ |
| R_A4 (Precision strike) | R_G1 or R_G2 depending on scope | ⚠ partial |
| R_A5 (Regional war expansion) | R_G3 (Systemic breakdown) | ✓ |
| R_A6 (Internal destabilization) | R_G1 or R_G2 | ⚠ partial |

**Result:** The reduction S_A → S_G is *partially admissible*.

R_A4 and R_A6 are not cleanly contained within a single R_G class —
they span a boundary in the system-level partition.
This means the system-level scope loses structural information
precisely about these two regime types.

**ARW interpretation:**
A system-level analysis (e.g., aggregated conflict indices, energy price models)
cannot reliably distinguish precision-strike campaigns from contained pressure,
nor internal destabilization from stable deterrence.
These distinctions require the actor-level scope to remain visible.

---

## 6 The Hormuz Chokepoint as Scope-Transition Trigger

The Strait of Hormuz is not merely a "leverage point" — in ARW terms it is a
**scope-transition boundary**.

Under normal conditions, Hormuz throughput is within Δ_G — a perturbation
the system-level scope absorbs without regime change.

If throughput drops below the admissibility threshold of B_G
(global energy market continuity fails), the system-level boundary
condition is violated:

```
x ∉ X_{B_G}
```

This forces a scope transition: S_G loses admissibility, and the
system must be re-described at a new scope S_G' that includes
energy market disruption as an explicit observable.

The new scope S_G' induces a different partition — R_G3 (systemic breakdown)
becomes accessible that was previously structurally suppressed.

This is the formal ARW account of what is informally described as
"the Hormuz card" — it is not a bargaining chip but a
**scope-transition trigger** that reshapes the admissible regime space.

---

## 7 Pressure-Induced Regime Compression

External pressure (sanctions, military threat) modifies boundary conditions B.

In ARW terms, increasing external pressure on Iran narrows B_Iran:

```
B_Iran → B'_Iran  (more constrained)
```

This has two effects on the regime partition R_A:

1. **Regime compression:** some previously admissible regimes become
   inadmissible — the partition coarsens within Iran's action space
2. **Attractor deepening:** the remaining admissible regimes become
   more stable under perturbation — ε effectively increases for
   regime-internal transitions

The result is a system that appears more stable (fewer visible transitions)
while being structurally more fragile (less capacity to absorb novel perturbations).

This is the formal account of why siege-condition stability is misleading:
partition coarsening under pressure reduces distinguishability,
not genuine system stability.

---

## 8 Falsification Conditions

This ART instantiation makes structural claims that can be evaluated empirically.

The instantiation is **weakened** if:

- Actor behavior does not cluster into stable equivalence classes under Π_A
  (regimes do not form — behavior is purely continuous)
- The partial admissibility finding for R_A4 and R_A6 is wrong —
  i.e., system-level models reliably distinguish precision strikes
  from contained pressure without actor-level data
- The Hormuz scope-transition prediction fails —
  i.e., throughput disruptions do not reorganize the admissible regime space
- Pressure-induced regime compression does not increase structural fragility —
  i.e., externally pressured actors show *more* behavioral flexibility, not less

---

## 9 Relation to Existing Frameworks

| Framework | ARW interpretation |
|---|---|
| Game-theoretic asymmetric conflict models | Emergent effects of asymmetric B — not behavioral laws |
| Balance-of-power theory | Structural stability of R_G1 under current B_G |
| Deterrence theory | Formal suppression of R_A5 and R_G3 by boundary conditions |
| Conflict escalation ladders | Sequence of scope transitions as B conditions are successively violated |

---

*For the formal treatment of admissible reduction, see [docs/core/arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md).*
*For the scope template used here, see [art_scope_template.md](art_scope_template.md).*
