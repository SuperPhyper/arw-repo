---
status: note
layer: archive/transfers/
---

# Archive — Completed Transfers

Reference index for completed cross-case transfer analyses.
Source data (TransferMetrics.json, TransferReport.md) lives in `cases/*/transfer/`.
This directory is an **index only** — no data is duplicated here.

---

## Completed Transfers

| Transfer | Cases | Φ | Admissibility | Source |
|---|---|---|---|---|
| kuramoto_vs_pendulum | CASE-0001 ↔ CASE-0002 | 0.675 | partially_admissible | [cases/CASE-20260311-0001/transfer/kuramoto_vs_pendulum/](../../cases/CASE-20260311-0001/transfer/kuramoto_vs_pendulum/) |
| pendulum_vs_kuramoto | CASE-0002 ↔ CASE-0001 | 0.675 | partially_admissible | [cases/CASE-20260311-0002/transfer/pendulum_vs_kuramoto/](../../cases/CASE-20260311-0002/transfer/pendulum_vs_kuramoto/) |
| doppelpendulum_vs_kuramoto | CASE-0003 ↔ CASE-0001 | 0.40 raw / ≈0.95 matched-ε | highly_admissible (matched-ε) | [cases/CASE-20260311-0003/transfer/doppelpendulum_vs_kuramoto/](../../cases/CASE-20260311-0003/transfer/doppelpendulum_vs_kuramoto/) |

---

## Key Notes

**Φ measures observable transfer, not system transfer** (Finding 11, session 2026-03-18).
Two systems with the same physical BC structure but different observables may show low Φ.
Transfer reports document observable BC structures (e.g. r_ss = R³·A·D) for both scopes.

**Metrics reference:** `docs/bc_taxonomy/transfer_distortion_metrics.md`
