---
status: working-definition
layer: docs/art_instantiations/
title: "KHT Unified Architecture — Index"
created: 2026-05-14
part_of: kht_unified_architecture
---

# KHT Unified Architecture — Index

This document is the entry point for the KHT (Kognitive Hierarchie Theorie) unified
architecture series. It describes the four-layer structure, the causal relationships
between layers, and the status of each document.

---

## Architecture Overview

KHT is a four-layer architecture with a strict bottom-up causal direction. Each layer
is an emergent coarsening of the one below it — not a replacement but a higher-level
description of phenomena that arise when constraints are applied to the layer beneath.

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 4: AI Context Navigation Simulation                  │
│  Computational instantiation of Layers 1–3 as a            │
│  behavioral proxy for a KHT-typed agent.                    │
│  → kht_architecture_layer4.md                               │
└──────────────────────────────┬──────────────────────────────┘
                               │ downstream application
┌──────────────────────────────▼──────────────────────────────┐
│  Layer 3: Dynamic Regime Transitions                        │
│  Four cognitive regimes (Ego, Subconscious, Unconscious,    │
│  Superego) driven by control parameters (τ, σ, ξ).         │
│  Includes social-level dynamics and the Resonance Mechanism.│
│  → kht_architecture_layer3.md                               │
└──────────────────────────────┬──────────────────────────────┘
                               │ contextual perturbations
┌──────────────────────────────▼──────────────────────────────┐
│  Layer 2: Persistent Profiles                               │
│  16 coverage-complete profiles emerge from the Layer 1      │
│  space via biological BCs (Restriction + Dissipation).      │
│  The Appendix function hierarchy is a Layer 2 output.       │
│  → kht_architecture_layer2.md                               │
└──────────────────────────────┬──────────────────────────────┘
                               │ biological BCs
┌──────────────────────────────▼──────────────────────────────┐
│  Layer 1: The Operator–Modulator Space                      │
│  32 fully symmetric primitive cognitive combinations:       │
│  4 operators × 8 modulator clusters.                        │
│  Formal null model; no hierarchy, no type, no trajectory.   │
│  → kht_architecture_layer1.md                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Layer Summaries

### Layer 1 — The Operator–Modulator Space
**File:** `kht_architecture_layer1.md`

The foundational primitive space. Four trajectory-free operators (Ni, Si, Ne, Se)
combined with eight modulator clusters (from three binary axes: T/F, I/E, J/P) yield
32 fully symmetric Operator–Modulator combinations. No combination is structurally
privileged at this level.

Key contributions:
- Formal separation of operator (what is processed) from modulator (how it is processed)
- Duality map: each (O, M) pair has a unique dual (O*, M*) via simultaneous operator-pair
  swap and full modulator inversion
- Distance metric on O×M: d = d_op + Hamming(M), range 0–5
- Layer 1 as formal null model: the symmetry that biological BCs must break

Reconciliation with Appendix: the eight Appendix functions (Ni, Fe, Ti, Se, ...) are
Layer 1 combinations at a fixed I/E modulator setting — a coarser description, not
a contradiction.

---

### Layer 2 — Persistent Profiles
**File:** `kht_architecture_layer2.md`

The 16 stable psychological types emerge through two sequential biological boundary
conditions acting on the Layer 1 space:

1. **Restriction** (genetic connectivity bias): selects the accessible profile subspace X_B
2. **Dissipation** (Hebbian consolidation): converges on a dominant attractor within X_B

Profiles are structurally valid if and only if they satisfy the **coverage criterion**:
minimal complete coverage of all three modulator axes and both operator families. Applied
to the Layer 1 duality geometry, this yields exactly 16 valid profiles.

Key contributions:
- The number 16 is a structural consequence of coverage + duality, not a taxonomic choice
- The Appendix function hierarchy (Ni > Fe > Ti > Se) is the relative activation weighting
  produced by Dissipation — a Layer 2 dynamic property, not a primitive postulate
- Profile identity (which blocks) vs. activation weighting (relative priority within blocks)
  are formally distinguished
- Falsifiable prediction: coverage-violating profiles exhibit higher regime instability

---

### Layer 3 — Dynamic Regime Transitions
**File:** `kht_architecture_layer3.md`

