---
status: note
layer: cases/CASE-20260430-0013/
case_id: CASE-20260430-0013   # assign sequential ID on repo commit
title: "Vertical Spring-Mass Chain — Multi-Scale Observable Scope"
version: 3
created: 2026-04-30
supersedes: ScopeSpec_signature_first_multi_scale_pendulum_v2.md
changes_from_v2: >
  System redesigned: vertical 1D spring-mass chain (N masses, N springs)
  with periodic vertical pivot excitation. No angular degrees of freedom.
  Observable hierarchy redefined as absolute/relative displacements —
  no coordinate transformation required.
  CHECK-3 resolved as C1 (direct forcing, gravity as static preload).
  π_micro redefined as spring-extension variance (relative displacement).
  π_meso as COM variance (absolute, mass-weighted).
  π_macro as end-mass variance (absolute, terminal).
  N = 1..5 as conditioned parameter, separate runs.
  2D sweep (A, Ω) as active BC domain.
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/multi_scale_observables_and_latent_regime_formation.md
  - docs/advanced/multi_scale_sweep_protocol.md
  - cases/CASE-20260311-0002/
related_cases:
  - CASE-20260311-0002
  - CASE-20260311-0003
open_questions:
  - Q-MULTI-01
  - Q-MULTI-02
---

# ScopeSpec — Signature First (v3)
## Vertical Spring-Mass Chain: Multi-Scale Observable Scope

**Scientific purpose:** Empirically test the latent regime formation
hypothesis using the simplest possible multi-scale mechanical system.
A vertical spring-mass chain with N masses and periodic pivot excitation
provides a clean hierarchy of absolute and relative displacement
observables without angular degrees of freedom or coordinate
transformations. The observable hierarchy is directly readable from
simulation coordinates.

**Design principle:** Simplicity as science. The system is chosen to make
the observable hierarchy maximally transparent, not to maximize physical
richness. Each observable level corresponds directly to a measurable
quantity — no post-processing transformation is required.

---

## 1. System

**Type:** 1D vertical spring-mass chain

**Configuration:**
```
pivot (z_0 = A·sin(Ω·t)) — prescribed vertical motion
  |
[spring 1, k]
  |
[mass 1, m]
  |
[spring 2, k]
  |
[mass 2, m]
  |
  ...
  |
[spring N, k]
  |
[mass N, m]    ← end mass
```

All masses move only in the vertical direction. Equal masses m and
equal spring constants k for all initial runs (N=1..5).

**State vector:**
```
x = (z_1, ..., z_N, ż_1, ..., ż_N) ∈ ℝ^{2N}
```

where z_i(t) is the absolute vertical position of mass i, measured
downward from the pivot rest position.

**Equations of motion (lab frame):**
```
m · z̈_i = m·g
         - k · (z_i - z_{i-1} - l_0)     [spring above]
         + k · (z_{i+1} - z_i - l_0)     [spring below, absent for i=N]
         - γ · ż_i                        [viscous damping]
```

with boundary condition:
```
z_0(t) = A · sin(Ω · t)    [prescribed pivot motion]
```

**Gravity:** Acts as static preload, shifts equilibrium positions z_i,eq
downward by m·g·i/k relative to the zero-gravity case. Does not create
parametric coupling in the 1D vertical case. Gravity is included for
physical realism (correct equilibrium structure) but does not change
the qualitative regime structure.

---

## 2. Full Parameter Tuple B

| Parameter | Symbol | Role | Type | Initial value |
|---|---|---|---|---|
| Forcing amplitude | A | Primary sweep axis | Active | [0.0, 0.5] m |
| Forcing frequency ratio | Ω/ω_1 | Primary sweep axis | Active | [0.2, 3.0] |
| Link count | N | Structural complexity | Conditioned | 1, 2, 3, 4, 5 (separate runs) |
| Damping coefficient | γ | Energy dissipation | Conditioned | 0.05 |
| Mass | m | Energy scale | Conditioned | 1.0 kg |
| Spring constant | k | Frequency scale | Conditioned | 1.0 N/m |
| Rest length | l_0 | Geometric scale | Conditioned | 1.0 m |

**Active BC domain (initial runs):**
```
B_active = A × (Ω/ω_1)
         = [0.0, 0.5] × [0.2, 3.0]
```

**Reference frequency:**
```
ω_1(N, k, m) = eigenfrequency of mode 1 for given N, k, m
```

Ω is expressed as ratio Ω/ω_1 so that resonance structure is
N-independent in normalized coordinates. This ensures comparability
across runs with different N.

**Eigenfrequencies for uniform chain (k_i=k, m_i=m):**
```
ω_j = 2·√(k/m) · sin(j·π / (2(N+1))),   j = 1..N
```

