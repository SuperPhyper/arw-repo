---
status: working-definition
layer: docs/overview/
last_updated: 2026-09-16
---

# Empirical Results

Collected empirical findings of the ARW/ART programme, with their tier and their limits.

> **Read this first.** Everything below was produced under the Phase-1 practice: a case,
> a 1D boundary-condition sweep, a scalar ε, a go/no-go decision. Under
> [validation strategy v2](../notes/validation_strategy_v2.md) that practice is retired as
> the focus of validation. These results validate the **codimension-0 slice** only and now
> count as *consistency constraints* the general regime construction must reproduce — not
> as validation of it. Where a result has been withdrawn or bounded, that is stated in
> place rather than dropped.

---

## 1 ε-Analysis and Scope Resolution

*(see [../advanced/epsilon_and_scope_resolution.md](../advanced/epsilon_and_scope_resolution.md))*

- **Admissible ε-interval.** The partition structure is stable across ranges of ε
  (plateaus). The ε-sweep locates these empirically, which replaces guessing ε.
- **Scope fragility at transitions.** The admissible ε-interval narrows where the system
  changes fastest — Kuramoto: r = −0.77 between plateau width and observable gradient
  ([figures/epsilon_kappa_robustness.png](../../figures/epsilon_kappa_robustness.png)).
- **One ε does not cover several observables.** On the double pendulum (CASE-20260311-0003),
  `lambda_proxy` and `var_rel` share plateau structure on `agreement_rate = 0.367` of the
  ε-grid, with a 4.3× span disparity between them (0.0688 vs. 0.2974) and a swept grid
  reaching ε = 0.5 — seven times `lambda_proxy`'s entire span. Recorded in the case's own
  `EpsilonMultiObservable.json` since 2026-03 and left undrawn until 2026-08.
- **Observable agreement as a completeness diagnostic.** Where observables disagree,
  latent degrees of freedom are active
  ([../advanced/scope_completeness.md](../advanced/scope_completeness.md)).

**Limit, added 2026-08-04.** `epsilon_multi_observable.py` sweeps a single scalar applied
to every observable, so only the diagonal ε₁ = ε₂ is explored; it implements Rule B
(common refinement) and never addresses the joint (ε₁, ε₂) region its own docstring asks
about. Producing that region is T2 item 1 of validation strategy v2.

---

## 2 Observable Decomposition and Pre-Scopal Structure

*(see [../advanced/observable_decomposition.md](../advanced/observable_decomposition.md))*

- **Observables carry pre-scopal substrates.** Every non-trivial observable π is a
  composition of basis operations (Restriction, Aggregation, Symmetry, Discretization,
  Approximation). For r_ss, roughly 25 assumptions span levels A0–A6; exactly one of them
  is a scope decision.
- **Observable range R(π) and exclusion zone Z(π).** An observable is structurally valid
  only on R(π) ⊆ B. Where B overlaps Z(π), the observable fails from substrate failure
  (F0), not from insufficient span (F1)
  ([../glossary/observable_range.md](../glossary/observable_range.md)).
- **θ\* in CASE-0001 is a scope transition, not a regime boundary.** κ_c lies in Z(r_ss),
  where five substrate assumptions fail at once. A different observable — e.g.
  χ = ∂r_ss/∂κ, which diverges rather than collapsing — is needed to resolve the partition
  there (Q_NEW_12).
- **Φ measures observable transfer, not system transfer.** Φ = f(S_A, S_B), not
  f(System_A, System_B). Two physically identical systems with different observables can
  show low Φ.
- **`lambda_proxy` is insufficient by construction.** Assumptions A6.1 and A6.2 (finite T,
  finite δθ(0)) are violated by definition, which explains its empirical insufficiency in
  CASE-0002/0003 from first principles rather than after the fact.

---

## 3 Theorem H2′ — IVA Dimensionality Principle

*(see [../advanced/h2_prime_theorem.md](../advanced/h2_prime_theorem.md))*

> **dim_eff(Z(π)) = rank(IVA_ext(π))**

The effective dimension of an observable's exclusion zone in parameter space equals the
rank of its extended independent violation axes — the number of linearly independent
directions along which the observable's pre-scopal substrate fails. Proved via the Regular
Value Theorem and the Rank Theorem, with generic transversality from Lemma G and
measure-zero exceptions handled by Sard's theorem.

