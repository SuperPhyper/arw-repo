---
status: note
layer: docs/notes/
title: "Scope-Constructing Agent and KHT — Reconciliation of the Existence Test"
created: 2026-07-27
depends_on:
  - docs/cognitive_architecture/agent_context_navigation_project_brief_v2.md
  - docs/art_instantiations/kht_architecture_layer1.md
  - docs/art_instantiations/kht_architecture_layer2.md
related:
  - existence_test_preregistration_wp3.md (external — not in repo; unfrozen, import is part of its own freeze protocol)
  - docs/context_navigation/scope_constructing_agent_architecture.md
  - docs/notes/scope_constructing_agent_implementability.md
  - docs/context_navigation/switch_minimization_criterion.md
  - Simulationen/labyrinth_scope_constructing/ARCHITECTURE.md (external — simulation code, not in repo)
---

# Scope-Constructing Agent and KHT — What Still Fits, What Broke, What Opened

The labyrinth agent exists in this project for one reason: to test whether
low-dimensional mode structure arises from learning alone, in a system that
carries no typological heritage (brief v2 §1). The new agent in
`Simulationen/labyrinth_scope_constructing/` is architecturally different from
the one WP3 was written for. This note settles what that does to the KHT link.

Three answers up front:

1. **The reason for the link is stronger, not weaker.** The old observation space
   contained three ready-made distance observables built to match three
   prescribed modes; the new one does not. That was the most direct
   contamination route in the whole design, and it is gone.
2. **The measurement apparatus of WP3 largely does not survive.** E2, the
   decision-relevant criterion, cannot be computed at all on the new agent.
3. **A structural correspondence appeared that nobody designed**, between KHT's
   operator/modulator split and the agent's own layering — and it exposes a
   sharp limit on what the current build can possibly find (§4).

---

## 1. What never depended on the architecture

Brief v2 §1: an artificial agent is informative because it carries no MBTI
heritage as a confounder. That argument is about *provenance*, not about the
learning algorithm. It holds for any agent.

What does depend on the architecture is whether the agent's own design smuggles
the hypothesis back in. On that, the new build is a clear improvement:

| Contamination route (brief v2 §3) | Old stack | New stack |
|---|---|---|
| State representation pre-encoded along hypothesized axes | `d_nav`, `d_stuck`, `d_time` — three global distance observables, built to correspond to the three prescribed modes `navigate/stuck/time`. Any axis recovered by PCA over weight vectors on that space is partly a recovery of the designer's typology. | 16 primitive channels, no distance in any form, no aggregate. Observables are *compositions* the agent forms. |
| Policy architecture with a fixed mode count | 64 archetype slots (surplus, closed) | 32 mode slots, and modes are not slots but recurring solutions; duplicates are not instantiated |
| Environment mapped onto axes | six substrates by physical admissibility | unchanged, inherited |
| Interpretation door | axis-wise pre-classification (WP3 §5.1) | needs re-derivation, see §3 |

So the single biggest KHT-relevant change is independent of any result: the
observation space no longer contains the answer.

---

## 2. What broke in the WP3 apparatus

WP3 is at `frozen: false`, so nothing here violates a freeze. But three of its
four criteria were written against objects the new agent does not have.

| Criterion | What it needs | Status | Candidate replacement |
|---|---|---|---|
| **E1 separation** | `M[a,s]` = mean `progress_rate` of archetype *a* on substrate *s*; median dominance ratio ≥ 1.2 | **Reformulable.** No `progress_rate` as an effectiveness scalar, but a mode × layout matrix of mean encounter duration or mean prediction error carries the same information | mode × layout matrix of mean encounter duration; the existing mode×band NMI is a cousin of it |
| **E2 dimensionality** (decision-relevant) | participation ratio over per-archetype `w_in ⊕ w_out ⊕ context` (30-dim) | **Cannot be computed.** The new agent has no weight vector and no context centroid. A mode is (Π_m, W, Q). | three genuinely different options: (a) 109-dim sparse indicator of Π_m → dimensionality of the *description* space; (b) flattened forward models W; (c) the R_m stability profiles. They answer different questions and one must be chosen and frozen *before* running |
| **E3 stability** | Hungarian matching on \|cos\| in the shared 30-dim feature space | **Cannot be computed**, same reason | matching modes across runs by Jaccard overlap of Π_m — arguably cleaner than cosine on weights, since it compares *what is described* rather than a numeric profile |
| **E4 axis comparison** | the frozen A1–A9 classification | **Needs re-examination** — the agent changed, and several axes moved (§3) | §3 |

Consequence: the SCA programme needs **its own preregistration**, not an edit to
WP3. The recommendation of the implementability note (§7 there) stands and is now
concrete: freeze WP3 for the WP1 agent, write a second preregistration for this
one, share the environment and the observer, share nothing else.

