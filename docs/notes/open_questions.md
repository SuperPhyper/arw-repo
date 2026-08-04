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

*Partial structural response (2026-04-29, Felder 2026):* σ_Δ(x) = sup_{δ∈Δ} |O(x+δ) − O(x)|
is now a named pointwise quantity. The admissible resolution regime is defined as
sup_x σ_Δ(x) < ε < ε*(O,X_B), where the sup is the binding constraint. This makes
the *effective* ε requirement state-dependent in a specific sense: wherever σ_Δ(x) is
large, the local stability requirement on ε tightens. However, this does not yield a
formally state-dependent ε in the scope tuple — ε remains a global scalar. The question
of whether and how to extend the scope tuple to allow ε: X_B → ℝ₊ remains open.
Status: partially addressed via σ_Δ(x) — formal scope-tuple extension open

**Q3 — Multiple ε for multiple observables**
When Π = {π₁, π₂, ...}, each observable may have a natural resolution scale.
What is the joint admissibility condition?
Is ε a vector, a matrix, or a function on the product space?

*Empirical evidence (CASE-0003, 2026-03-12):* Double pendulum with lambda_proxy
and var_rel: only 37% agreement across ε-values. var_rel (span=0.297) requires
ε ≈ 0.015; lambda_proxy (span=0.069) requires ε ≈ 0.008. A single shared ε
cannot satisfy both. This operationalises the question: the εᵢ vector is the
minimal adequate description for multi-observable scopes.

*Partially resolved at the definitional level (2026-04-29, Felder 2026 §8):*
The admissible resolution regime for a k-observable scope is a **region in ℝᵏ**:
{ (ε₁,...,εₖ) : ∀ i: sup_x σ_Δ(x; πᵢ) < εᵢ < ε*(πᵢ, X_B) }.
The box-shaped approximation currently used in ARW (component-wise I_εᵢ) is a
special case assuming decoupled observables. Cross-observable ε constraints
(when the stability of one observable depends on the resolution of another)
remain open. See also Q-NEW-COVER-2 below.
Status: partially resolved — definitional; cross-observable constraints open

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

*Partially resolved (2026-04-29, Felder 2026):* The observable cover C_ε is a
Čech cover — the same object studied in persistent homology. The admissible
resolution regime (sup σ_Δ, ε*) is the ARW counterpart to the persistence window
in which topological features are stable. The observable-space cover height method
(`docs/advanced/observable_space_cover_height.md`) accumulates evidence across ε
scales analogously to persistence diagrams, but without full topological bookkeeping.
The formal correspondence to persistent homology — in particular whether ARW cover
height is computable from a persistence diagram and vice versa — remains open.
See `docs/core/observable_information.md` for the connection.
Status: partially resolved — Čech cover link established; persistence correspondence open

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

