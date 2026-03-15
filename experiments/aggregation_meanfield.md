---
status: working-definition
---

# ART Instantiation: Agent ↔ Mean-Field Scope Comparison
## Cross-Scope Admissibility and Distortion Analysis

This document defines the ART scope for the mean-field aggregation experiment.
It is the direct companion to [agent_consensus_models.md](agent_consensus_models.md)
and constitutes the **primary cross-scope comparison** of Phase 2.

The experiment's purpose is not to study opinion dynamics per se,
but to use the opinion dynamics system as a controlled environment
in which the ARW cross-scope comparison methodology can be developed,
calibrated, and stress-tested.

---

## 1 The Cross-Scope Comparison Problem

The central ARW question for this experiment:

> Given two scopes S_agent and S_mf describing the same underlying system,
> when is S_agent → S_mf an admissible reduction,
> and how can the degree of inadmissibility be quantified?

The agent-level scope S_agent tracks individual agents.
The mean-field scope S_mf tracks aggregate population distributions.

These are different **descriptive regimes** of the same system —
not different models of different things.

---

## 2 Mean-Field Scope Definition

### S_MF

```
S_MF = (B_MF, Π_MF, Δ_MF, ε_MF)
```

**B_MF — Boundary Conditions**

- Large population limit: N → ∞ (or N sufficiently large)
- Homogeneous mixing: every agent is equally likely to interact with every other
- No correlations between agents beyond what ρ(x,t) captures
- Bounded confidence rule applied to distribution

BC class: **aggregation** — the defining BC of mean-field descriptions.
Individual agent identities and their correlations are suppressed by construction.

**Π_MF — Observables**

```
Π_MF = { ρ(x, t) : x ∈ [0,1] }
```

The opinion density distribution ρ(x,t) is the sole observable.
ρ(x,t)dx = fraction of agents with opinion in [x, x+dx] at time t.

Individual agent states xᵢ are invisible at this scope.
Correlations between agent pairs are invisible at this scope.

**Δ_MF — Admissible Perturbations**

- Smooth perturbations to ρ: ||δρ||_L1 < 0.05
- Perturbations that preserve total probability: ∫δρ dx = 0
- Local opinion shifts that do not reorganize peak structure

**ε_MF — Resolution Threshold**

```
ε_MF: distribution differences with ||ρ - ρ'||_L1 < 0.05 are indistinguishable
```

Individual agent movements that don't shift the distribution are below resolution.

---

## 3 Mean-Field Regime Partition

```
A(S_MF) = R_MF
```

| Regime | Distribution signature | ε_bc range |
|---|---|---|
| R_MF1 — Consensus | ρ(x,t) → δ(x - x*) single peak | ε_bc > 0.5 |
| R_MF2 — Polarization | ρ(x,t) → α·δ(x - x₁) + (1-α)·δ(x - x₂) | 0.2 < ε_bc < 0.5 |
| R_MF3 — Fragmentation | ρ(x,t) → Σ αₖ·δ(x - xₖ), k ≥ 3 | ε_bc < 0.2 |

Note: R_MF4 (frozen disorder) from the agent-level scope
does not appear cleanly at this resolution —
a diffuse distribution is below ε_MF resolution.
This is already a **distortion signal**.

---

## 4 Formal Cross-Scope Comparison

### Scope pair

```
S_agent = (B_Op, Π_Op, Δ_Op, ε_Op)     [from agent_consensus_models.md]
S_MF    = (B_MF, Π_MF, Δ_MF, ε_MF)
```

### Admissibility criterion

The reduction S_agent → S_MF is admissible if:

```
for every x ∈ D: [x]_agent ⊆ [x]_MF
```

Each agent-level regime class must be fully contained within
a mean-field regime class on the relevant domain D.

### Compatibility matrix

| Agent regime | MF regime | Compatible? | Condition |
|---|---|---|---|
| R_Op1 (Consensus) | R_MF1 | ✓ | Always |
| R_Op2 (Polarization) | R_MF2 | ✓ | Large N |
| R_Op3 (Fragmentation) | R_MF3 | ✓ | Large N |
| R_Op4 (Frozen disorder) | — | ✗ | No MF equivalent at ε_MF |
| R_Op1/R_Op2 boundary | R_MF1 or R_MF2 | ⚠ | Finite-N fluctuations cause misclassification |

