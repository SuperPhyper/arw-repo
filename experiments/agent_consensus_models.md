---
status: working-definition
---

# ART Instantiation: Agent Consensus Models
## Opinion Dynamics — Consensus, Polarization, Fragmentation Regimes

This document defines the ART scope for the agent-based opinion dynamics experiment.
This system is the primary **social regime test case** of Phase 2:
it provides a well-studied agent-based model whose regime structure
(consensus / polarization / fragmentation) maps directly onto
ARW partition concepts, and whose mean-field reduction is explicitly tested
in the companion experiment [aggregation_meanfield.md](aggregation_meanfield.md).

---

## 1 System Description

**Domain:** Agent-based social dynamics — opinion formation in networked populations

**Why this system:**
Opinion dynamics models are well-studied, have known regime structures,
and admit explicit mean-field reductions (e.g., Deffuant model, bounded confidence).
The regime transition from consensus to polarization to fragmentation
is a clean test case for BC-induced regime generation and cross-scope comparison.

**State space X:**
N agents, each with an opinion xᵢ ∈ [0, 1]:

```
x = (x₁, x₂, ..., x_N) ∈ [0,1]^N
```

Agents interact according to an update rule governed by boundary conditions.

**Key control parameters:**
- Confidence bound ε_bc (not to be confused with ARW resolution ε)
- Network topology (all-to-all, lattice, scale-free)
- Interaction frequency and asynchrony

---

## 2 Scope Definition

### Agent-Level Scope S_Op

```
S_Op = (B_Op, Π_Op, Δ_Op, ε_Op)
```

**B_Op — Boundary Conditions**

- N agents with bounded confidence: agents only interact if |xᵢ - xⱼ| < ε_bc
- Opinion space bounded: xᵢ ∈ [0, 1]
- Synchronous or asynchronous update schedule
- Fixed network topology (initially all-to-all)

BC class: **coupling (confidence-bounded) + restriction (bounded opinion space)**

The confidence bound ε_bc is the primary BC parameter.
It determines which interactions are admissible — a direct ARW boundary condition.

**Π_Op — Observables**

```
Π_Op = { x₁(t), ..., x_N(t), cluster_structure(t) }
```

Individual opinions and their clustering structure are tracked.
Cluster structure: partition of agents into groups with |xᵢ - xⱼ| < δ_cluster.

**Δ_Op — Admissible Perturbations**

- Small perturbations to individual opinions: δxᵢ < 0.02
- Single agent opinion resets
- Temporary removal of single interaction links

**ε_Op — Resolution Threshold**

```
ε_Op: opinion differences < 0.02 are indistinguishable
```

Agents within 0.02 opinion distance are in the same regime class.

---

## 3 Regime Partition under S_Op

```
A(S_Op) = R_Op
```

| Regime | Behavioral signature | ε_bc range |
|---|---|---|
| R_Op1 — Consensus | All agents converge to single opinion cluster | ε_bc > 0.5 |
| R_Op2 — Polarization | Exactly two stable opinion clusters, symmetric | 0.2 < ε_bc < 0.5 |
| R_Op3 — Fragmentation | Three or more stable clusters, system-size dependent | ε_bc < 0.2 |
| R_Op4 — Frozen disorder | No convergence, opinion diversity maintained | Very small ε_bc |

**Structural observation:**
The BC parameter ε_bc directly determines which interactions are admissible (B_Op)
and therefore which regime partition emerges. This is a direct demonstration
of the ARW claim: **boundary conditions generate regime structures**.

R_Op2 (polarization) is of particular interest — it is a BC-induced
symmetry-breaking regime that disappears under both stronger and weaker coupling.

---

## 4 Network Topology Variation

Changing the network topology changes B_Op while keeping Π_Op constant.

| Topology | BC change | Expected partition shift |
|---|---|---|
| All-to-all | Baseline | Clean R_Op1–R_Op4 structure |
| Scale-free | High-degree hubs dominate interactions | R_Op2 destabilized — hubs drive consensus faster |
| Lattice | Local interactions only | R_Op3 enriched — local clusters persist longer |
| Modular (community structure) | Inter-community links sparse | R_Op2 replaced by community-locked polarization |

Each topology change is a BC class variation (coupling topology).
This tests the hypothesis: **similar BC classes → similar regime graphs**.

---

## 5 Cross-Scope Comparison: S_Op → Mean-Field S_MF_Op

The companion experiment [aggregation_meanfield.md](aggregation_meanfield.md)
defines the mean-field scope formally. Here we specify the compatibility prediction.

**Mean-field scope S_MF_Op:**

```
Π_MF_Op = { ρ(x, t) }  — opinion density distribution
```

Individual agent identities are suppressed. Only the population-level
opinion distribution is tracked.

**Admissibility prediction:**

| S_Op regime | Maps to S_MF_Op regime | Compatible? |
|---|---|---|
| R_Op1 (Consensus) | Single delta-peak in ρ | ✓ |
| R_Op2 (Polarization) | Two delta-peaks in ρ | ✓ |
| R_Op3 (Fragmentation) | Multiple peaks in ρ | ✓ for large N |
| R_Op4 (Frozen disorder) | Broad ρ distribution | ⚠ finite-N dependent |

**Partial admissibility region:**
Near the R_Op1/R_Op2 transition boundary, finite-N fluctuations cause
the mean-field description to misclassify states.
This is the expected **distortion zone** — quantifiable as a function of N.

---

## 6 Distortion Metrics

| Metric | Definition | Expected behavior |
|---|---|---|
| Transition boundary shift | |ε_bc*(S_Op) - ε_bc*(S_MF_Op)| | → 0 as N → ∞ |
| Regime count match | |R_Op| vs |R_MF_Op| at same ε_bc | Match for large N |
| Polarization detection accuracy | Does S_MF_Op detect R_Op2? | Fails near boundary for small N |

---

## 7 Connection to ARW Research Questions

| Research question | Consensus model test |
|---|---|
| Do BC classes generate characteristic regime structures? | ε_bc directly maps to regime type — clean demonstration |
| Can regime structures transfer across scopes? | S_Op → S_MF_Op admissibility tested explicitly |
| Can distortion be quantified? | Transition boundary shift as function of N |
| Do similar BC classes produce similar regime graphs? | Network topology comparison |

---

## 8 Falsification Conditions

- No stable cluster structure emerges — opinion dynamics are purely continuous
- Regime transitions are not BC-driven — ε_bc changes produce no partition change
- Mean-field description perfectly matches agent-level for all N — distortion metrics are zero
- Network topology changes produce no regime partition shift — BC class hypothesis fails

---

*For the mean-field comparison, see [aggregation_meanfield.md](aggregation_meanfield.md).*
*For BC taxonomy, see [docs/bc_taxonomy/boundary_condition_classes.md](../docs/bc_taxonomy/boundary_condition_classes.md).*
