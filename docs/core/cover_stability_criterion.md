---
status: working-definition
layer: docs/core/
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/perturbation_spread.md
  - docs/glossary/observable_range.md
  - docs/advanced/epsilon_and_scope_resolution.md
---

# Cover Stability Criterion

## Overview

The cover stability criterion (Felder 2026) provides the formal necessary condition
for when a scope S = (B, Π, Δ, ε) can sustain **observable information** — that is,
when the descriptive apparatus of ARW is valid at all.

It formalizes the construction underlying the ARW regime partition, resolves the
transitivity problem in direct ε-indistinguishability, and introduces the
**admissible resolution regime** as the formal counterpart to the ARW admissible
ε-interval I_ε.

This document states the criterion in ARW language. The source is:
*Rico Felder, "When Does a System Have a Well-Defined State? Cover Stability as a
Necessary Condition for Observable Information", 2026 (v1 + v2).*

---

## 1. The ε-Adjacency Graph and Observable Cover

Let O : X → ℝ be an observable (π ∈ Π in ARW notation) and ε > 0 a resolution threshold.

**Definition (ε-adjacency graph).**
The graph G_ε(O) has vertex set X and an edge between x, y ∈ X whenever:

```
|O(x) − O(y)| ≤ ε
```

**Definition (Observable cover C_ε).**
The observable cover C_ε is the set of **connected components** of G_ε(O).
Each cover element C ∈ C_ε is a maximal path-connected set of states that are
mutually reachable through chains of ε-adjacent states.

This is a **Čech cover construction**. It is the correct object for the ARW
regime partition because it is **transitivity-safe**: the condition
|O(x)−O(y)| ≤ ε and |O(y)−O(z)| ≤ ε does not force x and z into the same class
unless x and z are also connected via a chain of ε-adjacent intermediate states
(the sorites resolution, Felder 2026 §3).

**Connection to the ARW scope tuple.**
The direct ε-indistinguishability relation x ~_S y ↔ |Π(x)−Π(y)| ≤ ε in
`docs/glossary/scope.md` is the **edge condition** of G_ε(O). The ARW regime
partition corresponds to the connected components C_ε — not to the equivalence
classes of ~_S closed under transitive closure. For well-separated regimes
(typical cases) the two agree; near regime boundaries the Čech construction
is formally correct and avoids spurious regime merging.

### Non-triviality

The cover C_ε is **non-trivial** if it contains more than one component
(i.e. the system has at least one detectable distinction at resolution ε).
The cover collapses to trivial (single component) when ε ≥ ε*(O,X).

**Definition (collapse threshold).**
ε*(O,X) is the smallest ε at which C_ε becomes trivial:

```
ε*(O,X) := inf { ε > 0 : |C_ε| = 1 }
```

ε*(O,X) depends on the topology of the observable image O(X), not only its span.
For a connected-interval image, ε*(O,X) = ½·span(O(X)). For fragmented or
multi-component images, ε*(O,X) can be substantially smaller than ½·span.
This is the basis for the topology-corrected F1 criterion (see
`docs/glossary/observable_range.md`).

---

## 2. Perturbation Spread and Cover Stability

Let Δ be the admissible perturbation class (scope component).
The **perturbation spread** at state x is:

```
σ_Δ(x) := sup_{δ ∈ Δ} |O(x+δ) − O(x)|
```

(Full treatment: `docs/glossary/perturbation_spread.md`.)

**Definition (Δ-stable cover element).**
A cover element C ∈ C_ε is **Δ-stable** if:

```
sup_{x ∈ C} σ_Δ(x) < ε
```

That is: every state in C remains within the cover element under all admissible
perturbations. No perturbation δ ∈ Δ can move a state across the ε-boundary
of its cover element.

**Definition (cover stability).**
The cover C_ε is **Δ-stable** if every cover element is Δ-stable.

---

## 3. Proposition 1 — Necessary Condition for Observable Information

**Proposition 1 (Felder 2026).**
*Observable information* — the existence of at least one well-defined, stable
descriptive distinction — requires:

```
(i)  C_ε is non-trivial     (ε < ε*(O,X))
(ii) C_ε is Δ-stable        (sup_x σ_Δ(x) < ε)
```

Together these define the **admissible resolution regime**:

