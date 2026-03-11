---
status: working-definition
---

# ε and Scope Resolution

## Overview

ε is the resolution threshold parameter in the ARW scope tuple:

```
S = (B, Π, Δ, ε)
```

It determines the granularity at which the scope distinguishes states —
the minimum observable difference that constitutes a meaningful distinction.

This document consolidates and sharpens the treatment of ε,
including its interaction with Δ, its role in partition generation,
and its interpretation as a resolution window in real systems.

---

## 1 Formal Definition

Two states x, y ∈ X_B are indistinguishable under scope S if:

```
|Π(x) − Π(y)| < ε
```

They are assigned to the same regime class: x ~_S y.

ε is not a measurement precision — it is a **structural parameter of the scope**.
It specifies what resolution the description *requires* to be meaningful,
not what resolution an instrument can achieve.

---

## 2 ε as a Resolution Window

In real systems, ε is better understood as a **resolution window** than a
scalar threshold. Behavioral regimes occupy finite regions in parameter space,
and two states are equivalent when their observable differences remain within
this window — not just below a single cutoff.

```
ε ⊆ observable space   (region, not point)
x ~_S y   iff   Π(x) - Π(y) ∈ ε
```

**Example — ECDL laser:**
A single-mode laser operates stably within a finite current and temperature window.
Within that window, the observable (output mode) is invariant.
The window is ε. States inside are a single regime class; crossing the window boundary
triggers a mode hop — a scope transition.

**Example — Labyrinth agent:**
Policy embeddings within cosine distance 0.1 are in the same mode.
The "0.1 ball" is ε in the policy embedding space.
Two trajectories are the same mode if their embeddings fall within this ball,
regardless of which specific path through the maze was taken.

---

## 3 ε Determines Partition Granularity

ε controls how many regime classes the ARW operator induces:

```
ε large  →  many states indistinguishable  →  coarse partition (few classes)
ε small  →  more states distinguishable    →  fine partition (many classes)
```

This makes ε the primary parameter for moving between levels
of a hierarchical partition:

```
ε₁ > ε₂ > ε₃   →   R_S(ε₁) ⊇ R_S(ε₂) ⊇ R_S(ε₃)   (coarser to finer)
```

Each ε value induces a distinct scope and a distinct partition.
Changing ε while keeping B and Π fixed is a scope transition along
the resolution dimension.

---

## 4 The Admissible ε-Interval

Section 3 shows that changing ε shifts the partition. But not every ε-change
produces a *structural* change — across a range of ε values, the partition
retains the same regime count, adjacency graph, and qualitative structure.
Only at critical ε values does the partition jump (regimes merge or split).

This motivates replacing the question "what is the right ε?" with a
more robust formulation: **what is the interval of ε values under which
a given scope remains structurally valid?**

### Definition

For a fixed scope skeleton (B, Π, Δ), the **admissible ε-interval** is:

```
I_ε = [ε_min, ε_max]
```

where:

- **ε_min** is the smallest ε above which the partition is stable against
  observational noise. Below ε_min, the partition fragments: small fluctuations
  create spurious regime classes. Formally: for ε < ε_min, the partition is
  not Δ-consistent (see §5 below) — admissible perturbations generate
  observable differences above ε, producing noise-sensitive class assignments
  across the bulk of state space (not just at boundaries).

- **ε_max** is the largest ε below which the partition preserves the
  structurally relevant distinctions. Above ε_max, regimes that are
  qualitatively different (different stability properties, different
  dynamical behavior) collapse into the same class.

Within I_ε, the **partition invariants** (regime count N, adjacency graph G_S,
transition boundary locations θ*) are stable under small ε-perturbations.
At the interval boundaries, at least one invariant jumps.

### Formal Characterization

Define the partition invariant signature as:

```
σ(ε) = (N(ε), G_S(ε))
```

Then I_ε is the maximal connected interval containing the working ε
such that σ(ε) is constant:

```
I_ε = { ε' > 0 : σ(ε') = σ(ε₀) }   (connected component containing ε₀)
```

The interval boundaries are the **critical ε-values** — resolution-driven
analogs of the transition boundaries θ* that appear along BC parameters.

### The ε-Sweep

The admissible interval is determined empirically by an **ε-sweep**:
fix B, Π, Δ and the BC parameter values, then vary ε and record the
partition invariants at each step.

