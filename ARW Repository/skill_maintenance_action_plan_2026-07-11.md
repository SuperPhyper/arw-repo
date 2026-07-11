# Skill Maintenance Action Plan (2026-07-11)

**Scope:** all 4 active ARW skills (`arw-repo-context`, `arw-doc-consistency`, `arw-meta-guard`,
`arw-observable-analysis`), audited against the current state of `arw-repo` (HEAD `1f3597c`,
2026-06-29; cases through `CASE-20260602-0014`; DOC_INDEX through I-10).

**Headline finding:** the repo has produced roughly 5–6 weeks of substantial new work
(2026-06-03 → 2026-07-08: transfer-metric rewrite, a new applied signature-persistence
cluster, generator-admissibility/epistemic-context ART formalism, the KHT resonance-dialectic
synthesis, the conflict-navigation/facilitation-toolkit cluster, quantization/descriptive-collapse
extensions) that is **almost entirely unrepresented** in the skills, even though DOC_INDEX itself
is in good shape (no true orphans found — the *documents* are registered correctly; the
*skills* just never picked it up). The most serious single gap: the transfer-metric skill
content still presents Φ/PCI without the 2026-06-02 finding that v1 PCI is defective, and
still lists `transfer.py` as the tool without mentioning `transfer_v2.py`, which is now
canonical.

---

## Gap Table

