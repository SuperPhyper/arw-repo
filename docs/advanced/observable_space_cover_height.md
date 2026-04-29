---
status: working-definition
layer: docs/advanced/
last_updated: 2026-04-29
depends_on:
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
  - docs/advanced/epsilon_and_scope_resolution.md
---

# Observable-Space Cover Height

## Overview

Observable-space cover height is a method for probing scope granularity
across all resolution scales simultaneously, without committing to a single ε.

It was introduced to address two limitations of the standard ARW ε-sweep:

1. The ε-sweep requires a fixed ε as input and returns a partition at that scale.
   It does not reveal which ε values are informative without testing them one by one.
2. BC-space interval covers on uniform grids carry no structural information
   (see Finding 2, session 2026-03-27).

The method constructs covers in **observable space** rather than BC space,
then maps the resulting height field back to (BC₁, BC₂, ...) coordinates.

---

## Construction

Given a sweep of N simulation points with BC coordinates b_i and
observable values π(b_i):

**Step 1 — Sort by observable value.**
Order all points by π(b_i): π(b_{(1)}) ≤ π(b_{(2)}) ≤ ... ≤ π(b_{(N)}).

**Step 2 — Define epsilon range.**
Estimate Δπ = median positive step in the sorted sequence.
Set ε ∈ [Δπ/10, π_span] log-spaced (recommended: 200 steps).
This spans from sub-resolution to the full observable range.

**Step 3 — Build maximal interval covers.**
For each ε: group consecutive sorted points into maximal intervals.
Points i and i+1 belong to the same interval iff:

```
|π(b_{(i+1)}) − π(b_{(i)})| ≤ ε
```

This is a contiguous grouping, not a ball cover — transitivity is not applied.
A cover breaks wherever a gap > ε occurs in the sorted sequence.

**Step 4 — Accumulate weighted height.**
For each point b_i, accumulate across all covers C containing b_i and
all ε levels:

```
h(b_i) = Σ_{ε} Σ_{C ∋ b_i} (|C| − 1)
```

where |C| is the number of members in cover C.
The weight (|C| − 1) is zero for isolated points and grows with cover size.

**Step 5 — Map back to BC space.**
Plot h(b_i) as a function of the BC coordinates (κ, σ, ...).

---

## Interpretation

### High h(b_i)
Point b_i lies in dense regions of observable space at many ε scales.
Many neighboring BC points produce similar observable values.
Interpretation: b_i is deep inside a stable regime —
the scope is insensitive to BC perturbations of size Δb at this location.

### Low h(b_i)
Point b_i is isolated in observable space — few neighbors within ε
across most ε scales.
Interpretation: b_i is near a regime transition —
the observable changes steeply with BC, covers are small.

### Contour lines of h
Contour lines of h in (κ, σ) space run parallel to the regime boundary.
h encodes **distance from the transition** (depth inside a regime),
not regime identity.

---

## Relationship to ARW ε-Sweep

The standard ε-sweep fixes ε and counts regimes N(ε), looking for a stable
plateau N* over an interval [ε_lo, ε_hi].

Observable-space cover height is the **integral of the partition signal over all ε**:

```
h(b_i) ≈ ∫ w(b_i, ε) dε
```

where w(b_i, ε) is the weight contributed at resolution ε.

This makes ε a dependent variable rather than a free parameter:
instead of asking "how many regimes at this ε?", it asks
"at how many scales is this point embedded in a stable cluster?".

The two methods are complementary:
- ε-sweep: precise partition at a chosen resolution
- cover height: multi-scale regime depth map, no ε commitment required

---

## Scope Granularity and Invisible Regimes

A regime invisible to a fixed-ε sweep — because it exists only within a
narrow ε-window — would produce a local elevation in the cover height map
even if no individual ε shows a stable plateau.

This is the primary motivation for the method: to expose regimes that
require fine-grained ε selection to detect, without requiring that selection
to be made in advance.

**Open question (Q_NEW_13):** Do local maxima of h(b_i) in BC space correspond
systematically to stable ε-plateaus in the standard N(ε) curve?
If yes, cover height could serve as a pre-filter for ε-sweep parameter choice.
See `docs/notes/open_questions.md`.

---

## Diagnostic: BC-Space Covers Are Flat on Uniform Grids

An important negative result: if covers are built along BC axes rather than
the observable axis, a uniform BC grid produces 0% height variation.

**Reason:** All BC points are equidistant by construction. At any ε, every
point lies in a cover of identical size. The weighted height is a constant.

This holds even when ε is swept across four decades.

**Consequence:** BC-space covers are only informative when the BC sampling
is non-uniform (e.g. adaptive grids, experimental data with clustering).
For designed sweeps with uniform grids, observable-space covers are the
correct approach.

---

