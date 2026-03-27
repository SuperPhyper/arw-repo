---
status: hypothesis
layer: docs/advanced/
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
