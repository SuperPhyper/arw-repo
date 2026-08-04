---
status: hypothesis
promoted: 2026-08-01 (note -> hypothesis; external-review condition met — see §7)
layer: docs/notes/
created: 2026-08-01
supersedes: docs/notes/total_description_space.md
depends_on:
  - docs/glossary/scope.md
  - docs/core/falsification_schema.md
  - docs/glossary/observable_range.md
  - docs/glossary/perturbation_spread.md
  - docs/core/cover_stability_criterion.md
  - docs/core/observable_information.md
  - docs/advanced/epsilon_and_scope_resolution.md
  - docs/advanced/observable_space_cover_height.md
  - docs/advanced/bc_signature_forward_derivation.md
---

# The Scope Fibration D(S) — One Cover Construction, Four Morphism Types

**Status caveat.** Exploratory note. Nothing here modifies the frozen scope-tuple
semantics (B, Π, Δ, ε) or any falsification category. The note proposes a *reading*
of existing, separately established constructions as slices of one object, and
registers what would have to be checked for that reading to be promoted.

**Renaming note (2026-08-01).** This file supersedes
`docs/notes/total_description_space.md` (created the same day). "Total description
space" over-promised: it suggests the space of all descriptions of a system,
whereas the object defined here is specifically **the family of scope-induced
cover constructions of one system, indexed by scope parameters, together with the
admissible comparison maps between them**. External review (2026-08-01) confirmed
the rename candidate already flagged in the original delimitation. The symbol D(S)
is retained for continuity with the Q-DSP question series.

**Terminology guards.**
1. *Fibration* is used in the loose sense of a fibered family over a parameter
   base, not as a claim that homotopy-lifting properties hold. No result from the
   topology of fibrations is imported by the name.
2. *Fiber bundle* is deliberately **not** used, and the reason is substantive:
   a bundle requires local triviality, and the failure of local triviality is
   precisely where ARW's content lives. The falsification categories (§3) are
   readings of the obstructions to local triviality. D(S) is informative
   *because* it is not a bundle.

## 0. Delimitation

This note is **not** part of the "semantic description spaces" cluster
(`docs/art_instantiations/kht_resonance_dialectic.md` §6.3, Q_NEW_E/F, Q-RD-5/6),
which concerns parties sharing and mediating descriptions. Here the object is
ARW-level and structural: the family of cover constructions of *one* system,
indexed by scope parameters. The rename to "scope fibration" (see above) removes
the terminological collision the earlier file had to manage.

## 1. Motivating observation: three constructions, one construction

The repository (and the monograph drafts built on it) uses an ε-comparison →
connected-components construction in three separately defined settings:

1. **Over the state space / observable image.** The observable cover C_ε of O(X_B)
   (scope.md, INC-01 upgrade; Felder 2026): regimes as path-connected components;
   stability requirement σ_Δ < ε.
2. **Over a sweep path.** The ε-adjacency graph G_ε on ordered sweep samples
   (monograph Part VII V1; pipeline `extract_partition`): regimes of the observable
   image *along the swept path*. Deliberately defined as a graph, not a cover.
3. **Over the resolution axis.** Cover geometry as a function of η = −log(ε/ε₀):
   cover height profiles (`observable_space_cover_height.md`), persistence intervals
   of BC configurations (Definition 12, generator signature), and the cover exponent
   α = 1/(β−1) (`bc_signature_forward_derivation.md`).

A fourth direction is present but never named as one: **Δ**. The perturbation spread
σ_Δ(x) measures how the component structure at (x, ε) responds to admissible
perturbation — it is the sensitivity of the construction in the Δ-direction.

The precision of setting (2) must be preserved: the three settings are not the same
object and must not be re-blurred. The claim is weaker and sharper at once — they are
the same *construction* (pairwise ε-comparison, then components of the resulting
nerve/graph) instantiated over three declared base spaces. Setting (2) is the
restriction of setting (1) to an ordered one-dimensional sample; setting (3) is the
family of setting-(1) objects indexed by ε.

## 2. Definition sketch (candidate, not canonical)

Let S range over candidate scopes of a fixed system. Define the **scope parameter
space**

> P = { (B, π, Δ, ε) : π ∈ Π_declared, ε ∈ (0, ε*(O, X_B)), Δ admissible }

and assign to each p ∈ P its **fiber**: the regime structure (components of the
cover construction) that the scope at p produces, where defined. The **scope
fibration** D(S) is this assignment as a whole — the family of fibers together
with the comparison maps between them.

