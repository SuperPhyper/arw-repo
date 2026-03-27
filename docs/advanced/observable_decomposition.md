---
status: claim
---

# Observable Decomposition: Base Operations, Pre-Scopal Substrates, and BC Mapping

## Motivation and Program

An observable π is typically treated as atomic — a measurement that assigns
a value to a state. ARW permits a deeper analysis:

**Every non-trivial observable is a composition of base operations that can
be traced back to operator signatures (S1–S5) and BC classes.**

The decomposition program consists of four steps:

```
1. Decompose the observable into base operations
2. Fully inventory the pre-scopal substrate
3. Check Δ-stability of each substrate assumption → observable range R(π)
4. Map base operations to BC classes → identify latent degrees of freedom
```

Latent degrees of freedom are parameters contained in the operator structure
of π but not explicitly encoded in the scope S = (B, Π, Δ, ε). They are
candidates for new observables or for extensions of B.

---

## Pre-Scopal Substrate: Concept

The pre-scopal substrate of an observable π is the ordered set of assumptions
A = {A_i} that guarantee its algebraic and topological well-definedness —
**before** the scope S begins.

The substrate is hierarchical: each level presupposes the one below.
No layer can be skipped. The substrate precedes the scope definition —
it constitutes π as a well-defined expression before S = (B, Π, Δ, ε) begins.

**Stability classification used throughout:**
- **collapses**: assumption violation renders π undefined or meaningless
- **fragile**: assumption violation systematically distorts π
- **partially robust**: assumption violation has limited or recoverable effect
- **robust**: assumption violation has negligible effect on π

---

## Decomposition 1: r_ss (Kuramoto Order Parameter)

### Definition

```
r_ss · e^(iψ) = (1/N) · Σ_j e^(i·θ_j(t))

r_ss = lim_{T→∞} (1/T) · ∫ | (1/N) · Σ_j e^(i·θ_j(t)) | dt
```

### Base Operations

```
op_1:  θ_j          → selection of j-th oscillator             [S1: projection]
op_2:  e^(i·θ_j)    → quotient projection R → S¹               [S1: quotient]
op_3:  (1/N)·Σ_j    → discrete expectation over ensemble        [S5: expectation]
op_4:  |·|           → norm projection C → R⁺                  [S1: projection]
op_5:  lim_{T→∞}    → attractor limit                          [S4: dissipation, asymptotic]
```

### BC Structure

```
r_ss = Dissipation ∘ Restriction ∘ Aggregation ∘ Restriction ∘ Restriction
```

Three of five operations are Restriction. r_ss is structurally a
**cascade of information losses**, closed by aggregation and an attractor limit.

### Special Structure: S¹ Embedding

op_2 is not an arbitrary transformation. The map

```
φ: R → R/2πZ ≅ S¹
```

is a group quotient map. R is an abelian group under addition; 2πZ is a
normal subgroup; R/2πZ ≅ S¹ as a topological group. S¹ inherits a group
structure with a canonical Haar measure. This group structure is the
**prerequisite for op_3** (S5 expectation): the ensemble mean is
geometrically canonical only because S¹ has a group structure.

S¹ also carries non-trivial topological structure: π₁(S¹) = Z.
Winding numbers are discrete, integer-valued topological invariants —
**first-order latent degrees of freedom** invisible in r_ss.

The group structure and topology of S¹ are **not encoded in B, Π, Δ, ε**.
They are meta-assumptions about X itself, prior to the scope definition.

### Pre-Scopal Substrate: Full Inventory

#### Level A0: State Space

| Assumption | Content | Type |
|---|---|---|
| A0.1 | θ_j ∈ R (real, unbounded) | topological |
| A0.2 | N oscillators discretely indexable | algebraic |
| A0.3 | Phases independently parametrizable | structural |

#### Level A1: Quotient Structure

```
φ: R → R/2πZ ≅ S¹
```

| Assumption | Content | Type |
|---|---|---|
| A1.1 | θ ~ θ + 2π (identification well-defined) | quotient |
| A1.2 | 2πZ is a normal subgroup of (R, +) | algebraic |
| A1.3 | S¹ carries induced group structure | algebraic |
| A1.4 | φ is continuous and surjective | topological |
| A1.5 | Fiber φ⁻¹(p) discrete and uniformly distributed | metric |

#### Level A2: Measure and Integration

```
E[e^(iθ_j)] under μ
```

| Assumption | Content | Type |
|---|---|---|
| A2.1 | Haar measure on S¹ exists and is unique | measure theory |
| A2.2 | μ_stat is absolutely continuous w.r.t. Haar measure | measure theory |
| A2.3 | e^(iθ) is μ-integrable | analysis |
| A2.4 | Discrete average (1/N)Σ_j approximates ∫ dμ_stat | LLN |

#### Level A3: Dynamical Assumptions

