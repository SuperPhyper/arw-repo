---
status: working-definition
layer: docs/notes/
---

# Open Questions

Active unresolved questions in the ARW/ART research program.
Entries are drawn from limitations documents, experiment falsification sections,
and theoretical gaps identified during development.

---

## Formalization

**Q1 — Quantification of admissibility**
Admissibility is currently defined structurally (partition stability under Δ).
Can it be quantified as a continuous measure — an "admissibility degree" —
rather than a binary condition?
Candidates: mutual information between suppressed variables and observables;
Lyapunov exponent under perturbations; PCI as a proxy.

**Q2 — ε as a function of state**
The current formalism treats ε as uniform across X_B.
But near regime boundaries, finer resolution may be needed to resolve
the partition, while bulk states require less.
Should ε be state-dependent? What is the consistent formulation?

**Q3 — Multiple ε for multiple observables**
When Π = {π₁, π₂, ...}, each observable may have a natural resolution scale.
What is the joint admissibility condition?
Is ε a vector, a matrix, or a function on the product space?

*Empirical evidence (CASE-0003, 2026-03-12):* Double pendulum with lambda_proxy
and var_rel: only 37% agreement across ε-values. var_rel (span=0.297) requires
ε ≈ 0.015; lambda_proxy (span=0.069) requires ε ≈ 0.008. A single shared ε
cannot satisfy both. This operationalises the question: the εᵢ vector is the
minimal adequate description for multi-observable scopes.

**Q15 — Bidirectionality of the BC-class / operator-signature correspondence**
The document `docs/advanced/bc_operator_signatures_arw.md` establishes a forward mapping:
BC classes → operator signatures → regime partitions.
The open question is whether the inverse holds: given a known operator family
appearing in a model, can the active BC classes be uniquely recovered?
If yes, this would constitute a fully bidirectional formalization schema —
operator structure as a diagnostic for BC landscape, not just a consequence of it.
Conditions for uniqueness, degeneracy, and failure modes are unknown.
Related: Q5 (universality of BC-class partition types), Q14 (scope template reuse).
Status: open

**Q4 — Formal relationship between ARW and topological data analysis**
Regime partitions have a topological structure (adjacency, boundary topology).
Is there a formal correspondence between ARW partition types and persistence
homology or sheaf-theoretic descriptions of data structure?

---

## Empirical

**Q5 — Do BC classes generate partition types universally?**
The BC taxonomy predicts that coupling BC generates sequential partitions
across Kuramoto, pendulum, and opinion dynamics.
This is the central empirical hypothesis. Is it borne out?
Under what conditions does it fail? (Network topology variation is the
expected failure mode for coupling — does it generalize?)

*First positive data points (2026-03-12):*
- CASE-0001 (Kuramoto, Coupling) + CASE-0002 (Multi-link pendulum, Coupling):
  both produce sequential partitions with linear adjacency graphs. Φ=0.675
  (partially_admissible). Structural homology confirmed; transition sharpness differs.
- CASE-0001 (Coupling) + CASE-0003 (Doppelpendel, Restriction): at matched ε (both N=4),
  Φ≈0.95 (highly_admissible). Coupling and Restriction produce structurally equivalent
  sequential partitions when ε is aligned. BC classes differ in transition position and
  sharpness, not in partition topology. This is unexpected — the taxonomy predicts
  structural differences between classes, but the sequential topology appears universal
  for monotone observables. The class-specific signal may be in θ*/range (position) and
  plateau width (robustness), not in partition cardinality.

**Q6 — What is the scaling exponent for TBS(N)?**
The transition boundary shift is predicted to scale as TBS(N) ~ N^{-α}.
What is α for different BC classes?
Is it universal within a BC class, or system-dependent?

**Q7 — Can scope transitions be detected without ground truth?**
In the labyrinth, scope transitions are detected via salience spikes
and mode switches. But in new domains (without designed zone boundaries),
how would a scope transition be detected from behavioral data alone?
Is there an unsupervised admissibility-loss signal?

**Q8 — Does the mode ecology stabilize, or does it keep growing?**
After sufficient training episodes, does the agent converge to a fixed
number of modes, or does the mode count keep growing?
If it stabilizes, what determines the equilibrium count?

---

## Conceptual

**Q9 — Scope transitions vs. phase transitions: precise relationship**
The framework claims these can coincide but are conceptually distinct.
Are there systematic conditions under which they do coincide?
Is every phase transition a scope transition? Is every scope transition
associated with a phase transition in some dual system?

