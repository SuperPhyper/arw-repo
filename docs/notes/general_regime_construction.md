---
status: hypothesis
layer: docs/notes/
created: 2026-08-04
depends_on:
  - docs/glossary/scope.md
  - docs/core/cover_stability_criterion.md
  - docs/core/falsification_schema.md
  - docs/glossary/perturbation_spread.md
  - docs/notes/scope_fibration.md
  - docs/notes/description_atlas_programme.md
---

# The General Regime Construction — Δ-derived adjacency, with the 1D sweep as a degenerate case

**Purpose.** The operative regime construction in this repository is defined on an
ordered one-dimensional sweep. That restriction is historical, not principled, and
it costs more than convenience: on a 1D path the cover construction degenerates
into increment thresholding, the argument that justified adopting it becomes
vacuous, and an entire class of description failures is *generically invisible*.
This note states the construction without the dimension restriction, exhibits the
1D sweep as its degenerate special case, and lists what becomes definable only at
dimension ≥ 2.

**Status.** Proposed construction, answering the open part of Q_NEW_25. Not yet a
canonical definition; no case has been run under it.

---

## 1. Two findings that force the generalisation

### 1.1 The operative 1D construction degenerates into thresholding

`docs/glossary/scope.md` fixes the operative form: the ε-adjacency graph G_ε on
the sampled sweep, "edge between **consecutive** samples iff their observable
increment is ≤ ε", regimes = connected components.

On an ordered sample with consecutive-only edges the graph is a **path graph**.
Between any two nodes there is exactly one path. Connected components are
therefore precisely the maximal runs on which every consecutive increment stays
≤ ε — i.e. the construction reduces to *thresholding the increment sequence*.

This matters because of what it does to the justification.
`docs/core/cover_stability_criterion.md` adopts the cover over plain pairwise
indistinguishability for one stated reason: transitivity-safety, the sorites
resolution — "|O(x)−O(y)| ≤ ε and |O(y)−O(z)| ≤ ε does not force x and z into the
same class unless they are also connected via a chain". That argument has content
only where **several distinct chains** can connect two states. On a path graph
there is one chain, so the argument is vacuous in exactly the format the pipeline
uses. Note also that `cover_stability_criterion.md` defines G_ε(O) over **all**
pairs, not consecutive ones; the canonical definition retains the content, the
operative implementation discards it. This is a doc↔code divergence in the
central construction.

### 1.2 The 1D construction uses an undeclared adjacency

"Consecutive in the sweep" is not part of the scope tuple. It comes from the
sweep design — the parameter grid the experimenter chose — and it is nowhere
declared as a scope component. The construction therefore depends on a modelling
ingredient outside (B, Π, Δ, ε).

This is the same class of defect as the ε/Δ conflation found on observational
data (`ews_stage1_review_epsilon_vs_delta.md`): a quantity that looks given but
is in fact chosen, and is not declared. The general construction below removes it
by deriving adjacency from Δ, which *is* a declared component.

## 2. The general construction

> **Definition (candidate).** Let X_B be the admissible state set (or a sampled
> subset V ⊆ X_B), O : X_B → (M, d) an observable, Δ the admissible perturbation
> class, ε > 0.
>
> The **admissible-transition relation** is Δ-reachability:
>
>   x ⌢ y  :⟺  y ∈ x + Δ  (one admissible perturbation apart).
>
> The **ε-adjacency graph** G_{ε,Δ} has vertex set V and an edge {x, y} iff
>
>   x ⌢ y  **and**  d(O(x), O(y)) ≤ ε.
>
> **Regimes** are the connected components of G_{ε,Δ}, subject to the stability
> requirement that component membership be invariant under all δ ∈ Δ
> (assignment-instability indicator χ_{Δ,ε} = 0, mass criterion per
> `falsification_schema.md`).

Two properties are worth stating explicitly.

**Δ does double duty, and this is the point.** Δ already fixes which perturbations
the regime assignment must survive. Here it *also* fixes along which steps chains
may run. The two roles are the same commitment read in two directions — "these
differences do not matter" determines both what must be tolerated and what counts
as a neighbouring state. Nothing new is declared; an ingredient that was
previously smuggled in is now derived.