*Decision (2026-06-10, monograph audit repair WP-B3):* **(c) — the ART layer.**
The structure of X is carried by the domain instantiation: each ScopeSpec /
signature-first document declares the state-space structure its observables
require (as the pre-scopal substrate conditions A0–A6 already do in practice).
The scope tuple S = (B, Π, Δ, ε) remains unchanged; B keeps its frozen meaning
(selection of X_B ⊆ X, not declaration of X's structure). Consequence: ARW-core
statements are conditional on a well-defined X, and that conditionality is made
explicit at the ART level, not absorbed into the tuple. Rationale: keeps
ARW-core lean; avoids semantic overloading of B; matches existing practice in
signature-first documents. Canonization path: note in `docs/glossary/scope.md`
(scheduled with the INC-01 Čech-cover update) and Part VII V1 of the monograph.
Status: answered (by architectural decision; formal meta-layer formulation
remains available as future refinement if Part VII V2 requires it)

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

*Second, independent partial resolution (2026-07-08, `mode_scope_regime_audit.md` §2.6):*
χ_mode is formally derived as the derivative of soft regime-cell occupancy
(p_i(c) = softmax_i(-β·d_i(c))) with respect to context_load, giving
χ_mode(c) = ∂p_i(c)/∂c. Bottom-up BC structure: **R⁴·A·Approx** (more Restriction-heavy
than r_ss/var_rel, and — like lambda_proxy — carries an Approximation component from the
finite-difference estimator). The local Lipschitz constant at a two-class decision boundary
is L(c*) ≈ (β/4)·max|∂d_i/∂c|; a naive finite-difference estimator reproduces the C1
structure (2026-06-02 σ_Δ-proxy correction) exactly — one-sided underestimation as the
transition sharpens (L(c*)_true/χ_mode^FD ≈ h/w). The local-max estimator
χ_mode^LM(c) := sup_{h'≤r} |p_i(c+h') − p_i(c)|/h' is proposed as the correction, by direct
analogy with Corollary 1. This is a **separate candidate operationalization from the
2026-03-29 mode-switch-rate proxy above** — not a refinement of it. Both remain open until
tested against trajectory data; they are not yet known to agree or disagree empirically.
Status: partially_answered — two independent candidate operationalizations now exist
(mode-switch-rate, 2026-03-29; χ_mode^LM softmax-occupancy derivative, 2026-07-08);
neither has been empirically validated against trained-agent trajectory data.

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

**Q-CNS-06a — Should β (softmax assignment temperature) be added to B_emergent?**
χ_mode^LM's local Lipschitz constant L(c*) ≈ (β/4)·max|∂d_i/∂c| depends on β, the softmax
temperature of the regime-assignment procedure, independently of system dynamics — unlike
κ_c or E_sep, this divergence is governed by the assignment procedure itself, not enforced
by the underlying dynamics (not a Z_shared-in-the-K1-sense divergence). β is not currently
part of `B_emergent` in `context_navigation_emergent_modes_experiment.md`.
Source: `docs/context_navigation/mode_scope_regime_audit.md` §2.6.
Priority: medium.
Status: open

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

---

## Cover Stability and Observable Information (Felder 2026)
*(Added: session 2026-04-29)*

**Q-NEW-COVER-1 — Completeness of a set of observables relative to a system**
When is a set of observables *complete* relative to a system — i.e., when does
their joint cover structure resolve all relevant distinctions in X_B? Is there a
formal ARW condition for observable completeness that goes beyond individual
sufficiency (F1 not triggered) and individual stability (F-gradient not triggered)?
Reference: Felder 2026 §8 (multi-observable generalization).
Status: open

**Q-NEW-COVER-2 — Cross-observable ε constraints in the admissible region ℝᵏ**
The admissible resolution regime for a k-observable scope is a region in ℝᵏ.
The box-shaped approximation (component-wise I_εᵢ) assumes decoupled observables.
Are there systems where the stability of one observable constrains the admissible
ε of another? Under what structural conditions do cross-observable ε constraints arise,
and how would they be detected empirically (e.g. via the joint ε-sweep)?
Reference: Felder 2026 §8; `docs/core/observable_information.md` §Scope-Level.
Status: open

**Q-NEW-CROSS-1 — Physical correlates of descriptive crossovers**
Under what conditions does a descriptive crossover (Z_cover ∩ R(π) ≠ ∅)
have a physical correlate — e.g. an anharmonic crossover, a mode coupling threshold,
a soft mode — versus arising purely from the choice of observable and (ε, Δ)?
Is the crossover always visible as a gradient discontinuity, or can it arise
from a smooth but steep increase in |∇O|?
Reference: Felder 2026 §6.2; `docs/glossary/observable_range.md`.
*Update 2026-06-10:* the original motivating instance — the pendulum "secondary ridge
at E ≈ ω₀²" — was withdrawn 2026-06-02: it was the true separatrix under a wrong
E_sep = 2ω₀² convention (bugfix report P-0; research_journal.md 2026-06-02). The
question stands in general form, but there is currently **no confirmed empirical
instance** of a pure descriptive crossover (σ_Δ ≥ ε within R(π) without a regime
change). Identifying one is now part of the question; CASE-20260315-0008 (pitchfork,
flat-side geometry) is a candidate system.
Status: open

**Q-NEW-CROSS-2 — Analytic Lipschitz constant for ARW observables**
Can the Lipschitz constant L(x) be computed analytically for observables where
the operator structure is known (e.g. r_ss, var_rel, PLV)?
What does L(x) look like in Z_shared — does it diverge at the transition in
the same way for all class-E observables?
Reference: Felder 2026 Corollary 1 and Remark 4; `docs/core/cover_stability_criterion.md` §4.
Status: open

---

## Generator Admissibility Taxonomy
*(Added: session 2026-05-07)*

**Q-GEN-01 — Exhaustiveness of the three-type generator admissibility taxonomy**
- **Status:** open
- **Question:** Is the three-type generator admissibility taxonomy exhaustive?
  Candidate gap: non-autonomous generators may produce failure geometries not
  captured by Type I, II, or III. *(Terminology: types renamed 2026-07-17 —
  domain-boundary failure / branch-selection failure / joint-constraint
  incompatibility; see generator_admissibility_taxonomy.md.)*
- **Registered:** 2026-05-07
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md

**Q-GEN-02 — Signature-first inference for generator failure type**
- **Status:** partially answered (2026-05-07)
- **Question:** Can generator failure type be inferred purely from operator
  signatures (S1–S5)?
- **Partial answer:** Yes for Type I (S1/S2/S4/S5 dominant) and Type II
  (S3 dominant). No for Type III — requires explicit conflict analysis of K.
- **Remaining open:** Formal signature-first protocol for Type III.
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md

**Q-GEN-03 — Correct ARW formalization of the generator G**
- **Status:** partially answered (2026-05-07)
- **Question:** What is the correct ARW formalization of the generator G?
- **Partial answer:** G = (Λ, Σ, φ, C). φ: Λ → (B, Π) partial instantiation.
  A(G) and A_f(G | C) formally defined.
- **Remaining open:** Formal topology conditions on Λ per failure type;
  formal A_f / A_h boundary independent of specific C.
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md

**Q-GEN-04 — Minimal C for non-empty A_f per failure type**
- **Status:** open
- **Question:** What is the minimal C that makes A_f(G | C) non-empty for
  each generator failure type?
- **Registered:** 2026-05-07
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md

**Q-GEN-05 — Forcing vs. Symmetry Breaking in Type II canonical cases**
- **Status:** open
- **Question:** Does the Forcing reformulation as inter-regime coupling change
  the identification of Type II canonical cases (e.g. ghost sector in quadratic
  gravity: Forcing incommensurability, Type II-a, or degenerate vacuum sectors,
  Type II-b under the proposed split)?
- **Registered:** in source doc 2026-05-30; registered here 2026-07-17 (late —
  found unregistered during the ID-collision sweep of the Part VI revision
  session; the pulse §5 prefix map claimed Q-GEN-01–04)
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md

**Q-GEN-06 — Derivation of minimum C components from the five relation types**
- **Status:** partially answered (see docs/notes/c_components_derivation_attempt.md:
  C is not arbitrary; sub-questions Q-GEN-06a/06b remain open there)
- **Question:** Is there a derivation of the minimum C components from the five
  relation types (C and the Restriction meta-relation being formally parallel)?
- **Registered:** in source doc 2026-05-30; registered here 2026-07-17 (late,
  same sweep as Q-GEN-05)
- **Source:** docs/art_instantiations/generator_admissibility_taxonomy.md;
  docs/notes/c_components_derivation_attempt.md

**Q-GEN-07 — Structural sub-typing of Type II (branch-selection failure)**
- **Status:** open
- **Question:** Type II groups heterogeneous phenomena — mathematical
  non-uniqueness, coexisting stable attractors, epistemic undecidability,
  normative underdetermination — unified only by the external-selection-criterion
  feature. Do these divide along structural lines? Two candidate axes exist:
  the operator-side S3/S6 split already proposed under Q-GEN-01 (Type II-a
  Forcing incommensurability vs. II-b Symmetry-Breaking bifurcation), and the
  interpretive-side axis above (mathematical / attractor / epistemic /
  normative). Are the two axes aligned, orthogonal, or reducible?
- **Registered:** 2026-07-17 (from monograph Part VI §6.2, external-review
  revision; terminology per the same-day failure-type rename)
- **Source:** monograph Part VI §6.2; docs/art_instantiations/generator_admissibility_taxonomy.md
  (Q-GEN-01 update 2026-05-30)

---

## Epistemic Context and Functional Admissibility
*(Added: session 2026-05-07)*

**Q-EPO-01 — Formal ordering of the seven A_f criteria**
- **Status:** open
- **Question:** Can the seven A_f criteria be formally ordered by strength?
  Is there a minimal sufficient subset per failure type?
- **Registered:** 2026-05-07
- **Source:** docs/art_instantiations/epistemic_context_and_functional_admissibility.md

**Q-EPO-02 — Compression viability κ and ARW cover metrics**
- **Status:** partially answered (2026-05-07)
- **Question:** Is compression viability κ formally related to existing ARW
  cover metrics? Is cover height the formal bridge?
- **Partial answer:**
  - Local level: h_norm(b_i) = h(b_i)/h_max is a formally grounded proxy
    for κ_local. Three structural alignments confirmed: (1) regime interior =
    high h = high κ; (2) transition regions = low h = low κ (Z_cover active);
    (3) ε-persistence of h = compression robustness required by κ.
  - Global level: κ(G,C) ≈ E_λ[h_norm(φ(λ))] — expectation of h_norm over
    the scope family — is the generator-level bridge. This is a hypothesis,
    not yet proven.
  - Operationalization: h_norm is immediately computable via existing pipeline
    (cover_observable_space.py). Cross-scope aggregation requires new pipeline
    step.
- **Remaining open:** Formal proof of global correspondence; pipeline for
  cross-scope h_norm aggregation; tightness conditions (monotone vs.
  non-monotone observables).
- **Source:** docs/art_instantiations/epistemic_context_and_functional_admissibility.md;
  session finding documented in docs/notes/research_journal.md (session 2026-05-07)

**Q-EPO-03 — Relationship between C and the three generator failure types**
- **Status:** open
- **Question:** What is the formal relationship between C and the three
  generator failure types? Does each type impose a characteristic structure
  on the minimum C for non-empty A_f?
- **Registered:** 2026-05-07
- **Source:** docs/art_instantiations/epistemic_context_and_functional_admissibility.md

**Q-PROJ-01 — Structural requirements on successor scopes from failure mode**
- **Status:** open
- **Question:** The failure structure at an admissibility boundary (F-type
  mode, region of B, direction of approach) may carry partial information
  about what a more complete parametrisation would need to provide. An F0
  failure identifies an observable class that fails here — which implies a
  structural requirement on any observable that would succeed here. Can ARW
  generate such structural requirements systematically from the failure mode?
  That is, can the description of where and how a scope fails constrain the
  form of a successor scope — without projecting the current scope's content
  beyond its boundary?
- **Registered:** 2026-05-09
- **Source:** docs/notes/scope_failure_and_ontological_projection.md
- **Note:** Distinct from the projection error (Section 7 of source doc):
  asks not what the system is beyond the boundary, but what a valid
  description beyond the boundary would need to structurally provide.

---

## Diagnostic Workflow Ordering
*(Added: session 2026-05-10)*

**Q-CTX-01 — stability_mask_exclusion vs. ε↑ as primary F-gradient action**
- **Status:** open
- **Question:** Does `stability_mask_exclusion` need to be the primary action
  listed for F-gradient (before ε↑) in diagnostic workflows, or is ε↑ with a
  correct ε*(O,X_B) check operationally equivalent? In the eval run (2026-05-10),
  both approaches produced correct downstream results, but the ordering question
  was not resolved: a stability mask that excludes x where σ_Δ(x) ≥ ε preserves
  the cover structure in the remaining region, while ε↑ expands the resolution
  window globally — which may merge adjacent regimes. The two actions are not
  interchangeable when the high-gradient region is interior to X_B (not at a
  boundary).
- **Registered:** 2026-05-10
- **Source:** docs/notes/research_journal.md (Session 2026-05-10, Open questions);
  docs/meta/context_map/context_map_falsification_bc.md (F-gradient entry)
- **Related:** F-gradient falsification category (§3 of repo context); Q2 (state-dependent ε)

---

## Transfer & Within-Class BC Structure
*(Added: session 2026-06-02)*

**Q-REL-04 — Does dimension growth constitute a BC-structural break within the Dissipation class?**
- **Status:** **answered** (2026-06-02) — **STRUCTURAL BREAK, not a reparametrisation.**
- **Question:** A dimension-growing order axis (population growth N(t)=N₀e^{ρt} feeding new
  susceptibles) was conjectured to be either a genuine BC-structural break within the
  Dissipation class or merely a reparametrisation of stationary Dissipation.
- **Finding (answered):** Resolved via the intrinsic dynamics of the closed (s,i) fraction
  system of the growing-population SIR (ds/dt = ρ(1−s) − βsi, di/dt = i(βs − γ_r − ρ)), **not**
  via the transfer metric Φ. The ρ(1−s) replenishment term creates a new isolated stable
  endemic attractor (s*,i*>0) via a transcritical bifurcation at ρ*=β−γ_r; the stationary
  system (ρ=0) has only a degenerate line {i=0} with no endemic state. Creating a new isolated
  attractor is a topological change of the phase portrait, which a reparametrisation cannot
  produce. In ARW terms the regime partition **gains a regime** under dimension growth →
  structural break. Scope: this instantiation (susceptible replenishment), not a universal
  theorem about all dimension growth.
- **Why not Φ:** the transfer metric was shown not to resolve even between-BC-class distance
  (decoupling controls D-CTRL-1/2), and the locked observable g_max_percapita is F1-insufficient
  at the working ε (span 0.018 ≪ ε=0.05 → N=1). The earlier Φ=1.0 "reparametrisation" result
  was withdrawn (placeholder data + v1 metric defect).
- **Registered:** 2026-06-02 (referenced earlier in the dissipation-growth pre-registration but
  never previously entered here)
- **Source:** docs/notes/research_journal.md (Session 2026-06-02); external Simulationen
  workspace transfer_test_dissipation_growth/QREL04_RESOLUTION.md (+ qrel04_phase_portrait.png)
- **Related:** transfer-metric defects (pipeline/transfer_v2.py); Q9 (scope transitions vs.
  phase transitions)
- **Formal background (from the pre-registration):** the structural lever is the
  non-commutativity of Aggregation over a dimension-growing index set with Dissipation:
  in the dimension-constant case A_T · D = D · A_T (temporal aggregation transparent to
  BC class); in the dimension-growing case A_{N(t)} · D ≠ D · A_{N(t)}. The intrinsic-dynamics
  resolution confirms that this non-commutativity is structurally consequential
  (new isolated attractor via transcritical bifurcation at ρ* = β − γ_r).
- **Residual open sub-questions:**
  - (a) *Camouflage / observable selection:* temporal averaging suppresses exactly the
    heterogeneity that dimension growth introduces; a non-averaging observable over the
    ordering ≤ is required for any partition-level detection of the break. Selection and
    validation of such an observable remains open methodologically.
  - (b) *Multi-axis partial orders:* the pipeline is architecturally single-axis (ε-sweep
    over one parameter). Partial orders with incomparable pairs are outside the current
    apparatus; the answered case covers only the single-axis (monotone time) instance.
- **Note on a withdrawn duplicate (2026-06-10):** an earlier duplicate entry of Q-REL-04
  ("BC-Class Relational Structure" section) carried status *open* and cited Φ=0.9983 /
  Φ=0.5317 as calibration of Φ's "dynamic range" for BC-class distance. Those values were
  v1-metric results; the v1 ordering was withdrawn as a regime-count artifact (see Q-REL-05
  and research_journal.md 2026-06-02). The duplicate has been merged into this entry.

**Q-REL-05 — Does the transfer metric Φ carry any genuine BC-class distance signal?**
- **Status:** open, expected to resolve negatively (reformulated 2026-07-11 per the
  WP-A3 decision, `docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md`) — this
  is a deliberate change from a previously neutral "open" framing. **Partitions are
  many-to-one outputs of their generators**: distinct BC structures can produce
  near-identical partitions on normalised axes, so no partition-level construction can *in
  principle* recover BC-class distance. The expectation of a negative resolution should be
  stated as such (not left neutral) wherever this question is cited, per the decision note.
  Empirical confirmation would still require the answer below to remain "no" under further
  testing — this is a stated expectation grounded in the information-theoretic argument, not
  a proof; it should be revised back to neutral if a counter-construction is ever found.
- **Question:** With the v1 PCI defect removed (overlap-based PCI in transfer_v2), same-class and
  cross-class case pairs are still statistically indistinguishable in PCI_real once regime count
  is controlled (D-CTRL-1). Is there *any* construction on the induced partition that recovers
  BC-class distance, or must BC-class distance be measured on the operator signatures (S1–S5)
  directly rather than on the partition?
- **Path forward (WP-A5, proposed 2026-07-02, not yet built):** a signature-comparison
  artifact (working name `SignatureTransfer.json`) alongside `TransferMetrics.json`, making
  transfer a two-stage workflow — Stage 1 partition filter (Φ and companions, necessary
  condition only), Stage 2 signature comparison (Σ-level evidence, the structural claim).
  This would make Q-REL-05 empirically testable inside the pipeline rather than only
  argued from the D-CTRL results. Not yet implemented in this repo as of 2026-07-11.
- **Registered:** 2026-06-02
- **Source:** docs/notes/research_journal.md (Session 2026-06-02); Simulationen
  DECOUPLING_CONTROLS_RESULTS.md; reformulated 2026-07-11 per
  `docs/notes/decision_note_WP-A3_transfer_reframing_2026-07-02.md`

**Q-REL-08 — Canonical normalization for TBS_norm**
- **Status:** open
- **Question:** TBS_norm normalizes θ* by the *explored* sweep range, which is
  a design choice of the case, not a property of the system: widening a sweep
  moves the same threshold to a smaller fraction without any structural change.
  Is there a canonical or functionally grounded reference range — candidates:
  natural domain of the control parameter, characteristic scale, position of
  the first structural singularity, empirically reachable range, dimensionless
  control parameter — that makes TBS_norm comparable across independently
  designed sweeps? Until resolved, the sweep-window sensitivity band
  (transfer_v2) mitigates but does not remove the range dependence.
- **Registered:** 2026-07-17 (from the monograph Part VI external-review
  revision; the reviewer's sweep-enlargement objection is the operative
  counterexample). Numbered in the transfer-findings Q-REL sub-series (04–05);
  the three-origin fragility of the Q-REL prefix is known — consolidation
  pending per pulse §5.
- **Source:** monograph Part VI §6.3 + docs/notes/part_VI_revision_spec_external_review_2026-07-17.md
  (book workspace); docs/bc_taxonomy/transfer_distortion_metrics.md (Metric 2)

---

*(Section "BC-Class Relational Structure" removed 2026-06-10: it contained a duplicate
Q-REL-04 entry with stale status `open` and withdrawn v1-Φ calibration values. Its
formal content and residual sub-questions are merged into the answered Q-REL-04 entry
above; see also Q-REL-05.)*

---

## Scope-Component Conflict Typology
*(Added: session 2026-07-11, from docs/notes/scope_component_conflict_typology.md)*

**Q_NEW_A — Does "aggregation level" map onto ε alone, or is scale-equivocation a compound (ε + Π) conflict?**
Prerequisite for the typology's ε-conflict row (§1) to be considered well-defined.
A worked case (capital growth vs. productivity, §6 of the source note) suggests the
answer is case-dependent: pure ε only when aggregation changes resolution on a fixed
projection; Π-conflict when new codetermining variables enter the projection itself;
B-conflict when a different generator entirely produces the same observable label.
One confirmed case is not sufficient to close this.
Source: `docs/notes/scope_component_conflict_typology.md` §2.
Status: open

**Q_NEW_B — Can prediction 2 (§3 of the source note) be operationalized on a documented controversy?**
Needs a real controversy with published positions from ≥2 schools sharing ≥2 observables,
to test whether the hardest disagreements concentrate on Δ (admissible-perturbation
windows) rather than Π (which observables).
Source: `docs/notes/scope_component_conflict_typology.md` §3.
Status: open

**Q_NEW_C — Is the four-type conflict classification exhaustive, or do mixed conflicts dominate empirically?**
If mixed conflicts dominate, the typology functions as a decomposition basis rather
than a partition of controversies.
Source: `docs/notes/scope_component_conflict_typology.md` §1/§6.
Status: open

**Q_NEW_D — Does the typology transfer outside economics?**
The typology is stated at ARW level (domain-neutral); untested outside the originating
economic-schools instance, e.g. against a natural-science priority dispute.
Source: `docs/notes/scope_component_conflict_typology.md` §4.
Status: open

---

## J-Space / Regime-Occupancy Signature
*(Added: session 2026-07-11, from docs/related_fields/j_space_arw_signature_hypothesis.md)*

**Q-REL-06 — Does an occupancy-based χ_mode^J show the predicted finite-difference bias at task-transition points?**
Applied to this project's own agent at within-context sweep resolution (c = position in
context). Prediction: χ_mode^J peaks at genuine topic/task transitions, and a naive
finite-difference estimate exhibits the same one-sided underestimation bias as χ_mode
(§2.6 of `mode_scope_regime_audit.md`), requiring the local-max correction χ_mode^LM.
Only testable once the Emergent Modes Experiment produces trajectory data; no access to
Anthropic's internal J-Lens tooling exists to test this against the source finding directly.
Source: `docs/related_fields/j_space_arw_signature_hypothesis.md` §5.
Priority: medium.
Status: open

