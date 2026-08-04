---
status: note
layer: docs/notes/
title: "Scope-Constructing Agent Architecture — Implementability Analysis against the Labyrinth Codebase"
created: 2026-07-26
depends_on:
  - docs/context_navigation/scope_constructing_agent_architecture.md
  - docs/context_navigation/context_navigation_emergent_modes_experiment.md
  - docs/context_navigation/agent_online_scope.md
  - docs/context_navigation/agent_sleep_scope.md
  - docs/context_navigation/transfer_semantics_context_navigation.md
related:
  - docs/cognitive_architecture/agent_context_navigation_project_brief_v2.md
  - existence_test_preregistration_wp3.md (external — not in repo; unfrozen, import is part of its own freeze protocol)
  - Simulationen/labyrinth_existence_wp1/ (external — simulation code, not in repo)
  - pipeline/sweep_behavioral.py
  - pipeline/transfer_v2.py
open_questions:
  - Q-SCA-01
  - Q-SCA-02
  - Q-SCA-03
---

# Implementability Analysis — Scope-Constructing Agent Architecture in the Labyrinth

> **Purpose.** Section-by-section confrontation of
> `scope_constructing_agent_architecture.md` (hypothesis, 2026-07-26) with the running
> labyrinth code in `Simulationen/labyrinth_existence_wp1/`. This document decides what
> can be reused, what must be extended, what must be built, and what currently **cannot
> be measured at all**. It is a build-precondition document, not a design change to the
> architecture proposal.
>
> **Verdict up front.** The agent side of §14 arm C is roughly a two-thirds extension of
> existing code and is buildable. The *measurement* side is the blocker: neither of the
> two primary measures of §14 — transfer Φ and the stability-domain width 𝒫_m — is
> computable in the current setup, for the same underlying reason (§5). One design
> decision (introducing a graded BC axis κ into the labyrinth, §5.3) unlocks both.
> §15's matching condition ("C1 and C2 matched on gradient steps") does not apply to
> this codebase as written and must be restated (§6).

---

## 1. What the fork base actually is

`labyrinth_existence_wp1/` (2026-06-11, WP1 of project brief v2). Agent-facing stack:

| Module | Implements | Corresponding spec section |
|---|---|---|
| `env_base.py` | 25×25 grid, 10 observables (`m_eff, v_sight, e_edge, c_contact, m_cost, r_resource, w_eff, d_nav, d_stuck, d_time`), deterministic transition, reward shaping | `agent_online_scope.md` §2 |
| `env_open/halfwall/costpath/corridor/combined/procedural.py` | six substrate classes. R/C/F zone *labelling* is generic (`env_base._zone_label(col)`, column bands, reported as `info['zone']`); `env_combined.py` is the only environment that assigns **different substrate types** to the three bands (`R_END=8`, `C_END=16`, `VIS_RADIUS` per type) | `..._emergent_modes_experiment.md` §1.1 |
| `env_procedural.py` + `policy.py` maze pool (`N_MAZE_POOL = 30`) | unseen instances with preserved topology | δ₂ of `..._emergent_modes_experiment.md` §3 |
| `s_online.py` (`SOnline`) | weight field w over the 10 observables; scalar label-free salience s(t) = ‖obs_ema − c_active‖₂/√D; debounced trigger (`THETA_SAL=0.18, SAL_K=3, REFRACTORY=5`); encounter close + weight update; subscope mask (`THETA_W=0.10`); protocol buffer (FIFO, 50) | `agent_online_scope.md` §4, §5 — **but see §2** |
| `s_sleep.py` (`sleep_phase`) | flat archetype library, similarity matching, winner-takes-place revision by `progress_rate`, context centroid running mean, similarity merge (`THETA_MERGE=0.08`), overflow replacement at `MAX_ARCHETYPES=64` | `agent_sleep_scope.md` §3, §4 |
| `policy.py` | Gymnasium wrapper + PPO (SB3); policy input is `mask(w)·w·obs`, 10-dim; `net_arch=[32]`, 4 actions | — |
| `run_experiment.py` | smoke test, training with `SleepAndLogCallback` (sleep runs at **every episode end**), curriculum over the six substrates, evaluation (100 frozen-policy episodes) | — |
| `s_observer.py` | encounter-window segmentation, ε-sweep on `action_dist` (L1, 4-dim) and on `obs_mean` (L1, 10-dim), `EPS_MIN=0.01, EPS_MAX=1.0, EPS_N=50`, plateau finder, go/no-go (N≥2, width≥3), correspondence against `zone_type` | `arw_observer_scope.md`; `..._emergent_modes_experiment.md` §2 |

