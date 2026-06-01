---
status: hypothesis
layer: docs/bc_taxonomy/
last_updated: 2026-05-30
depends_on:
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/bc_taxonomy/bc_relational_structure.md
  - docs/core/cover_stability_criterion.md
  - docs/advanced/observable_decomposition.md
  - docs/notes/bc_bedrock_working_definition.md
---

# BC Failure Signatures

*Working basis for Part V of the ARW monograph (BC failure modes).*
*See `bc_relational_structure.md` for the structural derivation of the
two-directional failure structure from the relational taxonomy.*

---

## Purpose

Each BC class produces characteristic observable behaviour when active,
and a characteristic failure pattern when it is violated, exhausted, or
mismatched. These patterns — **failure signatures** — are distinct across
classes and across failure directions, and are the primary means by which
the operative BC can be identified from a failing description.

Each class can fail in **two structurally opposite directions**, producing
different failure signatures and different successor scopes. The two
directions follow from the relational structure of each class
(see `bc_relational_structure.md`).

---

## Formal Failure Mode Taxonomy

| Code | Name | Mechanism |
|---|---|---|
| **F0** | Substrate failure | Observable loses its referent — distinguishability fails at the substrate level. ε-independent. |
| **F1** | Observable insufficiency | ε ≥ ε*(O,X): cover trivial, no stable distinctions at this resolution. |
| **F-gradient** | Descriptive crossover | σ_Δ(x) ≥ ε within R(π): observable valid but geometry too steep for stable zone assignment. |
| **Z_shared** | Genuine transition zone | Zone membership structurally undecidable at the boundary between regimes. |

---

## Failure Signatures by BC Class

---

### 1. Coupling

**Relational domain:** Component × Component
**What it organizes:** Distinguishability between contemporaneous components

**Normal operation:**
Coherent collective mode tracked by the observable. Zone structure stable.
The description reliably assigns the system to coherent or incoherent zones.

---

**Direction 1 — Dissolution (coupling weakens below threshold)**

The collective mode breaks. The observable's coherent signal loses zone
structure: variance increases, the apparent regime boundary becomes noise.
The pre-break approach is observable: as the coupling parameter nears the
threshold, σ_Δ(x) grows near the instability band (the description becomes
increasingly sensitive before the mode breaks). The break itself is
discontinuous — the collective mode does not weaken gradually through the
threshold but ceases to be supportable.

*Onset:* Discontinuous break after a gradual approach phase of increasing
descriptive sensitivity.

*Primary failure modes:* Z_shared at the coupling threshold (zone
membership undecidable in the instability band); F-gradient in the
approach region.

*Key indicators:*
- σ_Δ increases sharply near the regime boundary before collapse
- Recovery time after perturbation lengthens during approach
- Observable variance increases discontinuously at the break

---

**Direction 2 — Freezing (coupling strengthens past admissible range)**

Rigid over-coupling progressively eliminates individual degrees of freedom.
Collective responses that were produced by mutual influence now simply
reflect a fixed joint configuration. The observable's partition collapses
toward triviality: fewer and fewer distinctions remain visible, as
individual variation is suppressed by the over-coupling. The system is
locked.

*Onset:* Gradual and monotonic — the partition collapses progressively
as coupling strengthens. No discontinuous break.

*Primary failure modes:* F1 as the partition becomes trivial (ε*(O,X)
shrinks as all variation is suppressed).

*Key indicators:*
- Output diversity decreases monotonically
- The observable shows progressively fewer distinguishable zones
- Cross-component variation approaches zero

---

### 2. Restriction

**Relational domain:** Admissibility of all other relation types (meta-relation)
**What it organizes:** The boundaries within which any relation can produce stable distinctions

*Note: Restriction has a different status from the other five classes —
it is the admissibility condition for each of the other relation types,
not a relation of the same kind. See `bc_relational_structure.md` §3.*

**Normal operation:**
Zone structure is stratified by the resource, energy, or admissibility
dimension. Below the restriction boundary, one set of regimes; at higher
levels, another. The observable operates within its valid subspace.

---

**Direction 1 — Restriction lifts (projection space expands)**

The admissible state space expands discontinuously. Solutions appear outside
the subspace the observable was designed for. The observable — calibrated for
the restricted subspace — now encounters states outside its design domain. The
observable's referent changes or disappears (the angular frequency ω = 0 at
the separatrix, then restarts as a rotation frequency in the new region).