**Dimension does not appear.** The construction is stated for any X_B with a
Δ-action. No ordering, no sweep, no grid.

### 2.1 The 1D sweep as a degenerate special case

Take X_B sampled on a one-parameter grid {b_1 < … < b_M}, and let Δ be (or be
approximated by) one grid step in the sweep parameter. Then x ⌢ y holds exactly
for consecutive samples, G_{ε,Δ} is the path graph, and the construction returns
the current operative definition. The existing cases are therefore not invalidated
— they are recovered as the codimension-0 slice of the general object, with their
adjacency now derived rather than assumed.

### 2.2 ε is a declared family, not a scalar (added 2026-08-04)

The definition above writes `d(O(x), O(y)) ≤ ε` with **one** observable and
**one** threshold. Both are restrictions, and the second is the less obvious one.

Three distinct multiplicities must be separated:

| Multiplicity | Form | Status in the repo |
|---|---|---|
| across observables | ε_i, one per π_i ∈ Π | **undeclared**: ScopeSpec carries a scope-level `epsilon` *and* a per-observable `resolution_floor` (CASE-0001: 0.09 and 0.01) with no stated relation |
| across the domain | ε(x), e.g. reading-dependent instrument accuracy or a relative tolerance | named once (`ews_stage1_review_epsilon_vs_delta.md` §2.1) and then dropped |
| across resolution | the family {S_ε}, I_ε, cover height, η = −log(ε/ε₀) | **already sound**: this is the ε-direction of the fibration, where a scope legitimately *is* a point |

Only the third is settled. The first two have been assumed away.

**Empirical note.** The scalar assumption has already been abandoned once, with
effect: run 2 of the Q-DSP-01 checks used the per-point condition
`d ≤ ε − s(x) − s(y)` rather than a global threshold, and that is exactly the step
that turned a vacuous test (1 of 112 rows) into one with 1.85M informative edge
checks. The non-scalar form was the one that worked.

**Commensurability.** A single numeric ε applied across observables with different
units is not merely imprecise, it is ill-formed. CASE-20260311-0003 carries
`lambda_proxy` (a rate, span 0.0688) and `var_rel` (dimensionless, span 0.2974) —
a factor 4.3 in span. The same ε is 4.3× more permissive relative to span for one
than the other, and the swept grid reaches ε = 0.5, i.e. seven times the entire
span of `lambda_proxy`. Any cross-observable ε therefore requires a **declared
normalisation** (by span, by ε*, by a physical scale), and the declaration is a
modelling step in its own right.

**Proposed form.**

> ε is declared as a family ε = (ε_i)_{π_i ∈ Π}, each ε_i possibly a function
> ε_i(x) on X_B, together with a normalisation statement wherever any
> cross-observable comparison is made.

A per-point ε breaks the symmetry of the edge relation, so the symmetrisation must
also be declared: `d(O(x),O(y)) ≤ min(ε(x), ε(y))` is the conservative choice
(fewer edges, finer partition) and is the recommended default; mean or max are
admissible but must be stated.

### 2.3 Two composition rules over Π — and they are not the same

With ε a family, a second choice appears that the 1D format concealed.

- **Rule A — joint graph.** Edge {x, y} iff x ⌢ y **and** d_i(O_i(x), O_i(y)) ≤ ε_i
  for *all* i; regimes are the components of that single graph.
- **Rule B — common refinement.** Build one partition per observable, then
  intersect them: x, y share a regime iff they share a regime under every
  observable (composite label tuple).

**On a 1D path these coincide**, because a cut appears wherever any observable's
consecutive increment exceeds its threshold, under either rule. **In general they
diverge**: a Rule-B class is defined by label agreement and need not be
*connected*, whereas a Rule-A component is connected by construction.

For the atlas and fibration readings this matters. A chart is meant to be a
*region* (`description_atlas_programme.md` §2), so connectedness is not optional
and **Rule A is the candidate** — but that has to be declared rather than
inherited. A disjunctive variant (edge iff *some* i agrees) is also formally
available; it yields coarser partitions, has no evident interpretation here, and
is recorded as considered and not adopted.