### 2a. The four directions

- **ε-direction**: coarsening maps. For ε ≤ ε′, every component at ε is contained
  in a component at ε′. This direction is a filtration; its component-level record
  is exactly what cover height and the persistence intervals of Definition 12 read.
- **Δ-direction**: stability constraint. The obstruction is properly the
  **assignment-instability indicator χ_{Δ,ε}** — whether component membership
  changes under δ — with σ_Δ its *proxy*; χ itself is computed nowhere
  (Q_NEW_26, open). σ_Δ(x) < ε is the proxy condition for the fiber to be
  locally constant under perturbation. (Made precise in §5a.)
- **π-direction**: reindexing. Changing the observable changes the image space the
  cover is built in; observable BC structure ≠ system BC structure (Session
  2026-03-18) says this reindexing is *not* fiber-preserving in general.
- **B-direction**: restriction/extension of the admissible state set; scope
  transitions live here.

Each established ARW instrument then reads as the study of D(S) along one direction
with the others held fixed: the regime partition (fix π, Δ, ε; vary state/sweep
parameter), the α-theorem and Σ-extraction (vary ε), stability masks (vary Δ),
transfer between observables and F0/F1 diagnosis (vary π), scope-transition analysis
(vary B).

### 2b. The four directions as four morphism types (added 2026-08-01)

External review proposed sharpening "four directions" to **four types of morphisms
on one object**, making D(S) a small category (equivalently: a directed network of
admissible description changes) rather than only a parameterized family. The
candidate assignment:

| Direction | Morphism type | Character |
|---|---|---|
| ε | **Coarsening** c_{ε→ε′} | Total: always defined for ε ≤ ε′; composes strictly (filtration) |
| Δ | **Stability action** | Partial: well-defined only where component membership is δ-invariant; obstruction measured by σ_Δ; always restored after an ε-shift of 2·sup σ_Δ (§5a) |
| π | **Observable change** | Base change: rebuilds the cover in a different image space; not fiber-preserving in general; comparisons require a declared common refinement |
| B | **Domain restriction/extension** | Restriction maps; **scope transitions are the distinguished morphisms** at which the fiber changes discontinuously |

Two consequences make this more than notation:

1. **It reframes Q-DSP-04 instead of leaving it as an anomaly.** The original
   worry — ε and Δ filter, π and B only reindex, so how can this be one object? —
   dissolves in categorical language, because a category carries heterogeneous
   morphism types natively. The question becomes which *composition laws* hold
   across types (e.g. does a B-restriction commute with an ε-coarsening?), which is
   checkable case by case rather than a structural embarrassment.
2. **Path vs. functor.** The category D(S) is *per system*. A **path** in D(S)
   (compose observable changes, ε-changes, B-restrictions) is navigation *within*
   one system's descriptions. Transfer *between* systems A and B is a structurally
   different object: a **candidate comparison functor** D(S_A) → D(S_B) (or a span
   between them), not a path. *Candidate*, deliberately: "functor" presupposes
   fully defined categories on both sides — objects, morphisms, composition laws,
   identities — and until Q-DSP-05 settles the composition laws, the honest name
   for what transfer does is **structure-preserving translation**. "Functor" is
   the target status, not the current one. This reproduces, at the level of language, the finding of
   Session 2026-03-18 that Φ measures observable transfer, not system transfer —
   conflating a path with a functor *is* that error. The distinction also gives
   the WP-A3 reframing (transfer as restatement between two descriptions) a
   natural home: a restatement is a path; a cross-system claim needs the
   cross-system translation.

**Guard (language, not foundation).** Categorical vocabulary is adopted here as
*vocabulary only*. No categorical theorem is invoked, no universal property is
claimed, and nothing operational may be derived from the categorical packaging
unless the packaging is first shown to be conservative — that is the content of
Q-DSP-05. If the packaging turns out to impose constraints beyond the operational
definitions (e.g. forced composition laws for partial Δ-maps), those constraints
are *predictions to check*, not facts.

### 2c. Architectural hierarchy — what is fundamental (added 2026-08-01, second review round)

The note connects fibrations, categories, persistence, interleavings, and local
triviality, and a reader is entitled to ask which of these structures is
fundamental. The dependency order is fixed here once, so that "everything fits
somehow" cannot substitute for it:

1. **Level 1 — fundamental: the cover construction** (ε-comparison → components).
   Everything else in this note is derived from it. It is also the only level the
   pipeline computes.
