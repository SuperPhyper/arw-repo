---
title: "Consistency Check — Spring-Mass Chain, Parametric Excitation"
purpose: pre-scopespec formal verification
status: working
created: 2026-04-30
---

# Consistency Check
## Spring-Mass Chain with Parametric Vertical Excitation

This document verifies the physical model, observable definitions, BC class
assignment, and substrate conditions before the ScopeSpec v3 is written.
All claims marked [CHECK] require explicit confirmation before proceeding.

---

## 1. Physical Model

### 1.1 System Description

N masses connected in series by springs, hanging vertically from a pivot point.
The pivot undergoes prescribed vertical motion:

```
y_pivot(t) = A · sin(Ω · t)
```

All masses move only in the vertical direction (1D).

Coordinates: let z_i(t) be the absolute vertical position of mass i,
measured downward from the pivot rest position.

Rest lengths: l_i (natural length of spring i).
Spring constants: k_i (spring i connects mass i-1 to mass i; spring 1
connects pivot to mass 1).
Masses: m_i (equal for initial run: m_i = m for all i).

### 1.2 Equations of Motion

In the lab frame, mass i satisfies:

```
m_i · z̈_i = m_i · g
           - k_i   · (z_i - z_{i-1} - l_i)       [spring above: restoring]
           + k_{i+1} · (z_{i+1} - z_i - l_{i+1})  [spring below: pulling down]
           - γ_i · ż_i                              [damping]
```

with boundary condition:

```
z_0(t) = A · sin(Ω · t)   [pivot position — prescribed]
```

and z_{N+1} term absent (free end below mass N).

**Change of coordinates — relative displacement:**

Let u_i(t) = z_i(t) - z_i,eq - A·sin(Ω·t) be the displacement of mass i
relative to its equilibrium position in the moving frame.

In the moving frame, the equations become:

```
m_i · ü_i = -k_i·u_i + k_{i+1}·u_{i+1} - k_{i+1}·u_i
           - γ · u̇_i
           + m_i · A · Ω² · sin(Ω·t)              [inertial forcing term]
```

This is the standard form for a parametrically forced chain. The forcing
appears as an inertial term proportional to m_i · A · Ω² — each mass
experiences forcing proportional to its own mass and the pivot acceleration.

[CHECK-1] The forcing term m_i · A · Ω² · sin(Ω·t) is uniform across all
masses when m_i = m (equal masses). This means the forcing projects equally
onto all normal modes weighted by their mass-normalized eigenvectors.
Verify: does this give uniform mode excitation or preferential first-mode
excitation? Answer depends on eigenvector structure.

### 1.3 Matrix Form

In vector form u = (u_1, ..., u_N)^T:

```
M · ü = -K · u - C · u̇ + f(t)
```

where:
- M = diag(m_1, ..., m_N)             [mass matrix]
- K = tridiagonal stiffness matrix:
    K_{ii}   = k_i + k_{i+1}
    K_{i,i+1} = K_{i+1,i} = -k_{i+1}
  (with k_{N+1} = 0 for free end)
- C = γ · I                            [proportional damping]
- f(t) = M · (A · Ω² · sin(Ω·t)) · 1  [forcing vector, 1 = ones vector]

### 1.4 Normal Mode Decomposition

Undamped eigenvalue problem:

```
K · v_j = ω_j² · M · v_j,   j = 1..N
```

Yields N eigenfrequencies ω_1 < ω_2 < ... < ω_N and eigenvectors V = [v_1,...,v_N].

Modal coordinates: u = V · q, giving N decoupled equations (for light damping):

```
q̈_j + 2ζ_j·ω_j·q̇_j + ω_j²·q_j = f_j(t)
```

where f_j = v_j^T · M · f(t) / (v_j^T · M · v_j) is the modal forcing amplitude.

**Key result:** f_j ∝ A · Ω² · (v_j^T · M · 1) — the forcing amplitude for
mode j depends on how well the eigenvector v_j overlaps with the uniform
forcing pattern M·1.

