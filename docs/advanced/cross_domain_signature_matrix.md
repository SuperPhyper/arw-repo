---
status: working-definition
source: derived from "Gleiche Operator-Signaturen in vielen Domänen" (2026-03-14)
layer: docs/advanced/
related: operator_signature_catalog.md, operator_signatures_cross_domain.md
---

# Cross-Domain Signature Matrix

This document provides the extended reference matrix mapping the five canonical operator
signatures (S1–S5) to nine domains. It expands the summary table in
`operator_signature_catalog.md` with sub-signatures, structural notes, and
domain-specific caveats.

**Level:** ARW (domain-neutral). Each cell names the structural instance, not the
concrete model equations — those belong in `docs/art_instantiations/` or `cases/`.

---

## Column Legend

| Code | Domain |
|---|---|
| DS | Dynamical Systems / Physics |
| CT | Control Theory |
| SP | Statistical Physics |
| QM | Quantum Mechanics |
| ECO | Ecology / Population Dynamics |
| NEURO | Neuroscience / Computational Neuroscience |
| ML | Machine Learning |
| EPI | Epidemiology / Social Systems |
| CAT | Category Theory / structural formalisms |

---

## Primary Matrix

### S1 — Projection / Selection → BC: Restriction (also Aggregation, Symmetry Breaking)

| Domain | Instance | Sub-signature | Structural note |
|---|---|---|---|
| DS | Poincaré section → First-Return Map | Section projection | Continuous flow reduced to discrete return map on Σ |
| CT | Output map `y = Cx` | Linear projection onto observation space | Selects observable subspace of state |
| SP | Zwanzig projection (relevant/irrelevant) | Orthogonal projector `P`, `Q = 1−P` | Explicit projection-operator construction; basis for GLE |
| QM | Projective measurement / Lüders update | `P_m ρ P_m / tr(...)` | PVM special case; non-commutative; state collapse |
| ECO | SIR/SEIR compartmentalization | Coarse-graining projection | Micro-individual → macro-aggregate state |
| NEURO | Spike-Triggered Average | Conditional summary operator | Projects stimulus space onto spike-triggered subspace |
| ML | PCA / linear embedding | Rank-k projector `W^T x` | Minimizes reconstruction error; orthogonal projector |
| EPI | Compartment reduction | Aggregation map | Same structure as ECO; explicit macro-state selection |
| CAT | Product projections `π_A`, `π_B` | Universal property of products | Defines projection categorically; basis for all instances |

**Sub-signatures present in S1:**

| Sub-signature | Description | Key invariant |
|---|---|---|
| Idempotent projector | `p ∘ p = p` | Idempotence |
| Orthogonal projector | `P = P*`, `P² = P` | Orthogonality + idempotence |
| Coarse-graining map | Many-to-one aggregation | Information loss; not invertible |
| Section / hyperplane cut | Flow restricted to Σ | Dimension reduction by 1 |
| Quotient projection | `X → X/~` | Equivalence class selection |

---

### S2 — Product ∘ Composition → BC: Coupling

| Domain | Instance | Sub-signature | Structural note |
|---|---|---|---|
| DS | Coupled ODE system `(ẋ, ẏ) = (f(x,y), g(x,y))` | Joint state + cross terms | No block-diagonal structure |
| CT | Feedback interconnection (plant + controller) | Product state + feedback composition | Åström & Murray structural principle |
| SP | Ising model | Configuration space `{−1,+1}^N`, coupling `J_{ij} s_i s_j` | Pairwise interaction = cross terms in energy |
| QM | Composite system | Tensor product `H_A ⊗ H_B` | **Non-Cartesian product** — see caveat below |
| ECO | Lotka-Volterra | `(x,y)` with cross terms `αxy`, `−βxy` | Classical product-state coupling |
| NEURO | E/I spiking network | High-dim. product state + synaptic weight matrix | Synaptic coupling = parameterized cross-term operator |
| ML | Layer composition in deep nets | `f_L ∘ ... ∘ f_1` | Sequential composition; coupling across layers |
| EPI | Multi-group SIR | Product of group states + cross-infection terms | Coupling between population groups |
| CAT | Pairing `⟨f, g⟩`, monoidal product | Universal property of products + natural pairing | QM case: dagger-compact category (Abramsky & Coecke) |

**Sub-signatures present in S2:**

| Sub-signature | Description | Key invariant |
|---|---|---|
| Cartesian coupling | `X₁ × X₂`, mixed `F` | Cross terms in dynamics |
| Tensor coupling (QM) | `H_A ⊗ H_B`, entanglement possible | Non-Cartesian; enables non-separable states |
| Parameter coupling | One system's state enters another's parameters | Weaker than full coupling; no joint state space needed |
| Feedback composition | Output of B fed back as input to A | Composition forms a loop, not a chain |

