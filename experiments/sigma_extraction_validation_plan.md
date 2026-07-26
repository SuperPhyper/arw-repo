---
status: working-plan
layer: experiments/
last_updated: 2026-07-14
depends_on:
  - experiments/sigma_extraction_bc_signatures.md
  - docs/advanced/bc_signature_extraction_observables.md
  - docs/advanced/bc_signature_forward_derivation.md
addresses:
  - Q-EXT-01 (Levels 1-3), Q-EXT-02 (Levels 1c, 4e), Q-EXT-03 (Level 2)
imported: 2026-07-14 from monograph workspace; canonical copy is this file
---

# Validation Plan: Σ-Extraction Protocol for BC Class Identification

Iterative 4-level plan. Each level builds on the previous.
Success criteria are concrete and checkable.

> **Update (2026-07-14) — forward derivation available.** This plan predates
> `docs/advanced/bc_signature_forward_derivation.md` (2026-06-03, numerically verified):
> the forward map operator structure → cover geometry, including the α = 1/(β−1) theorem
> and the β-exponent calculus (S5 lift +1, moment ×2). Consequences for this plan:
> (a) the Level-1 "expected profile" rows should be **derived** from the β-calculus per
> operator class, not only copied from the K0–T0 empirical references — a mismatch between
> β-derived and reference-derived expectation is itself a finding; (b) Level 4a–4c overlap
> with the forward derivation's worked examples — cite it and extend rather than re-derive;
> (c) the open questions this plan addresses are now registered as **Q-EXT-01–03** in
> `docs/notes/open_questions.md` (prefix registered 2026-07-14).

---

## Level 1 — Intra-Class Consistency
*Claim to test: The discriminant profile is a property of the BC class, not of the specific model.*

### Rationale
The six reference systems (K0–T0) are all "clean" representatives — most are
normal forms or analytically tractable models. If the protocol is general,
a *different* model of the same BC class should produce the same discriminant
profile (within measurement uncertainty).

### Available data from ARW pipeline

| Case | System | BC | Sweep | Observable | n pts | Status |
|---|---|---|---|---|---|---|
| CASE-0001 | Kuramoto | Coupling | κ ∈ [0,3] | r_ss | 15¹ | go |
| CASE-0002 | Multi-link pendulum | Coupling | κ ∈ [0,10] | var_rel, lambda_proxy | 25 | go |
| CASE-0003 | Doppelpendel | Restriction | E_target | var_rel | 12 | go |
| CASE-0004 | Stuart-Landau | Coupling + Emergence | K ∈ [0.01,0.12] | PLV, amp_asym | 12 | go |

All four cases have raw sweep data in `arw-repo/cases/*/results/raw/sweep_results.json`.
No new simulations needed for this level.

¹ n=15 matches the on-disk `sweep_results.json` (verified 2026-07-14). Note:
`arw-repo-pulse` §1 lists CASE-0001 as a 36-pt κ-sweep — discrepancy flagged for the
next pulse refresh; if a refined 36-pt sweep exists (F1: sweep_refinement is pending
for this case), prefer it for task 1a and re-check the density-sensitivity conclusion.

### Tasks

**1a — Coupling consistency (CASE-0001 vs. K0):**
Apply the extraction protocol to CASE-0001 (Kuramoto r_ss, n=15).
Compare discriminants to K0 (Kuramoto r_ss, n=80).
Expected: same profile type (step), similar ε_merge/span, same h_asym sign.
Potential issue: n=15 is sparse. Quantify sensitivity to sweep density.

**1b — Coupling consistency across models (CASE-0002 vs. CASE-0004):**
Apply protocol to CASE-0002 (multi-link pendulum, var_rel, Coupling BC)
and CASE-0004 (Stuart-Landau, PLV, Coupling BC).
Expected: Coupling profile despite different physical systems and observables.
If CASE-0004 PLV gives Coupling profile: strong evidence.
If CASE-0004 amp_asym gives a different profile: see Level 2.

**1c — Restriction consistency (CASE-0003 vs. P2):**
Apply protocol to CASE-0003 (Doppelpendel, var_rel, E-sweep, n=12).
Compare to P2 (simple pendulum, ω(E), n=80).
Expected: Restriction profile (low ε_merge/span, bilateral asym~0.02, low F-grad).
Note: n=12 is very sparse. This case may reveal the minimum viable sweep density.
**Convention note (2026-06-02):** E_sep = ω₀² (corrected from 2ω₀²). The 2D
reference field has been recomputed in `kuramoto_pendulum_cover_pipeline_v2/`.
No secondary ridge confirmed in the corrected data; P2 reference values remain
valid (1D sweep used analytic ellipk with correct E_sep throughout).

**Success criterion:** All Coupling cases (CASE-0001/0002/0004) produce
ε_merge/span > 0.05 and h_asym < 0. CASE-0003 produces ε_merge/span < 0.01.

### Deliverable
`sigma_extraction_arw_cases.py` — adapter script that reads
`sweep_results.json` and outputs the discriminant table.
New column in discriminant table: `source = arw_case`.