```
lim_{T→∞} (1/T) ∫₀ᵀ (·) dt
```

| Assumption | Content | Type |
|---|---|---|
| A3.1 | Trajectories exist for all t ≥ 0 | existence |
| A3.2 | Ergodicity: time average = ensemble average | dynamical |
| A3.3 | μ_stat is invariant under the flow | dynamical |
| A3.4 | μ_stat is unique (no multistability) | dynamical |
| A3.5 | Transients decay (attractor exists) | dynamical |
| A3.6 | Attractor independent of initial conditions | dynamical |

#### Level A4: Thermodynamic Limit

```
N → ∞
```

| Assumption | Content | Type |
|---|---|---|
| A4.1 | N large enough for LLN approximation | statistical |
| A4.2 | Finite-N fluctuations negligible | statistical |
| A4.3 | Coupling structure scales with N (mean-field) | structural |
| A4.4 | Phase transition sharp only in limit N→∞ | dynamical |

#### Level A5: Norm Projection

```
|·|: C → R⁺
```

| Assumption | Content | Type |
|---|---|---|
| A5.1 | Modulus well-defined on C | algebraic |
| A5.2 | Phase ψ discarded (information loss accepted) | scope decision |
| A5.3 | R⁺ is sufficient description space for coherence | model decision |

#### Level A6: Stationarity

```
r_ss = stationary value
```

| Assumption | Content | Type |
|---|---|---|
| A6.1 | r(t) converges to a constant limit | dynamical |
| A6.2 | Limit independent of observation time T | dynamical |
| A6.3 | No slow drift or intermittency | dynamical |

### Δ-Stability Analysis

#### Level A0

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A0.1 θ_j ∈ R | θ_j complex or discrete | φ not definable | **collapses** |
| A0.2 N discrete | N continuous (density field) | sum → integral; r_ss formally recoverable | **robust** |
| A0.3 Independent | Constraints between θ_j | effective dimension reduced | **partially robust** |

#### Level A1

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A1.1 θ ~ θ+2π | Period ≠ 2π (e.g. p/q resonance) | r_ss measures wrong coherence | **fragile** |
| A1.2 2πZ normal subgroup | Non-abelian group (e.g. SO(3)) | mean not canonically defined | **collapses** |
| A1.3 Group structure on S¹ | No group structure (only manifold) | Haar measure lost | **collapses** |
| A1.4 φ continuous | Discontinuous phase jumps | r_ss measurement unstable | **fragile** |
| A1.5 Fiber uniform | Asymmetric fiber (noise asymmetry) | systematic bias in r_ss | **fragile** |

#### Level A2

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A2.1 Haar measure unique | Multiple invariant measures | r_ss measure-dependent, not unique | **collapses** |
| A2.2 μ_stat abs. continuous | μ_stat singular (e.g. Cantor set) | integral not well-defined | **collapses** |
| A2.3 Integrability | e^(iθ) not integrable | technically unlikely in practice | **robust** |
| A2.4 LLN approximation | Strong correlations between θ_j | LLN fails; r_ss fluctuates strongly | **fragile** |

#### Level A3

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A3.1 Trajectories exist | Finite-time explosion | r_ss undefined after explosion time | **collapses** |
| A3.2 Ergodicity | Non-ergodic invariant tori (κ < κ_c) | r_ss time- and IC-dependent | **fragile** |
| A3.3 μ_stat flow-invariant | Slow drift of measure | r_ss time-dependent, no limit | **fragile** |
| A3.4 μ_stat unique | Multistability (multiple attractors) | r_ss IC-dependent | **fragile** |
| A3.5 Transients decay | Critical slowing (κ ≈ κ_c) | r_ss converges arbitrarily slowly | **fragile** |
| A3.6 Attractor IC-independent | Coexisting attractors | r_ss not reproducible | **fragile** |

#### Level A4

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A4.1 N large | Small N (e.g. N=3) | strong fluctuations; r_ss statistical | **fragile** |
| A4.2 Fluctuations negligible | Critical fluctuations (κ ≈ κ_c) | r_ss fluctuates as O(N^{-1/2}) | **fragile** |
| A4.3 Mean-field scaling | Non-mean-field coupling (local, NN) | r_ss measures non-existent global coherence | **collapses** |
| A4.4 Transition sharp | Finite N | transition smeared; κ_c not sharp | **partially robust** |

#### Level A5

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A5.1 Modulus well-defined | Ambiguous modulus (e.g. p-adic) | technically irrelevant physically | **robust** |
| A5.2 Phase ψ discarded | ψ carries relevant information | r_ss blind to rotation mode | **scope decision** |
| A5.3 R⁺ sufficient | Coherence multi-dimensional | r_ss underestimates structure | **fragile** |

#### Level A6