> **QM caveat:** The product in QM is tensorial (`⊗`), not Cartesian (`×`). Entangled
> states have no classical product-state interpretation. This is the primary case requiring
> extension of the ARW primitive "product". → `docs/advanced/quantum_operator_extension.md`

---

### S3 — Time-Coupled Product → BC: Forcing

| Domain | Instance | Sub-signature | Structural note |
|---|---|---|---|
| DS | Periodically forced oscillator `ẋ = f(x,t)` | `X × T`, periodic `T = S¹` | Non-autonomous; stroboscopic map available |
| CT | Time-variant system `ẋ = A(t)x + B(t)u(t)` | `X × ℝ`, exogenous input `u(t)` | Standard non-autonomous state-space form |
| SP | Driven / non-equilibrium systems (NESM) | External driving field `F(t)` | Breaks time-reversal symmetry |
| QM | TDSE with external field `iℏ∂_t ψ = H(t)ψ` | `H(t)` = time-dependent Hamiltonian | External field enters as `X × T` extension |
| ECO | Seasonal population dynamics | `β(t)` or `K(t)` periodic | Environmental forcing; `T = S¹` |
| NEURO | Stimulus-driven neural response | Stimulus `s(t)` as external input | System is non-autonomous during stimulus presentation |
| ML | Transformer / Attention (sequence index) | Token index as discrete `T = ℤ` | Index coupling, not physical time; structural analogy |
| EPI | Term-time / seasonal SEIR `β(t)` | Periodic transmission rate | Produces regime switching and complex epidemic dynamics |
| CAT | Monoid action `T × X → X` | Action axioms (`e·x = x`, `(st)·x = s·(t·x)`) | Generalizes time coupling to arbitrary monoid `T` |

**Sub-signatures present in S3:**

| Sub-signature | Description | Key invariant |
|---|---|---|
| Continuous time-coupling | `T = ℝ`, `ẋ = f(x,t)` | Non-autonomous ODE |
| Periodic forcing | `T = S¹`, `f(x, t+τ) = f(x,t)` | Stroboscopic / Poincaré reduction possible |
| Discrete index coupling | `T = ℤ` or finite index set | Used in ML sequence models |
| Exogenous input coupling | `u(t)` independent of system state | Control-theoretic standard case |

---

### S4 — Scaling ∘ Composition → BC: Dissipation

| Domain | Instance | Sub-signature | Structural note |
|---|---|---|---|
| DS | Damped oscillator, friction term `−γẋ` | Contraction in phase space | Attractor = fixed point or limit cycle |
| CT | Stable closed-loop system, Lyapunov decay | `‖x(t)‖ ≤ c e^{−λt} ‖x(0)‖` | Exponential stability = contraction |
| SP | Relaxation toward equilibrium | `ρ(t) → ρ_eq` as `t → ∞` | Semigroup evolution; convergence rate `c` |
| QM | Lindblad / GKSL dynamics | CP semigroup `ρ(t) = e^{Lt} ρ(0)` | Dissipative; relaxation onto stationary state |
| ECO | Logistic growth (Verhulst) | Self-limiting; saturation at `K` | Not a contraction in full sense; contraction-like regime |
| NEURO | Leaky Integrate-and-Fire | Leak term `−V/τ_m` | Exponential decay of membrane potential |
| ML | L2 regularization / weight decay | `w ← (1 − λη) w − η ∇L` | Systematic shrinkage; effective capacity damping |
| EPI | Disease extinction / decay phase | `I(t) → 0` below herd immunity threshold | Dissipative regime of epidemic dynamics |
| CAT | Endomorphism with contraction | Lipschitz constant `< 1` | Banach fixed-point theorem applies |

**Sub-signatures present in S4:**

| Sub-signature | Description | Key invariant |
|---|---|---|
| Metric contraction | `‖F(x)−F(y)‖ ≤ c‖x−y‖`, `c < 1` | Unique fixed point (Banach) |
| Exponential decay | `‖x(t)‖ ≤ C e^{−λt}` | Decay rate `λ > 0` |
| CP semigroup (QM) | `e^{Lt}`, `L` Lindblad generator | Completely positive; trace-preserving |
| Asymptotic projector | Dissipation → attractor projection **in the limit** | Not finite composition — limit operation only |

> **Important limit caveat:** Dissipation produces Restriction (projection onto attractor)
> **only asymptotically**, not as a finite operator composition. "Dissipation generates
> Restriction" is a limit statement. This must be kept explicit when relating S4 to S1.
> → Open question Q-DISS-01 in `docs/notes/open_questions.md`

---