**Q-REL-07 — Can "online occupancy signature" be principledly distinguished from "static representation geometry" in third-party interpretability reporting generally?**
Motivated by an initial informal framing that conflated Anthropic's J-Space (online,
per-forward-pass) with static embedding geometry (see source note §2/§3 for the correction).
Source: `docs/related_fields/j_space_arw_signature_hypothesis.md` §8.
Priority: low.
Status: open

*(Note: these were originally proposed as Q-REL-01/02 in the source note; renumbered on
import 2026-07-11 to avoid a collision with the pre-existing Q-REL-01/02 in
`docs/bc_taxonomy/bc_relational_structure.md`, an unrelated Σ-persistence topic. The repo
now has three independent Q-REL sub-series — 01–03, 04–05, 06–07 — from different import
sessions; check `docs/meta/DOC_INDEX.md` / grep before assigning further Q-REL numbers.)*

---

## Scope-Family Flow / RG-Analogue Audit
*(Added: session 2026-07-11, from docs/notes/scope_family_flow_and_kuramoto_limit_audit.md)*

**Q-INV-03 — Does the ε-induced scope family 𝒮_α(b) carry a directed flow structure under δ?**
**Status: resolved (definitional).** `bc_relative_observable_indistinguishability.md`
defines N_α^δ(b) as a genuine metric ball, so nesting is automatic
(δ₁ < δ₂ ⟹ N_α^{δ₁}(b) ⊆ N_α^{δ₂}(b)) and Δ_α O(b;δ) is monotone non-decreasing in δ,
guaranteeing a well-defined directed limit at δ → sup I_α(b). If d_α is a genuine metric,
the family is additionally sub-additive under composition (containment, not exact
semigroup composition) — the same epistemic status real RG flows have away from a fixed
point. Feeds into Q-INV-02 as a partial answer (see that entry's annotation in
`docs/advanced/invariance_as_scope_persistence.md`).
Source: `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md` §3.
Status: resolved

**Q-INV-04 — Does the δ → sup I_α(b) collapse limit coincide with the N → ∞ Emergent-Aggregation limit?**
Theoretically motivated via finite-size scaling (the Lipschitz blow-up L(κ)→∞ at κ_c,
already established for CASE-0001, is the same underlying divergence responsible for
finite-N transition-window narrowing in critical-phenomena theory) but empirically
untested — CASE-20260311-0001 fixes N=500 with no N-sweep in the current data. Proposed
test: extend CASE-0001 (or a variant) with an N-sweep (N ∈ {50,100,200,500,1000,2000})
around κ_c ≈ 1.475, compare finite-N transition width Δκ(N) scaling against I_α(κ)
narrowing scaling. If confirmed: would reframe RG universality as an internal special
case of ARW scope-invariance rather than an external analogy (speculative, conditional —
see source note §7 for the full, explicitly-flagged-as-not-established consequence chain).
Source: `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md` §4.
Status: open

---

## Σ Extraction from Observables (Q-EXT)
*(Prefix registered 2026-07-14. The questions were posed 2026-05-30 in
`docs/advanced/bc_signature_extraction_observables.md` but never registered here —
which allowed a silent collision: `docs/advanced/extended_z_observable_necessity.md`
independently used Q-EXT-01–06 for unrelated Z(π) questions. Decision 2026-07-14
(Rico): the extraction series keeps Q-EXT; the Z-observable series is renumbered
Q-ZOBS, see below.)*

**Q-EXT-01 — Can operator signatures be reliably distinguished in cover height profiles without model equations?**
- **Status:** open — first empirical evidence positive (Coupling vs. Restriction discriminant
  profiles separate cleanly in two clean systems; see `experiments/sigma_extraction_bc_signatures.md`).
- **Source:** `docs/advanced/bc_signature_extraction_observables.md`;
  `experiments/sigma_extraction_kuramoto_noise.md` (noise-robustness proposal);
  validation programme: `experiments/sigma_extraction_validation_plan.md` (imported 2026-07-14).

**Q-EXT-02 — What are the minimum data requirements for stable Σ extraction (sweep density, observable count)?**
- **Status:** open — Level-1 tasks of the validation plan (sparse ARW-case sweeps, n=12–26)
  are designed to bound this.
- **Source:** as Q-EXT-01.

**Q-EXT-03 — Σ stability under observable choice: does a different observable on the same system yield the same Σ?**
- **Status:** open — overlaps with Q_NEW_9/Q_NEW_11 (observable-BC vs system-BC); the planned
  Φ_obs test (WP-D3: CASE-0001 with r_ss vs. σ²(θ)) bears on it.
- **Source:** `docs/advanced/bc_signature_extraction_observables.md` §"multiple observables".

---

## Z-Observable Necessity (Q-ZOBS)
*(Renumbered 2026-07-14 from a colliding Q-EXT-01–06 series. Canonical table with all six
questions and priorities: `docs/advanced/extended_z_observable_necessity.md` §8. All open.
Registered here as a prefix reservation; extend the source document, not this entry.)*

---

## Qualitative Scope-Signature Abstraction (Q-QSC)
*(Prefix registered 2026-07-14 on import of `docs/advanced/qualitative_scope_signature_abstraction.md`
(Kaffeehaus session 2026-07-11). Collision check: prefix previously unused.)*

**Q-QSC-01 — Does a qualitatively-assigned BC signature survive contact with a formal pipeline case for the same system?**
- **Status:** open. Candidate test: minimal toy model of gravity-driven channel flow
  (qanat structure); check whether bottom-up extraction returns R·D as QSA predicted without data.
- **Source:** `docs/advanced/qualitative_scope_signature_abstraction.md`.

**Q-QSC-02 — Does QSA signature-equivalence predict successful engineering transfer, or only surface resemblance?**
- **Status:** open. First informal case: qanat-derived passive cooling vs. Mulden-Rigolen
  retention (both R·D) from the source session.
- **Source:** as Q-QSC-01; relates to `docs/notes/cross_scope_causal_construction.md`
  (label matching ≠ generator matching) and, via the two-stage transfer criterion,
  to Q-REL-05.

---

## Part VII Formalisation Round (registered 2026-07-17)

*(Source: monograph Part VII external-review revision; repo-side reconciliation
session 2026-07-17. Q_NEW numbering continues after Q_NEW_19–23, which are
claimed by `docs/advanced/admissible_resolution_lower_bound.md` — collision
check done.)*

**Q_NEW_24 — Should the falsification severity enum be split into claim-impact and repair-action axes?**
- **Status:** open (schema question; enum is a frozen repository convention, GUARD-3)
- **Question:** The severity enum {observable_replacement, sweep_refinement,
  scope_rejection} names licensed repair actions, but fuses *claim impact*
  (local / observable-class / scope-level) with *recommended action* — a
  high-impact failure can still be repaired by an observable swap. Should the
  schema carry event type × claim impact × action as separate fields?
- **Registered:** 2026-07-17, deferred rather than silently adopted in
  monograph Part VII V3.1.
- **Source:** monograph Part VII V3.1; schemas/ (GUARD-2/3).

**Q_NEW_25 — General regime construction beyond the 1D sweep: admissible-transition relation and attributed transition graph**
- **Status:** open
- **Question:** The operative regime construction (ε-adjacency graph on an
  ordered sweep) defines regimes of the observable image along the swept path
  only. The general notion — components under an *admissible-transition
  relation* (δ-reachability under Δ) on the full effective domain — is not
  constructed. Its metric-level counterpart is the Δ-induced or **attributed**
  transition graph (edges carrying ε_merge, hysteresis, order of contact α,
  signature type, BC label), which is also the condition for SDI to carry
  information independent of regime count (WP-A4 amendment 2026-07-17).
  Sub-questions: value-coincident distinct basins; multi-dimensional
  observable images; image-connectivity vs. state-space admissibility.
- **Registered:** 2026-07-17.
- **Source:** monograph Part VII V1.2 (scope limit) + V4.2 (SDI disposition);
  `docs/bc_taxonomy/transfer_distortion_metrics.md` (SDI section).

---

