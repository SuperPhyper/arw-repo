---
status: working-definition
layer: docs/art_instantiations/
title: "KHT Unified Architecture — Layer 3: Dynamic Regime Transitions"
sources:
  - KHT Breakdown & Social Dynamics Appendix (Felder, R. — unpublished)
  - KHT Gesamtausgabe — Operator/Modulator Formalization (Felder, R. — unpublished)
  - kht_architecture_layer1.md
  - kht_architecture_layer2.md
created: 2026-05-14
part_of: kht_unified_architecture (Layer 3 of 4)
previous: kht_architecture_layer2.md
next: kht_architecture_layer4.md  # AI context navigation simulation
related:
  - kht_arw_analysis.md
---

# KHT Unified Architecture — Layer 3: Dynamic Regime Transitions

## 1. What Layer 3 Adds

Layer 2 produced a **persistent profile** P = (Ego-block, Shadow-block) — a stable
attractor basin within the Layer 1 O×M space, fixed by biological boundary conditions.
Under ideal conditions, a person operates within their Ego-block indefinitely.

Empirically, this is not what happens. The same individual exhibits qualitatively
different cognitive modes depending on context: under time pressure they respond
differently than under exploration conditions; under sustained invalidation they
behave in ways that contradict their ordinary profile. The cognitive system is not
static — it transitions between distinct operational regimes.

Layer 3 describes:

1. What a cognitive regime is, formally
2. What the four regimes are and how they relate to the Layer 2 profile structure
3. What drives transitions between regimes (control parameters)
4. What changes at each transition, in terms of Layer 1 distance
5. How the individual-level regime dynamics scale to the social level
6. The ARW scope structure implied by Layer 3

---

## 2. Cognitive Regimes: Formal Definition

### 2.1 Definition

A **cognitive regime** R_i is a stable operational mode of the cognitive system,
characterized by:

- A **dominant block**: which (O, M) combinations are the primary processing center
- An **activation topology**: the relative weighting of all O×M cells within the
  active block
- A **transition condition**: the contextual parameter configuration that triggers
  entry into this regime

Two states x₁, x₂ ∈ X are in the **same regime** if their dominant blocks are
identical and their activation topologies are qualitatively similar. A **regime
transition** is a discontinuous shift in the dominant block.

### 2.2 The Four Regimes

KHT defines four regimes corresponding to the four sides of the mind. Each regime
is identified by which block structure is dominant, and what its relationship is to
the Layer 2 profile.

| Regime | KHT label | Dominant structure | Relationship to Layer 2 profile |
|---|---|---|---|
| **R1** | Ego | Ego-block (O₁, O₁*) × (M, M*) | Primary attractor; default operating mode |
| **R2** | Subconscious | Ego-block with inverted modulator-pair: (O₁, O₁*) × (M*, M) | Modulator-inverted Ego; same operators, swapped evaluation/orientation |
| **R3** | Unconscious | Shadow-block (O₂, O₂*) × (M', M'*) | Orthogonal operator pair; genuine structural novelty |
| **R4** | Superego | Full dual of Ego-block: (O₁*, O₁) × (M*, M) | Maximal distance from R1; all dimensions inverted |

### 2.3 Regime Distance from R1

Using the Layer 1 distance metric d((O₁,M₁),(O₂,M₂)) = d_op + d_Hamming(M):

| Transition | d_op | d_mod | Total d | Character |
|---|---|---|---|---|
| R1 → R2 | 0 | 3 | 3 | Modulator-only inversion; operators unchanged |
| R1 → R3 | 1 | 3 | 4 | Operator-pair swap + modulator shift |
| R1 → R4 | 1 | 3 | 4 | Full dual inversion; maximal structural opposition |

**Note on R3 vs R4 distance:** Both transitions have total distance 4 from R1.
They are maximally distant from R1 but differ in *kind*: R3 swaps the operator pair
(structural novelty in what is processed) while maintaining a coherent modulator
profile; R4 inverts everything simultaneously (processed content and evaluative
logic both invert). The qualitative difference between R3 (generative, exploratory)
and R4 (radical, overcorrective) is thus not a distance difference but a
**structural character difference** — R3 is an operator transition, R4 is a
full-dual inversion.

---

## 3. Control Parameters and Transition Conditions

### 3.1 The Three Primary Control Parameters

Layer 3 dynamics are driven by three contextual control parameters:

| Parameter | Symbol | Description | Transition triggered |
|---|---|---|---|
| Temporal pressure | τ | Subjective scarcity of time for cognitive processing | R1 → R2 (high τ) |
| Stress / invalidation | σ | Sustained external challenge to profile coherence; hostile invalidation | R1 → R4 (high σ) |
| Exploration opportunity | ξ | Available time and reduced cognitive cost for novel processing | R1 → R3 (high ξ) |