```
sup_x σ_Δ(x)  <  ε  <  ε*(O,X)
```

This is the formal counterpart to the ARW admissible ε-interval I_ε = [ε_min, ε_max]:

| ARW concept | Felder 2026 counterpart |
|---|---|
| ε_min = max_{x ∈ bulk} max_{δ ∈ Δ} \|Π(x+δ)−Π(x)\| | sup_x σ_Δ(x) — now formally named (see §2) |
| ε_max (largest ε preserving relevant distinctions) | ε*(O,X) — topology-determined upper bound |
| I_ε = [ε_min, ε_max] | Admissible resolution regime: (sup_x σ_Δ, ε*(O,X)) |

The admissible regime is non-empty iff sup_x σ_Δ(x) < ε*(O,X).
This is the precondition for any scope S = (B, Π, Δ, ε) to sustain observable information.

---

## 4. Corollary 1 — Lipschitz Bound on Perturbation Spread

**Corollary 1 (Felder 2026).**
If O is Lipschitz continuous with constant L > 0, and Δ is norm-bounded by r
(i.e. ‖δ‖ ≤ r for all δ ∈ Δ), then:

```
σ_Δ(x) ≤ L · r    for all x ∈ X
```

**Sufficient condition for pointwise stability:**

```
L · r < ε
```

**Admissible regime non-empty iff:**

```
L · r < ε*(O,X)
```

**Remark (Felder 2026, Remark 4 — pipeline justification).**
For smooth observables, the local Lipschitz constant equals the local gradient magnitude:
L(x) = |∂O/∂κ| (or the appropriate Jacobian norm in higher dimensions).
Therefore the leading-order bound on σ_Δ(x) is:

```
σ_Δ(x) ≤ |∂O/∂κ| · r + O(r²)
```

This justifies the gradient field |∂O/∂κ| as the **leading-order** Lipschitz bound.
However — see the validation caveat below — the *pointwise* gradient is only the
leading-order term and is **not** a faithful σ_Δ estimator near θ*.

**Validation caveat (C1, 2026-06-02 — `Simulationen/sigma_validation_c1/`).**
Direct measurement of σ_Δ(x) = sup_{|δ|≤r}|O(x+δ)−O(x)| against the *pointwise* proxy
|∂O/∂κ|·r on analytically tractable observables (pendulum ω(E), pitchfork x_ss(μ)) shows:
Corollary 1 holds exactly with the **local-max** Lipschitz L_local = max_{|d|≤r}|O'(x+d)|
(σ_Δ ≤ L_local·r, 0 violations); but the **pointwise** gradient under-estimates σ_Δ at θ*
by up to ~4× (pendulum separatrix) to ~10¹¹× (pitchfork bifurcation, where |∂O/∂κ|=0 on the
flat branch while a perturbation reaches across the bifurcation). The bias is **one-sided**
(F-gradient false negatives: "stable" reported where σ_Δ≥ε), clustered at θ*, growing with r.
**Corrective:** use the **direct windowed σ_Δ** (max |O_j−O_i| over the Δ-window on the sweep
grid) or the **local-max** L_local·r — both implemented in `pipeline/epsilon_kappa_map.py`
(`compute_sigma_delta_windowed`, output field `sigma_delta_windowed`). The pointwise field
`observable_gradient` is retained for backward comparison only and should not drive F-gradient
verdicts near θ*.

**Why cover stability fails at phase transitions.**
At dynamical phase transitions (e.g. κ ≈ κ_c in Kuramoto, E ≈ E_sep in the conservative
pendulum), the observable gradient |∇O| diverges. Corollary 1 then implies σ_Δ(x) → ∞,
so no finite norm-bounded Δ can stabilize the cover there. This explains from first principles
why the stability mask always fails at the transition (high-σ_Δ band = Z_shared).

**Descriptive crossover.**
Corollary 1 also explains the **secondary instability ridge** at E ≈ ω₀² in the
conservative pendulum (CASE-20260311-0003): the anharmonic crossover produces a sharp
increase in |∇O| without any dynamical phase transition. This is a **descriptive
crossover** (Felder 2026 §6.2): σ_Δ(x) > ε within R(π), not due to substrate failure
but due to high observable gradient. Classification: F-gradient (see
`docs/glossary/observable_range.md`), not F0.

---

## 5. Stability Mask

