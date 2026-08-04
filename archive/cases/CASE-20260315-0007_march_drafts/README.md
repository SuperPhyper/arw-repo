# Archived March Drafts — CASE-20260315-0007 (SIR epidemic, Aggregation)

The prefixed artifact triple from the case's March 2026 registration round, superseded
by the June 2026 revision that the pipeline actually ran.

| File | Date | Superseded by |
|---|---|---|
| `CASE-20260315-0007_ScopeSpec.yaml` | 2026-03-15 | `cases/CASE-20260315-0007/ScopeSpec.yaml` (2026-06-02) |
| `CASE-20260315-0007_BCManifest.yaml` | 2026-03-15 | `cases/CASE-20260315-0007/BCManifest.yaml` (2026-06-02) |
| `CASE-20260315-0007_CaseRecord.yaml` | 2026-03-15 | `cases/CASE-20260315-0007/CaseRecord.yaml` (2026-06-02) |

**Why archived (2026-08-04, core-concept drift audit D-10):** the case directory held two
copies of each artifact — bare-name and `CASE-<id>_`-prefixed — that had diverged by
131–297 lines with nothing marking which was canonical. The bare-name files are what the
pipeline consumed and what `results/partition/` reflects (N = 2, θ* = 0.2, working
ε = 0.10, go 2026-06-02, `status: complete`). Same precedent as
`archive/cases/CASE-20260315-0004_stuart_landau/`.

Read-only. Do not edit; do not restore into `cases/`.
