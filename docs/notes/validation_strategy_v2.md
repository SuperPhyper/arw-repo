---
status: experiment-proposal
layer: docs/notes/
created: 2026-08-05
depends_on:
  - docs/notes/general_regime_construction.md
  - docs/notes/description_atlas_programme.md
  - docs/notes/ews_discriminator_test_protocol.md
  - docs/notes/ews_stage1_review_epsilon_vs_delta.md
  - docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md
  - docs/core/falsification_schema.md
---

# Validation Strategy v2 — Three Tiers, and the Study as the New Unit

**Purpose.** The repository's original validation strategy — one system, one 1D
sweep, one go/no_go per case — was never declared as a strategy; it accreted as
practice during the framework's early phase. The generalisation of the regime
construction (`general_regime_construction.md`) has now made that practice's
limits explicit: the 1D cases validate only the degenerate codimension-0 slice
of the theory, and their central transfer metric does not survive the
generalisation. This note declares the successor strategy and the scaffolding it
requires. Decided with Rico 2026-08-05: **distinctiveness-first ordering** and a
**new unit of validation ("study")** rather than a backwards-compatible
extension of the case schema.

**What "v1" was.** Implicitly: unit = case; instrument = ordered 1D sweep;
success criterion = ε-plateau go/no_go; comparison = Φ. Its explicit ancestor,
the hardness ladder of `framework_validation.md`, is superseded (its flagship
"Strong (confirmed)" result did not survive the transfer_v2 recomputation).
Each of the four elements is now known to be damaged: the case validates the
degenerate special case only; the sweep carries an undeclared adjacency
(§1.2 of `general_regime_construction.md`); the plateau criterion survives
formally (N(ε) is a component count on any graph) but was only ever exercised
on path graphs; Φ/TBS_norm have no general form across the 1D/general break
(§5 of the same note), and Φ carries the open Q-REL-05 caveat besides.

**What this note is not.** It validates nothing. It is the declaration that was
missing: which claims the programme now stakes its correctness on, in which
order, and what artifact structure carries them.

---

## 1. Role change of the existing cases

The 1D cases (CASE-0001 through CASE-0007, CASE-0014) are relics of the early
phase — an attempt to generate validation before the theory's general form
existed. They are **withdrawn as the focus of the validation strategy** and
**retained as a regression suite**:

- Under the general construction with Δ = one grid step, each registered 1D
  partition must be reproduced **exactly** (`general_regime_construction.md`
  §2.1, §7.1). Failure falsifies the construction, not the cases.
- The cases are frozen: no new 1D cases are opened for validation purposes.
  (1D sweeps remain legitimate as *instruments* inside a study whose target
  requires them — e.g. the family-of-1D-sweeps arm of the codim-2 test in §4.)
- Case results may continue to serve as recognition anchors and worked examples
  in expository material, provided they are labelled as special-case results,
  not as validation of the general theory.

This role change resolves the tension cleanly: the relics are not discarded
evidence, they are the cheapest hard constraint the generalisation must satisfy.

## 2. The three tiers

Ascending order of evidential weight. Each tier has its own success and
failure conditions; no tier's success substitutes for another's.

### T1 — Coherence (internal)

The general construction and its declarations must be well-formed and must
contain the old results.

| Check | Success condition | Failure consequence |
|---|---|---|
| Recovery | General construction with Δ = one grid step reproduces every registered 1D partition: regime count N exact, membership exact in the interior; only cut-adjacent samples may shift by ≤ 1 grid step, and every such deviation is reported per case (**decided 2026-08-05, Q-VAL-02**; frozen here, before any recovery run) | Construction falsified; revise before anything else runs |
| ε-family well-formedness | Every study declares ε as a family (ε_i, optionally ε_i(x)) with normalisation and symmetrisation stated (Q-EPS-01/03) | Study inadmissible, not run |
| Δ-reachability concreteness | The sampled-domain rule for "one perturbation apart" is declared and is not silently "grid neighbours" (§6.2 of `general_regime_construction.md`) | Reintroduces the undeclared-adjacency defect; study inadmissible |

