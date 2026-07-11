# To-REPO → ARW Repository: Action Plan (2026-07-11)

**Files in To-REPO:** 9 (7 markdown docs + 1 duplicate pair collapsing to 1 + 1 logo image)
**New content:** 5 distinct new/updated conceptual docs, all from Kaffeehaus sessions 2026-07-04/07-05/07-08
**Out-of-scope content:** 2 files (CDS manifesto + logo) — not ARW/ART material, needs a placement decision
**Blockers found:** 1 open-question ID collision, 1 broken dependency path, 1 stale-vs-current merge conflict

---

## Delta Summary

| File | Target | Status |
|---|---|---|
| `scope_component_conflict_typology.md` | — | **DISCARD** — superseded by `-1` variant (missing §6/7) |
| `scope_component_conflict_typology-1.md` | `docs/notes/scope_component_conflict_typology.md` | **NEW** — use this variant (has §6 worked case, §7 Π-monopolization) |
| `cross_scope_causal_construction.md` | `docs/notes/cross_scope_causal_construction.md` | **NEW** |
| `shared_term_reflex_check.md` | `docs/notes/shared_term_reflex_check.md` | **NEW** |
| `mode_scope_regime_audit.md` | `docs/context_navigation/mode_scope_regime_audit.md` | **UPDATE** — repo has the pre-§2.6 version; needs merge, not overwrite (see Group B) |
| `j_space_arw_signature_hypothesis.md` | `docs/related_fields/j_space_arw_signature_hypothesis.md` | **NEW** — open-question IDs collide, must renumber first |
| `scope_family_flow_and_kuramoto_limit_audit.md` | `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md` | **NEW** — one dependency path in front-matter is wrong |
| `cds-manifesto-revised.md` | — | **HOLD** — not ARW/ART content, see Group E |
| `CDS Logo.png` | — | **HOLD** — asset for the above |

---

## Group A — New notes, ready as-is (3 files)

### A1: `scope_component_conflict_typology-1.md` → `docs/notes/scope_component_conflict_typology.md`

Use the **`-1` variant**, not the base file — it is a superset (adds §6 worked case on
capital-growth-vs-productivity and §7 "Π-monopolization" as a fifth conflict mode). The
base `scope_component_conflict_typology.md` is an earlier reconstruction of the same
note and should not be imported separately.

