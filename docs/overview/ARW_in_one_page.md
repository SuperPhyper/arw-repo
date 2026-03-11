---
status: working-definition
---

# ARW in One Page

## Overview

The **Allgemeine Regime-Wissenschaft (ARW)** framework studies how
**descriptive choices shape the structures that appear stable in a system**.

Rather than asking whether a model is *true*, ARW analyzes:

- which descriptions produce stable regime structures
- when those descriptions lose validity
- how new descriptive regimes emerge

ARW itself is **purely formal** and does not make empirical claims.
Concrete systems are introduced through **ART (Allgemeine Regime-Theorie)**,
which instantiates scopes for specific domains.

---

## Core Idea

Every scientific description implicitly defines a **scope**.

A scope specifies:

- which states are admissible
- which observables are used
- which perturbations are allowed
- what resolution distinguishes states

In ARW, a scope is defined as the tuple:

```
S = (B, Π, Δ, ε)
```

| Symbol | Meaning |
|---|---|
| B | boundary constraints — admissible states |
| Π | descriptions / projections — observables |
| Δ | admissible perturbations — robustness conditions |
| ε | resolution threshold — distinguishability |

---

## The ARW Operator

Given a scope, ARW produces a **regime partition** of the admissible state space:

```
A(S) = R_S
```

States that remain indistinguishable under the scope are grouped into the same regime.
The partition represents the **stable structure that the chosen description reveals**.

---

## How Regimes Appear

```
Scope S = (B, Π, Δ, ε)
        ↓
Distinguishability under Π
        ↓
Resolution threshold ε
        ↓
Robust indistinguishability (~_S)
        ↓
Regime partition R_S
```

Different scopes applied to the same system produce different regime structures.

---

## Admissibility

An observable is **admissible** when its relevant effects remain
distinguishable above the resolution threshold of the scope.

If an observable operates below the scope resolution:

- distinctions collapse
- the observable becomes effectively latent
- the scope may lose descriptive power

---

## Emergence

Emergence occurs when a scope loses admissibility and the effective
partition of the state space reorganizes. This produces:

- new regime structures
- new observable relations
- a different scope that stabilizes the description

---

## ARW vs ART

| | ARW | ART |
|---|---|---|
| **Role** | Formal operator over scopes | Concrete instantiation of scopes |
| **Empirical claims** | None | Yes — via specific B, Π, Δ, ε |
| **Output** | Regime partition structure | Measurable predictions and comparisons |

---

## What ARW Studies

ARW studies the **structure of descriptions** rather than the intrinsic nature of systems.

It asks:

- how descriptive regimes form
- why they fail
- how regime structures transfer across scopes

---

## Conceptual Summary

ARW provides a methodology for analyzing how **boundary conditions,
observables, perturbations, and resolution jointly determine the
regime structures that appear stable in a system description**.