## Σ Persistence / Signature Structure (Q-SIG)
*(Prefix registered 2026-07-17. The questions were posed in
`docs/advanced/bc_signature_persistence_and_dominance.md` (2026-05-30 cluster)
but never registered here — same failure mode as Q-GEN-05/06 and Q-EXT.
Numbering starts at 02 in the source doc; there is no Q-SIG-01 — recorded
as-is, do not reuse 01 without checking the source doc first.)*

**Q-SIG-02 — Intrinsicness of η_i**
- **Status:** open
- **Question:** Is the persistence interval of a BC class intrinsic to the
  generator, or dependent on the full constellation of active classes (and on
  the observer-declared reference scale ε₀ in η = −log(ε/ε₀))?
- **Source:** docs/advanced/bc_signature_persistence_and_dominance.md §7.

**Q-SIG-03 — Monotonicity of persistence intervals**
- **Status:** open
- **Question:** Is each class's activity a single η-interval, or can a class
  deactivate and re-activate across resolution?
- **Source:** docs/advanced/bc_signature_persistence_and_dominance.md §7.

**Q-SIG-04 — Restriction as meta-BC in the persistence measure**
- **Status:** open
- **Question:** Does Restriction enter the persistence measure as a class, or
  define its domain?
- **Source:** docs/advanced/bc_signature_persistence_and_dominance.md §7.

**Q-SIG-05 — Projection loss for Σ read in projected space**
- **Status:** open
- **Question:** What transfer claims are lost when Σ is read only in the
  observable's projected space?
- **Source:** docs/advanced/bc_signature_persistence_and_dominance.md §7.

**Q_NEW_26 — Computing assignment instability χ_{Δ,ε}**
- **Status:** open (implementation gap)
- **Question:** The exact boundary-state indicator χ_{Δ,ε}(x) = 1[∃δ ∈ Δ :
  r_ε(T_δ x) ≠ r_ε(x)] (monograph Part VII Def 6a) is computed nowhere: all
  pipeline stability masks use the σ_Δ proxy, whose reliability degrades near
  boundaries — exactly where χ matters. What is the cheapest faithful
  estimator of χ (perturbed re-partitioning per δ-sample? perturbed-graph
  component comparison C(G_ε^δ) vs C(G_ε)?), and how far does the σ-mask
  diverge from the χ-mask on the reference cases? Also carries the τ_∂
  boundary-fraction criterion for F-gradient, which is currently
  σ-estimated.
- **Registered:** 2026-07-18.
- **Source:** monograph Part VII V2.3/V3.1 (round-3 revision);
  docs/glossary/perturbation_spread.md.

---

## Outlook — Abstraction Chains (registered 2026-07-18)

*(Source: docs/notes/transfer_deflation_and_abstraction_chains.md §4, imported
2026-07-18 from the monograph workspace during Part IX drafting. Its §6
registration block was written 2026-07-02 but never executed — same failure
mode as Q-GEN-05/06, Q-EXT, Q-SIG. Collision check: Q_NEW_19–23 claimed by
admissible_resolution_lower_bound.md; 24–26 taken.)*

**Q_NEW_27 — Where does the necessity of the abstraction chain sit?**
- **Status:** open
- **Question:** "A deep chaining of abstraction arises necessarily" — candidate
  loci: (a) boundedness of any finite describer (cognition); (b) a property of
  description/representation as such; (c) temporally organized dynamics under a
  finite-capacity bound, proposed as the *common root* of (a) and (b). (c)
  needs an independent dynamical anchor to avoid survivorship-circularity and
  self-reference to ARW's own persistence notion (σ_Δ, ε). Fallback: the
  necessity claim may be false; then abstraction chains are an empirical
  regularity, not a structural consequence. Decides whether the ARW outlook is
  about cognition-under-time, representation-in-general, or a dynamical
  substrate beneath both.
- **Registered:** 2026-07-18.
- **Source:** docs/notes/transfer_deflation_and_abstraction_chains.md §4;
  monograph Part IX §9.2.5 (prose) + §9.4 (formal limits) + §9.1 (ID listing).

---

## Vertical Transfer — Inductive Strengthening and Scale-Gap Ambiguity (Q-STR, registered 2026-07-25)

*(Source: docs/notes/inductive_strengthening_cascade_closure.md §6 and
docs/notes/scale_gap_ambiguity_audit_stability.md §6, both drafted offline and
imported as a pair 2026-07-25. Collision check performed on import: the `Q-STR-`
prefix was unused across open_questions.md and docs/notes/ — no collision, unlike
the Q-REL-01/02 case. The cluster concerns the **resolution axis of a single
system** (vertical structure), and is deliberately not merged with the horizontal
system-to-system transfer cluster Q-REL-01–05.)*

**Q-STR-01 — Existence of a cascade-closed strengthening**
- **Status:** open
- **Question:** Given a scope family {S_ρ = (B, Π_ρ, Δ, ρ)} and a claim C(ρ) that
  holds at each resolution but does not reproduce itself across the cascade, under
  what conditions on the family and on C does a strictly stronger C′ ⇒ C exist that
  *is* cascade-closed? The move is folklore in mathematics (strengthening the
  induction hypothesis); what ARW would add is the condition for its availability.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/inductive_strengthening_cascade_closure.md §3.

**Q-STR-02 — Minimality of the strengthening**
- **Status:** open
- **Question:** Is there a least strengthening — minimal added projective load on
  Π_ρ — and is it unique up to descriptive equivalence? Bears directly on whether
  "strengthen the claim" is an actionable repair or only a post-hoc description of
  successful proofs.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/inductive_strengthening_cascade_closure.md §4, §6.

**Q-STR-03 — Cascade closure vs. Σ-persistence**
- **Status:** open
- **Question:** Is cascade closure a special case of generator invariance over a
  scope family — i.e. vertical transfer read as Σ-invariance along the ε-axis? If
  so, the Σ machinery already carries it and Q-STR-01/02 collapse into the
  Q-REL-01–03 cluster. If not, the resolution axis needs its own persistence notion
  distinct from Σ. Related but **not merged**: Q-REL-01–03.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/inductive_strengthening_cascade_closure.md §6.

**Q-STR-04 — Is audit stability equivalent to cascade closure?**
- **Status:** open (stated as a conjecture in the source, not a result)
- **Question:** A description is *audit-stable* over [ρ₂, ρ₁] if the realization-class
  diameter Amb(C; ρ₁→ρ) ≤ ε for every intermediate ρ — verification commutes with
  resolution change. Conjecture: audit stability over a range is equivalent to the
  existence of a cascade-closed strengthening whose per-scale content is verifiable
  within Π_ρ. Neither direction is proved.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/scale_gap_ambiguity_audit_stability.md §3.

**Q-STR-05 — Conditions under which strengthening refusal is a signal**
- **Status:** open
- **Question:** Adopting a cascade-closed strengthening is a costly self-binding: it
  forfeits the option value of the realization class. Under what assumptions on cost
  distribution and common knowledge does *unexplained refusal* to strengthen separate
  gap-exploiting describers from load-constrained ones? Likely imports standard
  costly-signaling structure; the open part is what, if anything, is ARW-specific
  beyond the formulation of the signal's content.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/scale_gap_ambiguity_audit_stability.md §4.

**Q-STR-06 — Measuring Amb, and whether N* bounds it**
- **Status:** open
- **Question:** Can Amb(C; ρ₁→ρ₂) be estimated in pipeline terms — sampling the
  realization class under B and computing the d_Π-diameter at ρ₂? And does the
  aggregation-limits machinery bound it? Checked on import: the variance crossover
  N* of `docs/advanced/arw_aggregation_limits_typological_observables.md` is a
  variance-exchange point, **not** a realization-class diameter, so no bound is
  inherited; whether σ²_W at fixed class assignment bounds Amb for
  aggregate-vs-individual instances is the open part.
- **Registered:** 2026-07-25.
- **Source:** docs/notes/scale_gap_ambiguity_audit_stability.md §5, §6.

---

## Semantic Description Spaces — Linkage and Discursive Mediation (registered 2026-07-25)

*(Source: the Resonanzdialektik working thesis, folded in 2026-07-25 as extensions
rather than as a new document — `docs/art_instantiations/kht_resonance_dialectic.md`
§6.3 and `docs/notes/scope_component_conflict_typology.md` §8. Collision check:
Q_NEW_E was free; Q_NEW_A–D belong to the typology note. Level discipline: Q_NEW_E is
ARW-level and owned by the typology note; Q-RD-5 is KHT-level and owned by the
resonance-dialectic doc.)*

*(Extended 2026-07-26 — stability revision. Q_NEW_F and Q-RD-6 added; Q_NEW_E and
Q-RD-5 revised. Collision check: both IDs were free. Level discipline unchanged and
enforced across the split: the generator/co-stability reading of linkage and the
Δ-conflict discriminator are ARW-level and stay with the typology note (Q_NEW_E,
Q_NEW_F); only the consequence for the mediation objective is KHT-level and carries a
Q-RD ID (Q-RD-6). Sources: `docs/notes/scope_component_conflict_typology.md` §8.1 and
`docs/art_instantiations/kht_resonance_dialectic.md` §5, §6.3.)*

**Q_NEW_E — Can a linkage disagreement be placed by a tuple-component typology?**
- **Status:** open (revised 2026-07-26)
- **Question:** Two parties share B, Π, Δ and ε, each grants the other's account the
  status of a description, and they still disagree — the difference lying in how the
  shared terms constrain one another. The scope tuple has no slot for relational
  structure over Π, so such a disagreement is invisible to a tuple-component typology
  by construction. Is the linkage difference irreducible, and where does it live?
- **Candidate answer (2026-07-26, §8.1 of the source):** the linkage is the
  **co-stability profile induced by a generator hypothesis**. σ_Δ is tuple-internal
  only for pure state functions; for the asymptotic observables this repository uses
  (r_ss, var_rel, lambda_proxy) O is defined through the dynamics, so σ_Δ requires the
  tuple *plus* a generator. Parties differing only in assumed dynamics therefore get
  different stability verdicts over one Π without either miscomputing. Computable form:
  a graph over Π with edges weighted by overlap of X_stab(π) = {x ∈ X_B : σ_Δ^π(x) < ε}.
  This selects the generator level (Σ) over the Q_NEW_25 transition graph, and does not
  route through S1–S5. Open part: whether two generator variants over one tuple produce
  distinguishable graphs on a worked case.
- **Cheapest negative outcome (revised):** not "B-conflict in disguise" as first stated,
  but **Δ-conflict in disguise** — see Q_NEW_F. If the prediction-commitment
  discriminator cannot be applied because parties adjust predictions post hoc, the two
  are operationally identical and Q_NEW_E and Q_NEW_F close negatively together.
- **Bears on:** Q_NEW_C (exhaustiveness of the classification). If irreducible, the
  typology is a projection of controversies rather than a partition of them.
- **Depended on by:** Q-COM-02 (discursive branch points as the locus where two
  generator hypotheses diverge); Q-RD-6 (whether the mediation objective's minimum
  ranges over generator hypotheses rather than over parties).
- **Registered:** 2026-07-25; revised 2026-07-26.
- **Source:** docs/notes/scope_component_conflict_typology.md §8, §8.1.