T1 is cheap and is a prerequisite, not a deliverable. Passing it claims nothing
beyond consistency.

### T2 — Distinctiveness (constructive)

Produce artifacts the 1D schema **cannot hold in principle**. This is the test
of whether the generalisation has substance or is notation. Ordered by cost:

1. **The (ε₁, ε₂) joint admissible region**, computed for CASE-20260311-0003 —
   answering the question `epsilon_multi_observable.py` poses in its docstring
   and does not answer. The half-answer already on disk (`agreement_rate =
   0.367`, 4.3× span disparity) is drawn as a conclusion, under a declared
   normalisation (Q-EPS-03).
2. **Rule A vs Rule B divergence** exhibited on a real ≥2D field: a Rule-B
   class that is not connected, i.e. not a region (Q-EPS-02). Decides whether
   the chart language applies to multi-observable regimes.
3. **θ\* as a boundary set**: run CASE-20260430-0013 or a Kuramoto (κ, σ)
   field under the general construction with a declared Δ, and report the
   boundary as a sampled curve with connectivity and codimension — the first
   artifact `Invariants.theta_star` cannot hold.
4. **Codim-2 detection**: a 2-parameter system with a known point defect,
   where the general construction detects the defect and a preregistered
   family of 1D sweeps through the same region does not. This is the direct
   test of the codimension argument and the prerequisite for any type-T
   (monodromy) work (Q-DSP-07). **Anchor decided 2026-08-05 (Q-VAL-03),
   staged:** first the constructed minimal model — the real-symmetric
   two-level system H(x, y) = [[x, y], [y, −x]], gap observable
   g(x, y) = 2√(x² + y²), degeneracy at the origin as the codim-2 point
   (von Neumann–Wigner counting), mixing angle θ(x, y) as the
   monodromy-carrying observable — with analytic ground truth and no external
   data dependency; a located physical instance (published
   conical-intersection data) is registered as a follow-up study once type-T
   machinery exists, and deliberately not first, because it would import the
   Δ-on-observational-data problem (Q-EWS-04) into a test of the construction
   itself.

Success condition per item: the artifact exists, was produced under frozen
declarations, and its 1D counterpart is demonstrably undefined or empty — not
merely coarser. Failure condition: if the general construction, run honestly on
these targets, yields nothing the 1D form does not already give, the
generalisation is elegant bookkeeping and this note's premise is wrong. That
outcome must be reported as such.

### T3 — Discrimination (external)

Preregistered differential predictions against incumbent methods, on data not
generated by this repository's own simulations. Two instruments exist:

- **The EWS discriminator test** (`ews_discriminator_test_protocol.md`) —
  criteria frozen, Cascade data not yet unblinded; currently stopped at Stage 1
  for the ε/Δ declaration problem (Q-EWS-04/05). Its resumption depends on the
  ε-family scaffolding from T1, which is the concrete bridge between tiers.
- **The atlas programme's outer half** (P-ATLAS: descriptive surplus at chart
  boundaries) — the inside half (no surplus within charts) has already fired;
  the outer half is the one that would establish distinctive content
  externally.

T3 is the only tier that can convince a reader who does not already accept the
framework's internal standards. It is deliberately *not* first: running
discrimination tests on top of an untested construction risks attributing a
failure of scaffolding to the theory, or worse, a success to it.

## 3. Ordering: distinctiveness first

Decided ordering: **T2, with T1 as its embedded prerequisite; T3 on the
strengthened construction.** Rationale:

- T1 alone proves consistency, which persuades no one and was never in doubt
  for the special case.
- T3 first would spend the programme's only irreversible resource — blinded
  external data — on instrumentation that has never been exercised.
- T2 items 1–2 are nearly free (data on disk; existing 2D field scripts in
  `Simulationen` as approximate computational core) and each produces a
  concrete object the old schema cannot express. That is the fastest way to
  make the generalisation load-bearing rather than programmatic.

## 4. The study — unit of validation

The successor to the case. A **study** is a declared question addressed to one
tier, with frozen declarations, run once.

