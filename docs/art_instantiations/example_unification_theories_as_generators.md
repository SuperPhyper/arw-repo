---
status: note
layer: docs/art_instantiations/
created: 2026-05-07
last_updated: 2026-05-07
depends_on:
  - docs/art_instantiations/generator_admissibility_taxonomy.md
  - docs/glossary/scope.md
---

# Example: Physical Unification Theories as a Generator Class

## Purpose

This document illustrates the generator admissibility taxonomy
(`generator_admissibility_taxonomy.md`) using physical unification theories —
specifically quadratic gravity — as a concrete example.

It is not a claim about the physics. The physical claims follow the literature
cited below. The ARW/ART mapping is a structural re-interpretation in generator
language, not an assertion attributed to any of the cited authors.

The motivating observation: when a new formal theory is announced as "unifying"
two prior frameworks, the precise epistemic status of that claim is rarely stated
explicitly. The generator taxonomy provides vocabulary for this gap.

---

## Two Predecessor Generators

### G_GR — General Relativity

- **Λ**: spacetime geometries parametrized by matter distribution, curvature,
  and cosmological constant
- **Σ**: dominant S2 (metric coupling) and S4 (geodesic contraction via curvature)
- **Collapse type: Type I** — sharp admissibility boundaries at geometric
  singularities (Schwarzschild radius, cosmological singularities) and at the
  boundary of the semi-classical approximation
- **A_f(G_GR)**: well-characterized for weak-field and cosmological regimes;
  collapses at Planck scale where quantum effects cannot be neglected

### G_QFT — Quantum Field Theory

- **Λ**: Hilbert space structures parametrized by coupling constants and
  energy scales
- **Σ**: dominant S5 (expectation as projection / measurement), S2 (field
  coupling), S3 (time evolution)
- **Collapse type: Type II** — solution space collapse at UV divergences,
  vacuum degeneracy, gauge redundancy; solutions are branch-dependent without
  renormalization or gauge fixing
- **A_f(G_QFT)**: well-characterized within renormalization windows; breaks
  down at gravitational coupling strengths

**Structural observation:** G_GR and G_QFT have different dominant collapse
types. A unification attempt must construct a generator G' whose A(G') contains
both A_f(G_GR) and A_f(G_QFT) as sub-regions — without introducing a new
Type III consistency collapse between their respective signature structures.

---

## Quadratic Gravity as G_QG

Quadratic gravity extends the Einstein-Hilbert action by higher-curvature terms:

> S = ∫ d⁴x √(-g) [ (M_P²/2)(R − 2Λ) − (1/2λ)C² − (1/ξ)R² + … ]

where C² is the Weyl tensor squared and R² is the Ricci scalar squared.
The choice of basis (R², R_μν R^μν, Gauss-Bonnet combinations) varies across
formulations but describes the same higher-derivative structure.

### What the literature establishes

**Established (Stelle 1977 and subsequent):**
- Quadratic gravity is perturbatively renormalizable in 4D — a property
  Einstein-Hilbert gravity alone does not have
- The theory propagates additional degrees of freedom beyond the massless
  graviton: typically a massive spin-2 mode and a scalar mode
- The massive spin-2 sector carries a ghost — negative kinetic energy —
  creating the central tension: renormalizability vs. unitarity/stability

**Established (Buccio, Donoghue, Menezes, Percacci 2024):**
- Known beta functions do not directly encode the physical momentum dependence
  of scattering amplitudes
- "Physical running" can be derived separately; asymptotic freedom is compatible
  with tachyon-freedom under appropriate conditions

**Established (Edelstein et al. 2021):**
- Quadratic gravity produces a positive, polarization-independent Shapiro time
  delay over shockwave backgrounds — passing the CEMZ causality diagnostic
- Higher-derivative terms do not automatically imply causality violation

### Generator mapping

| G = (Λ, Σ, φ, C) component | Quadratic gravity correspondence |
|---|---|
| Λ | Coupling space: (α, β, M_P, Λ_cosm), energy/scale sector, signature choice |
| Σ | Operator structure: metric coupling (S2), higher-derivative propagation, RG flow, gauge constraints |
| φ: Λ → (B, Π) | Generates admissible classes of spacetime/field/observable structures |
| R | Expected regime: GR in IR, QFT-compatible UV behavior, unitarity, causality, empirical reproduction |

**Key result from the mapping:**
G_QG clearly extends A(G) — the formally admissible region — relative to both
predecessors. Whether A_f(G_QG) is correspondingly extended remains the open
question, because A_f requires operational viability: the scope must reproduce
expected regimes at proportional instantiation cost.

---

## Collapse Classification of G_QG

