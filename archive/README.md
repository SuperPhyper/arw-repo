# Archive

This directory holds **completed or superseded artifacts** that are no longer
part of the active research core but are preserved for traceability.

## Structure

```
archive/
├── sessions/     Session-specific working documents from past research sessions.
│                 These have been merged into the canonical docs/ files.
├── transfers/    Summaries of completed cross-case transfer analyses.
│                 The source data remains in cases/ — this is a reference index.
└── cases/        Draft or superseded case directories that have been replaced by
                  a production case. Preserved for traceability.
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
| `open_questions_session_2026-03-18.md` | 2026-03-18 | `docs/notes/open_questions.md` |

### transfers/

| Transfer | Cases | Φ | Status |
|---|---|---|---|
| kuramoto_vs_pendulum | CASE-0001 ↔ CASE-0002 | 0.675 (partially_admissible) | completed |
| pendulum_vs_kuramoto | CASE-0002 ↔ CASE-0001 | 0.675 (partially_admissible) | completed |
| doppelpendulum_vs_kuramoto | CASE-0003 ↔ CASE-0001 | 0.40 raw / ≈0.95 matched-ε | completed |

Source data: `cases/CASE-*/transfer/`

> **All Φ values in the table above were produced by `pipeline/transfer.py` (v1) and are
> withdrawn as evidence of BC-class distance** — the v1 PCI never read per-point regime
> labels and was collinear with RCD/SDI (finding of 2026-06-02). The v1 output
> directories under `cases/*/transfer/` carry a `SUPERSEDED_v1.md` stamp since
> 2026-08-04. Canonical values, where a v2 run exists, are in
> `cases/*/transfer_v2/<A>_vs_<B>/TransferMetrics_v2.json`.

### cases/

| Directory | System | Reason archived | Superseded by |
|---|---|---|---|
| `CASE-20260315-0004_stuart_landau/` | Coupled Stuart-Landau | Pre-pipeline draft; non-standard naming; artifact filenames prefixed | `cases/CASE-20260318-0004/` |
| `CASE-20260315-0005_march_drafts/` | Multi-Link-Pendel, joint damping (Dissipation) | March 2026 prefixed artifact triple; diverged 111–186 lines from the June revision the pipeline ran, with nothing marking canonical status (drift audit D-10) | `cases/CASE-20260315-0005/*.yaml` (bare names) |
| `CASE-20260315-0007_march_drafts/` | SIR epidemic (Aggregation) | March 2026 prefixed artifact triple; diverged 131–297 lines from the June revision the pipeline ran (drift audit D-10) | `cases/CASE-20260315-0007/*.yaml` (bare names) |
| `CASE-20260430-0013_pendulum_drafts/` | Multi-link pendulum → spring-mass chain | Earlier ScopeSpec iterations; system redesigned | `cases/CASE-20260430-0013/ScopeSpec_signature_first.md` |
| `CASE-20260315-0007_nested_path_artifact/` | SIR epidemic | Byte-identical transfer output written to a doubled path `cases/<id>/cases/<id>/transfer/` | `cases/CASE-20260315-0007/transfer/` |
| `CASE-20260318-0004_nested_path_artifact/` | Coupled Stuart-Landau | Same doubled-path defect; held an unstamped second copy of the withdrawn Φ = 0.9983 v1 result | `cases/CASE-20260318-0004/transfer/` |

**Rule going forward:** a case directory holds **exactly one copy** of each artifact.
Where both a bare-name and a `CASE-<id>_`-prefixed copy exist, the bare name is
canonical and the prefixed copy is archived here. Cases registered in March 2026 that
were never revised (0006, 0008, 0009, SOC1) carry *only* prefixed filenames — that is a
naming inconsistency, not a duplication, and is left as is until those cases are run.
