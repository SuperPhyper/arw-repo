---
status: hypothesis
layer: docs/art_instantiations/
title: "Conflict Descriptions as Scopes — Asymmetric Warfare as a Forced Scope Change"
last_revised: 2026-08-08
created: 2026-08-08
depends_on:
  - docs/glossary/scope.md
  - docs/core/falsification_schema.md
  - docs/notes/general_regime_construction.md
  - docs/advanced/observable_decomposition.md
related:
  - docs/art_instantiations/art_geopolitical_scope_example.md
  - docs/art_instantiations/arw_for_game_theory.md
  - docs/art_instantiations/kht_group_dynamics.md
---

# Conflict Descriptions as Scopes

## Asymmetric Warfare as a Forced Scope Change

This document is an ART instantiation. It renders four established descriptions of
human conflict as ARW scopes over one shared state space, applies each to the state
region occupied by asymmetric warfare, and reads off the falsification verdicts. The
verdicts are not independent: they share a structure, and that shared structure
determines the scope constructed in §5 — a single tuple admissible on both the
symmetric and the asymmetric conflict region, which reproduces none of the four and
states in §5.6 what it gives up in exchange.

It is not a predictive model of any conflict and makes no claim about any actual
war. The object of study is the **descriptions**, not the wars.

**Level discipline.** Sections 2–5 attribute scopes to *parties*. A scope attributed
to a party is the analyst's declared description of that party's operative constraint
set — a modelling commitment in the sense of `general_regime_construction.md`. It is
not a psychological state, an intention, or a subject. Per the ARW-level rule in
`generator_admissibility_taxonomy.md`, no construction below requires a subject; every
scope component is declared.

---

## 1. The Shared State Space

All four descriptions are rendered over the same X, so that the differences between
them are differences in (B, Π, Δ, ε) and nothing else.

A state x ∈ X of a human conflict system is a snapshot comprising:

- force dispositions and materiel stocks of every organized party
- territorial and infrastructural control
- organizational structure of each party (topology, not size)
- accumulated cost borne by each party (casualties, expenditure, forgone alternatives)
- distribution of recognition/allegiance across the contested population
- attitudinal state of each party's supporting constituency
- information environment (what is reported, by whose categories)
- third-party postures

X is high-dimensional and only partially observable. As always in ARW, this is not an
obstacle: a scope declares which observables are tracked and at what resolution, and
everything else is outside Π by construction.

**Asymmetric warfare as a state region.** Let X_asym ⊆ X be characterised, without yet
prejudging any description, by the simultaneous presence of:

