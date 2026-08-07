---
status: working-definition
layer: docs/notes/
---

# Research Journal

Ongoing notes on theoretical developments, experimental decisions, and open threads.

---

## Format

Entries are informal and undated — this is a working document, not a log.
For resolved questions, see [open_questions.md](open_questions.md).
For formal documents, see the relevant folder in docs/.

---

## Current Focus

- BC taxonomy formalization (boundary_condition_classes.md now complete)
- Distortion metric calibration: which experimental system gives cleanest TBS(N) scaling?
- ε–Δ consistency condition: need a concrete procedure for empirical ε estimation
- Resonance: needs formal treatment — currently used informally in context_navigation documents

---

## Session 2026-03-12: CASE-0002 Repair + Cross-System Transfer

### Observable-Insuffizienz ≠ Scope-Falsifikation

Konzeptuelle Trennung bestätigt und operationalisiert:

- **Observable-Insuffizienz** (`span(π_i) < 2ε`): Observable wird ersetzt, nicht der Scope.
  Falsifikation bleibt auf BC-Ebene. CASE-0002: lambda_proxy (span=0.037) insuffizient;
  var_rel (span=0.274) tritt als primary ein. Scope bleibt valide.
- **Scope-Rejection** (`severity: scope_rejection`): Nur wenn die BC keinerlei Partition
  erzeugt — alle Observablen unzureichend, oder kein stabiles ε-Plateau.
- **sweep_refinement** (`severity: sweep_refinement`): θ* an Sweep-Grenze oder
  Sweep zu dünn — kein Scope-Problem, sondern Messproblem.

Diese Trennung ist jetzt in allen ScopeSpecs (v0.3) und im Schema formalisiert.

### γ-Kontaminant als BCManifest-Designlehre

CASE-0002 hatte `bc_02.sweeps: [{param: gamma, values: [0.1]}]` — γ wurde
als Sweep-Punkt mitgezogen, obwohl es fixiert sein sollte. Fix:
`sweeps: []` + `fixed_params: {gamma: 0.1}`.

**Lehre:** Parameter die in Phase 1 fixiert sind, gehören in `fixed_params`,
nicht in `sweeps`. Ein Eintrag in `sweeps` deklariert Sweep-Absicht.
Das BCManifest-Schema dokumentiert dieses Pattern jetzt explizit.

### TBS_norm — komparative Metrik für inkommensurable Achsen

`TBS_raw = |θ*_A − θ*_B|` ist sinnlos wenn die Sweep-Achsen verschiedene
Einheiten haben (κ dimensionslos vs. E in Joules).

`TBS_norm = |θ*_A / range_A − θ*_B / range_B|` normiert auf den jeweils
erkundeten BC-Raum und ist dimensionslos vergleichbar.

Befund aus CASE-0001 ↔ CASE-0003:
- TBS_raw = 2.525 (inkommensurabel)
- TBS_norm = |1.475/3.0 − 4.0/29.5| = |0.492 − 0.136| = 0.356 (moderate_shift)
- Kuramoto-Übergang bei 49% des κ-Raums, Doppelpendel-Übergang bei 14% des E-Raums

`pipeline.transfer` berechnet jetzt TBS_norm automatisch wenn `sweep_range`
in `Invariants.json` vorhanden ist. `pipeline.invariants` schreibt `sweep_range`.

### Coupling-BC-Signatur: kollektiv vs. niedrig-dimensional

Transfer CASE-0001 ↔ CASE-0002 (beide Coupling, Φ=0.675, partially_admissible):

- **Kuramoto** (N=500): scharfer Phasenübergang (spontane Symmetriebrechung, θ*/range=49%).
  Kollektives System braucht relativ mehr Kopplung für ersten Übergang.
- **Multi-Link-Pendel** (4D): gradueller Abfall der Winkelvarianz (Freiheitsgrad-Dämpfung,
  θ*/range=33%). Niedrig-dimensionales System tritt früher in koordinierte Phase ein.

Beide zeigen monotone Observable-Kurven und lineare Adjacency-Graphen.
Das ist die **Coupling-BC-Signatur**: sequentielle Partition, monotoner Observable,
linearer Adjacency-Graph. Unterschied: Schärfe des Übergangs.

### Multi-Observable-Problem — Q3 empirisch untermauert

CASE-0003 Doppelpendel: lambda_proxy und var_rel stimmen nur bei 37% der ε-Werte überein.
var_rel (span=0.297) hat 4.3× mehr Spreizung als lambda_proxy (span=0.069).
Verschiedene Observablen brauchen verschiedene εᵢ kalibriert auf ihren Wertebereich.
Ein einziges gemeinsames ε ist für Multi-Observable-Scopes unzureichend. → Q3.

### BC-Klassen-Transferstruktur — Q5 erste Datenpunkte

| Transfer | Φ | Befund |
|---|---|---|
| Coupling ↔ Coupling (CASE-0001↔0002) | 0.675 | partially_admissible; strukturelle Homologie erkennbar |
| Coupling ↔ Restriction (CASE-0001↔0003) | 0.40 / 0.95* | inadmissible bei ε-Mismatch; bei ε-Alignment highly_admissible |

*0.95 bei matched ε (beide N=4). Das bedeutet: die BC-Klassen unterscheiden sich
nicht in der *Topologie* der erzeugten Partition (beide sequentiell), sondern in
der *Position* des Übergangs im BC-Raum und der *Schärfe* des Übergangs.

## Pending Decisions

- Should ε be state-dependent or uniform? (see open_questions.md Q2)
- Merge modal_cognition and bc_taxonomy_cognitive_modes further, or keep separate?
- Does the labyrinth agent need a 5th mode (meta-mode for scope transition detection)?

## Notes on Resonance

The term "resonance" appears in several context_navigation documents and in the glossary.
Currently used informally to describe coherent coupling under compatible BCs.
The formal connection to BC coupling class needs to be made explicit.
Is resonance a special case of coupling BC, or a distinct mechanism?
Tentative answer: resonance is the *mechanism* by which coupling BC generates regime structure —
coupling constrains which frequencies/patterns can accumulate; resonance is the accumulation itself.
This needs formalization.

---

## Session 2026-03-18: Observable Decomposition

**Context:** Formalized observables as compositions of basis operations
traceable to BC classes. Conducted for: r_ss (Kuramoto), var_rel, lambda_proxy
(double pendulum), σ²(θ) (Kuramoto).

**Finding 1 — Pre-scope substrate** [claim]
Every non-trivial observable π carries a hierarchical substrate (~25 assumptions
for r_ss across levels A0–A6). Exactly one (A5.2: phase ψ discarded) is a scope decision.
All others are pre-scope. Reference: `docs/advanced/observable_decomposition.md`

**Finding 2 — Observable range R(π)** [claim]
The parameter-space subset where all substrate assumptions hold under Δ defines R(π).
Z(π) is the exclusion zone — failure of the substrate, not the scope.
```
R(r_ss)         = { κ ≪ κ_c } ∪ { κ ≫ κ_c }       Z: κ ≈ κ_c
R(var_rel)      = { E < E_diff, |Δθ| ≪ 2π }        Z: diffusion + phase wrapping
R(lambda_proxy) = { λ_true ≫ 0 } ∪ { λ_true ≪ 0 }  Z: transitions, weak chaos
R(σ²(θ))        = { σ(θ) ≪ π, P(θ) unimodal }      Z: Z_shared + wrap + multi
```
Reference: `docs/glossary/observable_range.md`

**Finding 3 — BC structure of observables** [claim]
All four observables are Restriction-dominated and blind to higher moments of P(θ,t):
r_ss = D∘R³∘A; var_rel = S∘A²∘R³; lambda_proxy = Approx∘D³∘R²; σ²(θ) = D∘A²∘R³.

**Finding 4 — S¹ embedding as two-layer structure** [interpretation]
φ: R → R/2πZ carries a topological layer (winding numbers as latent DOF) and an algebraic
layer (group structure). Both are meta-assumptions about X, prior to scope. (→ Q_NEW_1)

**Finding 5 — lambda_proxy structurally insufficient by construction** [claim]
A6.1 and A6.2 are violated by construction. Explains empirical insufficiency in CASE-0002/0003
from first principles, not just data.

**Finding 6 — F0 as new falsification category** [hypothesis]
F0: R(π) ∩ B ≠ B, severity: observable_replacement. Distinct from F1 (span) and scope
rejection (F2–F4). Not yet integrated into the formal falsification schema. (→ Q_NEW_2)

**Finding 7 — Z_shared as dynamic universal zone** [claim]
∀ π ∈ E: Z(π) ⊇ Z_shared. No scope with π ∈ E can have κ_c in its observable range.
Reference: `docs/advanced/observable_consequences.md` — K1

**Finding 8 — Phase transition κ_c is a scope transition, not a regime boundary** [interpretation]
θ* ≈ 1.475 (CASE-0001) is more precisely a scope transition (observable leaves R(π)) than
a regime boundary. CASE-0001 remains valid; framework needs formal distinction. (→ Q_NEW_10)

**Finding 9 — Φ measures observable transfer, not system transfer** [claim]
Φ = f(S_A, S_B), not f(System_A, System_B). Transfer reports should document observable BC
structures of both scopes. Reference: `docs/advanced/observable_consequences.md` — K4

**Finding 10 — Fluctuation observables as structural solution** [hypothesis]
χ = ∂r_ss/∂κ diverges at κ_c rather than collapsing — R(χ) ∋ κ_c. First candidate of a new
observable class suited for phase transitions. High priority as CASE-0001 extension. (→ Q_NEW_12)

Open questions raised in this session: see Q_NEW_1–12 in `docs/notes/open_questions.md`.

---

## Session 2026-03-27: 2D BC Sweep and Observable-Space Cover Height

**Context:** Kuramoto model (CASE-20260311-0001 lineage). New simulations in
`Simulationen/` sweep two boundary conditions simultaneously (κ, σ) and introduce
a novel method for visualizing scope granularity: observable-space interval covers.

---

### Finding 1 — 2D BC sweep reveals diagonal regime boundary [claim]

A full (κ × σ) sweep was conducted: κ ∈ [0, 3] (40 points), σ ∈ [0.4, 2.0]
(28 points), N = 400 oscillators, T = 150.0, observable = r_ss (mean of final 20%).
Total: 1120 simulation points.

The observable field shows a clean diagonal regime boundary consistent with the
analytical Kuramoto result κ_c = 2σ. The incoherent regime (r_ss ≈ 0) occupies
the upper-left, the synchronized regime (r_ss → 1) the lower-right.

Reference figure: `figures/kuramoto_2d_observable_heatmap.png`

---

### Finding 2 — BC-space interval covers are uninformative on uniform grids [claim]

Interval covers were first constructed along each BC axis independently (as in
`cover_bc_intervals_weighted.py`). The epsilon range was set to [Δb/10, Δb]
(sub-grid). This produced < 5% variation in weighted cover height across all
1120 points.

Extending the range to [Δb/10, BC_span] (four decades, log-spaced) yielded 0.0%
variation. Root cause: a perfectly uniform BC grid gives all points identical
cover membership at every epsilon. BC-space covers carry no structural information
about the observable field when the BC sampling is uniform.

**Methodological implication:** Cover structures meaningful for regime analysis
must be constructed in observable space, not BC space, when the BC grid is uniform.

---

### Finding 3 — Observable-space cover height as ε-marginalisation [claim]

A new method was developed: all points are sorted by their r_ss value. For each ε
in a log-spaced range [Δr/10, r_span] (200 steps), consecutive points whose r_ss
values differ by at most ε are grouped into maximal interval covers. Each point
accumulates weighted height = Σ (member_count − 1) over all covers and all ε levels.

Result: 57% dynamic range (min = 62299, max = 117322, mean = 96527, std = 18217).

This is an ε-marginalisation: instead of committing to a single ε, the height
integrates partition structure across all scales simultaneously.

Reference figure: `figures/obs_space_cover_height_panel.png`
Reference doc: `docs/advanced/observable_space_cover_height.md`

---

### Finding 4 — Cover height maps regime depth, not regime identity [interpretation]

When mapped back to (κ, σ) space, the observable-space cover height shows:

- HIGH height → incoherent regime (r_ss ≈ 0): many BC points produce nearly
  identical observable values → large, dense covers → high accumulated weight.
- LOW height → synchronized regime (r_ss varying 0.5–0.99): observable is more
  spread in value → smaller covers → lower weight.
- INTERMEDIATE → transition zone: r_ss changes steeply → each point isolated
  in observable space → minimum cover size.

The height contour lines run approximately parallel to the regime boundary
(κ = 2σ diagonal), confirming that height encodes distance from the transition,
not partition identity.

Reference figures: `figures/obs_height_overlay.png`, `figures/obs_space_cover_height_panel.png`

---

### Finding 5 — Motivation: scope granularity and invisible regimes [interpretation]

The observable-space cover height was designed to make scope granularity
operationally visible and to expose regimes that would be missed by a
single-ε partition. A regime existing only within a narrow ε-window would
produce a local height elevation even if no fixed-ε sweep detects a stable plateau.

The method makes ε a dependent variable (integrated over) rather than a free
parameter to be set. This is complementary to, not a replacement of, the
ARW ε-sweep pipeline.

Open question: whether cover-height maxima correspond systematically to
stable ε-plateaus in N(ε) — see Q_NEW_13 in `docs/notes/open_questions.md`.

---

### Finding 6 — Visualization: z-score normalization required [claim]

Raw and min-subtracted height plots of BC-space covers showed apparent structure
but with only 2–4% variation compressed by a large DC offset. Z-score normalization
((h − mean)/std) is required to make structural differences visible. This applies
to any height field with a large baseline relative to its variation.

Reference figure: `figures/cover_height_contrast_panel.png`
Reference script: `Simulationen/height_contrast.py`


---

## Session 2026-03-28: Cover Height Applied to All Active Cases

**Context:** Extension of the observable-space cover height method
(session 2026-03-27) to all four ARW cases with raw sweep data.
Central hypothesis tested: do sufficient observables show higher cover-height
dynamic range (DR) than insufficient observables?

Reference figures:
- `figures/cover_height_all_cases.png`
- `figures/cover_height_dr_comparison.png`

Implementation: `Simulationen/cover_multi_case.py`

---

### Finding 1 — DR alone is not a reliable sufficiency indicator [claim]

Dynamic range results across cases:

| Case    | Observable   | Sufficient | DR (%) |
|---------|--------------|------------|--------|
| 0001    | r_ss         | yes        | 103.3  |
| 0002    | var_rel      | yes        |  25.5  |
| 0002    | lambda_proxy | no         |  54.6  |
| 0003    | var_rel      | yes        |  38.6  |
| 0003    | lambda_proxy | no         |  60.6  |
| 0004    | PLV          | yes        | 126.3  |
| 0004    | amp_asym     | no         |  18.4  |

In CASE-0002 and CASE-0003, the insufficient observable (lambda_proxy) has
HIGHER DR than the sufficient observable (var_rel). The hypothesis as stated
is not universally supported.

---

### Finding 2 — DR reflects the structure of observable variation, not sufficiency per se [interpretation]

Three distinct patterns emerge:

**Pattern A — High DR, smooth/step profile (r_ss, PLV):**
Observable clusters near stable values in one or more regimes; the cover-height
profile is smooth and monotone or step-like. DR is high because regime interiors
are dense in observable space. This pattern indicates true regime structure.

**Pattern B — High DR, jagged/non-monotone profile (lambda_proxy in 0002/0003):**
Observable values are scattered randomly in a narrow range with no monotone trend.
Uneven local density in observable space creates variable cover sizes, producing
high DR. This DR reflects noise/structural failure, not regime clustering.

**Pattern C — Low DR, flat profile (amp_asym in 0004):**
Observable span is near-zero. Covers are uniformly tiny. DR is low.
This pattern is consistent with F1 (insufficient span).

---

### Finding 3 — Profile shape discriminates types of insufficiency [interpretation]

The cover-height profile shape provides information beyond DR:

- Smooth/monotone profile → gradual transition, regime structure present
  (var_rel transitions smoothly from 0.31 to 0.0002 in CASE-0002)
- Step-like profile → sharp transition, clear regimes
  (r_ss in 0001, PLV in 0004)
- Jagged/non-monotone profile → noisy observable, no regime structure
  (lambda_proxy in 0002/0003, consistent with its F0 structural failure)
- Flat profile → F1 failure, span too small to resolve regimes

This suggests that the SHAPE of the cover-height profile may be diagnostic
for the TYPE of observable failure (F0 structural vs. F1 span).

---

### Finding 4 — var_rel shows low DR in CASE-0002/0003 despite being sufficient [interpretation]

var_rel in CASE-0002 decreases monotonically from 0.31 to 0.0002 across 25 BC points.
In observable space, these values are roughly uniformly spread — covers are of
similar sizes throughout, yielding flat cover-height (DR = 25.5%).

This is consistent with the ARW pipeline result: var_rel is sufficient because
its span (~0.31) exceeds ε_working = 0.023, enabling a 3-regime partition.
But the smooth gradient means there are no prominent clusters in observable space —
the "regimes" only become visible once a threshold ε is applied.

Cover-height DR and pipeline sufficiency measure different aspects:
- Pipeline sufficiency: span relative to ε, plateau stability
- Cover-height DR: density contrast in observable space (clustering vs. spread)

These are complementary, not equivalent.

---

### Finding 5 — CASE-0004 (Stuart-Landau) shows cleanest discrimination [claim]

PLV (sufficient, emergence case): DR = 126.3%.
Cover-height profile shows a step-like structure consistent with the
phase-locking transition at K* ≈ 0.055.

amp_asym (insufficient, F1): DR = 18.4%.
Values nearly constant throughout sweep (~0.08), consistent with
amp_asym being the local emergence precursor that collapses before PLV responds.

CASE-0004 provides the clearest case where DR correctly discriminates
sufficient from insufficient. This may be because the emergence window
structure creates a particularly sharp contrast in observable space.

Open question: see Q_NEW_16 in `docs/notes/open_questions.md`.

---

## Session 2026-03-28 (II): 2D BC Sweep Cover Height — CASE-0002/0003/0004

**Context:** Extended the observable-space cover height analysis from 1D BC sweeps to 2D
BC grids. Self-contained RK4 simulations (no scipy dependency) were run for three cases,
sweeping two BCs simultaneously. Cover height analysis identical to 1D method but applied
to the flattened 2D sweep data; results are then visualized as 2D scatter plots and
heatmap overlays.

**Sweep grids:**
- CASE-0002 Pendulum: κ ∈ [0, 10] (20 pts) × γ ∈ [0.02, 0.4] (15 pts) = 300 points
- CASE-0003 Doppelpendel: E ∈ [0.5, 30] (22 pts) × m₂ ∈ [0.3, 2.0] (14 pts) = 308 points
- CASE-0004 Stuart-Landau: K ∈ [0.005, 0.15] (18 pts) × λ ∈ [0.3, 1.5] (14 pts) = 252 points

---

### Finding 1 — 2D cover height confirms CASE-0004 discrimination [claim]

DR results from 2D sweeps:

| Case       | Observable     | Class | DR (2D) | DR (1D, prev.) |
|------------|----------------|-------|---------|-----------------|
| CASE-0002  | var_rel        | S     | 11.9%   | 25.5%           |
| CASE-0002  | lambda_proxy   | I     | 17.5%   | 55.3%           |
| CASE-0003  | var_rel        | S     | 23.3%   | ~20%            |
| CASE-0003  | lambda_proxy   | I     | 89.3%   | ~89%            |
| CASE-0004  | PLV            | S     | 136.1%  | 126.3%          |
| CASE-0004  | amp_asym       | I     | 14.2%   | 18.4%           |

CASE-0004 remains the clearest discriminator: PLV DR (136%) vs. amp_asym DR (14%),
a 10× ratio. The 2D sweep confirms the 1D result with higher BC-space coverage.

---

### Finding 2 — 2D cover height reveals spatial structure the 1D sweep cannot [observation]

In the 2D setting, the height field h(BC₁, BC₂) is a 2D surface rather than a
1D profile. This exposes regime boundaries as 2D curves in (BC₁, BC₂) space.

Key observations from overlays:

**CASE-0002 var_rel:** The cover-height z-score shows a smooth gradient across
the κ-γ plane. The transition boundary is approximately diagonal — higher damping γ
requires higher coupling κ to maintain coordinated motion. The 2D overlay reveals
this coupling between the two BCs, invisible in either 1D sweep alone.

**CASE-0003 var_rel:** The low-energy region (E < 5 J) shows high cover height
(deep regime interior), transitioning sharply to the diffusion-dominated regime
at higher E. The m₂ axis has weaker influence, confirming that E is the primary BC.