```
ε-sweep protocol:
1. Choose ε range [ε_low, ε_high] spanning several orders of magnitude
2. For each ε value, compute A(S(ε)) = R_S(ε)
3. Record σ(ε) = (N(ε), G_S(ε))
4. Identify plateaus where σ is constant → these are admissible intervals
5. Identify jumps → these are critical ε-values
```

This is the resolution-dimension analog of the BC parameter sweep
already implemented in `pipeline.sweep`. The plateau structure directly
answers the ε-estimation question: any ε within the plateau is valid,
and the plateau width measures how robust the scope is against
resolution misspecification.

### Plateau Width as Robustness Measure

The width of I_ε has direct interpretive value:

```
w(I_ε) = log(ε_max / ε_min)
```

(Log-ratio because ε spans orders of magnitude.)

- **Wide plateau** (large w): the scope is robust. The partition structure
  is not sensitive to the precise choice of ε. The regime distinctions are
  "real" in the sense that they persist across a broad resolution range.

- **Narrow plateau** (small w): the scope is fragile. A small change in
  resolution destroys or creates regime distinctions. This signals that the
  partition may be an artifact of a particular ε choice rather than a
  structural feature of the system under B and Π.

- **No plateau** (σ changes continuously): the system has no stable regime
  structure at this scope. The observables in Π may not be the right ones,
  or the BC class does not generate discrete regimes.

### Connection to Existing Framework Concepts

The ε-interval connects to several existing constructs:

**Admissible reduction (§6):** If S' is an admissible coarsening of S,
then ε' > ε but both lie within adjacent or overlapping plateaus.
The reduction is admissible precisely because the partition structure
is preserved across the ε-change. When ε' crosses a critical value
(exits the plateau), the coarsening is no longer admissible — it is
a scope transition.

**ε–Δ consistency (§5):** The lower bound ε_min is determined by Δ.
Specifically, ε_min is the smallest ε satisfying the consistency condition
for bulk states:

```
ε_min ≈ max_{x ∈ bulk} max_{δ ∈ Δ} |Π(x+δ) - Π(x)|
```

Below this, admissible perturbations cross the resolution threshold
everywhere, not just at boundaries.

**Distortion metrics:** The PCI (Partition Compatibility Index) between
two scopes can be reinterpreted as measuring whether their ε-values
fall in the same plateau. PCI ≈ 1 when both scopes are in the same
admissible interval; PCI drops when they are in different plateaus.

### Example — Kuramoto System

Empirical ε-sweep on CASE-20260311-0001 (N=500 oscillators, 15 κ-values
in [0, 3], Π = {r_ss}). The sweep varies ε across [0.001, 1.0]
in 80 logarithmic steps and records σ(ε) = (N(ε), G_S(ε)) at each step.

**Observable landscape:** The 15 sweep points produce r_ss values
that cluster naturally: 10 points in the incoherent range (r_ss ∈ [0.039, 0.072])
with small inter-point gaps (Δr < 0.01), then two large jumps at the
synchronization transition (Δr ≈ 0.30 and 0.38), followed by the
synchronized range (r_ss > 0.74).

**Plateau structure:**

```
ε ∈ [0.009, 0.047]  →  N=5, edges=4   w = 1.66  (most robust)
ε ∈ [0.051, 0.134]  →  N=4, edges=3   w = 0.96
ε ∈ [0.146, 0.294]  →  N=3, edges=2   w = 0.70
ε ∈ [0.321, 0.350]  →  N=2, edges=1   w = 0.09
ε ∈ [0.382, 1.000]  →  N=1, edges=0   (collapsed)
```

**Interpretation:**

The *most robust* partition (widest plateau, w = 1.66) is the 5-regime
partition, not the expected 3-regime partition. This is because the
incoherent range contains fine structure: the 10 low-κ points have
observable gaps on the order of 0.001–0.009, which are real distinctions
at fine resolution. Only at ε > 0.05 do these sub-regimes merge.

The theoretically expected 3-regime partition (Incoherent / Partial /
Synchronized) appears at ε ∈ [0.146, 0.294] with w = 0.70 — a moderately
robust scope. This confirms that the 3-regime description is a valid
*coarsening* of the finer structure, but it requires a resolution that
deliberately ignores intra-regime variation in the incoherent phase.

The working ε = 0.05 from the original ScopeSpec sits at the boundary
between the N=5 and N=4 plateaus (critical ε* ≈ 0.049). This is a
fragile position — a small ε change flips the regime count. The ε-sweep
reveals that either ε ≈ 0.03 (comfortably inside N=5) or ε ≈ 0.09
(comfortably inside N=4) would be more robust choices.