[CHECK-2] For equal masses m_i = m, M·1 = m·1. The modal forcing amplitude
becomes f_j ∝ A · Ω² · m · (v_j^T · 1) — proportional to the sum of
eigenvector components. For a chain, v_1 has all positive components
(in-phase mode), so v_1^T·1 is large. Higher modes have alternating signs,
so v_j^T·1 → 0 for large j. This means the forcing preferentially excites
the first (lowest) mode. [CHECK: verify this for N=2,3,5 explicitly]

**Consequence for scope design:** If CHECK-2 is confirmed, the pivot forcing
primarily excites mode 1. Latent regime formation in higher modes requires
either (a) nonlinear mode coupling (energy transfer from mode 1 to mode j
via internal resonance), or (b) Ω near 2ω_j/n for direct parametric
excitation of mode j.

This is a critical finding for P2 (latent regime hypothesis): latent
higher-mode regimes may require specific Ω values, not just high A.

---

## 2. Parametric Resonance Structure

### 2.1 Mathieu Equation per Mode

In the absence of nonlinear coupling, each modal coordinate satisfies:

```
q̈_j + 2ζ_j·ω_j·q̇_j + ω_j²·q_j = f_j · sin(Ω·t)
```

This is a **driven** harmonic oscillator, not a Mathieu equation.

[CHECK-3] IMPORTANT: The standard parametric pendulum (pivot excitation of
a rigid pendulum) produces a Mathieu equation because the restoring force
is gravity·sin(θ), which gets modulated by the pivot acceleration. For a
spring-mass chain, the restoring force is the spring force k·u — it does
NOT depend on pivot position. The pivot acceleration appears only as an
inertial forcing term, not as a parameter modulation.

**Consequence:** This system is a **directly forced** chain, not a
parametrically excited one. The instability structure is resonance-based
(Ω ≈ ω_j for direct resonance) rather than Mathieu tongue-based
(Ω ≈ 2ω_j for parametric resonance).

[CHECK-3 resolution options:]
  (a) Accept: system is directly forced → resonance at Ω = ω_j,
      instability at large A due to nonlinear effects. Simpler physics,
      still produces regime structure.
  (b) Modify system: replace spring-mass chain with rigid pendulum chain
      (gravitational restoring force) → true parametric excitation,
      Mathieu tongues. Original design intent.
  (c) Hybrid: spring-mass chain with gravity as additional restoring force
      (pendulum-spring) → both effects present, more complex.

**This is the primary physics question to resolve before writing ScopeSpec v3.**

### 2.2 Resonance Structure (if CHECK-3a accepted)

For the directly forced spring-mass chain:

Primary resonances: Ω = ω_j for each mode j → amplitude diverges without damping
Sub/super-harmonic resonances: Ω = ω_j/n or n·ω_j for nonlinear systems

For N modes, there are N primary resonance frequencies in Ω-space.
The (A, Ω) parameter plane will show:
- N vertical resonance bands at Ω = ω_j
- Bandwidth of each band: ~2ζ_j·ω_j (proportional to damping)
- Band overlap when ω_j - ω_{j+1} < 2ζ_j·ω_j (dense spectrum)

### 2.3 Eigenfrequency Spacing for Equal Springs and Masses

For k_i = k, m_i = m (uniform chain), the eigenfrequencies are:

```
ω_j = 2·√(k/m) · sin(j·π / (2(N+1))),   j = 1..N
```

For N=5:
```
ω_1 = 2√(k/m)·sin(π/12)  ≈ 0.518·√(k/m)
ω_2 = 2√(k/m)·sin(2π/12) ≈ 1.000·√(k/m)
ω_3 = 2√(k/m)·sin(3π/12) ≈ 1.414·√(k/m)
ω_4 = 2√(k/m)·sin(4π/12) ≈ 1.732·√(k/m)
ω_5 = 2√(k/m)·sin(5π/12) ≈ 1.932·√(k/m)
```