| Assumption | Perturbation | Consequence for r_ss | Stability |
|---|---|---|---|
| A6.1 r(t) converges | Permanent oscillation of r(t) | r_ss has no limit | **collapses** |
| A6.2 T-independent | Intermittency or slow modulation | r_ss T-dependent; not reproducible | **fragile** |
| A6.3 No slow drift | Aging or slow relaxation | r_ss systematically distorted | **fragile** |

### Stability Summary

```
Stability         Count    Levels
collapses           8      A0.1, A1.2, A1.3, A2.1, A2.2, A3.1, A4.3, A6.1
fragile            13      A1.1, A1.4, A1.5, A2.4, A3.2–3.6, A4.1–4.2, A5.3, A6.2–6.3
partially robust    2      A0.3, A4.4
robust              3      A0.2, A2.3, A5.1
scope decision      1      A5.2
```

**Critical observation:** The fragile assumptions cluster precisely at κ ≈ κ_c:
A3.2, A3.4, A3.5, A4.2, A6.2 are simultaneously fragile there.
r_ss is structurally designed to work far from the phase transition.
At the most interesting point (κ ≈ κ_c) it violates five pre-scopal
assumptions simultaneously.

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All j' ≠ j | Individual phase dynamics θ_j(t) |
| op_2 | Winding number ∈ Z | Topological invariant |
| op_3 | Distribution of θ_j | Higher moments (variance, skewness, ...) |
| op_4 | Collective phase ψ | Rotation mode of ensemble |
| op_5 | Transient dynamics | Relaxation structure, convergence rate |

### Observable Range

```
R(r_ss) = { κ ≪ κ_c } ∪ { κ ≫ κ_c }
Z(r_ss) = { κ ≈ κ_c }
```

---

## Decomposition 2: var_rel (Relative Angular Variance)

### Definition

```
var_rel = Var(θ₁ - θ₂) / Var_ref
```

Var_ref: reference variance at fully incoherent state.

### Base Operations

```
op_1:  θ₁, θ₂         → selection of two degrees of freedom    [S1: projection]
op_2:  θ₁ - θ₂        → difference / relative coordinate       [S1: implicit quotient]
op_3:  (·)²            → squaring (sign discarded)              [S1: restriction]
op_4:  E[(·)]          → expectation value (time average)       [S5: expectation]
op_5:  E[(·)] - E[·]²  → centering step                         [S5: conditional structure]
op_6:  (·) / Var_ref   → normalization                          [S4: scaling]
```

### BC Structure

```
var_rel = Scaling ∘ Aggregation ∘ Aggregation ∘ Restriction ∘ Restriction ∘ Restriction
```

### Structural Difference from r_ss

var_rel carries **no** S¹ quotient structure. Δθ = θ₁ - θ₂ lives in R,
not R/2πZ. This makes var_rel robust against topological assumptions —
but fragile against **phase wrapping** at large amplitudes: when Δθ reaches
the order of 2π, the difference computed on R is incorrect.

var_rel additionally carries a **pair selection assumption**: the pair
(θ₁, θ₂) must be representative of the system. With heterogeneous coupling
structure, var_rel is pair-dependent — a latent degree of freedom in the
coupling geometry.

### Pre-Scopal Substrate: Full Inventory

#### Level A0: State Space

| Assumption | Content | Type |
|---|---|---|
| A0.1 | θ₁, θ₂ ∈ R (real, unbounded) | topological |
| A0.2 | Two degrees of freedom separately selectable | structural |
| A0.3 | Difference θ₁ - θ₂ well-defined on R | algebraic |

#### Level A1: Difference Structure

```
Δθ = θ₁ - θ₂
```

| Assumption | Content | Type |
|---|---|---|
| A1.1 | Difference linear and well-defined | algebraic |
| A1.2 | Δθ is the relevant degree of freedom (not θ₁, θ₂ separately) | model decision |
| A1.3 | Δθ ∈ R (no quotient structure imposed) | topological |
| A1.4 | Sign of Δθ irrelevant for variance | symmetry assumption |

#### Level A2: Measure and Expectation

```
E[Δθ²] - E[Δθ]²
```

| Assumption | Content | Type |
|---|---|---|
| A2.1 | Stationary measure μ_stat exists for Δθ | measure theory |
| A2.2 | E[Δθ²] finite (second moment exists) | analysis |
| A2.3 | E[Δθ] finite (first moment exists) | analysis |
| A2.4 | Ergodicity: time average = ensemble average | dynamical |
| A2.5 | μ_stat absolutely continuous w.r.t. Lebesgue measure on R | measure theory |

#### Level A3: Dynamical Assumptions

| Assumption | Content | Type |
|---|---|---|
| A3.1 | Trajectories exist for all t ≥ 0 | existence |
| A3.2 | Δθ(t) stationary in the relevant regime | dynamical |
| A3.3 | No divergence of Δθ (bounded dynamics) | dynamical |
| A3.4 | μ_stat unique (no multistability) | dynamical |
| A3.5 | Transients decay | dynamical |

