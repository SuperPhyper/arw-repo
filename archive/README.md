# Archive

This directory holds **completed or superseded artifacts** that are no longer
part of the active research core but are preserved for traceability.

## Structure

```
archive/
├── sessions/     Session-specific working documents from past research sessions.
│                 These have been merged into the canonical docs/ files.
└── transfers/    Summaries of completed cross-case transfer analyses.
                  The source data remains in cases/ — this is a reference index.
```

## Policy

- Documents here are **read-only** — do not edit them.
- The canonical versions of merged content live in `docs/notes/`.
- A file is archived when: (a) its content has been integrated into a canonical doc,
  or (b) it is session-scoped and no longer reflects current state.

## Index

### sessions/

| File | Session | Merged into |
|---|---|---|
| `README_session_2026-03-18.md` | 2026-03-18 | — (session summary, no merge needed) |
| `research_journal_session_2026-03-18.md` | 2026-03-18 | `docs/notes/research_journal.md` |
| `open_questions_2026-03-18.md` | 2026-03-18 | `docs/notes/open_questions.md` |
| `open_questions_session_2026-03-18.md` | 2026-03-18 | `docs/notes/open_questions.md` |

### transfers/

| Transfer | Cases | Φ | Status |
|---|---|---|---|
| kuramoto_vs_pendulum | CASE-0001 ↔ CASE-0002 | 0.675 (partially_admissible) | completed |
| pendulum_vs_kuramoto | CASE-0002 ↔ CASE-0001 | 0.675 (partially_admissible) | completed |
| doppelpendulum_vs_kuramoto | CASE-0003 ↔ CASE-0001 | 0.40 raw / ≈0.95 matched-ε | completed |

Source data: `cases/CASE-*/transfer/`
