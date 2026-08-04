# Nested-Path Artifact — CASE-20260318-0004

Byte-identical duplicates of `cases/CASE-20260318-0004/transfer/TransferMetrics.json`
and `TransferReport.md`, written on 2026-06-02 to
`cases/CASE-20260318-0004/cases/CASE-20260318-0004/transfer/` — a doubled output path
from a pipeline run invoked with the case root already in the path argument.

The outer copies remain in place and carry a `SUPERSEDED_v1.md` stamp. These are the
files holding the **Φ = 0.9983 `highly_admissible`** v1 result for CASE-0004 ↔ CASE-0001
that `docs/advanced/framework_validation.md` was built on; the v2 recomputation of the
same pair gives Φ = 0.7794 `ambiguous_requires_inspection` with `N_CONFOUND` and
`COMPONENT_DISAGREEMENT`. Having a second, unstamped copy of that number in a
nonstandard path was a live miscitation risk.

Found 2026-08-04, core-concept drift audit follow-up. The now-empty nested directories
could not be removed from this workspace; delete `cases/CASE-20260318-0004/cases/`
manually if desired.
