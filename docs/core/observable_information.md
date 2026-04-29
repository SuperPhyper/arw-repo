---
status: working-definition
layer: docs/core/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
  - docs/advanced/epsilon_and_scope_resolution.md
  - docs/glossary/observable_range.md
---

# Observable Information

## Definition

**Observable information** exists for a configuration (X, O, Δ, ε) if and only if
the observable cover C_ε is both non-trivial and Δ-stable:

```
(i)  |C_ε| > 1               — non-trivial: at least one meaningful distinction exists
(ii) sup_{x ∈ X} σ_Δ(x) < ε — Δ-stable: all distinctions survive admissible perturbations
```

This is the **necessary condition for scope validity** (Felder 2026, Definition 6 and
Proposition 1). It answers the question ARW presupposes: *when does the descriptive
apparatus of a scope sustain a well-defined state description at all?*

---

## Motivation

ARW asks: given a valid scope S = (B, Π, Δ, ε), what regime structure does it produce?
But ARW does not itself ask: *when is a scope valid in the first place*?

Observable information is the formal answer. It is the precondition for the ARW
regime-partition machinery to be meaningful — the condition under which a descriptive
alphabet of regime labels exists.

Classical information-theoretic measures (Shannon entropy, mutual information) implicitly
presuppose that a well-defined alphabet of outcomes exists. Observable information
asks the more primitive question: does a stable alphabet exist at all?

---

## ARW Equivalences

The observable information condition maps directly onto existing ARW constructs:

| Observable information | ARW concept | Where |
|---|---|---|
| Non-trivial cover: ε < ε*(O,X) | F1 not triggered (topology-corrected) | `docs/glossary/observable_range.md` |
| Δ-stable cover: sup σ_Δ(x) < ε | F2 not triggered (partition reproducible) | `docs/core/` |
| Admissible resolution regime: sup σ_Δ < ε < ε*(O,X) | I_ε = [ε_min, ε_max] | `docs/advanced/epsilon_and_scope_resolution.md` |
| Observable information exists | Scope S is valid | `docs/glossary/scope.md` |

**The admissible ε-interval I_ε is precisely the set of ε values for which
observable information exists** — the interval over which the scope sustains
a non-trivial, stable cover.

---

## The Exclusion Zone Reinterpreted

The exclusion zone Z(π) = P \ R(π) (`docs/glossary/observable_range.md`) is the
region of parameter space where the pre-scope substrate of π fails.

Observable information provides a complementary characterization:

```
Z(π) ⊆ { x : observable information fails for any ε, because σ_Δ(x) → ∞ }
```

Within R(π), observable information can still fail locally if σ_Δ(x) ≥ ε
for a chosen ε — this is the F-gradient (descriptive crossover) case.
The two failure modes are:

| Failure mode | Location | Cause | Remedy |
|---|---|---|---|
| Z(π) / F0 | Outside R(π) | Pre-scope substrate fails | Replace observable |
| F-gradient | Inside R(π) | σ_Δ(x) ≥ ε, high |∇O| | Increase ε, reduce Δ, or replace observable |

Observable information is violated in both cases but for structurally different reasons.

---

## Connection to Open Questions (resolved)

**Q4 — Formal relationship between ARW and topological data analysis** (`docs/notes/open_questions.md`):
*Partially resolved.* The cover construction C_ε is a Čech cover — the same object
studied in persistent homology. The admissible resolution regime (sup σ_Δ, ε*) is the
ARW counterpart to the persistence window in which topological features are stable.
Cover height (see `docs/advanced/observable_space_cover_height.md`) accumulates
evidence across ε scales analogously to persistence diagrams, but without the full
topological bookkeeping. The formal correspondence to persistent homology remains open.

**§8 question in `docs/advanced/epsilon_and_scope_resolution.md`** — "Is there a
relationship between ε and information-theoretic mutual information?":
*Resolved at the structural level.* Observable information is the precondition that
must hold before information-theoretic quantities are meaningful. The admissible
ε-interval is the range over which the descriptive alphabet is stable enough for
entropy and mutual information to be well-defined. The specific relationship between
plateau width w(I_ε) and channel capacity remains open.

---

## Scope-Level Formulation

In ARW notation, observable information for scope S = (B, Π, Δ, ε) with a single
observable π ∈ Π requires:

```
(i)  ε < ε*(π, X_B)                    — cover C_ε is non-trivial over X_B
(ii) sup_{x ∈ X_B} σ_Δ(x) < ε         — cover is Δ-stable
```

For a multi-observable scope Π = {π₁, ..., π_k}, observable information for the
joint scope requires these conditions to hold for each πᵢ with its respective εᵢ.
The admissible region becomes a region in ℝᵏ (Felder 2026 §8 Outlook):

```
{ (ε₁,...,ε_k) : ∀ i: sup_x σ_Δ(x; πᵢ) < εᵢ < ε*(πᵢ, X_B) }
```

The box-shaped approximation currently used in ARW (component-wise I_εᵢ) is a
special case assuming decoupled observables. Cross-observable ε constraints
remain open (see Q-NEW-COVER-2 in `docs/notes/open_questions.md`).

---

## Related Concepts

- Cover stability criterion and proof → `docs/core/cover_stability_criterion.md`
- Perturbation spread σ_Δ(x) → `docs/glossary/perturbation_spread.md`
- Admissible ε-interval I_ε → `docs/advanced/epsilon_and_scope_resolution.md`
- Observable range R(π), exclusion zone Z(π) → `docs/glossary/observable_range.md`
- F-gradient (descriptive crossover) → `docs/glossary/observable_range.md`
- Scope tuple S = (B, Π, Δ, ε) → `docs/glossary/scope.md`