#### Level A4: Normalization Structure

```
Var_ref
```

| Assumption | Content | Type |
|---|---|---|
| A4.1 | Var_ref well-defined and finite | analysis |
| A4.2 | Var_ref > 0 (no division by zero) | structural |
| A4.3 | Var_ref system-independent (external reference) | model decision |
| A4.4 | Normalization linear and monotone | structural |

#### Level A5: Selection Assumptions

```
θ₁ - θ₂ as choice of degrees of freedom
```

| Assumption | Content | Type |
|---|---|---|
| A5.1 | Exactly two degrees of freedom selected | scope decision |
| A5.2 | Pair (θ₁, θ₂) representative of the system | model decision |
| A5.3 | Other pairs yield equivalent information | symmetry assumption |
| A5.4 | Relative phase fully encoded in difference | structural |

### Δ-Stability Analysis

#### Level A0

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A0.1 θ ∈ R | θ on S¹ (quotient) | difference mod 2π; variance distorted | **fragile** |
| A0.2 Separately selectable | Constraints between θ₁, θ₂ | effective dimension reduced | **partially robust** |
| A0.3 Difference well-defined | Non-commutative structure | difference not canonical | **collapses** |

#### Level A1

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A1.1 Linearity | Nonlinear coupling geometry | Δθ not a natural degree of freedom | **fragile** |
| A1.2 Δθ relevant | Individual θ_j carry more information | var_rel underestimates structure | **fragile** |
| A1.3 Δθ ∈ R | Phase wrapping (Δθ mod 2π) | variance systematically underestimated at large swings | **fragile** |
| A1.4 Sign symmetry | Asymmetric dynamics | variance robust; structural information lost | **robust** |

#### Level A2

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A2.1 μ_stat exists | Non-stationary dynamics | variance time-dependent | **collapses** |
| A2.2 E[Δθ²] finite | Heavy-tailed distribution | variance diverges | **fragile** |
| A2.3 E[Δθ] finite | Drift in Δθ | centering step distorted | **fragile** |
| A2.4 Ergodicity | Non-ergodic regimes (e.g. chaos) | time average ≠ ensemble average | **fragile** |
| A2.5 Abs. continuity | Singular measure (fractal attractor) | variance not well-defined | **collapses** |

#### Level A3

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A3.1 Existence | Explosion | var_rel undefined | **collapses** |
| A3.2 Stationarity | Energy input / slow drift | var_rel grows unboundedly | **fragile** |
| A3.3 Boundedness | Chaotic diffusion (high E) | Δθ diffuses; variance diverges | **fragile** |
| A3.4 Uniqueness | Multistability | var_rel IC-dependent | **fragile** |
| A3.5 Transients | Critical slowing | convergence arbitrarily slow | **fragile** |

#### Level A4

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A4.1 Var_ref finite | Pathological reference system | normalization undefined | **collapses** |
| A4.2 Var_ref > 0 | Fully ordered reference | division by zero | **collapses** |
| A4.3 Var_ref system-independent | Var_ref influenced by system | circular normalization | **fragile** |
| A4.4 Linearity | Nonlinear normalization | monotonicity lost | **robust** |

#### Level A5

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A5.1 Exactly two | N > 2 degrees of freedom relevant | var_rel projects onto subspace | **fragile** |
| A5.2 Representativity | Asymmetric coupling | pair choice biases result | **fragile** |
| A5.3 Equivalence of pairs | Heterogeneous coupling | var_rel pair-dependent | **fragile** |
| A5.4 Difference complete | Higher-order correlations relevant | var_rel blind to structure | **fragile** |

### Stability Summary

```
Stability         Count    Levels
collapses           7      A0.3, A2.1, A2.5, A3.1, A4.1, A4.2, (A3.3 at high E)
fragile            16      A0.1, A1.1–1.3, A2.2–2.4, A3.2–3.5, A4.3, A5.1–5.4
partially robust    1      A0.2
robust              2      A1.4, A4.4
scope decision      2      A5.1, A5.2
```

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
R(var_rel) = { E < E_diff,  |Δθ| ≪ 2π }
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

### Base Operations

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

### Pre-Scopal Substrate: Full Inventory

#### Level A0: State Space

| Assumption | Content | Type |
|---|---|---|
| A0.1 | Tangent space TₓX well-defined | differential-geometric |
| A0.2 | δθ ∈ TₓX (perturbation in tangent space) | structural |
| A0.3 | Linearization of flow valid for |δθ| small | analysis |
| A0.4 | Norm on TₓX well-defined and consistent | metric |

#### Level A1: Linearization Structure