### 2.4 Finding: `epsilon_multi_observable.py` does not answer its own question

The repository already contains a multi-observable ε module, and its docstring
states the question exactly:

> *"Does a single ε suffice, or does each observable need its own εᵢ? What is the
> joint admissible region in (ε₁, ε₂) space?"*

Three observations on the implementation, all checkable:

1. **The (ε₁, ε₂) region is never computed.** The sweep iterates a single scalar
   (`for eps in eps_values`) and applies it to every observable, so only the
   diagonal ε₁ = ε₂ is explored. Question 3 of the docstring is unanswered by the
   module that poses it.
2. **It implements Rule B**, not Rule A: joint regimes are composite label tuples
   ("two points are in the same regime iff they agree on ALL observables"). Given
   §2.3 this is a substantive choice made implicitly.
3. **The evidence that one ε does not suffice is already in the output.**
   `CASE-20260311-0003/results/partition/EpsilonMultiObservable.json` records
   `agreement_rate = 0.367` — the two observables produce the same plateau
   structure on barely a third of the ε-grid — alongside the 4.3× span disparity
   above. The module was run, the answer to its question 2 looks negative, and
   nothing was drawn from it.

This is a doc↔code divergence of the same class as the two already recorded in
this note (§1.1) and in `qdsp01_check_results/README_qdsp01_check.md` (the
"σ_Δ" field that is a finite difference).

## 3. What is generically invisible in 1D

This is the argument that makes the generalisation necessary rather than merely
tidy.

A boundary in a parameter space has a **codimension**. In a 2-parameter space a
regime boundary is generically a curve (codim 1), but genuine *defects* can be
points (codim 2). A one-dimensional sweep through such a space meets a codim-1
curve transversally — fine — but meets a codim-2 point only by coincidence, i.e.
with probability zero under generic placement.

> **A 1D sweep is generically blind to every structure of codimension ≥ 2.**

This is not a resolution problem that a finer sweep repairs; refining a
1D sweep does not increase the chance of hitting a point in a plane. Only raising
the dimension of the swept region does.

The class is not exotic. For real symmetric two-level systems, degeneracies occur
at codimension 2 (von Neumann–Wigner counting: two independent conditions must
hold simultaneously) — conical intersections are exactly such point defects in a
2-parameter plane. The atlas programme's candidate **type-T obstruction**
(`description_atlas_programme.md` §5) therefore cannot be reached from any 1D
sweep, in principle rather than in practice.

## 4. What becomes definable at dimension ≥ 2

| Object | 1D status | Status in the general construction |
|---|---|---|
| Transitivity / sorites content | vacuous (one chain) | substantive: multiple chains, cover genuinely ≠ pairwise closure |
| Nerve topology | trivial (path is contractible; H₁ = 0) | non-trivial H₁ possible → topological obstruction type T becomes reachable |
| θ* | scalar | boundary **set**: curve or hypersurface, with connectivity, curvature, and codimension of its own |
| Z(π) exclusion zone | interval | region with shape; can disconnect X_B or not |
| Regime adjacency | path graph | general graph: triple junctions, nesting, non-simply-connected regimes |
| Path dependence | up-sweep vs down-sweep (hysteresis) | full loop structure — the setting in which monodromy is even statable |
| Defects of codim ≥ 2 | generically missed | detectable |

The entries in the right column are not refinements of the left column. Several
of them have no 1D counterpart at all, which is why the framework's distinctive
content has never been in a position to show itself.

## 5. What breaks in the current schema, and how it generalises

