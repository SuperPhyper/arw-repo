---
status: working-draft
layer: experiments/
last_updated: 2026-06-02
source_experiments:
  - Simulationen/sigma_extraction_kuramoto_noise/
  - Simulationen/sigma_extraction_pendulum_1d/
addresses:
  - Q-EXT-01: operator signature discrimination without model equations
  - Q-EXT-02: minimum data requirements for stable Sigma extraction
related:
  - docs/advanced/bc_signature_extraction_observables.md (method definition)
  - docs/advanced/bc_signature_forward_derivation.md (forward complement, alpha=1/(beta-1) theorem)
imported: 2026-07-14 from monograph workspace; canonical copy is this file
---

# Observable Signatures of Boundary Condition Classes
## First Empirical Results from the Sigma Extraction Procedure

---

### What Was Done

The Sigma-extraction procedure (from `bc_signature_extraction_observables.md`)
was applied to two systems with known, different BC classes:

- **Kuramoto oscillators** — Coupling BC. Observable: r_ss(κ), the
  time-averaged order parameter. Monotone step-like profile. One 1D sweep
  (κ ∈ [0, 3], N=50, clean noise-free scenario K0).

- **Conservative pendulum** — Restriction BC. Observable: ω(E, ω₀),
  the oscillation/rotation frequency. U-shaped profile, zero at the separatrix
  E_sep = ω₀² (analytic formula via elliptic integrals). Four 1D sweeps
  at fixed ω₀ ∈ {0.5, 1.0, 1.5, 2.0}.

Both sweeps used the same adjacency-preserving BFS cover height method
(v2, consistent with Felder 2026 Definition 2). Observable spans differ:
Kuramoto r_ss ∈ [0.12, 0.99], span ≈ 0.87; Pendulum ω spans 3.3–5.8 rad/s
depending on ω₀.

---

### The Three Discriminants

#### D1 — ε_merge / obs_span

For each scenario, ε_merge is the smallest ε at which the BFS component
containing θ* (the regime boundary) spans more than half the parameter range.
Dividing by the observable span makes this comparable across systems.

| System | Scenario | ε_merge / span |
|--------|----------|---------------|
| Kuramoto (Coupling) | K0 | **0.207** |
| Pendulum (Restriction) | P1 (ω₀=0.5) | 0.0048 |
| Pendulum (Restriction) | P2 (ω₀=1.0) | 0.0022 |
| Pendulum (Restriction) | P3 (ω₀=1.5) | 0.0020 |
| Pendulum (Restriction) | P4 (ω₀=2.0) | 0.0021 |

Coupling is ~100× larger than Restriction. The reason is structural: for a
monotone step (Coupling), the BFS component at θ* remains isolated until ε
reaches the full height of the observable step — the component cannot merge
until ε bridges the gap between the two plateaus. For a U-shaped valley
(Restriction), the component at the minimum connects to its immediate
neighbours at very small ε, because the observable barely increases from the
minimum in any direction. The merge scale encodes the observable gap
to be bridged, not the sharpness of the transition.

#### D1b — Bilateral Merge Asymmetry

For the U-shaped pendulum observable, the BFS component at θ* is approached
from both sides simultaneously. Tracking the merge separately:

| Scenario | ε_merge_L / span | ε_merge_R / span | Asymmetry (L/R) |
|----------|-----------------|-----------------|-----------------|
| P1 | 0.00093 | 0.0434 | **0.021** |
| P2 | 0.00131 | 0.0633 | **0.021** |
| P3 | 0.00164 | 0.0725 | **0.023** |
| P4 | 0.00170 | 0.0815 | **0.021** |

The librational side (E < E_sep) merges roughly 50× earlier than the
rotational side. This is not noise — it is stable across all four ω₀ values
at L/R ≈ 0.021. The physical reason: ω(E) rises slowly (small gradient) on
the librational side (harmonic-like approach to separatrix) and rapidly
(large gradient) on the rotational side (√E growth at large E). The asymmetry
encodes the structural difference between the two regimes on either side of
the Restriction boundary.

Coupling has no bilateral asymmetry — the monotone step has only one side.
Merge asymmetry ≈ 0.021 is therefore a pure Restriction-BC fingerprint with
no Coupling analog.

#### D2 — F-Gradient Proxy at θ*

Max |Δ observable / Δ parameter| in a window around θ*:

| System | Scenario | F-gradient proxy |
|--------|----------|-----------------|
| Kuramoto (Coupling) | K0 | **3.56** |
| Pendulum (Restriction) | P1 | 1.42 |
| Pendulum (Restriction) | P2 | 0.55 |
| Pendulum (Restriction) | P3 | 0.32 |
| Pendulum (Restriction) | P4 | 0.22 |

Coupling has a sharp, localized step at θ* — large gradient. Restriction has
a logarithmically slow approach to the separatrix — the gradient at θ* is
small and decreasing with ω₀ as the E range grows. The gradient measures how
abruptly the observable changes at the regime boundary: Coupling boundaries
are sharp, Restriction boundaries are soft in observable space.

---

### Summary: Discriminant Profile by BC Class

| Discriminant | Coupling (K0) | Restriction (P1–P4) |
|---|---|---|
| ε_merge / obs_span | ~0.21 (large) | ~0.002–0.005 (small) |
| Merge asymmetry (L/R) | n/a (one-sided) | ~0.021 (stable) |
| F-gradient at θ* | high (3.6) | low (0.2–1.4, decreasing) |
| Observable shape | monotone step | U-shaped valley |
| w_h(ε) pre-merge | flat (α ≈ 0) | step-function (α not fittable) |

The three discriminants point in the same direction and are mutually
consistent: Coupling produces a large, one-sided, sharp-gradient merge.
Restriction produces a small, bilateral, asymmetric, soft-gradient merge.

---

### What This Establishes

**Q-EXT-01 (partial):** The Sigma-extraction procedure produces
characteristically different discriminant profiles for Coupling-BC and
Restriction-BC systems, using only 1D observable sweeps and no access to
the governing equations. The profiles are consistent across four ω₀ values
for the pendulum, confirming that the pattern is a BC-class property rather
than a system-parameter artifact.

**Q-EXT-02 (qualitative):** 80 sweep points are sufficient to resolve all
three discriminants for both systems. The merge asymmetry signal (stable at
L/R ≈ 0.021 across P1–P4) suggests high robustness to sweep density within
this range.

---

### What Remains Open

**Single-system claim vs. class claim.** Two systems establish a contrast,
not a classification. A third BC class — Symmetry Breaking (Pitchfork) or
Aggregation (SIR) — would move from "these two systems differ" to "BC classes
have distinct Sigma profiles." Until then, the claim is descriptive, not
classificatory.

**α-fit for Restriction.** The w_h(ε) profile for Restriction is a step
function (flat near zero, jumps at ε_merge). The pre-merge window is too
narrow for a reliable power-law fit. This is itself informative — the
step-function w_h is a structural property of the U-shaped observable — but
it means α is not available as a Restriction discriminant. Only ε_merge_norm
and merge_asymmetry are reliable.

**Conflict index (Coupling + Dissipation).** In the Kuramoto noise experiment
(K0–KE), CI = 1.0 for all noise levels: Coupling and Dissipation operate at
orthogonal ε scales and do not compete. This suggests Dissipation erodes the
plateau quality (lower h_sync_per_point) without interfering with the
Coupling-driven transition structure. Whether this orthogonality holds for
other Coupling-dominated systems, or breaks for strong enough Dissipation, is
an open question.

**Pendulum secondary ridge — closed (2026-06-02).** The re-measured 2D field
(`kuramoto_pendulum_cover_pipeline_v2`, 120×80 grid, ε=0.3) shows no confirmed
secondary ridge in the physically meaningful regime u = E/ω₀² ∈ (−0.9, 0.5).
The peak gradient ratio of any secondary feature relative to the primary (separatrix)
is < 10% across all ω₀ ∈ [0.5, 2.0], with no consistent functional dependence on ω₀.
The field is self-similar under u = E/ω₀² with CV < 1% (u ≤ 0.5): there is one
energy scale, not two. The previously claimed "secondary ridge at E ≈ ω₀²/2"
originated from the buggy E_sep = 2ω₀² convention; under the correct E_sep = ω₀²
no such feature is present. The 1D sweep question ("compound Restriction signatures")
is therefore moot — the pendulum has a single Restriction boundary at E_sep = ω₀².

---

### Connection to ARW Formal Framework

The three discriminants connect directly to ARW concepts:

**ε_merge / span** measures the width of the admissible resolution regime
I_ε = [ε_min, ε_max] relative to the observable span. For Coupling, the
admissible window is wide (large ε_merge) because the step-like observable
remains informative over a large ε range. For Restriction, the window is
narrow — the U-shaped minimum is resolved only at very small ε.