*Onset:* Sudden — restriction boundaries are structural discontinuities.

*Primary failure modes:* F0 at the subspace boundary (observable loses
referent in the new region); Z_shared at the separatrix itself.

*Key indicators:*
- Observable discontinuity (null point, jump, step) at the boundary
- Cover-stability instability band aligns with the analytic boundary
- Observable values appear that were previously unreachable

---

**Direction 2 — Restriction tightens (projection space contracts)**

The accessible state space contracts. Regimes that required higher resource
levels become inaccessible. The observable remains valid within the reduced
subspace but finds a coarser partition — fewer zones, fewer distinctions.
The description is impoverished but not invalid.

*Onset:* Sudden — the restriction change happens at a specific parameter
value. Recovery does not happen gradually; the system adapts to the new boundary.

*Primary failure modes:* Not F0 (observable remains valid). Abrupt
impoverishment of regime structure without invalidating the observable.

*Key indicators:*
- Sudden disappearance of previously stable zones
- Partition collapses from fine to coarse at the boundary
- Observable continues to report values but covers a smaller range

---

### 3. Dissipation

**Relational domain:** State × State_ordered (ordered-continuation relation)
**What it organizes:** Distinguishability over ordered continuation

*ARW-native formulation:* An attractor is a region where distinguishability
is sustained along the ordering. A repulsor is a region where distinguishability
cannot be maintained along the ordering. Dissipation failure is failure of
the ordered preservation of distinctions.

*Primitive distinction from Coupling:* Coupling is an unordered relation
(R_C ⊆ X × X, no ordering required). Dissipation is an ordered relation
(R_D ⊆ X × X_≤ where ≤ is an ordering on X). Time is the most common
ordering, but any ordered structure qualifies: developmental stages,
learning sequences, organisational histories, evolutionary lineages.
Attractors, repulsors, hysteresis, and path-dependence are secondary
phenomena arising from the ordering — not the primitive definition.
The ordering is also why Dissipation has a natural epistemic parameter τ
(ordering scale) while Coupling has none.*

**Normal operation:**
Attractor-based stability. The description becomes more stable over time,
not less. Zone boundaries are robust. Recovery from perturbations is smooth
and fast.

---

**Direction 1 — Dissipation weakens (temporal distinguishability erodes)**

Attractor basins flatten. The temporal preservation of distinctions weakens:
states that were previously held in distinguishable regions by the dissipative
force can now drift across what were zone boundaries. The description remains
locally valid but becomes fragile: recovery time lengthens, zone boundaries
blur, the same observable that was stable in the morning is unstable later.
In the limit, the system approaches conservative dynamics — no attractor
confinement, free exploration, and indistinguishability between formerly
well-separated zones.

*Onset:* Gradual, monotonic. Zone boundaries blur progressively.

*Primary failure modes:* F-gradient as primary signal (σ_Δ > ε as basins
flatten, observable increasingly sensitive); F0 at the limit when the
attractor disappears entirely.

*Key indicators:*
- Recovery time after perturbation increases continuously
- Zone boundaries become progressively less sharp at constant ε
- Hysteresis narrows: transition costs between zones decrease

---

**Direction 2 — Dissipation deepens (temporal distinguishability discretises)**

Attractor basins deepen. Temporal confinement strengthens: trajectories
converge more rapidly to fewer, more stable attractors. The observable
finds sharper, more discrete zone structure. Transitions between zones
become increasingly rare, requiring exceptional inputs. The partition
collapses toward fewer, deeper zones — ultimately toward a single deep
attractor with near-zero transition probability.

*Onset:* Gradual, monotonic. Zone boundaries sharpen and collapse progressively.

*Primary failure modes:* The inverse of F-gradient — the observable becomes
insensitive (σ_Δ → 0), eventually reporting a single stable state regardless
of context. Partition collapses toward trivial from above (not below).

*Key indicators:*
- Output diversity decreases monotonically over time
- Transition frequency between zones approaches zero
- Zone boundaries become sharper but fewer

**Discriminant between directions:** Direction of zone-sharpness change.
Blurring → weakening dissipation. Sharpening and collapsing → deepening.

---

### 4. Forcing

