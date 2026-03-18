---
status: claim
---

# Observable Decomposition: Basis Operations and BC Mapping

## Motivation and Program

An observable π is typically treated as atomic — a measurement that assigns
a value to a state. ARW permits a deeper analysis:

**Every non-trivial observable is a composition of basis operations that can
be traced back to operator signatures (S1–S5) and BC classes.**

The decomposition program consists of four steps:

```
1. Decompose the observable into basis operations
2. Fully inventory the pre-scope substrate
3. Check Δ-stability of each substrate assumption → observable range R(π)
4. Map basis operations to BC classes → identify latent degrees of freedom
```

Latent degrees of freedom are parameters contained in the operator structure
of π but not explicitly encoded in the scope S = (B, Π, Δ, ε). They are
candidates for new observables or for extensions of B.

---

## Pre-Scope Substrate

The pre-scope substrate of an observable π is the ordered set of assumptions
A = {A_i} that guarantee its algebraic and topological well-definedness —
**before** the scope S takes effect.

Substrate hierarchy for r_ss:

```
A0  State space assumptions
 └─ A1  Quotient / topology / algebra
     └─ A2  Measure / integration
         └─ A3  Dynamics / ergodicity
             └─ A4  Thermodynamic limit
                 └─ A5  Norm projection
                     └─ A6  Stationarity
```

Each level presupposes the one below. The substrate is hierarchical —
no layer can be skipped.

---

## Decomposition 1: r_ss (Kuramoto Order Parameter)

### Definition

```
r_ss · e^(iψ) = (1/N) · Σ_j e^(i·θ_j(t))

r_ss = lim_{T→∞} (1/T) · ∫ | (1/N) · Σ_j e^(i·θ_j(t)) | dt
```

### Basis Operations

```
op_1:  θ_j         → selection of j-th oscillator              [S1: projection]
op_2:  e^(i·θ_j)   → quotient projection R → S¹               [S1: quotient]
op_3:  (1/N)·Σ_j   → discrete expectation over ensemble        [S5: expectation]
op_4:  |·|          → norm projection C → R⁺                   [S1: projection]
op_5:  lim_{T→∞}   → attractor limit                           [S4: dissipation asymptotic]
```

### BC Structure

```
r_ss = Dissipation ∘ Restriction ∘ Aggregation ∘ Restriction ∘ Restriction
```

Three of five operations are Restriction. r_ss is structurally a
**cascade of information losses**, closed by aggregation and an attractor limit.

### Special Structure: S¹ Embedding

op_2 is not an arbitrary transformation:

```
φ: R → R/2πZ ≅ S¹
```

is a group quotient map. R/2πZ is an abelian group; S¹ carries an
induced group structure with Haar measure. This is the only reason the
ensemble mean (S5 / op_3) is geometrically well-defined.

The group structure of S¹ is **not encoded in B, Π, Δ, ε** — it is a
meta-assumption about X itself, prior to the scope definition.

S¹ also carries topological structure: π₁(S¹) = Z (winding numbers).
Winding numbers are discrete integer-valued invariants — first-order
latent degrees of freedom invisible in r_ss.

### Pre-Scope Substrate (summary, 25 assumptions across A0–A6)

| Level | Key assumptions | Δ-stability |
|---|---|---|
| A0: State space | θ_j ∈ R, N discrete, independent | mostly robust |
| A1: Quotient | θ ~ θ+2π, abelian group, S¹ continuous | fragile / collapse |
| A2: Measure | Haar measure unique, μ_stat abs. continuous, LLN | fragile |
| A3: Dynamics | trajectories exist, ergodicity, μ_stat unique, transients decay | fragile at κ_c |
| A4: Thermo. limit | N large, fluctuations small, mean-field scaling | fragile at κ_c |
| A5: Norm projection | |·| well-defined, phase ψ discarded | robust / scope decision |
| A6: Stationarity | r(t) converges, T-independent, no slow drift | fragile at κ_c |

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All j' ≠ j | Individual phase dynamics |
| op_2 | Winding number ∈ Z | Topological invariant |
| op_3 | Distribution of θ_j | Higher moments (variance, skewness, ...) |
| op_4 | Collective phase ψ | Rotation mode of ensemble |
| op_5 | Transient dynamics | Relaxation structure, convergence rate |

### Observable Range

```
R(r_ss) = { κ ≪ κ_c } ∪ { κ ≫ κ_c }
Z(r_ss) = { κ ≈ κ_c }
```

At κ ≈ κ_c, assumptions A3.2, A3.4, A3.5, A4.2, A6.2 are simultaneously fragile.

---

## Decomposition 2: var_rel (Relative Angular Variance)

### Definition

```
var_rel = Var(θ₁ - θ₂) / Var_ref
```

Var_ref: reference variance at fully incoherent state.

### Basis Operations

```
op_1:  θ₁, θ₂         → selection of two degrees of freedom    [S1: projection]
op_2:  θ₁ - θ₂        → difference / relative coordinate       [S1: implicit quotient]
op_3:  (·)²            → squaring (sign discarded)             [S1: restriction]
op_4:  E[(·)]          → expectation (time average)            [S5: expectation]
op_5:  E[(·)] - E[·]²  → centering step                        [S5: conditional structure]
op_6:  (·) / Var_ref   → normalization                         [S4: scaling]
```