**Q_NEW_F — Does the Δ-conflict row conflate a normative and an underdetermined type?**
- **Status:** open
- **Question:** The Δ-conflict row of the typology (§1) is described as "the genuinely
  normative dispute", surviving disambiguation completely. A generator conflict in the
  sense of Q_NEW_E issues the same verdict ("this perturbation is absorbable /
  regime-violating") but arrives at it by hypothesising the map rather than stipulating
  the input — and is therefore *not* normative but **underdetermined**: decidable by
  evidence, though only after the perturbation has occurred. Since the phenomenology is
  identical, the diagnostic cannot currently separate them. Proposed discriminator:
  does the position commit its holder to a prediction that an observed perturbation
  could contradict? Yes → generator conflict; no → Δ-conflict.
- **Known weakness:** the discriminator is sharp only where the prediction is fixed ex
  ante, which in live controversy it rarely is. This is the joint on which both this
  question and Q_NEW_E fail together.
- **Bears on:** Q_NEW_C, Q_NEW_E; and on the resolution column of the §1 table, which
  is currently wrong for any case of the second type.
- **Depended on by:** Q-COM-02 (whether a branch point is locatable in live discourse
  by this discriminator, without either party articulating its generator).
- **Registered:** 2026-07-26.
- **Source:** docs/notes/scope_component_conflict_typology.md §8.1.

**Q-RD-1 — Is maximin the correct mediation objective?**
- **Status:** open (priority: high)
- **Question:** Is the maximin joint-admissibility criterion the right objective, or
  does empirical mediation behaviour fit a different aggregation (e.g. Nash product
  of admissibilities)? Needs a case with two measurable perspectives.
- **Registered:** 2026-07-25 (stated in the source document 2026-06-29; see note).
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §5, §9.

**Q-RD-2 — Explicit (τ, σ, ξ) trajectory for the R3-mediation pathway?**
- **Status:** open (priority: medium)
- **Question:** Can the mediation pathway be expressed as an explicit control-parameter
  trajectory? KHT-specific form of Q-L3-4.
- **Registered:** 2026-07-25 (stated 2026-06-29).
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §9;
  kht_architecture_layer3.md §7.

**Q-RD-3 — Which boundary-condition manipulation holds coupling near K_c?**
- **Status:** open (priority: medium)
- **Question:** At the group level, what manipulation reliably sustains shared
  resonance without crossing into premature lock-in or collapse? Relates to the
  κ_c ↔ N* correspondence.
- **Registered:** 2026-07-25 (stated 2026-06-29).
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §9.

**Q-RD-4 — Same structure at the individual level, or only analogy?**
- **Status:** open (priority: low)
- **Question:** Does individual Shadow integration show the same maximin structure as
  group mediation, or are the two levels only analogically related?
- **Registered:** 2026-07-25 (stated 2026-06-29).
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §9.

**Q-RD-5 — Does maximin have a discursive form under the *fairness* reading?**
- **Status:** open (priority: medium; scope narrowed 2026-07-26)
- **Question:** Is a reorganized shared description space the argmax of
  min-admissibility over the parties' elaborations, with the minimum ranging over the
  *parties*?
- **Known obstacle (2026-07-26):** the individual and group levels supply a facilitator
  who can check whether a claimed inadmissibility is real; the discursive level does
  not. Self-reported and unverifiable inadmissibility makes the criterion strategically
  manipulable — it rewards assertion, producing veto inflation rather than maximin. The
  "parties are not fixed" objection originally recorded here is secondary to this one.
- **Registered:** 2026-07-25; narrowed 2026-07-26 when the robustness axis was split
  off as Q-RD-6.
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §5, §6.3, §9.

**Q-RD-6 — Does the minimum range over parties or over generator hypotheses?**
- **Status:** open (priority: medium)
- **Question:** If the parties' elaborations are read as generator hypotheses (Q_NEW_E,
  2026-07-26) rather than as positions or preferences, the min in
  m* = argmax_m min(R(m, x_A), R(m, x_B)) acquires a second candidate domain: candidate
  *dynamics* rather than participants. On that reading the criterion is a Wald-type
  minimax under model uncertainty — select the description that stays admissible under
  every candidate generator. Which reading is correct for discursive mediation?
- **What the robustness reading buys:** the "parties are not fixed" objection in Q-RD-5
  does not arise, and a generator hypothesis (unlike a preference) commits its holder to
  predictions that later perturbations can contradict — the same prediction-commitment
  check as Q_NEW_F, and a partial substitute for the missing facilitator.
- **What it costs:** conservatism. A description robust to every candidate dynamics may
  be too weak to constrain anything, which is the discursive analogue of a maximally
  gap-ambiguous coarse description (Q-STR-04/06).
- **Relation to Q-RD-1:** orthogonal. Q-RD-1 varies the aggregation form (maximin vs.
  Nash product) holding the domain fixed; this varies the domain holding the form fixed.
- **Registered:** 2026-07-26.
- **Source:** docs/art_instantiations/kht_resonance_dialectic.md §5, §6.3, §9;
  docs/notes/scope_component_conflict_typology.md §8.1.

*Registration-drift note: Q-RD-1–4 were listed in their source document and in its
DOC_INDEX row from 2026-06-29 but never entered here — the same failure mode recorded
for Q-SIG, Q-EXT and Q_NEW_27. Found and corrected 2026-07-25.*

---

## Sleep Scope — Perturbative Consolidation (Q-SLP)

*Registered 2026-07-26 on import of
`docs/context_navigation/sleep_as_perturbative_description_consolidation.md`.
**Not** the same series as Q-SL-01–04 in `docs/context_navigation/agent_sleep_scope.md`,
which concern the effectiveness-based consolidation rule this note proposes replacing.
The one-character prefix difference is a known near-collision — see DOC_INDEX I-12.*

**Q-SLP-01 — What makes an internally generated perturbation admissible?**
- **Status:** open (priority: high)
- **Question:** By what rule does the agent generate Δ_replay, the internal
  perturbation set over the encounter buffer, and what makes a generated
  perturbation admissible rather than arbitrary?
- **Why it is load-bearing:** the whole persistence criterion σ_Δ(D) < ε is only as
  meaningful as Δ_replay is principled. An arbitrarily narrow Δ_replay makes every
  description persistent and the criterion vacuous; an arbitrarily wide one makes
  every description fail. This is the note's weakest joint and should be attacked
  before the discriminating experiment (§9) is worth running.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/sleep_as_perturbative_description_consolidation.md §4, §10.

**Q-SLP-02 — How is Δ-robustness operationalized for a symbolic archetype?**
- **Status:** open (priority: high)
- **Question:** σ_Δ presupposes a distance d_Π on the descriptive space. For an
  archetype that is a symbolic structure rather than a point in ℝⁿ, what supplies
  d_Π? What is the relation between Δ-robustness and admissibility volume?
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/sleep_as_perturbative_description_consolidation.md §4, §10.

**Q-SLP-03 — Frequency or survival rate, and is the ordering axis a scope family?**
- **Status:** open (priority: medium)
- **Question:** Do archetypes arise from encounter frequency or from survival rate
  under variation? And is the consolidation-cycle ordering axis a scope family in
  the sense of `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md` §2, or only
  formally analogous? The first half is decided by the §9 experiment; the second is not.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/sleep_as_perturbative_description_consolidation.md §3.1, §10.

---

## Architectural Aesthetics (Q-AES)

*Registered 2026-07-26 on import of
`docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md`.
Prefix was unused.*

**Q-AES-01 — Can the active scope be determined independently of the judgment it explains?**
- **Status:** open (priority: high)
- **Question:** Can an observer's active scope be fixed independently of the aesthetic
  judgment it is invoked to explain — e.g. by assigning the task before eliciting the
  judgment?
- **Why it gates the note:** without this, scope-relative beauty explains every observed
  preference post hoc and forbids nothing. The source note is deliberately held at
  `note` rather than `hypothesis` for exactly this reason, and this question is the
  route out.
- **Registered:** 2026-07-26.
- **Source:** docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md §9.1, §10.