**Relational domain:** Regime × Regime (inter-regime coupling, directional)
**What it organizes:** Distinguishability between regime organizations

*Key structural distinction from Coupling:* Forcing is directional — one
regime organizes another. This asymmetry is not present in Coupling (symmetric
component relations). See `bc_relational_structure.md` §2.3.*

**Normal operation:**
One regime (organizer, Regime A) imposes structure on another (organized,
Regime B) through a directional inter-regime relation. The organized regime
produces coherent structure partly from its own dynamics, partly from the
structure Regime A provides. Observable reflects both the organized regime's
internal structure and the organizing relation.

---

**Direction 1 — Regime decoupling (organizer loses reach)**

The inter-regime relation weakens. Regime A no longer constrains what
Regime B can distinguish. Regime B no longer receives organizing structure
from A. The observable shows irregular switching: neither the inter-regime
description (organized by A) nor the autonomous description (B alone) holds
stably. The description is in an underdetermined intermediate zone.

*Onset:* Can be sudden (organizing regime disappears abruptly) or gradual
(coupling weakens progressively). No pre-break approach phase in the
*organized* system — distinguishes decoupling from coupling dissolution.

*Primary failure modes:* F-gradient where the two regime structures are
most sensitive to each other; Z_shared where their boundaries directly conflict.

*Key indicators:*
- Observable correlation with organizing regime's structure drops
- Irregular alternation between forced-response and autonomous patterns
- No detectable pre-break approach phase in the organized system's observables

---

**Direction 2 — Regime absorption (organized loses autonomy)**