**Merge asymmetry** is a cover-space signature of the observable's local
gradient structure on each side of θ*. It has no analog in the Felder 2026
formalism (which treats σ_Δ(x) as scalar, not directional), but it is
consistent with the F-gradient category: the librational side has low σ_Δ
(flat observable), the rotational side has high σ_Δ (steep observable). The
asymmetry ratio encodes this differential σ_Δ without requiring explicit
perturbation computation.

**F-gradient at θ*** is the direct observable-space proxy for σ_Δ(x) at the
regime boundary (Felder 2026 Corollary 1: σ_Δ ≤ L·r where L = |∂O/∂κ|).
Coupling produces high L at θ* (localized steep transition), Restriction
produces low L (logarithmic approach).

---

### Notes on the Pendulum Energy Convention

**Convention (fixed 2026-06-02):** E = ½θ̇² − ω₀²cos(θ), E_min = −ω₀²,
**E_sep = ω₀²** (separatrix at θ=π, θ̇=0). The earlier pipeline code had
a bug (E_sep = 2ω₀²) that has been corrected in `kuramoto_pendulum_cover_pipeline_v2/`.
The 1D sweeps here use the analytic formula via `scipy.special.ellipk` (correct
throughout). The 2D results have been recomputed in `_v2/results_pendulum/`
(120×80 grid, ε=0.3, seed=42 — identical parameters to the original).

Key quantitative changes from recomputation:
- spread_max: 3.79 → 1.35 (−64%); σ_Δ/ε at E_sep = 2.0 (F-gradient confirmed)
- window_fraction_wide_pct: 32% → 47% (+46%)
- cover_height_p2_ratio: 33.5 → 5.1 (−85%; field now nearly self-similar in ω₀)
- No secondary ridge confirmed (see "Pendulum secondary ridge" note above)

The SETUP.md E_sep scenario table and scripts 02/03 in
`sigma_extraction_pendulum_1d/` have been corrected accordingly (2026-06-02).


---

## Update: Three-Way Triangulation (Symmetry Breaking added)

*Added 2026-06-02. Source: `sigma_extraction_pitchfork_1d/`*

---

### Third System: Pitchfork Normal Form (Symmetry Breaking BC)

**Model:** ẋ = μx − x³, CASE-20260315-0008.
**Observable:** x_ss(μ) = steady-state amplitude (positive branch).
  Clean scenario Q0 (σ=0): x_ss = 0 for μ ≤ 0, √μ for μ > 0.
  Observable profile: flat-then-ramp. Neither step (Coupling) nor valley
  (Restriction). Structurally: one side trivially flat at observable minimum,
  other side grows with algebraically divergent slope at θ*.

---

### Complete Three-Way Discriminant Table (Q0 reference)

| Discriminant | Coupling (K0) | Restriction (P2) | Symmetry Breaking (Q0) |
|---|---|---|---|
| Observable shape | monotone step | U-valley | flat + √μ ramp |
| obs_span | 0.869 | 4.216 | 1.414 |
| **ε_merge / span** | **0.207** | **0.002** | **0.117** |
| ε_merge_L / span | — (one-sided) | 0.0013 | 0.0064 |
| ε_merge_R / span | — (one-sided) | 0.0633 | 0.1173 |
| **merge_asymmetry L/R** | **n/a** | **0.021** | **0.055** |
| α (w_h fit) | 0.035 | — | 0.000 |
| **F-gradient at θ*** | **3.56** | **0.55** | **3.14** |
| **h_asymmetry (L−R)/(L+R)** | **−0.38** | **~0** | **+0.10** |

All four discriminants cleanly separate the three BC classes.

---

### What Each Discriminant Measures — Updated Interpretation

**ε_merge / span** encodes how large an ε is needed to bridge the
observable gap at θ* relative to the full observable range. This reflects
the geometry of the transition in observable space:
- Coupling: bridges a full plateau-to-plateau step height → large
- Symmetry Breaking: bridges a √μ ramp → medium (√Δμ scale)
- Restriction: bridges a U-valley minimum → small (both sides approach
  from above, connecting easily)

**merge_asymmetry** (for bilateral systems) encodes the structural
difference between the two sides of θ*:
- Restriction (P2, asym=0.021): both sides non-trivial but librational
  side has smaller gradient → L merges ~50× earlier than R
