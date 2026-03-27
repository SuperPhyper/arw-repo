---
status: note
---

# Open Questions — Session 2026-03-18 (Q_NEW_1–12)

*To be merged into `docs/notes/open_questions.md`*

---

## Q_NEW_1: Status of Meta-Assumptions about X

**Question:** The algebraic and topological structure of X (e.g. group
structure of S¹, differentiability of the flow) is a prerequisite for
the well-definedness of many observables — but it does not appear in the
scope tuple S = (B, Π, Δ, ε).

Does the structure of X belong to:
- (a) B (boundary constraints selecting X_B ⊆ X)?
- (b) an independent meta-layer below S?
- (c) the ART layer (domain-specific, not part of ARW-Core)?

**Status:** open

**Reference:** `docs/advanced/observable_decomposition.md` — S¹ embedding in r_ss

---

## Q_NEW_2: F0 — Integration into Falsification Schema

**Question:** Using an observable outside its range R(π) is neither
observable insufficiency (F1) nor scope rejection (F2–F4).
Should F0 be introduced as an independent category?

Proposal:
```
F0: R(π) ∩ B ≠ B
    Label: observable outside its range
    Severity: observable_replacement
```

Sub-questions:
- Is F0 a subtype of F1 or categorically distinct?
- How is R(π) operationally determined (from substrate analysis or empirically)?
- Must F0 be entered in ScopeSpec.yaml as a falsification condition?

**Status:** open

**Reference:** `docs/glossary/observable_range.md`

---

## Q_NEW_3: Latent Degrees of Freedom — Criteria for B-Extension vs. New Observable

**Question:** Every Restriction operation in an observable generates a
latent degree of freedom. Under what criteria should a latent DOF:
- (a) be treated as a new observable π' with its own scope S'?
- (b) be incorporated into B of the existing scope?
- (c) be ignored (system-irrelevant)?

Candidates from the current analysis:
```
ψ(t)              — collective rotation phase (from r_ss / op_4)
σ²(θ)             — phase variance (from r_ss / op_3)
w_topo            — winding number (from r_ss / op_2)
λ_conv            — convergence rate (from r_ss / op_5)
coupling geometry  — (from var_rel / op_1)
Lyapunov spectrum  — (from lambda_proxy / op_1)
```

**Status:** open — next planned analysis step

**Reference:** `docs/advanced/latent_degrees_of_freedom.md`

---

## Q_NEW_4: Product Scope — Empirical Tractability

**Question:** The construction S_joint = S_1 ×_B S_2 is admissible by
definition of the scope tuple. The open question is empirical:

Does a product scope (e.g. from r_ss-scope and var_rel-scope) carry
a robust ε-plateau? How does ε_joint relate to ε_1 and ε_2?

Expectation: product scopes may require more frequent revision than simple
scopes, as they accumulate the pre-scope substrates of both components
plus their compatibility.

**Status:** open — tractable only after Q_NEW_3 is resolved

---

## Q_NEW_5: w_min as Criterion for Robust Discreteness

**Question:** The statement "a discrete state space corresponds to a
scope whose induced partition is finite and stable over an admissible
ε-interval" is correct but incomplete. Complete formulation:

```
Effectively discrete  ↔  ∃ [ε_min, ε_max] with w > w_min
                          and N(ε) = const
                          and partition stable under Δ
```

What is w_min? Is there an ARW-internal criterion for minimum plateau
width below which discreteness counts as "fragile"?

**Status:** open

---

## Q_NEW_6: Completeness of Regime Partition Relative to P(θ, t)

**Question:** All current observables are projections from P(θ, t) — the
full time-dependent phase distribution. The regime partition P_S is based
on one-dimensional projections, never on P(θ, t) itself.

Are there regime differences that are exclusively visible in P(θ, t) and
invisible to all current observables?

Formally: let R_true be the "true" regime partition based on P(θ, t).
Does P_S = R_true hold? Or P_S ⊊ R_true?

**Implication if P_S ⊊ R_true:** ARW structurally cannot distinguish all
regimes as long as only first and second moment observables are used.
Completeness of the partition would then be a structural constraint of the
observable choice, not an empirical question.

**Status:** open

**Reference:** `docs/advanced/latent_degrees_of_freedom.md` — LF-SHARED-A

---

## Q_NEW_7: Symmetry Breaking as Partition Property