| BC class | rank(IVA_ext) | Shape of Z(π) |
|---|---|---|
| Coupling | 0 | isolated point (κ_c) — a scope singularity, not a region |
| Symmetry Breaking | ≥ 1 | at least a half-line or surface |
| k independent BCs | k | k-dimensional manifold |

Checked against three cases: CASE-0001 (Kuramoto, point at κ_c ≈ 1.49), CASE-0008
(pitchfork normal form, half-line along μ ≥ 0), CASE-0010 (German school system, 2D
surface in joint BC space). CASE-0008 and CASE-0010 are signature-first documents, not
pipeline runs — the check is analytic there, not measured.

**Corollary C4 (observable class necessity).** Two observables with different
rank(IVA_ext) cannot be substituted within the same scope; they belong to structurally
distinct observable classes. This connects directly to the F0 falsification category.

---

## 4 First Empirical Emergence Case — CASE-20260318-0004

*(coupled Stuart–Landau oscillators, K-sweep; see
[../advanced/arw_emergence_bc_relative.md](../advanced/arw_emergence_bc_relative.md))*

- **Emergence window:** ε ∈ [0.082, 0.805], width 0.723; N = 4 regimes, θ\* = 0.055
  (primary phase-locking transition R2 → R3; all transitions at 0.035 / 0.045 / 0.055).
- **Local precursor before the relational transition:** the local observable `amp_asym`
  collapses before the relational observable `PLV`.
- **Δ-robustness:** stable for λ ∈ [0.4, 1.3]; breaks at λ > 1.3 for weak K.
- The case's predicted partition was binary (N = 2); measured N = 4, `count_match: false` —
  recorded rather than reconciled.

---

## 5 Observable-Space Cover Height

*(see [../advanced/observable_space_cover_height.md](../advanced/observable_space_cover_height.md))*

- **Cover height as ε-marginalisation.** Instead of committing to a single ε, the cover
  height h integrates partition structure across all ε-scales at once. For the Kuramoto 2D
  sweep (1120 points) this yields 57 % dynamic range across BC space.
- **Height maps regime depth, not identity.** High h → interior of a flat regime; low h →
  transition zone. Height contours run parallel to the regime boundary.
- **Profile shape discriminates failure type.** Smooth/monotone → sufficient or gradual
  transition; jagged/non-monotone → F0 structural failure; flat → F1 span failure.
  CASE-0004 gives the cleanest discrimination (PLV 136 % DR vs. `amp_asym` 14 %, a 10×
  ratio).
- **2D sweeps reveal BC interaction structure.** In CASE-0002 (κ × γ), cover-height
  contours are diagonal — the regime boundary is a joint function of both BCs and is
  invisible in either 1D sweep (Q_NEW_18). This is one of the observations that later
  forced the dimension-free construction.
- **Dynamic range alone is not a sufficiency indicator.** In CASE-0002/0003 the
  insufficient observable (`lambda_proxy`) has *higher* DR than the sufficient one
  (`var_rel`); DR must be read together with profile shape.

**Caveat.** The 2D scripts compute grid-neighbour adjacency, not Δ-derived adjacency, so
they instantiate the general construction only approximately.

---

## 6 Cross-Scope Transfer

*(canonical implementation: `pipeline/transfer_v2.py`; see
[../bc_taxonomy/transfer_distortion_metrics.md](../bc_taxonomy/transfer_distortion_metrics.md))*

Φ = 0.55·PCI + 0.25·topology + 0.20·max(0, 1 − TBS/0.5); weights provisional. The guards
`VOID` and `TRIVIAL_PARTITION` make Φ **undefined**, not low.

| Comparison | Φ | Verdict | Flags |
|---|---|---|---|
| CASE-0001 vs CASE-0007 | 0.625 | partially_admissible | — |
| CASE-0004 vs CASE-0001 | 0.7794 | ambiguous_requires_inspection | N_CONFOUND, COMPONENT_DISAGREEMENT |
| Control, cross-class: 0003 vs 0007 | 0.7285 | ambiguous_requires_inspection | N_CONFOUND, COMPONENT_DISAGREEMENT, TBS_WINDOW_FRAGILE |
| Control, same-class: 0001 vs 0002 | 0.6954 | partially_admissible | TBS_WINDOW_FRAGILE |
| CASE-0005 vs CASE-0014 | — | TRIVIAL_PARTITION (N ≤ 1) | — |