**Q-AES-02 — Does the Δ-constraint mechanism outperform fluency accounts?**
- **Status:** open (priority: medium)
- **Question:** Does reading the environment as a constraint on Δ (suppressing the
  perturbations under which the active scope's observables would fail) predict
  preference better than familiarity, processing-fluency, status-signalling or
  prospect-refuge accounts? Secondarily: do KHT operator profiles predict environmental
  preference in the direction the source note's §5 implies?
- **Registered:** 2026-07-26.
- **Source:** docs/notes/architectural_aesthetics_scope_dependent_description_persistence.md §3, §5, §9.2, §10.

---

## Communicative Branching Points (Q-COM)

*Registered 2026-07-26 on import of
`docs/notes/communicative_branching_points_nuclear_discourse.md`. Prefix was unused.
Both questions are checks on whether that note earns separate existence from
`docs/art_instantiations/kht_resonance_dialectic.md` §6.3 and
`docs/notes/scope_component_conflict_typology.md` §8/§8.1 (Q_NEW_E/Q_NEW_F).*

**Q-COM-01 — Is marking a branch point cheaper than explicating an elaboration?**
- **Status:** open (priority: medium)
- **Question:** §6.3 of kht_resonance_dialectic.md establishes that explicating an
  ambiguity node is expensive and that refusing it is usually legitimate. The
  cartography strategy asks only that the *location* of the branch be marked, not that
  either party explicate its own elaboration. Is that actually cheaper?
- **Consequence either way:** if yes, cartography survives the cost objection that
  defeats explication and is a distinct strategy. If no, the source note collapses into
  §6.3 and should be merged and superseded.
- **Registered:** 2026-07-26.
- **Source:** docs/notes/communicative_branching_points_nuclear_discourse.md §5, §9.

**Q-COM-02 — Is a branch point locatable without either party articulating its generator?**
- **Status:** open (priority: medium)
- **Question:** Under the generator reading of `scope_component_conflict_typology.md`
  §8.1, a branch point is where two generator hypotheses over a shared tuple begin to
  produce different σ_Δ-profiles. Can it be located in live discourse via the
  prediction-commitment discriminator of Q_NEW_F, without either party stating its
  generator?
- **Known obstacle:** the ex-ante limitation recorded in §8.1 applies here in full — the
  discriminator is sharp only where predictions are fixed in advance, which in live
  controversy they rarely are. If that defeats it, Q-COM-02 closes negatively together
  with Q_NEW_E/Q_NEW_F rather than independently.
- **Registered:** 2026-07-26.
- **Source:** docs/notes/communicative_branching_points_nuclear_discourse.md §5, §9;
  docs/notes/scope_component_conflict_typology.md §8.1.

---

## Scope-Constructing Agent Architecture (registered 2026-07-26)

*(Source: `docs/context_navigation/scope_constructing_agent_architecture.md`, an
alternative formulation of the Context Navigation architecture filed the same day.
Collision check: the Q-SCA prefix was unused; Q-SL-*, Q-SLP-*, Q-OL-* and Q-CNS-* are
the adjacent series in this area — see DOC_INDEX I-12 for the Q-SL/Q-SLP near-collision.
Level discipline: these are ART-level questions about an agent architecture. The
ARW-level question they lean on, Q_NEW_E, stays with the conflict-typology note; Q-SCA-03
and Q-SCA-05 are the links back, not relocations.)*

**Q-SCA-01 — Is scope-varied recapitulation more than data augmentation?**
- **Status:** open (priority: high)
- **Question:** Does re-organizing a stored encounter under controlled variation of its
  scope, e′ = ℛ(e; δB, δΠ, δε, δw), produce modes whose stability domain 𝒫_m is *wider*
  than the perturbation envelope encountered during training — extrapolative rather than
  interpolative robustness? Or is the effect entirely accounted for by the additional
  effective sample count?
- **Decisive measurement:** the 𝒫_m width comparison between arms C1 (identical episodic
  replay) and C2 (scope-varied recapitulation), matched on **gradient steps, not episode
  count**. If C2 tracks the training envelope rather than exceeding it, the construct is
  augmentation with extra vocabulary and the source document should be superseded rather
  than repaired.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/scope_constructing_agent_architecture.md §8, §14, §15.

**Q-SCA-02 — Which reconstruction level suffices for signature extraction?**
- **Status:** open (priority: medium)
- **Question:** Counterfactual reconstruction can run at four levels — actual environment
  simulation, a learned world model, symbolic/relational reconstruction, or internal
  activation reconstruction. The architecture assumes full simulation is unnecessary.
  Untested.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/scope_constructing_agent_architecture.md §9.2.

**Q-SCA-03 — Is R_m the same construction as X_stab(π) at a different level?**
- **Status:** open (priority: medium)
- **Question:** The mode stability profile R_m(δ) = Pr(admissible navigation | m, δ) is
  proposed as the mode-level analogue of the observable co-stability domain
  X_stab(π) = {x ∈ X_B : σ_Δ^π(x) < ε}. Are these formally the same construction one level
  apart, or only analogous? Note the domains differ: X_stab lives in X_B, 𝒫_m in Δ.
- **Bears on:** whether an ART result here transfers back to the ARW-level Q_NEW_E.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/scope_constructing_agent_architecture.md §10;
  docs/notes/scope_component_conflict_typology.md §8.1.

**Q-SCA-04 — Is the intermediate mode the R3 mediation pathway?**
- **Status:** open (priority: medium)
- **Question:** Is m_{A/B}, the functional intermediate configuration during a
  weight-driven mode transition, the same mechanism as controlled R3 activation in
  `kht_resonance_dialectic.md` §4, or a distinct agent-level phenomenon that resembles it?
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/scope_constructing_agent_architecture.md §12.

**Q-SCA-05 — Learned structure over Π vs. assumed structure over Π**
- **Status:** open (priority: high)
- **Question:** The weight field w is a *learned* structure over Π; a generator hypothesis
  (Q_NEW_E) is an *assumed* one. Neither has a slot in S = (B, Π, Δ, ε). Are they the same
  object, such that a multi-agent population exchanging description packages is an ART
  instantiation of the linkage question — or does the learned case lack the property that
  makes the ARW case tuple-invisible?
- **Why it matters:** §13 of the source document is the first setting in which the
  robustness reading of the maximin criterion (Q-RD-6) and the prediction-commitment
  discriminator (Q_NEW_F) become checkable in simulation, because unlike in discourse the
  environment resolves a prediction within an episode. If the discriminator fails there,
  it will not work in discourse either.
- **Bears on:** Q_NEW_E, Q_NEW_F, Q-RD-6.
- **Registered:** 2026-07-26.
- **Source:** docs/context_navigation/scope_constructing_agent_architecture.md §0.1, §13.

*(Q-SCA-06 to -09 registered 2026-07-29 from
`docs/cognitive_architecture/planning_admissible_scope_agent_design.md`. Collision
check run against `open_questions.md` and all of `docs/`: 06–09 were unused in the
Q-SCA prefix, as were the candidate prefixes Q-PLAN, Q-HOR and Q-CVH. Same ART level
as 01–05.)*

**Q-SCA-06 — Does the agent know its own remaining load-bearing capacity?**
Split into three parts, because the three answers have different consequences. The
internal quantity is a hazard estimated from a description's current margin to its
own failure threshold; the external quantity is the rollout horizon measured on
controlled material.

**Q-SCA-06a — Calibration**
- **Status:** open (priority: medium)
- **Question:** Does a predicted hazard of ~0.2 correspond to an observed failure rate
  of ~0.2 under the controlled offline test? Required for the theoretical claim, not
  for selection.
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §1.1, §9.

**Q-SCA-06b — Ranking**
- **Status:** open — first measurement taken 2026-07-29, **underdetermined** (priority: high)
- **Question:** Does the hazard estimate order descriptions by their later measured
  rollout horizon *beyond what the present residual already orders*? Ranking alone
  suffices for selection.
- **First measurement:** Spearman −0.688 for the hazard, −0.665 for the
  present-residual control, partial correlation small and sign-inconsistent across
  seeds. **Not evidence against the layer:** the world used had a rollout horizon of
  1–6 steps, so the target quantity has no dynamic range and the question cannot be
  resolved there. See Q-SCA-10.
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §8.2;
  Simulationen/kontextnavigation_minimal/persistence.py (external).

**Q-SCA-06c — Generalisation**
- **Status:** open (priority: medium)
- **Question:** Does the prediction survive new regimes, other perturbation magnitudes,
  and BC-preserving transfer — or is it in-sample only?
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §9.

**Q-SCA-07 — Can a slower upper loop set ε where a single loop cannot?**
- **Status:** open (priority: high)
- **Question:** A single-timescale self-set resolution provably fails: over a swept
  constant the agent either invents descriptions in a world that never changes or
  stops noticing a real regime change, with no value passing both. Does the nested
  construction — lower loop calibrating observables within a scope, upper loop
  calibrating the scope, on separated timescales — escape this? Candidate information
  source: cross-description contrast, which exists only because a library exists.
- **Bears on:** docs/notes/conflict_navigation_nested_calibration.md;
  docs/notes/kht_reconciliation_scope_constructing.md §4.1.
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §7.5, §4.

**Q-SCA-08 — Does the three-way projection tension generate mode structure?**
- **Status:** open (priority: medium)
- **Question:** Closure under iteration pushes a projection wider, expressibility of B
  pushes it onto particular components, rollout search cost pushes it narrower. Do
  regimes resolving that tension differently generate the mode structure, or does one
  pressure dominate and reduce it to a capacity limit?
- **Method constraint:** all three quantities on the same runs, added one at a time
  with a measured delta.
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §5.

**Q-SCA-09 — Does perturbation survival volume predict rollout persistence?**
- **Status:** open (priority: medium)
- **Question:** V_Δ(D) = ∫ R_D(η) dη is censoring-free and closer to the ARW notion of
  stability; the rollout horizon is in time units and is what planning admissibility
  needs. Are they the same property of a description under two measurements, or two
  properties? If the same, one offline reference suffices and the existing
  recapitulation stability profile over an η-grid is most of it.
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §1.4.

**Q-SCA-10 — What dynamic range must a world have for Q-SCA-06 to be answerable?**
- **Status:** open (priority: high)
- **Question:** Measured requirement rather than a hypothesis: the rollout horizon must
  vary by at least an order of magnitude across descriptions and situations before a
  horizon-prediction test has any power. An action-driven random walk does not meet
  this (measured horizon 1–6 steps). Which generator families do, and should a world's
  horizon distribution be measured *before* an agent is run in it, as the salience
  check now precedes every transfer sweep?
- **Registered:** 2026-07-29.
- **Source:** planning_admissible_scope_agent_design.md §8.3.

---

## Switch Minimization as Description Criterion (registered 2026-07-27)

*(Source: `docs/context_navigation/switch_minimization_criterion.md`. Collision check:
the Q-PAR prefix was unused repo-wide; the adjacent series in this area are Q-SCA-*
(scope-constructing architecture), Q-SL-*/Q-SLP-* (sleep scope) and Q-CNS-*. Level
discipline: these are ART-level questions about an agent architecture and its
measurement; the ARW-level quantities they lean on — σ_Δ, ε*(O,X), I_ε — stay with
`docs/glossary/perturbation_spread.md` and `docs/advanced/epsilon_and_scope_resolution.md`.)*

**Q-PAR-01 — Do the agent's and the observer's partitions coincide?**
- **Status:** open (priority: high)
- **Question:** Does the agent's context partition under ε_agent (`THETA_SAL` in the WP1
  implementation, the deviation threshold in observation space) coincide with the
  observer's behavioural partition under ε_observer (the L1 threshold on `action_dist` /
  `obs_mean`)? The two thresholds live in different spaces on different observables.
- **Why it matters:** if they disagree, "the agent's modes" and "the measured regimes" are
  different objects, and every correspondence analysis in this experiment series needs an
  explicit translation step. Agent-level analogue of Q-SCA-03.
- **Registered:** 2026-07-27.
- **Source:** docs/context_navigation/switch_minimization_criterion.md §2.1.

**Q-PAR-02 — Is the online switch rate a consistent estimator of offline persistence?**
- **Status:** open (priority: high)
- **Question:** At fixed ε, is the observed switch rate a consistent estimator of the
  offline persistence criterion σ_Δ(D) < ε of
  `sleep_as_perturbative_description_consolidation.md` §4? The online rate samples whatever
  Δ the environment happened to deliver; the offline criterion perturbs actively.
- **Decisive measurement:** where the two disagree, which one predicts transfer to held-out
  labyrinth topologies. This sharpens the discriminating experiment of that document's §9.
- **Registered:** 2026-07-27.
- **Source:** docs/context_navigation/switch_minimization_criterion.md §5.

**Q-PAR-03 — Two candidate causes of a wide stability domain**
- **Status:** open (priority: high)
- **Question:** Under a parsimony objective, a wide 𝒫_m has two candidate causes — the
  objective itself, which directly rewards descriptions that survive perturbation, and
  scope-varied recapitulation. Can they be separated by measuring 𝒫_m width in arms
  C0/C1/C2 at identical objective, ε_agent and λ — or does the objective saturate the
  effect and make Q-SCA-01 untestable in this environment?
- **Why it matters:** without this control, C2 can win the §14 comparison of
  `scope_constructing_agent_architecture.md` for a reason that has nothing to do with
  recapitulation.
- **Bears on:** Q-SCA-01.
- **Registered:** 2026-07-27.
- **Source:** docs/context_navigation/switch_minimization_criterion.md §7.

**Q-PAR-04 — Which salience does a parsimony criterion minimize?**
- **Status:** open (priority: medium)
- **Question:** Does parsimony pressure on the active-description deviation ŝ also reduce
  mode-competition salience S(c) = Var_m(F_m(c)) as defined in `salience_mode_ecology.md`
  §5? The two are different quantities: the first is a property of the active description
  alone, the second of the whole ecology, and the second is not computed anywhere in the
  implementation.
- **Why it matters:** if they move oppositely, "minimizing salience" is ambiguous and every
  report must name its target explicitly.
- **Registered:** 2026-07-27.
- **Source:** docs/context_navigation/switch_minimization_criterion.md §9.

**Q-PAR-05 — Is the criterion a description-length criterion?**
- **Status:** open (priority: medium)
- **Question:** Is switch minimization under an admissibility constraint an MDL-type
  criterion — mode count plus switch cost traded against residual deviation — and if so,
  does the λ-plateau correspond to a code-length minimum?
- **Why it matters:** if the correspondence holds it supplies an external, non-hypothesis
  calibration for λ and removes the last free parameter from the construction.
- **Registered:** 2026-07-27.
- **Source:** docs/context_navigation/switch_minimization_criterion.md §12.

---

