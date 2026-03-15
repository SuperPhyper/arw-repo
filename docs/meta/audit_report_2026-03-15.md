---
status: note
layer: docs/meta/
generated: 2026-03-15
---

# ARW Audit Report — 2026-03-15

**Files checked:** 165  
**Errors:** 0  
**Warnings:** 15  

## Warnings

### `cases/CASE-20260311-0001/CaseRecord.yaml`
- [CR-01] v0.2: go_nogo block present but verdict missing

### `cases/CASE-20260311-0001/ScopeSpec.yaml`
- [SS-04] Observable 'r_ss' missing observable_sufficiency

### `cases/CASE-20260311-0001/transfer/kuramoto_vs_pendulum/TransferMetrics.json`
- [TM-04] N_A≠N_B (ε-mismatch): phi_matched_epsilon missing

### `cases/CASE-20260311-0001/transfer/kuramoto_vs_pendulum/TransferReport_extended.md`
- [MD-04] German text detected — repo language is English

### `cases/CASE-20260311-0002/CaseRecord.yaml`
- [CR-01] v0.2: go_nogo block present but verdict missing

### `cases/CASE-20260311-0002/ScopeSpec.yaml`
- [SS-04] Observable 'var_rel' missing observable_sufficiency
- [SS-04] Observable 'lambda_proxy' missing observable_sufficiency

### `cases/CASE-20260311-0002/transfer/pendulum_vs_kuramoto/TransferMetrics.json`
- [TM-04] N_A≠N_B (ε-mismatch): phi_matched_epsilon missing

### `cases/CASE-20260311-0003/CaseRecord.yaml`
- [CR-01] v0.2: go_nogo block present but verdict missing

### `cases/CASE-20260311-0003/ScopeSpec.yaml`
- [SS-04] Observable 'lambda_proxy' missing observable_sufficiency
- [SS-04] Observable 'var_rel' missing observable_sufficiency
- [SS-04] Observable 'E_mean' missing observable_sufficiency

### `cases/CASE-20260311-0003/transfer/doppelpendulum_vs_kuramoto/TransferMetrics.json`
- [TM-04] N_A≠N_B (ε-mismatch): phi_matched_epsilon missing

### `cases/CASE-20260311-0003/transfer/doppelpendulum_vs_kuramoto/TransferReport.md`
- [MD-04] German text detected — repo language is English

### `docs/notes/research_journal.md`
- [MD-04] German text detected — repo language is English

## Violations by Rule

| Rule | Count | Type |
|---|---|---|
| CR-01 | 3 | Warning |
| MD-04 | 3 | Warning |
| SS-04 | 6 | Warning |
| TM-04 | 3 | Warning |