```
δθ(T) ≈ Dφ_T(x₀) · δθ(0)
```

| Assumption | Content | Type |
|---|---|---|
| A1.1 | Flow φ_T differentiable in x | analysis |
| A1.2 | Jacobian Dφ_T exists and is finite | analysis |
| A1.3 | Linearization valid over entire interval [0,T] | analysis |
| A1.4 | Perturbation remains infinitesimal (no nonlinear regime) | structural |

#### Level A2: Norm Structure

```
|δθ(T)| / |δθ(0)|
```

| Assumption | Content | Type |
|---|---|---|
| A2.1 | Norm sub-multiplicative and consistent | metric |
| A2.2 | Ratio norm-independent in limit T→∞ | analysis |
| A2.3 | |δθ(0)| > 0 (no division by zero) | structural |
| A2.4 | Growth isotropic (direction-independent) | symmetry assumption |

#### Level A3: Logarithmic Structure

```
log(|δθ(T)| / |δθ(0)|)
```

| Assumption | Content | Type |
|---|---|---|
| A3.1 | Ratio > 0 (perturbation grows or stays) | structural |
| A3.2 | Growth exponential (not polynomial, not super-exponential) | dynamical |
| A3.3 | log well-defined and finite | analysis |

#### Level A4: Time Structure

```
(1/T) · (·)  and finite T
```

| Assumption | Content | Type |
|---|---|---|
| A4.1 | T large enough for convergence to λ_true | dynamical |
| A4.2 | Transients decayed before measurement begins | dynamical |
| A4.3 | No regime change during [0,T] | dynamical |
| A4.4 | (1/T)·log converges monotonically | analysis |
| A4.5 | Finite T gives good approximation | **proxy assumption** |

#### Level A5: Directional Structure

```
Choice of δθ(0)
```

| Assumption | Content | Type |
|---|---|---|
| A5.1 | Random δθ(0) converges to maximal LE (Oseledets) | Oseledets theorem |
| A5.2 | Maximal LE representative of chaos degree | model decision |
| A5.3 | Single direction sufficient (no Lyapunov spectrum needed) | scope decision |
| A5.4 | δθ(0) not accidentally in stable subspace | structural |

#### Level A6: Proxy Structure

```
lambda_proxy ≈ λ_true
```

| Assumption | Content | Type |
|---|---|---|
| A6.1 | Finite T sufficient | **approximation assumption** |
| A6.2 | Finite |δθ(0)| sufficient | **approximation assumption** |
| A6.3 | Proxy monotone with λ_true (order preserved) | model decision |
| A6.4 | Proxy reliably distinguishes chaos from order | **core claim** |

### Δ-Stability Analysis

#### Level A0

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A0.1 Tangent space | Non-differentiable flow | linearization undefined | **collapses** |
| A0.2 δθ ∈ TₓX | Discrete states | tangent space non-existent | **collapses** |
| A0.3 Linearization valid | Large perturbations | nonlinear terms dominate | **fragile** |
| A0.4 Norm consistent | Energy-dependent norm | lambda_proxy scaling-dependent | **fragile** |

#### Level A1

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A1.1 Differentiability | Non-smooth flow | Jacobian undefined | **collapses** |
| A1.2 Jacobian finite | Singularity in flow | lambda_proxy diverges | **fragile** |
| A1.3 Linearization over [0,T] | Regime change in [0,T] | linearization breaks | **fragile** |
| A1.4 Infinitesimal | Finite perturbation (measurement noise) | nonlinear saturation | **fragile** |

#### Level A2

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A2.1 Norm consistent | State-dependent metric | ratio norm-dependent | **fragile** |
| A2.2 Norm-independence | Short T | norm-dependence remains | **fragile** |
| A2.3 |δθ(0)| > 0 | Numerical zero | division by zero | **collapses** |
| A2.4 Isotropy | Anisotropic growth | directional lambda_proxy | **fragile** |

#### Level A3

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A3.1 Ratio > 0 | Perturbation shrinks | log negative — still defined | **robust** |
| A3.2 Exponential growth | Polynomial growth (marginal chaos) | lambda_proxy → 0 but T-dependent | **fragile** |
| A3.3 log finite | Ratio = 0 or ∞ | log undefined | **fragile** |

#### Level A4

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A4.1 T large enough | T too short | lambda_proxy ≠ λ_true systematically | **fragile** |
| A4.2 Transients decayed | Measurement during transient | lambda_proxy overestimates | **fragile** |
| A4.3 No regime change | Transition region E ≈ E_c | lambda_proxy averages over regimes | **fragile** |
| A4.4 Monotone convergence | Intermittency | lambda_proxy fluctuates strongly | **fragile** |
| A4.5 Finite T sufficient | Slowly chaotic systems | proxy systematically too small | **fragile** |