The modes are **not equally spaced** — they cluster near ω_max = 2√(k/m).
This means resonance bands in Ω-space are denser at high Ω.

[CHECK-4] For N=1 (single spring-mass): only one mode at ω_1 = √(k/m).
The (A, Ω) plane has a single resonance band. This is the baseline case
and should be simulated first to verify the observable pipeline before
extending to N>1.

---

## 3. Observable Consistency

### 3.1 π_micro — Modal Energy Distribution

```
E_j(t) = ½·(q̇_j² + ω_j²·q_j²)       [energy in mode j]
E_total(t) = Σ_j E_j(t)

π_micro(b) = { E_j(t) / E_total(t) }_{j=1..N}   [vector observable]
           OR
             E_1(t) / E_total(t)                  [scalar: first-mode fraction]
```

**[CHECK-5] Vector vs. scalar:**
The full distribution {E_j/E_total} is a vector of length N. For ARW cover
construction, we need a scalar observable. Options:

  (a) Scalar: E_1/E_total — fraction in first mode. Range [0,1].
      Loses information about which higher mode is active.
  (b) Scalar: Shannon entropy H = -Σ_j (E_j/E_total)·log(E_j/E_total).
      Range [0, log(N)]. Maximum when energy equally distributed across modes.
      Minimum (0) when all energy in one mode.
  (c) Scalar: dominant mode index = argmax_j E_j. Discrete — not suitable
      for continuous cover construction.
  (d) Vector observable with multi-dimensional cover. Not yet in ARW pipeline.

**Recommendation:** Use (b) — modal entropy H. It is:
  - Scalar → compatible with existing cover pipeline
  - Monotone in modal delocalization → captures regime transitions cleanly
  - Maximum sensitivity near equal energy distribution → good for detecting
    the transition from first-mode dominance to multi-mode excitation
  - F-gradient risk at mode-crossing points (where H changes rapidly)

### 3.2 π_meso — Center of Mass Variance

```
z_COM(t) = (Σ_i m_i · z_i(t)) / M_total

π_meso(b) = Var_t[ z_COM(t) ]   over stationary window
```

**Substrate check:**
- A0–A4: z_COM always computable, finite variance for bounded forcing ✓
- A5: stationary after transient decay (γ > 0 ensures this) ✓
- A6: stationarity holds when Ω is not exactly at resonance;
      AT resonance: amplitude may grow without bound if γ = 0.
      With γ > 0: bounded amplitude at resonance, stationarity holds ✓

**[CHECK-6]** At exact resonance Ω = ω_j with light damping γ small:
the steady-state amplitude is A·Ω²/(2ζ_j·ω_j²) — large but finite.
z_COM variance will be large near resonance. This is the expected
regime signal, not a substrate failure. Confirm: σ_Δ at resonance
may exceed ε (F-gradient), but R(π_meso) is not violated.

### 3.3 π_macro — End Mass Variance

```
π_macro(b) = Var_t[ z_N(t) ]   over stationary window
```

**Structure-preservation argument:**
z_N = z_COM + (z_N - z_COM). The difference (z_N - z_COM) is the
displacement of the end mass relative to the center of mass — this
captures internal chain deformation. Two configurations with identical
z_COM trajectory but different internal deformation will have different
z_N trajectories. Therefore:

π_macro IS sensitive to some internal structure (unlike the rigid-body
end-effector case). This weakens the original macro-blindness argument.

**[CHECK-7] Is π_macro genuinely macro-blind for this system?**

For the spring-mass chain, z_N in modal coordinates:

```
z_N(t) = Σ_j v_j[N] · q_j(t)
```

where v_j[N] is the N-th component of eigenvector j.

Var_t[z_N] = Σ_j (v_j[N])² · Var_t[q_j] + cross terms (small for
             distinct frequencies)

This means π_macro IS sensitive to all modes, weighted by (v_j[N])².
For a chain hanging from above: v_j[N] (end mass component) tends to be
largest for j=1 (first mode, all masses move together) and decreases for
higher modes. So π_macro is dominated by mode 1, with decreasing
sensitivity to higher modes.

