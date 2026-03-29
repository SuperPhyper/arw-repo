---
status: working-definition
layer: docs/overview/
---

# ARW Core Concepts: The Four Scope Components

ARW rests on a single organizing idea: a regime partition is never a property of a
system alone. It is always a property of a *scoped analysis* — a system studied
under specific conditions, with specific instruments, at a specific resolution.

The four components of a scope — B, Π, Δ, ε — make those conditions explicit.
This document introduces each one through examples before defining it formally.

If you have not yet read [why_arw.md](why_arw.md), that document motivates why
these components are needed. This document explains what they are.

---

## B — Boundary Conditions: What states are in scope?

### The intuition

Every empirical study operates within implicit constraints.
An ecologist studying predator-prey dynamics in a nature reserve is not studying
all possible population states — starvation events, external mass migrations,
and disease outbreaks may be excluded by design, not by nature.
A fluid dynamicist studying laminar flow at low Reynolds numbers is working
within a boundary that excludes turbulent states.

These exclusions are not failures of completeness. They are deliberate choices that
define the domain of inquiry. ARW calls this component **B** — the set of
boundary constraints that determines which states X_B ⊆ X are admissible.

### What B does formally

B restricts the state space X to an admissible subset X_B. Any state outside X_B
is out of scope — not because it cannot occur, but because the analysis does not
claim to describe it.

This matters for regime analysis because **the same system can partition differently
under different boundary conditions**. A double pendulum constrained to low-energy
oscillations shows ordered regimes; the same pendulum under high-energy conditions
shows chaotic regimes. The regimes are different not because the physics changed,
but because B changed.

### Common B structures in practice

| Domain | Typical B | What it excludes |
|---|---|---|
| Fluid dynamics | Reynolds number range | turbulent / strongly nonlinear states |
| Ecology | Geographic boundary, carrying capacity | emigration, external forcing |
| Epidemiology | Homogeneous mixing assumption | spatial heterogeneity, network structure |
| Neuroscience | Resting-state condition | task-evoked, anesthetized |
| Coupled oscillators | Identical natural frequencies | frequency detuning |

### Key point

B is not a deficiency of the analysis. It is a prerequisite for making
regime claims precise. A study that does not specify B has implicitly assumed
some B — ARW makes it explicit.

---

## Π — Observables: What are you measuring?

### The intuition

Two researchers studying the same physical transition may reach different conclusions
about how many regimes exist, not because they disagree about the physics, but because
they are measuring different things.

In our double pendulum study, we measured two observables:

- **λ_proxy** — an approximation of the Lyapunov exponent (sensitivity to initial conditions)
- **Var_rel** — relative variance of the angle difference between the two links

At resolution ε = 0.008, λ_proxy resolved one regime across the entire energy range.
Var_rel resolved thirteen. Both observables were applied to the same system under the
same conditions. The disagreement is not about the physics — it is about what is being
measured, and how structurally suited each observable is to the task.

### What Π does formally

Π is the set of admissible observables — functions π: X → Y that map system states
to a descriptive space. Each observable π carries its own **range** R(π): the region
of parameter space where π can reliably distinguish states.

Outside R(π), an observable may compress all variation into a single value (as λ_proxy
did), or produce structurally distorted output. Using an observable outside its range
does not just give a noisy answer — it silently changes the number of regimes you find.

### Observable failure is structural, not just noisy

ARW distinguishes two failure modes for observables:

**F1 — Resolution failure:** The observable's spread of values is smaller than 2ε.
Two states that differ physically look identical under this observable at this resolution.
Fix: choose a different observable or reduce ε.

**F0 — Range failure:** The observable is structurally outside R(π).
Its underlying assumptions are violated by the system state — not due to noise,
but by construction.
Fix: replace the observable with one from a different structural class.

λ_proxy near a phase transition is a classic F0 case: the Lyapunov exponent requires
an infinite-time limit and non-zero separation, both of which are violated exactly
where the transition occurs.

### The observable selection problem

Observable selection is not merely a technical choice. It determines what structure
is visible. ARW asks: *given B and the BC class governing this system, which observables
have R(π) ⊇ B?* This is the formal version of the question that domain scientists
answer informally when they choose their measurements.

---

## Δ — Perturbations: How stable must the partition be?

### The intuition

A regime partition that holds only for exactly one parameter value is not scientifically
useful. We expect regimes to be *robust* — to persist under small changes in initial
conditions, measurement noise, slight parameter shifts, or minor variations in
experimental setup.

But "small change" needs to be specified. A partition that is robust to ±1% parameter
variation may collapse under ±10% variation. A partition that holds under independent
initial conditions may fail under correlated ones.

**Δ** is the set of admissible perturbations — the class of changes under which a
regime partition must remain stable to be considered valid.

### What Δ does formally

A regime partition is valid under scope S only if it is stable under all δ ∈ Δ.
If the partition changes when δ is applied — if the regime boundary θ* shifts,
or the number of regimes N changes — the partition fails the Δ-stability check.

This is formalized as a falsification criterion:

**F2 — Partition not reproducible:** θ* is unstable under Δ. The boundary cannot
be reliably located because it moves under admissible perturbations.
Verdict: scope_rejection (the scope itself is inadequate, not just the observable).

### Δ in practice: what scientists already do

When a physicist checks that their result holds across different initial conditions,
they are implicitly checking Δ-stability. When an ecologist verifies that a population
regime persists across slightly different carrying capacities, they are doing the same.
ARW names this component and makes the perturbation class explicit, so that
the scope of a result is visible in the claim itself.

### Δ and BC classes interact