Sandbox check (2026-07-26): `env`, `s_online`, `s_sleep`, `s_observer` import and run
standalone under numpy 2.2.6; `policy.py` / `run_experiment.py` additionally need
`gymnasium` + `stable_baselines3`, which are present on Rico's machine only. The
non-PPO parts of a fork are therefore testable in the sandbox; full runs are local.

---

## 2. Correction to §0 of the architecture document (load-bearing)

§0 of `scope_constructing_agent_architecture.md` lists as "used, not redefined":

> | Saliency triggers, strength, saliency record | `agent_online_scope.md` §3 |
> | Archetype library structure and matching rule | `agent_sleep_scope.md` §3, §4.1–4.2 |

and §5 closes with *"Trigger taxonomy and strength grading are `agent_online_scope.md` §3."*

**Those sections are superseded by the running implementation, and deliberately so.**
`agent_online_scope.md` §3 specifies three *named* triggers (`structure_loss`,
`resource_threshold`, `progress_drop`), a three-level strength grading, and §4.1 a
library **partitioned by saliency type** with hard-gate matching. WP1 removed all of it
(project brief v2 §2; `labyrinth_existence_wp1/README.md`): one scalar category-free
signal, flat library, similarity matching, no strength buckets, no `priority_mode`
distance gate. This closes brief v2 §3's anti-circularity door "salience labels".

Consequence for the build: arm C inherits the **WP1 stack**, not the spec text. Any
"trigger taxonomy" or "strength grading" reintroduced into §5's scope audit, or any
categorical field in the failure signature F of §7/§9.3, reopens that door and makes
the emergent mode count an input again. Concretely: **F must be a vector, not a class
name** (§4.4 below).

Recommended repo action, separate from the build: either add a supersession note to
`agent_online_scope.md` §3/§4.1 pointing at brief v2 §2, or correct the §0 table of the
architecture document to cite WP1. Right now a reader of §0 will implement the labeled
version.

---

## 3. Where the existing code sits in the §14 arm matrix

| §14 arm | Requirement | Status in this codebase |
|---|---|---|
| **B** | single unstructured policy, regimes read out post hoc | **Available with a switch.** PPO + `s_observer` already do this; arm B = fix w ≡ 1/D, disable salience/archetypes, keep the observer. Roughly 20 lines of flags. |
| **C0** | scope-constructing agent, no offline phase | **This is essentially WP1 as it stands.** `sleep_phase` is not an offline phase in §8's sense: it reads *aggregated* protocol records and never replays or re-describes anything. As a C-arm ablation, WP1 = C0. |
| **C1** | identical episodic replay | **Not present.** No trajectory-level record exists to replay (§4.1). |
| **C2** | scope-varied recapitulation | **Not present.** The core of the proposal is the part with no code. |
| **A** | prescribed mode library + gating selector (`agent_architecture_mode_ecology.md`) | **Not present, and not equal to the pre-WP1 baseline.** The labeled baseline in `labyrinth_emergent - procedural - verification/` has categorical triggers and a partitioned library, but no prescribed mode library and no gating selector over modes — `agent_architecture_mode_ecology.md` §3/§4 requires both. Arm A is a genuine new build, and the most expensive arm to build *honestly* (a badly built arm A makes C-SCA win for free). |

**Reading.** The three-arm claim C-SCA is not testable by extending one agent; A and C2
are both new. If the budget forces a cut, the C1-vs-C2 ablation (Q-SCA-01) survives
alone and decides §15's cheap negative; arm A alone does not decide anything.

---

## 4. Requirement-by-requirement gap table

### 4.1 §7 — Scope retention in the encounter protocol

Current protocol record (`s_online.py` `_close_encounter_and_update`):

```
{context, salience, coverage_dist, covered, C_in, C_out, w_in, w_out, progress_rate, duration}
```

§7 asks for `e_i = (X_i, S_i^entry, m_i^entry, T_i, S_i^exit, m_i^exit, r_i, F_i)`.