The observable hierarchy holds approximately:
  - π_macro dominated by mode 1 (v_1[N] large)
  - π_meso weighted by all modes via mass weighting
  - π_micro resolves all modes directly

But π_macro is NOT completely blind to higher modes — it has partial
sensitivity. This should be documented in the ScopeSpec as a quantitative
claim: π_macro sensitivity to mode j scales as (v_j[N])².

---

## 4. BC Class Consistency

The sweep is over (A, Ω) — two parameters.

A (forcing amplitude): **Restriction** — A controls the energy envelope
injected into the system. Higher A → larger accessible phase space volume.

Ω (forcing frequency): **Forcing** — Ω selects which modes receive energy
preferentially. It does not restrict the phase space but modulates the
energy injection pattern.

**Primary BC class: Forcing + Restriction**
This is consistent with the ScopeSpec v2 assignment. No change needed.

**[CHECK-8] Are A and Ω truly independent BC axes?**
Near resonance (Ω ≈ ω_j), the effective energy injection is
A·Ω²/(2ζ_j·ω_j) — it depends on both A and Ω jointly.
The regime boundaries in (A, Ω) space are therefore NOT axis-parallel:
a low A near resonance can inject as much energy as a high A off-resonance.

This means the (A, Ω) cover structure will have **non-axis-parallel
boundaries** — analogous to the diagonal boundary in CASE-0002.
This is expected and is an ARW positive finding, not a problem.

---

## 5. Δ Consistency

Δ = small perturbations to initial displacements u_i(0) and velocities u̇_i(0).

```
Δ = { δ : ||δu_i(0)|| ≤ r_u,  ||δu̇_i(0)|| ≤ r_v,  for all i }
```

**[CHECK-9]** For the directly forced system, initial conditions determine
the transient behavior but not the steady-state amplitude (which is set by
A, Ω, γ). Therefore:
  - σ_Δ for stationary-window observables should be small in stable regimes
  - σ_Δ large only near resonance (where transient decay is slow, γ small)
  - σ_Δ large if T_sim is too short (transient not fully decayed)

This means T_sim must satisfy: T_sim >> 1/(ζ_j·ω_j) for all j.
For γ = 0.05 and ω_1 ≈ 0.5: T_sim >> 40 time units.
Recommended: T_sim = 200 (5× safety factor), T_transient = 100.

---

## 6. Summary of Open Checks

| ID | Question | Blocking? | Resolution |
|---|---|---|---|
| CHECK-1 | Forcing projects onto modes — uniform or preferential? | No | Verify analytically for N=2,3,5 |
| CHECK-2 | First mode preferentially excited for equal masses? | No | Verify v_j^T·1 for N=5 |
| **CHECK-3** | **Spring-mass chain: direct forcing, not parametric** | **YES** | Choose option a/b/c before ScopeSpec v3 |
| CHECK-4 | N=1 as baseline case | No | Simulate first |
| CHECK-5 | π_micro scalar definition: entropy H recommended | No | Confirm choice |
| CHECK-6 | π_meso substrate at resonance: bounded, no F0 | No | Confirm with γ>0 |
| CHECK-7 | π_macro partial sensitivity to higher modes | No | Quantify (v_j[N])² weighting |
| CHECK-8 | Non-axis-parallel regime boundaries in (A,Ω) | No | Expected positive finding |
| CHECK-9 | T_sim >> 1/(ζ·ω): T_sim=200 recommended | No | Set in BCManifest |

**CHECK-3 is the only blocking item.**

The physics question: is the intended system a directly forced spring-mass
chain (resonance-based regime structure) or a parametrically excited system
(Mathieu-tongue-based regime structure)?

Both are scientifically valid. They produce different regime structures
in (A, Ω) space and test different aspects of the multi-scale observable
theory. The choice determines the ScopeSpec v3 content.
