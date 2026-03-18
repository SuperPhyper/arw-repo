---
status: claim
---

# Latent Degrees of Freedom: BC Mapping and Observable Hierarchy

## Context

This document continues the observable decomposition analysis
(`docs/advanced/observable_decomposition.md`).
Every Restriction operation in an observable generates a latent degree of
freedom — a parameter contained in the operator structure of π but not
explicitly encoded in the scope S = (B, Π, Δ, ε).

Here all latent degrees of freedom from the three decomposed observables
(r_ss, var_rel, lambda_proxy) are consolidated, mapped to BC classes,
and examined for redundancies and shared structure.

---

## Complete Inventory

| ID | Observable | Operation | Discarded information | Latent degree of freedom |
|---|---|---|---|---|
| LF-01 | r_ss | op_1 | All j' ≠ j | Individual phase dynamics θ_j(t) |
| LF-02 | r_ss | op_2 | Winding number ∈ Z | Topological invariant w_j |
| LF-03 | r_ss | op_3 | Distribution of θ_j | Higher moments (σ², skewness, ...) |
| LF-04 | r_ss | op_4 | Collective phase ψ | Rotation mode of ensemble |
| LF-05 | r_ss | op_5 | Transient dynamics | Relaxation structure, convergence rate |
| LF-06 | var_rel | op_1 | All other pairs | Global coupling geometry |
| LF-07 | var_rel | op_2 | Absolute phases θ₁, θ₂ | Individual dynamics |
| LF-08 | var_rel | op_3 | Sign of Δθ | Direction of phase difference |
| LF-09 | var_rel | op_4 | Distribution of Δθ | Higher moments |
| LF-10 | var_rel | op_5 | Time structure of fluctuations | Correlation time, spectrum |
| LF-11 | var_rel | op_6 | Absolute scaling | System-specific energy scale |
| LF-12 | lambda_proxy | op_1 | All perturbation directions | Lyapunov spectrum |
| LF-13 | lambda_proxy | op_2 | Directional information δθ | Unstable manifold |
| LF-14 | lambda_proxy | op_3+4 | Non-exponential growth | Polynomial dynamics |
| LF-15 | lambda_proxy | op_5 | Time structure of growth | Intermittency, λ(t) fluctuations |
| LF-16 | lambda_proxy | op_6 | Convergence behavior | Finite-time Lyapunov spectrum |

---

## BC Mapping

| ID | Latent degree of freedom | BC class | In B? | Type |
|---|---|---|---|---|
| LF-01 | Individual phase dynamics θ_j(t) | Restriction | no | latent-external |
| LF-02 | Topological invariant w_j ∈ Z | Restriction | no | latent-external |
| LF-03 | Higher moments σ², skewness | Aggregation | no | latent-external |
| LF-04 | Rotation mode ψ(t) | Restriction | no | latent-external |
| LF-05 | Convergence rate / relaxation structure | Dissipation | no | latent-external |
| LF-06 | Global coupling geometry | Coupling | no | latent-external |
| LF-07 | Individual dynamics θ₁, θ₂ | Restriction | partial | latent-internal |
| LF-08 | Direction of phase difference | Restriction | no | latent-external |
| LF-09 | Higher moments of Δθ | Aggregation | no | latent-external |
| LF-10 | Correlation time, spectrum | Coupling | no | latent-external |
| LF-11 | System-specific energy scale | Forcing | no | latent-external |
| LF-12 | Lyapunov spectrum (all directions) | Restriction | no | latent-external |
| LF-13 | Unstable manifold | Restriction | no | latent-external |
| LF-14 | Polynomial / sub-exponential dynamics | Dissipation | no | latent-external |
| LF-15 | Intermittency, λ(t) fluctuations | Coupling | no | latent-external |
| LF-16 | Finite-time Lyapunov spectrum | Aggregation | no | latent-external |

### BC Distribution

```
Restriction     6    LF-01, 02, 04, 08, 12, 13
Aggregation     3    LF-03, 09, 16
Coupling        3    LF-06, 10, 15
Dissipation     2    LF-05, 14
Forcing         1    LF-11
Symmetry br.    0    —
```

---

## Structural Findings

### Finding 1: Coupling is latent in all three observables

LF-06, LF-10, LF-15 are all BC class Coupling — even though none of the
three observables has Coupling as its primary BC (CASE-0001: Coupling as
system BC, but r_ss projects it away; CASE-0003: Restriction as system BC).

```
Coupling is latently present in all three observables.
The coupling between degrees of freedom is systematically
projected away by the observables — it is never directly visible.
```

This partially explains why transfer between CASE-0001 (Coupling system)
and CASE-0003 (Restriction system) yields Φ=0.40 raw: the observables do
not expose the BC structure the system carries, but projections thereof.

### Finding 2: Symmetry Breaking is entirely absent

No latent degree of freedom was assigned to Symmetry Breaking.
Two possible interpretations:

```
(a) Symmetry Breaking is not encoded in observable structure —
    it is an emergent phenomenon at the level of the regime partition
    itself, visible as bifurcation in partition structure under
    parameter variation, not as discarded information of a single observable.

(b) Symmetry Breaking resides in P(θ, t) — in distribution asymmetries
    (non-vanishing skewness, multimodality) that moment-based observables
    do not fully capture.
```

### Finding 3: Shared latent degree of freedom LF-SHARED-A

LF-03 (r_ss), LF-09 (var_rel), and LF-16 (lambda_proxy) are different
instances of the same deeper degree of freedom:

```
LF-SHARED-A:  P(θ, t) — full time-dependent phase distribution
              BC class: Aggregation
              In B: no
              Type: latent-fundamental
```

The three observables are different one-dimensional projections from P(θ, t):

```
r_ss         = |E_j[e^(iθ)]|      — first Fourier mode of P(θ)
var_rel      = Var(Δθ) / Var_ref  — second moment of P(Δθ)
lambda_proxy = growth rate δθ     — local geometry of P(θ, t)
```

None of the three observables carries the full information of P(θ, t).
The regime partition in ARW is performed on the basis of projections
from P(θ, t) — never on P(θ, t) itself.

---

## Observable Hierarchy

The decomposition analysis reveals a natural three-level hierarchy:

```
Level 0:  P(θ, t)
          full time-dependent phase distribution
          — not directly observable; carries all regime information
          — latent-fundamental: LF-SHARED-A
                ↓
                projection (S1, S5): Fourier mode, moments, local geometry
                ↓
Level 1:  r_ss, var_rel, lambda_proxy, ψ(t), σ²(θ), C(τ), ...
          moments and modes of P(θ, t)
          — current and candidate observables
          — each observable is a specific projection
                ↓
                ε-clustering: d_Π(x,y) ≤ ε → x ~_S y
                ↓
Level 2:  regime label N
          discrete partition
          — scope output
```

Current ARW scopes operate at Level 1 → 2.
Level 0 → 1 is pre-scope — it constitutes the observables before
the scope takes effect.

### Implication

```
If regime differences are exclusively visible in P(θ, t) —
i.e. in structures of higher order than first and second moments —
then those regimes are invisible to all current observables.

The completeness of the regime partition is therefore an open question:
not "were the regimes counted correctly",
but "were all regimes seen at all".
```

---

## Candidates for New Observables

From the latent degrees of freedom, concrete candidates emerge,
ordered by priority:

| Candidate | From LF | BC class | Expected property | Priority |
|---|---|---|---|---|
| σ²(θ) | LF-03 | Aggregation | Second moment of P(θ) — complements r_ss | high |
| ψ(t) | LF-04 | Restriction | Collective rotation phase — measures drift | medium |
| C(τ) = ⟨δθ(t)δθ(t+τ)⟩ | LF-10 | Coupling | Correlation function — time structure | medium |
| λ_max(T) spectrum | LF-12, 16 | Aggregation | Multiple Lyapunov exponents | low |
| w_topo | LF-02 | Restriction | Winding number — topologically discrete | low |

### σ²(θ) as Primary Candidate

σ²(θ) is the natural complement to r_ss:

```
r_ss     = |⟨e^(iθ)⟩|    — coherence (first mode)
σ²(θ)   = Var(θ)          — dispersion (second moment)
```

Together, r_ss + σ²(θ) would provide two independent projections from
P(θ, t) that should structurally see different regime boundaries.
However, analysis shows they share Z_shared entirely — no complementarity
at κ_c. See `docs/advanced/observable_decomposition.md` for details.

---

## Types of Latent Degrees of Freedom

```
latent-fundamental:
    LF-SHARED-A (P(θ,t)) — underlies all observables,
    not accessible by extending individual observables

latent-external:
    LF-02, 04, 05, 06, 08, 10, 11, 12, 13, 14, 15, 16
    — outside B, accessible via new observable or B-extension

latent-internal:
    LF-07 — partially in B, but not fully exploited
```

---

## Open Questions

1. Is the regime partition complete relative to P(θ, t)?
   → `docs/notes/open_questions.md`: Q_NEW_6

2. Under what criteria does a latent degree of freedom become a new
   observable vs. a B-extension?
   → `docs/notes/open_questions.md`: Q_NEW_3 (already open)

3. Why is Symmetry Breaking absent from all latent degrees of freedom?
   → `docs/notes/open_questions.md`: Q_NEW_7

---

## Related Documents

- `docs/advanced/observable_decomposition.md` — decomposition of the four observables
- `docs/advanced/observable_consequences.md` — consequences K1–K6
- `docs/glossary/observable_range.md` — R(π), F0
- `docs/bc_taxonomy/boundary_condition_classes.md` — BC classes 1–6
- `docs/notes/open_questions.md` — Q_NEW_3, Q_NEW_6, Q_NEW_7