### S5 — Expectation / Conditional Expectation as Projection → BC: Stochastic Coupling + Reduction

| Domain | Instance | Sub-signature | Structural note |
|---|---|---|---|
| DS | Stochastic reduction of noise-driven system | Marginalizing over noise realization | Projection onto deterministic envelope |
| CT | MMSE estimator / Kalman filter | `E[x | Z_k]` = orthogonal projection in L² | Minimizes MSE; conditional mean |
| SP | Mori-Zwanzig formalism → GLE | `P` = projection onto relevant observables | Memory terms arise from projected-out degrees |
| QM | Born rule / measurement statistics | `Tr(P_m ρ)` as expectation of projector | Probability as expectation value of projector |
| ECO | Environmental noise averaging | `E[x | environment class]` | Effective dynamics over environmental ensemble |
| NEURO | Spike-Triggered Average / decoding | `P(x | s)`, conditional statistics | STA = conditional summary of stimulus-response |
| ML | Scaled Dot-Product Attention | `∑ softmax(QKᵀ/√d) · V` ≈ discrete `E[V | query]` | Formal expectation over value distribution |
| EPI | Risk / expected case count | `E[cases | intervention]` | Conditional forecast as projection |
| CAT | Adjunction / conditioning structure | Right adjoint as "best approximation" | Categorical generalization of conditional expectation |

**Sub-signatures present in S5:**

| Sub-signature | Description | Key invariant |
|---|---|---|
| L²-orthogonal projection | `E[· | G] = Proj_{L²(G)}(·)` | Idempotence; tower law; MSE minimization |
| MMSE estimator | `argmin_f E[(X − f(G))²]` = `E[X|G]` | Optimality condition |
| Discrete weighted sum | `∑ wᵢ vᵢ`, `∑ wᵢ = 1` | Finite-sample approximation to expectation |
| Mori-Zwanzig projector | `P` onto relevant observables, `Q = 1−P` | Connects to S1; memory kernel arises from `Q` |

---

## Parameter Coupling (Sub-Signature across S2/S3)

A frequently occurring sub-signature that sits between S2 (Coupling) and S3 (Forcing):

**Parameter coupling:** One system's state enters another system's *parameters* rather than
its state space directly.

```
ẋ = f(x; θ(y)),   θ : Y → Θ
```

This is weaker than full state-space coupling (no joint `X × Y` required) but stronger
than pure forcing (the parameter depends on a co-evolving system, not an exogenous clock).

| Domain | Instance |
|---|---|
| ECO | Predator density modulates prey growth rate |
| NEURO | Neuromodulator concentration modulates synaptic gain |
| EPI | Intervention policy modulates transmission rate `β` |
| ML | Hypernetwork: one network outputs weights of another |

---

## Quotient / Coarse-Graining (Sub-Signature of S1)

A structurally important sub-signature of S1 that deserves explicit listing:

**Quotient projection:** `X → X/~` where `~` is an equivalence relation on states.

```
π_~ : X → X/~,   x ↦ [x]
```

| Domain | Instance |
|---|---|
| SP | Coarse-graining in renormalization (block spins) |
| DS | Quotient dynamics on orbit space |
| EPI | SIR compartmentalization (all susceptibles are equivalent) |
| CAT | Coequalizer / quotient object |
| ML | Embedding layer (discrete tokens → equivalence classes in ℝ^d) |

---

## Structural Caveats Summary

| Caveat | Affects | Description |
|---|---|---|
| Non-Cartesian product (QM) | S2, S5 | Tensor `⊗` ≠ Cartesian `×`; entanglement has no classical analog |
| Non-unique BC semantics | S1 | Projection appears as Restriction, Aggregation, Measurement, Coarse-Graining — context determines BC label |
| Dissipation → Restriction only asymptotically | S4 → S1 | Not a finite composition; limit operation only |
| Irreducible domain-specific operators | S4, S3 | Renormalization, semigroup generators may require own primitives in extensions |
| Discrete vs. continuous T | S3 | `T = ℤ` (ML, discrete maps) vs `T = ℝ` (physics) — same structural role, different mathematical category |

---

## Cross-Reference to Open Questions

| Open Question | Relevant Signatures | Location |
|---|---|---|
| Q-DISS-01: Dissipation → Restriction: limit or composition? | S4, S1 | `docs/notes/open_questions.md` |
| Q-SIG-01: Uniqueness of BC semantics (ARW-Q15) | S1, S2, S5 | `docs/notes/open_questions.md` |
| Q-TENSOR-01: Extension `×` → `⊗` for QM | S2, S5 | `docs/advanced/quantum_operator_extension.md` |

---

*Generated from: "Gleiche Operator-Signaturen in vielen Domänen" (project resource, 2026-03-14)*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