Within the adult adaptation phase, contextual perturbations drive transitions between
four cognitive regimes. Each transition is characterized by its distance in the Layer 1
metric and by what structurally changes:

| Transition | Distance | Character |
|---|---|---|
| R1 → R2 (Ego → Subconscious) | 3 | Modulator-only inversion; moderate cost |
| R1 → R3 (Ego → Unconscious) | 4 | Operator-pair swap; structural novelty |
| R1 → R4 (Ego → Superego) | 4 | Full dual inversion; maximal opposition |

Key contributions:
- Control parameters τ (time pressure), σ (stress/invalidation), ξ (exploration)
  drive regime transitions with type-specific thresholds θ*
- R4 is a scope transition (Z_shared-type): all R1-calibrated observables fail there
- The Resonance Mechanism (social decision protocol) is a structured R3 activation
  protocol — it manages group cognition by inducing controlled Unconscious phases
  instead of uncontrolled Superego activations
- Observable sufficiency table: no single observable covers all four regimes; the
  active modulator cluster (O3) has the widest cross-regime validity

---

### Layer 4 — AI Context Navigation Simulation
**File:** `kht_architecture_layer4.md`

The computational downstream application of Layers 1–3. A Layer 4 simulation consists
of three components:

1. **Context Parser**: estimates (τ, σ, ξ) from input signals
2. **Regime Engine**: maintains current regime state and applies transition logic
3. **Response Generator**: produces outputs consistent with the active (O, M) configuration

Key contributions:
- Design constraints C1–C8 derived from lower layers (must not be violated without
  revising lower-layer theory)
- Fidelity limits: the simulation is a behavioral proxy, not a KHT-typed agent; it
  cannot reproduce biological Layer 2 emergence or genuine R4 destabilization
- Layer 4 as synthetic data generator: produces output in the ARW observable vocabulary,
  making it directly testable against empirical data
- Multi-agent extension: faction formation and Resonance Mechanism protocol implementable
  as coupled LLM instances

---

## Source Reconciliation

The KHT unified architecture integrates two source documents:

| Source | Scope in unified architecture |
|---|---|
| KHT Breakdown & Social Dynamics Appendix | Primary description of Layers 2–3 and social dynamics; the function hierarchy and regime transitions are its core content |
| KHT Gesamtausgabe (Operator/Modulator formalization) | Provides Layer 1 (the fine-grained primitive space); refines Layer 2 by replacing the function-stack model with the block architecture |

The Gesamtausgabe does not supersede the Appendix — it microfounds it. The Appendix
describes the coarser Layer 2–3 phenomena correctly at their own scale; the Gesamtausgabe
provides the finer Layer 1 mechanism from which those phenomena emerge.

---

## Relationship to ARW Analysis

The ARW analysis of KHT is documented in `kht_arw_analysis.md`. That document was
written against the Appendix source only and has been revised to incorporate the
four-layer architecture. Key updates:

- BC class assignments are now grounded in the Layer 1 architecture
- Regime transitions are characterized by Layer 1 distances
- The observable sufficiency analysis incorporates Layer 3's cross-regime table
- The scope tuple S_KHT_L3 extends the earlier S_KHT_meso

---

## Open Questions: Cross-Layer

The following questions span multiple layers and cannot be resolved within a single
layer document.

| ID | Question | Layers involved | Priority |
|---|---|---|---|
| Q-CL-1 | Is there a feedback from Layer 3 to Layer 2? Can chronic R4 activation produce lasting changes in the Layer 2 activation weighting (Hebbian drift)? | L2, L3 | medium |
| Q-CL-2 | The distance metric (Layer 1) should predict transition cost (Layer 3). Is this relationship empirically testable? What proxy for "transition cost" is measurable? | L1, L3 | high |
| Q-CL-3 | The coverage criterion (Layer 2) is a modeling decision. Can it be derived from a more fundamental Layer 1 principle, or does it require independent justification? | L1, L2 | medium |
| Q-CL-4 | Layer 4 simulations generate synthetic observable data. At what level of simulation fidelity does the synthetic data become a useful approximation to empirical human data? | L3, L4 | high |
| Q-CL-5 | The SD/UD developmental subtype (Layer 2) should produce measurable differences in Layer 3 regime dynamics (different θ* values for R2 vs R3 transitions). Can this be used as an empirical test of the subtype distinction? | L2, L3 | medium |
