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

