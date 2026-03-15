---
status: open-question
source: derived from "Gleiche Operator-Signaturen in vielen Domänen" (2026-03-14)
layer: docs/advanced/
related: operator_signature_catalog.md, cross_domain_signature_matrix.md
open_questions: [Q-TENSOR-01, Q-SIG-01]
---

# Quantum Operator Extension

This document examines what happens when ARW's primitive operator basis —
composition `∘`, product `×`, projection `π` — is applied to quantum mechanical
systems. The central finding is that the QM case exposes a structural limit of the
current primitive set and motivates a generalization from Cartesian to monoidal products.

**Status:** This is an open-question document. It frames the problem and proposes
directions; it does not yet contain resolved definitions.

---

## The Core Problem

ARW's primitive "product" `×` is implicitly Cartesian: for two systems A and B, the
joint state space is `A × B`, and states are pairs `(a, b)`. Crucially, every state of
the joint system decomposes into a state of A and a state of B.

In quantum mechanics this is false. The joint Hilbert space of two systems is the
**tensor product** `H_A ⊗ H_B`, and generic states are **not** separable:

```
|ψ⟩ ∈ H_A ⊗ H_B   does NOT imply   |ψ⟩ = |φ_A⟩ ⊗ |φ_B⟩
```

Entangled states have no classical product-state decomposition. This means:

- S2 (Product ∘ Composition / Coupling) works in QM, but with `⊗` not `×`
- S5 (Expectation as Projection) works in QM, but the probability rule
  involves `Tr(P_m ρ)`, not a direct L²-projection in the classical sense
- The BC class "Coupling" remains valid as a semantic label, but the underlying
  primitive must be generalized

---

## Cartesian vs. Monoidal Product

### Cartesian product (classical setting)

```
A × B   with   π_A : A × B → A,   π_B : A × B → B
```

- Every element of `A × B` has a unique decomposition `(a, b)`
- Projections are total and deterministic
- Diagonals exist: `Δ : A → A × A`
- Copying and deleting states is free

### Monoidal (tensor) product (quantum setting)

```
H_A ⊗ H_B   (tensor product of Hilbert spaces)
```

- Generic states are **not** decomposable as `|φ_A⟩ ⊗ |φ_B⟩`
- No global projection `H_A ⊗ H_B → H_A` that preserves the full quantum state
  (partial trace is the closest analog, but it is a trace, not a projection)
- No-cloning theorem: `Δ : H → H ⊗ H` does not exist as a unitary
- No-deleting theorem: erasure is not a free operation

### Categorical framing

Both cases are instances of a **symmetric monoidal category**:

| Property | Cartesian (Set, Vect classical) | Monoidal (Hilb, FdHilb) |
|---|---|---|
| Product | `×` (Cartesian) | `⊗` (tensor) |
| Unit object | `{*}` (terminal) | `ℂ` (ground field) |
| Diagonal | `Δ(a) = (a,a)` ✅ | No unitary diagonal ❌ |
| Projections | `π_A`, `π_B` total ✅ | Partial trace only; lossy ❌ |
| Entanglement | Impossible by definition | Generic feature |

The framework of **dagger-compact categories** (Abramsky & Coecke 2004) provides
a categorical foundation where QM's tensor structure is native.

---

## Impact on ARW Signatures

### S2 — Coupling

The structural role "couple subsystems via a joint state space" is preserved. The
primitive changes:

| Setting | Joint state space | Primitive |
|---|---|---|
| Classical | `X₁ × X₂` | Cartesian `×` |
| Quantum | `H_A ⊗ H_B` | Tensor `⊗` |

**ARW consequence:** If the primitive `×` is generalized to "symmetric monoidal product",
S2 applies to both settings without modification at the signature level. The BC label
"Coupling" remains stable.

### S5 — Expectation as Projection

In classical probability: `E[X | G] = Proj_{L²(G)}(X)` — a genuine L²-orthogonal
projection.

In quantum mechanics the closest analog is the **partial trace**:

```
ρ_A = Tr_B(ρ_{AB})
```

This is:
- Linear ✅
- Positive ✅
- Trace-preserving ✅
- **Not** a projector in the operator sense (`Tr_B ∘ Tr_B ≠ Tr_B` in general) ❌

The partial trace is better understood as a **conditional expectation on a von Neumann
algebra** — which does recover the projection interpretation, but in a non-commutative
function algebra, not in classical L².

**ARW consequence:** S5 requires either (a) restriction to the classical/commutative
sub-case, or (b) extension of "conditional expectation" to non-commutative conditional
expectations (operator algebraic setting).

### S1 — Projection / Selection

Projective measurements in QM are genuine projectors (`P² = P`, `P = P*`) — S1 applies
directly. However:

- Measurement is **destructive**: post-measurement state is `P|ψ⟩/‖P|ψ⟩‖`, not just
  a selection from a pre-existing ensemble
- Non-commutativity: `[P_m, P_n] ≠ 0` in general — measurement order matters
- Multiple measurements do not compose as classical projections

**ARW consequence:** S1 applies at the signature level, but the BC label "Restriction"
needs a non-classical reading: it restricts **into** a post-measurement state, not
**onto** a pre-existing sub-state-space.

---

## CP Maps and the Dissipation Signature

Markovian open quantum dynamics (Lindblad / GKSL) is given by a completely positive
trace-preserving (CPTP) map or its generator:

```
dρ/dt = Lρ = −i[H, ρ] + ∑_k (L_k ρ L_k† − ½{L_k†L_k, ρ})
```

This is:
- A semigroup evolution `ρ(t) = e^{Lt} ρ(0)` → matches S4 (Dissipation / contraction)
- Completely positive → physically valid quantum operation
- Generally irreversible → entropy-increasing

CP maps are **not** expressible as `Scaling ∘ Composition` in the classical sense, but
they are the quantum analog of the dissipation signature. The semigroup structure
(S4 invariant) is preserved; the operator algebra is non-commutative.

---

## Proposed Primitive Extension

To natively cover QM, ARW's primitive "product" should be generalized:

| Current | Proposed extension | Covers |
|---|---|---|
| `×` (Cartesian product) | Symmetric monoidal product `⊗` | Classical × and quantum ⊗ as special cases |
| Classical composition `∘` | Composition in dagger category | Adjoint / unitary operations |
| Projection `π` | Completely positive map (CP map) | Quantum channels, measurements, partial trace |

This extension would make QM a **native domain** of ARW rather than a special case
requiring per-signature caveats.

---

## Open Questions

### Q-TENSOR-01: Extend `×` → `⊗`

**Question:** Should ARW's primitive "product" be redefined as a symmetric monoidal
product, making Cartesian and tensor products both special cases?

**Implications:**
- Positive: QM becomes native; S2 and S5 generalize cleanly
- Risk: increased abstraction cost for classical-domain users
- Requirement: categorical reformulation of at least S2 and S5

*Status: open — requires decision on scope of ARW primitive layer*

### Q-TENSOR-02: Non-commutative conditional expectation for S5

**Question:** Can S5 (Expectation as Projection) be extended to non-commutative
conditional expectations on von Neumann algebras, and does the ARW BC label
"Stochastic coupling + reduction" remain meaningful in that setting?

**Implications:**
- Connects to Takesaki's theory of conditional expectations on von Neumann algebras
- Mori-Zwanzig already sits at the boundary (classical projection operator on a
  quantum-like structure)

*Status: open — significant technical depth required*

### Q-TENSOR-03: Which BC labels are stable under the extension?

**Question:** If the primitive `×` is generalized to `⊗`, which BC class assignments
remain stable and which need revision?

**Preliminary assessment:**

| BC Class | Stability under `×` → `⊗` | Note |
|---|---|---|
| Restriction | Partially stable | Measurement-as-restriction needs non-classical reading |
| Coupling | Stable | Structural role preserved; primitive changes |
| Forcing | Stable | `H(t)` is a direct analog of `f(x,t)` |
| Dissipation | Stable at signature level | CP semigroup = quantum analog |
| Aggregation | Needs review | Partial trace ≠ classical coarse-graining |
| Symmetry Breaking | Stable | Spontaneous symmetry breaking exists in QM |

*Status: open — requires case study (see validation program, action 4)*

---

## Recommended Next Step

**Validation action 4** from `docs/notes/validation_program_signatures.md`:

Implement a QM case study covering:
1. Projective measurement (S1 / Restriction)
2. Tensorial composite system (S2 / Coupling)
3. Lindblad dissipation (S4 / Dissipation)

and check for each whether the current ARW primitive set is sufficient, and which
BC labels survive the extension.

---

## Primary Sources

- Abramsky & Coecke (2004), *A categorical semantics of quantum protocols*
  (dagger-compact categories, tensor as monoidal product)
- Nielsen & Chuang (2010), *Quantum Computation and Quantum Information*,
  chapters on composite systems, measurement, quantum operations
- Lindblad (1976), *On the Generators of Quantum Dynamical Semigroups*
- Takesaki (1972), *Conditional expectations in von Neumann algebras*
  (non-commutative conditional expectation)
- Mac Lane, *Categories for the Working Mathematician*
  (monoidal categories, universal properties of products)

---

*Generated from: "Gleiche Operator-Signaturen in vielen Domänen" (project resource, 2026-03-14)*
*Verified against: arw-repo-context SKILL, arw-meta-guard SKILL*
