---
status: working-definition
---

# Resonance

## Definition

Resonance is the mechanism by which boundary conditions enable coherent
accumulation of influence between degrees of freedom.

Under compatible boundary conditions, interactions between degrees of
freedom do not cancel but compound — they build stable, repeating patterns.
Resonance is the condition under which this coherent accumulation is possible.

```
resonance: B compatible with interaction structure
→ degrees of freedom accumulate coherent influence
→ stable patterns form above the resolution threshold ε
→ regime structure emerges
```

## Formal Role in ARW

Resonance is the mechanism that connects B (boundary conditions) to
the observable regime structure A(S) = R_S.

Boundary conditions do not directly produce regimes — they produce
the conditions under which degrees of freedom can resonate.
Resonance is the intermediate step:

```
B (boundary conditions)
→ admissible interactions (which couplings are structurally permitted)
→ resonance (which interactions accumulate coherently)
→ stable patterns above ε
→ regime classes in R_S
```

This makes resonance the *mechanism* of BC-induced regime generation —
not a separate concept, but the causal link between B and R_S.

## Resonance and BC Classes

Each BC class generates a characteristic resonance structure:

| BC class | Resonance condition | Resulting pattern |
|---|---|---|
| Coupling | Frequency matching or phase compatibility | Synchronization (Kuramoto, pendulum R_P4) |
| Restriction | Resource level compatibility | Strategy saturation regimes |
| Symmetry breaking | Asymmetric accumulation | One pattern dominates over equivalent alternatives |
| Forcing | Driving frequency near natural frequency | Entrainment, phase locking |
| Dissipation | Energy removal concentrates dynamics | Attractor formation |

Resonance **fails** when boundary conditions change and the interaction
structure no longer supports coherent accumulation — this is when a
scope loses admissibility. The previously resonant degrees of freedom
decouple; the existing regime structure destabilizes.

## Resonance and Latent Degrees of Freedom

Variables that are not currently resonating are latent — they are
dynamically present but do not accumulate coherent influence above ε.

A scope transition occurs when a latent degree of freedom begins to
resonate under new or changed boundary conditions:

```
latent DOF begins resonating
→ its effects exceed ε
→ current regime structure reorganizes
→ scope transition (possibly emergence)
```

This is the formal ARW account of how new structure "comes into existence":
it was always dynamically present, but began resonating — became visible
above the resolution threshold — only when boundary conditions changed.

## Distinction from Coupling

Resonance is not identical to coupling.

Coupling (BC class) specifies that degrees of freedom *can* influence
each other — it is a structural constraint.

Resonance describes whether they *do* accumulate coherent influence —
it depends on both the coupling structure and the compatibility of their
dynamics (frequencies, phases, timescales).

```
coupling  = structural permission for interaction
resonance = coherent accumulation of that interaction
```

Strong coupling without frequency compatibility produces no resonance
(and no synchronization regime). This is why the Kuramoto model has a
critical coupling threshold K_c — below K_c, coupling exists but
resonance does not.

## Not Identical To

- **Resonance in physics (mechanical/electrical):** In ARW, resonance is a general
  structural concept, not limited to oscillating systems. Any coherent accumulation
  of influence under compatible BCs is resonance in the ARW sense.
- **Correlation:** Correlation is a statistical relationship. Resonance is a
  structural mechanism. Resonance produces correlation, but correlation
  can exist without resonance (spurious correlations, shared external drivers).
- **Coupling (BC class):** See distinction above.

## Open Questions

The formal quantification of resonance remains open (see `docs/notes/open_questions.md`, Q1).
Current treatment is mechanistic rather than metric — resonance is identified
by its effects (stable patterns, regime formation) rather than measured directly.

A candidate formalization: resonance could be quantified as the rate of
coherent influence accumulation, normalized by ε. This would give a
continuous resonance strength that crosses a threshold when regime structure forms.

## Related Concepts

- [boundary_conditions.md](boundary_conditions.md)
- [latent_degrees_of_freedom.md](latent_degrees_of_freedom.md)
- [scope_transition.md](scope_transition.md)
- [resonance_field.md](resonance_field.md)