### Type I — inherited from G_GR

The EFT reading of quadratic gravity provides the clearest Type I structure.
EFT treats higher-derivative terms as valid only within a cutoff window; outside
this window, the description loses operative validity. This is a Type I boundary:
not everything that follows formally from resummation is admissible in the EFT
scope. The cutoff marks ∂A(G_EFT) explicitly — making EFT arguably the most
honest admissibility geometry in the table of unification candidates.

### Type II — characteristic of G_QG

The most prominent collapse structure in quadratic gravity is Type II: additional
poles, complex poles, ghost pairs, Fakeon prescriptions, and gauge/branch-dependent
interpretations do not concern an outer parameter boundary but the solution and
spectral structure of G_QG itself.

Several strategies attempt to stabilize this solution landscape:

| Strategy | Mechanism | ARW reading | Status |
|---|---|---|---|
| Local quadratic gravity (Stelle) | Ghost remains in spin-2 sector | Type II unresolved | Formally renormalizable, physically open |
| Fakeon / purely virtual particles (Piva 2023) | Problematic modes mediate interaction but are not external on-shell states | Branch restriction within A_h | Perturbatively worked out; ontologically/causally contested |
| Lee-Wick / complex poles | Ghosts as complex resonance structure | Complex pole branch selection | Formally interesting; stability open |
| Nonlocal / infinite-derivative gravity | Entire form factors avoid additional poles | Type II collapse avoided by construction | Ghost-free at linear level; full Lorentz unitarity open |
| EFT | Higher-derivative terms only perturbative; ghost pole outside validity window | Type I boundary makes Type II moot within window | Methodologically cleanest in IR |

Liu, Modesto, and Calcagni (2023) argue for perturbative unitarity in theories
with complex conjugate ghost pairs — from an ARW perspective, this is a
branch-selection mechanism attempting to stabilize a problematic solution sector
within A_h(G_QG).

### Type III — risk, not established collapse

The central Type III risk is the ghost/unitarity/causality triad. Type III arises
when a generator's internal rule structure produces irresolvable conflicts —
K ≠ ∅ in Σ with no dominance hierarchy.

Quadratic gravity is not automatically Type III. The more precise statement is:

> G_QG carries a Type III risk as long as it remains open whether
> renormalizability, unitarity, causality, and Lorentzian reconstruction can be
> simultaneously stabilized in a physically acceptable generator.

Fakeon/purely-virtual-particle approaches (Piva 2023) accept controlled
microscopic acausality as the price for perturbative unitarity — this is not a
side effect but part of the quantization prescription itself. From a generator
perspective: this resolves the K conflict by accepting one constraint (causality)
as endogenous to the generator's perturbation class Δ, rather than external.
This is a Type III resolution strategy — it redefines what counts as admissible
perturbation rather than eliminating the conflict.

Edelstein et al. (2021) provide evidence against naive Type III collapse on
causality grounds: the positive Shapiro delay result suggests the causality
constraint is not necessarily in conflict with the higher-derivative structure,
at least in the tested regime.

---

## A_h vs. A_f: What Has Actually Been Established

| Level | Assessment |
|---|---|
| A(G_QG) — formal admissibility | Substantially extended relative to G_GR alone |
| A_h(G_QG) — hypothetical admissibility | Substantially extended; solution landscape richer |
| A_f(G_QG) — functional admissibility | Partially extended; not fully characterized |
| Type III risk eliminated | Not yet |

The cleanest summary from the literature:

> Quadratic gravity connects QM and GR more formally than Einstein-Hilbert
> gravity, but does not yet resolve the physical consistency conflict definitively.
> (literature consensus)

In generator language:

> G_QG primarily extends the hypothetically admissible generator space A_h(G).
> It provides local candidates for A_f(G), but global functional admissibility
> still depends on ghost, unitarity, causality, and Lorentz reconstruction questions.

---

## Asymptotic Safety as a Comparison Case

Asymptotic safety is structurally close to generator thinking because it centers
not on a single propagator but on flows in theory space. RG fixed points serve as
the source of renormalizability and predictive power (D'Angelo 2024: non-trivial
fixed point in Lorentzian Einstein-Hilbert truncation).

Saueressig and Wang (2025) examine the relationship between Euclidean and
Lorentzian RG flows via ADM/Wick rotation — supporting the interpretation that
signature and time structure are themselves non-trivial stability questions of the
descriptive regime, not trivially given primitives.

From a generator perspective: asymptotic safety attempts to define A_f(G) via
RG fixed point structure rather than via explicit scope instantiation. The open
question — what physical spectrum and pole structure does the full theory possess
— is the A_f characterization problem in generator language.