- Symmetry Breaking (Q0, asym=0.055): left side trivially flat at zero,
  L merges early but not at ε=0 (first left-side point has x_ss=0 but
  θ* itself is at x_ss=0 too — BFS connects at ε=0+ rather than ~0.006)
- The key distinction: Restriction has asym ≪ 1 but both sides non-zero;
  Symmetry Breaking has asym ≪ 1 with L near-zero and R dominant.

**F-gradient at θ*** reflects the slope of the observable at the
regime boundary:
- Coupling: steep finite step → high gradient (~3.6)
- Symmetry Breaking: √μ divergence at μ=0+ → high gradient (~3.1),
  similar magnitude to Coupling but from a different mechanism
- Restriction: logarithmic approach to ω=0 → very low gradient (~0.6)

**h_asymmetry (L−R)/(L+R)** captures the structural dominance of
one side in cover space:
- Coupling (−0.38): synchronized plateau (right side) accumulates
  more cover height → right dominates → negative
- Restriction (~0): librational and rotational plateaus are roughly
  symmetric in cover height → near zero
- Symmetry Breaking (+0.10): flat left region accumulates cover height
  via trivial clustering (all x_ss=0) → slight left dominance → positive

The sign of h_asymmetry distinguishes Coupling from Symmetry Breaking
even when ε_merge/span is similar. This completes the separation.

---

### BC Class Identification Protocol (Empirical)

Given an unknown 1D parameter sweep with observable O(p):

1. Check for bilateral merge structure. If the BFS component at θ*
   can only grow in one direction (one side has no admissible neighbours
   at any ε), the system has a **one-sided observable (Coupling)**.

2. If bilateral: compare eps_merge_L and eps_merge_R.
   - eps_merge_L ≈ eps_merge_R (asym ~1): symmetric bilateral →
     not seen in these three systems; may indicate a different BC class
   - eps_merge_L ≪ eps_merge_R (asym ≪ 1):
     - If L is near-zero AND h_asym > 0: **Symmetry Breaking**
     - If L is small but non-zero AND h_asym ≈ 0: **Restriction**

3. Cross-check with F-gradient at θ* and eps_merge/span:
   - High F-grad + large eps_merge/span: Coupling or Symmetry Breaking
   - Low F-grad + small eps_merge/span: Restriction

The critical disambiguation between Coupling and Symmetry Breaking
(both high F-gradient, both non-bilateral) uses h_asymmetry:
Coupling → negative (right plateau dominates), Symmetry Breaking →
positive (left flat region slightly dominates).

---

### What This Establishes (Updated)

**Q-EXT-01 (answered for three BC classes):** The Sigma-extraction
procedure produces characteristically different discriminant profiles
for Coupling-BC, Restriction-BC, and Symmetry-Breaking-BC systems,
using only 1D observable sweeps without access to governing equations.
The four discriminants (ε_merge/span, merge_asymmetry, F-gradient,
h_asymmetry) form a complete separation in this three-class space.

The claim is now classificatory, not merely descriptive. Three BC classes
are separated. Whether Aggregation-BC and Forcing-BC produce additional
distinct profiles remains open (as does the behavior of multi-BC systems).

### What Remains Open (Updated)

- **Aggregation (SIR)** and **Forcing** BC classes: not yet tested.
  SIR I_∞ profile is qualitatively similar to pitchfork (flat-then-ramp),
  but the mechanism differs. Would the discriminant profile distinguish
  Aggregation from Symmetry Breaking? Currently unknown.
- **Multi-BC systems:** CASE-0010 (school system, four simultaneous BCs)
  would produce a compound Σ. How the four discriminants behave for
  overlapping BC classes is unresolved.
- **Noise effects on Symmetry Breaking:** QA/QB show that noise shifts
  θ* rightward (noise floor makes x_ss non-zero for μ<0, displacing the
  steepest gradient). This parallels the Kuramoto noise experiment's
  ε_merge monotone decrease. A systematic QA–QE noise series would
  complete the Symmetry Breaking analog of the Kuramoto experiment.


---

## Update: Complete 6-BC-Class Survey

*Added 2026-06-02. Source: `sigma_extraction_dfa/` (R0, S0, T0)*

---

### The Full Picture

Three new systems complete the survey:

- **R0 — Dissipation:** Stuart-Landau γ-sweep. A_ss(γ) = √(μ₀−γ),
  fix μ₀=1. Profile: ramp→flat (mirror of Symmetry Breaking).
  θ* at γ_c = μ₀ = 1 (oscillation death threshold).