## ARW-level: Observable Information and BC-Responsiveness (registered 2026-07-27)

*(Source: `docs/notes/observable_information_and_bc_responsiveness.md`. Collision check:
Q_NEW_A–F are in use, G was free; Q-OBS and Q-SELF were also free but the Q_NEW_* series
is where the ARW-level questions live, so this stays there rather than opening a prefix.
Level discipline: ARW-level. The ART-level consequences are Q-PAR-* and Q-SCA-* with the
agent documents.)*

**Q_NEW_G — What condition does entail BC-responsiveness, and can a system compute it about itself?**
- **Status:** open (priority: high)
- **Established first (not the question):** observable information — non-trivial cover
  plus Δ-stability, `docs/core/observable_information.md` — does **not** entail that the
  observable responds to B. An observable that reads the describing system rather than the
  described one satisfies both conditions maximally (σ_Δ = 0 exactly) while producing an
  identical image on every admissible B, which is the F1_BC condition. Demonstrated by
  construction; see §1 of the source note.
- **Question:** what is the minimal *additional* condition that does entail
  BC-responsiveness — and is there a formulation computable by a system that cannot
  observe its own boundary conditions? F1_BC supplies the semantics but is defined by
  comparing O(X_B) across B, which an agent under the anti-circularity commitment of the
  existence test cannot do.
- **Two candidate answers, of unequal standing (revised same day):**
  (a) a non-zero, **clustered** failure rate — a description that never breaks carries no
  partition. Implemented and measured: necessary, and demonstrably *not* sufficient, since
  the descriptions fail at ordinary rates, so a non-zero floor removes a degenerate corner
  without creating BC-responsiveness. (The accompanying separation figures are subject to
  the measurement audit and are not load-bearing here.)
  (b) a **cross-encounter level contrast** — if BC information sits in a channel's level
  across contexts rather than its variation within one, BC-responsiveness is computable by
  comparing stored encounters, which the protocol buffer already supports and the offline
  phase currently does not do. Untested.
- **The sharpened form of the question:** can *any* within-context statistic suffice, or is
  BC-responsiveness only ever computable by comparison across contexts?
- **Why it matters:** this is the lower bound that `switch_minimization_criterion.md`
  (C-PAR) lacks. C-PAR states an upper bound on the failure rate; alone it pushes toward
  descriptions that never break, which §3 of the source note identifies as descriptions of
  the describing system. The two-sided form `0 < failure rate < parsimony bound` is
  structurally the same as `sup_x σ_Δ(x) < ε < ε*(O,X)`.
- **Measured instance (corrected twice the same day):** the first reading attributed a
  substrate-separation failure to self-directed descriptions; the self-share numbers did
  not support that (0.20–0.58 across conditions against a 0.31 chance level, lowest in the
  mixed condition). A subsequent measurement audit then found that the separation ratio
  itself was defective in three successive versions — circular, saturated, wrong grain —
  so no separation verdict from those runs is usable in either direction, and the agent
  turns out to navigate ~10× better than chance. **The question does not rest on that
  ratio.** What does support it: median substrate separability |d| = 0.23 over
  the selected compositions, 14 of 32 negligible, every `DIFF` composition at |d| ≈ 0, and
  `cost_here` — the most substrate-diagnostic channel in the environment — absent from
  every surviving description because it is *constant within* each substrate. The failure
  survived heavy-tailed exploration, four selection criteria, adaptation, critical periods
  and value replay, all of which are within-window criteria.
- **Bears on:** Q-SLP-01 (an arbitrarily narrow Δ_replay makes every description
  persistent — the same class of self-confirming criterion), Q-PAR-02, Q-PAR-04.
- **Registered:** 2026-07-27.
- **Source:** docs/notes/observable_information_and_bc_responsiveness.md §1, §4, §7.

---

## MINDS Generalization — Coordination Protocol Beyond Facilitation (Q-MINDS, registered 2026-07-31)

*(Source: `docs/notes/minds_generalization_beyond_facilitation.md`. Collision check: no
Q-MINDS ID existed anywhere in `docs/` before registration. Level discipline: ART-level
(Resonance Dialectics / KHT family); the maximin criterion itself stays owned by
`kht_resonance_dialectic.md` — Q-MINDS-02 is deliberately routed through Q-RD-6 rather
than duplicating it.)*

**Q-MINDS-01 — Does a MINDS-based meta-controller improve multi-agent coordination over voting/averaging baselines?**
- **Status:** open (priority: high — cheapest operational test of the generalization claim)
- **Question:** implement the MINDS diagnostic set (friction diagnosis, shared-term
  check, synthesis test) as a coordination layer over a small LLM-agent ensemble.
  Does it outperform voting/averaging baselines at (a) detecting ontology conflicts
  (agents using the same term differently, or working from divergent task
  descriptions) and (b) preventing false consensus (a minority agent carrying a
  critical constraint gets overruled)?
- **Why it matters:** a negative result confines MINDS to domains with human-like
  conversational dynamics and demotes the note's "full transfer" claims to analogy;
  a positive result makes the toolkit an operative CDS artifact beyond facilitation.
- **Registered:** 2026-07-31.
- **Source:** docs/notes/minds_generalization_beyond_facilitation.md §4 (domain 1), §6.

**Q-MINDS-02 — For non-human parties, does the Synthesis Test's maximin coincide with the Q-RD-6 robustness reading?**
- **Status:** open
- **Question:** when "parties" are constraint carriers (datasets, services, coupled
  subsystems) rather than persons, the party-minimum and the generator-hypothesis
  minimum of Q-RD-6 may coincide or diverge. Which is it — and if they diverge, which
  minimum does the Synthesis Test actually operationalize?
- **Why it matters:** the generalization claim rests on the maximin objective being
  well-defined without human parties; this is exactly the reference-class question
  Q-RD-6 already poses, extended to the non-human case.
- **Bears on:** Q-RD-1, Q-RD-5, Q-RD-6.
- **Registered:** 2026-07-31.
- **Source:** docs/notes/minds_generalization_beyond_facilitation.md §2, §5.

**Q-MINDS-03 — What scope-level criterion separates a non-substitutable constraint from a strong preference?**
- **Status:** open
- **Question:** the whole protocol hinges on "non-substitutable" constraints
  (viability conditions) being distinguishable from preferences. Candidate
  criterion: a constraint is non-substitutable iff its violation moves the
  system out of X_B (boundary violation) rather than to a different admissible
  point within X_B. Does this hold up, and is it decidable in practice for
  the candidate domains?
- **Why it matters:** without such a criterion, "every party must survive into
  the solution" is unfalsifiable — any component can be declared a viability
  condition post hoc.
- **Registered:** 2026-07-31.
- **Source:** docs/notes/minds_generalization_beyond_facilitation.md §3.

**Q-MINDS-04 — Is there a minimal modular kernel for domains without conversational dynamics?**
- **Status:** open
- **Question:** the ecology/infrastructure case suggests only {Anchor, Coverage,
  Synthesis, Scope} transfer where no conversational dynamics exist. Is this the
  minimal kernel, and what exactly is lost when the conversational diagnostics
  (readiness read, in-session tracking, mediation arc) drop out?
- **Why it matters:** determines whether MINDS decomposes into a
  domain-independent core plus a conversational layer, or whether the
  conversational layer is load-bearing for the whole protocol.
- **Registered:** 2026-07-31.
- **Source:** docs/notes/minds_generalization_beyond_facilitation.md §4 (domain 8), §7.

---

## Total Description Space D(S) — Fibration Reading of the Cover Construction (registered 2026-08-01)

*(Source: `docs/notes/total_description_space.md`; ownership transferred 2026-08-01
to its same-day successor `docs/notes/scope_fibration.md` (rename + extension after
external review). Collision check: Q-DSP prefix
grepped against open_questions.md and all of docs/ — free. Level discipline: all four
questions are ARW-level and owned by the source note. Delimited against the semantic
"description spaces" cluster (Q_NEW_E/F, Q-RD-5/6), which is unrelated. Extends the
partially resolved Q4 (ARW ↔ TDA correspondence, see docs/core/observable_information.md).)*

**Q-DSP-01 — Do the four directions of D(S) commute where they overlap?**
- **Status:** partially_answered (2026-08-01)
- **Answer (ε–Δ pair, paper derivation in scope_fibration.md §5a):** the Δ-direction
  always induces well-defined component maps after an ε-shift of 2σ̄ = 2·sup σ_Δ
  (triangle inequality on edges) — a 2σ̄-interleaving in the persistence-theory
  sense. Strict (unshifted) well-definedness holds iff no pairwise increment lies
  in (ε − 2σ̄, ε + 2σ̄] — a gap condition identified with the pipeline's robust
  ε-plateau criterion. Once maps are well-defined, commutativity is automatic (all
  maps descend from the identity on the sample index set). Open part: coherent
  composition of π- and B-morphisms with the ε–Δ pair.
- **Empirical checks (2026-08-01, scope_fibration.md §5b, two runs):** seed-swap
  tests on the Kuramoto v2 2D field. Run 1 (112 checks): c* ≤ 2σ̄ held 112/112 —
  read as implementation validation (bound follows from the triangle inequality);
  strict-descent violations strongly enriched at, and in this run confined to,
  the independently known transition band (all within 0.15 of the analytic line;
  baseline 9.8%). Run 2 (local edge-wise gap condition, 1,852,996 edge checks):
  risky cell (gap satisfied ∧ descent violated) exactly 0, with both classes
  heavily populated; P(violated | gap violated) = 0.043 (sound but conservative
  flag; necessity never claimed). Status: analytically established,
  computationally instantiated, empirically consistent — not "validated".
  Runs 3–4 (same day): 1D CASE-0001 rerun with DECLARED Δ — strict descent
  20/20 on the registered plateau interior (ε = 0.09, 0.134), marginal at the
  plateau edge (0.066: 10/20), off-plateau violations localized near registered
  regime boundaries; risky gap cell again 0. Blind reconstruction: line
  recovered from violations alone (slope within 6.4%), nulls decisively beaten —
  but NO added localization power over direct σ_Δ / |ΔO| thresholding
  (instrumental claim bounded; architectural claim untouched). Note promoted
  note → hypothesis 2026-08-01 (external-review condition met).
- **Question (original):** Is the fiber assignment (B, π, Δ, ε) ↦ regime structure well-defined
  as a single object — specifically, does ε-coarsening after Δ-perturbation agree
  with Δ-perturbation after ε-coarsening at the component level?
- **Why it matters:** precondition for D(S) being one object rather than four
  unrelated parameter studies; gate for note → hypothesis promotion.
- **Registered:** 2026-08-01.
- **Source:** docs/notes/total_description_space.md §2, §7.

**Q-DSP-02 — Does the no-complete-invariant result apply literally to D(S)?**
- **Status:** open
- **Question:** Does the (ε, Δ)-bidirection of D(S) satisfy the hypotheses of
  multidimensional persistence (Carlsson & Zomorodian 2009), so that the
  no-complete-discrete-invariant theorem applies to ARW's total description space
  literally rather than as an analogy?
- **Why it matters:** if literal, ARW's central stance (conditions strengthen claims)
  acquires a limitative-theorem backing: no unconditioned global summary of D(S)
  exists. If only analogical, the claim must be stated with declared disanalogies.