### BC Structure

```
var_rel = Scaling ∘ Aggregation ∘ Aggregation ∘ Restriction ∘ Restriction ∘ Restriction
```

### Structural Difference from r_ss

var_rel carries **no** S¹ quotient structure. Δθ = θ₁ - θ₂ lives in R,
not R/2πZ. This makes var_rel robust against topological assumptions —
but fragile against **phase wrapping** at large amplitudes (A1.3):
when Δθ reaches the order of 2π, the difference on R is incorrect.

var_rel also carries a **pair selection assumption** (A5.2): the pair
(θ₁, θ₂) must be representative of the system. With heterogeneous
coupling structure, var_rel is pair-dependent — a latent degree of freedom
in the coupling geometry.

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All other pairs (θ_i, θ_j) | Global coupling structure |
| op_2 | Absolute phases θ₁, θ₂ | Individual dynamics |
| op_3 | Sign of Δθ | Direction of phase difference |
| op_4 | Distribution of Δθ | Higher moments |
| op_5 | Time structure of fluctuations | Correlation time, spectrum |
| op_6 | Absolute scaling | System-specific energy scale |

### Observable Range

```
R(var_rel) = { E < E_diff, |Δθ| ≪ 2π }
Z(var_rel) = { chaotic diffusion } ∪ { phase wrapping at large amplitudes }
```

---

## Decomposition 3: lambda_proxy (Finite Lyapunov Estimator)

### Definition

```
lambda_proxy = (1/T) · log( |δθ(T)| / |δθ(0)| )
```

The true Lyapunov exponent would be:

```
λ_true = lim_{T→∞} lim_{|δθ(0)|→0} (1/T) · log( |δθ(T)| / |δθ(0)| )
```

lambda_proxy takes **neither limit**.

### Basis Operations

```
op_1:  δθ(0)            → selection of initial perturbation     [S1: projection]
op_2:  |·|               → norm projection                      [S1: projection]
op_3:  log(·)            → logarithmic scaling                  [S4: scaling]
op_4:  |δθ(T)|/|δθ(0)|  → ratio formation                      [S4: scaling]
op_5:  (1/T)·(·)         → time normalization                   [S4: scaling]
op_6:  finite T           → truncated limit                     [approximation — no BC class]
```

### BC Structure

```
lambda_proxy = Approximation ∘ Dissipation³ ∘ Restriction²
```

**op_6 is not a BC class.** It is a truncated limit — an approximation
assumption that structurally fails to converge near regime boundaries.

### The Structural Problem

```
A6.1 (finite T sufficient)       — violated by construction
A6.2 (finite |δθ(0)| sufficient) — violated by construction
```

These assumptions are not fixable by better measurement — they are
inherent to the definition of lambda_proxy. The systematic error is
unavoidable.

Consequence: lambda_proxy is **structurally insufficient by construction**,
not because the scope is wrong, but because the observable approximates
a limit it can in principle never reach. The insufficiency follows from
the operator structure, not from empirical findings alone.

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All other perturbation directions | Lyapunov spectrum (not just max LE) |
| op_2 | Directional information of δθ | Unstable manifold |
| op_3+4 | Non-exponential growth | Polynomial / sub-exponential dynamics |
| op_5 | Time structure of growth | Intermittency, fluctuations of λ(t) |
| op_6 | Convergence behavior | Finite-time Lyapunov spectrum |

### Observable Range

```
R(lambda_proxy) = { deeply chaotic: λ_true ≫ 0 } ∪ { deeply ordered: λ_true ≪ 0 }
Z(lambda_proxy) = { transition regions } ∪ { weak chaos: λ_true ≈ 0 }
```

---

## Decomposition 4: σ²(θ) (Phase Variance)

### Definition

```
σ²(θ) = (1/N) · Σ_j (θ_j - θ̄)²    where  θ̄ = (1/N) · Σ_j θ_j
```

Key structural difference from r_ss: θ̄ is an **arithmetic mean on R**,
not on S¹. No quotient structure is applied.

### Basis Operations

```
op_1:  θ_j              → selection of j-th oscillator          [S1: projection]
op_2:  θ̄ = (1/N)·Σ θ_j → arithmetic ensemble mean on R        [S5: expectation on R]
op_3:  θ_j - θ̄          → centering / residual                  [algebraic]
op_4:  (·)²              → squaring                             [S1: restriction]
op_5:  (1/N)·Σ(·)²      → expectation of square                [S5: expectation]
op_6:  lim_{T→∞}         → stationary limit                     [S4: dissipation asymptotic]
```

### BC Structure

```
σ²(θ) = Dissipation ∘ Aggregation ∘ Restriction ∘ Restriction ∘ Aggregation ∘ Restriction
```

### Critical Difference from r_ss

