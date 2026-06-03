---
status: claim
layer: docs/advanced/
date: 2026-06-03
depends_on:
  - docs/advanced/bc_signature_extraction_observables.md
  - docs/advanced/observable_space_cover_height.md
  - docs/advanced/bc_operator_signatures_arw.md
  - docs/core/cover_stability_criterion.md
resolves: Q-NEW-CROSS-2 (forward direction)
verification: numerical (exact BFS cover extraction); α-theorem §6; β-calculus §8.5
---

# BC Signature — Forward Derivation (Operator Structure → Cover Geometry)

## Purpose

`bc_signature_extraction_observables.md` runs the chain **backwards**: from a
measured cover-height profile it *infers* the operator signature and BC class.
C2 (`Simulationen/sigma_validation_c1/C2_RESULT.md`) established that the genuine,
robust discriminators are five **cover-geometry** features — merge laterality,
ε_merge/span, merge asymmetry (ε_merge_L/ε_merge_R), h-asymmetry sign, and α — and
that the gradient/steepness column carries no independent BC information.

This document runs the chain **forwards**: it derives those five features
*analytically* from the operator structure of a generator, so that C2's empirical
6/6 identification table becomes a **corollary of the operator structure** rather
than an observed regularity. This is the forward half of open question Q-NEW-CROSS-2
("can the signature be computed analytically from operator structure?").

The forward chain:

```
generator (S-operator + sweep parameter)
   → canonical local form  O(κ) ~ f(κ − θ*)  near the regime boundary
       → discrete increment profile  g(δ) = |O'(θ* + δ)| · Δκ
           → cover combinatorics (which bonds heal, in which order)
               → the five cover-geometry discriminants
```

Step 1 (generator → functional form) is already tabulated in
`bc_operator_signatures_arw.md` and §4 of the observable-analysis skill. The new
content is the middle reduction and the four sub-maps below.

---

## 1. Reduction: the cover is a functional of the increment profile alone

On a uniform sweep grid (spacing Δκ) the observable O(κ_i) defines increments
g_i = O(κ_{i+1}) − O(κ_i). The ε-cover graph connects neighbours i, i+1 **iff**
|g_i| ≤ ε. Therefore the entire component structure at every resolution ε is fixed
by the **sorted multiset of increment magnitudes {|g_i|}**:

- a bond i "heals" (becomes an edge) exactly at ε = |g_i|;
- as ε grows, bonds heal in increasing order of |g_i|;
- the component containing θ* is the maximal contiguous run around θ* whose
  interior bonds are all ≤ ε.

