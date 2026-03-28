---
status: working-definition
layer: docs/meta/
last_updated: 2026-03-29
---

# ARW Repository Maintenance Checklist

Recurring checklist for keeping the repository clean, consistent, and research-ready.
Run this after every major session or before committing a batch of changes.

---

## 1. Case Artifact Completeness

For each directory in `cases/CASE-YYYYMMDD-####/`:

- [ ] `ScopeSpec.yaml` present
- [ ] `BCManifest.yaml` present
- [ ] `CaseRecord.yaml` present
- [ ] `README.md` present
- [ ] `ScopeSpec_signature_first.md` present (for cases created after 2026-03-15)
- [ ] All filenames are standard (no `CASE-YYYYMMDD-####_` prefixes)
- [ ] Pi-block observables each have a `primary: true/false` field
- [ ] `CaseRecord.yaml` has a `go_nogo` verdict (not blank/missing)
- [ ] If pipeline has run: `results/partition/Invariants.json` includes `sweep_range: [min, max]`
- [ ] Observable sufficiency fields present in ScopeSpec (`observable_sufficiency:`)

Pre-pipeline cases (`pipeline_status: pre-pipeline`) are exempt from results checks.

---

## 2. Document Front-Matter

For every `.md` file in `docs/` subdirs (except `README.md` files and `notes/`):

- [ ] YAML front-matter block present at top
- [ ] `status:` field is one of: `definition | claim | hypothesis | note | open-question | working-definition`
- [ ] `layer:` field matches the actual directory path

Exempt from front-matter: `README.md`, figure caption files in `figures/`, working notes in `docs/notes/`.

---

## 3. Language Consistency

- [ ] All canonical `.md` and `.yaml` files in `docs/` and `cases/` are written in English
- [ ] German prose is only acceptable in `docs/notes/` (informally) and session archives
- [ ] Run: `grep -rn "[äöüÄÖÜß]" docs/ cases/ --include="*.md" --include="*.yaml"` to spot-check

---

## 4. Archive Hygiene

- [ ] `archive/README.md` index is up to date (all archived sessions and cases listed)
- [ ] No exact duplicate files in `archive/sessions/` — verify with `md5sum archive/sessions/*.md | sort | uniq -d`
- [ ] No draft cases remain in `cases/` that have a production successor in `cases/` (→ archive)
- [ ] `archive/cases/` entries are all referenced in the archive README index

---

## 5. Docs Index Consistency

- [ ] `docs/INDEX.md` reflects all current docs files (no orphaned entries, no missing files)
- [ ] New conceptual documents added to index before or immediately after creation
- [ ] Use `arw-doc-consistency` skill when in doubt

---

## 6. Open Questions & Research Journal

- [ ] `docs/notes/open_questions.md` — no questions are stale (check status fields)
- [ ] `docs/notes/research_journal.md` — last session findings have been added
- [ ] Session-specific working docs archived after integration (see archive policy)

---

## 7. Transfer Coverage

- [ ] `archive/README.md` → `transfers/` index lists all completed cross-case transfers
- [ ] Planned transfers (from skill context) are still current
- [ ] Φ values and admissibility verdicts match the TransferMetrics.json files in `cases/`

---

## 8. Pipeline Validation

Run from repo root when pipeline code or schemas have changed:

```bash
python pipeline/validate.py          # Schema validation across all cases
python pipeline/audit.py             # Failure audit checks
```

- [ ] `validate.py` exits with 0 errors (warnings are documented in `docs/meta/audit_report_YYYY-MM-DD.md`)
- [ ] `audit.py` produces no new unresolved findings
- [ ] If warnings exist: create or update `docs/meta/audit_report_YYYY-MM-DD.md`

---

## 9. docs/cases/ Motivational Documents (TODO)

- [ ] **Pending:** Write one motivational `.md` per active case in `docs/cases/`
  - CASE-20260311-0001 — Kuramoto (Coupling)
  - CASE-20260311-0002 — Multi-Link-Pendel (Coupling)
  - CASE-20260311-0003 — Doppelpendel (Restriction)
  - CASE-20260318-0004 — Coupled Stuart-Landau (Coupling / emergence)
- [ ] Template available: `docs/cases/CASE_TEMPLATE_signature_first.md`

---

## 10. Skill Consistency

- [ ] `arw-repo-context` skill case table matches actual cases in `cases/`
- [ ] `arw-meta-guard` rules reflect current schema requirements
- [ ] Run `skill-maintenance` skill after any structural repo change

---

## Quick Reference — Common Issues

| Code | Issue | Fix |
|---|---|---|
| CR-01 | CaseRecord go_nogo verdict missing | Add verdict to go_nogo block |
| SS-04 | Observable missing `observable_sufficiency` | Add field to Pi block |
| TM-04 | phi_matched_epsilon missing at ε-mismatch | Compute and add to TransferMetrics.json |
| MD-04 | German text in English-only file | Translate or move to notes/ |
| ARCH-01 | Duplicate file in archive/ | Delete the redundant copy |
| CASE-NM | Non-standard case dir name | Rename to `CASE-YYYYMMDD-####` |