2. **Level 2 — D(S): the organization of the covers** into one indexed family.
   No new mathematical content enters at this level; it is bookkeeping made
   explicit.
3. **Level 3 — the morphisms: navigation between covers.** All operational
   content attaches here: σ_Δ, plateaus, the falsification categories, the
   path-vs-translation distinction.
4. **Level 4 — categorical vocabulary: one possible language for Level 3.**
   Adopted as language only; its conservativity over Level 3 is Q-DSP-05. Never
   load-bearing.
5. **Level 5 — persistence theory: a neighboring formalism**, not the foundation.
   Levels 1–3 happen to produce its native structures (filtrations,
   interleavings); this permits importing its results if and only if the
   correspondence is established (Q-DSP-02), and permits nothing before that.

A claim in this note is exactly as strong as the lowest level it uses. §5a uses
Levels 1–3 only — which is why it could be *derived*. The no-complete-invariant
anchor (§4) uses Level 5 — which is why it remains *conditional*. Any future
addition to this note should state its level.

## 3. Falsification categories as degeneracy types of D(S)

The falsification schema, read against D(S), classifies the ways a fiber can fail
to exist or to be well-defined — it is not merely a checklist but a (candidate)
classification of the singular locus of the fibration, i.e. of the obstructions to
local triviality (see terminology guard 2):

| Category | Reading in D(S) |
|---|---|
| F0 | Fiber undefined: the pre-scopal substrate fails, the construction has no input (R(π) violated) |
| F1 | Fiber trivial along ε: ε ≥ ε*(O, X_B), cover collapses to one component |
| F-gradient | Fiber Δ-unstable on a set of positive mass: μ(χ=1)/μ(X_B) > τ_∂ inside R(π) — *not* a single unstable point (mass criterion, Part VII 2026-07-18) |
| F2 | Fiber not reproducible: component membership varies under δ ∈ Δ (Δ-direction failure at the partition level) |
| F3 | Degeneracy along the whole π-family: no observable yields a stable non-trivial fiber |
| F4 | Boundary artifact of the sampled base region, not of D(S) itself |
| Scope transition | Discontinuity of the fiber along the B-direction (distinguished morphism, §2b) |
| Z_shared | A region of P excluded for a whole class of π simultaneously |

Nothing in this table changes any category's operational definition; it relocates
them from "list of failure verdicts" to "types of non-smooth points of one object."
The canonical operational source is `docs/core/falsification_schema.md` (promoted
2026-08-04), including the decision order F0 → F4 → F1 → F3 → F2 → F-gradient and
the severity binding (F-gradient primary severity: `scope_refinement`). The table
above is a *reading* of that schema, ordered for the fibration argument, not a
competing procedure — if the two ever diverge, the schema wins.

## 4. The structural anchor: no complete invariant

The ε-direction alone is a one-parameter filtration; at the component level this is
the H₀ layer of persistent homology, a correspondence already registered as
partially resolved (Q4 discussion in `docs/core/observable_information.md`). Adding
any second direction (Δ-radius r, a boundary/sweep parameter, or an observable
family parameter) makes D(S) a **multi-filtration**.

For multi-filtrations there is a known structural result: multidimensional
persistence admits **no complete discrete invariant** analogous to the
one-parameter barcode; the rank invariant is complete only in the one-parameter
case (Carlsson & Zomorodian, *The Theory of Multidimensional Persistence*, Discrete
& Computational Geometry 42(1), 71–93, 2009).

If the identification in §2 survives scrutiny, this imports a theorem-level fact
into ARW's self-description: **the scope fibration of a system admits no
unconditioned global summary.** Any faithful record of D(S) requires declaring a
slice — fixing some directions to read others. Declared conditions on a claim are
then not concessions but coordinate declarations, and *some* declaration is
structurally forced. This is the strongest available backing for the framework's
central stance (conditions strengthen rather than weaken claims), and it is backing
of the right kind: a limitative result, not an appeal to modesty.

Two honesty guards on this anchor:

1. The Carlsson–Zomorodian result is about persistence modules over multi-filtered
   complexes. Whether the ARW directions (especially π and B, which reindex rather
   than filter) satisfy the hypotheses is exactly the open part — the result must
   not be cited as *about* ARW until the correspondence is made precise (Q-DSP-02).
   The interleaving structure derived in §5a is *supporting evidence* for the
   correspondence (interleavings are the native morphisms of persistence theory),
   not a proof of it.