For smooth O, g(δ) ≈ |O'(θ* + δ)| · Δκ. **Every cover-geometry discriminant is a
functional of this increment profile** — not of |O| values, and not of the
pointwise gradient as a σ_Δ proxy (cf. C1: the proxy is the *wrong* object for
stability; here |O'| enters only as the bond-ordering field, which is exact).

Operational definitions (from `sigma_extraction_*/03_signature_discrimination.py`,
restated as functionals of g):

- **cover height** h(κ) = Σ_ε (|C_ε(κ)| − 1): large where κ sits in big components
  across many ε-levels (flat regions), small where κ is isolated (steep surroundings).
- **w_h(ε)** = κ-span of the θ*-component.
- **ε_merge_{L,R}** = smallest ε for which the θ*-component extends past 50 % of the
  left / right sub-span; equivalently ε_merge_R = max increment over the inner half
  of the right wing, and symmetrically for L.
- **merge asymmetry** = ε_merge_L / ε_merge_R.
- **h-asymmetry** = (h_L − h_R)/(h_L + h_R), plateau means at ±0.3 around θ*.
- **α**: exponent of w_h(ε) ~ ε^α in the pre-merge regime [ε_lo, ε_merge/2].

---

## 2. Sub-map A — Merge laterality (one-sided vs bilateral)

A wing is **active** iff O varies on it (g ≠ 0 at the resolution scale). A flat wing
has g ≈ 0, so all its bonds heal at ε → 0⁺ — it is connected from the start and
contributes no structure to the growing θ*-component.

> **Rule A.** The merge is *one-sided* iff exactly one wing of θ* is active;
> *bilateral* iff both wings carry a non-vanishing increment profile.

Coupling is the canonical one-sided case: across a synchronisation transition one
phase is an essentially flat plateau (the ordered branch saturates, or the
disordered branch is flat at the resolution scale), so the cover grows from θ* into
the single active wing. All other five generators put structure on both sides of
θ* → bilateral.

---

## 3. Sub-map B — the α-theorem (the load-bearing result)

Let the local form be a power law O(κ) ~ |κ − θ*|^β, β > 0 (the generic regime-
boundary form; β is fixed by the operator structure — see §5). Then
g(δ) ≈ β |δ|^{β−1} Δκ, and the θ*-component half-width δ*(ε) solves g(δ*) = ε.

**Two regimes, decided by the sign of (β − 1):**

- **β > 1 — derivative *vanishes* at θ* (flat bottom).** Bonds are smallest at θ*
  and grow outward. δ*(ε) = (ε / (β Δκ))^{1/(β−1)}, so the span grows smoothly:
  ```
  w_h(ε) ∝ ε^{1/(β−1)}        ⟹   α = 1/(β − 1).
  ```
- **β < 1 — derivative *diverges* at θ* (cusp / vertical tangent).** The central
  bond at θ* is the *largest*; every outer bond is smaller. The component is pinned
  at the grid floor (w_h ≈ Δκ) until ε exceeds the central bond, then connects
  abruptly. In the pre-merge window w_h is floored ⟹ **α ≈ 0** (a sharp signature).
- **β = 1 — linear ramp.** Uniform bonds → degenerate step-like merge, α ≈ 0 /
  ill-defined.

> **Theorem (forward α).** For a power-law boundary form with exponent β,
> α = 1/(β − 1) when β > 1, and α ≈ 0 when β ≤ 1. Equivalently β = 1 + 1/α.

This is the analytic content behind C2's one residual ambiguity: **Aggregation and
Symmetry Breaking share the flat→ramp profile and are separable only by α.** The
theorem explains *why*: it is the difference between a derivative that **vanishes**
(smooth concave growth, β > 1, finite α) and one that **diverges** (square-root cusp
of a pitchfork, β = ½, α ≈ 0). The discriminant is not a fitted curiosity; it reads
off the order of contact of the observable with its regime boundary.

---

## 4. Sub-map C — h-asymmetry sign and merge asymmetry

**h-asymmetry sign.** h is large on the flatter wing (bigger components, earlier).
Hence

> **Rule C1.** sign(h-asym) = sign(flatness_L − flatness_R). h-asym > 0 ⟺ the left
> wing is flatter (flat→ramp profiles); h-asym < 0 ⟺ the right wing is flatter
> (ramp→flat, and the saturating-plateau side of a step).

**Merge asymmetry.** ε_merge_L/ε_merge_R is the ratio of the inner-half maximum
increments of the two wings. A symmetric feature gives ≈ 1 (a resonance bell); a
feature with one steep wall and one shallow wall gives a value far from 1.

> **Rule C2.** merge_asym ≈ 1 ⟺ symmetric bilateral feature (Forcing bell);
> merge_asym ≪ 1 or ≫ 1 ⟺ strongly unequal wing steepness (Restriction U-valley).

---

## 5. Instantiation — all six generators

β below is the order of contact of the canonical local form (from
`bc_operator_signatures_arw.md`); predictions follow from §2–§4. Measured values are
from `sigma_extraction_dfa/analysis/six_way_table.md`.

| Generator | canonical local O near θ* | β | laterality (A) | α = pred / meas | h-asym pred / meas | merge_asym meas |
|---|---|---|---|---|---|---|
| Coupling | step/sigmoid Θ(κ−κc), plateau one side | →∞ (step) | one-sided | ≈0 / 0.035 | <0 / −0.385 | — (one-sided) |
| Symmetry Breaking | pitchfork √: |κ−θ*|^{1/2} | 1/2 (cusp) | bilateral (flat→ramp) | ≈0 / −0.000 | >0 / +0.097 | 0.055 |
| Aggregation | concave growth |κ−θ*|^β | ≈1.55 | bilateral (flat→ramp) | 1.8 / 1.82 | >0 / +0.360 | 0.26 |
| Dissipation | relaxation amplitude, ramp→flat | ≈2 (ramp) | bilateral (ramp→flat) | (1) / — | <0 / −0.385 | 0.18 |
| Restriction | projection U-valley | ≈2 walls | bilateral | (1) / — | sym / — | 0.02 |
| Forcing | resonance bell A(Ω), peak | ≈2 (peak) | bilateral | (1) / — | ≈0 / **−0.30** | 0.92 |

**Back-solving β from measured α confirms the theorem:** Aggregation α = 1.82 ⟹
β = 1 + 1/1.82 = 1.55 (smooth concave); Symmetry Breaking α ≈ 0 ⟹ cusp (β = ½ of the
pitchfork). The two flat→ramp generators are thus separated by the order of contact,
exactly as Rule B predicts.

---

## 6. Numerical verification of the keystone

The exact BFS cover extraction (identical to the pipeline) on synthetic
O = |κ − θ*|^β over a 201-point grid:

| β | predicted α = 1/(β−1) | measured α |
|---|---|---|
| 0.50 | — (cusp) | 0.000 |
| 0.75 | — (cusp) | 0.000 |
| 1.50 | 2.000 | 1.967 |
| 2.00 | 1.000 | 1.025 |
| 3.00 | 0.500 | 0.502 |

The forward α-map reproduces the cover exponent to within grid resolution for β > 1
and collapses to the sharp α ≈ 0 signature for the cusp (β < 1). Script:
`Simulationen/` (forward-map verification, 2026-06-03).

---

## 7. What is derived, and what remains open

**Derived (forward, from operator structure):**
- merge laterality (Rule A) — one-sided for Coupling, bilateral otherwise;
- the α-discriminant as α = 1/(β−1) / ≈0, including the Aggregation↔Symmetry-Breaking
  split (Rule B, numerically confirmed);
- h-asymmetry sign from wing flatness (Rule C1);
- merge-asymmetry from wing-steepness ratio (Rule C2).

**Open / to tighten:**
- **Forcing h-asymmetry mismatch.** Rule C1 predicts h-asym ≈ 0 for a symmetric
  bell, but the measured S0 value is −0.30. The likely cause is that the bell peak
  sits near a sweep boundary (max-at-boundary), so the in-window flanks are unequal.
  Either the canonical form must carry the boundary position, or S0 must be re-run
  with the peak centred. (Flagged, not yet resolved.)
- **One-sided α.** For a flat wing the pre-merge fit window collapses (full span is
  reached at tiny ε); α is then ill-defined, consistent with Coupling α ≈ 0. A
  dedicated active-wing fit is needed if α is wanted for one-sided cases.
- **Forward ε_merge magnitude.** Laterality and the ratio are derived; the absolute
  ε_merge/span (which separates Forcing as "high") still needs an analytic estimate
  from the inner-half max increment, not just its ratio.
- **From β to the operator.** §5 took β from the canonical-form catalogue. §8 now
  derives β itself from the S1–S5 operator composition via an exponent calculus
  (two rules numerically verified). What remains is fixing the *base* exponent q for
  the harder generators (Dissipation, Restriction) from first principles rather than
  by inspection of the canonical form.
- **Multi-generator composition.** Whether signatures of co-active generators
  (C+D in noisy Kuramoto, the four classes of CASE-0010) superpose separably in
  these coordinates is the decisive test of the generator idea and is untouched here.
  Note (C2 cont.): the current Σ-extraction must first be made ε-resolved and
  scale-normalised before composition is testable — see `C2_RESULT.md`.

---

## 8. β from operator composition (the exponent calculus)

§3 reduced the cover discriminant α to the order of contact β; §5 still *read* β off
the canonical form. This section derives β itself from the operator chain, closing the
forward direction of Q-NEW-CROSS-2. The claim: **β is built by an exponent calculus in
which each S-operator acts on the order of contact in a fixed way.**

### 8.1 Base exponent q (the generator's defining operator near θ*)

The sweep parameter enters as a control u = κ − θ*. The BC generator's *defining*
operator fixes the bare exponent q of the primitive response m(u) ~ u^q:

| Generator | defining operator | mechanism near θ* | base q |
|---|---|---|---|
| Symmetry Breaking | S1 selection under parameter variation (degeneracy lifting) | pitchfork normal form, m ~ u^{1/2} | 1/2 (cusp) |
| Coupling | S2 product∘composition (mean-field self-consistency) | synchronisation onset r ~ u^{1/2}, flat sub-critical branch | 1/2 (cusp), one-sided |
| Restriction | S1 hard projection / admissibility edge | kink at a constraint (q=1) or smooth constrained extremum (q=2) | 1–2 |
| Forcing | S3 time-coupled resonance | Lorentzian/quadratic peak, m ~ m_max − c·u² | 2 |
| Dissipation | S4 contraction / logistic saturation | smooth ramp→flat shoulder (Verhulst) | ≈2 |

### 8.2 Operator actions on the exponent (verified rules)

- **S5 aggregation / expectation over an in-κ threshold spread:** **β ← β_unit + 1.**
  O(κ) = ∫ m(κ−ξ) ρ(ξ) dξ; the cumulative integral over a heterogeneity density whose
  support spans the transition adds exactly one power. *Conditional on heterogeneity:*
  if the spread σ → 0 (identical units) the lift vanishes and the transition re-sharpens
  to the bare cusp — a falsifiable prediction (Aggregation's α should track the
  heterogeneity width). Verified: unit q ∈ {0, ½, 1} → within-spread β = {1.00, 1.49,
  1.99} ≈ {q+1}; far-field returns to q.
- **Moment / norm observable** (variance = 2nd moment, |·|², squared amplitude):
  **β ← 2·β.** Verified exactly: m ~ u^{0.5,1,1.5} → O = m² gives β = {1.0, 2.0, 3.0}.
- **Smooth invertible composition ∘** (monotone reparametrisation, log of a quantity
  bounded away from 0): preserves the leading exponent (chain rule).
- **S4 / S1 onto a diverging quantity** (rate or relaxation-time observable at a
  critical attractor change): critical slowing gives a *negative/divergent* exponent —
  the cusp/Z_shared regime governed by C1's σ_Δ machinery, not a smooth β.

### 8.3 Per-generator composition → β → α

| Generator | composition | β | α = 1/(β−1) | measured α |
|---|---|---|---|---|
| Symmetry Breaking | q=½, no aggregation, linear observable | 1/2 (cusp) | ≈0 | −0.000 (Q0) |
| Coupling | q=½, r_ss=\|E[e^{iθ}]\| (mean, no in-κ smoothing) | 1/2 (cusp) | ≈0, one-sided | 0.035 (K0) |
| **Aggregation** | **cusp q=½ + S5 lift (+1)** | **3/2** | **2.0** | **1.82 (T0)** |
| Forcing | q=2 quadratic peak | 2 | 1 | (bilateral, sym) |
| Dissipation | q≈2 smooth ramp→flat | ≈2 | ≈1 | (h_asym<0) |
| Restriction | q=2 smooth U-valley (or q=1 hard edge) | 1–2 | 0.5–1 | (separatrix special) |

The headline is **Aggregation**: its β ≈ 1.55 (measured) is not a free parameter but
the bare synchronisation/onset cusp (q = ½) **lifted by exactly +1 by the aggregation
operator S5**. This is why Aggregation and Symmetry Breaking — identical flat→ramp
profiles, identical bare exponent ½ — separate by α: only Aggregation carries the S5
lift. The discriminant that C2 found empirically is generated by the presence or
absence of one operator in the chain.

### 8.4 The subtlety that keeps this honest

S5 appears in *both* Coupling (forming r_ss = |E[e^{iθ}]|) and Aggregation, yet only
Aggregation gets the +1 lift. The distinction: the lift requires expectation **over a
distribution of unit-level thresholds spread along the sweep axis** (frequency spread,
parameter heterogeneity). Coupling's expectation builds an order parameter *at fixed κ*
— it does not convolve the transition in κ, so no lift. Operationally: the +1 is
present iff the aggregation integrates over heterogeneity that the sweep parameter
resolves. This makes the rule conditional and testable, not a blanket "S5 ⇒ +1".

### 8.5 Verification

`Simulationen/signature_forward_map/verify_beta.py` (Rule 1, Rule 2 above) and
`verify_alpha.py` (β → α). The two scripts together exercise the full chain
operator → β → α on synthetic observables with the exact BFS cover extraction.

---

## Relation to existing docs

- `bc_signature_extraction_observables.md` — the **inverse** (measured cover → BC class).
  This doc is its forward complement and uses the same operational definitions.
- `observable_space_cover_height.md` — defines h(b_i); §1 here restates it as a
  functional of the increment profile.
- `bc_operator_signatures_arw.md` / `operator_signature_catalog.md` — supply the
  canonical local forms (β) consumed in §5.
- `cover_stability_criterion.md` / C1 — clarifies that |O'| enters here only as the
  exact bond-ordering field, **not** as a σ_Δ proxy (which C1 showed is biased at θ*).