| Assumption | r_ss | σ²(θ) | Difference |
|---|---|---|---|
| S¹ quotient structure | yes (A1.1–1.5) | no | fundamental |
| Group structure / Haar measure | yes | no | fundamental |
| Arithmetic mean on R | no | yes (A1.1) | fundamental |
| Phase wrapping sensitivity | no (S¹ robust) | yes (A1.3) | critical |
| Ergodicity | yes (A3.2) | yes (A3.3) | shared |
| Uniqueness of μ_stat | yes (A3.4) | yes (A4.4) | shared |
| Critical slowing down | yes (A3.5) | yes (A4.5) | shared |
| Sensitivity to multimodality | robust | fragile (A1.2) | different |

### Observable Range

```
R(σ²(θ)) = { κ: σ(θ) ≪ π  and  P(θ) unimodal  and  ergodic }

Z(σ²(θ)) = Z_shared ∪ Z_wrap ∪ Z_multi
  Z_shared = { κ ≈ κ_c }          — shared with r_ss
  Z_wrap   = { σ(θ) ≈ π }         — own exclusion zone: phase wrapping on R
  Z_multi  = { P(θ) multimodal }  — own exclusion zone: θ̄ not a location parameter
```

### Answer to Q_NEW_8: Does σ²(θ) see into Z(r_ss)?

Z_shared is shared entirely between r_ss and σ²(θ). Both collapse at
κ ≈ κ_c from the same dynamic reasons (ergodicity, uniqueness of μ_stat,
critical slowing down). **No complementarity at κ_c.**

σ²(θ) has its own exclusion zones not shared with r_ss:
- Z_wrap appears when σ(θ) ≈ π — possible in the incoherent regime
  where r_ss still works
- Z_multi appears when P(θ) is bimodal — also possible in the incoherent regime

This yields the precise complementarity picture:

```
               κ ≪ κ_c       κ ≈ κ_c      κ ≫ κ_c
              (incoherent)  (transition)  (synchronous)
──────────────────────────────────────────────────────
r_ss             ✓             ✗            ✓
σ²(θ)            ✓ / ✗*        ✗            ✓
──────────────────────────────────────────────────────
* fragile when σ(θ) large or P(θ) multimodal
```

---

## Comparison: All Four Observables

```
                  r_ss           var_rel        lambda_proxy   σ²(θ)
────────────────────────────────────────────────────────────────────────
Operations          5               6               6            6
BC structure     R³·A·D         R³·A²·S         R²·D³·Approx  R³·A²·D
Collapses          8               7              7+2*           5
Fragile           13              16              18            16
Robust             3               2               1             1
Critical zone   κ ≈ κ_c       E high + wrap    transitions    κ ≈ κ_c
                                                everywhere
Topo. assumption S¹ (strong)   R (weak)        TₓX (medium)   R (weak)
Moment          1st (Fourier)  2nd (Δθ)        local (λ)      2nd (θ)
────────────────────────────────────────────────────────────────────────
* structurally violated by construction
```

### Shared Structure

- All four are **Restriction-dominated**
- All four depend on **ergodicity**
- All four are **blind to higher moments** of the phase distribution
- All four share latent degree of freedom: full distribution P(θ, t)

### Z_shared as Dynamic Universal Zone

```
Z_shared = { p ∈ P | ergodicity violated
                  OR μ_stat not unique
                  OR critical slowing down diverges }
```

For all π in observable class E (stationary expectations):

```
∀ π ∈ E:  Z(π) ⊇ Z_shared
```

Z_shared is a **lower bound** on the exclusion zone — no observable
of this class can reliably operate at κ_c. This is not a measurement
problem; it is a structural constraint imposed by the system dynamics.

---

## Implications for ARW

### 1. Π is not atomic

The components of Π (observables) are not primitive objects. Every
observable carries an internal structure of basis operations, a pre-scope
substrate, and an observable range. This structure should be part of scope
documentation.

### 2. F0 as a new falsification category

The existing categories F1–F4 do not apply when an observable is used
outside its range. F0 is needed:

```
F0: R(π) ∩ B ≠ B  (observable outside its range)
    Severity: observable_replacement (not scope_rejection)
```

### 3. Latent degrees of freedom as extension candidates

Every Restriction operation in an observable generates a latent degree
of freedom. This is a candidate for:
- A new observable π' with its own scope S'
- An extension of B (if the degree of freedom is system-relevant)

### 4. Observable range as scope design criterion

When designing a scope:

```
R(π) ⊇ { parameter region of interest, including regime boundaries θ* }
```

If this is not satisfied, the scope is structurally blind to the most
interesting physics.

---

## Related Documents

- `docs/glossary/observable_range.md` — formal definition of R(π), F0
- `docs/glossary/scope.md` — scope tuple S = (B, Π, Δ, ε)
- `docs/bc_taxonomy/boundary_condition_classes.md` — BC classes 1–6
- `docs/advanced/latent_degrees_of_freedom.md` — BC mapping, LF-SHARED-A
- `docs/advanced/observable_consequences.md` — consequences K1–K6
- `docs/notes/open_questions.md` — Q_NEW_1–12