| Field | Status | Note |
|---|---|---|
| `w_in`/`w_out` | present | |
| `S^entry`/`S^exit` | **missing** | Needs an explicit scope object. In this codebase S is realizable as (B = substrate class id, Π = active mask over the 10 observables, Δ = perturbation set in force, ε = the resolution actually in use). Only Π and B have code counterparts today; Δ and ε are not agent-side quantities at all (ε lives in `s_observer`, i.e. observer-side). **This is the first conceptual decision the fork forces: does the agent carry its own ε, or is ε observer-only?** The architecture document assumes the former (§3: "the distinctions that currently count"); WP1 implements the latter. |
| `X_i` (the encounter field) | **missing and required for §8** | Only the EMA-smoothed `context` survives. Recapitulation over a stored encounter needs the **raw observation window**, i.e. the per-step 10-dim vectors between two salience events. Buffer cost is small: episodes are capped at `T_MAX=120` steps with ~6–12 salience events, so an encounter is ~10–20 steps; the FIFO-50 protocol buffer (spanning several episodes) then holds at most 50 × 120 × 10 float64 ≈ 480 kB worst case. |
| `T_i` (transformations traversed) | **missing** | Realizable as the w-trajectory within the encounter plus mask changes. Cheap once `X_i` is stored. |
| `F_i` (failure signature) | **missing, and needs a definition** | See §4.4. |
| `m_i^entry/exit` | **missing** | Archetype identity is not written into the protocol; the matched archetype is used and discarded. Needs a stable archetype id (currently archetypes are anonymous dicts in a list, and `remove()` in the merge pass shifts indices — ids must be assigned, not positional). |

### 4.2 §8 — Recapitulation: what is cheap and what is not

The four variation axes of ℛ(e; δB, δΠ, δε, δw) are **not equally expensive in this
environment**, and the difference is not the one §9.2 anticipates:

| Axis | Cost | Why |
|---|---|---|
| δw | **free** | Re-run the S_online pipeline over the stored raw observation window with a different weight field. No environment, no world model. |
| δε | **free** | Same, if ε becomes agent-side (§4.1). |
| δΠ | **cheap but bounded** | Realizable only as *masking subsets of the fixed 10 observables* (the `THETA_W` mask already does exactly this). No observable can be *added* offline — Π is a compile-time constant. §8's question "what would I have seen under a different weighting of Π" is answerable; "under a richer Π" is not. This bounds Q-SCA-02 more than the document assumes. |
| δB | **expensive** | B is the substrate class / maze instance. Changing it invalidates the stored observation window; the episode must be re-simulated. |

The decisive split is not the four reconstruction *levels* of §9.2 but **passive vs.
active recapitulation**:

- **Passive** (δw, δε, δΠ over the stored window): re-describes a fixed trajectory.
  Answers "what would I have seen, and would a different scope have made this
  navigable?" Requires **no world model at all** — a strong and cheap result for
  Q-SCA-02, and the natural C2 implementation.
- **Active** (δB, or any variation where the re-described scope would have produced
  *different actions*): requires re-simulation. Feasible here — the environment is
  deterministic given `(instance, seed, spawn, exit)` and instances are pooled and
  seeded — but the re-run is then **a different episode, not the same one**, and the
  invariant extraction of §9.3 loses its paired structure.

**Recommendation.** Build C2 as passive recapitulation first, and treat active
recapitulation as a separate later variant. Passive C2 is the honest test of Q-SCA-01:
it adds *no new environment samples whatsoever*, which is exactly what an
augmentation-vs-reorganization discrimination needs (§6).

### 4.3 §9.1 / §9.4 — Prioritization, merge, split, prune

| §9 element | Status |
|---|---|
| Prioritized encounter selection p(e_i) ∝ λ₁\|σ_i\| + λ₂U_i + λ₃N_i + λ₄T_i | **missing.** `s_sleep.py` filters (`C_in > EPS_STAB`, `duration ≥ 5`, `≥ 5` valid protocols) but does not rank. `salience` and `coverage_dist` are already stored, so \|σ\| and a novelty proxy N are available at once; U and T need definitions. |
| *unresolved-encounter* branch (§5, fourth branch) | **missing.** Currently a coverage failure (`covered == False`) triggers exploration and is otherwise treated like any other protocol. Marking it unresolved and giving it maximum recapitulation priority is a small, well-defined extension — and it is the one branch of §5 with no counterpart in the existing selection mechanism, so it is worth isolating as its own ablation. |
| merge | **present** (`THETA_MERGE=0.08`, encounter-count-weighted centroid). Note it merges on *similarity*, whereas §9.4 wants merge on *overlapping stability profiles under a shared BC signature* — a different and stronger criterion that needs §4.5. |
| prune | **partially present** as overflow replacement of the weakest, least recently updated archetype at 64 slots. Not a redundancy prune. |
| split | **missing entirely**, and gated on §4.5: "bimodal profile over Δ" is not computable without a graded Δ. |