**Q10 — Is emergence in ARW ontological or epistemic?**
ARW defines emergence as a descriptive event (scope reorganization),
not an ontological claim. But the reorganization is forced by dynamics —
the system itself changes in a way that makes the old description inadmissible.
Where exactly is the boundary between "the description changes" and
"something new comes into existence"? This question is left open deliberately.

**Q11 — BC classes as a complete taxonomy**
The current taxonomy has six classes. Is this complete?
Are there important BC types in social, biological, or cognitive systems
that are not captured by restriction, coupling, symmetry breaking,
dissipation, forcing, or aggregation?

---

## Methodological

**Q12 — How to specify ε empirically**
In the experiment files, ε is set as a hyperparameter (0.05 rad, 0.1 cosine distance).
Is there a principled procedure for deriving ε from data,
consistent with the consistency condition max_{δ ∈ Δ}|Π(x+δ) - Π(x)| < ε?

**Q13 — Partition extraction without known equations of motion**
In the pendulum and Kuramoto, partition extraction can use analytical results.
In the labyrinth and social systems, equations of motion are not available.
What is the general pipeline for partition extraction from trajectory data?

**Q14 — Scope template reuse across domains**
Can an ART scope specification from one domain (e.g., Kuramoto coupling BC)
be transferred to a structurally similar domain (e.g., opinion dynamics coupling BC)
without re-derivation? What is the formal condition for scope template reuse?

---

## External Frameworks

**Q16 — Formal correspondence between ARW and DSGRN**
DSGRN (Dynamic Signatures Generated by Regulatory Networks, Cummins et al. 2018)
constructs a finite partition of parameter space such that each region carries an
identical Morse graph (qualitative dynamical summary). The structural parallels to ARW
are strong: parameter space → partition → regime adjacency graph in DSGRN maps
directly onto BC space → regime partition → adjacency graph in ARW. Open questions:

(a) Is DSGRN a specific ART instantiation — i.e., does it operate within the ARW
framework as a BC-parameterized case with switching/piecewise-linear dynamics?

(b) DSGRN assumes a fixed model representation; ARW explicitly varies scope
(observable selection, resolution ε, aggregation). Can DSGRN regime partitions be
shown to be robust or to degrade systematically under scope variation?

(c) Both produce adjacency graphs over regime regions. Is there a graph morphism
between DSGRN's parameter graph and ARW's regime adjacency graph for the same
physical system?

(d) DSGRN's Morse graph provides a richer dynamical summary per regime (fixed
points, cycles, attractor structure) than ARW's current partition type vocabulary.
Does incorporating Morse graph structure into CaseRecord artifacts add value?

See also: docs/notes/arw_dsgrn_dialogue_plan.md, docs/notes/literature_links.md
(Cummins et al. 2018).
Status: open

---

## Observable Decomposition & Pre-Scope Structure
*(Added: session 2026-03-18)*

**Q_NEW_1 — Status of meta-assumptions about X**
The algebraic and topological structure of X (e.g. group structure of S¹,
differentiability of the flow) is a prerequisite for the well-definedness of many
observables — but it does not appear in the scope tuple S = (B, Π, Δ, ε).
Does the structure of X belong to (a) B, (b) an independent meta-layer below S,
or (c) the ART layer (domain-specific, not part of ARW-Core)?
Reference: `docs/advanced/observable_decomposition.md` — S¹ embedding in r_ss.
Status: open

**Q_NEW_2 — F0: integration into falsification schema**
Using an observable outside its range R(π) is neither observable insufficiency (F1)
nor scope rejection (F2–F4). Proposal: F0: R(π) ∩ B ≠ B, severity: observable_replacement.
Sub-questions: Is F0 a subtype of F1 or categorically distinct? How is R(π) operationally
determined? Must F0 be entered in ScopeSpec.yaml?
Reference: `docs/glossary/observable_range.md`.

*Partial resolution (2026-03-29):* `observable_replacement` is now a documented severity
value in `schemas/ScopeSpec.yaml` with full F0 semantics. CASE-0001 CaseRecord documents
an F0 case (r_ss at κ_c). Sub-question still open: should F0 entries be **required** in
ScopeSpec when R(π) ∩ B ≠ B is known? Pipeline does not yet enforce this.
Status: partially resolved — schema updated; requirement question open