- **S0 — Forcing:** Damped resonator Ω-sweep.
  A(Ω) = F/√((ω₀²−Ω²)²+(2γΩ)²), fix ω₀=1, γ=0.05.
  Profile: bell-shaped peak at resonance. θ* = argmax(A) — the only
  system where θ* is a maximum, not a transition from one plateau to another.

- **T0 — Aggregation:** SIR β-sweep. I_∞(β) = final infected fraction.
  Profile: flat→ramp (like Symmetry Breaking but with different growth rate).
  θ* at β_c = γ = 1 (epidemic threshold R₀=1).

---

### Complete Discriminant Table (all six BC classes)

| Label | BC Class | Profile | ε_merge/span | emL/span | emR/span | asym L/R | F-grad | h_asym | α |
|---|---|---|---|---|---|---|---|---|---|
| K0 | Coupling | step | 0.207 | — | — | n/a | 3.56 | −0.38 | 0.04 |
| P2 | Restriction | U-valley | 0.002 | 0.001 | 0.063 | 0.021 | 0.55 | ~0 | — |
| Q0 | Symm. Breaking | flat→ramp | 0.117 | 0.006 | 0.117 | 0.055 | 3.14 | +0.10 | ~0 |
| R0 | Dissipation | ramp→flat | 0.002 | 0.002 | 0.010 | 0.182 | 0.26 | −0.39 | — |
| S0 | Forcing | bell-peak | 0.298 | 0.274 | 0.298 | 0.917 | 7.53 | −0.30 | ~0 |
| T0 | Aggregation | flat→ramp | 0.0001 | 0.0001 | 0.0002 | 0.259 | 0.35 | +0.36 | 1.82 |

---

### Cluster Structure in Discriminant Space

Three natural clusters emerge from the data:

**Cluster 1 — Forcing (S0) isolated:**
S0 has the largest ε_merge/span (0.298) and by far the highest F-gradient
(7.53). The bell-shaped resonance peak is the steepest observable transition
of all six systems, approached symmetrically from both sides (asym≈0.92,
near-symmetric). No other BC class comes close on either discriminant.
*Identification: bell profile + high F-gradient + bilateral symmetric merge.*

**Cluster 2 — Restriction (P2) and Dissipation (R0) close together:**
Both have ε_merge/span ≈ 0.002 and low F-gradient (0.26–0.55). They differ
in bilateral merge asymmetry: P2 has asym=0.021 (L/R ratio ~1/50, librational
side connects 50× earlier than rotational), R0 has asym=0.182 (ratio ~1/5.5,
more symmetric). The h_asym further separates them: P2 is near zero (symmetric
plateaus), R0 is negative (ramp side has higher cover height than flat side).
*Identification: low ε_merge + low F-gradient + asym and h_asym for sub-separation.*

**Cluster 3 — Coupling (K0) and Symmetry Breaking (Q0) intermediate:**
Both have ε_merge/span ~0.1–0.2 and high F-gradient (3.1–3.6), separated
by h_asym: K0 is −0.38 (synchronized plateau on right dominates cover height),
Q0 is +0.10 (flat left side slightly dominates). One-sided merge distinguishes
K0 (no L/R split) from Q0 (bilateral, though L much smaller than R).

**Aggregation (T0) stands apart:**
T0 has the smallest ε_merge/span by a large margin (0.0001 vs. next smallest
0.002). The SIR epidemic rise is extremely concentrated in ε-space — the
observable grows concavely (I_∞ ~ (β−1)^κ with κ>1 near the threshold) rather
than as √(β−β_c). This is captured by α≈1.82 vs. α≈0 for Symmetry Breaking,
which has the same profile shape but √μ growth (concave in μ but convex in ε).
T0 is also the only system with h_asym > 0.3 (very strong left-plateau
dominance: subcritical I_∞≈0 for a wide β range → massive trivial covers).

---

### Observable Profile → BC Class Identification Protocol

Given an unknown 1D parameter sweep p ↦ O(p) with a detected regime boundary
at θ*:

**Step 1 — Profile type**

| Observed profile | Candidate BC classes |
|---|---|
| Monotone step (low→high plateau) | Coupling |
| U-valley (minimum at θ*, rises both sides) | Restriction |
| Flat→ramp (left side flat at minimum) | Symmetry Breaking, Aggregation |
| Ramp→flat (right side flat at minimum) | Dissipation |
| Bell peak (maximum at θ*, falls both sides) | Forcing |