### 4.4 The failure signature F — needs a definition, and it must stay label-free

F appears in §7 (protocol), §9.3 (signature extraction) and in the mode tuple of §4.
Nothing in the code records anything like it. It is also the single most likely place
for the anti-circularity door of §2 to swing back open, because the intuitive
implementation is a small set of named failure types.

Proposed definition, kept vector-valued: at encounter close, record

```
F_i = ( deviation vector at close (10-dim),  Δprogress_rate over the encounter,
        Δr_resource,  contact fraction,  net displacement / path length )
```

— all already available or trivially derivable from the stored window. Failure *classes*
then only ever appear as clusters found in F-space by the observer, never as agent-side
labels. This keeps §9.3's "which failure signature announces the breakdown" answerable
without naming failures.

### 4.5 §10 — R_m and 𝒫_m: the hard blocker

`R_m(δ) = Pr(admissible navigation | m, δ)` and `𝒫_m = {δ ∈ Δ : m(S+δ) stable}` require
a **graded, quantified perturbation channel**. The environment has none:

- No perceptual noise. Grep confirms no noise term anywhere in `env_base.py`,
  `env_maze.py`, `env_cells.py`, `env_procedural.py`; observations are computed
  deterministically from position and state. δ₁ of `..._emergent_modes_experiment.md`
  §3 ("random noise up to magnitude η") **is not implemented**.
- δ₂/δ₃ (other instances, other seeds) are *categorical*, not graded. You cannot ask
  "how far out in Δ does this mode survive" against a set of unordered instances, and
  §14's sharp prediction is precisely a statement about *width* — 𝒫_m wider than the
  training envelope. Without a magnitude axis there is no envelope and no width.

**So §14's secondary measure is currently unmeasurable, and §15's decisive comparison
(𝒫_m width vs. training envelope) with it.** This is the primary blocker, and it is a
missing 30-line environment wrapper plus a decision about what Δ *is* for this agent.

### 4.6 §14 primary measure Φ — second blocker, same root cause

Φ per `transfer_semantics_context_navigation.md` §2.1 is computed by
`pipeline/transfer_v2.py`, which requires per case a `PartitionResult.json` and an
`Invariants.json` carrying **`sweep_range`** and **`theta_star`**. The labyrinth
observer writes none of these — `s_observer.save_observer_results` writes its own
schema (`H1_go_nogo`, `epsilon_sweep`, `epsilon_sweep_obs`, `correspondence_analysis`,
`windows_summary`).

An adapter exists — `pipeline/sweep_behavioral.py` — and its own docstring names the
obstacle:

> "Phase 1 (labyrinth) has **NO BC parameter sweep** — all Zone A constraints are fixed.
> The 'sweep' here is … sweep ε … The output follows the same schema as
> EpsilonSweep.json but uses ε (not κ) as the sweep axis."

With ε as the sweep axis there is no θ*, so `compute_tbs` returns undefined and PCI has
no common normalized axis to resample onto. **RCD survives; TBS and PCI do not; hence Φ
does not.** Reporting Φ from an ε-axis sweep would be a metric misuse, and given the
standing v1-PCI defect finding (2026-06-02) it is exactly the kind of number that later
has to be retracted.

### 4.7 §13 — Multi-agent

No multi-agent environment exists at any point in the four labyrinth generations; the
Gym wrapper is single-agent and the observer segments one trajectory at a time.
§13 is a separate build, not an extension. It should stay out of the first fork — but
note that §13 is where the document places its own heaviest load (Q-SCA-05, Q_NEW_F),
so "out of the first fork" is a scheduling decision to be recorded, not a downgrade.

---

## 5. The one decision that unblocks both measures

Both blockers (§4.5, §4.6) have the same root: **the labyrinth has no graded BC axis.**
Physics cases sweep κ; the labyrinth sweeps nothing.

### 5.3 Proposal: introduce a graded κ into the environment

Candidates already latent in the code, in order of least invasiveness:

| κ candidate | Where it lives now | Graded? |
|---|---|---|
| step-cost level (`cost_map` scale) | `env_costpath.py`, `env_base.cost_map` | continuous, trivially parameterizable |
| visibility radius | `env_combined.VIS_RADIUS` per zone type | small integer, already per-zone |
| resource budget `t_max` / `r_resource` slope | `env_base`, `T_MAX` | continuous |
| observation noise magnitude η | **does not exist** | continuous once built |

A single graded axis serves three purposes at once:

1. **Φ becomes computable** — a κ-parameterized behavioral sweep yields θ* and
   `sweep_range`, so `transfer_v2` runs as designed and §14's primary measure is real.
2. **Δ acquires a magnitude** — 𝒫_m and R_m become estimable, and §14's sharp
   prediction (𝒫_m wider than the training envelope) becomes a statement with a number
   on both sides. Train within κ ∈ [κ_lo, κ_hi]; probe outside it.
3. **Split becomes decidable** — "bimodal profile over Δ" (§9.4) presupposes exactly
   this axis.

Cost: one environment wrapper (graded κ + optional observation noise), one adapter from
`s_observer` output to `PartitionResult.json` / `Invariants.json`. Both are small
relative to arm A.

**Caveat to record.** Introducing κ makes the labyrinth more like the physics cases,
which is convenient for the pipeline and slightly changes the object of study: the
zone-topology correspondence (H1/H2 of `..._emergent_modes_experiment.md`) is a
*categorical* comparison, and a κ-sweep is not a substitute for it. Both should be run;
κ is added alongside the zone comparison, not in place of it.

---

## 6. §15's matching condition does not apply as written

§15 requires C1 and C2 to be *"matched on gradient steps, not on episode count"*. In
this codebase the offline phase and the gradient learner are disjoint:

- **PPO** (the only gradient learner) is trained purely on environment steps in
  `LabyrinthGymEnv`. It never sees the sleep phase, the protocol buffer, or the
  archetype library.
- The **weight field** w is not learned by gradient at all. `_close_encounter_and_update`
  sets `w ← clip(w_target + U(−δ,δ))`, normalized — stochastic hill-climbing around the
  matched archetype's `w_out`, with `delta_scale` annealed by archetype effectiveness.
- The **archetype library** is revised by winner-takes-place replacement on
  `progress_rate`, again no gradient.

So recapitulation cannot add gradient steps unless it is deliberately wired into PPO
(e.g. re-training on re-described observation windows). Two options, and the choice
changes what Q-SCA-01 means:

| Option | What C2 varies | Matching condition |
|---|---|---|
| **(a) library-only recapitulation** (recommended first) | archetype library and w only; PPO untouched | match C1/C2 on **number of library revision events** and on environment steps. The augmentation confound nearly vanishes: passive recapitulation (§4.2) adds no new samples of any kind, so an advantage cannot be sample count. |
| (b) recapitulation feeds PPO | policy gradient too | then §15's gradient-step matching applies literally, and the confound is real and must be controlled as written. |

Under (a), §15's cheap negative is not "extra effective sample count" but **"extra
library update count"**, and the matched control is C1 with the same number of identical
re-reads. Worth recording as a sharpening of §15 rather than a deviation from it — the
falsification logic is unchanged, only the currency.

---

## 7. Relation to the existence-test programme (must be settled before building)

`existence_test_preregistration_wp3.md` is at `frozen: false`. It freezes agent
hyperparameters (all of the WP1 constants), E1 separation, E2 participation-ratio
dimensionality bands, E3 seeds/orders, E4 KHT axis comparison — an evaluation programme
on the *same environment and the same observer* as §14, but with different measures and
a different question (existence of low-dimensional structure vs. superiority of an
architecture on transfer).

Two things collide if this is not settled first:

1. §14's arms change the agent, so WP1's frozen hyperparameters no longer describe the
   agent under test. Arm C has constants WP3 never mentions.
2. §5.3's graded κ changes the environment, and WP2 (environment build, six
   admissibility filters) is still open.

**Recommendation:** keep the existence test intact and register the SCA programme as its
own work package with its own preregistration, sharing `env*` and `s_observer` but not
the WP3 criteria. Freezing WP3 *before* starting the SCA build is the cleaner order —
otherwise the temptation to adjust WP1 constants "while we are in there" is large, and
WP3's whole point is that they are fixed.

---

## 8. Proposed build order for `labyrinth_scope_constructing/`

Fork of `labyrinth_existence_wp1/`. Environment and observer stay **byte-identical**
where possible — §14 is only meaningful if all arms are analysed by the same pipeline.

