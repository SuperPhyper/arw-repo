# Nested-Path Artifact — CASE-20260315-0007

Byte-identical duplicates of `cases/CASE-20260315-0007/transfer/TransferMetrics.json`
and `TransferReport.md`, written on 2026-06-02 to
`cases/CASE-20260315-0007/cases/CASE-20260315-0007/transfer/` — a doubled output path
from a pipeline run invoked with the case root already in the path argument.

No information is lost by archiving them: the outer copies are identical and remain in
place (now carrying a `SUPERSEDED_v1.md` stamp, since both are v1 transfer output).

Found 2026-08-04, core-concept drift audit follow-up. The now-empty nested directories
could not be removed from this workspace; delete `cases/CASE-20260315-0007/cases/`
manually if desired.
