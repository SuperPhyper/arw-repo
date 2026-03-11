---
status: draft
---

# Canonical Vocabulary

This table provides the strict ARW definitions alongside informal intuitions
and explicit distinctions from adjacent terms in related fields.

Readers with backgrounds in dynamical systems, reinforcement learning,
or philosophy of science should pay particular attention to the
"not identical to" column.

---

| Term | Strict Definition | Informal Intuition | Not identical to |
|---|---|---|---|
| **Scope** S = (B, Π, Δ, ε) | A tuple specifying admissible states, observables, perturbations, and resolution | The set of choices that define *how* you look at a system | A model, a theory, or a coordinate system — scopes are descriptive conditions, not predictive structures |
| **Regime** | An equivalence class of states under robust indistinguishability within scope S | A stable behavioral mode — "what the system is doing" | An attractor — regimes are scope-relative partitions; attractors are intrinsic dynamical objects |
| **Regime partition** R_S | The full set of equivalence classes induced by A(S) over admissible states | The complete map of behavioral modes visible under a given description | A phase diagram — phase diagrams are domain-specific; regime partitions are scope-relative and formally defined |
| **Admissibility** | A scope S (or observable π) is admissible when suppressed degrees of freedom remain dynamically irrelevant | "This description still works here" | Validity or correctness — admissibility is structural compatibility, not truth |
| **Scope dominance** | A scope S is dominant when it successfully orders the system's relevant degrees of freedom | "This description is in control" | Predictive accuracy — a scope can dominate without being maximally predictive |
| **Scope transition** S → S' | A shift to a new scope when the current one loses dominance | A change in *how the system must be described* | A phase transition — phase transitions are domain events; scope transitions are descriptive shifts that may or may not coincide with them |
| **Boundary conditions** B | Constraints on admissible states that determine which degrees of freedom can accumulate coherent influence | The structural rules the system operates under | Initial conditions — B constrains the *space* of states, not a single starting point |
| **Admissible perturbation** Δ | The set of perturbations under which regime distinctions must remain stable | "What counts as noise" for this description | Noise in a statistical sense — Δ defines robustness requirements, not a probability distribution |
| **Resolution threshold** ε | The smallest distinguishable difference between states under Π | The granularity of the description | Measurement precision — ε is a structural parameter of the scope, not an instrument property |
| **Latent degrees of freedom** | Variables that are dynamically active but suppressed by the current scope | Hidden variables that can wake up | Hidden variables in the quantum sense — these are classical structural variables, not ontological claims |
| **Coarse-graining** | A scope transition Π → Π' ⊂ Π that reduces observable resolution | Zooming out | Mean-field approximation — coarse-graining is a structural operation; mean-field is a specific dynamical approximation |
| **Emergence** | Stabilization of new descriptive structure after a scope loses admissibility | New order becoming visible at a higher scope | Epiphenomenon or irreducibility — emergence in ARW is a descriptive event, not an ontological claim |
| **ARW operator** A(S) | The formal map from scope to regime partition: A(S) = R_S | "Given how you look, here is what you see" | A dynamical evolution operator — A(S) produces structure from description, not trajectories from initial conditions |
| **ART instantiation** | A concrete specification of S = (B, Π, Δ, ε) for a real system | Applying ARW to a specific domain | A model — an ART instantiation is a structured descriptive choice, not a set of equations |

---

## Notes on Adjacent Fields

### Dynamical Systems Theory

Dynamical systems theory studies the intrinsic evolution of systems.
ARW studies how *descriptive choices* shape what structures appear stable.

The two are complementary: ARW can be applied *on top of* dynamical systems
to analyze when and why a given dynamical description remains valid.

Key distinction: basins of attraction are intrinsic dynamical objects.
Regime partitions in ARW are scope-relative — the same system can exhibit
different partitions under different scopes.

### Coarse-Graining in Statistical Physics

Coarse-graining reduces microscopic descriptions to macroscopic ones.
ARW formalizes when such reductions are *admissible*:
a coarse-grained description is admissible when its regime partition
is a compatible coarsening of the fine-grained partition.

### State Abstraction in Reinforcement Learning

State abstraction groups environment states to simplify learning.
In ARW terms, this is a scope transition Π → Π'.
Admissibility corresponds to whether the abstraction preserves
the regime structure relevant for the agent's task.

### Philosophy of Science

ARW provides a formal vocabulary for concepts discussed in
philosophy of science: theory change, perspectivism, levels of description.
It does not replace philosophical analysis but offers structural
precision for some of these discussions.