#### Level A5

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A5.1 Oseledets | Short T | convergence to max LE not guaranteed | **fragile** |
| A5.2 Max LE representative | Sub-dimensional chaos | max LE overestimates chaos degree | **fragile** |
| A5.3 Single direction | Multiple unstable directions | Lyapunov spectrum needed | **fragile** |
| A5.4 Not in stable subspace | Unlucky random choice | lambda_proxy underestimates | **fragile** |

#### Level A6

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A6.1 T sufficient | Always violated by construction | systematic error unavoidable | **structurally fragile** |
| A6.2 |δθ(0)| sufficient | Always violated by construction | systematic error unavoidable | **structurally fragile** |
| A6.3 Monotone with λ_true | Nonlinear regime | order not preserved | **fragile** |
| A6.4 Distinguishes chaos | Weak chaos (λ_true ≈ 0) | proxy not discriminative | **collapses** |

### Stability Summary

```
Stability              Count    Levels
collapses                7      A0.1, A0.2, A1.1, A2.3, A6.4, (+A6.1*, A6.2*)
structurally fragile     2      A6.1, A6.2 (violated by construction)
fragile                 18      majority
robust                   1      A3.1
scope decision           1      A5.3
```

### The Structural Problem

A6.1 and A6.2 are not fixable by better measurement — they are inherent
to the definition of lambda_proxy. The systematic error is unavoidable.
lambda_proxy is **structurally insufficient by construction**: the
insufficiency follows from operator structure, not from empirical findings.
This provides a structural explanation for the empirical finding
lambda_proxy: primary=false in CASE-0003.

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All other perturbation directions | Full Lyapunov spectrum |
| op_2 | Directional information of δθ | Unstable manifold |
| op_3+4 | Non-exponential growth | Polynomial / sub-exponential dynamics |
| op_5 | Time structure of growth | Intermittency, fluctuations of λ(t) |
| op_6 | Convergence behavior | Finite-time Lyapunov spectrum |

### Observable Range

```
R(lambda_proxy) = { deeply chaotic: λ_true ≫ 0 } ∪ { deeply ordered: λ_true ≪ 0 }
Z(lambda_proxy) = { transition regions } ∪ { weak chaos: λ_true ≈ 0 }
```

Z(lambda_proxy) is structurally wider than for r_ss and var_rel, because
A6.1 + A6.2 are violated everywhere — the exclusion zone is not confined
to a local parameter region but appears wherever λ_true is not clearly
separated from zero.

---

## Decomposition 4: σ²(θ) (Phase Variance)

### Definition

```
σ²(θ) = (1/N) · Σ_j (θ_j - θ̄)²     where  θ̄ = (1/N) · Σ_j θ_j
```

Key structural difference from r_ss: θ̄ is an **arithmetic mean on R** —
not on S¹. No quotient structure is applied.

### Base Operations

```
op_1:  θ_j              → selection of j-th oscillator           [S1: projection]
op_2:  θ̄ = (1/N)·Σ θ_j → arithmetic ensemble mean on R         [S5: expectation on R]
op_3:  θ_j - θ̄          → centering / residual                   [algebraic]
op_4:  (·)²              → squaring                              [S1: restriction]
op_5:  (1/N)·Σ(·)²      → expectation of square                 [S5: expectation]
op_6:  lim_{T→∞}         → stationary limit                      [S4: dissipation, asymptotic]
```

### BC Structure

```
σ²(θ) = Dissipation ∘ Aggregation ∘ Restriction ∘ Restriction ∘ Aggregation ∘ Restriction
```

### Pre-Scopal Substrate: Full Inventory

#### Level A0: State Space

| Assumption | Content | Type |
|---|---|---|
| A0.1 | θ_j ∈ R (real, unbounded) | topological |
| A0.2 | N oscillators discretely indexable | algebraic |
| A0.3 | Phases independently parametrizable | structural |

#### Level A1: Arithmetic Mean Structure

```
θ̄ = (1/N) · Σ_j θ_j   on R
```

| Assumption | Content | Type |
|---|---|---|
| A1.1 | Addition on R well-defined (no quotient structure) | algebraic |
| A1.2 | θ̄ is a representative location parameter | model decision |
| A1.3 | Phase wrapping irrelevant (θ_j ∈ R, not S¹) | **topological — critical** |
| A1.4 | Mean exists and is finite | analysis |

#### Level A2: Centering Structure

```
θ_j - θ̄
```

| Assumption | Content | Type |
|---|---|---|
| A2.1 | Residual well-defined on R | algebraic |
| A2.2 | Residual is the relevant degree of freedom | model decision |
| A2.3 | E[θ_j - θ̄] = 0 by construction | structural |
| A2.4 | Centering fully removes drift | dynamical |

#### Level A3: Measure and Expectation

```
E[(θ_j - θ̄)²]
```

