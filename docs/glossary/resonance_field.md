---
status: working-definition
---

# Resonance Field

## Definition

A resonance field is the structured landscape of possible resonance conditions
across a system's parameter space — the map of where and under what boundary
conditions coherent accumulation of influence is possible.

```
resonance field: parameter space → { resonating, non-resonating }
```

It describes not a single resonance event, but the full structure of which
BC configurations permit which degrees of freedom to resonate.

## Role in ARW

The resonance field is the parameter-space view of what the ARW operator
produces point-by-point:

```
A(S(θ)) = R_S(θ)   for each parameter value θ
```

Plotting how regime partitions change across θ traces the resonance field:
regions where regime structure is stable correspond to resonance zones,
and transitions between zones are resonance boundaries — the points where
one resonance pattern gives way to another.

In this sense, the resonance field is equivalent to the **regime graph
embedded in parameter space** — it shows not just which regimes exist,
but where each regime's resonance conditions are satisfied.

## Resonance Field and Regime Transitions

Regime transitions (scope transitions in parameter space) occur at
resonance field boundaries — the parameter values where the resonance
condition for the current regime fails and a new resonance pattern becomes dominant.

```
θ crosses resonance boundary
→ current resonance pattern destabilizes
→ new regime's resonance conditions satisfied
→ scope transition
```

This is the resonance field interpretation of what bifurcation analysis
describes for dynamical systems: bifurcation points are resonance
field boundaries.

## Examples

| System | Parameter θ | Resonance field structure |
|---|---|---|
| Kuramoto | Coupling K | Non-resonant (K < K_c) → partially resonant → fully resonant |
| Pendulum | Driving frequency Ω | Resonance zones near Ω ≈ ω₀, ω₀/2, ω₀/3 (subharmonic resonances) |
| Opinion dynamics | Confidence ε_bc | Resonance of opinion clusters: narrow zones = fragmentation; wide = consensus |
| Labyrinth agent | BC tuple per zone | Each zone defines a local resonance field for mode selection |

## Relation to BC Classes

The resonance field's topology is shaped by the BC class:

- **Coupling BC:** resonance field has a single sharp threshold (K_c)
  separating non-resonant from resonant regions — binary topology
- **Forcing BC:** resonance field has multiple resonance zones at
  rational frequency ratios — Farey sequence structure
- **Restriction BC:** resonance field stratified by resource level —
  each saturation level is a resonance boundary

## Not Identical To

- **Energy landscape:** An energy landscape describes potential energy as a function
  of configuration. A resonance field describes interaction coherence as a function
  of boundary conditions. They are related (resonance often corresponds to energy minima)
  but conceptually distinct.
- **Phase diagram:** A phase diagram maps thermodynamic phases across (T, P) space.
  A resonance field maps regime structure across BC parameter space.
  Phase diagrams are a special case of resonance fields for thermodynamic systems.

## Open Questions

Like resonance itself, the resonance field currently lacks a direct quantification.
The regime partition A(S(θ)) is well-defined, but a smooth field interpolating
between discrete regime assignments — a continuous resonance strength as a function
of θ — has not been formalized.

This is connected to open question Q1 in `docs/notes/open_questions.md`.

## Related Concepts

- [resonance.md](resonance.md)
- [boundary_conditions.md](boundary_conditions.md)
- [regime_partition.md](regime_partition.md)
- [scope_transition.md](scope_transition.md)