---

## Level 2 — Observable Swap
*Claim to test: The discriminant profile depends on the BC class, not the observable.*

### Rationale
ARW explicitly distinguishes observable BC structure from system BC structure.
r_ss has Restriction-dominated BC structure (R³·A·D) regardless of what system
it observes. var_rel has different BC structure. If the protocol reflects the
system's BC class, swapping observables on the same system should not change
the profile type. If it reflects the observable's BC structure, it should change.
This test resolves which is the case.

### Planned tests (no new simulations needed)

**2a — Kuramoto: r_ss vs. variance(r_ss)**
CASE-0001 has r_std (standard deviation of r over measurement window) available
alongside r_ss. Apply the protocol separately to r_ss and r_std on the same
κ-sweep. Compare discriminant profiles.
Expected if BC-class-driven: same Coupling profile for both.
Expected if observable-BC-driven: r_std might show different profile
(r_std is sensitive to Dissipation-like fluctuations).

**2b — CASE-0002: var_rel vs. lambda_proxy**
ARW labels var_rel as "sufficient" and lambda_proxy as "insufficient" for
CASE-0002. Apply the protocol to both on the same κ-sweep (n=25).
Expected: var_rel → Coupling profile.
lambda_proxy → weaker or different profile (possibly no stable θ* detection,
or different ε_merge/span).
This directly tests whether "sufficient vs. insufficient" maps to
"protocol succeeds vs. fails."

**2c — CASE-0004: PLV vs. amp_asym**
ARW labels PLV as "sufficient" and amp_asym as "insufficient by design"
(emergence condition). Apply protocol to both.
PLV → Coupling profile expected.
amp_asym → profile may collapse at emergence boundary (the amp_asym collapse
below K_c=0.055 is exactly the emergence phenomenon).

**Success criterion:**
For sufficient observables: protocol produces a classifiable profile consistent
with the known BC class.
For insufficient observables: protocol either (a) fails to detect a stable θ*,
(b) produces a profile inconsistent with the known BC class, or (c) gives
high α variance / unreliable discriminants.
This would operationalise "observational sufficiency" in terms of the protocol.

### Deliverable
Section in `sigma_extraction_bc_signatures.md`:
"Observable sufficiency and discriminant reliability."

---

## Level 3 — Blind Classification
*Claim to test: The 5-step protocol correctly identifies BC class from sweep data alone.*

### Rationale
Levels 1–2 test consistency within known contexts. Level 3 tests predictive
validity: given a sweep output from an unknown system, does the protocol assign
the correct BC class without prior knowledge?

### Design
Blind classification requires a "test set" of sweeps with known BC labels
that were NOT used to define the protocol (to avoid circular validation).
Available test candidates:

| Test case | True BC class | Observable | Notes |
|---|---|---|---|
| CASE-0001 Kuramoto r_ss | Coupling | r_ss | Already in training set — use as sanity check |
| CASE-0002 pendulum var_rel | Coupling | var_rel | Different system from K0 |
| CASE-0003 Doppelpendel var_rel | Restriction | var_rel | Different system from P2 |
| CASE-0004 Stuart-Landau PLV | Coupling | PLV | Different model from K0/P2 |
| New: SIR with different γ | Aggregation | I_∞ | Parameter variation of T0 |
| New: noisy pitchfork QB | Symm.Breaking | x_ss | Already computed |

For the true blind test, CASE-0002 and CASE-0004 are ideal: they use
different systems/observables from the six reference cases but have known
ground-truth BC labels from ARW classification.

### Tasks

**3a — Protocol application:**
For each test case, apply the 5-step identification protocol mechanically
(no manual override). Record the protocol's classification.

**3b — Error analysis:**
For each misclassification (if any): identify which discriminant(s) caused
the error. Is it sweep sparsity? Observable choice? Noise? Profile ambiguity
(flat→ramp cases)?

**3c — Confusion matrix:**
Build a 6×6 confusion matrix over all test cases (rows: true class,
columns: predicted class). Identify which pairs are most confused.

**Success criterion:**
Correct classification rate ≥ 5/6 cases on non-training test cases.
Restriction/Dissipation confusion is acceptable as a known weak pair;
Coupling/Forcing confusion is not acceptable (they are distant in discriminant space).

### Deliverable
Confusion matrix table in `sigma_extraction_bc_signatures.md`.
Protocol revision if systematic errors found.

---

## Level 4 — Formal Derivation
*Claim to test: The discriminant values are predictable from BC class structure and system parameters.*

### Rationale
If ε_merge/span and h_asym are genuine ARW quantities (not just empirical
heuristics), their values should be computable from the formal scope tuple
S = (B, Π, Δ, ε) and the observable's BC structure. This level derives
analytic predictions and checks them against empirical values.

### Derivations planned

