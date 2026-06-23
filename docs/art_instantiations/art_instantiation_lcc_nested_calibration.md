---
status: hypothesis
layer: docs/art_instantiations/
related:
  - docs/notes/conflict_navigation_nested_calibration.md  # nested calibration loop (anchor); verified 2026-06-24 (in DOC_INDEX)
  - docs/glossary/scope.md                         # verified 2026-06-24 (in DOC_INDEX)
  - docs/glossary/observable_range.md              # verified 2026-06-24 (in DOC_INDEX)
  - docs/glossary/perturbation_spread.md           # verified 2026-06-24 (in DOC_INDEX)
  - docs/bc_taxonomy/boundary_condition_classes.md # verified 2026-06-24 (in DOC_INDEX)
  - docs/art_instantiations/kht_architecture_layer1.md  # KHT Layer 1 — operator/modulator (dependency, §5); verified 2026-06-24
audience: ARW/ART repository; governance / conflict-navigation instantiation
source: handwritten notes 2026-06-13 ("ARW: The Four Layers of a Low-Carbon Concrete Standard Update")
revision: v2 (2026-06-23) — adds obstruction typology, kinematics/dynamics factorization,
  cost-landscape topology, goal-metric construction, cooperation-will as boundary condition
---

# ART Instantiation: Nested Calibration and a Typology of Calibration Obstructions

**Level: ART** (concrete domain instantiation) with one explicitly ARW-level
contribution (§3, the kinematics/dynamics factorization). The LCC standard-update is
the worked instance; the obstruction typology and the cost-landscape framing are the
transferable claims. Not a pipeline case (no sweep, no `Invariants.json`).

---

## 1. State space and scope tuple

Let **X** be the space of candidate *standard configurations*; `x ∈ X` is one possible
version of the procurement standard. `S = (B, Π, Δ, ε)`:

| Component | Instantiation |
|---|---|
| **B** | Boundary constraints selecting `X_B ⊆ X`: public-procurement legality, embodied-carbon-reduction mandate, supplier-ecosystem feasibility, political feasibility, documentation/compliance. |
| **Π** | Observables: GWP `kg CO₂e/m³`, volumetric thresholds, supplier-readiness levels, mix-admissibility criteria, cost deltas, performance constraints, documentation completeness. |
| **Δ** | Admissible perturbations: proposed parameter moves, supplier-readiness fluctuation, cost variation within bounds, messaging adjustment. |
| **ε** | Resolution threshold over `Π`. |

**Regime partition `R_S`**: stable equivalence classes (*admissible-mix*, *supplier-ready*,
*politically-feasible*, *documentation-complete*) — the "workable positions." Each party's
acceptable outcome corresponds to a non-empty regime in `R_S`.

Transitions in the source notes are **parameter transitions** within fixed `S`, not scope
transitions. That distinction is the hinge of everything below.

---

## 2. The nested calibration loop

Two loops, different objects, different timescales (cf. `nested_calibration_loop.md`):

| Loop | Operates on | Timescale | Venue |
|---|---|---|---|
| **Lower — observable calibration** | `Π` parameters / thresholds within fixed `B` | fast, convergent | in-session |
| **Upper — scope calibration** | `B` and the target regime ("set point") | slow, reflective | between sessions |

**Refinement (from discussion 2026-06-23).** The notes located the upper loop *spatially*
("between sessions / not in the room"). The fundamental requirement is weaker and more
general: **the two loops must not run simultaneously.** Live scope-calibration is possible,
but then observable-calibration must pause. The invariant is **loop separation**, not place
or time. Running both at once in the same room is what converts a Calibration process into
a Conflict process in real time.

---

## 3. The central factorization: scope-kinematics vs coupling-dynamics (ARW-level)

A calibration process has **two independent axes**. Conflating them is the recurring error.

- **Kinematics (scope):** what is *describable, admissible, distinguishable* — fixed by
  `S = (B, Π, Δ, ε)` and the partition `R_S`. Answers: does a shared workable regime
  *exist and is it visible*?
- **Dynamics (coupling):** what is *selected and moved toward* — fixed by an inter-level
  **coupling operator** (the modulator acting on the operator; between agents, the coupling
  between modulators). Answers: do the parties actually *move* to a visible shared regime?

These are different object types. Kinematics is a tuple; the coupling operator is **not** a
`(B,Π,Δ,ε)` tuple at any aggregation level (see §5). This factorization is what keeps
"conflict = scope pathology" from collapsing into a tautology: not every conflict is a
scope defect.

---

## 4. Typology of calibration obstructions