---

## 3. The nine KHT elements, re-examined

WP3 §5.1 classified each element as (i) plausibly BC-independent — the agent can
speak to it — or (ii) biologically grounded — the agent is silent. Several of
those judgements change, and mostly in the direction of *better* access.

| # | KHT element | WP3 verdict | Now | Why |
|---|---|---|---|---|
| A1 | **J/P** — convergence (selects, closes) vs divergence (keeps open, runs parallel) | (i) candidate | **directly measurable, better than before** | the scope audit *is* this distinction: `switch`+`adjust` close on existing structure, `form`+`unresolved` keep options open. The branch mix is a first-class logged quantity, not a factor loading |
| A2 | **Latent / Transient** — persistent profile vs transiently accessible mode | (i) candidate | **native** | mode identity in this architecture *is* persistence. `mean_duration`, `age` and 𝒫_m measure it directly. The old design had no such quantity at all |
| A3 | **I/E** — stabilization from internal state vs environmental feedback | (i) conditional, "weaker analog" | **stronger than conditional** | readable straight off Π_m: does the mode's forward model rely on proprioceptive/interoceptive channels (internal) or tactile/distal ones (external)? KHT defines the modulator as *where stabilization comes from*, which is exactly what the forward model rests on |
| A4 | **Ni↔Se** — projective condensation into model-points vs stimulus-gradient tracking | (i) conditional | **a coordinate of the description** | the candidate pool contains both families literally: `MEAN12` is time-averaged condensation, `ID`/`DIFF4` are instantaneous value and gradient. Layer 1 §1.1's own wording ("condenses input into abstract model-points" vs "captures real-time gradients, intensity transitions") describes the two operator families in the pool |
| A5 | Si↔Ne — discrete state anchors vs variant maps | silent, **Π** ("10-dim space carries no variant topology") | **arguably now addressable** | the offline phase generates *variants* of a description and either adopts them or not. `identical` vs `scope_varied` is a discrete-anchor vs variant-map contrast at the level of description handling. This is a change to a frozen classification and must be re-decided explicitly, not assumed |
| A6 | T/F — structural-consistency vs relational-contextual evaluation | (ii) BC, no social BCs | **still silent, and now for a sharper reason** | the agent has exactly one evaluative criterion (prediction error under an admissibility filter). T/F requires two competing criteria; there is no second one to be modulated between |
| A7 | 16-count / duality / Ego–Shadow blocks | (ii) BC | **still silent, conditionally reachable** | the duality construction (invert all three modulators) has an agent-side analogue *only if* modulators become agent-side — see §4 |
| A8 | function hierarchy / activation weighting | (ii) BC | **still silent** | the agent does have a dominance structure (`n_active` per mode), but the specific weighting KHT claims is Restriction-shaped; unchanged |
| A9 | SD/UD developmental subtypes | (ii) BC, no handle at all | **an agent-side developmental axis now exists** | six staged capability levels, self-paced on description stability, with a measurable time-to-stabilize curve and recorded stalls. This is *not* biological maturation and the BC-mismatch clause fully applies — but for the first time the *form* of a developmental claim has an agent-side counterpart. This is also where the temptation to overclaim is largest |

Net: A1–A4 are more directly measurable than under the old design and depend less
on post-hoc factor analysis; A5 and A9 moved from "silent" to "arguably
reachable"; A6–A8 are unchanged.

---

## 4. The correspondence nobody designed — and the limit it exposes

KHT Layer 1 splits the space in two:

- **Operators** generate cognitive content. Four of them, in two antagonistic
  pairs (Ni↔Se, Si↔Ne).
- **Modulators** generate no content. They are *global* parameters that determine
  how operator output is filtered, oriented and selected. Three binary ones →
  8 clusters, with a duality map obtained by inverting all three.

The agent, built without reference to this, has the same split:

| KHT Layer 1 | Scope-constructing agent |
|---|---|
| operators — generate descriptive content | the composition operators over the raw field (`ID`, `MEAN4/12`, `DIFF4/12`, `VAR8`, `RATE12`) |
| operator pair Ni↔Se | temporal-integration antagonism inside that pool: `MEAN12` vs `ID`/`DIFF4` |
| modulators — global, content-free, determine how output is handled | ε_agent (what counts as a distinction at all), the selector (which criterion recruits observables), λ (parsimony pressure) |
| modulator cluster — a complete global setting | one configuration of those three = one run of the simulation |
| duality — invert all three | the maximally distant configuration in the factor space |