**Methodological lesson:** The ε-sweep resolves the estimation question
without needing to "guess" ε. The plateau structure is a property of the
system under (B, Π, Δ) — not a modeling choice. The researcher selects
*which plateau* to work in (i.e., what resolution level is appropriate
for the question at hand), and any ε within that plateau is equivalent.

See [figures/epsilon_sweep_kuramoto.png](../../figures/epsilon_sweep_kuramoto.png)
for the visualization of σ(ε) and plateau widths.

### Plateau Stability Under BC Variation — I_ε(κ)

A natural follow-up: does the admissible ε-interval change as the BC
parameter κ varies? A 2D (κ, ε) scope robustness map on Kuramoto
(80 κ-values in [0, 3.5], 60 ε-values) reveals a clear pattern:

**The scope is least robust near the phase transition.**

The local plateau width w(κ) — computed via sliding-window ε-sweeps —
drops from w ≈ 5.7 in the deep incoherent regime (κ < 0.5) to
w ≈ 1.6 in the transition region (κ ≈ 1.0–1.7), then recovers to
w ≈ 5.0 in the deep synchronized regime (κ > 2.8).

The correlation between w and the observable gradient |dr_ss/dκ|
is r = −0.77 — strongly negative. Where the system changes fastest
(|dr_ss/dκ| peaks at κ ≈ 1.48 with a value of 4.05), the scope is
most fragile.

**Interpretation:** This is not an artifact of sparse sampling. It reflects
a structural property: near the phase transition, small changes in κ
produce large observable shifts, which means the ε-threshold must be
precisely tuned to avoid either merging distinct regimes or fragmenting
a single regime. The admissible ε-interval narrows because the
observable landscape is steep.

This has a practical consequence: scope specifications near phase
transitions need tighter ε calibration. The ε-sweep is most valuable
precisely in the regions where the system is most interesting.

See [figures/epsilon_kappa_robustness.png](../../figures/epsilon_kappa_robustness.png)
for the visualization of w(κ) vs |dr/dκ|.

### Multiple Observables — Pendulum (λ_proxy, Var_rel)

The pendulum (CASE-20260311-0002) provides the first test of the
multi-observable ε question. It has two observables with very different
ranges:

```
lambda_proxy:  span = 0.037  (range [0.061, 0.098])
var_rel:       span = 0.275  (range [0.038, 0.313])
```

Independent ε-sweeps per observable reveal fundamentally different
plateau structures:

```
lambda_proxy:                          var_rel:
  N=12  ε∈[0.0001, 0.0006]  w=1.58     N=13  ε∈[0.0001, 0.0117]  w=4.76
  N=10  ε∈[0.0008, 0.0013]  w=0.58     N= 8  ε∈[0.0156, 0.0181]  w=0.14
  N= 9  ε∈[0.0016, 0.0021]  w=0.29     N= 5  ε∈[0.0209, 0.0241]  w=0.14
  N= 5  ε∈[0.0028, 0.0049]  w=0.58     N= 3  ε∈[0.0322, 0.0430]  w=0.29
  N= 1  ε∈[0.0076, 0.5000]  w=4.19     N= 1  ε∈[0.0496, 0.5000]  w=2.31
```

The two observables agree on N for only 30% of ε-values. They operate on
different ε-scales: lambda_proxy collapses to N=1 at ε ≈ 0.008, while
var_rel still distinguishes 13 regimes at that resolution.

**The joint partition** (same ε for both, regime = agreement on all
observables) is dominated by whichever observable is more discriminating
at that ε. In practice, this means the joint partition tracks var_rel
at intermediate ε, because lambda_proxy has already collapsed.

**Conclusion:** A single shared ε is insufficient for multi-observable
scopes with observables of different dynamic ranges. The admissible
ε-interval must be specified per observable:

```
I_ε = [ε₁_min, ε₁_max] × [ε₂_min, ε₂_max]
```

where each εᵢ is calibrated to the range and structure of πᵢ.
Alternatively, observables can be normalized to a common scale
before applying a single ε — but this normalization is itself a
scope choice that affects the partition.

---

## 5 The ε–Δ Interaction (Critical)

The interaction between ε and Δ is the most important and least
documented aspect of ε in the framework.

**Setup:**
Δ defines which perturbations are "noise" — perturbations the scope must
remain stable under. ε defines which observable differences are "meaningful".

**The critical case:**
A perturbation δ ∈ Δ (within the admissible range) that produces
an observable change |Π(x+δ) - Π(x)| > ε (above resolution threshold).