A process **calibrates** iff a shared non-empty regime in `R_S` exists, is visible, and is
reachable under `Δ`. Obstructions fall into four structurally distinct classes — the first
three kinematic, the fourth dynamic.

| Class | Condition | Axis | Remedy direction |
|---|---|---|---|
| **(a) Scope under-specification** | `B` and/or `Π` incomplete → a party's regime is unrepresentable; the shared regime is *not visible* though it may exist | kinematic | complete `B`/`Π`; widen scope |
| **(b) Δ-asymmetry** | a shared regime exists in the (extended) scope, but a party's `Δ` rejects exactly the perturbations that reach it — **power** as asymmetric admissible-perturbation set | kinematic | symmetrize reachability; change who can move what |
| **(c) Empty acceptable intersection** | no regime is acceptable to all parties under *any* admissible scope within cost bound — **values / identity** | kinematic | no calibration; only scope transformation beyond bound |
| **(d) Selection / strategic obstruction** | a shared, non-empty, mutually *preferred* regime exists **and is visible**, but the inter-modulator coupling does not reach it — **coordination / commitment** (e.g. PD with common knowledge) | **dynamic** | not a scope operation; see §5–§7 |

**Key claim (ARW-level).** Classes (a)–(c) are scope pathologies, possibly multi-level —
they reduce to mis-specification of `S`. Class (d) is **not** a scope pathology at any
aggregation level: lifting the preference to a higher-aggregation scope `S'` (its observables
shared, its orderings agreed) leaves the obstruction intact one level up. The obstruction is
a fixed-point property of the coupling operator, not of any scope. Class (d) is therefore the
falsifiable boundary of the reduction: a real conflict no scope operation can touch. Its
existence is what gives the reduction teeth rather than making it a universal solvent.

> The notes' classification "Calibration vs Conflict" is the (a)+(c)-vs-Calibration cut.
> The full typology distinguishes (a), (b), (c), (d). The LCC case is **Calibration**:
> `B` inherited, set point ex ante, `Π` shared, every party's regime non-empty.

---

## 5. The motivation cost-landscape (hypothesis — KHT Layer 1 dependency)

Selection requires an object `S` does not contain: a **preference / cost field** — an
ordering over `R_S`, i.e. a valuation of descriptions, not a description. At higher
aggregation it can appear as the `Π'` of a scope `S'` whose substrate is `R_S`; but the
*downward* selection/control channel is an **inter-level operator**, not a tuple.

**Topology.** "What motivates" is a multi-basin cost field over `R_S`:
- **basins** = motives / stable preferred regimes;
- **saddles / barriers** = ambiguous-gradient regions between motives;
- **reachability is `Δ`-relative**: whether a basin is left depends not on the depth of the
  neighbour but on whether available `Δ` clears the barrier. Motivation is a property of the
  **pair (landscape, Δ)**, not of the landscape alone.

**Metastable conflict (answers Q-LCC-03).** A shared acceptable regime that is *non-empty
but cover-unstable* — `σ_Δ` over the shared regime approaching `ε` as process `Δ`
accumulates — is structurally analogous to **F-gradient**, lifted to the regime/cost-field
level: calibrates short-term (regime exists at coarse `ε`), collapses long-term (accumulated
`Δ` fragments the cover). "Smouldering conflict / fragile agreement" is this F-gradient-analog,
not a separate type.

**The coupling operator (the unformalized core).** Class (d) lives in the *form* of the
downward operator:
- **Best-Response** → fixed point beside the good regime (PD-type); class (d), irreducible;
- **Reference-Tracking** → follows a set point; no fixed-point trap; reduces.

Typing this operator **is** the formalization of "motivation" in KHT Layer 1. It cannot be
settled by adding aggregation levels (regress); only by typing the operator. The Labyrinth
agent is the existence test: hold the cost/salience structure fixed, vary the agent's `Δ`,
and check whether emergent modes change (→ motivation is `Δ`-relative) and whether
Best-Response vs Tracking produce distinguishable behavioural signatures **without encoding
the category as input**.

**Source of the field (open).** The first symmetry break over `R_S` must be externally
coupled (a free internal field would explain everything → universal solvent). But once a `Π`
exists, the ongoing gradient may be **B-anchored** (necessity/expectation — heteronomous) or
**Π/Δ-anchored** (reducing `σ_Δ` = competence; enlarging range of `Π` = curiosity; stabilizing
the cover = coherence — intrinsic, not freely chosen because `σ_Δ`, cover, range are fixed
once `Π` exists). Whether KHT admits Π/Δ-anchored motivation decides whether it models
fully heteronomous agents or agents with an intrinsic motivation source.

---

## 6. Constructive: the common goal-metric as upper-loop construction