2. "No complete discrete invariant" does not mean "nothing global can be said."
   Incomplete invariants (rank invariant; ARW's α, cover height, Σ̄) can still carry
   substantial global information. The claim is about completeness, not usefulness.

## 5. Compatibility of the directions

### 5a. Q-DSP-01, paper part: lax commutativity with exact commutativity on plateaus

*Setting.* Finite sample set V ⊂ X_B (full pairwise comparison for the cover
setting, consecutive-sample comparison for the sweep setting; the argument is
identical). Observable O: X → (M, d). For ε > 0 let G_ε(V) be the graph on V with
an edge {x, y} iff d(O(x), O(y)) ≤ ε, and let π₀ denote its component set. For
δ ∈ Δ let V_δ = {x + δ : x ∈ V}, carrying the same index set as V. Write
σ̄ = sup_{x ∈ V} σ_Δ(x).

*Claim 1 (Δ-maps exist after an ε-shift of 2σ̄).* For every edge {x, y} of
G_ε(V), the triangle inequality gives
d(O(x+δ), O(y+δ)) ≤ σ_Δ(x) + d(O(x), O(y)) + σ_Δ(y) ≤ ε + 2σ̄.
Hence the identity on the index set maps edges of G_ε(V) into edges of
G_{ε+2σ̄}(V_δ), and therefore induces a well-defined map
π₀(G_ε(V)) → π₀(G_{ε+2σ̄}(V_δ)). The ε- and Δ-directions are always compatible
**up to an ε-shift of 2σ̄** — a lax square. This is precisely an
**interleaving** in the sense of persistence theory, with interleaving constant
2σ̄.

*Claim 2 (exact commutativity under a gap condition).* The unshifted map
π₀(G_ε(V)) → π₀(G_ε(V_δ)) is well-defined if no edge is stretched past ε, for
which d(O(x), O(y)) ≤ ε − 2σ̄ on all edges suffices; the reverse direction holds
symmetrically if no non-edge with d(O(x), O(y)) > ε drops to ≤ ε. Both hold
simultaneously if **no pairwise increment lies in (ε − 2σ̄, ε + 2σ̄]** — a gap
condition on the increment spectrum around ε.

*Claim 3 (commutativity is free once maps are well-defined).* All maps in sight —
coarsenings c_{ε→ε′} and Δ-maps — are induced by the identity on the shared index
set. Any two compositions π₀(G_ε(V)) → π₀(G_{ε′}(V_δ)) along different orders of
coarsening and perturbation are therefore descents of the same map and agree
wherever both are defined. **The entire content of Q-DSP-01 is well-definedness of
the Δ-direction maps; commutativity itself carries no additional obstruction.**

*Operational identification.* The gap condition of Claim 2 is an interval of
ε-values, of width at least 2σ̄, on which the component structure is constant —
this is exactly the **robust ε-plateau** criterion already operational in the
pipeline's go_nogo logic. Consequences: (i) on plateaus, the (ε, Δ)-square of
D(S) commutes strictly — the fibration is locally trivial there; (ii) between
plateaus, only the 2σ̄-interleaved structure survives; (iii) F2 (θ* unstable
under Δ) and F3 (no robust plateau for any observable) are precisely the
operational detectors of the strict regime's failure. The pipeline's plateau
requirement is thereby identified as the condition under which the fibration is
locally trivial in the (ε, Δ)-plane — the go_nogo criterion acquires a geometric
meaning it was not designed to have.

*Guards.* (i) σ̄ is a **global** sup over the sample. The repo's canonical
admissibility condition is no longer the bare global bound but the **bulk supremum
plus bounded boundary layer**, sup_{x∈X_bulk} σ_Δ(x) < ε together with
μ(χ=1)/μ(X_B) ≤ τ_∂ (`perturbation_spread.md`, sharpened 2026-07-18), precisely
because a global bound would forbid every perturbation-sensitive transition state.
The derivation below with global σ̄ is therefore the *idealised* form — valid as a
bound, but conservative. Empirically this is not academic: with global σ̄ the gap
condition of Claim 2 held in only 1 of 112 rows (run 1), i.e. it was vacuous — the
empirical face of exactly the reason the global form was abandoned. The per-edge
localisation used in run 2 is the move toward the canonical refinement, not a
deviation from it. The pointwise refinement restricts V to the stability mask
X_stab = {x : σ_Δ(x) < threshold} and runs the same argument there. (ii) For dynamics-defined observables (r_ss, var_rel, lambda_proxy), σ_Δ
requires the tuple plus a generator (see the Q_NEW_E discussion in
`docs/notes/scope_component_conflict_typology.md` §8.1); the argument applies
unchanged once σ_Δ is defined. (iii) This resolves the (ε, Δ)-pair only. The
compatibility of π- and B-morphisms with the other two directions is *not*
addressed here and remains the open part of Q-DSP-01/Q-DSP-04.

**Status effect: Q-DSP-01 is partially answered** (ε–Δ pair: yes, laxly always,
strictly on plateaus; π/B compositions: open). Registered in
`docs/notes/open_questions.md`.

### 5b. What existing data could already test — first check executed 2026-08-01

**Executed (2026-08-01, two runs on the Kuramoto v2 2D field, seed-swap
perturbations {7,13,99,137} vs. reference 42; scripts and full results:
`Simulationen/qdsp01_interleaving_check.py`, `qdsp01_local_gap_test.py`,
`qdsp01_check_results/`). Status framing (external review, adopted): the ε–Δ
interleaving construction is analytically established, computationally
instantiated, and empirically consistent with an existing Kuramoto field; its
nontrivial localization prediction is supported in one harsher-than-declared
perturbation test. Not claimed: "empirically validated."**

- **Claim 1 (c* ≤ 2σ̄): 112/112** — read as *implementation validation*, not as a
  risky test (the bound follows from the triangle inequality); the data adds that
  the construction instantiates on real fields without discretization surprises
  and that the bound is conservative (max c*/(2σ̄) = 0.313, median 0.060).
- **Localization (the informative finding):** at ε ≈ 0.053, strict-descent
  violations (271/35,243 edges) are **strongly enriched at, and in this run
  confined to, the independently known transition band** (all within 0.15 of the
  analytic line κ = 1.485σ; baseline 9.8%). The analytic line is the independent
  referent; co-location with the pipeline "σ_Δ" field is **not** independent —
  that field is a four-neighbour finite difference on the sweep grid
  (`compute_perturbation_spread`), i.e. a discrete gradient magnitude, not a
  spread over a declared perturbation class. Reported as consistency only. Not shown: band-wide coverage, absence of
  off-band violations under all ε, or reconstructability from violations alone.
- **Claim 2, local sufficiency direction: passed a high-power test.** Local
  edge-wise gap condition d ≤ ε − s(x) − s(y) over 1,852,996 edge checks:
  confusion cell (gap satisfied ∧ descent violated) = **0**, with 1.25M
  gap-satisfied and 598k gap-violated edges — the exact prediction held at scale.
  Quantified beyond the theory: P(violated | gap violated) = 0.043 — the local
  condition is sound but conservative; necessity fails and was never claimed.
- Caveats: seed swap is harsher than the case's declared Δ (no contradiction with
  CASE-0001 go_nogo); 2D paper field, not the registered 1D sweep.