The inter-regime relation overwhelms. Regime A's organizational structure
completely determines what Regime B can distinguish. Regime B's autonomous
structure is progressively replaced by A's. What required two descriptions
(organizer + organized) collapses to one (only A's structure). The organized
regime loses its structural identity.

*Onset:* Gradual and monotonic. The organized regime's autonomous structure
is progressively suppressed.

*Primary failure modes:* F1 as the partition produced by B's autonomous
structure collapses — the distinctions B previously made are no longer
admissible within A's organizational scope.

*Key indicators:*
- Output diversity of the organized regime decreases toward what A can accommodate
- Cross-validation against A's regime structure shows increasing overlap
- Collapse is asymmetric: A's structure survives, B's does not

**Discriminant from Coupling freezing:** Absorption is asymmetric — the
organizer's structure survives, not a jointly produced frozen state. Observable
cross-validation against the organizer reveals this asymmetry.

---

### 5. Symmetry Breaking

**Relational domain:** State × State (previously equivalent states)
**What it organizes:** Distinguishability between formerly equivalent states

**Normal operation:**
The system occupies one branch of the broken symmetry. The selected state
is stable, with characteristic asymmetry in transition costs (hysteresis).
Reaching the alternative branch requires substantially more than the reverse.

---

**Direction 1 — Forward break (symmetry breaks)**

Approaching the bifurcation from the symmetric side: fluctuations around
the symmetric state increase, recovery time lengthens, spontaneous
excursions toward one branch become more frequent. This is the characteristic
pre-breaking signature — asymmetric and directional fluctuations, not uniform
fragility. At the bifurcation, Z_shared: both branches reachable, zone
membership undecidable. After the break: topology change, hysteresis created,
the selected branch holds against small perturbations.

*Onset:* Gradual approach (increasing asymmetric fluctuations) followed by
discontinuous break.

*Primary failure modes:* Z_shared at the bifurcation; F0 if the degenerate
symmetric state is approached from the broken side and the selected attractor
disappears.

*Key indicators:*
- Asymmetric (not uniform) fluctuations increasing before the break
- Recovery time lengthens asymmetrically toward one branch
- Discontinuous topology change: hysteresis appears where none existed

**Discriminant from dissipation exhaustion:** Dissipation exhaustion produces
uniform fragility. Symmetry-breaking approach produces asymmetric, directional
fluctuations leaning toward one branch.

---

**Direction 2 — Restoration approach (broken state becomes unstable)**

From the broken state: fluctuations around the selected branch increase,
the alternative branch becomes more reachable, hysteresis narrows. If the
broken state has generated secondary structures (institutional dependencies,
habit formation, complementary products), restoration may redirect toward
a second-order break rather than symmetry recovery.

At a restoration bifurcation: F0 — the selected attractor ceases to exist.
This is distinguishable from the original Z_shared because the observable
shows collapse of the previously stable branch (not emergence of asymmetry
from a symmetric background).

*Onset:* Gradual approach (hysteresis narrowing) followed by discontinuous
transition.

*Primary failure modes:* F0 at the restoration bifurcation (selected state
ceases to exist); Z_shared if the system is in the symmetric zone between
the broken and restored states.

*Key indicators:*
- Hysteresis width narrows (diagnostic quantity)
- Increasing excursions toward the alternative branch
- Collapse of the previously stable branch rather than emergence of new symmetry

---

### 6. Aggregation

**Relational domain:** Description_level × Description_level
**What it organizes:** Distinguishability between description resolutions

*Unique property: Aggregation failure is the only failure mode invisible
in the observable itself. The aggregate's σ_Δ stays small even as the
description loses coherence, because the averaging operation suppresses
precisely the variation that is failing.*

**Normal operation:**
The aggregate observable reports stable regime boundaries. Different sub-
populations or time windows give consistent threshold locations. The
aggregate's grain coherently represents the population it averages over.

---

**Direction 1 — N* failure (heterogeneity exceeds grain)**

Population heterogeneity grows past the critical aggregation grain N*.
The aggregate is now the mean of two or more incompatible sub-populations.
σ_Δ of the aggregate stays small (camouflage) while σ²_between grows.
The aggregate produces a stable number that no longer has a coherent referent.

*Onset:* Gradual, monotonic (slowly increasing heterogeneity). **No onset
signal in the aggregate itself** — the observable appears stable throughout.

*Primary failure modes:* F0 below N* (substrate A2/A3 fail: stationary
measure no longer unique over the aggregated population). ε-independent —
refining resolution cannot recover an aggregate of incompatible populations.

*Key indicators:*
- Aggregate remains flat while sub-group pictures diverge (disaggregation test)
- Confidence intervals on threshold location widen (if sampled)
- Cross-validation across sub-groups fails

---

**Direction 2 — Over-coarseness failure (grain too coarse for the structure)**

The aggregation grain is too large to resolve structure that exists at a
finer scale. The aggregate smooths over distinctions that the question
requires to be visible. All states appear equivalent — not because the
population is incoherent, but because the description level is above the
relevant structure.

*Onset:* Not an onset process — the grain was always too coarse, or the
structure at the finer level only became relevant with a new question.

*Primary failure modes:* F1 — the partition collapses toward triviality
from above. The grain, not the heterogeneity, is the problem.

*Key indicators:*
- Disaggregation reveals regime structure the aggregate cannot see
- The aggregate reports a single stable zone where sub-group analysis finds multiple
- No onset trajectory: the failure is structural from the start

**Discriminant between directions:** N* failure — structure was visible,
then hidden as heterogeneity grew. Over-coarseness — structure was never
visible at this grain, revealed only by disaggregation.

---

## Multi-BC Failure Interaction

When multiple BC classes are simultaneously active, their failure signatures
can compound and mask each other.

### Masking patterns

| Observed signature | Apparent diagnosis | Actual mechanism | Discriminant |
|---|---|---|---|
| Sudden collective mode dissolution | Coupling dissolution | Dissipation exhaustion lowered the effective coupling threshold | Onset: no pre-break sensitivity increase (dissipation); pre-break sensitivity increase present (coupling) |
| Sudden loss of collective structure | Coupling dissolution | Regime decoupling (forcing) — organizing regime lost reach | No pre-break phase in organized system's observables |
| Structure collapses to single regime | Coupling freezing | Regime absorption — organized regime subsumed by organizer | Asymmetry: one structure survives (absorption), joint frozen state (freezing) |
| New structure appears suddenly | Symmetry breaking | Restriction lifting — system entered previously inadmissible region | Hysteresis absent (restriction); hysteresis created (symmetry breaking) |
| Gradual, monotonic degradation | Dissipation exhaustion | Aggregation N* failure | Disaggregation test: uniform shallow basins (dissipation) vs. divergent sub-groups with flat aggregate (aggregation) |

### Detection principle (two-directional update)

The onset trajectory is the first discriminant, but must account for
two directions per class:

| Onset | Zone-sharpness direction | Candidate class/direction |
|---|---|---|
| Sudden discontinuity | Any | Coupling dissolution, Restriction lifting/contracting, Symmetry breaking (at bifurcation), Forcing decoupling (sudden) |
| Gradual monotonic, blurring | Zones becoming softer | Dissipation weakening, Coupling dissolution (approach phase) |
| Gradual monotonic, sharpening | Zones becoming harder and fewer | Dissipation deepening, Coupling freezing, Forcing absorption |
| Irregular, non-monotonic | Variable | Forcing mismatch/decoupling (gradual), multi-BC interaction |
| No observable onset | Aggregate stable throughout | Aggregation N* failure (disaggregation required); Aggregation over-coarseness (structural from start) |

Additional discriminant — fluctuation asymmetry:
- Asymmetric, directional fluctuations → Symmetry breaking approach
- Uniform fragility → Dissipation exhaustion

### The effective scope principle

The effective scope of a multi-BC description is the intersection of
the admissible regions of all active BCs. If one BC is failing, the
effective scope is shrinking even if the others remain satisfied.

Importantly (from `bc_relational_structure.md`): Restriction is embedded
in every other relation as its admissibility condition. When a Restriction
embedded in Coupling, Forcing, or any other class fails, the outer class
appears to fail — the actual mechanism is the meta-relational Restriction
condition being violated.

---

## Scope Transitions After BC Failure

Each failure direction produces a characteristic successor scope:

| BC class | Failure direction | Successor scope |
|---|---|---|
| Coupling | Dissolution | Individual-level scope (components independent) |
| Coupling | Freezing | Single-regime scope (locked collective state) |
| Restriction | Lifting | Expanded scope requiring new observable for new region |
| Restriction | Contracting | Reduced subspace scope (impoverished but valid) |
| Dissipation | Weakening | Conservative-like scope (no attractor confinement) |
| Dissipation | Deepening | Single deep-attractor scope (maximally stable, minimal structure) |
| Forcing | Decoupling | Autonomous scope of organized regime (transition zone before stabilisation) |
| Forcing | Absorption | Organizer's scope (asymmetric: only A's structure remains) |
| Symmetry Breaking | Forward break | Asymmetric scope (new topology, hysteresis present) |
| Symmetry Breaking | Restoration | Symmetric scope or second-order broken scope |
| Aggregation | N* failure | Stratified sub-group scopes (requires disaggregation) |
| Aggregation | Over-coarseness | Finer-grain scope (requires different observable) |