**CASE-0004 PLV:** The phase-locking transition appears as a curved boundary in
(K, λ) space. Higher λ requires higher K for synchronization — consistent with the
Stuart-Landau analytical prediction K_c ≈ λ. The 2D cover height maps this
transition boundary more precisely than the 1D K-sweep.

**CASE-0004 amp_asym:** Flat cover height throughout the (K, λ) plane, confirming
F1 failure (span near-zero) regardless of which BC combination is probed.

---

### Finding 3 — CASE-0003 lambda_proxy anomaly persists in 2D [observation]

lambda_proxy shows DR = 89.3% in the 2D sweep, consistent with its high DR in
the 1D sweep (~89%). The 2D overlay shows the high-DR profile is structurally
different from var_rel: the height field is patchy and non-monotone rather than
smooth. This confirms the Pattern B diagnosis (F0 structural failure: noisy
observable masquerading as high-DR sufficient).

This is the most important cross-check from the 2D analysis: the two insufficient
observables (lambda_proxy and amp_asym) display opposite DR signatures (high vs. low),
but both produce structurally distinct cover-height fields relative to the sufficient
observables in the same systems. DR alone still does not discriminate; spatial profile
structure does.

---

### Finding 4 — BC interaction structure visible only in 2D [claim]

In the 2D var_rel overlay for CASE-0002, cover-height contours are not axis-aligned.
They run diagonally across the (κ, γ) plane, indicating that κ and γ interact:
the position of the regime boundary depends on both BCs jointly, not independently.

This is a structural observation that no 1D BC sweep can reveal. 2D cover height
analysis is therefore a prerequisite for detecting BC interaction effects.

**Consequence for ARW:** The scope tuple S = (B, Π, Δ, ε) should in principle
permit BC interactions within Δ. Diagonal regime boundaries are the empirical
signature of Δ being a joint condition on {BC₁, BC₂} rather than independent
conditions on each BC.

Open question: see Q_NEW_18 in `docs/notes/open_questions.md`.

---

Figures:
- `figures/cover2d_0002_varrel_panel.png` — κ×γ observable field, z-score, min-subtracted
- `figures/cover2d_0002_varrel_overlay.png` — height contours on observable heatmap
- `figures/cover2d_0002_lambdaproxy_panel.png` — λ-proxy insufficient observable 2D
- `figures/cover2d_0002_lambdaproxy_overlay.png`
- `figures/cover2d_0003_varrel_panel.png` — E×m₂ sufficient observable 2D
- `figures/cover2d_0003_varrel_overlay.png`
- `figures/cover2d_0003_lambdaproxy_panel.png` — E×m₂ insufficient observable 2D
- `figures/cover2d_0003_lambdaproxy_overlay.png`
- `figures/cover2d_0004_plv_panel.png` — K×λ PLV sufficient 2D
- `figures/cover2d_0004_plv_overlay.png`
- `figures/cover2d_0004_ampasym_panel.png` — K×λ amp_asym insufficient 2D
- `figures/cover2d_0004_ampasym_overlay.png`
- `figures/cover2d_dr_comparison.png` — cross-case DR bar chart

Implementation: `Simulationen/sweep_2d_all_cases.py` (RK4), `Simulationen/cover_2d_all_cases.py` (analysis)


---

## Session 2026-03-29: Q-CNS-06 to Q-CNS-09 — Theoretical Analysis

These questions arose from the context-navigation audit (`mode_scope_regime_audit.md`).
The entries below give the current best theoretical treatment and derive testable predictions.

---

### Q-CNS-06 — Minimal fluctuation observable for cognitive mode transitions

**Question:** What is the minimal fluctuation observable for mode transitions in the
cognitive architecture, and does it show a Z_shared peak at transition points?

**Theoretical analysis (interpretation):**

The structural analog in the physical cases is χ = ∂r_ss/∂κ at K_c (CASE-0001).
r_ss is class-E (stationary expectation); it fails at the transition (F0, R(r_ss) ∌ κ_c).
χ is class-F (fluctuation / derivative); R(χ) ∋ κ_c — precisely valid where r_ss fails.

For the cognitive architecture, mode_dist is the primary observable (class-E: stationary
expectation over mode activations within a zone). mode_dist fails at zone boundaries
(A4 violation → F0 condition). The corresponding fluctuation observable is:

```
χ_mode(p) = ∂(mode_dist_concentration) / ∂(context_load)
```