**Runs 3 and 4 (2026-08-01, later same day; scripts
`qdsp01_case0001_1d_rerun.py`, `qdsp01_blind_reconstruction.py`):**

- **1D rerun on the registered CASE-20260311-0001 protocol with the declared Δ**
  (36-pt sweep regenerated per ScopeSpec, own ω-draw; 20 IC-jitter replicas,
  δ = 0.1 rad): strict descent holds **20/20 on the registered N=4 plateau
  interior** (ε = 0.09 working, 0.134), is marginal exactly at the plateau edge
  (0.066: 10/20), and fails below plateau with violations localized near the
  registered regime boundaries (κ ≈ 1.0–1.4, 2.27 vs. Invariants boundaries
  1.475/1.8/2.25). Local gap risky cell again exactly 0. The go_nogo-plateau =
  local-triviality identification is thereby confirmed on the case's own
  protocol, not only on the harsher seed-swap variant.
- **Blind reconstruction test:** from 895 pooled violation edges alone (analytic
  line hidden), robust fit recovers κ = 1.580σ + 0.038 vs. truth 1.485σ (slope
  within 6.4%); median distance 0.067 vs. ≈ 0.47 for matched-count null models.
  **But the added-power question is answered no in this test:** matched-count
  top grid-neighbour-spread edges (median 0.011, 100% in-band) and top-|ΔO| edges
  (0.031) localize as well or better — and those two are near-variants of one
  another, both finite differences. In this instantiation D(S) is a coherent unifying reading
  with verifiable consequences — **not a superior diagnostic instrument**.
  **Test-design limitation (recorded 2026-08-04):** a smooth 2D field with a single
  transition is a *chart interior* in the sense of
  `description_atlas_programme.md` §2 — there steepness and assignment instability
  coincide, so the task had no room for the distinction the fibration is about, and
  the gradient is near-optimal by construction. Under the registered prediction
  P-ATLAS this negative result is the *expected* one and does not bear on the
  boundary case; the instrumental claim is **not yet fairly tested** rather than
  tested and refuted. Standing guard: the replacement test (inter-chart, type-T
  decoupling) is specified in advance and carries a stated failure outcome that
  would close the claim permanently. This
  bounds the instrumental claim; it does not touch the architectural one.
  *(Correction 2026-08-04, skill refresh: an earlier fairness note claimed the
  winning baseline consumed a full δ-protocol per grid point and was thus more
  expensive. It is a finite difference and consumes no protocol at all — the
  violation set was beaten by a strictly **cheaper** local quantity, so the
  negative result is harsher, not softer, than first recorded.)*