For k=m=1: ω_j = 2·sin(j·π/(2(N+1)))

Resonance bands in Ω/ω_1 space occur at:
```
Ω/ω_1 = ω_j/ω_1 = sin(j·π/(2(N+1))) / sin(π/(2(N+1)))
```

These are analytically known for all N — they constitute the
theoretical predictions for θ*_micro before any simulation.

**Conditioned parameters:** γ, m, k, l_0 fixed per run. All values
recorded in BCManifest. N fixed per run; five separate runs for N=1..5.

---

## 3. Observable Definitions

The observable hierarchy maps directly onto the coordinate structure
of the simulation. No transformation required.

### π_micro — Spring Extension Variance (Relative, Internal)

```
d_i(t) = z_i(t) - z_{i-1}(t) - l_0    [extension of spring i from rest]
         i = 1..N,  z_0(t) = A·sin(Ω·t)

π_micro(b) = (1/N) · Σ_{i=1}^{N} Var_t[ d_i(t) ]    [mean spring extension variance]
```

**What it sees:** How much each spring is being stretched and compressed
over time. If all masses move together (coherent, first-mode motion),
all spring extensions are small and similar. If internal modes are
active, adjacent masses move differently — spring extensions are large
and variable across springs.

**What it loses:** Nothing about internal structure. This is the direct
measure of relative motion between adjacent masses.

**BC class signature:** Restriction (direct measurement of relative
displacements; no aggregation operator). The observable resolves the
finest level of structure in the chain.

**Structure-preservation:** By construction — d_i(t) is the relative
displacement between mass i and mass i-1. It directly reflects internal
mode activity without compression.

**Substrate check (A0–A6):**
- A0: z_i well-defined for all t ✓
- A1: difference operator d_i = z_i - z_{i-1} - l_0 well-defined ✓
- A2: Var_t converges in stationary window (γ > 0 ensures stationarity) ✓
- A3: system reaches stationary state after transient decay ✓
- A4: stationary window T_obs sufficient (T_obs >> 1/(γ/m)) ✓
- A5: mean subtracted implicitly by variance operator ✓
- A6: no drift in stationary window (forced system with damping) ✓

**F-gradient risk:** High near resonance Ω/ω_1 = ω_j/ω_1 — spring
extensions grow rapidly with A near resonance. σ_Δ(b) may exceed ε
in resonance bands. Apply stability mask; do not classify as F0.

---

### π_meso — Center-of-Mass Variance (Absolute, Collective)

```
z_COM(t) = (1/N) · Σ_{i=1}^{N} z_i(t)    [equal masses: simple mean]

π_meso(b) = Var_t[ z_COM(t) ]
```

**What it sees:** How much the collective center of mass moves. If all
masses move coherently (rigid-body-like), z_COM reflects the collective
motion. If internal modes are active and cancel in the mean, z_COM may
be small even when individual masses move significantly.

**What it loses:** Relative motion between masses — if mass 1 moves up
while mass 2 moves down by the same amount, z_COM is unchanged. Internal
anti-phase modes are invisible to π_meso.

**BC class signature:** Aggregation (mean over all masses) + Restriction.
Structure-preserving in the sense that it retains the collective
amplitude — but it compresses the internal distribution.

**Structure-preservation criterion check:**
```
Var_{configs at fixed π_macro}[ π_meso ] > 0   ?
```
For the spring-mass chain: two configurations with the same end-mass
variance but different internal mode distributions will in general have
different COM variances (unless the anti-phase modes perfectly cancel).
The criterion holds generically. At anti-phase mode resonance (even N):
COM variance is suppressed while spring extensions are large — this is
a latent regime that π_macro may also miss.

**Substrate check:** Same as π_micro — all A0–A6 satisfied with γ > 0.

---

### π_macro — End-Mass Variance (Absolute, Terminal)

```
π_macro(b) = Var_t[ z_N(t) ]
```

**What it sees:** How much the bottom mass moves. This is the terminal
observable — what an external observer measuring only the end output
would see.

**What it loses:** All internal structure. z_N depends on all spring
extensions, but only through their sum:
```
z_N(t) = z_0(t) + Σ_{i=1}^{N} (d_i(t) + l_0)
        = A·sin(Ω·t) + Σ_i d_i(t) + N·l_0
```

Therefore:
```
Var_t[z_N] = Var_t[ Σ_i d_i(t) ]   (pivot variance cancels in covariance)
```

**This is the key structural fact:** π_macro is the variance of the
**sum** of spring extensions. Two configurations with very different
individual d_i(t) patterns can produce the same sum variance if their
covariances compensate. π_macro is therefore blind to the internal
distribution of motion — only the net accumulated extension matters.