where mode_dist_concentration is a scalar measure of how peaked the mode distribution is
(e.g., 1 − H(mode_dist) / H_max, or the dominant mode's probability mass).

**Pre-scopal analysis of χ_mode:**
- Stationarity (A4): required over context_load increments Δλ — valid away from transitions
- Differentiability (A_diff): requires mode_dist to be smooth in context_load — valid in regime interiors
- Observable BC structure: Aggregation-dominated (∂ of an aggregation) with Restriction co-component → A·R

**Expected behavior (claim):**
χ_mode peaks at regime boundaries in parameter space. At the transition point, where
mode_dist has entered its exclusion zone Z(mode_dist), the fluctuation observable χ_mode
remains valid (R(χ_mode) ∋ transition) and reaches its maximum.

This is the Z_shared peak predicted by the ARW framework — the fluctuation observable's
peak coincides with the class-E observable's exclusion zone.

**Minimal operationalization:**
The simplest implementation is the **mode-switch rate** per episode, which approximates
∂(mode_distribution)/∂(episode) without requiring explicit context_load parameterization.
At regime boundaries, mode-switch rate peaks. This is already measurable in the labyrinth
experiment and requires no additional instrumentation.

**Status:** interpretation — testable via labyrinth experiment (compare mode-switch rate
profile across BC parameter sweep with mode_dist coverage height profile).

---

### Q-CNS-07 — BC class of a mode: stable under change of observation set Π?

**Question:** If the labyrinth agent is observed with different observables, does the same
behavioral mode appear to have the same BC class?

**Theoretical analysis:**

This is the cognitive instance of Q_NEW_9 (BC class: system vs. scope property).
The resolution for physical cases (K5 in `docs/advanced/observable_consequences.md`)
is that observable BC structure and system BC structure are distinct: r_ss is
Restriction-dominated regardless of the Kuramoto system it observes.

For cognitive modes: two observables are available —
- mode_dist: Aggregation-dominated (A·R) — projects mode sequence onto a distribution
- salience_mean: Restriction-dominated (R·A) — projects mode-fitness variance onto a scalar

If BC class is a sub-scope property of R_m (the revised position from the audit), then:
the BC class *as seen through mode_dist* reflects the observable's A·R structure overlaid
on the system's actual BC class. The BC class *as seen through salience_mean* reflects
R·A structure overlaid on the same system.

**Theoretical prediction (hypothesis):**
The BC class assignment will NOT be stable across observables if the two observables
have structurally different BC notations (A·R vs. R·A). The Φ_obs value between the
two scope descriptions will be < 1. In the extreme case, a Restriction-mode environment
could appear as an Aggregation-dominated BC if observed through mode_dist.

**Consequence for experimental design:**
BCManifest entries for labyrinth cases must specify both:
1. System BC class: the zone type (R / C / F as designed)
2. Observable BC class: the notation for each observable used (A·R for mode_dist, R·A for salience_mean)

The Φ_obs (observable-transfer) experiment in transfer_semantics §2.2 is the direct
empirical test: compute Φ between S_1=(B, {mode_dist}, Δ, ε_1) and S_2=(B, {salience_mean}, Δ, ε_2)
on the same labyrinth. A low Φ_obs confirms BC-class instability under Π change.

**Status:** hypothesis — testable by transfer experiment type §2.2 (same system, different observables).

---

### Q-CNS-08 — Empirical signature: scope transition vs. regime transition in behavioral data

**Question:** How do we distinguish a scope transition (S_global failure) from a regime
transition (mode switch) in the behavioral data of a context-navigation agent?

**Theoretical analysis:**

From the audit, the formal distinction is:
- Regime transition: agent moves between R_i and R_j within S_global; partition updated, not replaced
- Scope transition: S_global loses validity; all π ∈ Π enter Z(π); descriptive framework fails

This translates to the following behavioral signatures (interpretation):

| Feature | Regime transition | Scope transition |
|---|---|---|
| Observables affected | Mode-specific (Π_m of old mode enters Z) | All observables simultaneously anomalous |
| Duration | Transient — new mode emerges | Sustained — no stable mode found |
| Salience pattern | Peak then decline to new stable level | Elevated plateau; does not decline |
| mode_dist shape | Shifts to new dominant mode | Becomes flat or unstable |
| Task performance | Dips then recovers in new mode | Collapses; no recovery via mode switch |
| Anchor activation | New anchors found (new zone) | No anchors match; full exploratory mode |

**Formal discrimination criterion (claim):**

Let T_stable be the time to re-stabilize mode_dist after an event (salience spike or mode switch).
Let σ_mode be the variance of mode_dist over T_stable.

```
Regime transition:   T_stable < T_consolidation  AND  σ_mode → 0 (converges to new mode)
Scope transition:    T_stable ~ T_consolidation  OR   σ_mode ≁ 0 (does not converge)
```

In words: if the agent finds a new stable mode within one consolidation interval,
the event was a regime transition. If the agent fails to stabilize within a consolidation
interval, the event was a scope transition — the current S_global is inadequate.

**Experimental operationalization:**
This is directly testable in the labyrinth experiment by introducing:
1. Standard zone-crossing events (regime transitions by design)
2. Novel zone types that were not present during training (potential scope transitions)
Category 2 should produce sustained salience elevation and T_stable > T_consolidation.

**Status:** claim with formal criterion — testable in labyrinth experiment Phase 2.

---

### Q-CNS-09 — Consolidation: asymptotic sharpening or faster mechanism?

**Question:** Does consolidation produce asymptotic partition sharpening (K6: dissipation
is a limit process), or is there a faster non-asymptotic mechanism?

**Theoretical analysis:**

The K6 finding (from `docs/advanced/observable_decomposition.md`) states that dissipation
contracts the state space toward attractors only asymptotically — projective mapping
is the limit, not a finite-step operation.

If consolidation is purely dissipative, the empirical signature must be:
- Monotone decrease in partition boundary width (ε-instability zone) over consolidation cycles
- No discontinuous jumps in partition stability after individual consolidation phases
- The convergence rate is proportional to anchor density (more anchors → faster asymptotic approach)

**The alternative hypothesis:**
If there exists a non-asymptotic (faster) mechanism — e.g., discrete winner-take-all
anchor replacement, phase-transition-like reorganization of the anchor set — the signature
would be:
- Step-like jumps in partition stability (discontinuous, not monotone)
- Stability increase concentrated at specific consolidation cycles, not distributed across all

**Testable prediction (hypothesis):**
Asymptotic consolidation predicts that the partition ε-stability metric (ε-plateau width)
increases monotonically and smoothly across consolidation cycles.
A faster mechanism predicts step-like increases.

**Operationalization:**
Measure the ε-sweep N(ε) plateau width after each consolidation cycle.
Plot plateau width as a function of consolidation cycle count.
Monotone smooth → asymptotic (K6 prediction confirmed).
Step-like → faster mechanism present.

**Practical implication:**
If consolidation is purely asymptotic, the architecture should not expect post-consolidation
improvements to be immediately visible in the next episode. Evaluation of consolidation
effects requires accumulation over multiple cycles, not single-shot testing.

**Status:** hypothesis — testable by ablation study with ε-sweep per consolidation cycle.


---

## Session 2026-03-30: Emergent Modes Experiment — Case Registration

**Case registered:** CASE-20260330-0012

**What was done:**
Registered the Emergent Modes Experiment as a formal ART case. The experiment
was previously defined in two docs-layer documents:
- `docs/context_navigation/context_navigation_emergent_modes_experiment.md` (experiment-proposal)
- `docs/context_navigation/context_navigation_scope_spec_emergent.md` (working-definition)

Today's session translated these docs into the three standard case artifacts:

| Artifact | Status | Key content |
|---|---|---|
| ScopeSpec.yaml | draft | S_emergent = (B_emergent, Π_emergent, Δ_emergent, ε_emergent); primary observable: action_dist; F0–F4 falsification conditions |
| BCManifest.yaml | draft | BC components: Restriction (primary, bc_01), Coupling (co-driver, bc_02), ε-sweep program (bc_03); transfer target: CASE-0011 |
| CaseRecord.yaml | draft | go_nogo criterion: stable ε-plateau at N >= 2 in >= 80% of training runs; emergence_docs linked; physical analogs documented |

---

### Structural decisions (claims)

**CASE-20260330-0012 is a new case strand, not Phase 2 of CASE-0011.**

Status: claim

CASE-20260329-0011 is Phase 1 of the Designed Modes Experiment (agent with prescribed
mode library M). CASE-20260330-0012 is the Emergent Modes Experiment (unstructured policy,
ARW as observation instrument). These are complementary experiments on the same environment,
not sequential phases of one experiment. The `next_phase` pointer in CASE-0011 should
eventually point to Designed Modes Phase 2 (zone switching), not to this case.

**The ε-sweep for this case is over ε, not over a physical BC parameter.**

Status: claim

All prior cases sweep a physical BC parameter (κ for Kuramoto, E for Doppelpendel, K for
Stuart-Landau). In CASE-0012, the agent is trained on a multi-zone environment; the "sweep"
is the post-hoc ε-sweep over action_dist behavioral data. The `sweep_range` in Invariants.json
will record [ε_min, ε_max], not a BC parameter range. This is a new sweep type in the
case portfolio. TBS_norm computation against physical cases is undefined; TBS can only be
computed against other labyrinth cases with the same sweep type.

**Observable BC notation for action_dist: A·R.**

Status: claim (consistent with scope spec docs)

action_dist is Aggregation-dominated (projects action sequences onto a probability vector)
with a Restriction component from the finite action space. This places it in the same
observable class as trajectory_entropy, and different from mode_dist (A·R·B, with B for
the mode library Restriction in CASE-0011).

---

### Open questions registered

| ID | Question | Status |
|---|---|---|
| Q-EMG-01 | Does the emergent partition arise gradually (asymptotic) or abruptly (phase-transition-like) during training? | open |
| Q-EMG-02 | Is the emergent partition richer than N = zone count? Could sub-zone strategies produce finer-grained clusters? | open |

These are in addition to Q-CNS-03, Q-CNS-05, Q-CNS-06, Q-CNS-08 already registered,
which this case also bears on (see CaseRecord.yaml scientific_value.open_questions).

---

### Prerequisite for execution

The case artifacts are complete. To run the experiment, the following are still needed:

1. **RL agent and labyrinth environment** — unstructured policy (no mode library),
   multi-zone labyrinth with zones R, C, F. Not yet implemented; see
   `experiments/labyrinth_experiment_agenda.md` for environment design.

2. **Behavioral adapter for the ARW pipeline** — the existing pipeline modules
   (`epsilon_sweep.py`, `extract_partition.py`, `invariants.py`) operate on numerical
   time series from physical simulations. A behavioral adapter is needed to extract
   action_dist from RL trajectory data and feed it to the pipeline in the expected format.

3. **Transfer directory** — `transfer/CASE-0011_vs_CASE-0012/` to be created when
   the partition results from both cases are available.

Status: the case is formally registered and ready for implementation.

---

## Session 2026-04-29 — Felder 2026 Integration: Foundational Layer for ARW

**Topic:** Full integration of Felder (2026), *When Does a System Have a Well-Defined
State? Cover Stability as a Necessary Condition for Observable Information* (v1 + v2)
into the ARW canon. Migration plan executed; commit preparation completed.

---

### Key findings

**Finding 1 — The paper is ARW's missing foundational layer.**
Felder (2026) proves when a descriptive setup is valid at all — the logical precondition
for ARW's regime-partition machinery. It is not a replacement but a grounding.
The migration is: four consequential corrections + five new formal concepts absorbed.

**Finding 2 — F-gradient as a new falsification category.**
CASE-0003 (conservative Doppelpendel) with observable ω(E,ω₀) reveals a secondary
instability ridge at E ≈ ω₀² (anharmonic crossover). This cannot be classified as F0
(substrate is sound; ω ∈ R(ω) at this energy) or Z_shared (no ergodicity failure at
the anharmonic crossover). It is a **descriptive crossover**: σ_Δ(x) ≫ ε due to high
|∇ω| within R(ω). New category F-gradient added to the falsification schema.
At ε = 0.05, the primary ridge (E_sep = 2ω₀²) and secondary ridge (E ≈ ω₀²) merge
into a single connected instability band (~4% of parameter window).

> **Correction (2026-06-02, P-0 bugfix — supersedes the ridge structure above):**
> E_sep was mis-hardcoded as 2ω₀² in the pipeline; under the energy convention
> E = ½θ̇² − ω₀²cosθ the separatrix is **E_sep = ω₀²**. The "secondary ridge at
> E ≈ ω₀²" **does not exist** — it was the true separatrix re-labelled under the buggy
> convention. The pendulum has a **single** F-gradient ridge, at the separatrix
> (σ_Δ ≈ 0.61, σ_Δ/ε ≈ 2.0 at ε = 0.3; field self-similar in u = E/ω₀², one energy
> scale). The F-gradient **category** introduced in this finding stands; only the
> two-ridge structure is withdrawn. See `Simulationen/bugfix_report_20260602_p0_esep.md`;
> canon corrected in `cover_stability_criterion.md` §4/§7 and `observable_range.md`.

**Finding 3 — F1 criterion is topology-dependent (correction).**
The shorthand `span(π) < 2ε → F1` is valid only when O(X_B) is a connected interval.
The general condition is ε ≥ ε*(O,X_B), where ε*(O,X_B) is the cover-collapse
threshold (topology-determined). For fragmented or multi-component observable images,
ε*(O,X) can be much smaller than ½·span. Updated in: observable_range.md, ScopeSpec.yaml,
arw_concepts.md.

**Finding 4 — σ_Δ(x) is now the canonical name for the ε–Δ consistency condition.**
Previously unnamed in ARW; now formally defined as σ_Δ(x) = sup_{δ∈Δ}|O(x+δ)−O(x)|.
The "max_{δ∈Δ}|Π(x+δ)−Π(x)| < ε" consistency condition is identical to σ_Δ(x) < ε.
ε_min = sup_{x∈bulk} σ_Δ(x) is now the formal definition of the lower bound of I_ε.

**Finding 5 — Gradient proxy in epsilon_kappa_map.py formally justified.**
Corollary 1 (Felder 2026): if O is Lipschitz with constant L and Δ is norm-bounded
by r, then σ_Δ(x) ≤ L·r. For smooth O, L(x) = |∂O/∂κ| locally → the pipeline's
gradient field is the leading-order bound on σ_Δ. This closes the gap between the
heuristic and the formal stability criterion.

**Finding 6 — Q4 and the ε-information question are partially resolved.**
The observable cover C_ε is a Čech cover (studied in persistent homology).
The admissible resolution regime = the ε window where observable information exists.
The ε-information question (§8 of epsilon_and_scope_resolution.md) is resolved at
the structural level: observable information is the necessary precondition for
Shannon entropy and mutual information to be meaningful. Plateau width w(I_ε) as
a channel-capacity proxy remains open.

**Finding 7 — Multi-observable admissible regime is a region in ℝᵏ.**
Felder 2026 §8 explicitly states the generalization. ARW's component-wise I_εᵢ
(box in ε-space) is a special case assuming decoupled observables. Q3 partially resolved.

---

### Artifacts created/updated in this session

**New files (commit-ready):**
- `docs/core/cover_stability_criterion.md` — A-1 + A-6 (P1)
- `docs/glossary/perturbation_spread.md` — A-2 (P1)
- `docs/core/observable_information.md` — A-4 (P1)

**Updated files:**
- `docs/glossary/observable_range.md` — F-gradient, Z_cover, F1 topology correction (A-7, B-1)
- `docs/advanced/epsilon_and_scope_resolution.md` — formal σ_Δ naming, ε*(O,X) (A-3)
- `docs/advanced/observable_space_cover_height.md` — Felder 2026 section, promoted to working-definition (A-5)
- `schemas/ScopeSpec.yaml` — F-gradient doc, F1 topology note (B-1, B-2)
- `docs/overview/arw_concepts.md` — F-gradient category added (B-2)
- `docs/related_fields/related_fields_and_methodological_connections.md` — §8 Felder 2026 (C-1)
- `docs/notes/literature_links.md` — Felder 2026 entry (C-1)
- `docs/notes/open_questions.md` — Q3 partially resolved, Q4 partially resolved, new Q-NEW-COVER-1/2, Q-NEW-CROSS-1/2
- `docs/meta/DOC_INDEX.md` — three new entries, one status update

**Deferred (P3/P4):**
- D-1 (CASE-0001 Gaussian reference line audit), D-2 (CASE-0001-2D), D-3 (CASE-0003 ω observable),
  E-1/E-2 (stability_mask.py), F-1 (scope.md B vs. X note), F-3/F-4/F-5 — all deferred,
  no false urgency created. Action plan in Knowledgebase: paper_migration_action_plan_2026-04-29.md.
## Session 2026-05-07: Generator Admissibility Taxonomy — Full Development

### Context

Session developed a new ART-layer formalism for generator classification,
motivated by the observation that many formal systems (Hamiltonians, Lagrangians,
field equations, institutional formalisms) are generators of admissible scope
families rather than descriptions of single regime structures.

The session proceeded in four phases:
1. Inductive derivation of three collapse types from known generator classes
2. Partial formalization of Q-GEN-02 (signature inference) and Q-GEN-03
   (formal structure of G)
3. Fundamental revision: A_f(G | C) — functional admissibility as context-relative
   relation; C = (O, Δ_C, ε_C, ρ, τ, σ, κ) replacing R
4. Formal investigation of Q-EPO-02: Cover-height as compression viability proxy

---

### Finding 1 — Three generator collapse types (hypothesis)

Induced from cross-domain survey of known generator types:

| Type | Collapse location | Dominant signature | A_f/A_h boundary |
|---|---|---|---|
| I — Boundary | ∂A(G) in Λ | S1, S2, S4, S5 | Sharp |
| II — Solution Space | Interior of Λ | S3 | Interior bifurcation |
| III — Consistency | Internal to G | K ≠ ∅ | Gradual, within A_h |

Supported by structural argument and literature evidence from quadratic gravity
(Stelle 1977, Piva 2023, Edelstein et al. 2021).

---

### Finding 2 — Generator formal structure G = (Λ, Σ, φ, C) (hypothesis)

Revised from earlier G = (Λ, Σ, φ, R). R (expected regime structure) was too
narrow — C (epistemic-operational context) is the correct generalization, with
R ⊂ C.

Components:
- Λ: parametrization space (topological, not necessarily metric)
- Σ = (P, D, K): signature structure — present, dominant, conflict
- φ: Λ → (B, Π): partial instantiation — G determines domain and observable
  class; observer determines Δ and ε
- C = (O, Δ_C, ε_C, ρ, τ, σ, κ): epistemic-operational context

The partial nature of φ is constitutive: observer sovereignty over Δ and ε
is preserved.

Remaining open: formal topology conditions on Λ per collapse type; formal
definition of A_f / A_h boundary independent of specific C. (Q-GEN-03)

---

### Finding 3 — A_f(G | C): functional admissibility is context-relative (hypothesis)

A_f is not a property of G — it is a relation between G and C.

> A_f(G | C) = {λ ∈ A(G) : S = (φ(λ), Δ_C, ε_C) satisfies all seven
> criteria of C}

Seven criteria: Δ-Stability, Reproducibility, Observable Persistence, Resource
Proportionality, Predictive Closure, Compression Viability (κ), Transfer Stability.

Criterion 6 (Compression Viability) identified as the deepest: it connects
admissibility to information economy and explains persistence of formally
superseded theories (Newton in A_f under macroscopic C).

---

### Finding 4 — Science as stability filter (interpretation)

> Science is not a truth generator. It is a stability filter for description.

A(G) is context-independent — determined by generator structure alone.
A_f(G | C) is context-dependent — the selection within A(G) under operative
epistemic conditions. This is not relativism: the formal boundary A(G) is fixed;
what varies is which subset of A(G) is operationally viable.

---

### Finding 5 — Emergent degrees of freedom as new compression axes (interpretation)

Emergence = new stable compression axis entering A_f when coarser ε_C forces
aggregation and a new collective observable achieves higher κ than the
fine-grained description under C. Connects ARW scope-splitting to κ formally.
Potential bridge: Q-EPO-02.

---

### Finding 6 — Time as exceptionally stable compression axis (interpretation)

Time has high A_f stability across wide C because it is causally reproducible,
compression-viable across complexity scales, and achieves predictive closure
efficiently. Its appearance as a structural primitive is epistemic-operational,
not ontological. Connects to Lorentz reconstruction problem in QG literature.

---

### Finding 7 — Q-EPO-02 partially answered: Cover-height as κ proxy

**Status: partially answered (2026-05-07)**

**Question:** Is compression viability (κ) formally related to existing ARW
cover metrics? Is cover height the formal bridge?

**Formal investigation:**

Cover height is defined as:

  h(b_i) = Σ_ε Σ_{C ∋ b_i} (|C| - 1)

This measures cumulative group size across all ε scales — how persistently a
point is co-described with other points across resolutions.

Compression viability κ requires: a scope reduces system complexity without
losing operative coherence, stably across the operative ε range of C.

**Where the correspondence holds (locally):**

Three structural alignments confirmed:

1. Regime interior = high h = high κ: deep regime points are co-described
   with many others across many ε — maximal compression efficiency
2. Transition regions = low h = low κ: near ∂A(G), cover elements are small
   and ε-sensitive — compression efficiency collapses. This is Z_cover(π,ε):
   the region where Δ-stability collapses ε-dependently
3. ε-persistence = compression robustness: h aggregates over all ε, measuring
   robustness of compression under resolution variation — exactly what κ requires

**Local proxy (confirmed):**

  κ_local(b_i) ≈ h_norm(b_i) = h(b_i) / h_max

This is immediately computable via the existing ARW pipeline (cover_observable_space.py).

**Where the correspondence requires extension (globally):**

h(b_i) measures compression within a single scope S. κ as an A_f criterion
applies across the generator family {S_i}. The global bridge requires:

  κ(G, C) ≈ E_λ[h_norm(φ(λ))]

— the expectation of normalized cover height over all λ ∈ A(G), weighted by C.
This is a new pipeline requirement: aggregation of h_norm across the scope family.

**Result table:**

| Level | Correspondence | Status |
|---|---|---|
| Local (single scope) | h_norm(b_i) ∝ κ_local | Formally grounded |
| Global (generator family) | κ(G,C) ≈ E_λ[h_norm] | Hypothesis, not proven |
| Operationalization | h_norm as κ-proxy | Immediately available |

**Remaining open:** Formal proof of global correspondence; pipeline implementation
for cross-scope h_norm aggregation; conditions under which h_norm is a tight vs.
loose proxy for κ (monotone vs. non-monotone observables).

---

### Structural homologies with quadratic gravity literature (note)

The session identified structural parallels between ARW/ART concepts and
problems in the quadratic gravity literature — documented in
`example_unification_theories_as_generators.md`. These are structural
homologies, not physical confirmations.

---

### Documents produced this session

- `docs/art_instantiations/generator_admissibility_taxonomy.md`
  (hypothesis, revised: R → C, A_f(G|C), Q-GEN-04 added)
- `docs/art_instantiations/epistemic_context_and_functional_admissibility.md`
  (hypothesis, new: formal C, seven criteria, science as stability filter)
- `docs/art_instantiations/example_unification_theories_as_generators.md`
  (note, revised: literature anchors, structural homology section)

### Open questions registered or updated this session

- Q-GEN-01: Three-type taxonomy exhaustive? (open)
- Q-GEN-02: Signature-first for Type III (partially answered)
- Q-GEN-03: Formal topology of Λ; A_f/A_h boundary (partially answered)
- Q-GEN-04: Minimal C for non-empty A_f per collapse type (new, open)
- Q-EPO-01: Formal ordering of seven criteria (new, open)
- Q-EPO-02: Cover-height as κ proxy (partially answered — see Finding 7)
- Q-EPO-03: Relationship between C and collapse types (new, open)

---

## Session 2026-05-09: Scope failure as ontological projection

**Context:** Conversational derivation from discussion of Bell inequalities,
the 2022 Nobel Prize (Aspect, Clauser, Zeilinger), and ARW's structural role
in epistemology. Starting point: whether ARW can offer a new perspective on
the simulation thesis via Bell inequalities and temporal causality.

### Finding 1 (interpretation)

F-type failures are description-relative. The standard reaction — treating
failure patterns at admissibility boundaries as ontological claims about the
system beyond the boundary — is a projection error.

The Bell inequality case is the primary example: the violation of Bell
inequalities is an F2-failure of the LHV scope (S_LHV = bipartite system,
joint measurement outcomes, Δ_LOCC). The standard interpretation "locality
is disproven" projects beyond the admissibility boundary of S_LHV. The
F2-failure tells us that no scope of the form S_LHV produces a stable
product partition here. It does not characterise the system beyond that
boundary.

### Finding 2 (interpretation)

Implicit admissibility boundaries are the structural enabler of model
overreach. Without explicit boundary markers, scope claims accumulate
beyond their valid range. Models become larger than their actual
admissibility warrants — not through deliberate overreach, but because
there is no structural signal marking where description ends.

ARW's F-schema (F0–F4) and A_f / A_h distinction function as a projection
filter: they mark where description ends without asserting what lies beyond.
This is the minimal and most precise role of a meta-framework.

### Finding 3 (interpretation)

This is structurally distinct from epistemic ceilings
(docs/advanced/epistemic_ceilings_as_scope_saturation.md), which concern
internal cover exhaustion within a scope's admissibility region. The
projection error concerns the boundary itself: failure at ∂A(S) misread
as a positive claim about the region beyond ∂A(S).

| | Epistemic ceiling | Ontological projection |
|---|---|---|
| Location | Inside A(S) | At / beyond ∂A(S) |
| Mechanism | Cover exhausted | Failure pattern misread as external claim |
| Resolution | Scope change | Boundary identification + declared silence |

### Documents produced this session

- `docs/notes/scope_failure_and_ontological_projection.md` (note, new)

### Open questions registered this session

- Q-PROJ-01: Can failure structure at the admissibility boundary constrain
  the form of a successor scope — without projecting current scope content
  beyond the boundary? (open)

---

## Session 2026-05-10: Context Map Integration and Skill Effectiveness Evaluation

### Context

Four markdown files implementing an agent-optimised context map notation
(`<ID>: <type>∈<layer> | <relation> | <trigger→action>`) were imported from
external preparation and integrated into `docs/meta/context_map/`. The files
compress ARW scope/cover/observable objects, falsification entries (F0–F4 +
F-gradient), pipeline DAG with GUARD rules, and the full case registry into
machine-readable form intended to reduce navigation overhead for LLM agents
working in the repo.

Following integration, all four ARW skills (`arw-meta-guard`,
`arw-repo-context`, `arw-doc-consistency`, `arw-observable-analysis`) were
updated to reference the context map and packaged as `.skill` files.

An 8-scenario eval was designed and run to test whether the updates produced
correct agent behaviour. Prompts targeted known failure modes: GUARD citation
errors, falsification ID usage, BC class mapping, ε-direction for F-gradient,
and stability_mask handling.

### Corrections applied during integration

Before eval, the following errors were identified and corrected in the source files:

| File | Error | Fix |
|---|---|---|
| `context_map_transfer_emergence_cases.md` | SIR BC class listed as FORCING | Corrected to AGGREGATION (population expectation operator) |
| `context_map_transfer_emergence_cases.md` | Case IDs dated 20260429 | Corrected to 20260315 |
| `context_map_transfer_emergence_cases.md` | Missing cases 0011/0012/0013 | Added |
| `context_map_transfer_emergence_cases.md` | CASE-0003 BC class COUPLING+RESTRICTION | Corrected to RESTRICTION only |
| `context_map_pipeline.md` | `stability_mask.py` described as existing module | Marked as PLANNED (action E-1) |
| All four files | `layer: docs/index/` (non-existent directory) | Corrected to `layer: docs/meta/context_map/` |

### Eval design

Eight scenarios exercising the following dimensions:

1. GUARD rule citation (correct GUARD number for a falsification ID error)
2. Falsification ID enum completeness (F-gradient must be in the closed set)
3. F0 vs. F-gradient differential diagnosis
4. F-gradient ε-direction under descriptive crossover
5. BC class mapping from operator signature
6. Transfer distortion metric selection
7. stability_mask.py status handling
8. ¬-differential diagnosis (distinguishing adjacent F-types)

Prompts were submitted manually; responses evaluated against ground truth.

### Eval results (initial round)

| Prompt | Initial result | Primary error |
|---|---|---|
| 1 | PASS | — |
| 2 | PARTIAL | GUARD-4 cited instead of GUARD-2; F2 suggested instead of F3 |
| 3 | PASS | — |
| 4 | PARTIAL | ε-direction stated as "decrease ε" despite correct formula in same block |
| 5 | PASS | — |
| 6 | PASS | — |
| 7 | PASS | — |
| 8 | PASS | — |

### Iterative fixes and rerun results

**Round 1 fixes (context_map_falsification_bc.md):**
- Added explicit `ε-direction: ↑ INCREASE ε above sup_x(σ_Δ) | ¬decrease` field to F-gradient entry
- Added `actions_ranked_note` with primary/secondary/tertiary/last_resort labels
- Added ¬-differential notes to all F-types (F0¬F-gradient¬F1, F1¬F1_BC¬F0, etc.)

**Round 1 rerun results:**

| Prompt | Rerun result | Remaining error |
|---|---|---|
| 2 | PARTIAL+ | GUARD-4 → GUARD-2 fixed; F2 persisted |
| 4 | PARTIAL+ | stability_mask appeared in protocol; ε-direction still "decrease" |

**Root cause identified:** `arw-observable-analysis/SKILL.md` contained two
conflicting inline statements: `→ decrease ε` (line 156) and `adjust ε or L`
(line 440 diagnostic step 4). These overrode the context map entry because
they appeared closer to the agent's active reasoning context. The formula
`sup_x σ_Δ(x) < ε` was written correctly but the action instruction contradicted
it — a formula/action divergence the agent did not self-catch.

**Round 2 fixes:**
- `arw-observable-analysis/SKILL.md`: replaced both conflicting statements with
  `INCREASE ε above sup_x(σ_Δ) [¬decrease]`
- Added inline `ε-contradiction-check` at both sites:
  `if_you_wrote_decrease_ε AND sup(σ_Δ)<ε in_same_block → CONTRADICTION | correct to ε↑`
- `context_map_falsification_bc.md`: added `ε-contradiction-check` field to F-gradient entry

**Round 2 rerun results:**

| Prompt | Final result | Notes |
|---|---|---|
| 2 | PASS | GUARD-2 correct; F3 or F4 suggested (F3 is correct); context map cited for confirmation |
| 4 | PASS | ε-direction correct; agent explicitly flags "Do not decrease ε — contradiction"; ε*(O,X_B) check included |

### Finding 1 (methodology)

Formula/action divergence is a systematic LLM failure mode in technical documentation.
When a correct formula (`sup σ_Δ < ε`) and a contradicting action (`decrease ε`) appear
in the same document, agents preferentially follow the action instruction — proximity to
reasoning context dominates over logical consistency checking. The effective fix is not
to remove the formula but to add an explicit contradiction-check co-located with the action.

### Finding 2 (skill architecture)

Inline skill text overrides context map references when the skill is loaded into active
context. Updating only the context map is insufficient if the skill itself contains
conflicting statements. Both layers must be consistent. Order of authority:
`inline SKILL.md text > context map reference > general knowledge`.

### Finding 3 (eval design)

The ε-direction error (Prompt 4) was detectable only because the eval included a scenario
where ε-direction was the operative decision variable. General skill-correctness evals
that test only classification (F-type, BC class) will miss formula/action divergence errors.
Eval scenarios should include at least one prompt per quantitative decision variable
(ε, r, L, σ_Δ threshold) where the direction of adjustment is the ground truth.

### Documents produced this session

- `docs/meta/context_map/context_map_framework.md` (working-definition, new)
- `docs/meta/context_map/context_map_falsification_bc.md` (working-definition, new)
- `docs/meta/context_map/context_map_pipeline.md` (working-definition, new)
- `docs/meta/context_map/context_map_transfer_emergence_cases.md` (working-definition, new, v0.2)

### Open questions registered this session

- Q-CTX-01: Does `stability_mask_exclusion` need to be the primary action listed
  for F-gradient (before ε↑) in diagnostic workflows, or is ε↑ with a correct
  ε*(O,X_B) check operationally equivalent? Currently unresolved in eval. (open)

---

## Session 2026-06-02: Transfer-metric rigour pass + Q-REL-04 resolved

### Context

A critical re-examination of the three transfer tests (CASE-0004↔0001, CASE-0001↔0007,
and the Dissipation-Stationary↔Dissipation-Growing test) exposed defects in the transfer
metric and produced a definitive resolution of Q-REL-04. Work performed against the
external Simulationen workspace; the metric engine and pipeline fixes land in this repo.

### Transfer metric Φ — defect and fix

`pipeline/transfer.py` (v1) computed PCI as a structural proxy of regime count + adjacency
edge count; it never read the per-point regime labels in `annotated_results`. PCI was thus
collinear with RCD and SDI (whose node term is itself |N_A−N_B|), so ~90% of Φ's weight
tracked the regime count N. A new non-destructive module `pipeline/transfer_v2.py` was added:

- real overlap-based PCI from `annotated_results` on a common normalised BC axis (+ ARI);
- RCD and adjacency folded into one topology term (no triple-counting of N);
- TBS with a sweep-window-sensitivity band and an observable-intrinsic locator;
- a mechanical validator returning VOID on empty `annotated_results`, missing `sweep_range`,
  or an undocumented ε mismatch; and a TRIVIAL_PARTITION guard for N≤1.

### Finding (claim): Φ does not resolve BC-class distance

Recomputed with real overlap: same-class CASE-0004↔0001 PCI=0.659 vs cross-class
CASE-0001↔0007 PCI=0.650 — statistically tied. Decoupling controls confirm it: D-CTRL-1
(same N=2, different BC: CASE-0003↔0007) gives Φ=0.729 (not low); D-CTRL-2 (different N,
same BC: CASE-0001↔0002) shows directional containment 0.833 (admissible coarsening — the
one structural signal). The v1 "monotonic Φ ordering proves hierarchical BC-distance
resolution" is a regime-count artifact. Φ is a normalised-axis partition-overlap filter,
not a BC-class metric.

### Finding (answered): Q-REL-04 — dimension growth is a STRUCTURAL BREAK

The Dissipation-growth test's earlier Φ=1.0 ("reparametrisation, Q-REL-04 resolved") was
withdrawn: both cases had empty partitions (placeholder data), and the locked observable
`g_max_percapita` is F1-insufficient at the working ε (span 0.018 ≪ ε=0.05 → N=1). Φ cannot
answer the question (it doesn't even resolve between-class distance). Resolved instead via
the intrinsic dynamics of the closed (s,i) fraction system of the growing-population SIR:

    ds/dt = ρ(1−s) − β s i ,   di/dt = i(β s − γ_r − ρ)

Fixed-point/eigenvalue analysis: at ρ=0 a degenerate line {i=0} (no endemic state); for
0<ρ<ρ*=β−γ_r the disease-free point becomes a saddle and a NEW isolated stable endemic
attractor (s*,i*>0) appears via a transcritical bifurcation. Creating a new isolated
attractor is a topological change of the phase portrait — impossible under a reparametrisation.
Therefore dimension growth (susceptible replenishment) is a genuine BC-structural break within
the Dissipation class: the regime partition gains a regime. This is the opposite of the
withdrawn placeholder, and vindicates the camouflage analysis (the scalar observable masks
the endemic structure). Scope: this instantiation, not a universal theorem.

### Pipeline defects fixed (found while making the test runnable)

| File | Defect | Fix |
|---|---|---|
| `pipeline/extract_partition.py` | OBSERVABLE_MAP lacked `sir_growing`, `pendulum_gamma` → empty observables → no partition | added both extractors |
| `pipeline/sweep.py` | missing `__main__` sweep runner | restored (BCManifest-driven; output mirrors CASE-0007) |
| `pipeline/invariants.py` | read `_sweep_point`; extract_partition writes `sweep_point` → `sweep_range` silently None → spurious VOID | accept both keys |

### Documents

- `pipeline/transfer_v2.py`, `pipeline/extract_partition.py`, `pipeline/sweep.py`,
  `pipeline/invariants.py` (this repo)
- Full analysis + phase portrait: external Simulationen workspace
  (`transfer_test_dissipation_growth/QREL04_RESOLUTION.md`, `DECOUPLING_CONTROLS_RESULTS.md`,
  `TEST3_RESULT.md`, `protocol_deviation_log.md`)

### Open questions touched

- Q-REL-04 → **answered** (structural break, by intrinsic dynamics). Registered in
  open_questions.md this session.

---

## Session 2026-07-17: Generator failure-type rename + Q registrations (monograph Part VI revision)

**Context.** An external review of monograph Part VI (transfer chapter) was triaged in the
book workspace (`docs/notes/part_VI_revision_spec_external_review_2026-07-17.md` there).
Decisions by Rico (D1/D2/D5) executed book-side same day; this session propagates the
repo-side consequences.

### Finding 1 — Collapse-type names renamed (decision, Rico 2026-07-17)

The three generator admissibility types are renamed (numbering unchanged):

| Old | New |
|---|---|
| Type I — Boundary Collapse | Type I — Domain-Boundary Failure |
| Type II — Solution Space Collapse | Type II — Branch-Selection Failure |
| Type III — Consistency Collapse | Type III — Joint-Constraint Incompatibility |

Umbrella term: *failure type* (was *collapse type*). Rationale (claim): in Type II the
solution space grows/branches — uniqueness fails, not the space; in Type III "internally
inconsistent" overstated joint unsatisfiability under specific activations. Applied to:
`generator_admissibility_taxonomy.md` (canonical, with terminology note + old names as
one-cycle aliases), `example_unification_theories_as_generators.md`,
`epistemic_context_and_functional_admissibility.md` (Q-EPO wording),
`open_questions.md` (Q-GEN-01–04 wording), DOC_INDEX row. Historical journal/audit
entries left untouched.

### Finding 2 — Type I epistemic caveat added (working hypothesis)

Book-side Newton analysis (Part VI §6.2): the ε-independent structural boundary must be
distinguished from graded ε-dependent practical degradation, and the boundary may not be
encoded in G itself — identifiable only from the successor generator (retrospective
identifiability). Added as explicit caveat to the taxonomy doc's Type I section;
status: working hypothesis, no Q-ID yet.

### Finding 3 — ID-collision sweep result (process)

Pulse §5 claimed Q-GEN-01–04; the taxonomy doc had already assigned Q-GEN-05/06
(2026-05-30) without registering them in `open_questions.md`. Both now registered (late).
New: **Q-GEN-07** (structural sub-typing of Type II — interpretive axis vs. the Q-GEN-01
S3/S6 operator axis) and **Q-REL-08** (canonical normalization for TBS_norm; limitation
note added to `transfer_distortion_metrics.md` Metric 2). Pulse §5 prefix map is stale
(also missing Q-EXT/Q-ZOBS/Q-QSC registered 2026-07-14) — pulse refresh due.

### Documents

- `docs/art_instantiations/generator_admissibility_taxonomy.md` (rename + caveat, last_updated bumped)
- `docs/art_instantiations/example_unification_theories_as_generators.md` (rename)
- `docs/art_instantiations/epistemic_context_and_functional_admissibility.md` (rename in Q-EPO block)
- `docs/notes/open_questions.md` (Q-GEN wording; Q-GEN-05/06 late registration; Q-GEN-07, Q-REL-08 new)
- `docs/bc_taxonomy/transfer_distortion_metrics.md` (TBS_norm limitation, Q-REL-08)
- `docs/meta/DOC_INDEX.md` (taxonomy row updated)
- Book workspace: `part_VI_draft_v1.md`, `part_VII_draft_v1.md` (V4.3 weights note),
  revision spec + forward-reference ledger (see spec §7 execution log)

### Open questions touched

- Q-GEN-05, Q-GEN-06: registered late (found unregistered)
- Q-GEN-07: new, open
- Q-REL-08: new, open
- Q-REL-05 / WP-A3 framing: unchanged (external review independently endorses it)

---

## Session 2026-07-17 (2): Part VII formalisation — repo reconciliation

**Context.** Monograph Part VII went through two external review rounds and an
external revision session; the resulting text (imported to the book workspace
same day) made formal decisions the repo did not yet reflect. This session
reconciles the repo. Book-side spec:
book workspace `docs/notes/part_VII_revision_spec_external_review_2026-07-17.md` §7–8.

### Finding 1 — SDI is trivially collinear with RCD in the 1D-sweep tier (claim, constructive)

The sweep-form transition graph is forced to a path on N nodes (regimes are
contiguous runs of an ordered sweep), so GED(path(N_A), path(N_B)) is a
deterministic monotone function of |N_A − N_B|. Not empirical — by
construction. Disposition (WP-A4 amendment, recorded in the repair plan):
w₄ = 0 in Φ by default; SDI reported unnormalised as diagnostic; enable only
against an attributed transition graph or a constructed Δ-induced graph
(→ Q_NEW_25). WP-A4 acceptance criterion extended: per-metric
independent-information requirement.

### Finding 2 — d(Σ,Σ') §6 superseded (claim)

The persistence doc's compatibility degree was a similarity (1 = match)
computed only on shared classes, dropping exactly the configurations where
systems disagree. Canonical now: d_Σ = mean |Σ̄_A − Σ̄_B| over K_A ∪ K_B
(zero-extension), in [0, 1], 0 = match; peak ratio P_A^max/P_B^max as
robustness-scale check; thresholds τ_Σ + band are calibration conventions.
Also fixed: η = −log(ε/ε₀) with declared per-instantiation ε₀ (dimensionless);
Σ carried as pair (Σ̄_G, P_G^max) on observed family K_G.

### Finding 3 — Metric doc v2 sync executed

`transfer_distortion_metrics.md`: TBS notation corrected to two-step θ̂* form
(old θ*/range assumed b_min = 0; transfer_v2.py computed the correct form all
along); PCI max-overlap correspondence rule + directed-overlap-score reading +
ARI companion; SDI constructive-triviality note; Φ section rewritten to the
v2 clamped convex form with N_max, w₄ = 0 default, transfer_v2.py channel
mapping (0.55/0.25/0.20), decision-score status, three-way verdict band.

### Finding 4 — Glossary updates per monograph decisions D1/D2

`scope.md`: operative cover = ε-adjacency graph G_ε on the sampled sweep
(Čech language = continuum idealisation); regimes are sweep-path regimes;
ε*(O, **b**) sweep-relative; frozen tuple semantics untouched.
`perturbation_spread.md`: general action form σ_Δ(x) = sup d(O(T_δ x), O(x))
canonical (additive = vector-space instance, Felder 2026 unchanged as that
instance); global condition refined to bulk-sup + boundary-mass pair with
τ_∂, tied to F-gradient (crossing constitutes the event).

### Registrations

- Q_NEW_24 (severity impact/action split — schema question, deferred in VII
  V3.1), Q_NEW_25 (general admissible-transition regime construction +
  attributed transition graph). Collision check: Q_NEW_19–23 already claimed
  by admissible_resolution_lower_bound.md.
- Q-SIG prefix registered (Q-SIG-02–05, posed 2026-05-30 in the persistence
  doc, never registered — same failure mode as Q-GEN-05/06 and Q-EXT; note:
  no Q-SIG-01 exists).
- CASE-20260602-0014 CaseRecord verified: go_nogo = no_go with F1 entry and
  superseded_placeholder already recorded — book CITE and repo agree.

### Documents

- docs/bc_taxonomy/transfer_distortion_metrics.md (four sections)
- docs/advanced/bc_signature_persistence_and_dominance.md (§1 symbols, §6)
- docs/glossary/scope.md, docs/glossary/perturbation_spread.md
- docs/notes/arw_audit_repair_plan_2026-06-10.md (WP-A4 amendment)
- docs/notes/open_questions.md (Q_NEW_24/25, Q-SIG section)
- docs/meta/DOC_INDEX.md (two rows updated)

### Open questions touched

- Q_NEW_24, Q_NEW_25: new, open. Q-SIG-02–05: registered late.
- Q-REL-05 / Q-REL-08: unchanged, referenced.
- Note for next pulse refresh: §5 prefix map now needs Q-SIG, Q_NEW range
  through 25; τ-conventions (τ_θ, τ_ε, τ_∂, τ_Φ, τ_Σ, τ_β) named in VII —
  case artifacts must declare values where cited.

---

## Session 2026-07-18: Part VII round-3 revision — typing pass + repo reconciliation

**Context.** Third external review round of monograph Part VII: no architecture
objections, remaining issues are type conflicts between levels. All four
decisions (Rico) as recommended; book edits + repo reconciliation same night.
Spec: book workspace `docs/notes/part_VII_revision_spec_round3_2026-07-18.md`.

### Findings (claims unless noted)

1. **σ ≠ χ.** Observable spread σ_Δ does not imply regime-assignment change.
   New: assignment instability χ_{Δ,ε} (Def 6a) *defines* boundary states and
   the F-gradient mass (as a fraction, μ(χ=1)/μ(X_B) > τ_∂); σ demoted to
   computable proxy. χ computed nowhere → **Q_NEW_26** (implementation gap).
   Perturbation actions now typed per observable support: T_{δ,π} : U_π(X) →
   U_π(X). Repo: perturbation_spread.md updated (incl. fraction fix of the
   2026-07-17 addendum).
2. **F-schema amendments** (decision D2): F1 generalized to claim-relative
   insufficiency (ε ≥ ε* total collapse = special case, the form the pipeline
   tests); decision order revised to F0 → F4 → F1 → F3 → F2 → F-gradient
   (edge-θ* makes F2 uninterpretable before F4); F2 dual tests (Var vs range,
   not equivalent); A6 split: invalidity → F0, valid-but-unresolving → F1
   (Lyapunov stays F1, derivably insufficient). Repo: observable_range.md
   generalization note; context_map_falsification_bc.md AMENDMENT block
   (tree historical until regeneration); skills to pick up at refresh.
3. **R(π) split:** R_0 (intrinsic, pre-scopal) vs R_Δ (Δ-robust,
   scope-relative); P_B ⊆ P typing fix; R_eff = R_0 ∩ R_Δ ∩ P_B.
4. **ε* closed form:** ε*(O, **b**) = max adjacent gap; plateau sequence from
   the gap multiset; half-open plateau convention [g_(k), g_(k+1)).
5. **PCI operative form aligned:** point-weighted containment, both
   directions + strict min as scalar (transfer_v2.py had it; Def 9 and the
   metric doc now say it); Φ scalar is symmetric — containment reading lives
   in the directional pair, arrow refers to the reading.
6. **α-theorem renamed** "local sweep-cover scaling" (β > 1 branch only);
   β < 1 grid-pinning split off as a diagnostic rule (cusp signature); c_±
   coefficients and per-wing monotonicity already in from round 2.
7. Book-side: scope-variation taxonomy (V1.4; "resolution artifact" →
   resolution-induced transition), h(b) operational definition (normalised,
   ∈[0,1]), TBS single-primary-boundary validity note, N_max + active-weight
   normalisation, V4 epistemic-status box, descriptive-emergence recoverability
   wording, ART-as-architecture note, repo-language removed from visible text.

### Documents

- Book: part_VII_draft_v1.md (round-3 pass), part_VI_draft_v1.md (β ≤ 1
  lumping fix in §6.4 formula line)
- Repo: docs/glossary/perturbation_spread.md, docs/glossary/observable_range.md,
  docs/meta/context_map/context_map_falsification_bc.md (amendment),
  docs/bc_taxonomy/transfer_distortion_metrics.md (PCI alignment),
  docs/notes/open_questions.md (Q_NEW_26)

### Open questions touched

- Q_NEW_26: new (χ implementation gap). Q_NEW_24/25, Q-SIG, Q-REL-08:
  referenced, unchanged.
- Next pulse refresh additionally: F-schema amendment, Q_NEW range through 26,
  σ/χ distinction for arw-meta-guard §6 + arw-repo-context §3 + context maps.

### Addendum (2026-07-18, round 4 — three closing corrections)

Round-4 review accepted the round-3 pass (PCI/Φ, V5/V6 "gelungen") with three
remaining corrections, all executed same day:

1. **λ_T typed as its own observable.** The A6 conflict is resolved by
   typing, not by verdict: λ_T's referent is the finite-time exponent at
   declared horizon T; its A6 tests λ_T-stability (can pass) → F1 for the
   claimed structure, derivable a priori. Read as a λ_∞ estimator without a
   passing convergence test → F0. (V2.1 + V3.1 disambiguation updated.)
2. **χ sweep-form.** r_ε(T_δ x) was undefined (perturbed points need not be
   sweep nodes; r_ε exists only on nodes). Canonical: χ_{Δ,ε}(x_j) =
   1[∃δ: C_ε^δ(x_j) ≢ C_ε(x_j)] — component identity of the same node
   across unperturbed/perturbed graphs, up to boundary-sample tolerance.
   (Def 6a + perturbation_spread.md corrected.)
3. **σ→χ honesty + F-gradient ε-logic.** The σ↔χ error relation is
   uncharacterised (both directions possible; C1's one-sidedness concerns
   gradient→σ only) — folded into Q_NEW_26. "Never lower ε" reclassified as
   proxy-based pipeline convention, not a χ-theorem; ε-repairs constrained
   to the selected plateau + verified by recomputation. V1.3 lower bound
   labelled operational (σ-proxy). Context map: AMENDMENT-2026-07-18b.

Reviewer's optional Φ(S_A→S_B) notation change declined (semantics now
explicit in text; notation kept for continuity). Remaining task per
reviewer: linguistic trimming (WP-F4), not mathematics.

---

## Session 2026-07-25: Vertical Transfer — Q-STR Cluster Imported

**Context:** Two notes drafted offline (uploaded by Rico) imported as a pair:
`inductive_strengthening_cascade_closure.md` and
`scale_gap_ambiguity_audit_stability.md`. The pair arrived attached to a lay
outreach text pairing the Wirecard collapse with the Wang–Zahl Kakeya proof,
under consideration for the monograph's narrative track.

**Finding 1 — A third repair move, not currently in the framework** [claim]
ARW formalizes two responses to descriptive failure: scope reduction (shrink
obligations) and observable replacement (swap π after F0/F1). Both weaken or
change the description. The notes name a third that *strengthens* it: replace C
by C′ ⇒ C chosen so C′ reproduces itself across an ε-cascade where C does not.
Cost: higher projective load on Π_ρ at every scale. Gain: closure along the
resolution axis without per-scale re-derivation. Explicitly the inverse of scope
reduction — a framework knowing only reduction predicts the wrong repair for
cascade-closure failures.

**Finding 2 — The cluster is vertical, and is not the Φ machinery** [claim]
The ε-cascade {S_ρ = (B, Π_ρ, Δ, ρ)} varies resolution on *one* system. Existing
transfer machinery (Φ, PCI, TBS_norm, Σ) is horizontal — between systems. The
two are kept separate: Q-STR-03 asks whether cascade closure reduces to
Σ-invariance along ε, and until that is answered the Q-STR and Q-REL clusters
are not merged.

**Finding 3 — Relation to the plateau family is open, not settled** [interpretation]
The ε-cascade runs along the same axis on which V1.3 / `epsilon_and_scope_
resolution.md` define stability plateaus {I_ε^(1), …, I_ε^(k)}. Plateaus are the
*partition-level* structure of that axis; cascade closure is a *claim-level*
property of it. Neither is known to determine the other. This matters for the
monograph: the descriptive half of the Wirecard structure ("each level internally
consistent, nothing carries across the level boundary") is already covered by the
plateau family plus V1.4's resolution-induced transition; the repair half
(strengthening, audit stability) is not.

**Finding 4 — N* does not bound Amb** [claim, from import check]
The companion note conjectured that the variance-crossover machinery of
`arw_aggregation_limits_typological_observables.md` might bound the
realization-class diameter Amb. Checked on import: N* is the aggregation level at
which within- and between-class variance exchange magnitude — not a diameter. No
bound is inherited. Recorded as the open part of Q-STR-06 rather than
cross-referenced as settled.

**Finding 5 — Refusal to strengthen is a candidate signal** [hypothesis]
Because cascade closure carries real projective load, volunteering it is a costly
self-binding: it forfeits the option value of the realization class. Unexplained
refusal is then evidence the gap is load-bearing for the refusing party. Inverts
the audit posture — instead of hunting falsehood at the coarse scale (where there
is none), ask for the strengthening and read the response. Conditions under which
this separates gap-exploiters from the load-constrained: Q-STR-05.

**Registration.** Q-STR- prefix collision-grepped against `open_questions.md` and
`docs/notes/` before use — unused, no collision (contrast Q-REL-01/02, 2026-07-11).
Q-STR-01–06 registered. Both DOC_INDEX rows added. A notation guard was added to
the first note on import: its ρ is the canonical resolution threshold ε renamed
for family-index legibility, *not* a fifth scope-tuple component.

**Status discipline.** Both remain `status: note`. Q-STR-04 is stated as a
conjecture in its source and is registered as such. Wang–Zahl is a literature
anchor only (Fields Medal to Hong Wang, ICM Philadelphia, 23 July 2026; Zahl is
co-author of the proof, not co-recipient) — not an ART instantiation, no case
artifacts implied.

---

## Session 2026-07-25 (II): Resonanzdialektik Thesis — Folded In, Not Filed

**Context:** A working thesis on Resonanzdialektik as reorganization of semantic
description spaces (uploaded by Rico) assessed against the existing cluster:
conflict typology, shared-term reflex check, cross-scope causal construction,
three facilitation notes, kht_resonance_dialectic. Deliberately handled as
extensions to three existing documents rather than a new one; the name stays,
per Rico — it is established in KHT.

**Finding 1 — Most of the thesis is already covered** [claim]
The ambiguity node is the same-B/same-Π reflex check seen from the other side,
and the conflict typology already classifies the resulting disputes. What the
thesis adds at that point is a name and a *positive* reading: the existing tools
treat drift purely as a hazard to flag.

**Finding 2 — The ambiguity node is a realization class** [claim]
"Ambiguity is both precondition and problem" is not in the repo — except, as of
this morning, in `scale_gap_ambiguity_audit_stability.md`. The two are the same
formal object on different substrate: the public term is the coarse level, each
party's elaboration the fine one, and Amb is the diameter of the compatible set.
Communication works because Amb is large; it constrains nobody for the same
reason. Explication is a cascade-closed strengthening and is therefore costly.
**Consequence for the earlier note:** this makes the *legitimate-refusal* branch
of its §4 the normal case rather than the exception, which is a real constraint
on the signal reading — recorded in that note's §5 so §4 is not applied to
public language without a cost argument.

**Finding 3 — Linkage over membership does not fit the typology** [claim]
The thesis's strongest structural claim: world-models differ less in which terms
they contain than in how those terms are linked. Same B, Π, Δ, ε; no
Π-monopolization; still a disagreement. The scope tuple has no slot for
relational structure over Π, so this is invisible to a tuple-component typology
*by construction* — stronger and more checkable than "the typology is
incomplete". Registered as Q_NEW_E against Q_NEW_C; candidate homes are Σ or the
transition graph Q_NEW_25 declares missing. The cheap negative outcome
(B-conflict in disguise) is named first as the thing to test for.

**Finding 4 — Q-RD-1–4 were never registered** [observation]
Cited in the DOC_INDEX row for kht_resonance_dialectic.md since 2026-06-29 and
listed in that file's §9, but absent from open_questions.md — the same drift
already recorded for Q-SIG, Q-EXT and Q_NEW_27. Registered this session, with
Q-RD-5 added for the discursive form of the maximin criterion.

**Level discipline.** §6.3 of the KHT doc carries the thread but does not own the
domain-neutral claims: those belong to the typology note (Q_NEW_E) and the
scale-gap note (§5). Monograph: nothing added, by decision — the material is
note-grade and §9.2's five-part arc is closed.

---

## Session 2026-07-26: World-models as generator hypotheses — the stability revision

**Trigger.** Continuation of the 2026-07-25 (II) session. Rico's correction to the
linkage claim of that session: the point about world-models is that *varying basic
assumptions produce differently stable projections* — initially independent of
factual correctness. The previous framing had located the difference in what terms
*mean*; this locates it in what *stays put under perturbation*, which is machinery
the repository already has.

**Finding 1 — σ_Δ is not tuple-internal** [claim]
σ_Δ(x) = sup_{δ∈Δ} |O(x+δ) − O(x)| appears determined by (Π, Δ) and a state. That
holds only for pure state functions. The observables actually in use — r_ss,
var_rel, lambda_proxy — are steady-state or asymptotic: O is defined through the
dynamics. σ_Δ therefore requires the tuple **plus a generator**. This is the
mechanism the 2026-07-25 linkage claim was missing: two parties holding B, Π, Δ, ε
fixed and differing only in assumed dynamics obtain different σ_Δ-profiles over X_B,
hence different verdicts on which projections carry an ε-plateau, with neither
miscomputing and neither refuted at the time of dispute.

**Finding 2 — A world-model is a generator hypothesis** [claim]
Consequence of 1. The "same nodes, different topology" formulation of the previous
session is then not a primitive but the observable shadow of the generator. Made
computable as a co-stability graph over Π with edges weighted by overlap of
X_stab(π) = {x ∈ X_B : σ_Δ^π(x) < ε}. This selects the Σ candidate home over the
Q_NEW_25 transition graph, on a stronger argument than the conditional stated on
2026-07-25 ("if linkage differences are signature differences") and without routing
through S1–S5. Measurement caveat carried over: near θ* the mask must use direct σ_Δ
or the local-max Lipschitz bound, not the pointwise gradient proxy (C1/C2,
2026-06-02), or edges appear spuriously.

**Finding 3 — Misclassification, not absence** [claim]
Sharper than the 2026-07-25 statement that the typology "cannot place" such a case:
it *does* place it, wrongly and systematically, in the **Δ-conflict** row. Both types
issue the same verdict; the Δ-conflict stipulates the input, the generator conflict
hypothesises the map. So the §1 resolution column ("the genuinely normative dispute")
is wrong for the second type, which is not normative but underdetermined — decidable
by evidence, only later. Discriminator proposed: does the position commit to a
prediction an observed perturbation could contradict? Registered as **Q_NEW_F**,
separately from Q_NEW_E because it attacks an existing table row rather than the
completeness of the table.

**Finding 4 — Revised cheap negative** [observation]
The negative outcome named on 2026-07-25 was "B-conflict in disguise". The more
likely and more damaging one is **Δ-conflict in disguise**: if parties adjust
predictions post hoc, the discriminator of Finding 3 cannot be applied, the two types
are operationally identical, and Q_NEW_E and Q_NEW_F close negatively together. This
is the weakest joint in the revision and is recorded as such in both the note and the
question entries.

**Finding 5 — Q-RD-5 bundled two questions** [observation]
The maximin criterion (kht_resonance_dialectic.md §5) is ambiguous on an axis Q-RD-1
does not cover. Q-RD-1 varies the *aggregation form* (maximin vs. Nash product); the
second axis is what the minimum *ranges over* — parties (fairness reading) or their
generator hypotheses (robustness reading, Wald-type minimax under model uncertainty).
The two coincide at the individual and group levels because a facilitator supplies a
check; they come apart at the discursive level, which has none. Under the fairness
reading the discursive criterion is strategically manipulable (veto inflation, since
claimed inadmissibility is self-reported); under the robustness reading it is not,
because the min ranges over dynamics rather than people and a generator hypothesis
commits its holder to contradictable predictions. Split off as **Q-RD-6**; Q-RD-5
narrowed to the fairness axis.

**Level discipline.** The generator/co-stability reading and the Δ-conflict
discriminator are ARW-level and stay with `scope_component_conflict_typology.md`
(§8.1, Q_NEW_E/Q_NEW_F). Only the consequence for the mediation objective is
KHT-level and carries a Q-RD ID. `kht_resonance_dialectic.md` §6.3 gets a sharpening
box that points at the note rather than restating its claim.

**Status.** Argued, not tested. No case has been run with two generator variants over
a shared tuple; until one has, the co-stability graph is a construction proposal.
Monograph untouched.

---

## Session 2026-07-26 (II): To-REPO import batch — three notes, ten stale files

**Trigger.** Rico staged a To-REPO batch (15 `.md` + 1 asset) for triage. This is a
housekeeping session; no new formal claim was produced, but two structural findings
came out of the triage itself and are recorded because they are recurring.

**Triage result.** Ten of fifteen files were already in the repo, and in every
non-identical case the *repo* copy was the superset — the To-REPO copies were
leftovers from the 2026-07-11 and 2026-07-25 batches that were never cleared. One
further file (`Resonanzdialektik_Beschreibungsknoten_Arbeitsthese.md`) had been
absorbed into `kht_resonance_dialectic.md` §6.3 on 2026-07-25 with no standalone repo
file, by design, and so also had no import action. All fourteen moved to
`To-REPO/_imported/` with a reconciliation table.

**Finding 1 — the staging folder had no clear-down step** [open-question → resolved procedurally]
Prior import sessions imported *from* To-REPO but never removed what they imported, so
every subsequent session re-triaged the same files and had to re-derive that they were
stale. The `-1` duplicate pair recorded as a hazard on 2026-07-11 is a symptom of the
same thing: files accumulate in the queue and get reconstructed rather than looked up.
Fixed by convention rather than by rule: `To-REPO/_imported/` now holds processed
files with a README stating where each one's live version is. Anything left at the top
level of `To-REPO/` is by definition unprocessed.

**Finding 2 — near-collision in the Q-SL prefix** [claim]
`agent_sleep_scope.md` holds Q-SL-01–04. The note imported this session needed a sleep
series and took Q-SLP-01–03. A prefix-level grep for `Q-SL` matches both, so the two
series are not separable by the collision check the guard skill prescribes, which
greps for exact ID strings but not for prefix containment. Recorded as DOC_INDEX I-12
rather than renamed, because Q-SL-01–04 are cited elsewhere. Generalization worth
noting: the ID-collision procedure adopted 2026-07-11 catches exact reuse but not
prefix shadowing.

**Imports.**

1. `docs/context_navigation/sleep_as_perturbative_description_consolidation.md`
   [hypothesis] — sleep read as falsification rather than optimization: replay
   perturbs a stored encounter rather than reconstructing it, and consolidation
   selects on σ_Δ(D) < ε rather than on `progress_rate`. Companion to
   `agent_sleep_scope.md`, which it does not supersede. Added on import: the σ_Δ
   formalization of §4, and §9 — the two rules disagree on archetypes that are
   *effective but fragile*, which makes them experimentally separable with no new
   instrumentation. Weakest joint is Δ_replay: the criterion is only as principled as
   the internal perturbation set (Q-SLP-01).

2. `docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md`
   [note] — beauty as scope-relative compatibility between an environment and the
   descriptions an observer's active scope runs on, with the environment read as a
   constraint on Δ. Held at `note` deliberately: §9 records that the claim as stated
   is near-unfalsifiable (active scope is attributable post hoc; fluency and
   familiarity accounts are not excluded). Q-AES-01 is the gate.

3. `docs/notes/communicative_branching_points_nuclear_discourse.md` [note] —
   translated and renamed from a German session note on the Nuklearia communication
   strategy. Filed with an explicit §0 delimitation: the branching-point claim itself
   is already owned by `kht_resonance_dialectic.md` §6.3 and
   `scope_component_conflict_typology.md` §8/§8.1, and this note carries only the
   worked discursive instance, the cartography framing, the literature anchors, and
   the latent-assumption warning. Q-COM-01 is the check that would merge it back into
   §6.3 if the cartography framing turns out not to be cheaper than explication.

**Not imported.** CDS manifesto, two variants of the Veritasium-style narrative arc,
and the CDS logo moved to `To-REPO/related materials/` — outreach, not repo artifacts.
Noted there that the *substance* of the narrative arc is now carried by import 1, which
is the source of truth if the two ever disagree.

**Housekeeping.** DOC_INDEX gained three rows plus I-11 (its own closing section was
duplicated verbatim; second copy removed) and I-12 (above). Seven open questions
registered across three previously unused prefixes. No case, schema, pipeline module
or monograph content touched.

**Addendum (same session) — reconciliation with three notes imported the same day**

`communicative_branching_points_nuclear_discourse.md`,
`architectural_aesthetics_scope_dependent_description_persistence.md` and
`sleep_as_perturbative_description_consolidation.md` were imported on 2026-07-26 in
a separate pass. All three are correctly registered (DOC_INDEX rows present,
Q-COM-01/02, Q-AES-01/02, Q-SLP-01–03 all in open_questions.md, near-collision I-12
recorded for Q-SL-* vs Q-SLP-*). No repairs needed. Two things were added:

**Back-references.** The nuclear-discourse note consumes §8.1 and Q_NEW_F but the
reference was one-way. §8.1 now has a "Downstream" paragraph and Q_NEW_E/Q_NEW_F
carry "Depended on by" lines. This is the same one-way-link pattern that produced
the Q-RD registration drift; caught early here.

**Finding 6 — three independent sources of σ_Δ variation** [observation]
Read together, the three same-day notes and §8.1 make σ_Δ vary from three different
places: the admitted perturbation set (Δ — the classical route, and the one the
typology's Δ-conflict row already covers); the *environment*, which suppresses
perturbations and thereby lowers σ_Δ for the observables an active scope runs on
(aesthetics note §3); and the *generator*, through which an asymptotic observable is
defined (§8.1). Only the third is invisible to the scope tuple. Nobody had noticed
the pattern because the three notes were drafted independently. Recorded in §8.1
rather than in a new document — a fourth note on σ_Δ variation is exactly the
pile-up the DOC_INDEX exists to prevent. If Q_NEW_F is pursued, this three-way
distinction is what the Δ-conflict row will have to carry.

**Addendum 2 (same session) — scope-constructing agent architecture filed**

A session sketch proposing a context-navigation agent whose learning target is
description construction rather than action selection was mapped section by section
against the nine existing context-navigation documents before anything was written.

**Finding 7 — most of the sketch was already specified, and more operationally**
[observation]
Encounter field, weight field w with update rule and normalization, w_in/w_out as
first-class protocol fields, saliency triggers and grading, encounter protocol,
archetype library and matching, modes as reduced scopes, salience as a mode-ecology
property, three-layer memory, the labyrinth setup and its H1–H4 hypotheses — all
present, several at a higher level of operational detail than the sketch. An earlier
read in this session had called the dynamic weight field new; that was wrong
(`agent_online_scope.md` §4 specifies it).

**Finding 8 — five elements have no predecessor** [claim]
(1) Recapitulation as controlled *scope* variation, e′ = ℛ(e; δB, δΠ, δε, δw). The
existing sleep phase does not replay at all — it compares recorded protocols by
progress_rate; the new sleep note replays under δ ∈ Δ_replay but to measure σ_Δ of a
description. Neither varies the scope. (2) Mode merge/split/prune inside the
consolidation phase — `agent_sleep_scope.md` §4.3 explicitly defers exactly this to
post-hoc S_observer analysis. (3) The mode stability profile R_m(δ), which is σ_Δ one
level up from the observable. (4) Multi-agent description packages and migration —
grep confirmed zero multi-agent material anywhere in context_navigation/ or
cognitive_architecture/. (5) Functional intermediate modes m_{A/B}.

**Filing decision.** Not distributed as four extensions to existing files, which was
the anti-pile-up default, but filed as a standing alternative formulation at Rico's
direction — the reframing is held superior in its core idea, and the sketch's formal
deviations were drift errors rather than positions. The document carries the same
posture as the sleep note: alternative, not replacement, promotable only on a
discriminating experiment.

**Notation drift caught on import** [observation]
The sketch transposed Π and Δ (Π glossed as perturbations, Δ as a stability horizon)
and listed the active observable as a fifth tuple component. Both corrected and
recorded in §0.1 of the new document rather than silently fixed. Notable that the
sketch used the *correct* semantics throughout its substantive sections — only the
legend was wrong, which is how this drift survives review.

**Cross-level consequence.** §13 (multi-agent) is the first setting where the
robustness reading of the maximin criterion (Q-RD-6) and the prediction-commitment
discriminator (Q_NEW_F) become checkable, because the environment resolves a
prediction within an episode. Registered as Q-SCA-05. If the discriminator fails in
simulation it will not work in discourse — which makes the agent work a test bed for
this morning's ARW-level revision rather than a separate track.

---

## Session 2026-07-27: Scope-constructing agent — built, measured, and the gate it does not pass

**What was built** [observation]
A new agent in `Simulationen/labyrinth_scope_constructing/` (7 modules, numpy only, no
PPO), constructed from `scope_constructing_agent_architecture.md` rather than by
extending the WP1 stack. Deliberately *not* inherited from the WP1 environment: the
10-dimensional observation vector, three of whose dimensions (`d_nav`, `d_stuck`,
`d_time`) are variants of global distance-to-exit and were built to correspond to the
three prescribed modes of the earlier design. Only wall layouts and cost maps were
reused. The description layer is a pool of 109 compositions over 16 primitive channels;
which four of them a mode uses is learned.

**Salience redefined as prediction failure** [claim]
The WP1 signal measures deviation from a stored context centroid, and the agent can
drive that to zero by pulling the reference onto the observation — the degenerate
minimizer was its own coverage-failure fallback. Here the reference is a *prediction of
the next field*, which cannot be made trivially true except by predicting. The
degeneracy is closed by construction rather than by a guard rule.

**Three mechanism findings, all negative or redirecting** [observation]
(1) *Dark room.* Rewarding prediction-error reduction at the action level made the agent
predictable by becoming passive: error 0.031→0.017, switch rate 4.1→1.1, and final
distance to the exit *worsening* 17.1→21.2 over 150 episodes. Removing the term reversed
the distance trend. How well a description predicts is the description layer's business;
in the action reward it is a level confusion with a degenerate optimum.
(2) *Selection blindness.* Under a habitual-variability criterion the agent never once
selected the exit cue into any description across 200 episodes — not for lack of range
(0.82) but because the cue is near-constant most of the time, habitual spread 0.047
against 0.44 for the tactile channels. An intrinsic criterion built on habitual
variability is blind to rarely-but-decisively informative channels by construction. Same
shape of problem as Q-SLP-01: a self-confirming criterion.
(3) *Ceiling test found no ceiling.* Pinning the gradient observable into every
description — innate privilege, used as a control and not as a fix — left the goal rate
exactly where it was (0.073 → 0.073). The two mechanisms that did raise cue uptake
(adaptation, failure-recruitment) had the *worst* competence. So the cue was never the
binding constraint.

**Action-conditioned forward model — forced by the developmental staging** [claim]
Staging sensory and motor access (six cumulative stages, self-paced on description
stability) broke the earliest stage completely: with only proprioception online, every
description was forced to contain the action channels, and predicting one's own next
action means predicting one's own Q values and exploration noise. Error sat at 0.30 and
the library saturated at the mode cap inside 25 episodes. The predictor is now
conditioned on the operation taken. Notable methodologically: the defect was invisible at
full sensory access, where the tactile channels masked it.

**Value replay: approach improves, arrival does not** [observation]
A reverse value sweep over stored encounters (hippocampal replay analogue) was predicted
to move competence and did not: goal rate 0.070 → 0.067. What moved, consistently in two
seeds: near-miss rate 0.17 → 0.25, switch rate roughly halved, and the exit cue finally
entering descriptions (0 modes → 1–2) *without any change to the selection criterion* —
better value estimates lead the agent where the cue varies, so the same criterion sees it.
A 40-episode probe had appeared to double the goal rate; that was 2 versus 4 arrivals.
Recorded because the wrong reading came from an insensitive measure.

**The separation gate does not pass, and exploration does not change that** [observation]
*(Verdict withdrawn — see "Second correction: the separation measurement itself" at the
end of this entry. The ratio quoted below came from a saturated quantity; the gate is
unmeasured, not failed.)*
Heavy-tailed exploration (run-and-tumble, power-law run lengths, matched on the fraction
of steps under exploratory control) plus substrate mixing across the four base layouts.
220 episodes: ε-greedy median r = 1.010 (share r>1 = 0.625), run-and-tumble median
r = 1.006 (0.500); pass needs 1.2 and 0.70. Modes are *indifferent* to substrate.
Counting the channels behind the surviving descriptions appeared to explain why: 14 of 20
slots are proprioceptive or interoceptive. *(Withdrawn later the same session — see the
correction at the end of this entry. The count was condition-specific and the causal
attribution did not survive measurement.)* A description built on "what my body just did" predicts
equally well in all four substrates, and the selection criterion rewards predictability —
the body is the most predictable thing available. Per brief v2 §4.1 this is a design
iteration, not a result.

**Measurement defect caught and fixed** [observation]
The separation matrix was first built on mean prediction error per (mode, substrate) —
nearly circular, since prediction error is what the switch criterion selects on, so a
mode is active where it predicts well by construction. A 60-episode run duly "passed" at
median r = 2.14 with 31 modes, most long dead. Rebuilt on displacement rate, an efficacy
quantity independent of the selection criterion, counting only modes alive in the final
library. This is the same class of error as the v1 PCI defect: a metric that measures the
mechanism that produced it.

**KHT reconciliation** [interpretation]
`kht_reconciliation_scope_constructing.md`. The reason for the KHT link is *strengthened*
— the most direct contamination route (three mode-shaped distance observables) is gone.
WP3's apparatus largely does not survive: E2, the decision-relevant criterion, is not
computable, because the new agent has no weight vector and no context centroid. A1–A4
become more directly measurable and less dependent on post-hoc factor analysis; A5 and A9
move from silent to arguably reachable. And an unplanned structural correspondence: the
agent's composition operators are KHT's operators, while ε_agent, the selector and λ are
its modulators — but all three are **exogenous**, so the build runs one modulator cluster
per run and can only find operator-side structure. That is a clean structural explanation
for mode counts of 6–14 that never collapse.

**Status, stated plainly** [observation]
Under WP3's gates with substituted quantities the current data is Gate 0/1: no
low-dimensional organization demonstrated, no separation, competence flat at ~7%. The
instrument was rebuilt; there is no reading. Several sessions of mechanism findings have
not moved the existence question, and brief v2 §9 exists to make that sayable.

**Registered:** Q-PAR-01–05 (prefix was unused repo-wide). Documents imported:
`scope_constructing_agent_implementability.md`, `switch_minimization_criterion.md`,
`kht_reconciliation_scope_constructing.md`, plus
`agent_context_navigation_project_brief_v2.md` — the repo had held only the superseded v1.
WP3 deliberately not imported: its own freeze protocol makes import the act of freezing,
and it is still `frozen: false`.

**Addendum — the gate failure is a theory result, not a data result** [claim]
The separation failure was read once more and turned out to be about the framework rather
than about the agent. Counting channels: 11 of 20 description slots are held by `act_*`
and `time_left`, which cannot distinguish substrates *even in principle*. *(This count
and the causal reading built on it are withdrawn — see the correction below.)* Those
observables satisfy `observable_information.md` in full — non-trivial cover, and
σ_Δ = 0 exactly, since the perturbation channel perturbs the system and not the agent's
own record — while producing an identical image on every boundary condition. So
observable information, the necessary condition for scope validity, does not exclude the
F1_BC condition. The two are independent, and one line of construction shows it.

This cannot arise in the physical cases, where every observable is applied to the system.
It arises the moment the describing system is inside the world it describes, which is the
first structural difference between the cognitive strand and the physics cases with
consequences for the ARW apparatus rather than only for interpretation.

Generalized: a criterion evaluated on a description's *own* behaviour selects for
whatever the criterion finds easiest, and "easiest" is a property of the describing
system. Three instances now on record — Q-SLP-01 (a narrow Δ_replay makes everything
persistent), habitual variability (blind to rarely-decisive channels), and persistence
itself (selects the describing system). Filed as a class, because the fixes are not
interchangeable.

The prescriptive consequence: C-PAR is an upper bound on the failure rate and needs a
lower one, since a description that never breaks carries no partition. Two-sided form
`0 < failure rate < parsimony bound`, structurally the same as
`sup_x σ_Δ(x) < ε < ε*(O,X)`. C-PAR's own degeneracy analysis found the upper failure
mode and missed this one — it asked how the agent could cheat the count to zero, not what
happens when the count reaches zero legitimately. Registered as Q_NEW_G, the first
ARW-level question to come out of the agent strand rather than the physical cases.
Document: `observable_information_and_bc_responsiveness.md`.

**Correction to the addendum, same session** [observation]
The causal story in the addendum above did not survive measurement and is withdrawn. The
"11 of 20 slots are BC-unresponsive" figure was from a single 120-episode single-substrate
run and was presented as general. Measured across four conditions the self-directed share
is 0.20–0.58 (chance level 0.31), and in the mixed-substrate condition — the only one in
which the separation ratio means anything — descriptions are 67 % exteroceptive while
separation "fails" identically at r ≈ 1.013 — a figure later found to come from a
saturated quantity and withdrawn. What carries this correction is the self-share alone:
it is *lowest* in the condition the original claim needed it highest in.

What replaced it is better founded. Taking the 32 compositions the surviving descriptions
use and evaluating each under a fixed random walker in all four substrates: median
substrate separability |d| = 0.23, 14 of 32 below 0.2, every `DIFF` composition at
|d| ≈ 0.00–0.06 (a windowed difference under a symmetric walk carries no substrate
information at all, yet several were selected) — and `cost_here`, the most
substrate-diagnostic channel in the environment by construction, absent from every
surviving description. It is absent *because it is constant within* three of the four
substrates: its within-window spread is near zero, so every selection criterion in the
implementation discards it, while the substrate information sits in its *level*
(0.4 / 0.3 / gradient / barriers).

Generalized, and this is the finding: **a criterion computed from statistics within a
context is structurally blind to differences between contexts, because a BC difference
presents itself as a difference of levels across contexts the describing system never
sees side by side.** That is why nothing helped — heavy-tailed exploration, adaptation,
critical periods, value replay and four selection criteria are all within-window
criteria, so the five attempts were the same attempt five times.

Consequence for the proposed repair: the failure-rate floor (§7.1 of the note,
implemented as `--fail-floor`) is necessary but demonstrably not sufficient — the failing
descriptions fail at ordinary rates. The proxy the measurement calls for is a
cross-encounter *level* contrast (§7.2), which the protocol buffer already supports and
which `fit_and_score` currently precludes by evaluating every window independently.
The floor was then implemented and run (`--fail-floor 0.10`, 200 episodes, mixed
substrates): separation still fails at median r 1.029 versus 1.013 without it, the
self-directed share *rose* from 0.20 to 0.40, and the constraint rejected every proposed
variant in 335 cases and fell back to the unfiltered pool — so it was largely inoperative.
Recorded as a negative with a caveat: the fallback behaviour needs fixing before the
number means much. It is not the mechanism.

C1 (observable information does not
entail BC-responsiveness, by construction) is untouched by any of this; C2 is downgraded
to an unsupported conjecture; C3 is the measured claim.

Methodological note for the record: the wrong reading came from generalizing a channel
count taken in one condition, and it was caught only because the same count was recomputed
in the condition the gate is measured in. Both the original claim and its correction are
kept visible in the note rather than edited away.

**Second correction: the separation measurement itself, three times over** [observation]
Prompted by Rico's remark that the design of admissible trajectories may be *the* central
lever in designing a learning environment. Checking the substrates against that standard
turned into an audit of the measurement, and the audit went further than the substrates.

*The substrates.* In terms of admissible trajectories the four inherited layouts are two
kinds: corridor and halfwall make some trajectories impossible (~9 % blocked cells,
uniform cost), open and costpath make all possible but some expensive (0 % blocked,
structured cost). Within each pair the difference is quantitative. `halfwall` was a
distinct class in the old design only because it blocks *movement but not vision* — and
this agent has no vision channel, so the distinction that defined it does not exist for
it. Substrate classes inherited from an observation space that was then deleted. Grouping
the four into two moved the ratio barely (1.003 → 1.007, 1.015 → 1.073), which is what
sent the check one level deeper.

*The measurement.* Three quantities, three distinct defects. Mean prediction error is
**circular** — it is what the switch criterion selects on, so a mode is active where it
predicts well by construction. Displacement rate is **saturated** — blocked cells are only
~9 % of the grid, so mature modes sit at 0.92–0.96 everywhere, home and away, and a ratio
of two near-identical numbers is 1.0 by arithmetic. Per-step progress is at the **wrong
grain** — dominated by the long tail of milling steps; every mode averaged 0.49–0.51.

*The reading that was nearly published.* That third result invited "the agent does not
navigate at all". Checked against an actual random walker in the same four substrates
first: random reaches the exit in 0.7 % of episodes and comes within five cells in 3.0 %;
the agent manages 5.0–7.3 % and 29–36 %, closest approach 14–16 against 31.3. It navigates
about ten times better than chance. The competence was real the whole time and no
per-step quantity could see it.

*What the corrected measure shows.* At episode grain — per episode, the mode that carried
it and that episode's closest approach — the values are no longer pinned near 1.0: they
range 0.73–1.86 across three seeds, one pass and two fails, with only 2–5 modes clearing
the minimum sample out of 180 episodes. Real but badly underpowered. **No separation
verdict is claimed in either direction.** Every earlier "the gate does not pass" statement
was reading an artifact, and those statements are now marked as such wherever they appear.

*What survives independently.* C1 (a construction). The composition-separability
measurement behind C3 (Cohen's d over substrates under a fixed random walker — it never
used the gate). The channel counts. The substrate-redundancy finding above. Q_NEW_G does
not rest on the ratio.

*The pattern, recorded because it is the third time* [interpretation]
Four quantities, three defects, every one found by checking rather than by the data
announcing it — and two of the three would have been written up as findings otherwise.
The recurring error has one shape: choosing a quantity because it is *independent of the
selection criterion*, and not also checking that it has *dynamic range at the grain being
measured*. Independence and informativeness are separate properties and only the first was
ever verified. Worth adding to the pre-commit habits alongside the existing guard rules:
before a ratio is reported, state the range of its numerator and denominator.

## Session 2026-07-29: Persistence as a carried state variable — and the falsifier that fired

**Six measurement criteria retired in one week** [observation]
Separation on prediction error (circular), on displacement rate (saturated), on
per-step progress (wrong grain), the phantom→goal gradient (uncontrolled), the
one-mode "pass" (degenerate), and the absolute threshold `median r ≥ 1.2` (no valid
null — the one-description arm returns 1.55 on one layout and 0.81 on another instead
of 1.0). Replaced by a within-substrate relabelling null, which the degenerate arm
reproduces to excess 0.000 on all five seeds. Two further defects were found in
measures written during the same week: a one-sided sum of noise reported as a
transfer cost, and a rollout horizon compared against a one-step threshold.
**The recurring shape:** a criterion evaluated with the quantity its own selection
process produces. The rule adopted — every criterion ships with a null construction
and a degenerate arm on which the null must be exactly recovered.

**Absorption: why a regime difference must not be locally readable** [claim]
`two_band` distinguished its substrates by a feature. The feature was present (AUC
0.89 against a median candidate of 0.013) and selection recruited it (ranks 0 and 1 of
109). No partition formed — NMI(mode × substrate) 0.052, separation ratio at its null.
If every description can already tell the regimes apart, specialising is redundant.
A regime distinction is a scope boundary only when it cannot be read off the
description's inputs. This is the design constraint the labyrinth work bought.

**The forward map must predict the change** [claim]
With an absolute target and identity initialisation, 97.2 % of fitted weight sat in the
persistence block and 2.2 % in the action block. Such a map cannot notice a regime that
acts only on the action→effect relation: error ratio across an unannounced action
inversion 0.84–1.14. Predicting the change raised the action share 17-fold; navigation
competence collapsed in the same move, and that second effect is unexplained.

**A single-timescale self-set resolution fails** [claim]
Swept over its one free constant, the agent either invents descriptions in a world that
never changes (4.5 at the low setting) or stops noticing the real change (0 switches at
the high one). No value passes both. **Retraction:** first reported as showing a
modulator cannot be set from operator-side experience at all — too strong. What is shown
is that a *single-timescale* self-set resolution fails. The nested construction of
`conflict_navigation_nested_calibration.md` is untouched by it and is adopted.

**Three laws that do work** [claim]
Resolution profile over ε (the time-index transposition of cover height), assignment over
contiguous segments, and a gain calibrated against a stationary control condition.
Per-sample assignment gives partition agreement 0.508; from five contiguous samples,
1.000. That five equals the independently measured identifiability limit — the coherence
length the partition needs and the smallest window on which two descriptions are
distinguishable are the same quantity. A within-stream surrogate for the null does **not**
exist: permuting segments preserves the regime structure, permuting samples destroys the
state's autocorrelation with it. Temporal structure and regime structure are not
separable by permuting the stream.

**Persistence layer proposed, and its own falsifier fired** [claim]
Failure is retrospective, survival prospective. The design gives each description a
hazard estimated from its current margin (internal, enters selection) and validates it
against a rollout horizon measured on controlled material (external), with selection
made lexicographic so that survival-maximisation cannot collapse into describing
nothing — a collapse already observed in the ε arm above. The document named its own
cheapest falsifier and it was run the same day: rollout horizon 2–6 steps against an
oracle-calibrated accumulation floor, and the hazard estimate adds essentially nothing
over the present residual (partial correlation small, sign-inconsistent). The second
result is **underdetermined by the first** — a horizon ranging over 1–6 steps cannot
resolve a horizon-prediction test — and is recorded as such rather than as evidence
against the layer. Converted into a quantified requirement on the next world (Q-SCA-10).

**Open questions registered** [observation]
Q-SCA-06a/b/c, 07, 08, 09, 10, all from
`docs/cognitive_architecture/planning_admissible_scope_agent_design.md`.
Collision check run against `open_questions.md` and all of `docs/` before assignment.

**Open request** [observation]
The design's lexicographic order demotes switch minimisation to a tie-break. That is a
change to `docs/context_navigation/switch_minimization_criterion.md` and is raised for
its owner, not adopted.

---

## Session 2026-07-31: MINDS generalization — facilitation as first instantiation, not the toolkit

**MINDS reframed as a coordination protocol** [claim]
The MINDS toolkit (art-of-resonance.org, v0.8) is only superficially a facilitation
kit. Structurally it is a viability-preserving scope-navigation protocol for coupled
systems with partial descriptions: "parties" generalize to any constraint carrier
(models, datasets, services, goals, institutions, time horizons, artistic motifs).
The transferable core is the seven operations Tuning / Framing / Friction diagnosis /
Coverage / Anchor / Resolution / Synthesis, with the Synthesis Test's maximin — judge a
solution by the worst-represented necessary component, never the average — as the
distinguishing element. Registered as
`docs/notes/minds_generalization_beyond_facilitation.md` with five transfer conditions,
a negative condition (single objective + substitutable components → classical
optimization suffices), and ten candidate instantiations. The toolkit's own
architecture (generic core, domain companions kept outside it) already anticipates
this reading.

**Sharpest transfers named** [observation]
Multi-agent AI meta-controller (diagnose *why* agents fail to converge, and which kind
of cognitive work is missing, instead of voting/averaging — the four lenses read
directly as an agent ensemble) and ontology/schema merging (the purest case: MINDS
mediating descriptions, not social interests). Ecology/infrastructure transfers only
modularly — Anchor, Coverage, Synthesis, Scope survive; conversational diagnostics do
not.

**Level discipline kept** [observation]
The maximin criterion stays owned by `kht_resonance_dialectic.md`; the note only
extends its candidate reference class, which lands in Q-RD-6 territory rather than a
new criterion. Frozen scope-tuple semantics untouched.

**Open questions registered** [observation]
Q-MINDS-01–04 (meta-controller test; party-minimum vs. hypothesis-minimum for
non-human parties; non-substitutable constraint vs. preference criterion; minimal
modular kernel). Collision check run against `open_questions.md` and all of `docs/`
before assignment — prefix was free.

---

## Session 2026-08-01: Total description space D(S) — fibration reading of the cover construction

**One construction, four directions** [claim]
The repository's three separately defined ε-comparison → components constructions
(observable cover C_ε over O(X_B); ε-adjacency graph G_ε on sweep samples; cover
geometry over the resolution axis η) are instances of one construction over three
declared base spaces, with σ_Δ as the unnamed fourth (Δ-)direction. Registered as
`docs/notes/total_description_space.md`, which defines a candidate scope parameter
space P = {(B, π, Δ, ε)} with the regime structure as fiber. The Part VII V1
graph-vs-cover precision is preserved: same construction, not same object.

**Falsification categories as degeneracy types** [interpretation]
F0/F1/F-gradient/F2/F3/F4/scope-transition/Z_shared reread as the types of
non-smooth points of D(S) — fiber undefined / trivial along ε / Δ-unstable /
non-reproducible / π-family-wide degenerate / sampling artifact / B-discontinuous /
class-wide excluded region. Operational definitions untouched; completeness of the
table is Q-DSP-03.

**Limitative anchor identified** [open-question]
The ε-direction is H₀ persistence (extends the partially resolved Q4 correspondence
in `docs/core/observable_information.md`); any second direction makes D(S) a
multi-filtration, for which no complete discrete invariant exists (Carlsson &
Zomorodian, Discrete Comput. Geom. 42(1), 2009 — verified citation). If the
correspondence holds literally (Q-DSP-02), "no unconditioned global summary of a
system's description space exists" becomes theorem-backed rather than stance-backed.
Origin of session: monograph introduction promises a science of description whose
instruments the book delivers only slice-wise; the recurring cover formalism was the
visible trace of the unnamed total object.

**Registered** [observation]
Q-DSP-01–04 (prefix collision-checked, free); DOC_INDEX row added; delimited against
the semantic description-spaces cluster (Q_NEW_E/F, Q-RD-5/6). Promotion path: §7 of
the note (commutativity check + consistency check on CASE-20260311-0001/-0003 data).

---

## Session 2026-08-01 (second entry): Scope fibration — rename, morphism types, Q-DSP-01 paper part

**Rename executed after external review** [observation]
`total_description_space.md` superseded same-day by `docs/notes/scope_fibration.md`.
Reason: the old name over-promised (space of *all* descriptions); the object is the
family of scope-induced cover constructions indexed by scope parameters. "Fiber
bundle" was explicitly rejected for a substantive reason: bundles require local
triviality, and the falsification categories are precisely the obstructions to
local triviality — D(S) is informative *because* it is not a bundle.

**Four directions sharpened to four morphism types** [interpretation]
ε-coarsening (total, filtration), Δ-stability action (partial, obstruction = σ_Δ),
π-observable change (base change), B-restriction (with scope transitions as
distinguished morphisms). Consequence: a *path* in D(S) is intra-system navigation;
cross-system transfer is a *functor* D(S_A) → D(S_B). Conflating the two is exactly
the Session 2026-03-18 finding (Φ measures observable transfer, not system
transfer), now visible at the level of language. Categorical vocabulary adopted as
language only; conservativity registered as Q-DSP-05.

**Q-DSP-01 partially answered on paper** [claim]
For the ε–Δ pair: Δ always induces well-defined component maps after an ε-shift of
2σ̄ (triangle inequality) — a 2σ̄-interleaving; strict well-definedness holds iff no
pairwise increment lies in (ε − 2σ̄, ε + 2σ̄] (gap condition); commutativity is
automatic once maps are well-defined (all maps descend from the identity on the
sample index set). The gap condition is the pipeline's robust ε-plateau criterion:
**the go_nogo plateau requirement is the local-triviality condition of the
fibration in the (ε, Δ)-plane** — a geometric meaning the criterion was not
designed to have. Open part: π/B composition laws. Interleaving structure counts as
supporting evidence (not proof) for the Q-DSP-02 persistence correspondence.

**Registrations** [observation]
Q-DSP-05 registered; Q-DSP-01 → partially_answered; Q-DSP-04 reframed (composition
laws, not filter-vs-reindex); DOC_INDEX supersession chain recorded. Next gates
(scope_fibration.md §7): second reading of §5a, then the §5b data check on
CASE-20260311-0001/-0003 cover-height fields.

---

## Session 2026-08-01 (third entry): Second review round — restraint edits on scope_fibration.md

**Architectural hierarchy fixed** [observation]
New §2c fixes the dependency order once: Level 1 cover construction (fundamental,
the only computed level) → Level 2 D(S) as organization → Level 3 morphisms
(all operational content) → Level 4 categorical vocabulary (language only,
Q-DSP-05) → Level 5 persistence theory (neighboring formalism, importable only via
Q-DSP-02). Rule added: every claim is as strong as the lowest level it uses —
§5a uses Levels 1–3 (hence derivable), the §4 anchor uses Level 5 (hence
conditional). Any future addition must state its level.

**"Functor" demoted to target status** [observation]
Cross-system transfer is now a *candidate* comparison functor / structure-preserving
translation until Q-DSP-05 settles the composition laws — "functor" presupposes
fully defined categories on both sides.

**Convergence flagged** [observation]
The reviewer independently proposed reading ARW as a theory of *description
transformations* (objects = admissible paths between descriptions). This converges
with the monograph's standing meta-claim (session 2026-05-29: ARW as a theory of
description dynamics — how descriptions gain, lose, and switch stability), reached
there from the philosophical arc, here from the mathematical side. The fibration
supplies that meta-claim's formal object (morphisms = the transformations).
Whether to elevate this from observation to the note's framing is Rico's call —
not executed.

---

## Session 2026-08-01 (fourth entry): Q-DSP-01 first data contact — interleaving bound holds, violations localize on the singular locus

**Check design** [observation]
Seed-swap perturbation test of scope_fibration.md §5a on the Kuramoto v2 2D field
(160×112 over κ×σ, reference seed 42, replicas {7,13,99,137}; deliberately harsher
than the case's declared Δ). 112 checks (4 seeds × {full grid, stability mask} ×
14 ε). Script: `Simulationen/qdsp01_interleaving_check.py`; results:
`Simulationen/qdsp01_check_results/`. Levels 1–3 only (components + union-find +
triangle inequality); no persistence machinery invoked.

**Claim 1 confirmed: 112/112** [claim]
Minimal descent shift c* ≤ 2σ̄ in every check; bound conservative
(max c*/(2σ̄) = 0.313, median 0.060 — path connectivity heals most direct edge
stretches).

**Strict-descent failures are geometry, not noise** [claim]
At ε ≈ 0.053 (near the case's working ε), 271/35,243 reference edges violate
unshifted descent — and 100% of them lie within 0.15 of the analytic threshold
diagonal κ = 1.485σ (all-point baseline: 9.8%); median endpoint σ_Δ on violating
edges 6.5× global median. Local triviality of the (ε,Δ)-square fails exactly on
the singular locus, as the fibration reading predicts.

**Claim 2 only vacuously tested** [open-question]
With global σ̄, the gap condition held in 1/112 rows (strict descent also held
there) — no counterexample, but the sufficiency direction needs the
pointwise/masked refinement with the declared Δ-protocol, plus a rerun on the
registered CASE-20260311-0001 1D sweep. Both registered in scope_fibration.md
§5b/§7 as remaining gates.

**Caveat kept visible** [observation]
Strict failure at ε_working = 0.05 under seed swap does not contradict CASE-0001's
go_nogo: seed swap redraws oscillator frequencies (realization change), which is
outside the case's milder declared Δ; the pipeline mask excludes the band.

---

## Session 2026-08-01 (fifth entry): Third review round — sober status framing; local gap test passes at scale

**Status reframed** [observation]
Adopted from external review: "analytically established, computationally
instantiated, empirically consistent with an existing Kuramoto field; localization
prediction supported in one harsher-than-declared perturbation test." Claim 1's
112/112 demoted from finding to implementation validation (the bound is a triangle
inequality consequence — the data's contribution is absence of type/discretization
surprises and quantified conservativeness). Localization claim weakened from
"exactly on the singular locus, nowhere else" to "strongly enriched at, and in
this run confined to, the independently known transition band"; the analytic line
κ = 1.485σ is the independent referent, co-location with the pipeline σ_Δ field is
constructively related and downgraded to consistency.

**Local edge-wise gap test: risky cell exactly empty** [claim]
Replacing the vacuous global gap test (1/112 non-vacuous rows) with the per-edge
condition d ≤ ε − s(x) − s(y) (s = pointwise displacement of the applied
perturbation): over 1,852,996 edge checks (4 seeds × 14 ε), the cell
(gap satisfied ∧ descent violated) contains **0** edges, with 1.25M gap-satisfied
and 598k gap-violated edges — the exact sufficiency prediction of
scope_fibration.md §5a held at scale in a test with real power. Quantified beyond
the theory: P(violated | gap violated) = 0.043 — the local gap condition is a
sound but conservative flag (necessity fails badly and was never claimed).
Script: `Simulationen/qdsp01_local_gap_test.py`.

**Next tests registered by value** [observation]
(1) Blind reconstruction test: estimate the singularity region from descent
violations alone, compare localization power against null models (permuted edges,
density-weighted edges, |∇O| thresholding, direct σ_Δ thresholding) — decides
whether D(S) is a diagnostic instrument or only a reinterpretation. (2) 1D
CASE-20260311-0001 rerun with declared Δ — registry hygiene; external review
judges note → hypothesis promotion justified after it.

---

## Session 2026-08-01 (sixth entry): Runs 3–4 — declared-Δ rerun confirms plateau identification; blind test bounds the instrumental claim; note promoted to hypothesis

**Run 3: registered protocol, declared Δ** [claim]
CASE-20260311-0001 sweep regenerated per ScopeSpec (36 pts, N=500, own ω-draw;
δ_01 = 0.1 rad IC jitter, 20 replicas; spread calibrates as documented, mean
0.0022). Strict descent: 20/20 on the registered N=4 plateau interior (ε = 0.09
working, 0.134); 10/20 exactly at the plateau edge (0.066); failures below
plateau localize near the registered regime boundaries (κ ≈ 1.0–1.4, 2.27 vs.
Invariants 1.475/1.8/2.25). Local gap risky cell: 0 (3,621 gap-satisfied edges).
The go_nogo-plateau = local-triviality identification now holds on the case's own
protocol, not only under harsher seed swaps.

**Run 4: blind reconstruction — works, but no diagnostic surplus** [claim]
From 895 pooled violation edges alone, robust fit recovers κ = 1.580σ + 0.038
(truth 1.485σ; slope within 6.4%); median distance to the line 0.067 vs ≈ 0.47
for matched-count nulls. However, matched-count top-σ_Δ (0.011, 100% in-band) and
top-|ΔO| (0.031) baselines localize as well or better: the fibration violation
adds no localization power over the quantities it is constructed from, in this
test. Verdict recorded in scope_fibration.md §5b: D(S) is a coherent unifying
reading with verifiable consequences, not (currently) a superior diagnostic
instrument. The instrumental claim is bounded; the architectural claim is
untouched. Fairness note: σ_Δ baseline consumes the full δ-protocol per point,
the violation set used 4 cheap replicas.

**Promotion executed** [observation]
scope_fibration.md note → hypothesis (front-matter + DOC_INDEX), per the external
review's stated condition (1D rerun) now met. §7 rewritten: hypothesis →
working-definition requires a second system (pendulum, CASE-20260311-0003 data
exist), Q-DSP-02 made precise or weakened, Q-DSP-05 settled; the run-4 bound must
not be used as a promotion argument. Scripts/results:
`Simulationen/qdsp01_case0001_1d_rerun.py`, `qdsp01_blind_reconstruction.py`,
`qdsp01_check_results/`.

---

## Session 2026-08-01 (seventh entry): Evidence-status audit — EWS discriminator test specified

**Diagnosis accepted** [observation]
Rico's assessment (claims plausible, not sufficiently supported) triaged into
three claim classes: (A) mathematical results — derived and numerically verified,
but the citation base is self-referential and unreviewed; (B) empirical-structural
results — one system family, self-generated, unreplicated; (C) universality claims
across organisations/ecosystems/science/cognition — carried by illustrative
examples that demonstrate nothing. The introduction promises class C. Run 4's
honest negative (no diagnostic surplus over σ_Δ) generalises into the question a
reader may ask of the whole book: what can ARW do that existing tools cannot?

**Test specified before data contact** [experiment-proposal]
`docs/notes/ews_discriminator_test_protocol.md`: preregistered comparison against
the early-warning-signals programme. Distinctive claim: EWS is observable-blind
and reads indicator rises as system properties; ARW's F0/F-gradient taxonomy
allows an alarm to be a property of the *description*, predicting that genuine
transitions produce cross-observable coherent alarms while artifacts are
observable-idiosyncratic and co-located with that observable's σ_Δ. Delimited
against multivariate EWS (which aggregates to gain power; ARW reads the
disagreement). Data: Cascade whole-lake experiment — Peter (manipulated,
transition) vs Paul (reference, none), same instruments, same period; public via
EDI. Criteria, baselines (B1–B4 incl. plain σ_Δ threshold and multivariate EWS),
and all four outcomes' consequences for the monograph fixed in advance.

**Named risk** [open-question]
Declarability of Δ on observational data is the real obstacle — ARW's
perturbation class is native to simulation. Choosing Δ after seeing the alarms
would make the test circular, so it is fixed in step 1 or the protocol stops.
First step is deliberately a feasibility check (data inventory + Δ declarability),
not an analysis. Q-EWS-01–03 to be registered on execution.

**Publication route** [observation]
Rico is outside academia; peer review is not a practical path for the class-A
results. Not resolved this session; noted that preprint/data-repository routes
(Zenodo/OSF DOI, open review) remain available and do not require affiliation.

---

## Session 2026-08-01 (eighth entry): EWS protocol hardened — review round 4

**Reframed as a discrimination study, not "ARW vs EWS"** [observation]
Title and framing fixed: *A Preregistered Discrimination Study of
Observable-Specific versus System-Level Early Warning Signals*. The question —
when an indicator rises, is that a property of the system or of the observable? —
stands independently of ARW; ARW supplies one candidate discriminator among
competitors. Consequence: a negative result is a finding about early-warning
methodology rather than an internal disappointment, and the study is usable by
researchers with no stake in ARW.

**Five hardening measures adopted** [observation]
(1) *Partial time blinding*: all timestamps shifted by one common random offset,
preserving lags/windows/alignment while removing the calendar — with the limit
stated explicitly rather than oversold (seasonal gaps and diel cycles keep
within-year phase inferable; what the offset removes is alignment against the
published manipulation schedule). (2) *Structured observable admission*: family /
variable / reason / expected mechanism / admissibility concern, the last column
being the rule that an F0 verdict may only be invoked if its risk was named in
advance; plus a deliberate forcing-variable negative control. (3) *Audit trail*:
`03_prereg/` with append-only `decision_log.md`, `delta_definition.md`,
`observable_admission.md`, `coherence_rule.md`, `baseline_parameters.md`.
(4) *Forced prediction before unblinding*: per-series call with confidence and a
mandatory "expected reason if wrong" cell — prevents the post-unblinding
discussion from collapsing into indicator-value debate. (5) *Freeze*:
`freeze_prereg.py` SHA-256 manifest (tamper-tested: single-character edit
detected) plus git tag `cascade_prereg_v1`; neither lock sufficient alone, both
together make silent criteria change detectable.

**Δ elevated to a property of the measurement apparatus** [claim]
`delta_definition.md` requires Δ to be derived from instrument precision,
calibration spec and replicate structure — from the EML metadata, never from the
values. The short-lag fallback is permitted only with its bias direction stated
(it inflates σ_Δ, making the ARW side more conservative); observables where the
bias could run the other way are inadmissible under it.

**H2 decision rule tightened** [observation]
The coherence rule must dominate B1, B3 *and* B4 simultaneously; matching any one
is not domination. B2 (hindsight-tuned EWS) is reported as an upper bound only.

---

## Session 2026-08-04: Cascade Stage-1 stop reviewed — the metadata declares ε, not Δ

**Rico executed Stage 1 and stopped correctly** [observation]
Analyst handoff v2 contains metadata, prereg records and blinded rehearsal CSVs —
no key, no raw sources, methods-only extract of the Batt et al. SI (the full PDF
correctly quarantined: its role-labelled trajectories can fingerprint the blinded
series). Two deviations self-recorded: DEV-001 (blinding staged before Stage 1
cleared → blinded set demoted to infrastructure rehearsal), DEV-002 (SI can
fingerprint identities → fresh mapping and fresh analyst context required for any
confirmatory run). The protocol's stop condition fired and was obeyed rather than
renegotiated — that is the substantive methodological result of this round.

**Retrieved fact: manufacturer specs exist for the declared configuration** [claim]
The EML names YSI 6600 V2-4 with ROX 6150 optical DO and 6025 optical Chl-a. The
manufacturer specification sheet (E52-02) publishes: DO %sat resolution 0.1%,
accuracy ±1% of reading or 1% air saturation (0–200%); pH resolution 0.01,
accuracy ±0.2 unit; temperature 0.01 °C / ±0.15 °C; chlorophyll range ~0–400
µg/L, resolution 0.1 µg/L, detection limit ~0.1 µg/L, linearity R²>0.9999 — and
**no accuracy figure at all**. Route 1 of the Stage-1 record's three exits is
therefore partially open.

**Conceptual correction: those numbers are ε, not Δ** [claim]
An accuracy figure states when two readings are indistinguishable — that is the
definition of ε. Δ is the admissible perturbation class: a modelling commitment
about which variations count as the same system state, which no datasheet can
supply. The distinction is invisible in simulation (Δ is injected there) and
became visible only on observational data. Consequences: ε *is* declarable for DO
and pH; Δ is undeclarable from metadata **in principle**, not accidentally, so no
further metadata archaeology would help. Bias direction added (absent from the
Stage-1 record, and backwards in the earlier delta_definition draft):
underestimating Δ shrinks σ_Δ → σ_Δ < ε holds more easily → more stability
verdicts, fewer F-gradient calls → **anti-conservative for H1**.

**Chlorophyll fails on manufacturer grounds, F0-shaped** [interpretation]
No stated accuracy, and the 6-Series manual calls single-point-calibrated
fluorescence "only semiquantitative with regard to chlorophyll" — valid for
relative change, not absolute concentration. The analysis would use it for
cross-observable agreement on absolute alarm position, i.e. outside its declared
valid use. Admitting it with its 0.1 µg/L *resolution* as the uncertainty floor
would set ε orders of magnitude too low, in the anti-conservative direction.

**Stronger stop reason: the coherence rule loses its object** [claim]
With chlorophyll excluded and model-derived GPP/R/NEP excluded for process error,
the admissible response set is DO %saturation and pH — two observables, with
temperature only as forcing-variable control. "≥ k of n agree" carries no
information at n = 2. The Cascade dataset therefore cannot support the
discriminator test as designed — not because Δ is undeclarable (repairable by an
honest modelling commitment) but because the surviving observable set is too small
for H1 to be about anything. A replacement needs ≥ 4 independently instrumented
response observables with published accuracy specs plus a same-apparatus labelled
negative (the Cascade design's real strength, worth preserving).

**Registrations** [observation]
Q-EWS-01 answered negative *with corrected question*; Q-EWS-02/03 open but
untested with the power blocker recorded; Q-EWS-04 new (admissible form of a Δ
declaration for observational data; candidate: declared Δ-family with verdict
stability required across it). Flagged: `docs/advanced/epsilon_and_scope_resolution.md`
and `docs/glossary/perturbation_spread.md` treat Δ only in its simulation-native
form and need the observational case. Review doc:
`docs/notes/ews_stage1_review_epsilon_vs_delta.md`. Blinded CSVs were not opened.

---

## Session 2026-08-04 (second entry): Stage-1 review corrected — ε_instr ≠ ε_operational ≠ Δ

External review round 5 caught the first draft over-correcting: having separated
ε from Δ, it then treated manufacturer specifications as *determining* ε. Five
precisions incorporated; the note is revised, not appended to.

**Three objects, not two** [claim]
Resolution (smallest representable difference), accuracy (deviation from a
reference value) and ε (the scope's adjacency threshold) are distinct.
Specifications constrain the **instrument contribution** to ε; a preregistered
mapping rule is still required, and it is not unique — pH ±0.2 admits
ε_truth = 0.2 (reading vs true value) or ε_pair = 0.4 (two readings mutually
compatible); DO accuracy is reading-dependent, so the instrument contribution is
initially a function ε(x), not a scalar. Drift between weekly rotations,
temporal aggregation and the published preprocessing add further contributions
the datasheet does not cover. Registered as Q-EWS-05.

**pH standardization circularity** [claim]
The published analysis z-scored pH within each year. An accuracy in pH units
therefore applies only to the *raw* series; after standardization the induced ε
would be ±0.2 divided by a data-estimated annual SD — data-derived, hence exactly
the circularity preregistration exists to prevent. Raw units only.

**Bias direction is conditional** [interpretation]
The anti-conservativeness of an underestimated Δ requires σ_Δ to be
inclusion-monotone. The repo's canonical σ_Δ(x) = sup_{δ∈Δ}|O(x+δ)−O(x)| is, so
the corollary holds here; a distributional σ_Δ variant would not inherit it and
must re-derive it. "Err upward" is bounded — an arbitrarily wide Δ tests a
different claim; the clean form is the declared family Δ_min ⊆ … ⊆ Δ_max with
verdict stability required across it.

**Chlorophyll: F0 is Π-relative, and the first draft forgot that** [interpretation]
Corrected classification: F0 for **Π_abs** (absolute concentration) under the
available calibration record; **Π_rel** (relative fluorescence change) remains
conceptually admissible — an alarm location need not depend on absolute
concentration — but has no external ε rule (RFU carries no accuracy figure) and
unquantified drift. The fault is the mismatch between sensor validity and chosen
Π, not the sensor alone. Applying the F-taxonomy to the framework's own draft is
the lesson.

**Stronger power finding: shared channels, not just small n** [claim]
"No configuration of k carries information" overstated it — k=2 of 2 tests
concordance but degenerates to pairwise unanimity, losing redundancy and partial
coherence. The decisive objection is independence: DO and pH come from the same
sondes and share logging, deployment, weekly rotation and preprocessing incl. the
documented mean-shift correction, so common-mode instrument error propagates into
both and apparent coherence is not system-level evidence. Replacement criteria
revised: ≥3 response observables is the mathematical minimum for a non-trivial
majority, ≥4 a robustness recommendation (k=3 of 4 tolerates one failure), on
**independent measurement channels**. Role separation restored: the reference
lake is the system-side labelled negative; temperature is a covariate control,
not a negative response control (it varies between lakes itself).

**Framework consequence** [observation]
`docs/advanced/epsilon_and_scope_resolution.md` and
`docs/glossary/perturbation_spread.md` treat **both** ε and Δ only in their
simulation-native forms. The observational case needs: the specification →
ε_operational mapping rule (Q-EWS-05) and the Δ-as-modelling-commitment form
(Q-EWS-04). This is the largest framework gain of the whole EWS episode, and it
came from a test that never ran.

---

## Session 2026-08-04 (third entry): Core-concept drift audit — the doc↔code interface is where canon rots

One pass per core concept, checking canonical documents against each other, against
the pipeline code, against the case artifacts, and against the newest journal and
open-questions entries. Full record: `docs/notes/arw_core_concept_drift_audit_2026-08-04.md`.

**The repo is healthier than its own snapshot claims** [observation]
242 non-README docs, 100% front-matter compliance, every file registered in
DOC_INDEX including all twelve uncommitted ones, supersession chains recorded with
reasons, no orphans, no Q-ID collisions (the apparent Q-CNS-06 / Q-SCA-06 duplicates
are parent/sub-question pairs). The June repair plan's repo-side packages — WP-B1,
WP-B2 (INC-01 + σ_Δ/ε* naming), WP-A4 (SDI canon) — are genuinely executed, not just
marked done. Drift did not accumulate where the anti-pile-up machinery looks.

**It accumulated at the doc→code interface instead** [claim]
`pipeline/stability_mask.py` does not exist and never has (planned, action E-1/E-2),
yet `epsilon_and_scope_resolution.md` claimed the exact stability mask is computed
"(exactly)" in it, and `perturbation_spread.md` attributed the direct σ_Δ computation
to it while describing `epsilon_kappa_map.py` as proxy-only. Since 2026-06-02
`epsilon_kappa_map.py::compute_sigma_delta_windowed` has computed direct σ_Δ with
`proxy_pointwise`, `proxy_localmax` and a `pointwise_underestimates` flag. An agent
following canon looks for a missing module and falls back on precisely the pointwise
proxy C1 invalidated at θ* — the one-sided false-negative mode. Notably
`cover_stability_criterion.md` was *already* correct: the divergence sat inside one
concept cluster for two months without anything catching it, because nothing in the
consistency machinery compares prose against `pipeline/`. Fixed in all three documents
and in `context_map_pipeline.md`.

**Second-largest locus: the machine-readable context maps** [observation]
Still v0.1, never resynced after the 2026-06-02 transfer/σ_Δ work. The pipeline map had
`stability_mask.py` in the DAG chain and `transfer.py` as the transfer stage, with
`transfer_v2.py`, `sweep_behavioral.py` and `pipeline/kernels/` absent. Corrected in
place. Version discipline across the four maps is inconsistent (0.1 / 0.1 / 0.1 / 0.3
with an internal 0.2 block, no `last_updated` anywhere) — which is why this stayed
invisible.

**`transfer_distortion_metrics.md` contradicted itself** [claim]
The WP-A4 amendment (SDI collinear with RCD by construction in the 1D-sweep tier,
w₄ = 0, independent-information requirement) was executed in the SDI and Φ sections,
but the closing "Using the Metrics Together" section still demanded all four metrics
and asserted "RCD = 0, TBS ≈ 0, PCI ≈ 1, but SDI > 0" — a configuration the same
document proves impossible in that tier. Reconciled. Φ v2's channel mapping to
`transfer_v2.py` was checked against the code and matches, weights included.

**Empirical position has improved and the commentary has not** [interpretation]
The 2026-06-10 audit's finding B2 states that Dissipation, Forcing, Symmetry Breaking
and Aggregation have zero pipeline-validated cases. On disk CASE-0005 (Dissipation,
`pendulum_gamma`) and CASE-0007 (Aggregation, `sir_epidemic`) both carry
`decision: "go"` with full partition output; 0007 is `status: complete`. Four of six
classes now have an anchor. Against that: both cases hold two divergent copies of their
YAML triple — March originals under `CASE-<id>_*.yaml` and June canon under bare names,
111–297 diff lines apart, nothing marking which is authoritative.

**Highest-traffic stale definition is in the skill layer** [observation]
`arw-repo-context` still defines SDI as the plateau-width similarity
1 − |w_A − w_B|/max(w_A, w_B) — the quantity WP-A4 explicitly ruled *not* to be SDI —
and carries the superseded four-term Φ. `arw-repo-pulse` is three weeks past its own
staleness threshold: its case table misses that 0005/0007 ran, its pipeline table
predates the σ_Δ implementation, and its Q-prefix map lists 9 of the 22 prefixes now
in use. Both are loaded first in every session, so their drift propagates into work
before any document is read. Not fixed in this pass (skill layer, separate maintenance
pass) — recorded as decision 5 in the audit.

**Registrations** [observation]
No new Q-IDs. Five decisions left open for Rico (F1 shorthand `span < 2ε` vs
`ε ≥ ε*(O,X)` in ~10 documents and the ScopeSpec schema comment; whether to promote a
canonical `docs/core/falsification_schema.md`, since the fullest statement of the
F-schema currently lives in a derived context map; duplicate case YAMLs; v1 transfer
directories; skill refresh). Theory-update queue reaffirmed with Q-EWS-04/05 at the
top, unchanged by this pass.

---

## Session 2026-08-04 (fourth entry): Audit decisions executed — and one defect the repairs surfaced

Rico settled all five open decisions from the drift audit the same day. Execution record
in `docs/notes/arw_core_concept_drift_audit_2026-08-04.md` §9.

**F1 shorthand: option (b)** [observation]
Canonical layer states `ε ≥ ε*(O, X_B)`; instantiation documents keep `span(π) ≷ 2ε` and
gain a pointer block scoping it to connected images. Seven documents patched that way,
three corrected outright (`schemas/ScopeSpec.yaml`, `CASE_TEMPLATE_signature_first.md`,
`observable_decomposition.md`). The reasoning behind the split: the shorthand is not
wrong, it is *tier-local*, and rewriting it in ML/neuroscience/statistical-physics
bridge documents would cost the accessibility those documents exist for. What was
actually dangerous was the schema comment — it is copied into every new ScopeSpec.

**`docs/core/falsification_schema.md` promoted** [claim]
The fullest statement of F0–F4 / F1_BC / F-gradient / Z_shared had been living in
`context_map_falsification_bc.md`, a `meta`-layer artifact whose own header declares it
derived. Consolidating it exposed how much canon was only there: the **Part VII V3.2
decision-order revision** (F0 → F4 → F1 → F3 → F2 → F-gradient, because F2 asks whether
θ* is stable and that presupposes θ* is estimated reliably — false while F4 is live), the
A6 split (an invalid A6 is F0; a valid but unresolving A6 is F1 — λ_T read as λ_∞ without
a convergence test versus λ_T on its own terms), claim-relative F1 with total collapse as
the special case the pipeline tests, the F-gradient **mass** criterion μ(χ=1)/μ(X_B) > τ_∂,
and the caveat that "never lower ε" is a proxy-based pipeline convention and not a
χ-theorem. None of that was reachable from `docs/core/` or `docs/glossary/`. The map is
now v0.2, `derived_from` the core document, with the core document declared to win.

**Archive and stamps** [observation]
Six March-dated YAMLs moved out of CASE-0005/0007; six `SUPERSEDED_v1.md` stamps written
into the legacy transfer directories, each naming the v1 PCI defect, the superseding v2
run and the v1 numbers for provenance. `archive/README.md` gained a one-copy rule and a
withdrawal notice over its own Φ table — which had been quoting v1 values without one.

**The repair surfaced a new defect (D-16)** [claim]
Stamping revealed that CASE-0007 and CASE-0004 each contained a **doubled output path**,
`cases/<id>/cases/<id>/transfer/`, holding byte-identical copies of their v1 transfer
output from 2026-06-02 — a run invoked with the case root already in the path argument.
The CASE-0004 copy is the one that matters: it holds an unstamped second instance of
**Φ = 0.9983 `highly_admissible`**, the number `framework_validation.md` was built on and
that the v2 recomputation replaced with Φ = 0.7794 `ambiguous_requires_inspection`
(N_CONFOUND, COMPONENT_DISAGREEMENT). Stamping the canonical directory alone would have
left a clean-looking copy of a withdrawn result one directory deeper. Archived.

**Methodological note** [interpretation]
Three of the four repairs found something the audit had not: the schema comment as the
real propagation vector for the F1 shorthand, the amount of canon trapped in a derived
artifact, and the nested-path duplicates. Auditing locates drift; *executing* the repair
is what walks the paths where drift actually lives. Worth repeating the pattern rather
than treating an audit report as the deliverable.

---

## Session 2026-08-04 (third entry): Assumption cross-check against refreshed skills — five corrections

Skills were refreshed (pulse regenerated 2026-08-04 after the core-concept drift
audit; `docs/core/falsification_schema.md` promoted to canonical). This session's
own work was re-checked against them. Five items of drift found, all corrected in
place; the substantive conclusions survive, one negative result hardens.

**C-1 (material). The pipeline's "σ_Δ" field is a finite difference, not a
perturbation spread** [claim]
`cover_pipeline_v2.py::compute_perturbation_spread` returns the max absolute
difference to the four grid neighbours — a discrete gradient magnitude on the
sweep grid, consuming no perturbation protocol. Consequences: (i) run 1's
"co-location with σ_Δ" is even less independent than flagged — it is near-identical
to the |ΔO| baseline; (ii) run 4's fairness note was **backwards**: it claimed the
winning baseline consumed a full δ-protocol per grid point and was thus more
expensive than the violation set, whereas it is strictly *cheaper* than the four
seed replicas. The negative result therefore hardens — the fibration violation set
was beaten on localisation by a cheaper, purely local quantity. Baseline renamed
"top grid-neighbour spread edges" throughout.

**C-2. CASE-0001 working ε is 0.09, not 0.05** [observation]
The qdsp01 README caveat cited "the case's working ε = 0.05". 0.05 is the ε in the
2D paper field's `metadata.json`; CASE-20260311-0001 uses ε = 0.09, revised up from
0.05 to sit in the N=4 plateau interior. The two were conflated. Run 3 was
unaffected — it used the ScopeSpec plateau [0.066, 0.134] and reported ε = 0.09 as
the working value correctly.

**C-3. F-gradient fires on a mass criterion, not pointwise** [claim]
`falsification_schema.md`: F-gradient fires when μ(χ=1)/μ(X_B) > τ_∂, where χ is
assignment instability — not at a single unstable point. `scope_fibration.md` §3
carried the pointwise form; corrected. Related: the Δ-direction obstruction in the
fibration reading is properly **χ**, with σ_Δ as its proxy (χ computed nowhere,
Q_NEW_26 open). This sharpens rather than weakens the fibration story and is now
stated in §2a.

**C-4. Global sup σ̄ is the idealised, superseded form — and run 1 shows why** [interpretation]
The canonical admissibility condition is bulk supremum plus bounded boundary layer
(`perturbation_spread.md`, sharpened 2026-07-18), because a bare global bound would
forbid every perturbation-sensitive transition state. §5a's derivation uses global
σ̄ and is therefore valid but conservative. Empirical convergence worth recording:
with global σ̄ the gap condition held in 1 of 112 rows — vacuous. That vacuity is
the empirical face of the theoretical reason the global form was abandoned, and
run 2's per-edge localisation is a move toward the canonical refinement rather
than a deviation from it.

**C-5. Canonical falsification source updated** [observation]
`docs/core/falsification_schema.md` (promoted 2026-08-04) is now the operational
source, including the decision order F0 → F4 → F1 → F3 → F2 → F-gradient and the
severity binding (F-gradient primary: `scope_refinement`). Added to `depends_on`
of `scope_fibration.md` and `ews_stage1_review_epsilon_vs_delta.md`, with an
explicit "if the two diverge, the schema wins" clause on the fibration §3 table.

**Checked and clean** [observation]
σ_Δ sup-form (bias-direction argument in the ε/Δ note holds); F1 stated as
ε ≥ ε*(O,X_B), consistent with the 2026-08-04 shorthand decision (option b);
Q-DSP-1–5 and Q-EWS-1–5 match the regenerated prefix registry with no collision;
no reference anywhere in this session's work to the non-existent
`stability_mask.py`; CASE-0003 N=2 and CASE-0004 N=4 corrections do not touch any
claim made here.

---

## Session 2026-08-04 (fourth entry): The description atlas — the Vollraum's form fixed, correspondence reframed as chart collection

**Strategic reframing (Rico)** [observation]
Two moves in sequence: (i) instead of testing ARW against fresh data — which kept
failing on feasibility — take *heavily validated* theories and ask whether ARW
reproduces their structures locally (correspondence principle, the standard every
general framework was first held to and ARW never was); (ii) the target remains the
Vollraum description, so correspondence work is not validation-by-borrowing but the
route to it.

**The Vollraum's form is forced** [claim]
If the no-complete-invariant reading holds (Q-DSP-02), a global summary of D(S) is
unavailable and the only available form is an **atlas**: charts (regions of constant
fiber) plus transition data plus obstructions. This turns §4's caveat into a
specification of what a completed description *is*. Registered as
`docs/notes/description_atlas_programme.md`.

**The charts already exist** [interpretation]
A validity condition as the sciences state it — Kn < 0.01, v ≪ c, N → ∞, m_e/M ≪ 1,
λ ≪ L, small amplitude, Ginzburg — is exactly the assertion that on that parameter
region the assignment is stable under the admitted perturbations, i.e. a chart.
Physics has mapped them for a century and validated them far beyond anything ARW can
produce; nobody has collected them as charts of one object. Reproducing a chart is
the trivial half (run-4 lesson applies without mercy); the payoff is the **transition
data** — overlaps, failures to glue, regions belonging to no chart. Known hard regions
read as obstructions: the Kn transition regime as a gap between charts, ensemble
inequivalence as a failed transition function, conical intersections as monodromy.

**P-ATLAS registered as a falsification condition** [claim]
*Inside a chart, ARW adds nothing over local analytic tools; any surplus can appear
only at chart boundaries.* The inside half follows from the definition (constant
fiber → locally trivial → nothing for a stability diagnostic that a gradient misses)
and **has already fired in the predicted direction**: run 4 tested a smooth
single-transition field — a chart interior — and the finite-difference baselines won.
The boundary half is untested, with a stated end state: no surplus there either
closes the instrumental claim permanently, leaving the architectural claim as a
descriptive framework with no diagnostic value. `scope_fibration.md` §5b amended
accordingly — run 4 is now "not yet fairly tested" rather than "tested and refuted",
with the test-design limitation (chart interior; steepness and assignment instability
coincide there) recorded and the replacement test's failure outcome fixed in advance.

**Obstruction types M / T / R** [claim]
The schema recognises only the metric mode (M: σ_Δ ≥ ε beyond τ_∂). The atlas reading
predicts two more: **T (topological)** — assignment not single-valued around a loop,
χ ≠ 0 where |∇O| stays finite, textbook instance being the geometric-phase sign change
of adiabatic states around a conical intersection; and **R (no common refinement)** —
two charts whose observable families admit no common refinement, so the overlap
comparison is undefined rather than negative. T matters most: it is the mode run 4
could not test (in a smooth field steepness and assignment instability coincide), and
a confirmed T would be the first case where the fibration **adds** a schema category
rather than re-describing one. Related to Q_NEW_26 — a topological obstruction is
exactly where the σ_Δ proxy for χ cannot work in principle.

**Well-posedness point** [observation]
An atlas is intra-system: paths, not functors (`scope_fibration.md` §2b). Q-REL-05
(Φ carries no BC-class-distance signal) was found on *cross-system* comparisons;
comparing two charts of one system on their overlap is the well-posed application of
the same machinery, where the known defect does not bite.

**Preregistered case list and guards** [observation]
Eight chart families fixed in advance (Knudsen; Born–Oppenheimer/conical
intersections; canonical↔microcanonical; Ginzburg; harmonic↔anharmonic; geometrical↔
wave optics; Markovian↔non-Markovian; rigid↔elastic), first three = A1, A2, A5. All
reported including failures. Guards: θ* derived from the ARW construction *before*
the literature value is consulted; a mandatory surplus prediction per case (A1's:
θ* = θ*(π, ε, Δ) predicts the *spread* of published Kn thresholds across quantities
as structure rather than imprecision — checkable, **not yet verified**); ARW/ART level
discipline. Q-DSP-06/07 registered; §9 lists three outcomes that would end the
programme.

---

## Session 2026-08-04 (fifth entry): Out of 1D — the general regime construction

Rico's directive: no interest in testing only in 1D; argue openly now, test beyond
1D later. Registered as `docs/notes/general_regime_construction.md` (hypothesis).

**Two defects of the 1D operative form** [claim]
(i) *Degeneration.* `scope.md`'s operative definition edges only **consecutive**
samples, so G_ε is a path graph; between two nodes there is exactly one chain, and
components are just the maximal runs with consecutive increments ≤ ε — the
construction is increment thresholding. Consequently the argument that justified
adopting the cover at all (transitivity-safety, sorites resolution) is **vacuous**
in the format the pipeline uses, since it requires several distinct chains.
`cover_stability_criterion.md` defines G_ε(O) over **all** pairs and does retain
the content: a doc↔code divergence in the central construction, of the same class
the 2026-08-04 drift audit found elsewhere.
(ii) *Undeclared adjacency.* "Consecutive in the sweep" comes from the sweep
design, not from (B, Π, Δ, ε). The construction has depended on an ingredient
outside the tuple — structurally the same defect as the ε/Δ conflation found on
observational data.

**Proposed general construction** [claim]
Adjacency = **Δ-reachability**: x ⌢ y iff y ∈ x + Δ; edge iff x ⌢ y and
d(O(x),O(y)) ≤ ε; regimes = components, subject to χ_{Δ,ε}. Δ does double duty —
fixing both what the assignment must survive and along which steps chains run —
so nothing new is declared and the smuggled ingredient is derived instead. No
ordering, sweep or grid enters; dimension does not appear. The 1D sweep is
recovered exactly as the special case Δ = one grid step, so existing cases are not
invalidated but re-derived.

**Codimension argument — the reason this is necessary, not tidy** [claim]
A 1D sweep meets a codim-1 boundary transversally but meets a codim-2 point defect
only by coincidence: **1D is generically blind to all structure of codimension
≥ 2**, and refining the sweep does not help. Real symmetric two-level degeneracies
are codim 2 (von Neumann–Wigner), so conical-intersection-type defects — the
atlas programme's candidate type-T obstruction — are unreachable from any 1D sweep
in principle. Q-DSP-07 therefore has this construction as a prerequisite.

**Schema consequences** [observation]
θ* scalar → boundary *set* (curve/surface, with connectivity and codimension);
`sweep_range` → swept region; **TBS_norm has no general form** and would need a
Hausdorff-type distance between boundary sets or must be declared inapplicable —
which, since TBS is a Φ component, means 2D cases cannot be compared to 1D cases
under the current transfer metric. Given Q-REL-05 this is the moment to make the
dependency explicit rather than patch it. The ε-plateau logic survives unchanged:
N(ε) is a component count, defined for any graph.

**Assets and honest limits** [observation]
The Simulationen 2D scripts already compute grid-neighbour adjacency and cover
height on 2-parameter fields — computational core exists, but their adjacency is
grid-derived, not Δ-derived, so they instantiate the construction only
approximately. CASE-20260430-0013 is registered as 2D and has never been run.
Risks recorded: sampling cost exponential in dimension (no sparse variant
designed); Δ-reachability must be made concrete without silently becoming "grid
neighbours" again; extra dimensions add noise unless they carry declared scope
content. Testing outlook (recovery check → 2D re-derivation with boundary as a set
→ codim-2 detection vs a family of 1D sweeps), each to be preregistered before
running.

---

## Session 2026-08-04 (sixth entry): ε is a family — three multiplicities, two composition rules, one unanswered module

Rico caught a second silent assumption: that there is one ε per scope. There is
not, and the repo already contradicts it in three places. Registered as
§2.2–§2.4 of `general_regime_construction.md` plus Q-EPS-01/02/03.

**Three multiplicities, only one of them sound** [claim]
Across resolution — the family {S_ε}, I_ε, cover height, η = −log(ε/ε₀) — is fine;
that is the fibration's ε-direction, where a scope legitimately *is* a point.
Across observables (ε_i) and across the domain (ε_i(x)) were assumed away. Repo
evidence: ScopeSpec carries a scope-level `epsilon` *and* a per-observable
`resolution_floor` (CASE-0001: 0.09 vs 0.01) with the relation nowhere stated; and
`ews_stage1_review_epsilon_vs_delta.md` §2.1 names ε(x) for reading-dependent
accuracy and then drops it.

**The scalar assumption had already been abandoned once, with effect** [observation]
Run 2 of the Q-DSP-01 checks used the per-point condition d ≤ ε − s(x) − s(y).
That is a non-constant threshold, and it is precisely the step that turned a
vacuous test (gap condition satisfied in 1 of 112 rows) into an informative one
(1.85M edge checks, risky cell empty). The non-scalar form was the one that worked
— unnoticed at the time.

**Commensurability: cross-observable ε is ill-formed without declared normalisation** [claim]
CASE-20260311-0003 runs `lambda_proxy` (rate, span 0.0688) and `var_rel`
(dimensionless, span 0.2974) under one ε — a 4.3× span disparity, with the swept
grid reaching ε = 0.5, seven times `lambda_proxy`'s entire span. Candidate
normalisations (span, ε*, declared physical scale) are each modelling steps.

**Two composition rules, concealed by 1D** [claim]
Rule A (joint graph: edge iff Δ-reachable and all d_i ≤ ε_i, then components) vs
Rule B (common refinement of per-observable partitions). They coincide on a path
graph and diverge in general: a Rule-B class need not be connected, a Rule-A
component is by construction. The atlas reading needs charts to be regions, which
argues for Rule A — but the choice must be declared. Recorded as Q-EPS-02.

**Finding: `epsilon_multi_observable.py` does not answer its own question** [claim]
The module's docstring asks "Does a single ε suffice, or does each observable need
its own εᵢ? What is the joint admissible region in (ε₁, ε₂) space?" — but the
implementation iterates one scalar and applies it to every observable, so only the
diagonal ε₁ = ε₂ is explored and question 3 is never addressed. It implements Rule
B implicitly. And the answer to its question 2 is arguably already in its own
output: `CASE-20260311-0003/results/partition/EpsilonMultiObservable.json` records
`agreement_rate = 0.367` — the two observables share plateau structure on barely a
third of the ε-grid — with nothing drawn from it. Third doc↔code divergence found
today, after the 1D consecutive-vs-all-pairs G_ε gap and the "σ_Δ" field that is a
four-neighbour finite difference.

**Risk added to the note** [observation]
An ε-family multiplies the declaration burden (each ε_i, each profile, the
symmetrisation, the normalisation). More declared freedom is more room for
post-hoc tuning, so any case using a non-constant ε-family must freeze its
declarations before the run.

---

## Session 2026-08-04 (seventh entry): The observer withdrawn from ARW level

Rico: "Beobachter haben ihre eigenen Generatoren zur Beschreibung des Erlebten. Ich
kann mir nicht mehr erklären, warum ein Beobachter überhaupt eine Rolle in der
formalen Konstruktion spielen sollte." Audited, and he is right.

**Where the term actually sat** [observation]
The frozen core is clean: `docs/glossary/scope.md`, `docs/core/*` — **zero**
occurrences. The term clustered in notes (12), context_navigation (6),
art_instantiations (6), advanced (4), with one hit each in glossary and overview,
both of which drew the line correctly (a constraint on the observer *vs* on the
framework; "observer-dependence" listed as an open question). The place it tipped
over is `generator_admissibility_taxonomy.md` — an **art_instantiations** document
asserting "This preserves the core **ARW principle**: the observer remains
sovereign over perturbation class and resolution." Same defect class as the other
three found today: a document at one layer legislating for another.

**Why the observer does no formal work** [claim]
Everything attributed to it is a declaration: Δ (which variations count as the
same state) and ε (which differences do not count). Those are parameters of the
description, not properties of a subject. A description at resolution ε with
tolerance Δ is an object with coordinates; it needs a specification, not a
spectator. Naming a subject opens a regress — a describing system has its own
generator and scopes, which would need their own observer, without end.

**The replacement loses nothing** [claim]
"Observer sovereignty" states only that φ: Λ → (B, Π), i.e. Δ and ε are not in the
image of φ. That is a statement about the **arity of φ**, not about subjects.
Restated: Δ and ε are free parameters of the scope — coordinates of D(S). A(G) is
untouched; its existential quantifier over (Δ, ε) *is* the coordinate reading, and
this is now said explicitly in the doc.

**Edits executed** [observation]
`generator_admissibility_taxonomy.md`: observer sentences replaced by the arity
statement plus a boxed **level rule** (observer = ART-level term for a modelled
describing system; not admissible in ARW-level constructions; corollary: an
instrument's resolution floor is a property of the composite system target +
apparatus, belonging to that composite's B/Π — not an observer constraint, which
corrects a claim made earlier the same day). `bc_signature_persistence_and_dominance.md`:
"ε … chosen by the observer" → declared parameter; Q-SIG-02 re-read as
*declaration-dependence*. `observable_consequences.md`: "BC class is
observer-dependent" → observable-dependent (scope-relative).
`emergent_solution_space.md`, `scope_extended_definition.md`,
`limitations_and_open_questions.md`: wording aligned. `bc_extraction_method.md`:
the "Observer activation" example marked as an ART-level actor in the modelled
social system, not a formal ingredient. ARW-level layers (glossary, core,
overview, advanced) now contain no formal use of the term.

**Where the observer legitimately belongs** [observation]
As a *modelled system* in ART: `docs/cognitive_architecture/`,
`docs/context_navigation/`, the scope-constructing-agent cluster. There a
describing system has its own G and its own scopes, and which (Δ, ε) it in fact
selects is an empirical question about that system — never an ingredient of the
general construction.

---

## Session 2026-08-05: Validation strategy v2 — the 1D cases retired as focus, the study as the new unit

Source: `docs/notes/validation_strategy_v2.md` (experiment-proposal). Decided
with Rico in-session; grew out of the question where the pipeline conceptually
falls short of the theory's frame.

**The 1D case programme was scaffolding, not strategy** [interpretation]
The case/1D-sweep/go_nogo/Φ practice of the early phase was never declared as a
validation strategy; it accreted. With `general_regime_construction.md` its
limits are explicit: the cases validate the codimension-0 slice only, the sweep
carries an undeclared adjacency, and Φ/TBS_norm do not survive the break. Rico's
framing: the cases are relics of the ARW founding phase — an attempt to generate
validation — and are no longer the focus of the validation strategy.

**Role change, not discard** [claim]
The 1D cases become a frozen regression suite: the general construction with
Δ = one grid step must reproduce their registered partitions (failure falsifies
the construction, not the cases — acceptance criterion open, Q-VAL-02). No new
1D cases are opened for validation purposes.

**Three tiers, distinctiveness first** [claim]
T1 coherence (recovery, ε-family well-formedness, concrete Δ-reachability rule)
is a prerequisite, not a deliverable. T2 distinctiveness produces artifacts the
1D schema cannot hold in principle — (ε₁,ε₂) joint region for CASE-20260311-0003
(the 0.367 agreement_rate finally drawn as a conclusion), Rule A/B divergence,
θ* as a boundary set, codim-2 detection (anchor system open, Q-VAL-03). T3
discrimination (Cascade EWS, P-ATLAS outer half) stays external and preregistered.
Ordering decided: T2 first — T3 would spend blinded external data on untested
instrumentation. Explicit failure condition: if T2 yields nothing beyond the 1D
form, the generalisation is bookkeeping and must be reported as such.

**The study replaces the case** [claim]
Unit = declared question at one tier, frozen declarations (Preregistration as
first-class artifact), boundary sets instead of scalars, no Φ across the break —
cross-study comparison goes to Σ (WP-A3; revives the unbuilt WP-A5). Schema
design open (Q-VAL-01).

**Honest cost stated** [observation]
Until T2 delivers, the validation column is empty: the general construction is
untested and the old evidence is demoted to consistency constraints. The
strategy note says this rather than bridging it. Monograph consequence
(deferred by Rico): the formal chapters will be adapted later; no monograph
edits this session.

**Q-VAL-01–03 worked through in sequence, same session** [observation]
Q-VAL-01: study schemas drafted as `schemas/StudySpec.yaml`,
`schemas/Preregistration_template.md`, `schemas/StudyRecord.yaml` (v0.1),
design rules R1–R10 in the headers (ε-family enforced; grid-neighbor adjacency
only with a Δ-derivation; verdict against preregistered criteria only;
surplus-over-1D honesty field; no Φ across the break). `validate_study.py`
planned, not built — [MC] checks by hand until then. Status
partially_answered; promotion after the first study runs.
Q-VAL-02 [decided, Rico]: boundary-tolerant recovery criterion — N exact,
interior membership exact, cut-adjacent samples ≤ 1 grid step, deviations
reported; frozen in the strategy note before any recovery run.
Q-VAL-03 [decided, Rico]: staged codim-2 anchor — constructed two-level
minimal model H(x, y) = [[x, y], [y, −x]] first (gap zero at origin, mixing
angle carries monodromy), physical conical-intersection instance as
registered follow-up once type-T machinery exists.