---

## Open Questions

1. **Coupling-Dissipation duality (Q-REL-01 in `bc_relational_structure.md`):**
   Are Coupling and Dissipation instances of the same relation type (self-relation)
   over different domains (spatial/temporal), or genuinely distinct? If the former,
   their failure signatures should be derivable from a single formal structure with
   domain as parameter.

2. **Restriction as meta-relation in failure analysis:**
   When Restriction fails, it changes the admissibility domain of all embedded
   Restrictions in the other five classes. Can failures be systematically attributed
   to the meta-relational level vs. the relation level?

3. **F-gradient as early warning:**
   Is F-gradient always a leading indicator of approaching F0? Or can F0 appear
   without prior F-gradient? The dissipation deepening direction (σ_Δ → 0) suggests
   F0 can appear without F-gradient from above.

4. **Aggregation onset invisibility:**
   The aggregate's σ_Δ stays small during N* failure (camouflage). Does this mean
   cover-stability analysis of the aggregate is structurally incapable of detecting
   aggregation failure? Is disaggregation the only path, or can cover-stability be
   extended to detect σ²_between?

5. **Onset speed ordering:**
   Hypothesis (from `bc_failure_signatures.md` v1): Restriction > Symmetry Breaking
   > Coupling > Forcing > Dissipation > Aggregation (fastest to slowest onset).
   Does the two-directional analysis change this ordering? (E.g., coupling freezing
   and dissipation deepening are both gradual; coupling dissolution and symmetry
   breaking forward break are both discontinuous.)

---

*Updated: 2026-05-30. Added two-directional failure analysis for all six classes,
Forcing reformulation as inter-regime coupling, Dissipation reformulation as temporal
distinguishability, masking table extended, scope transition table added.
Status promoted from `note` to `hypothesis` — relational structure provides
sufficient falsifiability conditions.*

*Promote to `working-definition` when at least two case studies demonstrate the
distinguishability of failure directions within the same BC class.*