Minimal artifact structure (design target, schema to be written — Q-VAL-01):

```
studies/STUDY-YYYYMMDD-####/
  StudySpec.yaml        # tier (T1|T2|T3), question, target Q-IDs,
                        # scope declarations: B, Π, Δ (+ sampled-domain
                        # reachability rule), ε-family block
                        # (ε_i [, ε_i(x)], normalisation, symmetrisation),
                        # composition rule (A|B) where |Π| > 1
  Preregistration.md    # frozen before run: predictions, success/failure
                        # criteria, analysis plan; hash + git tag
                        # (per the Cascade practice, now structural)
  results/              # boundary sets as sampled objects, regions as
                        # sample hulls — not scalars, not [min, max]
  StudyRecord.yaml      # outcome vs preregistration, deviations, verdict
```

Differences from the case schema, stated once:

- **Preregistration is a first-class artifact**, not a practice. The ε-family
  multiplies declared freedom (Q-EPS-01–03), and declared freedom without a
  freeze is post-hoc tuning surface (`general_regime_construction.md` §6.3).
- **Boundary objects are sets.** `theta_star: scalar` and
  `sweep_range: [min, max]` do not appear; their generalisations do.
- **No Φ across the break.** Studies are not compared to 1D cases via Φ/TBS —
  the metric has no general form (Q-REL-08) and carries Q-REL-05 regardless.
  Cross-study structural comparison, where needed, goes to the Σ level
  (WP-A3 decision; the unbuilt WP-A5 `SignatureTransfer.json` becomes the
  natural companion artifact, and this strategy is a reason to build it).
- **Cases are not extended.** The `cases/` tree remains as the regression
  suite (§1) and historical record.

## 5. Honest limits

1. Nothing in this note is evidence. The strategy inherits the current state:
   the general construction is untested, T2 item 4 has no constructed system
   yet, and T3 is stopped pending the ε/Δ declarations it depends on.
2. Withdrawing the 1D cases as validation focus empties the validation column
   until T2 delivers. This is the honest cost of the generalisation and is
   stated rather than bridged.
3. The break with Φ means there is **no continuity metric** between old and
   new results. Comparisons across the break are qualitative until a Σ-level
   procedure exists (open frontier per WP-A3).
4. Sampling cost bounds T2: beyond d ≈ 3 the dense-grid construction is
   unavailable and no sparse variant is designed
   (`general_regime_construction.md` §6.1). The strategy therefore claims
   d = 2 territory only.
5. The distinctiveness-first ordering has a known failure mode: indefinitely
   deferred external contact. Guard: T3's Cascade protocol is already frozen;
   the strategy commits to resuming it as soon as the ε-family scaffolding
   (T1) exists, not after all of T2 completes.

## 6. Registry

New IDs (prefix Q-VAL collision-checked against `open_questions.md` and
`docs/` 2026-08-05 — free):

- **Q-VAL-01** — Study-unit schema: what exactly StudySpec/Preregistration/
  StudyRecord must declare, and how the ε-family block and the sampled-domain
  Δ-reachability rule are encoded machine-checkably.
- **Q-VAL-02** — Recovery-check acceptance: exact reproduction of registered
  1D partitions, or a declared tolerance (and if so, which — label-identical
  vs boundary-position within one grid step)?
- **Q-VAL-03** — Codim-2 anchor system: which 2-parameter system with a known
  point defect serves T2 item 4 (constructed minimal model vs located
  physical instance, e.g. real-symmetric two-level degeneracy)?

Relations: operationalises the testing outlook of
`general_regime_construction.md` §7 (Q_NEW_25); consumes Q-EPS-01/02/03 as
admissibility conditions; prerequisite chain to Q-DSP-07 (type-T) via T2
item 4; sharpens the consequences of Q-REL-05/08 into a design rule (no Φ
across the break); depends on Q-EWS-04/05 resolution for T3 resumption.
Supersedes nothing: `framework_validation.md` was already superseded;
`validation_program_signatures.md` (Σ-signature program) is orthogonal and
untouched — its actions become T2/T3 candidates under the study unit if
revived.
