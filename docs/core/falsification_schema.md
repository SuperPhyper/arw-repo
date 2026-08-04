---
status: working-definition
layer: docs/core/
last_updated: 2026-08-04
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/observable_range.md
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
  - docs/advanced/epsilon_and_scope_resolution.md
  - docs/advanced/observable_decomposition.md
---

# Falsification Schema

**Source of truth for the ARW falsification categories F0–F4, F-gradient, F1_BC and the
cross-cutting exclusion zone Z_shared.** Promoted 2026-08-04 from
`docs/meta/context_map/context_map_falsification_bc.md`, which had been carrying the
fullest statement of the schema from the `meta` layer despite being a derived artifact
(core-concept drift audit, finding D-04). The context map remains the compressed,
agent-optimised rendering; **this file is what it renders.** When the two disagree, this
file wins and the map is regenerated.

The schema answers one question: when a scope produces an unexpected or unstable result,
**what failed** — the observable, the resolution, the sweep, or the scope itself?

Its governing asymmetry: **observable insufficiency is not scope rejection.** Most
failures are repaired by replacing an observable or adjusting ε, and only a minority
invalidate the scope. A schema that collapses these would make ARW unfalsifiable in the
wrong direction — every failure would read as a refuted scope.

---

## 1. Categories

Each entry: formal condition · verdict · repair. ε-dependence matters: F0 cannot be
repaired by any choice of ε; F1 and F-gradient can.

### F0 — Range violation (substrate failure)

```
R(π) ∩ B ≠ B          — the observable's range does not cover the admissible states
```

At least one pre-scopal substrate assumption A0–A6 fails somewhere in X_B
(`docs/advanced/observable_decomposition.md`). The observable loses its *referent*, not
merely its precision. **ε-independent** — no resolution choice recovers the region.

- **Verdict:** observable range violation
- **Repair:** `observable_replacement` — replace the observable, keep the scope
- **Diagnostic:** substrate analysis A0–A6; empirically σ_Δ rises sharply in the failure region
- **Canonical example:** r_ss at κ_c, where ergodicity, uniqueness of μ_stat and the
  well-definedness of r fail simultaneously (`docs/glossary/observable_range.md`)

**F0 is Π-relative.** The same measurement channel can be F0 under one observable
definition and admissible under another — chlorophyll fluorescence is F0 for absolute
concentration (Π_abs) and conceptually admissible for relative change (Π_rel). Classify
the observable, not the instrument.

**A6 split (Part VII, 2026-07-18):** an *invalid* A6 (e.g. a finite-time Lyapunov
estimator read as λ_∞ without passing a convergence test) is F0. An A6 that is valid but
simply does not resolve at the working ε is F1. λ_T is its own observable: with referent
λ_T at horizon T it can pass A6 and then fail as F1 for the claimed structure.

### F1 — Observable insufficiency

```
ε ≥ ε*(O, X_B)        — the cover C_ε collapses to a single component
```

ε*(O,X_B) is the smallest ε at which |C_ε| = 1. It depends on the **topology** of the
observable image, not on its span.

- **Verdict:** observable insufficiency
- **Repair:** `observable_replacement` (or reduce ε, but only while ε > sup_x σ_Δ(x) —
  otherwise the repair triggers Δ-instability instead)
- **Diagnostic:** compute ε*(O,X_B); check |C_ε| at the working ε

**Shorthand and its limit.** `span(π) < 2ε` is a sufficient condition for cover
triviality **only when O(X_B) is a connected interval**, where ε* = ½·span. For
multi-modal or fragmented images ε* can be far smaller than span/2, and the shorthand
then reports sufficiency where the cover has in fact collapsed. Repo documents that use
the shorthand carry an F1-notation pointer to this section (decision of 2026-08-04,
option b: canonical documents and the ScopeSpec schema state ε*, instantiation documents
keep the shorthand with a pointer).

**Claim-relative generalisation (Part VII V3.2, 2026-07-18):** in its general form F1
says the ε-partition *fails to refine the claimed structure R*. Total collapse (ε ≥ ε*)
is the special case the pipeline tests.

### F1_BC — BC without observable effect

```
F1 holds for every π ∈ Π
```

No admissible observable resolves anything at this resolution: the boundary condition
has no descriptive effect within the scope.

- **Verdict:** BC wirkungslos
- **Repair:** `scope_rejection`
- **Note:** the only route from observable insufficiency to scope rejection. A single
  insufficient observable is F1, never F1_BC.