| Step | Deliverable | Blocks | Notes |
|---|---|---|---|
| 0 | Fork + smoke test reproduces WP1 behaviour | — | establishes C0 as a measured baseline, not an assumed one |
| 1 | `perturb.py`: graded κ wrapper + observation-noise channel η | §4.5, §4.6, 4 | the actual blocker; smallest module with the largest unlock |
| 2 | `arw_adapter.py`: `s_observer` → `PartitionResult.json` + `Invariants.json` (`sweep_range`, `theta_star`) | §4.6 | then `pipeline/transfer_v2.py` runs unmodified |
| 3 | Protocol extension: raw window `X_i`, `S^entry/exit`, `T_i`, `F_i` (§4.4), archetype ids | §4.1 | pure bookkeeping; verify buffer size cost |
| 4 | `recapitulation.py`: passive ℛ over stored windows (δw, δε, δΠ-as-mask) | §4.2 | C2; C1 = identical re-read, same code path with zero variation |
| 5 | `modes.py`: R_m/𝒫_m estimation from step 1's κ/η grid; merge-on-profile-overlap, split-on-bimodality, prune | §4.3, §4.5 | first point where §9.4's criterion (not similarity) is testable |
| 6 | `run_arms.py`: B, C0, C1, C2 with shared seeds and matched library-update counts (§6a) | — | decides Q-SCA-01 |
| 7 | Arm A: prescribed mode library + gating selector per `agent_architecture_mode_ecology.md` §3/§4 | — | last, and deliberately built to be strong |

Steps 0–6 decide the document's own primary question (Q-SCA-01, the cheap negative).
Step 7 is needed only for the full C-SCA claim.

---

## 9. Implementation decisions this analysis surfaces

Not registered as Q-IDs — they are build decisions for Rico, not open research
questions. Numbered for reference in the fork's README.

| ID | Decision | Bears on |
|---|---|---|
| D-1 | Is ε agent-side or observer-only? The architecture document assumes agent-side (§3); WP1 implements observer-only. δε recapitulation requires agent-side. | §4.1, §4.2 |
| D-2 | Which κ (cost scale / visibility / resource budget / noise η) becomes the graded axis — and is the zone-topology comparison kept alongside it? | §5.3 |
| D-3 | Passive-only recapitulation for the first build, or active (re-simulating) as well? | §4.2, Q-SCA-02 |
| D-4 | Library-only recapitulation (§6a) or PPO-coupled (§6b)? Changes what Q-SCA-01's matched control is. | §6 |
| D-5 | Is F kept strictly vector-valued (§4.4), and is that written into the fork's README as an anti-circularity constraint? | §2, §4.4 |
| D-6 | Does arm A get built, or is the first result confined to the C0/C1/C2 ablation? | §3 |
| D-7 | Freeze WP3 before starting, or run both programmes with explicitly separate constants? | §7 |

---

## 10. Findings for the architecture document itself

Three items in `scope_constructing_agent_architecture.md` should be corrected or
annotated independently of whether the fork is built:

1. **§0 table and §5 cite superseded spec sections** (`agent_online_scope.md` §3, §4.1)
   as canonical. WP1 removed labeled triggers, strength grading and the partitioned
   library on purpose. → §2 above.
2. **§14's primary measure Φ is not computable** on an ε-axis behavioral sweep;
   `pipeline/sweep_behavioral.py` says so in its own docstring. Either κ is introduced
   (§5.3) or the primary measure must be restated. → §4.6.
3. **§15's gradient-step matching presupposes a gradient-coupled offline phase** that
   this architecture does not have. The matching currency is library update count unless
   recapitulation is deliberately wired into PPO. → §6.

None of the three touches the substance of C-SCA. All three change what has to be built
before C-SCA can lose.

---

## Maintenance History

- **2026-07-26**: Created. Gap analysis against `labyrinth_existence_wp1/` at Rico's
  direction (agenda decision: gap analysis first, full A/B/C + C0/C1/C2 scope, fork into
  a new folder). Code claims verified by reading `s_online.py`, `s_sleep.py`,
  `policy.py`, `run_experiment.py`, `s_observer.py`, `env_base.py`, `env.py` and by
  grep across the four labyrinth generations; import/run check of the non-PPO modules in
  the sandbox. Pipeline claims verified against `pipeline/sweep_behavioral.py` and
  `pipeline/transfer_v2.py`.
