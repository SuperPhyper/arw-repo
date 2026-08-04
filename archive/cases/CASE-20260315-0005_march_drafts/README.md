# Archived March Drafts — CASE-20260315-0005 (Multi-Link-Pendel, joint damping, Dissipation)

The prefixed artifact triple from the case's March 2026 registration round, superseded
by the June 2026 revision that the pipeline actually ran.

| File | Date | Superseded by |
|---|---|---|
| `CASE-20260315-0005_ScopeSpec.yaml` | 2026-03-15 | `cases/CASE-20260315-0005/ScopeSpec.yaml` (2026-06-02) |
| `CASE-20260315-0005_BCManifest.yaml` | 2026-03-18 | `cases/CASE-20260315-0005/BCManifest.yaml` (2026-06-02) |
| `CASE-20260315-0005_CaseRecord.yaml` | 2026-03-15 | `cases/CASE-20260315-0005/CaseRecord.yaml` (2026-06-02) |

**Why archived (2026-08-04, core-concept drift audit D-10):** the case directory held two
copies of each artifact — bare-name and `CASE-<id>_`-prefixed — that had diverged by
111–186 lines with nothing marking which was canonical. The bare-name files are what
`sweep.py` / `extract_partition.py` consumed and what `results/partition/` reflects
(N = 8, θ* = 0.1, working ε = 0.05, go 2026-06-02). Same precedent as
`archive/cases/CASE-20260315-0004_stuart_landau/`, archived for the same prefixed-filename
pattern.

Read-only. Do not edit; do not restore into `cases/`.