- **Construction constraint:** an agent constructing its own scope cannot apply F1_BC —
  it would have to quantify over all admissible observables
  (`docs/notes/observable_information_and_bc_responsiveness.md`).

### F2 — Partition not reproducible under Δ

```
θ* unstable under Δ   — the transition location shifts across admissible perturbations
```

- **Verdict:** partition not reproducible
- **Repair:** `scope_rejection`
- **Tests (not equivalent — each case declares which it uses):** Var(θ*) > τ_var, or
  range(θ*) > τ_range across the δ-sample.
- **Precondition:** F2 is uninterpretable while F4 is live — a θ* sitting at the sweep
  boundary has no reliable estimate to be unstable *about*.

### F3 — Collective plateau failure

```
no robust plateau in N(ε) for any π ∈ Π   ⇔   I_ε = ∅
```

Equivalently sup_x σ_Δ(x) ≥ ε*(O,X_B): the lower bound of the admissible resolution
regime exceeds its upper bound, so no valid ε exists.

- **Verdict:** collective failure
- **Repair:** `scope_rejection` — not resolvable by swapping a single observable

### F4 — Boundary artifact

```
θ* at the sweep boundary   — the true transition may lie outside the swept range
```

- **Verdict:** boundary artifact, **not** a scope failure
- **Repair:** `sweep_refinement` — extend the sweep and re-run before interpreting θ*

### F-gradient — Descriptive crossover

```
O ∈ R(π) everywhere, but σ_Δ(x) ≥ ε for some x ∈ X_B
```

The observable is structurally sound (all A0–A6 pass) but locally too steep for the
chosen resolution: the cover is not Δ-stable at those states. The zone
Z_cover = {x : σ_Δ(x) ≥ ε} ∩ R(π) is **ε-dependent** and shrinks as ε grows.

- **Verdict:** descriptive crossover
- **Repair (ranked):** stability-mask exclusion → **increase** ε above sup_x σ_Δ(x) →
  reduce the perturbation radius r → replace the observable
- **ε direction:** increase. The admissible regime is sup_x σ_Δ(x) < ε < ε*(O,X_B);
  F-gradient is a violation of the *lower* bound. Decreasing ε worsens it.
- **Reclassification:** if any A_i also fails at those states, this is F0, not F-gradient.
- **Canonical example:** the instability ridge at the double-pendulum separatrix
  E_sep = ω₀² (CASE-0003).

**Mass criterion (Part VII, 2026-07-18):** F-gradient fires when the unstable fraction
μ(χ = 1)/μ(X_B) exceeds a declared threshold τ_∂, where χ is assignment instability, not
a single unstable point. σ_Δ is the *proxy* for χ; χ itself is computed nowhere
(Q_NEW_26, open — see §6).

---

## 2. Z_shared — cross-cutting exclusion zone

Not an F-category. Z_shared is the universal exclusion zone for all class-E observables
at phase transitions: ergodicity, uniqueness of μ_stat, or the absence of critical
slowing fails there for *every* such observable. It applies **on top of** the F-schema
and cannot be repaired by any ε choice or observable swap within the class.

Distinguish carefully:

| Zone | Condition | ε-dependent? | Category |
|---|---|---|---|
| Z(π) | X_B \ R(π); A0–A6 violated | no | F0 |
| Z_cover | {x : σ_Δ(x) ≥ ε} ∩ R(π) | yes | F-gradient |
| Z_shared | class-wide substrate failure at a phase transition | no | none — cross-cutting |

---

## 3. Decision order

**Current order (Part VII V3.2, adopted 2026-07-18):**

```
F0  →  F4  →  F1  →  F3  →  F2  →  F-gradient
```

Rationale for the revision: F2 asks whether θ* is stable, which presupposes that θ* is
estimated reliably — false while F4 is live. Testing F4 before F2 removes an
uninterpretable branch. F0 stays first because it is ε-independent: no downstream test
means anything if the observable has lost its referent in part of X_B.

**Procedure:**

1. **F0** — run the A0–A6 substrate analysis over X_B. Any violation → observable
   replacement; stop.
2. **F4** — is θ* at a sweep boundary? → extend the sweep and re-run; stop.
3. **F1** — is |C_ε| = 1 at the working ε (ε ≥ ε*)? If yes, check every π ∈ Π: all → F1_BC
   (scope rejection); one → F1 (observable replacement).