### Distortion zones

Three distinct distortion zones are predicted:

**Zone 1 — R_Op4 invisibility:**
Frozen disorder is below resolution at S_MF.
The mean-field scope cannot distinguish R_Op4 from R_Op3 near the boundary.

**Zone 2 — Transition boundary shift:**
The ε_bc value at which R_Op1 → R_Op2 occurs shifts between scopes.
This shift is a function of N and quantifies finite-size distortion.

**Zone 3 — Cluster count disagreement:**
Near fragmentation boundaries, the number of clusters detected differs
between S_agent and S_MF. S_MF under-counts due to ε_MF resolution.

---

## 5 Distortion Metric Development

This experiment develops the following quantitative metrics:

### Metric 1 — Transition Boundary Shift (TBS)

```
TBS(N) = |ε_bc*(S_agent, N) - ε_bc*(S_MF)|
```

Measures how much the regime transition boundary shifts between scopes.
Expected: TBS(N) → 0 as N → ∞, TBS(N) > 0 for finite N.

### Metric 2 — Regime Count Discrepancy (RCD)

```
RCD = | |R_agent| - |R_MF| |
```

Measures how many regime classes are lost or merged under aggregation.
Expected: RCD = 1 for R_Op4 (always invisible at S_MF).

### Metric 3 — Partition Compatibility Index (PCI)

For each agent-level regime class Rᵢ, define compatibility:

```
PCI(Rᵢ) = 1  if [x]_agent ⊆ [x]_MF for all x ∈ Rᵢ
PCI(Rᵢ) = fraction of Rᵢ correctly classified otherwise
```

Overall: PCI = mean over all classes. Expected: PCI < 1 near transition boundaries.

### Metric 4 — Structural Distortion Index (SDI)

Compare the **regime graph** (adjacency structure of regime transitions)
between S_agent and S_MF:

```
SDI = graph_edit_distance(G_agent, G_MF)
```

where G_agent and G_MF are the directed graphs of admissible transitions.
Expected: SDI = 0 for large N, SDI > 0 when R_Op4 is absent from G_MF.

---

## 6 Experimental Protocol

### Phase A — Baseline partition extraction

1. Simulate N = {50, 200, 1000, 5000} agents
2. Sweep ε_bc ∈ [0.05, 0.6] in steps of 0.01
3. At each (N, ε_bc): extract regime partition under S_agent and S_MF
4. Record TBS, RCD, PCI, SDI as functions of N and ε_bc

### Phase B — Admissibility boundary mapping

1. For each N, identify ε_bc* where PCI drops below threshold (0.9)
2. Map the admissibility boundary in (N, ε_bc) parameter space
3. Fit functional form: TBS(N) ~ N^{-α}

### Phase C — Network topology variation

Repeat Phase A with scale-free and lattice topologies.
Expected: topology changes BC class, shifts admissibility boundary.

---

## 7 Connection to ARW Research Questions

| Research question | This experiment |
|---|---|
| Can transfer failure be quantified? | Yes — TBS, RCD, PCI, SDI are concrete metrics |
| When does scope reduction become inadmissible? | Admissibility boundary in (N, ε_bc) space |
| Is distortion systematic or random? | Expected: systematic, driven by finite-N effects |
| Do BC classes determine distortion patterns? | Network topology variation tests this |

---

## 8 Falsification Conditions

- TBS does not decrease with N — mean-field is not an asymptotic limit of agent scope
- PCI = 1 everywhere — no distortion exists, cross-scope comparison is trivial
- Distortion is random — no systematic structure, metrics are uninformative
- SDI = 0 for all N — regime graphs are always identical across scopes

---

*For the agent-level scope definition, see [agent_consensus_models.md](agent_consensus_models.md).*
*For distortion metric concepts, see [docs/bc_taxonomy/transfer_distortion_metrics.md](../docs/bc_taxonomy/transfer_distortion_metrics.md).*
*For the admissibility criterion, see [docs/core/arw_scope_reduction_partition_criterion.md](../docs/core/arw_scope_reduction_partition_criterion.md).*