**And here is the limit.** In KHT the modulators are *inside* the system and vary;
the 16 types are operator × modulator combinations. In the agent as built, all
three modulator-analogues are **exogenous** — set by the experimenter, constant
within a run. ε_agent is deliberately fixed (if the agent could raise it,
switch minimization collapses to not distinguishing anything, the F1 condition);
the selector is a command-line choice; λ is swept.

Therefore: **the current build can at most discover operator-side structure. It
cannot discover a modulator geometry, because it has exactly one modulator
cluster per run.** That is a clean structural explanation for something the pilot
runs kept showing — mode counts of 6–14 that do not collapse onto a small number.
The agent is recombining operators inside a single fixed cluster.

### 4.1 The architecture step this implies

Make the modulator-analogues part of the mode rather than of the run: each mode
carries its own resolution ε_m and its own recruitment criterion, and both are
revised in the offline phase like everything else. Then modes differ not only in
*which* observables they use but in *how their output is handled* — which is
exactly the operator × modulator product — and the existence question becomes the
one KHT actually poses: does that product space collapse onto a small number of
recurring clusters?

Anti-circularity check: this does not install the eight clusters. ε is continuous
and there are four selectors, so the offered space is larger than 2×2×2. That is
the degrees-of-freedom surplus principle of brief v2 §3, not a prescription. What
must be avoided is any per-mode modulator whose *poles* are named after KHT's.

One caveat to carry: with ε agent-side and revisable, the F1 degeneracy returns
(a mode could raise its own resolution until it distinguishes nothing). The guard
is the same lexicographic construction as offline admissibility — a mode may
revise ε_m only among settings that keep its description non-degenerate.

---

## 5. Scope discipline — unchanged

Brief v2 §1.2 stands untouched. The agent tests `BC_agent → mode geometry`; KHT
claims `BC_human → mode geometry KHT`. No outcome of one decides the other, and
cross-scope statements go only through explicit transfer analysis.

One nuance the new build adds: developmental staging is now part of B_agent. That
makes B_agent *more articulated* than a bare RL agent, and in exactly one respect
more similar to B_human (staged sensory and motor access), while remaining
utterly different in the others (no embodiment, no social coordination, no
language, no cultural evolution). This makes the eventual transfer analysis more
interesting and more delicate: the B-difference is no longer a single lump.

---

## 6. Status against the WP3 gates

For completeness, where the current pilot data would land if the WP3 rules were
applied with substituted quantities:

- Mode counts 6–14 across configurations, not converging to the three-band count.
- mode×band NMI 0.03–0.26 — weak.
- Competence: goal rate ~0.07. *(Corrected 2026-07-27 (III): this was previously called
  "flat". Against a random walker in the same substrates — goal 0.007, within-5-cells
  0.030 — the agent's 0.05–0.073 and 0.29–0.36 are roughly ten times chance. Competence is
  real and was being read off quantities with no dynamic range. The separation
  precondition E1 has no usable verdict in either direction: three successive versions of
  the ratio were defective, and the corrected episode-grain measurement is underpowered at
  180 episodes.)*

That is Gate 0/1 territory — design iteration, or outcome 3 (no low-dimensional
organization emerges). **We have changed the instrument; we do not have a
reading.** *(2026-07-27 (III): and for a while the instrument was not measuring what it
claimed. The gate verdict is withdrawn rather than reversed — it is unmeasured, not
failed.)* Nothing in the last several sessions moved the existence question, and
saying otherwise would be the failure mode brief v2 §9 was written to prevent.

---

## 7. What has to be decided

| # | Decision | Bears on |
|---|---|---|
| K-1 | Freeze WP3 for the WP1 agent and write a second preregistration for the SCA agent — or supersede WP3 entirely | §2 |
| K-2 | Which E2 replacement becomes decision-relevant: description-space dimensionality, forward-model space, or stability profiles. Must be fixed before running | §2 |
| K-3 | Re-decide A5 (silent by Π, or reachable via the variant-map contrast) and A9 (silent by BC, or reachable via the developmental axis) — explicitly, with reasons recorded | §3 |
| K-4 | Whether to make ε_m and the recruitment criterion mode-level and revisable, which is what would make the modulator geometry reachable at all | §4 |
| K-5 | Whether the existence question is still the primary target, given that the last several sessions produced mechanism findings and no movement on it | §6 |

---

## Maintenance History

- **2026-07-27**: Created in response to the question how the scope-constructing
  build relates to KHT at all. Main contributions: the contamination-route
  comparison showing the link is strengthened (§1); the enumeration of which WP3
  criteria survive and which cannot be computed (§2); the axis-by-axis
  re-examination, in which A1–A4 gain directness and A5/A9 move (§3); and the
  operator/modulator correspondence with the limit it implies — exogenous
  modulators mean the current build can only find operator-side structure (§4).