**4a — ε_merge for Coupling (Kuramoto):**
The BFS component at θ* merges when ε reaches the observable step height
at the transition: ε_merge ≈ r_ss(θ*_+) − r_ss(θ*_−).
For Kuramoto near the transition (using Strogatz): r_ss rises from ~0 to
~0.5 within Δκ ~ 0.5 of θ*. Observable span ≈ r_max − r_min ≈ 0.87.
Prediction: ε_merge/span ≈ 0.5/0.87 × (sharpness factor) ≈ 0.15–0.25.
Compare to empirical K0 value: 0.207. ✓ Consistent — needs analytic sharpness.

**4b — ε_merge for Pitchfork (Symmetry Breaking):**
The first right-side point has x_ss = √Δμ where Δμ = (μ_max − 0)/(n_right − 1).
ε_merge_R ≈ √Δμ (gap between θ* at x_ss=0 and first ramp point).
obs_span = √μ_max.
Prediction: ε_merge_R/span ≈ √Δμ/√μ_max = √(1/(n_right−1)).
For n_right=40, μ_max=2: Δμ = 2/39 ≈ 0.051. Prediction: √0.051/√2 ≈ 0.16.
Empirical Q0: eps_merge_R_norm = 0.117. Close — discrepancy from grid
irregularity (log-spaced near θ*).

**4c — ε_merge for Restriction (Pendulum):**
Near the separatrix, ω(E) ≈ π·ω₀/(2·K(k)) with K diverging logarithmically.
The first neighbouring point has |Δω| ≈ ω'(E_sep)·ΔE. Since ω'→∞ at E_sep,
even a small ΔE gives a large Δω. But Δω is bounded by the grid step in E-space.
ε_merge_L ≈ |ω(E_sep−ΔE) − ω(E_sep)| for the closest left-side point.
For ΔE=10⁻⁴ (our sampling): ε_merge_L ≈ ω(E_sep−10⁻⁴) ≈ π·ω₀/(2·K(1−10⁻⁴/2)).
Computable with scipy.special.ellipk. Prediction: check against empirical emL.
**Convention (2026-06-02):** E_sep = ω₀² (oscillatory k² = (E+ω₀²)/(2ω₀²) → 1
as E→E_sep from below). Formula above uses the correct convention throughout.

**4d — Connection to I_ε (admissible resolution regime):**
Felder 2026 defines I_ε = [ε_min, ε_max] where ε_max = ε*(O,X) (cover
collapse threshold). The claim: ε_merge ≈ ε_max for the BFS on the
θ*-component. Verify by comparing ε_merge to the ε at which the cover
count curve drops by 50% (a proxy for ε*(O,X)).

**4e — Sweep density sensitivity:**
From the Pitchfork derivation: ε_merge_R/span ~ √(1/n_right). If true,
discriminants are sweep-density-dependent. Test: rerun K0 and Q0 at
n ∈ {20, 40, 80} and check if ε_merge/span scales as predicted.
This also resolves the Level 1 concern about sparse ARW cases (n=12–25).

### Deliverable
Formal section in `sigma_extraction_bc_signatures.md`:
"Analytic predictions and their empirical verification."
Possibly: a brief technical note for the ARW repo documenting the
formal relationship between ε_merge and I_ε.

---

## Execution Sequence

```
Level 1 (1a, 1b, 1c)   — all from existing arw-repo data, no new simulations
  ↓
Level 2 (2a, 2b, 2c)   — same data, different observables
  ↓
Level 3 (3a, 3b, 3c)   — blind classification using 1+2 results
  ↓
Level 4 (4a → 4e)       — analytic derivations, density sweep
```

Levels 1 and 2 can partially run in parallel (same data source).
Level 3 requires Level 1 to be complete (needs confirmed discriminants).
Level 4a–4d can run independently of Levels 1–3 (analytic work).
Level 4e requires re-running reference sweeps (new computation).

---

## Risk Register

| Risk | Level | Mitigation |
|---|---|---|
| n=12–15 ARW cases too sparse for reliable discriminants | 1a, 1c | Report n-sensitivity; use Level 4e to quantify minimum n |
| lambda_proxy fails to produce any stable θ* (Level 2b) | 2b | Expected/acceptable — documents protocol failure mode for insufficient observables |
| CASE-0003 var_rel doesn't match Restriction profile (different obs BC structure) | 1c, 2 | Would confirm observable-dependence, revise protocol |
| R0/P2 confusion in blind test (Level 3) | 3a | Expected weak pair — document minimum discriminability condition |
| ε_merge analytic prediction doesn't match empirical within 30% | 4a–4c | Quantify residual; attribute to sweep-density effects (4e) |

---

## Open Questions This Plan Addresses

| Question | Level |
|---|---|
| Is the discriminant profile a BC-class property or a model artifact? | 1 |
| Is it a BC-class property or an observable-BC-structure property? | 2 |
| Does "observational sufficiency" map to "protocol reliability"? | 2b, 2c |
| Can the protocol correctly classify unknown sweeps? | 3 |
| What is the minimum sweep density for reliable discrimination? | 1c, 4e |
| What is the formal relationship between ε_merge and I_ε? | 4d |

