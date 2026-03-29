---
status: working-definition
layer: docs/context_navigation/
---

# Transfer Semantics for Context Navigation Experiments

## Purpose

This document specifies the correct ARW interpretation of transfer experiments
in the context-navigation architecture.

It applies the repo-canonical finding that **Φ measures observable transfer,
not system transfer** (Session 2026-03-18, Finding 9; `docs/advanced/observable_consequences.md` K4)
to the labyrinth agent setting.

This distinction is operationally consequential: two labyrinth instances with
identical zone structures but different observables may yield low Φ, while
two structurally different environments may yield high Φ if the same observables
are used and partition topology matches.

---

# 1 What Φ Measures

The transfer compatibility score Φ is defined over two scopes S_A and S_B:

```
Φ = composite(RCD, TBS_norm, PCI, SDI)
```

where:

| Metric | What it measures |
|--------|-----------------|
| RCD | |N_A − N_B| — regime count difference |
| TBS_norm | |θ*_A/range_A − θ*_B/range_B| — normalized transition position shift |
| PCI | Partition compatibility index — overlap of regime labellings |
| SDI | ε-stability similarity |

**Φ is a function of S_A and S_B, not of the underlying systems.**

This means Φ captures how well the **partition structure produced by the
chosen observables** transfers — not whether the physical or computational
systems are structurally similar.

---

# 2 Three Transfer Experiments in the Labyrinth Setting

The labyrinth agent architecture involves three distinct transfer experiments,
each with a different ARW interpretation.

## 2.1 Transfer across labyrinth instances (same observable)

**Setup:** Train on labyrinth L_A; test on labyrinth L_B (unseen geometry,
same zone types).

**Scope pair:**
- S_A = (B_A, Π, Δ, ε) — training labyrinth, primary observable mode_dist
- S_B = (B_B, Π, Δ, ε) — test labyrinth, same observable

**What Φ measures here:** Whether the regime partition structure (mode ecology)
generalizes across environments.

Because S_A and S_B use the same observable, Φ here primarily reflects
**Φ_sys** — system-side transfer. A high value means the mode ecology is
environment-general, not environment-specific. This directly answers the
OSV research question on regime generalization.

**Admissibility verdict threshold (working hypothesis):**
- Φ ≥ 0.75: highly_admissible — the learned mode ecology constitutes a
  generalizable behavioral partition.
- Φ < 0.5: inadmissible — the mode ecology is environment-specific; the
  agent has overfitted its partition to labyrinth L_A.

## 2.2 Transfer across observables (same system)

**Setup:** Apply two observables to the same labyrinth — e.g., mode_dist
(mode occupancy distribution) and salience_mean (admissibility competition
variance).

**Scope pair:**
- S_1 = (B, {mode_dist}, Δ, ε_1)
- S_2 = (B, {salience_mean}, Δ, ε_2)

**What Φ measures here:** Whether the two observables yield compatible
regime partitions of the same underlying system.

This is **Φ_obs** — observable-side transfer. A low value does not imply
the agent's behavior has no regime structure; it means the two observables
carve the behavioral space differently.

**Expected result:** mode_dist and salience_mean are structurally distinct
observables (Aggregation-dominated vs. Restriction-dominated; see
`docs/context_navigation/context_navigation_scope_spec.md` §5). A partially
admissible or lower Φ_obs is structurally expected and is not a failure.

**Diagnostic value:** If Φ_obs is near zero, the two observables are
essentially independent — using both in a joint scope requires the
product-scope construction (S_joint = S_1 ×_B S_2) with per-observable εᵢ.
If Φ_obs is high, the observables are largely redundant; one suffices.

## 2.3 Cross-level transfer: agent vs. mean-field (OSV Phase 2b)

**Setup:** Compare the regime partition of the agent-based model (individual
agent trajectories) with the regime partition of the corresponding mean-field
description (aggregate dynamics).

**Scope pair:**
- S_agent = (B_agent, Π_agent, Δ, ε_agent) — agent behavioral observables
- S_MF = (B_MF, Π_MF, Δ, ε_MF) — mean-field observables (e.g., consensus
  fraction, polarization index)

**What Φ measures here:** Whether the regime structure visible at the
agent level survives coarse-graining to the mean-field description.

This is the ARW transfer experiment for the social/opinion model in OSV Phase 2b.
A high Φ means the BC-induced regime partition is robust to the modeling-level
transition — a strong result for the framework's claims. A low Φ means the
mean-field description discards regime information present at the agent level.

**Note on TBS_norm:** The sweep axes differ (agent-level BC parameter vs.
mean-field parameter), so TBS_norm requires separate sweep_range entries for
both Invariants.json files. Do not compare TBS_raw values.

---

# 3 Reporting Requirements for Transfer Results

Every transfer result in the context-navigation experiment series must document:

```yaml
transfer_type: environment | observable | cross_level
scope_A:
  observable_key: mode_dist         # or salience_mean, etc.
  observable_bc_notation: A·R       # BC structure of the observable itself
scope_B:
  observable_key: mode_dist
  observable_bc_notation: A·R
phi_raw: 0.XX
phi_interpretation: >
  Φ here reflects [observable / system / cross-level] transfer.
  [Interpretation of what a high/low value means in this experiment.]
admissibility_verdict: highly_admissible | partially_admissible | inadmissible
```

The `observable_bc_notation` field is required because Φ conflates observable
structure and system structure unless explicitly decomposed. Documenting the
BC notation of both observables makes the Φ value interpretable.

---

# 4 Relationship to Pending Questions

| Question | Relevance |
|----------|-----------|
| Q_NEW_9 — BC class: system vs. scope property | Resolved partially by the Φ_obs / Φ_sys decomposition. Until Q_NEW_9 is answered, BCManifest should document both system BC (zone type) and observable BC (mode_dist = A·R). |
| Q_NEW_11 — Φ = Φ_obs × Φ_sys decomposition | The three transfer experiment types (§2.1–2.3) operationalize this decomposition for the labyrinth case. §2.1 gives Φ_sys; §2.2 gives Φ_obs; §2.3 is a mixed case. |
| Q_NEW_3 — Latent DOFs: new observable vs. B-extension | If mode_dist and salience_mean yield low Φ_obs, the joint scope construction becomes mandatory. This determines whether the latent DOF (mode competition state) is handled as a new π or folded into B. |
| Q-CNS-04 — Φ for structurally similar vs. dissimilar labyrinths | Directly addressed by transfer type §2.1. |

---

# 5 Reference

- `docs/advanced/observable_consequences.md` — K4: Φ as observable transfer
- `docs/bc_taxonomy/transfer_distortion_metrics.md` — formal definitions of RCD, TBS_norm, PCI, SDI, Φ
- `docs/context_navigation/context_navigation_scope_spec.md` — observable BC notation for mode_dist and salience_mean
- Session 2026-03-18, Finding 9 in `docs/notes/research_journal.md`
- Session 2026-03-29, CASE-0004↔CASE-0001 transfer (Φ=0.9, highly_admissible) as calibration reference.
  **Limitation:** TBS_norm could not be computed (sweep_range missing from CASE-0004 Invariants.json);
  TBS_score=0 in the Φ composite reflects this data gap, not a physical zero shift.
  TBS_norm should be recomputed once CASE-0004 pipeline artifacts are complete.
