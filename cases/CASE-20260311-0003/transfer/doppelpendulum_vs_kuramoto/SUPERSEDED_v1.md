# ⚠ SUPERSEDED — transfer v1 output

**Do not cite the Φ, PCI or SDI values in this directory.**

Produced by `pipeline/transfer.py` (v1). On 2026-06-02 the v1 PCI was found defective:
it was computed as a structural proxy from regime count and adjacency and **never read
per-point regime labels**, making it collinear with RCD and SDI. Roughly 90% of Φ's
weight therefore tracked regime count N, not partition structure. Every v1 Φ is
**withdrawn as evidence of BC-class distance or of structural transfer**.

- **Pair:** CASE-0003 ↔ CASE-0001
- **Superseding v2 run:** none — no v2 run exists for this pair. The nearest v2 evidence is cases/CASE-20260311-0003/transfer_v2/DCTRL1_0003_vs_0007/ (different partner).
- **v1 values recorded here (for provenance only):** Φ = 0.4 (inadmissible), PCI = 0.444, RCD = 5, SDI = 10

Canonical metric definitions: `docs/bc_taxonomy/transfer_distortion_metrics.md`.
Canonical implementation: `pipeline/transfer_v2.py` (real overlap PCI + ARI, guards
`VOID` / `TRIVIAL_PARTITION`, flags `N_CONFOUND` / `COMPONENT_DISAGREEMENT` /
`TBS_WINDOW_FRAGILE`).

Even a valid v2 Φ evidences **partition compatibility only** — necessary, never
sufficient, for structural transfer, and never evidence of shared BC class
(Q-REL-05, open).

*Stamp added 2026-08-04, core-concept drift audit finding D-12.*