**Q_NEW_3 — Latent degrees of freedom: B-extension vs. new observable**
Every Restriction operation generates a latent DOF. Under what criteria should a latent
DOF be (a) a new observable π' with its own scope S', (b) incorporated into B, or (c) ignored?
Candidates: ψ(t) (rotation phase), σ²(θ), w_topo, λ_conv, coupling geometry, Lyapunov spectrum.
Reference: `docs/advanced/latent_degrees_of_freedom.md`.
Status: open — next planned analysis step

**Q_NEW_4 — Product scope: empirical tractability**
The construction S_joint = S_1 ×_B S_2 is admissible. Does it carry a robust ε-plateau?
How does ε_joint relate to ε_1 and ε_2?
Status: open — tractable only after Q_NEW_3 is resolved

**Q_NEW_5 — w_min as criterion for robust discreteness**
Complete formulation needed: "Effectively discrete ↔ ∃ [ε_min, ε_max] with w > w_min
and N(ε) = const and partition stable under Δ." What is w_min? Is there an ARW-internal
criterion for minimum plateau width?
Status: open

**Q_NEW_6 — Completeness of regime partition relative to P(θ, t)**
Are there regime differences exclusively visible in the full phase distribution P(θ, t)
and invisible to all current (moment-based) observables? Formally: P_S = R_true or P_S ⊊ R_true?
Reference: `docs/advanced/latent_degrees_of_freedom.md` — LF-SHARED-A.
Status: open

**Q_NEW_7 — Symmetry breaking as partition property**
Symmetry Breaking appears for no latent DOF in the current BC mapping. Hypothesis (a): it is
an emergent phenomenon at the level of the regime partition (bifurcation structure), not a
single-observable property. Hypothesis (b): it is encoded in P(θ,t) distribution asymmetries.
Reference: `docs/advanced/latent_degrees_of_freedom.md` — Finding 2.
Status: open

**Q_NEW_8 — σ²(θ) as complementary observable to r_ss**
Finding (answered): σ²(θ) shares Z_shared with r_ss entirely — no genuine complementarity at κ_c.
σ²(θ) has additional own exclusion zones (Z_wrap, Z_multi) not shared with r_ss.
Reference: `docs/advanced/observable_decomposition.md` — σ²(θ) section.
Status: partially answered

**Q_NEW_9 — BC class: system property or scope property?**
Observable decomposition shows that BC classes appear in the observable itself (r_ss is
Restriction-dominated regardless of system). Is BC class in BCManifest (A) a property of
the system or (B) of the scope? Consequence of (B): BCManifest needs separate system BC
and observable BC; Φ decomposes into Φ_obs and Φ_sys.
Reference: `docs/advanced/observable_consequences.md` — K5.
Status: open — foundational question for BC taxonomy program

**Q_NEW_10 — Formal distinction: regime boundary vs. scope transition**
Does ARW need formal definitions distinguishing θ* (regime boundary within R(π))
from a scope transition at Z(π)? How is a scope transition documented in CaseRecord?
Reference: `docs/advanced/observable_consequences.md` — K3.
Status: open

**Q_NEW_11 — Transfer decomposition: Φ_obs × Φ_sys**
Can Φ be decomposed into Φ_obs(observable-BC_A, observable-BC_B) × Φ_sys(System_A, System_B)?
Operational approach: compare two scopes of the same system with different observables.
Requires a new case with two observables on the same system (CASE-0001 with r_ss vs. σ²(θ)).
Reference: `docs/advanced/observable_consequences.md` — K4.

*New data point (2026-03-29):* CASE-0004 (Stuart-Landau, PLV) → CASE-0001 (Kuramoto, r_ss):
Φ=0.9 (highly_admissible) across different systems AND different observables. This is
unexpectedly high given that Coupling↔Coupling with same observable (CASE-0001↔CASE-0002)
yielded only Φ=0.675. Tentative interpretation: high Φ here is driven by structural match
(both N=4, linear adjacency graph, same BC class) rather than observable similarity.
This motivates the Φ_obs × Φ_sys decomposition: the system contribution Φ_sys appears
dominant when BC class and partition topology match. Φ_obs test still requires
same-system different-observable case.
Status: open — new data from CASE-0004↔CASE-0001 motivates but does not resolve

**Q_NEW_12 — χ = ∂r_ss/∂κ as new observable for CASE-0001**
The susceptibility χ diverges at κ_c (R(χ) ∋ κ_c), unlike r_ss. Does a scope with Π = {χ}
yield a different regime partition? Is χ the first representative of a fluctuation-observable
class in ARW? High priority as CASE-0001 extension.
Reference: `docs/advanced/observable_consequences.md` — K6.