This state is **both admissible noise AND a distinguishable observable change**.
The scope assigns x and x+δ to different regime classes — but treats the
perturbation as admissible noise.

**Consequence:**
If this occurs, the regime assignment is unstable under admissible perturbations.
[x]_S and [x+δ]_S are different classes, but δ is within Δ.

This is the formal definition of a **partition boundary state**:
states x where ∃ δ ∈ Δ: |Π(x+δ) - Π(x)| > ε.

Such states are structurally ambiguous — they sit on the regime boundary
and their class assignment is noise-sensitive.

**Design implication:**
A well-specified scope should have ε and Δ consistent:
perturbations within Δ should produce observable changes below ε.

```
consistency condition:   max_{δ ∈ Δ} |Π(x+δ) - Π(x)| < ε   for bulk states x
```

Boundary states are the exception — and their density defines
the "width" of regime boundaries.
Narrow boundaries (few boundary states) → crisp partition.
Wide boundaries → diffuse partition → high distortion under aggregation.

---

## 6 ε and Admissibility

An observable π ∈ Π becomes **inadmissible** when its effects
on the observable space fall below ε:

```
|π(x) - π(y)| < ε   for all relevant pairs (x, y)
```

This means π produces no distinctions above resolution.
The degree of freedom associated with π is effectively latent —
it can be suppressed without changing the partition.

**Connection to emergence:**
When a previously admissible observable loses admissibility (its effects
drop below ε for the current scope), the partition loses a dimension.
The system appears to "simplify" — previously distinct regime classes merge.
This is the ε-mechanism behind emergence.

---

## 7 ε in the Experimental Systems

| System | ε specification | Interpretation |
|---|---|---|
| Kuramoto | Δr < 0.05 (order parameter) | Order parameter differences below 0.05 are same regime |
| Pendulum | δθ < 0.01 rad | Angular differences below 0.01 rad indistinguishable |
| Consensus models | Opinion difference < 0.02 | Agents within 0.02 opinion distance are same class |
| Labyrinth agent | Cosine distance < 0.1 (policy embedding) | Policies within 0.1 cosine distance are same mode |
| Mean-field (opinion) | ||ρ - ρ'||_L1 < 0.05 | Distribution differences below 0.05 are same MF regime |

**Empirical ε estimation:**
In each system, ε must be calibrated so that:
1. Bulk regime states are stable under Δ (consistency condition satisfied)
2. Boundary regions are identifiable (states where Δ-perturbations approach ε)
3. The resulting partition count matches theoretical predictions

---

## 8 Open Questions on ε

The following aspects of ε require further formalization:

- **ε as a function of state:** Should ε be uniform or can it vary across
  state space? High-symmetry regions may require finer resolution than bulk regions.
  If ε is state-dependent, the admissible interval (§4) becomes an admissible
  *region* in a function space — the formalization of this is open.
  The I_ε(κ) result (§4) suggests a related but distinct phenomenon: ε itself
  is uniform, but the *admissible range* of ε varies with system state.
- **ε-sweep implementation:** The ε-sweep protocol (§4) is implemented in
  `pipeline/epsilon_sweep.py` and validated on CASE-20260311-0001 (Kuramoto).
  The 2D map is implemented in `pipeline/epsilon_kappa_map.py`.
  The multi-observable sweep is in `pipeline/epsilon_multi_observable.py` and
  validated on CASE-20260311-0002 (Pendulum).
  Remaining: adaptive step refinement near critical ε-values, automatic
  plateau boundary detection.
- **Plateau stability under BC variation:** Empirically confirmed (§4).
  The admissible ε-interval narrows near phase transitions. Correlation
  between plateau width and observable gradient: r = −0.77 on Kuramoto.
  Open: does this hold for non-continuous transitions? For multi-stable systems?
- **ε and information content:** Is there a relationship between ε and the
  information-theoretic mutual information between scope observables?
  The plateau width w might correlate with channel capacity — wide plateaus
  indicate that the observable carries robust structural information.
- **Multiple ε for multiple observables:** Empirically confirmed as necessary
  (§4, Pendulum). Observables with different dynamic ranges require independent
  εᵢ. The admissible region is a box in ε-space. Open: what is the joint
  admissibility condition beyond component-wise? Does cross-observable
  correlation introduce additional constraints?
- **Observable normalization as scope choice:** The Pendulum result suggests
  that normalizing observables to a common scale before applying a single ε
  is itself a scope decision. Formalizing what "good" normalization means
  (preserving regime structure vs. destroying it) is an open problem.