| Assumption | Content | Type |
|---|---|---|
| A3.1 | Stationary measure μ_stat exists for θ_j | measure theory |
| A3.2 | E[θ²] finite (second moment exists) | analysis |
| A3.3 | Ergodicity: time average = ensemble average | dynamical |
| A3.4 | μ_stat absolutely continuous w.r.t. Lebesgue on R | measure theory |
| A3.5 | Uniform sampling over j | statistical |

#### Level A4: Dynamical Assumptions

| Assumption | Content | Type |
|---|---|---|
| A4.1 | Trajectories exist for all t ≥ 0 | existence |
| A4.2 | σ²(θ, t) converges to stationary value | dynamical |
| A4.3 | No divergence of θ_j (bounded dispersion) | dynamical |
| A4.4 | μ_stat unique (no multistability) | dynamical |
| A4.5 | Transients decay | dynamical |

#### Level A5: Stationarity Assumptions

| Assumption | Content | Type |
|---|---|---|
| A5.1 | σ²(θ) T-independent in stationary regime | dynamical |
| A5.2 | No slow drift of variance | dynamical |
| A5.3 | Fluctuations of σ²(θ,t) negligible | statistical |

### Δ-Stability Analysis

#### Level A0

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A0.1 θ_j ∈ R | θ_j on S¹ forced | arithmetic mean geometrically wrong | **fragile** |
| A0.2 N discrete | N → ∞ density field | sum → integral; robust | **robust** |
| A0.3 Independent | Constraints between θ_j | effective dimension reduced | **partially robust** |

#### Level A1

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A1.1 Addition on R | Circular geometry relevant | θ̄ on R wrong at large dispersions | **fragile** |
| A1.2 θ̄ representative | Multimodal distribution | θ̄ lies between modes — not a location parameter | **fragile** |
| A1.3 No phase wrapping | Dispersion large (σ ≈ π) | phase wrapping distorts σ²(θ) | **fragile** |
| A1.4 Mean finite | Heavy-tailed distribution | θ̄ diverges | **fragile** |

#### Level A2

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A2.1 Residual well-defined | Non-commutative structure | difference not canonical | **collapses** |
| A2.2 Residual relevant | Absolute phase carries information | centering loses information | **fragile** |
| A2.3 E[residual] = 0 | Systematic drift | centering assumption violated | **fragile** |
| A2.4 Centering removes drift | Slow phase drift | σ²(θ) grows unboundedly | **fragile** |

#### Level A3

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A3.1 μ_stat exists | Non-stationary dynamics | σ²(θ) time-dependent | **collapses** |
| A3.2 E[θ²] finite | Heavy-tailed distribution | variance diverges | **fragile** |
| A3.3 Ergodicity | Non-ergodic regimes | time average ≠ ensemble average | **fragile** |
| A3.4 Abs. continuity | Singular measure | σ²(θ) not well-defined | **collapses** |
| A3.5 Uniform sampling | Heterogeneous oscillators | variance pair-dependent | **fragile** |

#### Level A4

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A4.1 Existence | Explosion | σ²(θ) undefined | **collapses** |
| A4.2 Convergence | Permanent oscillation | no stationary limit | **collapses** |
| A4.3 Boundedness | Diffusion (high E) | σ²(θ) grows ~ t | **fragile** |
| A4.4 Uniqueness | Multistability | σ²(θ) IC-dependent | **fragile** |
| A4.5 Transients | Critical slowing | convergence arbitrarily slow | **fragile** |

#### Level A5

| Assumption | Perturbation | Consequence | Stability |
|---|---|---|---|
| A5.1 T-independence | Intermittency | σ²(θ) T-dependent | **fragile** |
| A5.2 No drift | Aging / slow relaxation | σ²(θ) systematically distorted | **fragile** |
| A5.3 Fluctuations small | Small N | σ²(θ) statistically unstable | **fragile** |

### Stability Summary

```
Stability         Count    Levels
collapses           5      A2.1, A3.1, A3.4, A4.1, A4.2
fragile            16      majority
partially robust    1      A0.3
robust              1      A0.2
```

### Critical Structural Comparison with r_ss

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

### Observable Range and Complementarity with r_ss

```
R(σ²(θ)) = { κ: σ(θ) ≪ π  and  P(θ) unimodal  and  ergodic }

Z(σ²(θ)) = Z_shared ∪ Z_wrap ∪ Z_multi
  Z_shared = { κ ≈ κ_c }          — shared with r_ss (ergodicity, slowing)
  Z_wrap   = { σ(θ) ≈ π }         — own exclusion zone: phase wrapping on R
  Z_multi  = { P(θ) multimodal }  — own exclusion zone: θ̄ not location parameter
```

**Does σ²(θ) see into Z(r_ss)?** No — not in the strong sense.