**Observable hierarchy summary:**

```
π_micro  measures  Var[d_i]        per spring       finest resolution
π_meso   measures  Var[mean(z_i)]  mean position    intermediate
π_macro  measures  Var[sum(d_i)]   accumulated      coarsest
```

The three observables are algebraically related but structurally distinct:
mean and sum of variances are equal only when springs are uncorrelated.
When internal modes create correlated spring extensions, the three
observables diverge — and this divergence is the regime signal.

---

## 4. Primitive Operators

| Operator | Symbol | Present? | Where |
|---|---|---|---|
| Coupling | ∘ | Yes | Spring forces couple adjacent masses |
| Restriction | × | Yes | A restricts accessible amplitude envelope |
| Dissipation | γ | Yes | Viscous damping at each mass |
| Forcing | F_ext | Yes | Pivot motion drives the chain |
| Aggregation | E[·] | Yes | π_meso (mean), π_macro (sum) |
| Symmetry Breaking | ⊗ | No | — |

**Primary BC class: Forcing + Restriction**

A (amplitude) is a Restriction operator: it bounds the energy that can
enter the system per cycle. Ω (frequency) is a Forcing operator: it
selects which modes receive energy preferentially through resonance.

The two axes of B are mechanically distinct BC classes — the 2D sweep
tests both simultaneously.

---

## 5. Expected Partition Structure

### Resonance bands (theoretical predictions for θ*_micro)

For N=1: single resonance band at Ω/ω_1 = 1.0

For N=3: resonance bands at Ω/ω_1 = 1.0, 1.73, 1.93  (approximately)

For N=5: resonance bands at Ω/ω_1 = 1.0, 1.85, 2.41, 2.73, 2.93

These are the predicted π_micro cover boundaries before any simulation.
The bands widen with increasing A (more energy → larger σ_Δ → boundary
smears). At small A, bands are narrow; at large A, adjacent bands may merge.

### Expected partition table

| Observable | N=1 expected N* | N=5 expected N* | Cover boundary character |
|---|---|---|---|
| π_macro (sum ext. var.) | 2 | 2–3 | Broad resonance envelope |
| π_meso (COM var.) | 2 | 3–4 | Collective resonance + anti-phase suppression |
| π_micro (mean spring var.) | 2–3 | 5–7 | Individual resonance bands per mode |

**Latent regime hypothesis (P2):** At Ω/ω_1 values near higher-mode
resonances (ω_j/ω_1 for j > 1), π_micro detects a regime transition
(spring extensions internally reorganized) while π_macro may remain in
a single cover element (sum of extensions unchanged). This is testable
because the resonance frequencies are analytically known.

**Anti-phase latent regime (new, specific to this system):**
For even N, anti-phase modes (adjacent masses moving in opposite
directions) have zero COM displacement contribution. π_meso will
be suppressed at anti-phase resonance while π_micro is large. This
is a structurally clean latent regime case — π_meso AND π_macro
both fail to see the anti-phase mode activity.

---

## 6. Perturbation Class Δ

```
Δ = { δ : |δz_i(0)| ≤ r_z = 0.01 m,
          |δż_i(0)| ≤ r_v = 0.01 m/s,
          for all i = 1..N }
```

Small relative to expected stationary amplitudes (~A = 0.1–0.5 m).
Uniform across all masses — tests regime robustness to symmetric
initial condition variation.

**T_sim as observable-specific substrate requirement:**

T_transient = 100 s and T_obs = 100 s are requirements of the substrate
assumptions (A6: stationarity) for the time-averaged observables
π_micro, π_meso, π_macro. They are not properties of the system.
A configurational observable π_κ would have no T_sim requirement.
This distinction must be recorded in BCManifest per observable:

```yaml
substrate_requirements:
  pi_micro:  { T_transient: 100, T_obs: 100, basis: "A6 stationarity, tau=m/gamma=20s" }
  pi_meso:   { T_transient: 100, T_obs: 100, basis: "A6 stationarity" }
  pi_macro:  { T_transient: 100, T_obs: 100, basis: "A6 stationarity" }
```

---

## 7. Resolution Vector ε_vector

Three-component: ε_vector = (ε_micro, ε_meso, ε_macro)

To be determined via ε-sweep. Initial estimates from expected
stationary amplitudes at mid-range A = 0.2 m, off-resonance:

| Observable | Expected span | ε estimate | Notes |
|---|---|---|---|
| π_micro | O(0.01–0.1) m² | 0.002–0.01 | Narrow: spring extensions small off-resonance |
| π_meso  | O(0.05–0.3) m² | 0.005–0.03 | Wider: COM includes direct forcing contribution |
| π_macro | O(0.1–0.5) m² | 0.01–0.05  | Widest: end-mass amplitude largest |

Grid density from sweep protocol:
```
Δb_min = ε_{ℓ*} / G_{ℓ*,max}
```
where ℓ* = argmax_ℓ G_ℓ,max/ε_ℓ — the observable with the largest gradient
relative to its working ε. For this system, π_micro is expected to be ℓ*
along the Ω/ω_1 axis (resonance bands are sharp), but this should be
confirmed in the pilot run rather than assumed.

---

## 8. Falsification Conditions

| ID | Observable | Trigger | Severity |
|---|---|---|---|
| F-gradient | π_micro | σ_Δ ≥ ε_micro in resonance bands | scope_refinement (stability mask; narrow Δ or tighten ε) |
| F1 | π_macro | span(π_macro) < 2·ε_macro across full B | observable_replacement or widen A range |
| F2 | any | θ* unstable under Δ | scope_rejection for that boundary |
| F3 | all | No observable produces plateau | scope_redesign |
| F4 | any | θ* at sweep boundary | sweep_refinement (extend A or Ω range) |

**Positive findings (not falsifications):**

- N*_micro > N*_macro: confirms latent regime structure ✓
- π_meso suppressed at anti-phase resonance while π_micro large: confirms
  anti-phase latent regime ✓
- Non-axis-parallel cover boundaries in (A, Ω) plane: confirms BC class
  non-independence (Forcing + Restriction interaction) ✓

---

## 9. Run Structure

**Five separate runs, one per N value:**

| Run | N | ω_1 (k=m=1) | Resonance bands Ω/ω_1 | Primary new feature |
|---|---|---|---|---|
| R1 | 1 | 1.0 | 1.0 | Baseline; single mode |
| R2 | 2 | 0.765 | 1.0, 1.85 | First multi-mode case |
| R3 | 3 | 0.445 | 1.0, 1.73, 1.93 | First potential latent regime |
| R4 | 4 | 0.390 | 1.0, ... | Anti-phase mode (even N) |
| R5 | 5 | 0.285 | 1.0, 1.85, 2.41, 2.73, 2.93 | Full multi-scale structure |

Run R1 serves as pipeline validation — single mode, single resonance
band, all observables should agree on N*=2 with boundary near Ω/ω_1=1.

**Transfer analysis across runs:**
Φ(R1, R5) at the π_macro level tests whether the terminal output
structure is preserved as N increases. If Φ is high, the macro
regime is robust to internal complexity. If Φ is low, adding internal
degrees of freedom fundamentally changes the terminal behavior.

---

## 10. Pre-Registration

**P1 (Cover anisotropy in B):** N*_micro ≥ N*_meso ≥ N*_macro for all runs
R2–R5 at their respective working ε values.

This tests whether the cover structure of the three observables is
anisotropic in B — specifically, whether π_micro resolves more structure
than π_macro in the (A, Ω) plane at the chosen ε values. P1 is not a
confirmation of an assumed hierarchy; it is an empirical measurement of
cover-geometric ordering for this system at these conditioned parameters.
Non-confirmation of P1 is a positive finding: it would mean that π_macro
and π_micro are comparably sensitive to B-variation at their working ε,
which itself constrains the observable coupling structure.

**P2 (Observable latency):** For N ≥ 3 and Ω/ω_1 near ω_j/ω_1 (j ≥ 2):
C_ε(π_micro, R) is non-trivial in region R while C_ε(π_macro, R) is trivial.
This is the cover-geometric definition of π_macro being latent with respect
to π_micro in R — no causal or temporal claim is implied.

**P3 (Anti-phase suppression):** For even N (R2, R4) at anti-phase
resonance: π_meso is suppressed (low variance) while π_micro is
elevated (large spring extension variance). π_macro may or may not
detect this — the outcome is an open empirical question.

**P4 (Non-axis-parallel boundaries):** Cover boundaries in (A, Ω)
space are not parallel to either axis — they follow the resonance
structure which is A-dependent (wider at higher A).

**P5 (N-scaling of latent regimes):** N*_micro scales approximately
with N (one resonance band per mode), while N*_macro scales much
more slowly — confirming that internal complexity accumulates in
π_micro while remaining largely invisible to π_macro.

**P6 (Baseline consistency — R1):** For N=1, all three observables
produce N*=2 with the same boundary location θ* ≈ Ω/ω_1 = 1.0.
This is the necessary condition for observable consistency at minimal
system complexity. If P6 fails, the pipeline has an error.
