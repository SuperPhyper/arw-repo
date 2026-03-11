---
status: working-definition
---

# ε and Scope Resolution

## Overview

ε is the resolution threshold parameter in the ARW scope tuple:

```
S = (B, Π, Δ, ε)
```

It determines the granularity at which the scope distinguishes states —
the minimum observable difference that constitutes a meaningful distinction.

This document consolidates and sharpens the treatment of ε,
including its interaction with Δ, its role in partition generation,
and its interpretation as a resolution window in real systems.

---

## 1 Formal Definition

Two states x, y ∈ X_B are indistinguishable under scope S if:

```
|Π(x) − Π(y)| < ε
```

They are assigned to the same regime class: x ~_S y.

ε is not a measurement precision — it is a **structural parameter of the scope**.
It specifies what resolution the description *requires* to be meaningful,
not what resolution an instrument can achieve.

---

## 2 ε as a Resolution Window

In real systems, ε is better understood as a **resolution window** than a
scalar threshold. Behavioral regimes occupy finite regions in parameter space,
and two states are equivalent when their observable differences remain within
this window — not just below a single cutoff.

```
ε ⊆ observable space   (region, not point)
x ~_S y   iff   Π(x) - Π(y) ∈ ε
```

**Example — ECDL laser:**
A single-mode laser operates stably within a finite current and temperature window.
Within that window, the observable (output mode) is invariant.
The window is ε. States inside are a single regime class; crossing the window boundary
triggers a mode hop — a scope transition.

**Example — Labyrinth agent:**
Policy embeddings within cosine distance 0.1 are in the same mode.
The "0.1 ball" is ε in the policy embedding space.
Two trajectories are the same mode if their embeddings fall within this ball,
regardless of which specific path through the maze was taken.

---

## 3 ε Determines Partition Granularity

ε controls how many regime classes the ARW operator induces:

```
ε large  →  many states indistinguishable  →  coarse partition (few classes)
ε small  →  more states distinguishable    →  fine partition (many classes)
```

This makes ε the primary parameter for moving between levels
of a hierarchical partition:

```
ε₁ > ε₂ > ε₃   →   R_S(ε₁) ⊇ R_S(ε₂) ⊇ R_S(ε₃)   (coarser to finer)
```

Each ε value induces a distinct scope and a distinct partition.
Changing ε while keeping B and Π fixed is a scope transition along
the resolution dimension.

---

## 4 The ε–Δ Interaction (Critical)

The interaction between ε and Δ is the most important and least
documented aspect of ε in the framework.

**Setup:**
Δ defines which perturbations are "noise" — perturbations the scope must
remain stable under. ε defines which observable differences are "meaningful".

**The critical case:**
A perturbation δ ∈ Δ (within the admissible range) that produces
an observable change |Π(x+δ) - Π(x)| > ε (above resolution threshold).

This state is **both admissible noise AND a distinguishable observable change**.
The scope assigns x and x+δ to different regime classes — but treats the
perturbation as admissible noise.

**Consequence:**
If this occurs, the regime assignment is unstable under admissible perturbations.
[x]_S and [x+δ]_S are different classes, but δ is within Δ.

This is the formal definition of a **partition boundary state**:
states x where ∃ δ ∈ Δ: |Π(x+δ) - Π(x)| > ε.

Such states are structurally ambiguous — they sit on the regime boundary
and their class assignment is noise-sensitive.

**Design implication:**
A well-specified scope should have ε and Δ consistent:
perturbations within Δ should produce observable changes below ε.

```
consistency condition:   max_{δ ∈ Δ} |Π(x+δ) - Π(x)| < ε   for bulk states x
```

Boundary states are the exception — and their density defines
the "width" of regime boundaries.
Narrow boundaries (few boundary states) → crisp partition.
Wide boundaries → diffuse partition → high distortion under aggregation.

---

## 5 ε and Admissibility

An observable π ∈ Π becomes **inadmissible** when its effects
on the observable space fall below ε:

```
|π(x) - π(y)| < ε   for all relevant pairs (x, y)
```

This means π produces no distinctions above resolution.
The degree of freedom associated with π is effectively latent —
it can be suppressed without changing the partition.

**Connection to emergence:**
When a previously admissible observable loses admissibility (its effects
drop below ε for the current scope), the partition loses a dimension.
The system appears to "simplify" — previously distinct regime classes merge.
This is the ε-mechanism behind emergence.

---

## 6 ε in the Experimental Systems

| System | ε specification | Interpretation |
|---|---|---|
| Kuramoto | Δr < 0.05 (order parameter) | Order parameter differences below 0.05 are same regime |
| Pendulum | δθ < 0.01 rad | Angular differences below 0.01 rad indistinguishable |
| Consensus models | Opinion difference < 0.02 | Agents within 0.02 opinion distance are same class |
| Labyrinth agent | Cosine distance < 0.1 (policy embedding) | Policies within 0.1 cosine distance are same mode |
| Mean-field (opinion) | ||ρ - ρ'||_L1 < 0.05 | Distribution differences below 0.05 are same MF regime |

**Empirical ε estimation:**
In each system, ε must be calibrated so that:
1. Bulk regime states are stable under Δ (consistency condition satisfied)
2. Boundary regions are identifiable (states where Δ-perturbations approach ε)
3. The resulting partition count matches theoretical predictions

---

## 7 Open Questions on ε

The following aspects of ε require further formalization:

- **ε as a function of state:** Should ε be uniform or can it vary across
  state space? High-symmetry regions may require finer resolution than bulk regions.
- **ε estimation procedure:** Given a system and a candidate Δ, how is the
  consistent ε determined empirically?
- **ε and information content:** Is there a relationship between ε and the
  information-theoretic mutual information between scope observables?
- **Multiple ε for multiple observables:** When Π = {π₁, π₂, ...}, can
  each observable have its own εᵢ? What is the joint admissibility condition?