## Empirical Result: Kuramoto 2D Sweep (2026-03-27)

System: Kuramoto model, N=400, T=150, observable = r_ss.
BC grid: κ ∈ [0, 3] (40 points), σ ∈ [0.4, 2.0] (28 points). Total: 1120 points.
ε range: [2.1 × 10⁻⁵, 0.96], 200 log steps.

Results:
- h_min = 62299, h_max = 117322, mean = 96527, std = 18217
- Dynamic range: 57%

The height field is highest in the incoherent regime (κ ≪ κ_c) and lowest
in the synchronized regime (κ ≫ κ_c), with a gradual gradient across
the diagonal transition boundary κ_c ≈ 2σ.

Figures:
- `figures/kuramoto_2d_observable_heatmap.png` — raw observable field
- `figures/obs_space_cover_height_panel.png` — height field: raw, z-score, min-subtracted
- `figures/obs_height_overlay.png` — height contours overlaid on observable field
- `figures/obs_cover_count_curve.png` — cover count decay as function of ε

Implementation: `Simulationen/cover_observable_space.py`

---

## Limitations

1. **Contiguous cover assumption:** the method groups consecutive sorted points,
   not all pairs within distance ε. Two points with nearly identical observable
   values but a third point between them (with a very different value) would not
   be co-grouped unless ε is large enough to bridge all intermediate gaps.

2. **Observable-space covers are not BC-space partitions:** the cover height
   reflects observable clustering, not spatial proximity in BC space. Two
   BC-distant points with the same observable value contribute to the same cover.

3. **Single observable:** the method as implemented uses one observable at a time.
   Extension to multi-observable scopes (Π = {π₁, π₂, ...}) requires a distance
   metric in the joint observable space. See Q_NEW_13.

4. **Interpretation asymmetry:** high height in the incoherent regime (Kuramoto)
   reflects the flat observable landscape there, not a "more stable regime"
   in the dynamical sense. The height reflects observable density, which depends
   on both the dynamics and the BC sampling geometry.

---

## Multi-Case Analysis: Sufficient vs. Insufficient Observables (2026-03-28)

Cover height was computed for all four active ARW cases with raw sweep data.

### Central hypothesis tested

Sufficient observables show higher cover-height dynamic range (DR) than
insufficient observables.

**Result: not universally supported.** DR alone is ambiguous.

### Three profile patterns observed

| Pattern | DR    | Profile shape     | Interpretation           | Example              |
|---------|-------|-------------------|--------------------------|----------------------|
| A       | High  | Smooth / step     | True regime structure    | r_ss (0001), PLV (0004) |
| B       | High  | Jagged / noisy    | F0 structural failure    | lambda_proxy (0002/0003) |
| C       | Low   | Flat              | F1 span failure          | amp_asym (0004)      |

The SHAPE of the cover-height profile, not DR alone, discriminates between
sufficient observables and the two types of failure (F0, F1).

### Key observation: DR vs. pipeline span

A sufficient observable with a smooth monotone gradient (var_rel in CASE-0002/0003)
can show LOW DR because its observable values are approximately uniformly distributed
in observable space — no prominent density clusters. The pipeline correctly identifies
it as sufficient because its span exceeds ε, but cover-height does not detect this.

Cover-height DR is high only when the observable has DENSITY CONTRAST in observable
space: dense clusters separated by sparse transition zones. A purely monotone
gradient lacks this contrast regardless of its span.

**Conclusion:** cover-height and pipeline sufficiency are complementary.
Cover-height detects observable clustering structure; the pipeline detects
span-relative-to-ε. Both are needed for a complete picture.

Figures:
- `figures/cover_height_all_cases.png` — per-case profiles
- `figures/cover_height_dr_comparison.png` — DR comparison bar chart

Reference: `docs/notes/research_journal.md` session 2026-03-28.

---

## 2D BC Sweep Analysis: Three Cases (2026-03-28)

Cover height was extended to 2D BC grids for CASE-0002, CASE-0003, and CASE-0004,
sweeping two BCs simultaneously.

### Setup

Self-contained RK4 simulations (no external dependencies) were run for:
- CASE-0002 Pendulum: κ ∈ [0, 10] × γ ∈ [0.02, 0.4] (300 pts)
- CASE-0003 Doppelpendel: E ∈ [0.5, 30 J] × m₂ ∈ [0.3, 2.0 kg] (308 pts)
- CASE-0004 Stuart-Landau: K ∈ [0.005, 0.15] × λ ∈ [0.3, 1.5] (252 pts)

Cover height was computed identically to the 1D case (the 2D grid is flattened
to a 1D array of observable values). Results are then projected back to the
2D BC plane for visualization.

### Results