Z_shared is shared entirely between r_ss and σ²(θ). Both collapse at
κ ≈ κ_c from the same dynamic reasons: ergodicity, uniqueness of μ_stat,
and critical slowing down are **shared substrate assumptions** arising from
the dynamics (A3/A4), not from the specific algebraic structure of the
observable. The dynamics near κ_c violates these assumptions for all
observables that presuppose a stationary expectation value.

However, σ²(θ) has its own exclusion zones not shared with r_ss —
Z_wrap and Z_multi can occur in the incoherent regime (κ ≪ κ_c)
where r_ss still functions:

```
               κ ≪ κ_c       κ ≈ κ_c      κ ≫ κ_c
              (incoherent)  (transition)  (synchronous)
──────────────────────────────────────────────────────
r_ss             ✓             ✗            ✓
σ²(θ)            ✓ / ✗*        ✗            ✓
──────────────────────────────────────────────────────
* fragile when σ(θ) large (phase wrapping) or P(θ) multimodal
```

The two observables are **not complementary** in the strong sense at κ_c.
Partial complementarity exists only in the incoherent regime.

### Latent Degrees of Freedom

| Operation | Discarded information | Latent degree of freedom |
|---|---|---|
| op_1 | All j' ≠ j | Individual phase dynamics |
| op_2 | Distribution of θ_j | Moments > 1st order of P(θ) |
| op_3 | Absolute phases | Collective drift θ̄(t) |
| op_4 | Sign of (θ_j - θ̄) | Asymmetry of distribution |
| op_5 | Time structure | Correlation time, spectrum of σ²(θ,t) |
| op_6 | Transients | Relaxation rate of variance |

---

## Comparison: All Four Observables

```
                  r_ss           var_rel        lambda_proxy    σ²(θ)
──────────────────────────────────────────────────────────────────────────
Operations          5               6               6              6
BC structure     R³·A·D         R³·A²·S         R²·D³·Approx   R³·A²·D
Collapses           8               7              7+2*             5
Fragile            13              16              18              16
Robust              3               2               1               1
Critical zone    κ ≈ κ_c      E high + wrap    transitions      κ ≈ κ_c
                                               everywhere
Topo. assumption S¹ (strong)   R (weak)        TₓX (medium)    R (weak)
Moment type     1st (Fourier)  2nd (Δθ)        local (λ)       2nd (θ)
──────────────────────────────────────────────────────────────────────────
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

For all observables in class E (stationary expectations):

```
∀ π ∈ E:  Z(π) ⊇ Z_shared
```

Z_shared is a **lower bound** on the exclusion zone of every observable
in class E. No observable of this class can reliably operate at κ_c.
This is not a measurement problem — it is a structural constraint
imposed by the system dynamics itself.

### Complementarity of Observable Ranges

```
R(r_ss)         fails at κ ≈ κ_c          (topological + ergodic)
R(var_rel)      fails at high E            (diffusive + geometric)
R(lambda_proxy) fails broadly              (constructive)
R(σ²(θ))        fails at κ ≈ κ_c + own   (ergodic + wrapping + multimodal)
```

r_ss and var_rel are structurally complementary — they fail at different
points for different structural reasons. lambda_proxy is the weakest
observable for regime boundaries due to its constructive insufficiency.

---

## Implications for ARW

### 1. Π is not atomic

The components of Π (observables) are not primitive objects. Every
observable carries an internal structure of base operations, a pre-scopal
substrate, and an observable range. This structure should be part of
scope documentation.

### 2. F0 as a new falsification category

The existing categories F1–F4 do not apply when an observable is used
outside its range. F0 is needed:

```
F0: R(π) ∩ B ≠ B  (observable outside its range)
    Severity: observable_replacement (not scope_rejection)
```

Distinction:
- Observable insufficiency (F1): span(π) < 2ε — too little spread
- F0: pre-scopal substrate breaks down — structural unreliability

### 3. Latent degrees of freedom as extension candidates

Every Restriction operation in an observable generates a latent degree
of freedom — a candidate for:
- A new observable π' with its own scope S'
- An extension of B (if system-relevant)

### 4. Observable range as scope design criterion

```
R(π) ⊇ { parameter region of interest, including regime boundaries θ* }
```

If not satisfied, the scope is structurally blind to the most
interesting physics — not by resolution but by structure.

---

## Related Documents

- `docs/glossary/observable_range.md` — formal definition of R(π), F0
- `docs/glossary/scope.md` — scope tuple S = (B, Π, Δ, ε)
- `docs/bc_taxonomy/boundary_condition_classes.md` — BC classes 1–6
- `docs/advanced/latent_degrees_of_freedom.md` — BC mapping, LF-SHARED-A
- `docs/advanced/observable_consequences.md` — consequences K1–K6
- `docs/notes/open_questions.md` — Q_NEW_1–12
