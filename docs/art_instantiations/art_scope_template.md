---
status: working-definition
layer: docs/art_instantiations/
---

# ART Scope Template

Use this template to define a concrete ART instantiation.
Each section maps directly to a component of the scope tuple S = (B, Π, Δ, ε).

For a complete worked example, see [art_geopolitical_scope_example.md](art_geopolitical_scope_example.md).

---

## 1 System Description

**Domain:**
What kind of system is this? (physical, social, computational, cognitive, ...)

**State space X:**
What constitutes a state of this system?
List the variables or features that together characterize a system snapshot.

**Modeling level:**
Is this an actor-level, aggregate, or multi-level description?

---

## 2 Scope Tuple S = (B, Π, Δ, ε)

### B — Boundary Conditions

What constraints determine which states are admissible?

- structural constraints (physical laws, resource limits, institutional rules)
- domain constraints (which actors, regions, timescales are included)
- modeling assumptions (what is held fixed)

List each constraint explicitly.
Note which constraints are hard (violation = scope breakdown)
and which are soft (violation = scope stress).

### Π — Observables

What is being measured or tracked?

```
Π = { observable_1, observable_2, ... }
```

For each observable, specify:
- what it measures
- how it maps states to a feature space
- what distinctions it can and cannot make

### Δ — Admissible Perturbations

What perturbations must the regime structure remain stable under?

List perturbations that are considered noise (within Δ) and
perturbations that are scope-transition triggers (outside Δ).

### ε — Resolution Threshold

What is the smallest distinguishable difference between states?

Specify what falls below resolution (indistinguishable within this scope)
and what is resolved (visible as a distinct regime difference).

---

## 3 Regime Partition

Apply the ARW operator:

```
A(S) = R_S
```

List the induced regime classes:

| Regime | Behavioral / structural signature | Admissibility notes |
|---|---|---|
| R1 | ... | ... |
| R2 | ... | ... |

Note which regimes are structurally suppressed by B,
and which are the dominant stability regions.

---

## 4 Scope Transition (optional)

If analyzing multiple scopes, define S' and check compatibility:

```
S' = (B', Π', Δ', ε')
A(S') = R_S'
```

**Compatibility check:**

For each regime class in R_S, does it map cleanly into a single class in R_S'?

| R_S class | Maps to R_S' class | Compatible? |
|---|---|---|
| R1 | R'_? | ✓ / ✗ / ⚠ partial |

**Result:** admissible reduction / inadmissible / partial

If partial: which distinctions are lost at the coarser scope?
What analytical questions become unanswerable at S'?

---

## 5 Falsification Conditions

What empirical findings would weaken or falsify this instantiation?

- Regime structure fails to form (behavior is purely continuous)
- Admissibility prediction is wrong
- Scope-transition triggers do not reorganize the regime space as predicted
- Partition compatibility result is incorrect

---

## 6 Relation to Existing Frameworks (optional)

How do existing models of this domain map onto ARW concepts?

| Existing framework | ARW interpretation |
|---|---|
| ... | ... |
