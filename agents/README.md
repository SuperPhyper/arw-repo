---
status: note
layer: agents/
---

# Agents

Agent role definitions for the multi-agent research scaffold.

---

## Planned Roles

| Agent | Role | Pipeline step |
|---|---|---|
| A0 | Orchestrator | `new_case`, registry management |
| A1 | Scope Formalizer | fills `ScopeSpec.yaml` |
| A2 | Boundary Taxonomist | fills `BCManifest.yaml` |
| A3 | Partition Engineer | runs `sweep`, `extract_partition`, `invariants` |
| A4 | Transfer Analyst | runs `transfer` |
| A5 | Skeptic / Failure Auditor | runs `audit_helpers` |

Key principle: no agent retains state between sessions.
All progress lives in artifacts. Any agent can be replaced or re-run
from the artifact state alone.

---

## Status

Placeholder — role definitions are currently documented in
[pipeline/PartitionPipeline.md](../pipeline/PartitionPipeline.md) § Agent Role Mapping.