| | Property |
|---|---|
| (a) | large and stable capability disparity between the parties |
| (b) | at least one party's organisation is not decomposable into a distinguished, removable, connectivity-critical node |
| (c) | victory conditions are **non-complementary** — not-losing counts as winning for one party |
| (d) | the parties' relevant time constants differ by an order of magnitude or more |
| (e) | the weaker party's admissible action set includes acts on the stronger party's *description* (its reporting categories, its constituency's cost tolerance), not only on its forces |

X_asym is a region of X, not a separate system. This matters: a scope that is valid on
X but fails on X_asym has failed on a *subset of its own declared domain*.

---

## 2. Four Descriptions as Scopes

**Notation warning.** Each ε below is rendered as a single resolution statement across
a multi-observable Π, because that is how the source description states it. By
`general_regime_construction.md` §2.2 a scalar ε across observables of heterogeneous
units is **ill-formed** without a declared normalisation. This is not an endorsement:
the defect is one of the three findings of §4.3, and it holds independently of anything
about asymmetry. Sections 2.1–2.4 render the descriptions as given; they do not repair
them.

### 2.1 S_CW — Clausewitzian / state-centric

```
S_CW = (B_CW, Π_CW, Δ_CW, ε_CW)
```

**B_CW.** Few collectively organised parties, each with a decision centre capable of
formulating a political purpose. Force is instrumental to that purpose. Each party
possesses an identifiable centre of gravity. A state of defeat exists and is reachable.
The trinity (government / army / people) is separable into three coupled components.

**Π_CW** = { `force_ratio`, `territorial_control`, `casualty_exchange_ratio`,
`center_of_gravity_status`, `political_objective_alignment` }
— primary: `center_of_gravity_status`.

**Δ_CW.** Tactical losses, friction, weather, single-battle reversals, local
withdrawals. The regime distinction must survive all of these.

**ε_CW.** Campaign-scale in time, theatre-scale in space. Individual engagements are
below resolution.

**Induced partition R_CW.** R1 armed peace · R2 limited war (means bounded by purpose)
· R3 absolute war (reciprocal escalation) · R4 decision (a centre of gravity is
destroyed). Control parameter: ratio of political stake to available means.

**BC classes present** (`boundary_condition_classes.md`): Class 1 Restriction
(admissible parties are states), Class 3 Symmetry breaking (attacker/defender),
Class 6 Aggregation (army as a single unit).

### 2.2 S_RC — Rational choice / game-theoretic

```
S_RC = (B_RC, Π_RC, Δ_RC, ε_RC)
```

**B_RC.** Party set fixed and enumerable. Preferences complete, transitive and stable
over the horizon. Game structure common knowledge, or an explicitly declared
information partition. Payoffs commensurable on a single scale. Actions drawn from a
fixed strategy set.

**Π_RC** = { `payoff_vector`, `strategy_profile`, `information_partition`,
`equilibrium_distance` } — primary: `equilibrium_distance`.

**Δ_RC.** Payoff noise, trembling-hand errors, small belief perturbations.

**ε_RC.** Strategy variations that do not change equilibrium selection are
indistinguishable.

**Induced partition R_RC.** R1 unique equilibrium / stable deterrence · R2 multiple
equilibria / coordination failure · R3 non-empty bargaining range (settlement
predicted) · R4 commitment problem (war as equilibrium).

See `arw_for_game_theory.md` for the general vocabulary translation; this section
instantiates it on conflict specifically.

### 2.3 S_GA — Galtungian conflict transformation

```
S_GA = (B_GA, Π_GA, Δ_GA, ε_GA)
```

**B_GA.** Conflict decomposes into contradiction / attitude / behaviour. Structural and
cultural violence exist as persisting configurations rather than events. An underlying
incompatibility exists and is in principle transformable. Horizon is generational.

**Π_GA** = { `structural_violence_index`, `cultural_legitimation`,
`attitude_polarization`, `direct_violence_rate`, `needs_satisfaction` }
— primary: `needs_satisfaction`.

**Δ_GA.** Individual incidents, single acts of direct violence, leadership turnover.

**ε_GA.** Coarse in time (years to decades), fine in social structure. Note this is the
**inverse** of ε_CW: what S_CW resolves, S_GA suppresses, and vice versa.

**Induced partition R_GA.** R1 latent conflict · R2 manifest conflict · R3 direct
violence · R4 negative peace · R5 positive peace.

### 2.4 S_RE — Structural realism / security dilemma

```
S_RE = (B_RE, Π_RE, Δ_RE, ε_RE)
```

**B_RE.** Anarchy — no authority above the units. Units functionally alike,
differentiated only by capability. Survival is the invariant goal. Capability is
aggregable.

**Π_RE** = { `capability_distribution`, `polarity`, `alliance_configuration`,
`offense_defense_balance`, `signal_credibility` } — primary:
`capability_distribution`.

**Δ_RE.** Leadership change, domestic political variation, single crises. This
placement is doctrinal, not incidental: the scope is explicitly anti-reductionist, so
unit-internal politics is declared to be a perturbation the description must absorb.

**ε_RE.** Unit-internal structure entirely below resolution.

**Induced partition R_RE.** R1 bipolar stability · R2 multipolar instability ·
R3 unipolarity · R4 power transition.

---

## 3. Each Scope Applied to X_asym

Verdicts follow the decision order of `docs/core/falsification_schema.md`:
**F0 → F4 → F1 → F3 → F2 → F-gradient**. F4 does not arise (there is no sweep
boundary artifact in a declarative scope), so the live order is F0 → F1 → F3 → F2 →
F-gradient.

### 3.1 S_CW on X_asym — F0, exhausting to F1_BC

Per observable:

| π ∈ Π_CW | On X_asym | Verdict |
|---|---|---|
| `center_of_gravity_status` | Property (b) removes the referent: there is no distinguished removable node whose status the observable reports. The substrate assumption "a connectivity-critical node exists" fails throughout X_asym, not at isolated points. | **F0** — ε-independent |
| `political_objective_alignment` | Requires a unique aggregable political will per party. For a non-centralised party this is the political analogue of a non-unique stationary measure: the aggregate is formally undefined, not merely noisy. | **F0** |
| `territorial_control` | Referent intact. But under (c) the cover fails to refine the claimed regime structure — control changes across states that belong to the same R_CW class, and R_CW classes contain states with opposite control values. | **F1**, claim-relative |
| `casualty_exchange_ratio` | Referent intact, resolves fine. Does not refine the claimed structure: under (c) and (d), favourable exchange ratios are compatible with every regime including R4-for-the-strong-party. | **F1**, claim-relative |
| `force_ratio` | Referent intact. Under (a) it is approximately constant across all of X_asym, so the induced cover on X_asym is trivial. | **F1** |

Reading the schema correctly, F0 fires first and its repair is `observable_replacement`
— **replace the observable, keep the scope**. So the honest reading is a repair loop,
not an immediate rejection:

1. F0 on `center_of_gravity_status` → replace it from within Π_CW.
2. Every remaining candidate in Π_CW returns F1 (claim-relative or total).
3. Π_CW is a **closed declared list**, so the quantifier in F1_BC is decidable here.
   F1 holds for every π ∈ Π_CW that still has a referent.
4. → **F1_BC** → `scope_rejection` on X_asym.

**This is the formal content of "asymmetric warfare requires a scope change."** It is
not "Clausewitz is outdated." It is: under the restriction to Π_CW, the boundary
condition set B_CW has no descriptive effect on X_asym. The repair path terminates in
rejection because it exhausts Π_CW, and this is decidable only because Π_CW is
declared and finite — the construction constraint in `falsification_schema.md` §F1_BC
(an agent constructing its own scope cannot apply F1_BC) does not bite for a scope
whose observable list is given in advance.

Note also that S_CW remains fully admissible **outside** X_asym. This is a
domain-restricted rejection, which is the strongest available result short of a global
one and is what ARW should produce here.

### 3.2 S_RC on X_asym — F0 on commensurability, then F2

**F0 on `payoff_vector`.** B_RC requires payoffs commensurable on a single scale. On
X_asym the parties' terminal values are not co-scaled — one party's payoff includes
items (continuation of a lineage or a cause, martyrdom, non-negotiable claims) that are
not exchange-priced against the other party's items. A single scale across
non-co-scaled quantities is **ill-formed without a declared normalisation**, and no
normalisation is available from the system.

This is structurally the *same* defect the repo has already isolated one level down:
a scalar ε across observables with different units is ill-formed absent a declared
normalisation (`general_regime_construction.md` §2.2; Q-EPS-01/03). Utility
commensuration is that defect at the payoff level. The parallel is not decorative —
the same repair applies, namely declaring a family plus a normalisation rule, and the
same failure applies when neither can be declared.

**F2 if commensurability is granted.** Suppose a normalisation is declared by fiat.
`equilibrium_distance` then has a referent, but θ* — the equilibrium selection point —
is unstable under Δ_RC: belief perturbations move it, and by (e) belief structure is
precisely the weak party's principal line of effect. Var(θ*) exceeds any workable
τ_var. → **F2** → `scope_rejection`.

**The anti-conservative bias, made explicit.** Δ_RC admits payoff trembles and small
belief perturbations, but not structural belief-manipulation. Narrowing Δ shrinks σ_Δ,
so σ_Δ < ε holds more easily, so more **stability** verdicts are issued
(`arw-repo-context` §1, inclusion-monotonicity of the canonical sup-form σ_Δ). A
rational-choice conflict model with a too-narrow Δ therefore does not fail neutrally —
it fails in the direction of **over-reporting the stronger party's stability**. This is
a derivation, not an observation, and it holds for every scope in this document whose
Δ contains the weak party's actual action channel (§4.2).

### 3.3 S_GA on X_asym — F1 at action resolution, plausibly F3

S_GA is the only one of the four whose **B survives X_asym intact**. It presupposes no
centre of gravity, no functional likeness, no commensurable payoffs, and no
complementary victory conditions. Properties (a)–(e) violate nothing in B_GA.

Its failure is elsewhere and is a resolution failure.

Fix the claim to the action-relevant one: *which regime is the system in, on the
timescale on which a decision must be taken* (weeks). At ε_GA, N(ε_GA) = 1 over any
such window — every state in a multi-year band lies in one cover component. →
**F1** for the action-relevant claim (claim-relative form: the ε-partition does not
refine the claimed structure).

Repair is `observable_replacement` or reduce ε. Reducing ε is only admissible while
ε > sup_x σ_Δ(x). For the Π_GA observables σ_Δ is large: structural-violence and
legitimation observables are not estimable to fine tolerance and they move
discontinuously under single events that are inside Δ_GA by declaration (an atrocity, a
widely circulated image). If sup_x σ_Δ(x) ≥ ε*(O, X_B) then I_ε = ∅ → **F3**,
collective failure, `scope_rejection` for the action-relevant Π.

Whether I_ε is actually empty is an empirical question and is registered below as
**Q-CFL-02**. The claim here is conditional and the condition is checkable.

The precise statement is therefore: **S_GA is descriptively sound on X_asym and
operationally empty at action resolution.** That is not a rhetorical dismissal; F3 is
a named failure mode with a stated cost, and S_GA's compensation is that it resolves
R5 (positive peace), which no other scope in this document resolves at all (§5.5).

### 3.4 S_RE on X_asym — F1_BC, with the channel-in-Δ pathology

| π ∈ Π_RE | On X_asym | Verdict |
|---|---|---|
| `capability_distribution` | Referent intact. Under (a) it is near-constant across X_asym while outcomes vary. Cover trivial w.r.t. the claimed structure. | **F1** |
| `polarity`, `alliance_configuration`, `offense_defense_balance` | Defined over *units* in the B_RE sense. Property (b) removes unit-hood for one party: the observable has no referent for it. | **F0** |
| `signal_credibility` | Presupposes a decision centre that can be committed. Same referent loss. | **F0** |

Every π either loses its referent or produces a trivial cover → **F1_BC** →
`scope_rejection` on X_asym.

**The channel-in-Δ pathology.** B_RE places unit-internal politics in Δ_RE by explicit
doctrine. By (e), that is exactly the channel through which the weak party's principal
effect propagates. So the partition depends strongly on a direction the scope has
declared to be "same state". Formally: σ_Δ is large along that direction, so the cover
is not Δ-stable there → **F-gradient**. Ordinarily F-gradient is repaired by
*increasing* ε above sup_x σ_Δ(x). Here that repair is unavailable: ε_RE is already at
the coarsest level that leaves any structure, and increasing it collapses the partition
entirely. The admissible window is empty in the same sense as §3.3.

**Severity bookkeeping.** The `scope_rejection` verdict for S_RE rests on F1_BC alone.
F-gradient never carries `scope_rejection` — its severity is `scope_refinement`
(ε/Δ/observable swap), and it appears here as a *secondary diagnostic* explaining
**why** the refinement path is closed, not as an independent ground for rejection.

That diagnostic is the sharpest in the document because it identifies a
**misassignment** rather than a limitation: a variable was placed in Δ that belongs in
Π. Neither replacing an observable nor tuning ε repairs a Δ/Π misassignment — both
operate inside a fixed partition of the tuple. Only a new scope does.

---

## 4. The Shared Defect

The four verdicts are not independent. Three defects run across them.

### 4.1 Defect 1 — a single-scope description of a two-scope system

Each of the four declares one (B, Π, Δ, ε) and applies it to the whole conflict:

| Scope | The shared-description assumption |
|---|---|
| S_CW | both parties operate under B_CW (purpose, centre of gravity, decidable defeat) |
| S_RC | a *common game* — hence common Π and common commensuration |
| S_RE | functional likeness — hence common B |
| S_GA | one contradiction, resolvable at one resolution — hence common ε |

On X_asym this is false in a specific way: the parties operate under different scopes,
**and each party's admissible action set contains acts that alter the other's scope
tuple** (property (e)). Attrition alters B of the weak party; a widely propagated
atrocity alters Π and ε of the strong party's constituency.

Restated: **asymmetry is not a capability ratio. It is a scope disparity.** Capability
disparity (a) is a symptom; the description-level disparity is the thing.

### 4.2 Defect 2 — the effect channel is inside Δ in all four

| Scope | Where the weak party's principal channel sits |
|---|---|
| S_CW | "moral factors" and friction — inside Δ, and outside Π by construction |
| S_RC | belief trembles — inside Δ, and bounded to small perturbations |
| S_RE | unit-internal politics — inside Δ by doctrine |
| S_GA | attitudes — inside Π, but at generational ε, so unresolved at action resolution |

Combined with the monotonicity result in §3.2, this yields a directional prediction
rather than a complaint: **all four scopes systematically over-report the stronger
party's stability**, because in each case the channel that destabilises the strong
party has been declared a perturbation to be absorbed. The bias direction follows from
inclusion-monotonicity of σ_Δ and is therefore not adjustable by better estimation
within any of the four scopes.

### 4.3 Defect 3 — scalar ε and a 1D control parameter

All four declare a single ε across observables of heterogeneous units — force ratios,
territorial fractions, casualty counts, attitude indices — with no stated
normalisation. By `general_regime_construction.md` §2.2 this is **ill-formed**, and it
is ill-formed independently of anything about asymmetry.

More consequentially: each of the four induces its partition along **one** control
parameter (stake-to-means ratio; payoff/commitment; capability ratio; structural
violence). Each is, in the pipeline's terms, a **1D sweep**. And the repo's own
finding is that a 1D sweep is **generically blind to structure of codimension ≥ 2**
(`general_regime_construction.md`, Q_NEW_25; validation strategy v2, Q-VAL-03).

§5.3 argues that the regime structure of X_asym is exactly codimension 2. If that is
right, it explains something the individual verdicts do not: why *repairs* to these
scopes keep failing. Counterinsurgency doctrine and population-attitude indices add
observables — they do not change the 1D sweep structure, so they inherit the blindness.

---

## 5. The Conflict Scope S_CONF

### 5.1 Design brief, and a correction to the two earlier ones

**Revised 2026-08-08 (second revision; see Q-CFL-09).** The two earlier versions of
this section both carried an unstated requirement: that the new description must
*recover* the four classical scopes as reductions. Version 1 built S_ASYM as an
asymmetry-specific scope and reported that S_GA could not be recovered. Version 2
withdrew that specific claim and concluded that unification therefore requires a scope
*family* along the resolution axis rather than a single tuple (§5.7).

Both conclusions follow from the recovery requirement. Neither survives dropping it.

The requirement is not obligatory, and it is expensive: recovering S_GA forces a large
Δ (positive versus negative peace is a stability statement under generational stress),
a large Δ raises sup_x σ_Δ(x), and the admissible window sup_x σ_Δ < ε < ε* then forces
a coarse ε — which is precisely why the resulting object could not also resolve
action-length structure. **The Δ-inflation came from S_GA alone.**

The brief adopted here is narrower and is the one the failures of §3 actually motivate:

> Construct one scope, over one X, admissible on **both** the symmetric and the
> asymmetric conflict region, whose induced partition distinguishes the regimes that
> decide outcomes in both. It is **not** required to reproduce any classical
> description. Every distinction it cannot make is stated in §5.6.

The last clause is the discipline that makes this different from scope-totalising
(§4.1): a scope that names what it cannot see is a scope, not a claim to cover
everything.

### 5.2 Both regions, one state space

Let X_sym ⊆ X be the region where properties (a)–(e) of §1 fail — approximately
matched capability, decomposable organisations, complementary victory conditions,
comparable time constants. X_asym is as defined in §1. S_CONF must be admissible on
X_sym ∪ X_asym.

**B is not the obstruction.** B_CONF is the *weakest* of the boundary condition sets in
play: it drops centre-of-gravity existence, decidable defeat, functional likeness,
payoff commensurability, complementary victory conditions and single decision centres.
Dropping an assumption does not exclude the systems that happen to satisfy it, so
X_{B_CONF} ⊇ X_{B_CW}. A symmetric conflict *has* a centre of gravity; it does not
need one *declared* in order to be described. This is why the apparent B-contradiction
between the classical and asymmetric readings is not a contradiction at all — it was an
artifact of treating a contingent feature as a boundary constraint.

What B_CONF does add:

- victory conditions need not be complementary
- organisational form is a declared per-party attribute, not a presupposition
- per-party time constants τ_i are declared, and their ratio is a scope parameter
- each party's exit threshold — the accumulated-cost boundary of its admissible
  region — is declared

### 5.3 The tuple

**Π_CONF is per-party.** This is the structural move version 1 missed. S_ASYM used `m`
for the strong party and `ρ` for the weak one, which silently encoded the asymmetry
into the observable list and made the scope asymmetry-specific by construction. Both
observables are defined for *every* party.

| π | Per party i | Defined on X_sym? |
|---|---|---|
| `m_i` — cost_tolerance_margin | distance from the current state to the boundary of party i's admissible region, in accumulated-cost units; m_i ≤ 0 means i's boundary condition is violated | yes — symmetric belligerents have cost boundaries too; exhaustion is the classical decision mechanism |
| `rho_i` — reconstitution_rate | replacement of organisational capacity per unit of capacity removed; ρ_i ≥ 1 means attrition is not a control parameter against i | yes — for a mobilising conventional army ρ can exceed 1 early and fall below 1 later |
| `legitimacy_flow_i` | net rate of transfer of population-level recognition toward i over the contested population | yes — home-front dynamics in symmetric wars are the same observable |
| `scope_control` | which party's categories the measurement and reporting system uses | yes — takes a near-tie value on X_sym, which is informative: it is the observable that *marks* symmetry rather than presupposing it |
| `territorial_control` | fraction of contested area | yes — retained **solely as a transfer anchor**, explicitly not partition-carrying (§5.6, cost 3) |

primary: `m_i`. The state of a two-party conflict is characterised for partition
purposes by (m_1, ρ_1, m_2, ρ_2).

**Δ_CONF**, declared as a family with verdict stability required across it:

```
Δ_min : tactical incidents, single engagements, individual casualty events
Δ_mid : + leadership decapitation of either party, + single scandal or atrocity events
Δ_max : + major economic shock, + onset of third-party intervention
```

Deliberately **not** included: generational structural stress. That omission is what
keeps sup_x σ_Δ(x) bounded, and it is paid for in §5.6 cost 1. The strong party's
constituency cost tolerance remains in Π (as m_i), not in Δ — unchanged from version 1
and still the single most consequential difference from all four classical scopes
(§4.2).

**ε_CONF**, a declared family with normalisation and symmetrisation stated
(Q-EPS-01/03):

| observable | normalisation |
|---|---|
| `m_i` | fraction of party i's declared exit threshold |
| `rho_i` | dimensionless |
| `legitimacy_flow_i` | fraction of contested population per unit τ_i |
| `territorial_control` | fraction of contested area, coarse |

Symmetrisation for state-dependent entries: `min(ε(x), ε(y))`. Note that `m_i` and
`legitimacy_flow_i` are normalised **per party** — the parties' thresholds and time
constants differ, and a single normalisation across them would reintroduce exactly the
commensurability defect that made S_RC F0 in §3.2.

### 5.4 Regime partition over both regions

The ρ-structure sorts states by which parties are attritable; the m-structure
overrides it when a boundary is violated.

| Regime | Condition | Content |
|---|---|---|
| **R_A — Symmetric attrition** | ρ_1, ρ_2 < 1; all m_i > 0 | Both parties attritable. Outcome decided by which m_i reaches 0 first. This is the classical case, and the classical *outcome structure* is reproduced without any classical observable. |
| **R_B — Asymmetric protraction** | exactly one ρ_i ≥ 1; all m_i > 0 | The attritable party's principal lever is inert against the other. Time is a control parameter, not a background. |
| **R_C — Mutual protraction** | ρ_1, ρ_2 ≥ 1; all m_i > 0 | Neither party can attrit the other. Nothing internal to the description decides the conflict; only a change in B ends it. **Named by none of the four classical scopes and by neither earlier version of this document.** |
| **R_D — Boundary exit** | some m_i ≤ 0 | The party whose boundary is violated exits, irrespective of ρ. Contains the diagnostic cell of version 1: m ≤ 0 for the stronger party while ρ < 1 for the weaker — a militarily defeatable opponent that outlasts anyway. |

Three observations.

**R_C is evidence the construction is not fitted.** It was not designed for; it falls
out of treating ρ per party. Protracted communal and multi-party internal conflicts sit
there, and their resistance to both classical and counterinsurgency description is a
prediction of the partition rather than an input to it.

**The classical outcome structure survives; the classical vocabulary does not.** R_A
reproduces decision-by-exhaustion. It does so through m_i, not through force ratio or
centre of gravity, and the mapping is one-way: R_A → "classical war" is well-defined,
"classical war" → R_A is not, because force ratio does not determine (m, ρ).

**Codimension.** The partition lives in a 4-dimensional observable space
(m_1, ρ_1, m_2, ρ_2), reducible by party-exchange symmetry but not to one dimension.
The §4.3 blindness argument therefore applies to every classical description here, and
reflexively to any 1D or 2D reading of S_CONF itself (Q-CFL-06).

### 5.5 Where the classical mechanisms reappear — as derived, not primitive

S_CONF does not contain the classical observables. It does have room for the
*mechanisms* they named, demoted from primitives to derived features that exist when
they exist:

| Classical primitive | Status in S_CONF |
|---|---|
| Centre of gravity | a mechanism by which m_i drops discontinuously — destroying it collapses a constituency's cost tolerance. Present when the organisation is COG-decomposable; simply absent otherwise, with no F0 incurred, because nothing in Π_CONF refers to it. |
| Force ratio | a determinant of dm_i/dt, not of the partition. It sets how fast margins are consumed, not which regime the system is in. |
| Equilibrium | a fixed point of the (m, ρ) flow, when one exists. |
| Structural violence | a determinant of the exit threshold declared in B_CONF — it shifts where m_i = 0 sits. |

This is the precise sense in which S_CONF does not reproduce the classical descriptions
while covering what they were describing.

### 5.6 The costs

Named, in descending order of how much they hurt.

**1. No peace description.** S_CONF has no observable distinguishing a transformed
contradiction from a suppressed one. Peace is not a regime in R_CONF; it is a boundary
of X_{B_CONF}. Consequence: S_CONF cannot say whether a settlement will hold. This is
structural, not an oversight — the distinction requires generational Δ, and admitting
it inflates sup_x σ_Δ(x) past any action-length ε (§5.7). Anyone needing that
distinction needs a second scope, and the two do not compose into one.

**2. The resolution window is unverified and the risk grew.** S_CONF needs
sup_x σ_Δ(x) < ε_i < ε*_i to hold for **four** partition-carrying observables rather
than two, on observables that are expensive to estimate and whose σ_Δ is largest
exactly at the boundaries that decide the partition (m_i near 0, ρ_i near 1). This is
Q-CFL-03, and S_CONF is *more* exposed to it than version 1's S_ASYM, not less. If the
window is empty, S_CONF is F3 by its own §6 criterion. **This is the single most
likely way the construction fails, and it is not addressed by anything above.**

**3. No operational resolution, and no transfer to the classical literature.**
ε*(m) is coarse in time — m moves on the timescale of constituency-level cost
accumulation. Engagements, campaigns and terrain are below resolution. S_CONF supports
no operational planning; it identifies a regime, not a course of action. Relatedly, it
shares no partition-carrying observable with any classical scope, so no Φ or TBS
comparison to that literature is defined. `territorial_control` is retained purely so
that *some* commensurable quantity exists, and it is explicitly not
partition-carrying — citing it as a bridge for partition claims would be a category
error.

**4. Estimation cost falls on the two hardest quantities.** m_i is a boundary distance
that requires the exit threshold in B_CONF to be declared before it can be measured at
all, and the declaration is a modelling commitment with no external source — the same
class of undeclarable-from-metadata object as Δ (Q-EWS-04). ρ_i requires organisational
data that adversaries do not publish. Cheap definitions, expensive measurements.

**5. Description symmetry is not action symmetry.** S_CONF describes both parties in
the same terms, which is the gain. It does not make T_12 = T_21 (§5.1 of version 2,
retained as §5.8): the channel by which each party can act on the other's description
remains asymmetric. Reading the symmetric observable list as implying symmetric options
would be a misuse.

**6. No falsification by recovery.** Because S_CONF reproduces no classical scope,
"S_CONF explains what S_CW explains" cannot be checked by partition compatibility. The
test must be direct and against a *mixed* case set containing both symmetric and
asymmetric conflicts — a harder test, and one whose case set has to be acceptable to
proponents of the descriptions being displaced (§6).

### 5.7 What was true in version 2, correctly scoped

The scope-family construction of version 2 is not withdrawn; its domain is corrected.
The argument was: Δ and ε are coupled through the admissible window
sup_x σ_Δ(x) < ε < ε*(O, X_B), so no single tuple has both a large Δ and a fine ε, and
a description that must cover action-length structure *and* generational stability must
therefore be a family {S_η} along the ε-axis of the fibration, with the content sitting
in the inter-level compatibility conditions.

That argument is **valid under the brief it was answering** — cover all four classical
descriptions, S_GA included. It is **not** an argument that both conflict *forms*
require a family, because the Δ-inflation entered only through S_GA. S_CONF covers both
forms in one tuple and pays for it with cost 1.

So the two results stand side by side, and the choice between them is a choice of
brief:

| Brief | Object | Price |
|---|---|---|
| cover both conflict forms, act at decision resolution | one tuple, S_CONF | no peace description (cost 1) |
| additionally resolve durable vs. suspended settlement | family {S_η}, inter-level compatibility structure | no single-level description; content sits between levels, and its general form is open (Q-CFL-08) |

### 5.8 Retained from earlier versions

**The scope-action operator.** Where the parties' operative constraint sets are
described separately, the conflict is C = (X, {S_1, S_2}, T_12, T_21), with T_ij the
declared set of admissible actions by i that modify components of S_j. S_CONF is the
joint description; C is the party-indexed one. T_12 ≠ T_21 is the irreducible content
of "asymmetry" and is not removed by S_CONF (cost 5). Formalisation status: Q-CFL-05.

**Connection to KHT.** `kht_group_dynamics.md` §3 and §4.1 supply a mechanism for m_i:
it is a boundary distance of a constituency, and KHT describes constituency-level
regime stabilisation — manifold collapse, attractor deepening, polarisation as
bifurcation — as a dynamic on that object. Two consequences, neither established here:

- KHT's attractor-deepening result predicts σ_Δ(m_i) is not uniform — small in a
  deepened collective regime, large near a bifurcation. If so, cost 2's F-gradient risk
  becomes *predictable* rather than merely present, which is the most promising
  available route to addressing the construction's main failure mode.
- The pressure-induced regime compression of `art_geopolitical_scope_example.md` §7 has
  the same shape one aggregation level up. Whether identical or analogous is Q-CFL-04.

## 6. Falsification Conditions

S_CONF is falsifiable as a description, independently of any claim about any conflict.
Every test must run on a **mixed** case set — symmetric and asymmetric conflicts
together — because covering both forms is what it claims (§5.6, cost 6).

| Test | Failure category if it fails |
|---|---|
| Across a mixed case set, (m_i, ρ_i) sorts outcomes better than force ratio alone | **F1**, claim-relative — the observables do not refine the claimed structure |
| For each of m_i, ρ_i there exists a declared ε with sup_x σ_Δ(x) < ε < ε*(O, X_B) on at least one real case | **F3** for Π_CONF — no admissible resolution window. This is the leading risk (§5.6, cost 2) |
| R_C (mutual protraction) is non-empty | the per-party treatment of ρ is over-built; a single ρ suffices and §5.4 is over-parameterised |
| R_D contains cases where the exiting party's opponent had ρ < 1 | if empty, the m-structure adds nothing over the ρ-structure and the partition collapses to one dimension |
| R_A reproduces the outcome ordering of symmetric wars that S_CW describes correctly | if not, S_CONF has not covered the symmetric form and the whole brief of §5.1 fails |
| The over-reporting prediction of §4.2 holds directionally | if strong-party stability is *under*-reported by the classical scopes, the σ_Δ monotonicity argument has been misapplied |

The third and fifth rows are the load-bearing ones: the third is the only claim S_CONF
makes that no predecessor makes, and the fifth is the one it would be easiest to fail
quietly.

## 7. What This Document Does Not Claim

- That any actual conflict occupies any particular cell of R_CONF. No case is analysed.
- That S_CW, S_RC, S_RE or S_GA are invalid. Each is rejected **on X_asym only** and
  remains admissible on its own domain.
- That S_CONF **replaces** them. It reproduces none of them (§5.5) and gives up six
  classes of distinction to cover both conflict forms in one tuple (§5.6). Displacement
  would have to be argued case by case against the §6 tests, and the peace-resolution
  brief is served by the family construction of §5.7, not by S_CONF.
- That the parties "have" scopes in any psychological sense. See the level-discipline
  note in the preamble: an attributed scope is a declared description, not a subject.
- That S_CONF has been instantiated. No ScopeSpec, no BCManifest, no pipeline run
  exists. Status is `hypothesis` for that reason.
- That ρ_i or m_i have accepted operationalisations. They have definitions; whether they
  have measurements is Q-CFL-03, and §5.6 cost 2 names this as the most likely way the
  construction fails.

---

## 8. Open Questions

| ID | Question |
|---|---|
| Q-CFL-01 | Is the F1_BC verdict for S_CW (§3.1) robust to enlarging Π_CW with any observable a Clausewitzian reading would admit, or does some admissible addition rescue the scope? The verdict's decidability depends on Π_CW being closed. |
| Q-CFL-02 | Is I_ε empty for Π_GA at action resolution (§3.3), or merely narrow? This decides F3 versus a recoverable F1. |
| Q-CFL-03 | Are `m_i` and `rho_i` estimable on real cases within their declared ε, i.e. does sup_x σ_Δ(x) < ε* hold for all four partition-carrying observables? If not, S_CONF is F3 by its own criterion. **Leading failure risk** (§5.6 cost 2). |
| Q-CFL-04 | Is KHT attractor deepening (`kht_group_dynamics.md` §4.3) the same phenomenon as pressure-induced regime compression (`art_geopolitical_scope_example.md` §7) at a different aggregation level, or merely analogous? |
| Q-CFL-05 | Does the scope-action operator T_ij require formalisation as a distinct ARW object, or is it expressible as a party-indexed section of the existing scope fibration? |
| Q-CFL-06 | Are there conflict regions where a *third* dimension is forced, making R_ASYM itself a 2D projection of codim-3 structure? The §4.3 argument applies reflexively. |
| Q-CFL-07 | Is the Δ-stability reading of positive vs. negative peace (§5.5) faithful, or does it drop a component of "transformation" that is genuinely not a stability statement? The §5.5 correction rests on it. |
| Q-CFL-08 | Is there a general form for the compatibility structure between resolution levels of S(η) (§5.7), or is it case-by-case? Without one, the family construction names the right object but supplies no machinery. |
| Q-CFL-09 | Is R_C (mutual protraction, §5.4) genuinely non-empty, and is the per-party treatment of ρ therefore necessary? R_C is the only structure S_CONF claims that no predecessor claims — if empty, the construction is over-parameterised. |

---

*Scope tuple semantics: `docs/glossary/scope.md`. Falsification categories:
`docs/core/falsification_schema.md`. ε-family and Δ-reachability requirements:
`docs/notes/general_regime_construction.md`. Reduction criterion:
`docs/core/arw_scope_reduction_partition_criterion.md`.*