*Progress (2026-03-29):* F0 closure for r_ss at κ_c is now documented in CASE-0001
CaseRecord (PATH B interpretation). CASE-0001-ext with χ as primary observable is
planned as the next Kuramoto case. The scope tuple for CASE-0001-ext is not yet created.
See `docs/notes/repo_weakpoints.md` Category 1 for the concrete next steps.
Status: open — high priority; CASE-0001-ext planned, not yet created

---

## Observable-Space Cover Height
*(Added: session 2026-03-27)*

**Q_NEW_13 — Cover-height maxima vs. ε-plateau correspondence**
Observable-space cover height h(b_i) accumulates weight across all ε scales.
Open question: do local maxima of h in BC space correspond systematically to
stable ε-plateaus in the standard N(ε) curve of the ARW pipeline?
If yes, h could serve as a pre-filter for ε selection — pointing to the
BC-space regions where a plateau is likely, before running the full ε-sweep.
If no, the two methods are genuinely complementary without formal correspondence.
Empirical test: compare h-maxima positions with plateau regions from
CASE-20260311-0001 (Kuramoto κ-sweep).
Reference: `docs/advanced/observable_space_cover_height.md`
Status: open

**Q_NEW_14 — Cover height for multi-observable scopes**
The current method uses a single observable to define the sort order and
cover membership. For Π = {π₁, π₂}, a joint distance metric on the product
observable space is needed. Candidates: L2 norm, L∞ norm, weighted combination.
Does the choice of metric affect which regimes are visible?
Is there a canonical metric derivable from the scope tuple structure?
Reference: `docs/advanced/observable_space_cover_height.md` — Limitations §3.
Status: open

**Q_NEW_15 — Cover height as scope-depth indicator: formal criterion**
The interpretation of high h as "deep inside a regime" is informal.
Can this be made precise? Candidate formalization: h(b_i) is a measure
of the ε-interval width over which b_i belongs to a cover of size ≥ k,
integrated over k. This would connect h to the plateau width w in the
ε-sweep (Q_NEW_5) and to the scope robustness condition under Δ.
Status: open

**Q_NEW_16 — Cover-height profile shape as failure-mode discriminator**
The cover-height profile shape appears diagnostic for observable failure type:
smooth profile → sufficient or gradual transition; jagged profile → F0 structural
failure (noise); flat profile → F1 span failure.
Can this be formalized? Is there a quantitative measure of profile smoothness
(e.g. total variation, autocorrelation along BC axis) that separates the three
patterns reliably? If yes, cover-height could serve as an automated pre-screening
step for observable selection, before running the full ARW pipeline.
Reference: `docs/notes/research_journal.md` session 2026-03-28, Finding 3.
Status: open

**Q_NEW_17 — Cover-height DR vs. pipeline span: formal relationship**
In CASE-0002/0003, var_rel is sufficient (large span relative to ε) but shows
low cover-height DR (smooth monotone gradient, no clustering). In CASE-0001/0004,
sufficient observables show high DR (step/cluster structure). Is there a formal
relationship between cover-height DR and observable span(π) / ε?
Conjecture: DR is high iff the observable has at least one dense cluster
(plateau), which requires either a step-like transition or a flat regime.
A purely linear/gradual observable can have large span but low DR.
Reference: `docs/notes/research_journal.md` session 2026-03-28, Finding 4.
Status: open

---

## Context Navigation — Cognitive Architecture
*(Added: session 2026-03-29, from mode_scope_regime_audit.md)*

**Q-CNS-06 — Minimal fluctuation observable for cognitive mode transitions**
What is the minimal fluctuation observable for cognitive mode transitions,
and does it show the Z_shared peak predicted by the ARW framework?
The structural analog is χ = ∂r_ss/∂κ in CASE-20260311-0001, which has
R(χ) ∋ κ_c — precisely where the class-E observable r_ss fails.
The cognitive counterpart would be χ_mode = ∂(mode_distribution)/∂(context_load),
a fluctuation-class observable with R(χ_mode) ∋ transition points.
Source: `docs/context_navigation/mode_scope_regime_audit.md` §2.2.
Priority: high.

*Theoretical analysis (session 2026-03-29):* The minimal operationalization is
mode-switch rate per episode — a proxy for χ_mode without requiring explicit
context_load parameterization. Observable BC structure: A·R (Aggregation-dominated
with Restriction co-component). Expected: mode-switch rate peaks at regime boundaries
where mode_dist has entered Z(mode_dist). Testable by comparing mode-switch rate
profile across BC parameter sweep with mode_dist coverage height profile.
See `docs/notes/research_journal.md` Session 2026-03-29.
Status: partially_answered — operationalization proposed; awaits experimental confirmation