| Artifact | Current form | Assumes | Generalisation |
|---|---|---|---|
| `Invariants.theta_star` | scalar | ordered axis, single boundary point | boundary set: sampled curve/surface, or a list of components with their codimensions |
| `Invariants.sweep_range` | `[min, max]` | 1D interval | swept region: box, or explicit sample hull |
| `TBS_norm` | \|θ*_A/range_A − θ*_B/range_B\| | scalar θ*, scalar range | **undefined** in the general case; requires a distance between boundary *sets* (Hausdorff-type) or must be declared inapplicable |
| ε-plateau on N(ε) | regime count along a line | 1D ordering | unchanged in form — N(ε) is a component count, defined for any graph; plateau logic survives |
| `sweep.py` / `extract_partition.py` | one `sweep_param` | 1D | needs a neighbourhood-structure argument instead of an implicit ordering |

The honest cost: **TBS_norm does not survive** without a new definition, and it is
a component of Φ. Any 2D case therefore cannot be compared to 1D cases with the
current transfer metric. Given that Φ already carries the open Q-REL-05 caveat,
this is a good moment to make that dependency explicit rather than patch around
it.

Existing partial assets: the 2D field scripts in `Simulationen`
(`cover_2d_all_cases.py`, `sweep_2d_all_cases.py`, `kuramoto_2d_sweep.py`,
`cover_observable_space.py`, `cover_pipeline_v2.py`) already compute
grid-neighbour adjacency and cover height on 2-parameter fields. Their adjacency
is *grid*-derived rather than Δ-derived, so they instantiate §2 only
approximately — but the computational core exists. CASE-20260430-0013 is
registered as a 2D case (A × Ω/ω₁) and has never been run: README,
consistency check and signature-first document only.

## 6. Risks and honest limits

1. **Sampling cost.** Component structure on a d-dimensional grid needs samples
   growing exponentially in d. Beyond d ≈ 3 a dense grid is not available and the
   construction needs a sparse-sampling variant, which is not designed.
2. **Δ-reachability must be made concrete.** "y ∈ x + Δ" is clean on paper; on a
   sampled domain it requires a rule for when two samples count as one
   perturbation apart. That rule is a declared modelling step and must not
   silently become "grid neighbours" — that would reintroduce §1.2's defect in a
   new place.
3. **The ε-family multiplies the declaration burden.** Each ε_i, each ε_i(x)
   profile, the symmetrisation rule and the normalisation are declared modelling
   steps. More declared freedom means more room for post-hoc tuning, so any case
   using a non-constant ε-family needs its declarations frozen before the run —
   the same discipline the Cascade protocol established.
4. **More dimensions can add noise, not structure.** The generalisation is
   justified only where the additional directions carry declared scope content.
   Sweeping a second parameter that nothing depends on adds sampling cost and no
   information.
5. **Nothing here is yet tested.** The construction has not been run on any case.
   Its first obligation is to reproduce the existing 1D results as the §2.1
   special case; failure to do so falsifies the construction, not the cases.

## 7. Testing outlook (not a preregistration)

In rough order of cost:

1. **Recovery check.** Run the general construction on an existing 1D case with
   Δ = one grid step, and verify it reproduces the registered partition exactly.
   Cheap, and a hard prerequisite.
2. **2D re-derivation.** Run CASE-20260430-0013 or the Kuramoto (κ, σ) field
   under §2 with a declared Δ, and report the boundary as a **set** rather than a
   scalar — the first artifact the current schema cannot hold.
3. **Codim-2 case.** Construct or locate a 2-parameter system with a point defect
   and test whether the general construction detects it while a family of 1D
   sweeps through the same region does not. This is the direct test of §3, and it
   is the prerequisite for any type-T work.

Each becomes a preregistered protocol before it is run, per the practice
established for the Cascade study.

## 8. Registry

- Partially answers **Q_NEW_25** (general regime construction beyond the 1D
  sweep): the construction is proposed here; the attributed transition graph and
  the SDI consequence named in that question remain open.
- Relates to **Q-DSP-07** (topological obstruction type): §3 shows the type-T
  question is not reachable at all from 1D, so this construction is its
  prerequisite.
- Relates to **Q-REL-08** (TBS normalisation) and **Q-REL-05**: §5 shows TBS_norm
  has no general form; this sharpens rather than resolves those questions.
- Registers **Q-EPS-01/02/03** (§2.2–§2.4): the form of a declared ε-family, the
  composition rule over Π, and the commensurability/normalisation requirement.