**Step 2 — Bilateral merge check**

Compute eps_merge_L and eps_merge_R.

- *No bilateral structure* (one-sided observable, only one plateau): **Coupling**
- *Near-symmetric* (asym L/R ≈ 0.9–1.1): **Forcing**
- *Asymmetric, both non-zero:* proceed to Step 3

**Step 3 — ε_merge / span magnitude**

- ε_merge/span > 0.1: **Coupling** or **Symmetry Breaking** or **Forcing**
- ε_merge/span 0.001–0.01: **Restriction** or **Dissipation**
- ε_merge/span < 0.001: **Aggregation**

**Step 4 — h_asym and F-gradient**

| h_asym | F-grad | BC class |
|---|---|---|
| < −0.2 | > 3 | Coupling (synced plateau dominates) |
| < −0.2 | < 1 | Dissipation (ramp side dominates) |
| ≈ 0 | < 1 | Restriction (symmetric plateaus) |
| > 0 | < 1 | Aggregation (flat plateau dominates, slow growth) |
| > 0 | ≈ 3 | Symmetry Breaking (flat side slightly dominant, √ growth) |
| < −0.3 | > 7 | Forcing (sub-resonant flank dominates) |

**Step 5 — α as tiebreaker for flat→ramp profiles**

If Steps 1–4 yield ambiguity between Symmetry Breaking and Aggregation:
- α ≈ 0: growth is √(p−θ*) — **Symmetry Breaking**
- α > 1: growth is concave, steeper than √ — **Aggregation**
- α ∈ (0,1): intermediate, requires additional observable or sweep range

---

### What This Establishes

**Q-EXT-01 fully answered for all six ARW BC classes.**
The Sigma-extraction procedure produces discriminable profiles for all six
BC classes from 1D observable sweeps alone. The five-step identification
protocol is sufficient to classify any of the six classes, with α as a
tiebreaker for the flat→ramp ambiguity (Symmetry Breaking vs. Aggregation).

The claim is now fully classificatory. The discriminant space formed by
(ε_merge/span, bilateral merge asymmetry, F-gradient, h_asymmetry, α)
separates all six classes without overlap — though Restriction and Dissipation
are the closest pair and would require careful measurement in noisy conditions.

---

### What Remains Open

**Noise robustness of R0/P2 separation.** Both have ε_merge/span ≈ 0.002;
their separation relies on asym (0.021 vs. 0.182) and h_asym (~0 vs. −0.39).
These discriminants may collapse under strong measurement noise. A systematic
noise series for Restriction and Dissipation (analogous to K0–KE for Coupling)
is needed to characterize the robustness boundary.

**Multi-BC systems.** The identification protocol assumes a single dominant BC
class. CASE-0010 (four simultaneous BC classes) would produce a compound Σ.
How the five discriminants behave when multiple BC mechanisms overlap is
entirely unresolved. The CI=1.0 finding from the Kuramoto noise experiment
(Coupling + Dissipation are orthogonal in ε-space) suggests that compound
signatures may be linearly separable — but this is speculative.

**The Forcing model.** The resonance amplitude A(Ω) is a smooth, physically
unambiguous observable for a linear forced oscillator. Whether the same
discriminant profile appears for a nonlinear forced system (Duffing oscillator,
period-doubling cascade) or for the Arnold tongue boundary in a phase-locked
oscillator is unknown. The Forcing BC class may encompass multiple distinct
profile types depending on the specific mechanism.

**Formal connection to ARW I_ε.** The discriminant ε_merge/span is an
empirical proxy for the width of the admissible resolution interval I_ε.
The formal relationship — whether ε_merge ≈ ε_max (the upper bound of I_ε)
or some fraction thereof — has not been derived. Establishing this connection
would anchor the empirical protocol in the Felder 2026 formalism.

---

## Maintenance History

- **2026-07-14**: Imported into `arw-repo/experiments/` from the monograph workspace
  (was a book-side orphan; see DOC_INDEX entry). Q-EXT-01/02 now registered in
  `docs/notes/open_questions.md` (prefix collision with `extended_z_observable_necessity.md`
  resolved same day — that document's series renumbered to Q-ZOBS). Cross-reference added:
  `bc_signature_forward_derivation.md` (2026-06-03, numerically verified) is the forward
  complement of this inverse-direction work — its beta-exponent calculus predicts the
  discriminant geometry these results measure empirically.