| Priority | Skill | Section | Gap type | Description |
|---|---|---|---|---|
| **high** | arw-repo-context | §2 Active Cases | missing | `CASE-20260602-0014` (Growing-Population SIR, Dissipation-Growing scope B, status `open`) absent from all case tables |
| **high** | arw-repo-context | §6 Transfer Metrics | outdated | Presents Φ/PCI/TBS_norm with no warning that v1 PCI (in `transfer.py`) was found defective 2026-06-02 (collinear with regime count N, ~90% of Φ's weight tracked N); no mention that `transfer_v2.py` is now canonical |
| **high** | arw-repo-context | §7 Pipeline Modules | stale reference | Lists `transfer.py` only; missing `transfer_v2.py` (canonical since 2026-06-02), `sweep_behavioral.py`, `pipeline/kernels/` (`labyrinth_agent.py`, `labyrinth_env.py`) |
| **high** | arw-repo-context | §8 Key Findings | missing | Stops at the 2026-06-02 E_sep/gradient-proxy fix; missing the same-day Q-REL-04 (dimension-growth structural break, answered) and Q-REL-05 (Φ does not resolve BC-class distance, open) findings, and everything from 2026-06-03–2026-07-08 (see "New clusters" below) |
| **high** | arw-observable-analysis | §9 Open Questions | missing | Q-REL-04 (answered) and Q-REL-05 (open) absent — these are core transfer/observable findings squarely in this skill's own domain |
| **high** | arw-observable-analysis | (no section) | missing | No coverage of the Σ-persistence / signature-derivation cluster (`bc_signature_forward_derivation.md`, `bc_signature_extraction_observables.md`, `bc_signature_persistence_and_dominance.md`, `bc_relational_structure.md`) — a direct extension of this skill's own §1 operator-signature material |
| **medium** | arw-meta-guard | §8 Invariants/TransferMetrics checks | missing | No mention of `transfer_v2` guards: VOID on empty `annotated_results` / missing `sweep_range` / undocumented ε-mismatch; TRIVIAL_PARTITION guard for N≤1; real overlap-based PCI + ARI; output path convention `transfer_v2/<A>_vs_<B>/TransferMetrics_v2.json` |
| **medium** | arw-repo-context | §2 Pending repo updates | outdated | List is dated "as of 2026-05-20" even though the skill's own maintenance history reaches 2026-06-02; several items are now further along or superseded |
| **medium** | arw-repo-context | §9 Session checklist | missing | No pointer to the new applied clusters (generator admissibility, conflict-navigation/facilitation, quantization/descriptive collapse) — an agent has no way to discover them except by accidental grep |
| **medium** | arw-observable-analysis | §7 Case implications table | missing | No row for CASE-20260602-0014 despite it being a direct instance of this skill's BC-classification apparatus (Dissipation-growing) |
| **low** | arw-doc-consistency | (procedure) | incomplete | No documented anti-pattern for the exact failure just hit twice this session: (a) open-question ID collision from offline/mobile-drafted notes reusing an ID already taken (Q-REL-01/02), (b) `-N` suffix duplicate files from reconstructed offline sessions needing a diff-before-import step |
| **low** | arw-repo-context | §2 case count | incomplete | "4 active + 10 pending" no longer adds up once CASE-0014 is properly counted; needs a recount rather than a hand-maintained total |

### New conceptual clusters present in the repo, absent from all 4 skills

These are registered in DOC_INDEX (so not "orphans" in the doc-consistency sense) but are
invisible to an agent that only loads the 4 skills:

- **Generator admissibility taxonomy** (`docs/art_instantiations/generator_admissibility_taxonomy.md`,
  `epistemic_context_and_functional_admissibility.md`) — G=(Λ,Σ,φ,C) formalism, A(G)/A_f/A_h, Q-GEN-01–04
- **Σ-persistence / signature-derivation cluster** (`bc_relational_structure.md`,
  `bc_signature_forward_derivation.md`, `bc_signature_extraction_observables.md`,
  `bc_signature_persistence_and_dominance.md`) — Q-REL-01–03, extends operator signatures S1–S5
- **KHT Resonance Dialectic** (`kht_resonance_dialectic.md`) — unifies formal/admissibility/procedural
  resonance senses, maximin joint-admissibility criterion, Q-RD-1–4
- **Conflict-navigation / facilitation toolkit** (`conflict_navigation_nested_calibration.md`,
  `facilitation_toolkit_tuning_or_framing.md`, `facilitation_between_the_sessions.md`,
  `facilitation_crystallize_the_friction.md`, `art_instantiation_lcc_nested_calibration.md`) —
  directly relevant background for the 5 To-REPO notes just imported this session (conflict
  typology, causal construction, reflex check all build on this cluster)
- **Quantization / descriptive collapse** (`arw_quantization_partition_stability.md` §3.6) and
  **aggregation limits / typological observables** (`arw_aggregation_limits_typological_observables.md`)

None of these need to be summarized in full — but at least one pointer sentence per cluster
belongs somewhere an agent will see it before starting related work.

---

## Cross-Skill Dependency Notes

- The Φ/transfer-metric fix (high, arw-repo-context §6) and the missing Q-REL-04/05 (high,
  arw-observable-analysis §9) are **the same underlying finding** viewed from two skills —
  both must be updated together or they will re-diverge.
- The transfer_v2 guard gap (medium, arw-meta-guard §8) is downstream of the same fix —
  three skills need the same transfer_v2 update in parallel (exactly the pattern this
  skill's own §4 warns about).
- CASE-20260602-0014 is missing from both arw-repo-context (§2) and arw-observable-analysis
  (§7) — one case addition, two skills to touch.

---

## Recommendation: Structural Revision, Not Just Patching

Patching the gaps above into the current 4-file structure would fix today's drift but not
the *cause* of it. All four skills mix two content types with very different half-lives:

| Content type | Half-life in this repo | Examples |
|---|---|---|
| **Stable** — canonical definitions, schemas, falsification taxonomy, layer map, procedural checklists | months, some frozen indefinitely | scope tuple B/Π/Δ/ε, F0–F4/F-gradient schema, layer map, GUARD rules, observable-decomposition method |
| **Volatile** — case tables, pipeline module inventory, "key findings" logs, pending-update lists | days to a few weeks (this repo produces several substantial docs/week via Kaffeehaus sessions) | active case status, which `.py` file is canonical, latest Q-REL/Q-CNS/Q-INV findings |

Today's drift happened *specifically* in the volatile sections, inside otherwise-fine stable
skills — and it happened silently, because there is no marker distinguishing "this is
canonical and frozen" from "this was true as of the last edit." A skill file that is 70%
stable and 30% volatile gets refreshed as a whole roughly never, because refreshing it means
re-reading and hand-diffing the stable parts too.

### Three options

**A — Minimal patch.** Fix the gap table above in place, add a "verify before trusting"
notice at the top of each volatile section, pointing to the live source
(`cases/`, `docs/meta/DOC_INDEX.md`, tail of `docs/notes/research_journal.md`,
tail of `docs/notes/open_questions.md`). Lowest effort, does not change recurrence risk.

**B — Split stable from volatile (recommended).** Extract the volatile sections of all
four skills into one new shared skill, e.g. `arw-repo-pulse`:
- Active case table, `go_nogo` status, pipeline module inventory (incl. version/deprecation
  notices like "transfer.py v1 deprecated for BC-distance claims, use transfer_v2.py"),
  a short "since last pulse" digest of the newest Q-IDs and clusters, each dated.
- Explicitly designed to be **replaced wholesale**, not hand-edited, each cycle — refresh
  procedure: `ls cases/`, tail `research_journal.md`, tail `open_questions.md`, diff against
  current pulse, regenerate. Wholesale replacement is far cheaper to keep honest than
  surgical edits to a mixed document, which is what failed here.
- The other four skills keep only stable content (definitions, schemas, procedures) and
  each gets one line: "for current case/pipeline/finding status, load `arw-repo-pulse`."
- Directly prevents recurrence of both the transfer_v2 miss and the CASE-0014 miss, and
  would have caught the Q-REL-01/02 ID collision from the previous session's action plan
  (a pulse skill whose whole job is "latest Q-IDs" is far more likely to be current than a
  9KB mixed document nobody wants to fully reread).

**C — Live-lookup only.** Remove embedded snapshot tables entirely; replace with a short
"read these live sources first" procedure and no enumerated facts at all. Maximizes
correctness, eliminates skill-side maintenance burden for volatile content entirely, at the
cost of a few extra tool calls per session (cheap relative to the risk just observed).

**Recommendation: B.** It keeps the fast-lookup value of the current skills for genuinely
stable content, isolates the part that actually drifts so it can be regenerated instead of
patched, and stops the four skills from maintaining overlapping/diverging copies of the same
"key findings" content (arw-repo-context §8 and arw-observable-analysis §7 already partially
duplicate each other and are already out of sync with one another).

---

## Execution Checklist

### Phase 1 — Content fixes (apply regardless of which structural option is chosen)
- [ ] Add CASE-20260602-0014 to case tables (arw-repo-context §2, arw-observable-analysis §7)
- [ ] Add transfer_v2 deprecation notice for `transfer.py` v1 PCI defect (arw-repo-context §6/§7)
- [ ] Add Q-REL-04 (answered) and Q-REL-05 (open) to arw-observable-analysis §9
- [ ] Add transfer_v2 guards to arw-meta-guard §8 (VOID conditions, TRIVIAL_PARTITION, ARI, file paths)
- [ ] Add one-line pointers for the 5 new clusters (generator admissibility, Σ-persistence,
      KHT resonance dialectic, conflict-navigation/facilitation, quantization/aggregation-limits)
      to arw-repo-context §9 checklist
- [ ] Add the two new anti-patterns to arw-doc-consistency (ID-collision check, `-N` duplicate diff step)
- [ ] Recount case totals in arw-repo-context §2 header

### Phase 2 — Structural decision
- [ ] Confirm with Rico: option A, B, or C
- [ ] If B: draft `arw-repo-pulse`, strip volatile sections from the other 4, add cross-references
- [ ] Re-run the gap analysis once more after restructuring, to confirm nothing was lost in the split

### Phase 3 — Packaging
- [x] Write updated SKILL.md content per skill (preserve unchanged stable sections verbatim)
- [x] Package as `.skill` files
- [x] Update each skill's own Maintenance History section

---

## Status: Executed 2026-07-11

Rico chose **Option B** (split volatile/stable). All Phase 1 content fixes were folded into
the restructuring rather than applied twice. Five `.skill` files were produced and delivered:

- `arw-repo-pulse.skill` — **new**. Holds the case table (incl. CASE-20260602-0014), pipeline
  module inventory with the transfer.py-v1/transfer_v2.py deprecation notice, Q-REL-04/05,
  the 6 newest conceptual clusters, and the open-question ID-prefix map. Designed to be
  replaced wholesale, not hand-edited — refresh procedure included at the end of the file.
- `arw-repo-context.skill` — trimmed to stable content only (framework orientation,
  falsification schema, layer map, case anatomy, transfer-metric *definitions*, foundational
  findings). Every place a case/pipeline/finding specific used to be inlined now points to
  `arw-repo-pulse`.
- `arw-observable-analysis.skill` — kept its full stable methodology; added Q-REL-04/05 and
  the CASE-20260602-0014 row (both were missing), cross-referenced the Σ-persistence/
  signature-derivation cluster, and pointed volatile lookups at the pulse skill.
- `arw-meta-guard.skill` — added v1/v2 TransferMetrics checks (VOID, TRIVIAL_PARTITION, ARI),
  the ID-collision and `-N`-duplicate-diff anti-patterns, and proposed (not yet canonical)
  GUARD-10/11.
- `arw-doc-consistency.skill` — added the same two anti-patterns to its own checklist/sweep
  sections, and updated §9 to reference `arw-repo-pulse`.

**Not done, left for Rico:** actually installing/replacing the live skills with these five
files (that's a user action, not something done automatically here), and promoting the
proposed GUARD-10/11 into `docs/meta/context_map/context_map_pipeline.md` if he agrees with
them (flagged as proposed, not applied, per arw-meta-guard's own "make it visible" rule).