A **co-constructed goal-metric** is, in this language, the upper loop building a *shared cost
field* over the common partition. Built well, every party's basin is non-empty — because each
placed its own basin in during construction. This is the **constructive** form of the
participation incentive (a party participates iff it has a non-empty, reachable basin).

**Reach and limit.** A shared goal-metric resolves (a)–(c): it makes a reachable shared
basin *exist and visible*. It does **not** resolve (d): a perfectly shared metric (PD: both
rank C,C highest) still collapses if the inter-agent coupling is Best-Response. Constructing
the landscape does not change the descent dynamics on it.

**Path, not just destination (`Δ`-relative barriers).** A shared *target* is not a reachable
*target*. Two groups agreeing on the same optimum can differ in the barrier structure of the
path: a high intermediate barrier exceeding the group's available `Δ` stalls the process
despite agreement. The operative upper-loop question is therefore not "is the optimum shared?"
but "is the hardest intermediate regime transition barrier ≤ available `Δ`?" — break the path
into `Δ`-clearable steps.

---

## 7. Cooperation-will as a boundary condition (not an output)

The cooperative coupling operator (Reference-Tracking of a shared set point rather than
Best-Response) is a **boundary condition of the procedure**, not a product of it. It sits in
`B` of the upper loop. No moderation architecture manufactures it.

This is a controllability-limit claim, against the implicit promise of most moderation theory
that the *right procedure* produces cooperation: **no procedure creates the will; it can only
shape the landscape so an existing will reaches a visible target.** The single lever between
precondition and outcome is **path-barrier height relative to `Δ`** (§6): the procedure cannot
raise the will, but it can lower how much will each step requires. Operationally: not "is the
will present (yes/no)?" but "does the present will suffice for the barriers of this path?"

---

## 8. Naming correction — "structural fallout" is not canonical F0

⚠ The source notes label the constraint-elision mode **"F0."** This is **not** canonical ARW
F0 (`R(π) ∩ B ≠ B`, observable-range violation; severity `observable_replacement`; see
`observable_range.md`). The notes describe a party's structure being dropped from the shared
description: a `B`-constraint elided (supplier/political) or a `Π`-observable dropped
(performance) → `X_B` mis-specified and/or `Π` incomplete → that party's regime becomes
empty/unrepresentable in `R_S` → loss of participation incentive. This is **class (a)**
(scope under-specification), a defect in the specification of `S` itself — distinct from
F0/F1/F-gradient, which all presuppose a correctly specified `S`. Use the name **constraint
elision**, not F0.

---

## 9. Open questions

| ID | Question | Status |
|---|---|---|
| Q-LCC-01 | Is "constraint elision" (§8) a distinct ART label, or exactly "`B` mis-spec + `Π` incomplete"? | open |
| Q-LCC-02 | Operationalize "calibratable regime": when does a party's regime become ∅ under `Δ`, in terms of `σ_Δ` over `X_B`? | open |
| Q-LCC-03 | Metastable Calibration↔Conflict band — confirmed as F-gradient-analog (§5)? Formalize `σ_Δ`(shared regime) → `ε` as the criterion. | partially answered (§5) |
| Q-LCC-04 | Promote to a pipeline `CASE` (sweep over admissible-configuration space) or is `X` irreducibly qualitative? | open |
| Q-LCC-05 | Type the downward coupling operator: Best-Response vs Reference-Tracking. Decides whether class (d) is irreducible or reduces. **KHT Layer 1.** | open |
| Q-LCC-06 | Does co-constructing the goal-metric (§6) merely share the *landscape*, or also reshape the inter-agent *coupling form* (Best-Response → Tracking)? If the latter, the procedure attacks (d) directly. | open |
| Q-LCC-07 | Conflict as transformation `T(S₁→S₂)`: define equivalence of transformations across domains (groupoid of scopes; conflicts as morphisms classified up to equivalence) to make cross-domain conflict comparison well-posed. | open |
| Q-LCC-08 | Does KHT admit Π/Δ-anchored (intrinsic) motivation, or only B-anchored (heteronomous)? (§5) | open |

---

## 10. Placement and provenance

- **Depends on:** `nested_calibration_loop.md` (loop construction) and the KHT Layer 1
  operator/modulator architecture (§5, Q-LCC-05) — confirm exact paths and `depends_on`
  against `docs/meta/DOC_INDEX.md` before commit.
- **Register** in `DOC_INDEX.md` as a revised ART instantiation (supersedes v1 of this file).
- A matched **non-repo** artifact exists: the facilitator-language translation
  ("Tuning or Framing?", v2) for field use by a practitioner with no ARW vocabulary.
  It is deliberately not a repo file and must not inherit 