**The central negative result (Q-REL-05).** The cross-class decoupling control (0.7285)
scores above the same-class control (0.6954). Φ carries no clear BC-class-distance signal
even with the corrected PCI, and must never be presented as BC-class evidence. Structural
transfer was relocated to the Σ level (WP-A3, 2026-07-02); the companion artifact WP-A5 is
proposed and not yet built.

**Withdrawn.** The v1 value Φ = 0.9983 `highly_admissible` for CASE-0004 ↔ CASE-0001 — on
which `framework_validation.md` was built — is withdrawn: v1's PCI never read per-point
labels and was collinear with RCD/SDI, so roughly 90 % of Φ's weight tracked regime count.
Replaced by 0.7794 `ambiguous`. All six v1 output directories carry a `SUPERSEDED_v1.md`
stamp; a Φ found in a directory *without* that stamp must be checked for provenance before
being cited.

---

## 7 BC-Class Coverage

Four of six BC classes have a pipeline-run anchor:

| BC class | Anchor case |
|---|---|
| Coupling | CASE-20260311-0001 / 0002 |
| Restriction | CASE-20260311-0003 |
| Dissipation | CASE-20260315-0005 |
| Aggregation | CASE-20260315-0007 |
| Forcing | none (CASE-20260430-0013 registered, partial output only) |
| Symmetry Breaking | none (CASE-0008 signature-first) |

Under validation strategy v2, "anchor" means anchor of the frozen regression suite, not of
the validation programme.

---

## 8 Negative and Bounded Results

Kept deliberately, because the programme's credibility depends on them being visible.

- **CASE-20260602-0014 (growing-population SIR): `no_go`.** Trivial partition at the
  working ε = 0.05; the observable `g_max_percapita` is F1-insufficient. ε\* ≈ 0.0146 is
  the cover-collapse threshold, not a working ε — the two have been confused in earlier
  summaries.
- **SDI is collinear with RCD** in the 1D-sweep tier, proved constructively (Part VII
  formalisation, 2026-07) → weight w₄ = 0 in Φ.
- **The scope-constructing agent fails its substrate-separation gate.** Every separation
  figure in `observable_information_and_bc_responsiveness.md` is explicitly **not
  load-bearing**; what stands is C1 (observable information does not entail
  BC-responsiveness) and the composition-separability measurement.
- **Scope fibration: instrumental claim bounded.** The 2σ̄-interleaving bound holds
  empirically (plateau-interior strictness 20/20 on a declared-Δ rerun) and blind
  reconstruction works — but diagnostic surplus over plain σ_Δ was **not** shown.
- **ε ≠ Δ on observational data (Q-EWS-04/05).** Three-way separation: ε_instr ≠
  ε_operational ≠ Δ. Instrument datasheets constrain the instrument component of ε only; Δ
  is a modelling commitment no metadata can supply, in principle. Underestimating Δ shrinks
  σ_Δ and yields *more* stability verdicts — i.e. it is anti-conservative. Consequence:
  `epsilon_and_scope_resolution.md` and `perturbation_spread.md` are flagged
  simulation-native for both ε and Δ, the largest open theory update.
- **χ is computed nowhere.** The assignment-instability indicator the F-gradient criterion
  is *about* has no implementation; every stability mask uses the σ_Δ proxy, whose
  reliability degrades exactly at boundaries (Q_NEW_26).
- **Two modules are cited in places as if they existed:** `stability_mask.py` and
  `validate_study.py` are **planned, not built**. Neither may be cited as a source of
  computed or validated values.

---

## Related

- [validation_strategy_v2.md](../notes/validation_strategy_v2.md) — what counts as
  validation from 2026-08-05 on
- [general_regime_construction.md](../notes/general_regime_construction.md) — why the 1D
  results are a codimension-0 slice
- [limitations_and_open_questions.md](limitations_and_open_questions.md) — framework-level
  open problems
- [repo_weakpoints.md](../notes/repo_weakpoints.md) — systematic gap assessment
- [research_journal.md](../notes/research_journal.md) — session-by-session derivation of
  everything above