These parameters are **continuous** in reality but act as **threshold triggers**:
regime transitions occur when a parameter crosses a critical value θ*(τ), θ*(σ),
or θ*(ξ). The threshold values are not universal — they vary across individuals
depending on the Layer 2 activation weighting (more strongly consolidated profiles
have higher thresholds; SD vs UD developmental subtype shifts the relative
thresholds for R2 vs R3).

### 3.2 Transition Mechanisms

**R1 → R2 (Ego → Subconscious): Modulator inversion under time pressure**

When τ exceeds θ*(τ), the Ego-block's modulator-pair inverts: M → M*, M* → M.
Operators do not change. The system continues processing with the same operator
pair (O₁, O₁*) but under inverted evaluation and orientation logic.

KHT describes this as "perspective novelty rather than structural novelty" — the
system sees the same information through the opposite evaluative lens. The cost
is moderate because operator infrastructure remains intact; only the modulator
routing changes.

This is consistent with the Layer 1 distance: d(R1, R2) = 3 (modulator Hamming
distance only) — a significant but recoverable reconfiguration.

Teaching and learning contexts naturally trigger R2: explaining a concept requires
the speaker to model the listener's perspective, which activates the modulator
complement within the same operator infrastructure.

**R1 → R3 (Ego → Unconscious): Operator-pair swap under exploration**

When ξ exceeds θ*(ξ), the Shadow-block (O₂, O₂*) × (M', M'*) becomes dominant.
The system shifts from its primary operator pair to the orthogonal pair.

KHT describes this as "reconstruction" rather than reflection — the system accesses
genuinely different processing mechanisms, not merely different evaluation of the same
inputs. This produces creative novelty: new patterns, novel associations, unexpected
reframings.

The cost is higher than R2: the operator infrastructure changes, requiring different
neural pathways. This explains why R3 requires either abundant time or neurochemical
conditions (stress-hormone reduction) that lower the effective switching cost.

**R1 → R4 (Ego → Superego): Full-dual inversion under sustained invalidation**

When σ exceeds θ*(σ), the system undergoes simultaneous inversion of both the
operator pair and the full modulator cluster. The Superego regime is the complete
structural dual of the Ego — what was evaluated as coherent is now evaluated as
incoherent, what was internally stabilized is now externally oriented, what was
closed is now open (or vice versa, depending on the J/P orientation).

KHT describes Superego activation as "radical or overcorrective" with the goal of
"re-equilibration" — not coping but systemic override. The full-dual structure
explains why: the system is not adjusting its operating mode but reversing it
entirely. Every dimension simultaneously inverts.

The consequence for observables is critical: all observables calibrated to R1
behavior are outside R(π) in R4. The attractor is structurally opposite, not merely
shifted. This is a **scope transition** in ARW terms, not a regime boundary within
a valid scope.

### 3.3 Parameter Interactions

The three control parameters are not fully independent:

- High σ can suppress ξ: sustained stress prevents exploration
- High ξ can buffer τ: abundant time reduces temporal pressure
- Chronic high σ can shift θ*(σ) downward over time (sensitization): the R4
  threshold lowers with repeated activation, making Superego transitions more
  likely under lower stress levels

These interactions mean the control parameter space is not simply ℝ³ with
independent axes — it has a coupled structure. For ARW scope purposes, the
B-constraint should specify which region of (τ, σ, ξ) space the scope operates
in, since the observable R(π) depends on parameter location.

---

## 4. Regime Dynamics: Temporal Structure

### 4.1 Transition Reversibility

Regime transitions differ in their reversibility profile:

| Transition | Reversibility | Recovery mechanism |
|---|---|---|
| R1 → R2 | High | Parameter τ decreases; modulator re-inverts to R1 |
| R1 → R3 | High | Parameter ξ decreases; Shadow-block activity decays; R1 re-establishes |
| R1 → R4 | Low (acute) | Parameter σ must decrease substantially; recovery is gradual |
| Chronic R4 | Very low | Extended R4 activation can produce Hebbian reinforcement of R4 cells — partial profile drift |

The asymmetry between R2/R3 (easily reversible) and R4 (difficult to reverse) is
a structural prediction of the architecture: R2 and R3 transitions change the
dominant block but preserve the Layer 2 profile's attractor basin; R4 transitions
push the system to its structural maximum distance, where the restoring force
toward R1 is weakest.

### 4.2 Dwell Time and Attractor Depth

Within each regime, the system exhibits a characteristic **dwell time** — how long
it remains in the regime before returning toward R1. Dwell time is determined by:

- The strength of the triggering parameter (τ, σ, ξ)
- The depth of the Layer 2 attractor (how strongly Dissipation consolidated the
  Ego-block): deeper attractors mean shorter dwell times in non-R1 regimes
- The SD/UD developmental subtype: SD individuals have shallower R3 access
  (longer R2 dwell) and UD individuals have shallower R2 access (longer R3 dwell)

### 4.3 The Hierarchical Feedback Cycle

The KHT Appendix identifies a characteristic feedback pattern: Je → Pi → Pe → Ji.
This describes the natural oscillation of cognitive attention across the four
regime-adjacent blocks during normal adaptive cognition (not full regime transitions,
but within-R1 micro-oscillation).

From the Layer 3 perspective, this cycle is an **intra-R1 attentional orbit** — the
Ego-block does not operate as a static configuration but rotates attention across
its four cells in a characteristic sequence driven by the interplay of
operator-family alternation and modulator-state cycling. The cycle maintains
within-R1 stability while allowing adaptive response to varying inputs.

This micro-oscillation is distinct from full regime transitions: it does not cross
block boundaries but moves within the Ego-block's activation topology.

---

## 5. Social-Level Regime Dynamics

### 5.1 From Individual to Group

At the social level, multiple individuals with different Layer 2 profiles interact.
Each individual's active regime (R1–R4) and dominant O×M configuration constitutes
their **cognitive contribution** to the group field.

KHT's social dynamics model treats groups as **distributed cognitive systems** in
which individual regime states collectively instantiate a group-level cognitive
topology. The key insight is that inter-individual coupling (Coupling BC class,
§5.1 of `kht_arw_analysis.md`) acts on the individuals' active modulator clusters:
individuals with overlapping active clusters resonate; those with dual clusters
experience maximal tension.

### 5.2 Group Regime: Factions as Collective Attractors

A **faction** is a stable group-level attractor in which a subset of individuals
with compatible active O×M configurations mutually reinforce each other's regime
states. The faction's collective "type" is the shared dominant O×M configuration
of its members.

The eight faction archetypes (SJ×FJ, SJ×TJ, SP×FP, SP×TP, NJ×FJ, NJ×TJ, NP×FP,
NP×TP) from the KHT Appendix are, in Layer 3 terms, the stable collective
attractor configurations that emerge when individual Layer 2 profiles with
compatible modulator clusters couple above a threshold group-coupling strength κ.

This is the Kuramoto analogy from `kht_arw_analysis.md` made precise: individual
active modulator clusters are the oscillator phases; κ is the inter-individual
coupling strength; faction formation is the synchronization transition at κ > κ_c.

### 5.3 Group-Level Regime Transitions

Group-level regime transitions are more complex than individual ones because they
involve:

1. **Coupling-driven synchronization**: below κ_c, individuals operate in their own
   regimes independently; above κ_c, coupling forces alignment toward a collective
   regime
2. **Diversity-stability tradeoff**: homogeneous groups (all members in compatible
   R1 configurations) have high κ and strong faction coherence but are vulnerable
   to collective R4 (groupthink under invalidation); heterogeneous groups have lower
   κ but more robust collective cognition
3. **Resonance Mechanism**: the KHT procedural framework for group decision-making
   is a structured intervention that manages group-level regime transitions — it
   prevents premature faction lock-in (collective R1 crystallization) and avoids
   group-level R4 by surfacing tensions as subgroup R3 processes

### 5.4 The Resonance Mechanism as Layer 3 Protocol

The Resonance Mechanism (KHT §Social Dynamics) maps directly onto the Layer 3
regime transition structure:

| Resonance Mechanism step | Layer 3 equivalent |
|---|---|
| Collection of individual Wants / Don'ts | Identification of active O×M configurations per participant |
| Identification of conflict fronts | Detection of dual-cluster pairs (maximal distance d = 4) in the group |
| Formation of temporary subgroups | Controlled R3 activation: subgroup enters exploratory Shadow-block mode to process the tension |
| Resolution within subgroup | R3 → R1 recovery within a shared context; new Ego-block activation weighting |
| Feedback to plenary | Propagation of revised O×M configuration back to the group field |
| Activation of new fronts | Second-order tensions surface as the first-order coupling structure changes |

The Resonance Mechanism is therefore not merely a social protocol — it is a
**structured Layer 3 dynamics management tool**: it deliberately cycles the group
through controlled R3 activations (rather than allowing uncontrolled R4 activations)
and ensures that every dual-cluster tension is processed before collective closure.

---

## 6. ARW Scope Structure for Layer 3

### 6.1 Regime Boundaries and Scope Transitions

The four regimes define a partition of the operational state space. From the ARW
perspective:

- **R1 ↔ R2**: This is a **regime boundary θ*** within a valid scope. Both R1 and R2
  use the same operator pair; observables that track operator-level behavior (behavioral
  vectors, operator-domain scores) remain valid across this boundary. The modulator
  inversion changes the *style* of output, not the *type* of processing. R(O_behavioral)
  includes both R1 and R2 states, provided ε is large enough to absorb the modulator-
  induced output shift.

- **R1 ↔ R3**: This is a **regime boundary θ*** for operator-sensitive observables but
  a **scope transition** for operator-specific observables. An observable that tracks
  Ni-specific processing (e.g. projection coherence) will have Z(π) at the R1→R3
  boundary when the operator shifts from Ni to Ne.

- **R1 ↔ R4**: This is a **scope transition** (Z_shared-type) for all observables
  calibrated to R1 behavior. The full-dual inversion means the attractor structure
  is opposite; no R1-calibrated observable can reliably describe R4 states.

### 6.2 Preliminary Scope Tuple (Layer 3 Extension)

Extending the scope tuple from `kht_arw_analysis.md`:

```
S_KHT_L3 = (B, Π, Δ, ε)

B:  B_Layer2 (adaptation phase, stable profile identity)
    AND: τ < θ*(τ) [no active R2 transition] OR scope explicitly covers R1+R2
    AND: σ < θ*(σ) [R4 excluded — scope transition boundary]
    AND: group composition G stable [no major faction restructuring]

Π:  O1: Behavioral vector scores (continuous; R·A structure)
         Valid in R1 and R2; Z(O1) at R1→R3 if operator-specific
    O2: OCEAN profile (A³·R structure)
         Valid in R1; side-blind (cannot distinguish R1 from R2)
    O3: Active modulator cluster (categorical; R⁴ structure)
         Valid in R1 and R2; F1 risk near cluster boundaries
    O4: Faction type (R²·A_group structure)
         Valid for stable group compositions within R1

Δ:  Day-to-day τ and ξ variation (mild regime perturbations within R1)
    NOT: Sustained σ elevation; major life transitions; R4-triggering events

ε:  Behavioral vector level: sup_x σ_Δ(x) < ε < ε*(O1, X_B)
    Modulator cluster level: ε must span within-cluster variation
    Admissible regime I_ε remains open pending empirical calibration
```

### 6.3 Observable Sufficiency Across Regimes

A key structural insight from Layer 3: **no single observable is sufficient across
all four regimes**. The regime partition creates a fundamental observational
fragmentation:

| Observable | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Behavioral vectors (O1) | ✓ valid | ✓ valid (modulator-shifted) | ~ partially valid | ✗ Z(π) |
| OCEAN profile (O2) | ✓ valid | ✓ (side-blind) | ~ (Shadow-block distortion) | ✗ Z(π) |
| Modulator cluster (O3) | ✓ valid | ✓ (cluster inverted) | ~ (different operator family) | ✓ valid (if R4-calibrated) |
| Operator-domain score | ✓ valid | ✓ valid | ✗ Z(π) (operator changes) | ✗ Z(π) |

This table reveals that O3 (active modulator cluster) has the widest coverage —
it remains valid even in R4 if separately calibrated for that regime. It is the
best candidate for a **cross-regime tracking observable**, though it requires
the highest measurement precision (categorical fine-grained assessment).

---

## 7. Open Questions for Layer 3

| ID | Question | Priority |
|---|---|---|
| Q-L3-1 | What are the quantitative threshold values θ*(τ), θ*(σ), θ*(ξ)? Are they universal or profile-dependent? Experimental design needed. | high |
| Q-L3-2 | Is the R1→R2 transition truly discontinuous (regime boundary) or gradual (descriptive crossover / F-gradient region)? The modulator-only character suggests it could be gradual, which would make it an F-gradient case rather than a clean θ*. | high |
| Q-L3-3 | Does chronic R4 activation produce measurable Hebbian drift in the profile (permanent activation weighting shift)? This would constitute a Layer 2 modification driven by Layer 3 dynamics — a feedback from Layer 3 to Layer 2. | medium |
| Q-L3-4 | The Resonance Mechanism is described as a structured R3 activation protocol. Can it be formalized as a sequence of (τ, σ, ξ) parameter manipulations? | medium |
| Q-L3-5 | At the group level: what is the critical coupling strength κ_c for faction formation? Does it depend on group size, profile diversity, or both? | medium |
| Q-L3-6 | The intra-R1 attentional orbit (Je→Pi→Pe→Ji cycle) is described qualitatively. Can it be modeled as a limit cycle within the Ego-block activation topology? What drives the cycle frequency? | low |
| Q-L3-7 | Is there a meaningful ARW transfer Φ between the individual-level Layer 3 scope and the group-level faction dynamics scope? Both involve regime partitions driven by coupling and forcing. | low |