| Case      | Observable     | Class | DR 2D  |
|-----------|----------------|-------|--------|
| CASE-0002 | var_rel        | S     | 11.9%  |
| CASE-0002 | lambda_proxy   | I     | 17.5%  |
| CASE-0003 | var_rel        | S     | 23.3%  |
| CASE-0003 | lambda_proxy   | I     | 89.3%  |
| CASE-0004 | PLV            | S     | 136.1% |
| CASE-0004 | amp_asym       | I     | 14.2%  |

CASE-0004 remains the clearest discriminator (10× DR ratio). The three-pattern
diagnosis from the 1D analysis holds in 2D.

### New finding: BC interaction structure

The 2D analysis reveals something the 1D sweeps cannot: whether regime
boundaries are axis-aligned or diagonal in BC space.

In CASE-0002, cover-height contours run diagonally across the (κ, γ) plane.
This indicates that the regime boundary is a joint condition on κ and γ —
neither BC independently determines which regime the system is in. The regime
depth function h(κ, γ) is not separable as h₁(κ) + h₂(γ).

In CASE-0004, PLV contours trace the theoretical synchronization boundary
K_c ≈ λ — a linear relationship between K and λ that is invisible in any
1D sweep at fixed λ.

This BC interaction detection is a capability unique to multi-dimensional
BC sweeps combined with cover height visualization.

Figures:
- `figures/cover2d_0002_*` — CASE-0002 κ×γ panels and overlays
- `figures/cover2d_0003_*` — CASE-0003 E×m₂ panels and overlays
- `figures/cover2d_0004_*` — CASE-0004 K×λ panels and overlays
- `figures/cover2d_dr_comparison.png` — cross-case DR comparison

Figure descriptions: `docs/figures/cover_2d_all_cases.md`
Implementation: `Simulationen/sweep_2d_all_cases.py`, `Simulationen/cover_2d_all_cases.py`
Open questions: Q_NEW_18 in `docs/notes/open_questions.md`


---

## Relationship to Cover-Stability Criterion (Felder 2026)

The formal foundation for the observable-space cover height method is now
provided by Felder (2026), which proves when a cover construction sustains
observable information (see `docs/core/cover_stability_criterion.md`).

### Agreement with the formal Čech cover (Felder 2026 §3)

The paper constructs the observable cover as **connected components of the
ε-adjacency graph G_ε(O)** — the formal Čech cover construction. The ARW
cover height method uses a **contiguous interval grouping** in sorted
observable space: groups break wherever a gap > ε occurs in the sorted sequence.

The two constructions **agree when the observable is monotone along BC space**.
When O is monotone (or approximately so), the path-connected components of
G_ε(O) coincide with the contiguous groups in sorted observable space.

They **diverge for non-monotone observables**: if observable values are
non-monotone along BC space, two BC points with similar observable values
may not be neighbors in sorted order. The Čech cover groups them (they are
ε-adjacent); the contiguous grouping may not (if a point with a different
value lies between them in sort order). The paper's construction is provably
transitivity-correct for all cases; the ARW method is an approximation that
works well for monotone observables but lacks formal grounding for non-monotone cases.

The cover height doc already acknowledged a related limitation (§Limitations §1).
It is now confirmed as a formal distinction, not merely a numerical approximation.

### Status of the three-pattern diagnostic

The three-pattern diagnostic (Pattern A: true regime structure; Pattern B: F0
structural failure; Pattern C: F1 span failure) is empirically confirmed across
four cases. The Felder 2026 framework provides the formal backing:

- **Pattern A** (smooth/step profile, high DR): observables for which
  sup_x σ_Δ(x) < ε — the admissible resolution regime is non-empty.
- **Pattern B** (jagged/noisy profile, high DR): F0 observables where
  pre-scope substrate fails — σ_Δ(x) → ∞ in Z(π). The noise in the profile
  reflects the instability of the observable outside R(π).
- **Pattern C** (flat profile, low DR): F1 observables where ε ≥ ε*(O,X)
  — the cover is trivial and cover height accumulates no differential signal.

A fourth pattern is now expected for **F-gradient** observables: a profile
with a pronounced dip at the descriptive crossover zone (E ≈ ω₀² in the
conservative pendulum), reflecting locally high σ_Δ within R(π). This pattern
has not yet been empirically tested with the cover height method (pending
CASE-0003b with ω observable).

### Promotion rationale

Promoted from `hypothesis` to `working-definition` on 2026-04-29:

- Empirically confirmed across four ARW cases (CASE-0001–0004)
- 2D BC sweep extension confirmed and validated (CASE-0002, -0003, -0004)
- Three-pattern diagnostic confirmed and formally grounded (Felder 2026)
- Formal relationship to the Čech cover construction clarified (agreement for
  monotone observables; known divergence for non-monotone cases)
- Remaining open question (Čech cover for non-monotone observables) is now
  a well-defined research question, not an unexamined limitation