The perturbations a partition can tolerate depend on the structural constraint
(BC class) generating it. A partition generated by Coupling (e.g., synchronized
vs. incoherent oscillators) may be robust to parameter noise but fragile to
topology changes (e.g., removing coupling links). Specifying Δ correctly requires
understanding what BC class is at work.

---

## ε — Resolution: How fine is your partition?

### The intuition

The Kuramoto model is said to have three regimes: incoherent, partially synchronized,
and fully synchronized. When we swept the resolution threshold ε across 80 values,
we found that this three-regime picture holds only for ε ∈ [0.15, 0.29] — a window
of about 0.70 log-units. Outside this window, the same system partitions differently:

- At ε = 0.001, the order parameter r_ss resolves 13 distinct regimes
- At ε = 0.38, everything collapses to a single undifferentiated regime

The three-regime answer is not wrong. It is *resolution-dependent*. The standard
result implicitly assumes a resolution — it just never says so.

### What ε does formally

ε is the resolution threshold. Two states x, y are **indistinguishable** under scope S
when their observable distance d_Π(x, y) ≤ ε. The partition into regimes is
a partition of the equivalence classes under this indistinguishability relation.

A coarser ε merges nearby states into fewer regimes. A finer ε splits them into more.
There is no single "correct" ε — but there are *better and worse* choices:

- **Robust ε**: an ε for which the partition is stable across a wide interval
  (plateau width w = log(ε_max/ε_min) is large)
- **Fragile ε**: an ε near a plateau boundary, where a small change flips the count
- **Underconstrained ε**: an ε so coarse that all structure is lost

### The plateau structure of ε

Not all regime counts are equally stable. In the Kuramoto analysis, N=5 had
a plateau width of 1.66 log-units — the most stable partition. N=3 had w=0.70.
This means the five-regime partition is more robust to resolution choice than
the textbook three-regime partition, even though the three-regime partition
is the one that matches physical intuition.

ARW treats plateau width as a **scope robustness measure**: the wider the plateau,
the less the regime count depends on the exact choice of ε.

### ε and observable selection interact

The effective resolution is not just ε — it also depends on the observable's spread.
An observable with a very small value range (like λ_proxy in the double pendulum case)
will show few regimes even at small ε, because all states map to a narrow range.
The relevant quantity is the ratio of observable span to ε, not ε alone.
This is why F1 (resolution failure) and F0 (range failure) are distinct: both
produce too few regimes, but for different structural reasons.

---

## The Scope Tuple: S = (B, Π, Δ, ε)

The four components together define a **scope**:

```
S = (B, Π, Δ, ε)
```

A regime partition is always a partition relative to a scope S.
The scope is the full specification of the conditions under which a regime claim holds.

This has a direct implication for how regime claims should be stated and read:

> *"The system has three regimes"*
>
> is an incomplete claim. The complete form is:
>
> *"Under scope S = (B, Π, Δ, ε), the system partitions into three regimes,
> with the boundary at θ* = θ, stable under Δ."*

The scope tuple does not add bureaucratic overhead. It makes visible what was
always implicitly assumed — and makes it possible to compare claims made under
different scopes, to transfer results between systems, and to detect when two
researchers are disagreeing about the scope rather than the physics.

---

## How the Four Components Interact

The components are not independent:

- **B constrains Π**: only observables with R(π) ⊇ B are admissible.
  An observable that collapses within B is out of range (F0).
- **Π constrains ε**: ε must be small relative to the observable's span,
  or all structure is lost (F1).
- **Δ constrains θ***: a partition boundary must be stable under all δ ∈ Δ,
  or the boundary is not real in any scientific sense (F2).
- **B and Δ together define the BC class**: the type of structural constraint
  governing the system's partitioning behavior is visible in how B is defined
  and what Δ the partition can tolerate.

These interactions are what makes scope specification non-trivial — and what makes
the formal framework necessary. Informal descriptions of regime analyses typically
get some components right and leave others implicit. ARW's claim is that leaving
them implicit makes regime results harder to compare, transfer, and falsify.

---

## From Scope to BC Classes

Once a scope is specified, ARW asks a further question: *why* does this system
partition the way it does under this scope?

The answer lies in the **BC class** — the type of structural constraint at work:

| BC Class | Structural mechanism | Typical signature |
|---|---|---|
| Restriction | state space is bounded or filtered | threshold in parameter |
| Coupling | subsystems are interdependent | synchronization, entrainment |
| Symmetry Breaking | parameter change destroys a symmetry | bifurcation, hysteresis |
| Dissipation | energy or information is lost over time | convergence to attractor |
| Forcing | external input drives the system | periodic or irregular drive |
| Aggregation | microscopic states are pooled | mean-field, coarse-graining |

BC classes are not additional assumptions. They are inferences from the scope tuple:
if the scope is well-specified, the BC class that generated the partition is
often recoverable from the observable signature. This is the basis of
ARW's signature-based modeling approach.

---

## Where to Go From Here

- **Formal operator foundation** — how B, Π, Δ, ε arise from three primitive
  operators (composition, product, projection):
  [`docs/overview/arw-operator.md`](arw-operator.md)
- **BC taxonomy** — formal definitions of the six BC classes and their
  observable signatures:
  [`docs/bc_taxonomy/boundary_condition_classes.md`](../bc_taxonomy/boundary_condition_classes.md)
- **Observable range and failure modes** — R(π), Z(π), F0, F1 in detail:
  [`docs/glossary/observable_range.md`](../glossary/observable_range.md)
- **A worked case** — full scope specification for the Kuramoto model:
  [`cases/CASE-20260311-0001/`](../../cases/CASE-20260311-0001/)