**Q-CNS-07 — BC class of a mode: stable under change of observation set?**
Is the BC class of a mode R_m stable under changes to the observation set Π?
If we observe the agent with different observables, does the same mode appear
to have the same BC class? This is the cognitive-architecture instance of Q_NEW_9
(BC class: system property or scope property?).
Source: `docs/context_navigation/mode_scope_regime_audit.md` §2.5.
Priority: medium.

*Theoretical analysis (session 2026-03-29):* The BC class of a mode as seen through
mode_dist (A·R) and as seen through salience_mean (R·A) will differ because the
observable's own BC structure overlays the system's actual BC class (K5).
The Φ_obs transfer experiment (same labyrinth, two observables) is the direct test.
Prediction: Φ_obs < 1 for mode_dist vs. salience_mean, confirming BC-class instability
under Π change for the cognitive architecture.
See `docs/notes/research_journal.md` Session 2026-03-29.
Status: partially_answered — hypothesis and test operationalized; awaits experiment

**Q-CNS-08 — Empirical signature: scope transition vs. regime transition**
What is the empirical signature of a scope transition (S_global failure, all
observables entering Z(π)) vs. a regime transition (mode switch, agent moves
between partition cells within S_global) in behavioral data?
This distinction is critical for interpreting zone boundary crossings
in the labyrinth experiment without ground-truth zone labels.
Source: `docs/context_navigation/mode_scope_regime_audit.md` §2.3.
Priority: high.

*Theoretical analysis (session 2026-03-29):* Formal discrimination criterion proposed.
Regime transition: T_stable < T_consolidation AND mode_dist converges to new dominant mode.
Scope transition: T_stable ≥ T_consolidation OR mode_dist does not converge.
In words: failure to find a new stable mode within one consolidation interval signals
S_global inadequacy, not a zone crossing. Testable by introducing novel zone types
(absent from training) into the labyrinth evaluation.
See `docs/notes/research_journal.md` Session 2026-03-29.
Status: partially_answered — formal criterion proposed; awaits experimental validation

**Q-CNS-09 — Consolidation: asymptotic sharpening or faster mechanism?**
Does consolidation produce asymptotic partition sharpening (as predicted by
dissipation analysis, K6 in observable_decomposition.md), or is there a faster
non-asymptotic mechanism? The expected empirical signature of purely asymptotic
sharpening is a monotone approach to stable partition over repeated cycles —
not an immediate post-consolidation step. Testable by ablation study on
consolidation phase frequency and partition stability measurement.
Source: `docs/context_navigation/mode_scope_regime_audit.md` §2.4.
Priority: medium.

*Theoretical analysis (session 2026-03-29):* The K6 prediction is clear: ε-plateau
width should increase monotonically across consolidation cycles (smooth, not step-like).
The alternative — discrete reorganization — would produce step-like jumps concentrated
at specific consolidation cycles. Operationalization: measure ε-sweep N(ε) plateau width
after each consolidation cycle and plot against cycle count. Monotone smooth → K6 confirmed.
Practical implication: consolidation effects require multiple cycles to be visible;
single-shot post-consolidation testing is insufficient to evaluate the mechanism.
See `docs/notes/research_journal.md` Session 2026-03-29.
Status: partially_answered — hypothesis and measurement protocol defined; awaits experiment

---

**Q_NEW_18 — Non-axis-aligned regime boundaries as BC interaction signatures**
In the 2D cover height analysis of CASE-0002 (κ × γ), cover-height contours
are diagonal in the (κ, γ) plane — not parallel to either BC axis. This indicates
that the regime boundary is a function of both BCs jointly, not independently.
Formally: the separation condition Δ is a constraint on (BC₁, BC₂) jointly,
not a product condition Δ₁ × Δ₂.
Open questions:
1. Does the ARW scope formalism currently permit joint-BC separation conditions?
2. If not, should Δ be extended to allow interaction terms (e.g. Δ = {κ·γ > c})?
3. How does the BC interaction structure relate to the BC class taxonomy
   (coupling vs. restriction vs. modulation)?
4. Can the degree of BC interaction be quantified from the cover-height field
   (e.g. angle of contour lines from axis-aligned)?
Reference: `docs/notes/research_journal.md` session 2026-03-28 (II), Finding 4.
Status: open