**Content:** Classifies scientific/normative controversies by which scope-tuple component
(B, Π, Δ, ε) the disputing parties vary. ε-conflicts are equivocations (dissolve on
disambiguation); Δ/Π/B-conflicts are genuine disagreements. Adds Π-monopolization as a
non-tuple-component conflict mode (denying a competing Π's legitimacy rather than disputing it).

**Status/Layer:** `note` / `docs/notes/` ✓ (frontmatter already correct)
**Depends on:** `docs/glossary/scope.md` ✓ exists
**Open questions to register:** Q_NEW_A, Q_NEW_B, Q_NEW_C, Q_NEW_D (§6 of the note) — no ID collisions found in `open_questions.md`
**DOC_INDEX:** New entry needed, layer `notes`

---

### A2: `cross_scope_causal_construction.md` → `docs/notes/cross_scope_causal_construction.md`

**Content:** Addresses causal claims carried across a scope boundary (aggregate↔instance).
Defines a level-shift detector (4 structural markers) and a three-part construction required
for a legitimate cross-scope causal claim (mechanism claim, instance-level signature evidence,
independently-checkable bridge claim with "undecidable" as a first-class outcome).

**Status/Layer:** `note` / `docs/notes/` ✓
**Depends on:** `docs/glossary/scope.md` ✓, `docs/notes/scope_component_conflict_typology.md` (import together with A1 — same session)
**DOC_INDEX:** New entry needed

---

### A3: `shared_term_reflex_check.md` → `docs/notes/shared_term_reflex_check.md`

**Content:** A lightweight two-question "reflex" (same B? same Π?) meant to flag term drift
live, before the heavier conflict typology (A1) or level-shift detector (A2) are needed.
Explicitly coarser/faster than both; recaps just enough of each to stand alone.

**Status/Layer:** `note` / `docs/notes/` ✓
**Depends on:** `docs/glossary/scope.md` ✓, A1, A2 (import all three together — front-matter cross-references assume co-presence)
**DOC_INDEX:** New entry needed

**Import order for Group A: A1 → A2 → A3** (each depends on the previous).

---

## Group B — `mode_scope_regime_audit.md` update (merge required, not overwrite)

**Repo version:** `docs/context_navigation/mode_scope_regime_audit.md` — already registered in
DOC_INDEX and already the source of Q-CNS-06 through Q-CNS-09 in `open_questions.md`.
**To-REPO version:** adds a new §2.6 ("χ_mode — Formal Derivation and Local-Max Correction")
that formally derives χ_mode as a softmax-occupancy derivative, its local Lipschitz constant,
a finite-difference bias parallel to the C1/C2 σ_Δ-proxy correction, and a local-max estimator
χ_mode^LM. Also adds a new open question Q-CNS-06a (whether β belongs in `B_emergent`) and
extends `depends_on` with `docs/core/cover_stability_criterion.md` and
`docs/context_navigation/context_navigation_emergent_modes_experiment.md` (both exist ✓).

**⚠ Conflict, not a clean update:** `open_questions.md`'s existing Q-CNS-06 entry already
carries a *different* partial resolution from session 2026-03-29 — a "mode-switch rate per
episode" proxy (BC structure A·R), independent of and not referencing the new §2.6 softmax
construction (BC structure R⁴·A·Approx). These are two distinct candidate operationalizations
of the same open question, not sequential refinements of one line. Before overwriting the file:

- [ ] Decide whether both operationalizations stay in Q-CNS-06 side by side (as competing
      candidates), or whether one is judged to subsume the other
- [ ] Do not let the §2.6 import silently replace the 2026-03-29 mode-switch-rate finding —
      both should be attributed and dated
- [ ] Add Q-CNS-06a as a new entry (no collision found)

**Action:** merge §2.6 into the repo file (append, do not replace existing §1–§6), update
`depends_on`, then hand-reconcile the Q-CNS-06 entry in `open_questions.md` per above.
**DOC_INDEX:** existing row's Notes column needs updating to mention §2.6/χ_mode addition.

---

## Group C — `j_space_arw_signature_hypothesis.md` (ID collision — fix before import)

**Content:** Corrects an informal framing that conflated Anthropic's "J-Space" finding
(July 2026) with static representation geometry. Reframes J-Space occupancy as
`p(R_i | context)` — the same object as `action_dist`/χ_mode occupancy already defined in
`mode_scope_regime_audit.md` §2.6 (Group B). Proposes `χ_mode^J` as a sharper, ARW-specific,
falsifiable prediction (should show the same one-sided finite-difference underestimation
bias as χ_mode, requiring the local-max correction).

**⚠ Blocker:** the note proposes **Q-REL-01** and **Q-REL-02** as new open-question IDs.
Both are already taken in `docs/bc_taxonomy/bc_relational_structure.md` (Coupling-Dissipation
duality / Restriction-as-functor — an unrelated topic). Renumber before adding to
`open_questions.md`, e.g. `Q-REL-06` / `Q-REL-07` (next free in that prefix), or a distinct
prefix if preferred (e.g. `Q-JSPACE-01/02`).

**Status/Layer:** `note` / `docs/related_fields/` ✓
**Depends on:** `docs/glossary/scope.md` ✓, `docs/context_navigation/mode_scope_regime_audit.md`
(import after Group B is merged, since it directly cites §2.6), `docs/advanced/observable_decomposition.md` ✓
**Import order: after Group B.**
**DOC_INDEX:** New entry needed, layer `related_fields` (currently has only one file — this is the second)

---

## Group D — `scope_family_flow_and_kuramoto_limit_audit.md` (fix path before import)

**Content:** Audit trail from a Kaffeehaus session exploring whether ARW has a native analogue
of renormalization-group flow/fixed points. Concludes ARW already has the needed native
constructs (ε-induced scope families, the N→∞ emergent-BC limit, Φ as invariance measure)
without importing external measure-theoretic machinery — that route is explicitly flagged as
a "wrong turn" for future avoidance. Resolves Q-INV-03 (𝒮_α(b) has a directed flow structure —
definitional, resolved) and leaves Q-INV-04 open (whether the δ-collapse limit and the N→∞
limit coincide — theoretically motivated via finite-size scaling, empirically untested).
§7 records speculative conditional implications if Q-INV-04 were later confirmed, explicitly
flagged as not established.

**⚠ Front-matter error:** `depends_on` lists `docs/advanced/aggregated_bc_structures.md`, but
the file actually lives at `docs/notes/aggregated_bc_structures.md`. Fix the path before import.

**Status/Layer:** `note` / `docs/notes/` ✓ (layer itself is correct, only the dependency path is wrong)
**Other depends_on targets, verified to exist:** `docs/advanced/epsilon_induced_scope_family.md` ✓,
`docs/advanced/bc_relative_observable_indistinguishability.md` ✓, `docs/advanced/invariance_as_scope_persistence.md` ✓,
`docs/advanced/epsilon_and_scope_resolution.md` ✓, `docs/glossary/scope.md` ✓
**Open questions to register:** Q-INV-03 (status: resolved), Q-INV-04 (status: open) — no
collisions (repo currently has only Q-INV-01/Q-INV-02, both in `invariance_as_scope_persistence.md`)
**Also required:** annotate the existing Q-INV-02 entry in `invariance_as_scope_persistence.md`
with a pointer to §3 of this note (per the note's own §6 "Recommended repo actions")
**DOC_INDEX:** New entry needed

---

## Group E — Not ARW/ART content (decision needed, no action taken)

### `cds-manifesto-revised.md` + `CDS Logo.png`

This is a manifesto for a "Center for Description Studies" — mission-statement prose with
no ARW/ART vocabulary, no front-matter, no scope tuple, no falsification schema. Thematically
adjacent (transferable description, cross-domain knowledge transfer) but not written as, or
formatted as, a repo conceptual document. It does not fit any layer in the DOC_INDEX map as-is.

**Recommend asking Rico:**
- Is this a companion/outreach document for a separate initiative, not meant to live in
  `docs/` at all (e.g. belongs in `papers/` as a standalone artifact, or in a different repo)?
- If it should live in `arw-repo`, which layer — most likely `docs/overview/` or a new
  top-level location outside the conceptual-doc index entirely (it isn't a "conceptual
  document" in the DOC_INDEX sense, it's a mission statement)?

No import action taken pending this decision.

---

## Execution Checklist

### Group A (3 new notes — import together, in order)
- [x] Copy `scope_component_conflict_typology-1.md` → `docs/notes/scope_component_conflict_typology.md` (discard base duplicate)
- [x] Copy `cross_scope_causal_construction.md` → `docs/notes/cross_scope_causal_construction.md`
- [x] Copy `shared_term_reflex_check.md` → `docs/notes/shared_term_reflex_check.md`
- [x] Add Q_NEW_A–D to `open_questions.md`
- [x] Add 3 DOC_INDEX entries (layer: notes)

### Group B (mode_scope_regime_audit.md merge)
- [x] Append new §2.6 to repo's `docs/context_navigation/mode_scope_regime_audit.md` (do not overwrite §1–§6)
- [x] Update file's `depends_on` front-matter (add cover_stability_criterion.md, context_navigation_emergent_modes_experiment.md)
- [x] Reconcile Q-CNS-06 in `open_questions.md`: keep both the 2026-03-29 mode-switch-rate finding and the new §2.6 χ_mode construction, clearly dated/attributed
- [x] Add Q-CNS-06a as new entry
- [x] Update DOC_INDEX Notes column for this file

### Group C (j_space — after Group B)
- [x] Renumber Q-REL-01/Q-REL-02 in the note to free IDs (Q-REL-06/Q-REL-07)
- [x] Copy to `docs/related_fields/j_space_arw_signature_hypothesis.md`
- [x] Add renumbered questions to `open_questions.md`
- [x] Add DOC_INDEX entry (layer: related_fields)

### Group D (scope_family_flow — fix path first)
- [x] Fix `depends_on` path: `docs/advanced/aggregated_bc_structures.md` → `docs/notes/aggregated_bc_structures.md`
- [x] Copy to `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md`
- [x] Add Q-INV-03 (resolved) and Q-INV-04 (open) to `open_questions.md`
- [x] Annotate existing Q-INV-02 entry with pointer to this note's §3
- [x] Add DOC_INDEX entry (layer: notes)

### Group E (decision, no import)
- [x] Asked Rico — decision: leave `cds-manifesto-revised.md` + `CDS Logo.png` in `To-REPO/` for now, no action

### Final
- [x] Meta-guard-style checks on all newly written/modified files (frontmatter, depends_on paths, ID collisions) — see "Status: Executed" below
- [x] Verified DOC_INDEX consistency for all new entries (targeted check, not a full 232-file re-audit)
- [ ] Clear imported files from `To-REPO/` — **could not delete programmatically**, see note below

---

## Status: Executed 2026-07-11

All groups A–D imported. Summary of what changed in `arw-repo`:

- **New files:** `docs/notes/scope_component_conflict_typology.md`, `docs/notes/cross_scope_causal_construction.md`,
  `docs/notes/shared_term_reflex_check.md`, `docs/related_fields/j_space_arw_signature_hypothesis.md`,
  `docs/notes/scope_family_flow_and_kuramoto_limit_audit.md`
- **Modified files:** `docs/context_navigation/mode_scope_regime_audit.md` (added §2.6, updated
  `depends_on`, updated §4/§6 tables, added Maintenance History), `docs/advanced/invariance_as_scope_persistence.md`
  (annotated Q-INV-02), `docs/notes/open_questions.md` (Q_NEW_A–D, Q-CNS-06 addendum + Q-CNS-06a,
  Q-REL-06/07, Q-INV-03/04), `docs/meta/DOC_INDEX.md` (6 rows added/updated)
- **Group E:** left as-is in `To-REPO/` per Rico's decision — no import, no deletion.

**Note on `To-REPO/` cleanup:** the imported source files could not be deleted from `To-REPO/`
— shell delete commands against that OneDrive-synced folder return "Operation not permitted"
(same restriction observed on the `ARW Repository/` folder). The 7 imported files are still
sitting in `To-REPO/` alongside the two Group E files; safe to delete manually now that their
content lives in `arw-repo`, but that step needs to happen on your end.

**Note on verification method:** `arw-repo` is OneDrive-synced, and the shell (bash) view of
it lagged behind the actual file state during this session — a `grep`/`wc -l` check on
`docs/meta/DOC_INDEX.md` via bash showed a stale, pre-edit version even after edits had been
applied and confirmed. The edits themselves are correct (verified via direct file-read/search
against the live file, not the shell mount); if you inspect the repo shortly after this
session and something looks out of date, give OneDrive a moment to sync before assuming an
edit didn't take.
