# Cases

Each subdirectory contains all artifacts for a single experiment instance.
A case bundles the full pipeline output for one system under one scope:
ScopeSpec → BCManifest → sweep → partition → invariants → transfer → audit.

---

## Case Structure

```
CASE-YYYYMMDD-####/
├── ScopeSpec.yaml              ← ART scope instantiation
├── BCManifest.yaml             ← BC classification + sweep program
├── CaseRecord.yaml             ← Case envelope (status, artifact registry)
├── results/
│   ├── raw/
│   │   └── sweep_results.json  ← Raw sweep output
│   └── partition/
│       ├── PartitionResult.json
│       └── Invariants.json
├── transfer/
│   └── <comparison_name>/
│       ├── TransferMetrics.json
│       └── TransferReport.md
└── audits/
    └── FailureAudit_Phase{N}.md
```

---

## Current Cases

| Case ID | System | Phase | Status |
|---|---|---|---|
| [CASE-20260311-0001](CASE-20260311-0001/) | Kuramoto oscillators | 1 (calibration) | End-to-end complete |
| [CASE-20260311-0002](CASE-20260311-0002/) | Multi-link pendulum | 1 (calibration) | Open |

---

## Creating a New Case

```bash
python -m pipeline.new_case --id CASE-YYYYMMDD-#### --system <system> --phase <N>
```

This scaffolds the directory structure and stamps schema copies with the case ID.
See [pipeline/README.md](../pipeline/README.md) for full CLI reference.

---

## Design Principle

No agent retains state between sessions.
All progress lives in artifacts. Any agent can be replaced or re-run
from the artifact state alone.
