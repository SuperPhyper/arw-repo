---
status: note
layer: docs/pipelines/
---

# Regime Graph Pipeline

## Purpose
Extend the partition result A(S) = R_S to the regime transition graph
A*(S) = (R_S, G_S), constructed via admissible perturbations.

Implementation: `pipeline.invariants` computes the adjacency graph G_S
from the partition result. See [pipeline/PartitionPipeline.md](../../pipeline/PartitionPipeline.md).