**Still open as checks:**

- The pipeline's cover-height fields over (sweep parameter, ε) are, at H₀ level,
  a discretized rank-invariant-like object over a 2-parameter base. Check whether
  the α-theorem is a statement about the asymptotics of this object near θ*
  (candidate: yes — it constrains the ε-scaling of the component containing θ*).
- σ_Δ as Δ-directional derivative: compare direct σ_Δ fields (CASE-20260311-0003
  corrected run) with the ε-positions at which component membership actually
  changes under sampled δ — §5a predicts these coincide up to the 2σ̄ shift, and
  exactly on plateaus.
- The two-directional record (ε, κ) already exists for CASE-20260311-0001 and
  CASE-20260311-0003; no new simulation is needed for a first consistency check.

## 6. Open questions (registered in docs/notes/open_questions.md)

- **Q-DSP-01** — *partially answered (2026-08-01, §5a)*: ε–Δ compatibility holds
  laxly always (2σ̄-interleaving) and strictly on ε-plateaus; open part: whether
  π- and B-morphisms compose coherently with the ε–Δ pair.
- **Q-DSP-02** — Does the (ε, Δ)-bidirection of D(S) satisfy the hypotheses of the
  multidimensional-persistence setting, so that the no-complete-invariant result
  applies literally rather than analogically? (§5a's interleaving is supporting
  evidence, not proof.)
- **Q-DSP-03** — Are the falsification categories exactly the degeneracy types of
  D(S) (a completeness claim for §3's table), or does the fibration reading predict
  failure modes not yet in the schema?
- **Q-DSP-04** — *reframed by §2b*: originally "do π and B filter or only
  reindex?"; now: which cross-type composition laws hold in the category D(S),
  and is the two-filtered-directions + two-base-change-directions structure
  irreducible?
- **Q-DSP-05** — Is the categorical packaging of §2b conservative — pure notation
  over the operational definitions — or does it impose additional constraints
  (e.g. composition laws for partial Δ-maps)? If conservative: safe as language.
  If not: each imposed constraint is a falsifiable prediction and must be
  registered as such.

## 7. Promotion path

**Promoted note → hypothesis on 2026-08-01.** Conditions met: §5a derivation
reviewed externally (third review round engaged and reformulated it correctly);
§5b checks executed — implementation validated 112/112; local gap sufficiency
risky cell exactly empty at 1.85M-edge (2D) and registered-protocol (1D) scale;
violations enriched at / in-run confined to the known transition band; **1D
CASE-0001 rerun with declared Δ confirms plateau-interior strictness 20/20**
(the external review's stated promotion condition).

hypothesis → working-definition requires: a second system (the pendulum field is
the natural candidate — CASE-20260311-0003 data exist); the Q-DSP-02
correspondence made precise or explicitly weakened to an analogy with stated
disanalogies; Q-DSP-05 settled (conservative, or surplus registered as
predictions). Note the registered bound from run 4: the *instrumental* claim
(diagnostic surplus over σ_Δ) is currently unsupported and must not be used as a
promotion argument; the promotion rests on the architectural claim and its
verified consequences. Promotion beyond hypothesis requires the Q-DSP-02 correspondence to
be made precise or explicitly weakened to an analogy with stated disanalogies, and
Q-DSP-05 settled in the conservative direction (or its non-conservative surplus
registered as predictions).