4. **F3** — is there a plateau in N(ε) for any π? If none anywhere → scope rejection.
5. **F2** — is θ* stable across the δ-sample under the case's declared test? If not →
   scope rejection.
6. **F-gradient** — with the substrate sound, is the unstable mass μ(χ=1)/μ(X_B) > τ_∂?
   → stability mask / raise ε / reduce r / replace observable.

The earlier σ_Δ-first tree (test σ_Δ ≥ ε before everything, branching on A0–A6) is
**historical**; it is preserved in the context map until the next map regeneration.

---

## 4. Pairwise discriminations

The categories are easy to confuse in exactly these pairs.

| Pair | The distinction |
|---|---|
| F0 vs F1 | F0 is structural (substrate fails); F1 is resolution (cover trivial). Independent axes — check the substrate first. High σ_Δ alone is **not** sufficient for F0. |
| F0 vs F-gradient | If A0–A6 all pass, it is not F0. F-gradient is steepness within a sound range; F0 is loss of referent. |
| F1 vs F1_BC | F1_BC requires F1 for **every** π ∈ Π. One insufficient observable is F1. |
| F1 vs F3 | F1: N(ε) = 1 for one π. F3: N(ε) never stabilises, for any π. |
| F1_BC vs F3 | F1_BC: observables have no spread. F3: they have spread but no stable plateau. |
| F2 vs F3 | F2: a plateau exists but θ* drifts across runs. F3: no plateau at all. |
| F2 vs F4 | F2: θ* unstable under perturbation *within* B. F4: θ* at the edge of the swept range — different causes, different repairs. |
| F4 vs scope failure | F4 alone never rejects a scope. The scope may be entirely valid. |
| Z(π) vs Z_cover | Z(π): substrate violation, ε-independent → F0. Z_cover: gradient excess, ε-dependent → F-gradient. |

---

## 5. Schema binding

Every ScopeSpec falsification entry carries an `id` from the closed enum
`{F0, F1, F1_BC, F2, F3, F4, F-gradient}` and a `severity`:

```
observable_replacement : F0 | F1 | F1_BC (partial) | F-gradient (secondary)
scope_rejection        : F1_BC | F2 | F3
sweep_refinement       : F4
scope_refinement       : F-gradient (primary)
universal_exclusion    : Z_shared
```

Observable-level insufficiency is recorded in the ScopeSpec `observable_sufficiency`
block, *not* in `falsification` — the falsification block operates at BC level. Guard
rules for both: `arw-meta-guard` (GUARD-2).

---

## 6. Open items

- **Q_NEW_26 — χ is computed nowhere.** The exact boundary-state indicator
  χ_{Δ,ε}(x) = 1[∃δ ∈ Δ : component identity changes] is what F-gradient is *about*; every
  pipeline stability mask uses the σ_Δ proxy instead, whose reliability degrades precisely
  at boundaries. The σ↔χ error relation is uncharacterised in both directions (the C1
  one-sidedness result concerns gradient → σ only). Carries the τ_∂ threshold with it.
- **Never lower ε** is a proxy-based pipeline convention, **not** a χ-theorem: changing ε
  changes the partition, so the χ-effect is not guaranteed monotone. Perform ε-repairs
  within the selected plateau and verify by recomputation.
- **F2 test choice** (variance vs range) is declared per case; the two are not equivalent
  and no canonical choice exists.
- **No meta-falsification.** This schema classifies failures *within* the framework. What
  would falsify the schema itself is a separate question (audit finding C1, 2026-06-10).

---

## 7. Provenance

| Element | Origin |
|---|---|
| F1–F4 | Original ARW falsification set |
| F0, Z(π), R(π) | Session 2026-03-18, `docs/glossary/observable_range.md` |
| F-gradient, ε*(O,X), σ_Δ, Z_cover | Felder 2026 integration, session 2026-04-29 |
| E_sep correction (ω₀², single ridge) | Session 2026-06-02 |
| Decision-order revision, A6 split, claim-relative F1, χ mass criterion | Monograph Part VII V3.2/V3.3, 2026-07-18 |
| F0 as Π-relative | EWS Stage-1 review, 2026-08-04 |
| Promotion to canonical core document | Core-concept drift audit, 2026-08-04 (D-04) |

**Related:** `docs/bc_taxonomy/bc_failure_signatures.md` gives the per-BC-class failure
signatures and their onset diagnostics; this document gives the categories those
signatures are expressed in.