The **binary stability mask** is the set of states that satisfy pointwise stability:

```
M_stable(ε) := { x ∈ X : σ_Δ(x) < ε }
```

Its complement M_unstable = X \ M_stable is the set of descriptively unreliable states.

In the pipeline, the mask should be computed from the **direct windowed σ_Δ**
(the C1-corrected estimator), not the pointwise gradient:

```
M_stable(ε)        := { x : σ_Δ_windowed(x) < ε }     # correct (use this)
M_stable_proxy(ε)  := { x : |∂O/∂κ| · r < ε }          # leading-order, biased at θ* (one-sided)
```

`pipeline/epsilon_kappa_map.py::compute_sigma_delta_windowed` computes σ_Δ(x) directly as the
max |O_j−O_i| over the Δ-window on the sweep grid (output field `sigma_delta_windowed`, with
`proxy_pointwise`, `proxy_localmax`, and a per-point `pointwise_underestimates` flag). A
standalone `pipeline/stability_mask.py` is **planned** (migration action E-1/E-2); until it
exists, use the `sigma_delta_windowed` field. See the C1 validation caveat in §4.

---

## 6. Connection to ARW Concepts

| Paper concept | ARW concept | Location |
|---|---|---|
| G_ε(O) connected components | Regime partition | `docs/glossary/partition.md` |
| σ_Δ(x) perturbation spread | ε–Δ consistency condition (now named) | `docs/glossary/perturbation_spread.md` |
| ε*(O,X) collapse threshold | ε_max (topology-corrected) | `docs/advanced/epsilon_and_scope_resolution.md` §4 |
| Non-trivial cover | Observable sufficient (F1 not triggered) | `docs/glossary/observable_range.md` |
| Δ-stable cover | Partition reproducible under Δ (F2 not triggered) | `docs/core/` |
| Admissible resolution regime | I_ε = [ε_min, ε_max] | `docs/advanced/epsilon_and_scope_resolution.md` |
| Observable information (Def 6) | Scope validity precondition | `docs/core/observable_information.md` |
| Stability mask M_stable | B-restricted admissible region | `pipeline/stability_mask.py` |
| Descriptive crossover | F-gradient failure category | `docs/glossary/observable_range.md` |

**Scope tuple alignment.**
The paper uses (X, O, Δ, ε) — X is assumed given, no explicit B component.
B in ARW corresponds to the implicit choice of parameter window X considered
in the paper: B is the ARW mechanism for restricting to the relevant domain.
The paper operates one level below the ARW scope: it asks when information
exists at all given (X, O, Δ, ε); ARW then adds B to select which X to consider.

---

## 7. Empirical Confirmation

The criterion has been empirically confirmed in two case studies in Felder 2026:

- **CASE-20260311-0001 (Kuramoto):** the stability mask fails exactly at κ_c
  (the synchronization transition), consistent with L → ∞ at the transition.
  The 1D κ-sweep captures a σ-fixed slice of the full 2D (κ,σ) stability structure.
  The correct Gaussian reference line is κ_c = √(8/π)·σ ≈ 1.596σ (not the
  Lorentzian formula 1.5σ; see CASE-0001 CaseRecord, D-1 update pending).

- **CASE-20260311-0003 (Conservative Pendulum):** with observable ω(E,ω₀),
  the cover-stability criterion recovers the separatrix **E_sep = ω₀²**
  model-independently (corrected 2026-06-02; the earlier value 2ω₀² was a bug —
  separatrix at θ=π, θ̇=0 gives E = −ω₀²·cos(π) = +ω₀²; see
  `Simulationen/bugfix_report_20260602_p0_esep.md`). There is a **single** instability
  ridge at E_sep = ω₀² (L diverges → Z_shared / F-gradient with σ_Δ/ε ≈ 2.0 at the
  separatrix). The previously claimed **secondary ridge at E ≈ ω₀²** does **not exist**:
  under the buggy convention E_sep_old = 2ω₀², the position u = E/E_sep_old = ω₀²/(2ω₀²) = ½
  was simply the true separatrix re-labelled. Re-measurement (Phase 1.3, 2026-06-02) finds
  no secondary feature > 10% of the primary peak.

---

*Confirmed across two case studies (Felder 2026 v1+v2). Status promoted from
note to working-definition on 2026-04-29.*
