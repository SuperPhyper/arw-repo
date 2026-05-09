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