- **Registered:** 2026-08-01.
- **Source:** docs/notes/total_description_space.md §4.

**Q-DSP-03 — Are the falsification categories exactly the degeneracy types of D(S)?**
- **Status:** open
- **Question:** Is the F0/F1/F-gradient/F2/F3/F4/scope-transition/Z_shared table a
  complete classification of the ways a fiber of D(S) can fail to exist or be
  well-defined — or does the fibration reading predict failure modes not yet in the
  schema?
- **Why it matters:** would relocate the falsification schema from operational
  checklist to derived classification; a predicted-but-unlisted failure mode would
  be a genuine discovery channel.
- **Registered:** 2026-08-01.
- **Source:** docs/notes/total_description_space.md §3.

**Q-DSP-04 — Do the π- and B-directions filter or only reindex?**
- **Status:** open (reframed 2026-08-01 by scope_fibration.md §2b: in categorical
  language the heterogeneity of morphism types is not an anomaly; the question
  becomes which cross-type composition laws hold in D(S))
- **Question:** ε and Δ-radius nest naturally (filtration-like); π and B change the
  base space of the cover construction instead. Do they admit any filtration-like
  structure (e.g. via observable refinement or B-restriction chains), or is D(S)
  irreducibly a fibered object with exactly two filtered directions?
- **Why it matters:** determines the correct mathematical home of D(S)
  (multi-filtration vs. fibration over a parameter space) and hence which existing
  results can be imported.
- **Registered:** 2026-08-01.
- **Source:** docs/notes/total_description_space.md §2, §6.

**Q-DSP-05 — Is the categorical packaging of D(S) conservative?**
- **Status:** open
- **Question:** §2b of `docs/notes/scope_fibration.md` recasts the four directions
  as four morphism types (ε-coarsening, Δ-stability action, π-observable change,
  B-restriction), making D(S) a small category. Is this packaging pure notation
  over the operational definitions, or does it impose additional constraints
  (e.g. forced composition laws for the partial Δ-maps)?
- **Why it matters:** if conservative, the categorical vocabulary is safe as
  language and may be used monograph-side without new proof obligations. If not,
  every imposed constraint is a falsifiable prediction and must be registered as
  such before the vocabulary is used. Guard stated in scope_fibration.md §2b.
- **Registered:** 2026-08-01.
- **Source:** docs/notes/scope_fibration.md §2b, §6.

---

## Description-Centric Evaluation

**Q-EVAL-01 — Can descriptive advance be measured objectively?**
- **Status:** open
- **Question:** Given two competing descriptions of the same phenomenon, can it be
  determined by measurement — not judgment — whether one constitutes a genuine advance
  over the other? Concretely: can the eight dimensions of
  `docs/notes/evaluating_descriptions_not_authors.md` §4 (or a corrected subset) be
  scored such that independent evaluators converge, and such that the score is not
  gameable in the Goodhart sense (§7 of that note)?
- **Why it matters:** if yes, research evaluation can shift from author/venue proxies
  to description-level metrics — the note's central proposal. If no, the note remains
  a heuristic checklist. For the ARW-internal subset (explicit scope, operationality,
  falsifiability, robustness; partially transferability) this is already a concrete
  measurement task, not a philosophical one.
- **Registered:** 2026-08-03.
- **Source:** docs/notes/evaluating_descriptions_not_authors.md §9.

**Q-EVAL-02 — Does any existing metascience programme take descriptions as objects?**
- **Status:** open
- **Question:** The reproducibility movement, registered reports, MDL, and
  falsificationism each institutionalize one or two of the eight dimensions. Does any
  existing programme evaluate *descriptions as objects* — rather than papers, authors,
  or isolated claims? The §8 delimitation in the source note is an unverified
  literature claim and must not be cited as a novelty argument until checked.
- **Why it matters:** determines whether the note proposes a new discipline or joins
  an existing one; also determines the honest framing for any monograph or outreach
  use of the idea.
- **Registered:** 2026-08-03.
- **Source:** docs/notes/evaluating_descriptions_not_authors.md §8.

---

## EWS Discrimination Study — Feasibility and Δ on Observational Data (registered 2026-08-04)

*(Source: `docs/notes/ews_discriminator_test_protocol.md` and
`docs/notes/ews_stage1_review_epsilon_vs_delta.md`. Collision check: Q-EWS prefix
grepped against open_questions.md and all of docs/ — free.)*

**Q-EWS-01 — Can Δ be declared for observational time series from measurement
structure alone?**
- **Status:** answered (negative, 2026-08-04) — with a correction to the question
- **Answer:** No, and not for the contingent reason first recorded. Stage 1 on the
  Cascade packages found no numerical precision in EML or Supporting Information;
  the manufacturer datasheet for the declared configuration (YSI 6600 V2-4, ROX
  6150, Chl 6025) *does* publish accuracy and resolution. But those figures
  constrain only the **instrument contribution** to ε — they do not determine the
  operational ε (a mapping rule is still required: truth-referenced ε=0.2 vs
  pairwise ε=0.4 for pH; reading-dependent ε(x) for DO; plus drift, aggregation
  and preprocessing), and they say nothing about **Δ**. Δ is
  the admissible perturbation class, a modelling commitment about which variations
  count as the same system state; no instrument documentation can supply it. The
  distinction is invisible in simulation (where Δ is injected) and became visible
  only on observational data.
- **Corollary (bias direction, conditional):** *if* σ_Δ is defined
  inclusion-monotonically (supremum radius/diameter over Δ — which the repo's
  canonical σ_Δ(x) = sup_{δ∈Δ}|O(x+δ)−O(x)| is), then narrowing Δ can only
  reduce or preserve σ_Δ, making σ_Δ < ε easier and yielding more stability
  verdicts — **anti-conservative** for H1. A distributional σ_Δ variant would not
  inherit this and must re-derive it. "Err upward" is bounded: an arbitrarily wide
  Δ tests a different claim. Clean form: declared family Δ_min ⊆ … ⊆ Δ_max with
  verdict stability required across it (Q-EWS-04).
- **Registered:** 2026-08-04.

**Q-EWS-02 — Does alarm coherence across observables discriminate genuine
transitions from descriptive artifacts (H1)?**
- **Status:** open, untested (the Cascade run stopped at feasibility)
- **Blocker found 2026-08-04 (two parts):** (i) with chlorophyll unsupported for
  the absolute-concentration projection and model-derived metabolism excluded for
  process error, the admissible response set is raw DO %sat and raw pH — at n = 2
  the *graded* coherence discriminator degenerates into pairwise unanimity
  (logically testable, but without redundancy or partial coherence); (ii) more
  decisively, DO and pH are not independent measurement-error channels — same
  sondes, shared logging, deployment, weekly rotation and preprocessing incl. the
  documented mean-shift correction, so common-mode instrument error propagates
  into both. A test of H1 needs ≥ 3 response observables (mathematical minimum for
  a non-trivial majority), ≥ 4 recommended for robustness (k=3 of 4 tolerates one
  failure), on **independent measurement channels**, plus a same-apparatus
  labelled negative (the reference *system* — not a forcing variable such as
  temperature, which is a covariate control only).
- **Registered:** 2026-08-04.

**Q-EWS-03 — Does the coherence rule add value over single-observable EWS, plain
σ_Δ thresholding, and multivariate EWS (H2)?**
- **Status:** open, untested (gated behind Q-EWS-02)
- **Registered:** 2026-08-04.

**Q-EWS-04 — What is the admissible form of a Δ declaration for observational data?**
- **Status:** open
- **Question:** Given that Δ is a modelling commitment rather than a measured
  quantity, what makes one declaration defensible and another circular? Candidate:
  declare a *family* of Δ values spanning the plausible range and require the
  verdict to be stable across the whole family, reporting a verdict that flips
  inside the family as the finding rather than selecting the favourable member.
- **Why it matters:** every future application of ARW to observational rather than
  simulated data faces this; without it, σ_Δ has no observational counterpart and
  the falsification schema cannot be applied outside simulation.
- **Registered:** 2026-08-04.
- **Source:** docs/notes/ews_stage1_review_epsilon_vs_delta.md §2, §5.

**Q-EWS-05 — What is the mapping rule from instrument specification to operational ε?**
- **Status:** open
- **Question:** A datasheet accuracy figure constrains the instrument component of
  ε but does not fix it. Open sub-questions: truth-referenced (ε = spec) versus
  pairwise-compatibility (ε = 2·spec) interpretation; reading-dependent accuracy
  giving ε(x) as a function versus a declared scalar collapse; and the
  contributions the specification does not cover at all — calibration drift
  between instrument rotations, temporal aggregation, and documented preprocessing
  (outlier removal, missing-day rules, mean-shift correction across instrument
  changes). Additionally: any observable-side standardization (e.g. annual
  z-scoring of pH) makes the induced ε data-derived and therefore circular under
  preregistration — such transforms must be excluded or the raw scale used.
- **Why it matters:** without this rule, "ε from the instrument" is an
  underdetermined claim, and the ε-plateau machinery has no defensible
  observational anchor.
- **Registered:** 2026-08-04.
- **Source:** docs/notes/ews_stage1_review_epsilon_vs_delta.md §2.1, §2.2, §6.

---

## Description Atlas — Form of the Vollraum and Obstruction Types (registered 2026-08-04)

*(Source: `docs/notes/description_atlas_programme.md`. Collision check: Q-DSP-01–05
in use per the 2026-08-04 pulse registry; 06/07 free. Continues the Q-DSP series
because the atlas is the form D(S) takes, not a separate object.)*

**Q-DSP-06 — Is the atlas an adequate form for the Vollraum description?**
- **Status:** open
- **Question:** If the no-complete-invariant argument holds (Q-DSP-02), a global
  summary of D(S) is unavailable and the description must take the form of charts
  (regions of constant fiber) plus transition data plus obstructions. Is that form
  adequate — or does it discard structure that the no-complete-invariant result
  does not actually force us to discard?
- **Why it matters:** decides what a *completed* D(S) description would look like,
  and therefore what the whole programme is aiming at. If the atlas form is lossy
  beyond what is forced, the target is wrong.
- **Registered:** 2026-08-04.
- **Source:** description_atlas_programme.md §1, §2.

**Q-DSP-07 — Does a topological obstruction type exist, distinct from the metric one?**
- **Status:** open
- **Question:** The falsification schema recognises only a metric mode of
  Δ-failure (σ_Δ ≥ ε on a set exceeding τ_∂). The atlas reading predicts a
  **topological** mode: assignment not single-valued around a loop (χ ≠ 0 on a
  circuit where |∇O| stays finite) — monodromy rather than steepness. Candidate
  instance: the sign change of adiabatic electronic state labels around a conical
  intersection. Is this a genuinely distinct obstruction type, or is every
  candidate reducible to the metric mode under a suitable observable choice?
- **Why it matters:** a confirmed type T would be the first case in which the
  fibration reading **adds a category** to the falsification schema rather than
  re-describing it. Reduction of all candidates to type M is a real negative
  result about the fibration's added structure.
- **Related:** Q_NEW_26 (χ computed nowhere; σ_Δ is its proxy — a topological
  obstruction is precisely a case where the proxy cannot work in principle, not
  merely in practice).
- **Registered:** 2026-08-04.
- **Source:** description_atlas_programme.md §5, §8.
