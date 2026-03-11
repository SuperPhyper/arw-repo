# Boundary Condition Taxonomy

Classification of boundary condition classes, the partition types they generate,
and the metrics for measuring distortion under scope transitions.

## Reading Order

| Document | Content |
|---|---|
| [boundary_condition_classes.md](boundary_condition_classes.md) | Six BC classes with formal definitions, regime consequences, cross-system instantiations |
| [partition_types.md](partition_types.md) | Five partition types (binary, sequential, clustered, multi-stable, hierarchical) |
| [bc_class_to_regime_type_map.md](bc_class_to_regime_type_map.md) | Explicit mapping from BC class to partition type, cross-system verification table |
| [transfer_distortion_metrics.md](transfer_distortion_metrics.md) | Four formal metrics (RCD, TBS, PCI, SDI) for quantifying scope-transition distortion |

## Central Hypothesis

Similar BC classes generate similar regime partition structures across different domains.

This folder operationalizes that hypothesis by:
1. Defining what "similar BC class" means (boundary_condition_classes.md)
2. Defining what "similar partition structure" means (partition_types.md)
3. Predicting which BC class maps to which partition type (bc_class_to_regime_type_map.md)
4. Providing tools to measure when the prediction fails (transfer_distortion_metrics.md)