---

## The Broader Pattern

Quadratic gravity is one instance of a general pattern:

> A new generator G' is constructed whose A(G') contains the admissible regions
> of two prior generators G₁ and G₂. This is presented as "unification."

The generator taxonomy makes three distinctions that standard discourse conflates:

**Distinction 1 — Formal containment vs. operational overlap:**
A(G') ⊇ A(G₁) ∪ A(G₂) does not imply A_f(G') ⊇ A_f(G₁) ∪ A_f(G₂).

**Distinction 2 — Inherited collapse vs. new collapse:**
G' inherits the collapse geometry of its predecessors and may add new collapse
structure — particularly Type III if predecessor signature structures conflict.

**Distinction 3 — A_h richness vs. A_f characterization:**
The scientific question is not the size of A_h(G) but the characterization of
A_f(G). This applies directly to string theory landscape problems, inflationary
model proliferation, and holographic duality families — all cases of formally
rich A_h(G) with partially characterized A_f(G).

| Theory | Generators combined | Inherited collapse | A_f status | Open collapse risk |
|---|---|---|---|---|
| Quadratic gravity | G_GR + G_QFT | Type I + Type II | Partial | Type III (ghost/unitarity) |
| String theory | G_QFT + G_GR (low-energy limit) | Type II + Type I | Very partial (landscape) | Type III (landscape degeneracy) |
| Loop quantum gravity | G_GR (discretized) | Type I modified | Partial | Type II (continuum limit) |
| EFT gravity | G_QFT restricted | Type II within window | Well-characterized within cutoff | Type I at cutoff boundary |
| Asymptotic safety | G_GR (RG-extended) | Type I modified | Partial (fixed point dependent) | Type II (Lorentz reconstruction) |

EFT gravity remains the most epistemically honest case: it explicitly restricts
A(G_EFT) to a window where A_f is well-characterized and marks the cutoff
boundary as a known Type I collapse. The admissibility geometry is made explicit
by construction — which is precisely what the generator taxonomy recommends as
the ART application protocol.

---

## Structural Homologies: What the Parallel Means and Does Not Mean

The following structural parallels emerge between ARW/ART concepts and problems
in the quadratic gravity literature:

| ARW/ART concept | Corresponding problem in literature |
|---|---|
| A_h vs. A_f distinction | Formal extension vs. operational viability (throughout QG literature) |
| Type II collapse | Branch/pole/spectral ambiguity (ghost poles, Fakeon prescriptions) |
| Type III risk | Unitarity-causality-renormalizability inconsistency |
| Time as stable ordering structure | Non-trivial Lorentz/Wick reconstruction (Saueressig/Wang 2025) |
| Generator family vs. single scope | Theory space / action space (asymptotic safety) |
| Endogenous Δ | Quantization prescription defines admissible perturbations (Fakeon approach) |

**What this means:** ARW/ART provides a language in which structural tensions
identified in the quadratic gravity literature become expressible at a
meta-level. The framework reconstructs some of these tensions from
epistemological and observational principles rather than from technical QFT
machinery.

**What this does not mean:** ARW does not solve the open problems in quantum
gravity. Structural homology is not physical confirmation. The ARW mapping is a
re-description, not a derivation.

The defensible claim is:

> ARW appears to make some recurring structural problems of modern theoretical
> physics formulable at an epistemic-generative level, independent of the
> domain-specific technical apparatus in which they were originally discovered.

---

## Literature Referenced

- Stelle (1977): Perturbative renormalizability of quadratic gravity (foundational)
- Buccio, Donoghue, Menezes, Percacci (2024): Physical running vs. beta functions;
  asymptotic freedom compatible with tachyon-freedom
- Piva (2023): Fakeon / purely virtual particles as renormalizable and unitary
  higher-derivative quantum gravity approach
- Liu, Modesto, Calcagni (2023): Perturbative unitarity for complex conjugate
  ghost pairs in local higher-derivative theories
- Edelstein et al. (2021): Causality of quadratic gravity via Shapiro delay /
  CEMZ diagnostic over shockwave backgrounds
- D'Angelo (2024): Non-trivial fixed point in Lorentzian Einstein-Hilbert
  truncation (asymptotic safety)
- Saueressig, Wang (2025): Euclidean vs. Lorentzian RG flows via ADM/Wick
  rotation in foliated asymptotic safety

---

## Status Note

Physical claims follow the cited literature. The ARW/ART mapping is structural
re-interpretation only — it is not attributed to the cited authors.

Candidate for promotion to `hypothesis` once the generator taxonomy itself
reaches `working-definition` status and at least one collapse type is validated
against an ARW case.