**Question:** In the BC mapping, Symmetry Breaking appears for no latent
degree of freedom. All LFs fall under Restriction, Aggregation, Coupling,
Dissipation, or Forcing.

Two hypotheses:

**(a) Symmetry Breaking is not an observable property:**
It is an emergent phenomenon at the level of the regime partition —
visible as bifurcation in partition structure under parameter variation,
not as discarded information of a single observable.

**(b) Symmetry Breaking is encoded in P(θ, t):**
It appears in distribution asymmetries (non-vanishing skewness,
multimodality) not fully captured by moment-based observables.

**Status:** open

**Reference:** `docs/advanced/latent_degrees_of_freedom.md` — Finding 2

---

## Q_NEW_8: σ²(θ) as Complementary Observable to r_ss

**Question:** σ²(θ) = Var(θ) is the second moment of P(θ, t) and the
natural structural complement to r_ss (first Fourier mode).

Specific sub-questions:
- What does the pre-scope substrate of σ²(θ) look like?
- Where does R(σ²(θ)) lie in parameter space?
- Is R(σ²(θ)) ∩ Z(r_ss) ≠ ∅ — does σ²(θ) see into the exclusion
  zone of r_ss (κ ≈ κ_c)?

**Finding (answered):** σ²(θ) shares Z_shared with r_ss entirely.
No genuine complementarity at κ_c. Both collapse from identical dynamic
reasons. σ²(θ) has additional own exclusion zones (Z_wrap, Z_multi)
not shared with r_ss.

**Status:** partially answered

**Reference:** `docs/advanced/observable_decomposition.md` — σ²(θ) section

---

## Q_NEW_9: BC Class — System Property or Scope Property?

**Question:** Observable decomposition shows that BC classes appear in
the observable itself, independently of the system. r_ss is structurally
Restriction-dominated regardless of which system it observes.

Is the BC class in BCManifest:
- (A) a property of the system, observed through the scope?
- (B) a property of the scope (system + observable combined)?

**Consequence of Position B:**
BCManifest would need to carry system BC and observable BC separately.
Transfer would only be meaningfully interpretable between scopes with
compatible observable BC structures. Φ would decompose into
Φ_obs and Φ_sys components.

**Status:** open — foundational question for BC taxonomy program

**Reference:** `docs/advanced/observable_consequences.md` — K5

---

## Q_NEW_10: Formal Distinction: Regime Boundary vs. Scope Transition

**Question:** K3 shows that θ* (regime boundary within a scope) and κ_c
(physical phase transition / scope transition) are conceptually distinct.
The framework currently does not treat them explicitly differently.

Does ARW need a formal definition of:

```
Regime boundary θ*:   discontinuity in π(x) within R(π)
Scope transition:     transition between two scopes S_A and S_B
                      at the boundary R(π), i.e. at Z(π)
```

And: how is a scope transition documented in CaseRecord and ScopeSpec?
Is a new artifact format needed?

**Status:** open

**Reference:** `docs/advanced/observable_consequences.md` — K3

---

## Q_NEW_11: Transfer Decomposition into Observable Transfer and System Transfer

**Question:** Φ = f(S_A, S_B) measures observable transfer.
Can Φ be decomposed into two components:

```
Φ = Φ_obs(observable-BC_A, observable-BC_B)
  × Φ_sys(System_A, System_B)
```

If so: how are Φ_obs and Φ_sys operationally separated?
Possible approach: compare two scopes of the same system with different
observables — then Φ measures purely Φ_obs.

**Status:** open — requires a new case with two observables on the same
system (CASE-0001 with r_ss vs. σ²(θ))

**Reference:** `docs/advanced/observable_consequences.md` — K4

---

## Q_NEW_12: χ = ∂r_ss/∂κ as New Observable for CASE-0001

**Question:** The susceptibility χ = ∂r_ss/∂κ is a fluctuation observable
that diverges at κ_c instead of collapsing. R(χ) ∋ κ_c — unlike r_ss.

Specific sub-questions:
- What does the pre-scope substrate of χ look like?
- Does χ require dense κ-sampling — or can it be estimated from existing
  CASE-0001 data?
- Does a scope with Π = {χ} yield a different regime partition than
  Π = {r_ss}?
- Is χ the first representative of a new observable class (fluctuation
  observables) in the ARW framework?

**Status:** open — high priority as CASE-0001 extension

**Reference:** `docs/advanced/observable_consequences.md` — K6
