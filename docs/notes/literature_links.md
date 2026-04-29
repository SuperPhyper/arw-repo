---
status: working-definition
layer: docs/notes/
---

# Literature Links

References relevant to the ARW/ART framework.

---

## Dynamical Systems

- Strogatz, S. (1994). *Nonlinear Dynamics and Chaos* — foundational for regime and bifurcation concepts
- Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence* — source of the Kuramoto model
- Ott, E. (2002). *Chaos in Dynamical Systems* — chaos and scope dominance loss

## Statistical Physics / Coarse-Graining

- Wilson, K.G. (1971). Renormalization group and critical phenomena — formal coarse-graining
- Kadanoff, L. (2000). *Statistical Physics* — block-spin coarse-graining as admissible reduction prototype

## Opinion Dynamics

- Deffuant, G. et al. (2000). Mixing beliefs among interacting agents — bounded confidence model
- Hegselmann, R. & Krause, U. (2002). Opinion dynamics and bounded confidence

## Reinforcement Learning / State Abstraction

- Li, L. et al. (2006). Towards a unified theory of state abstraction for MDPs — RL state abstraction as scope reduction
- Sutton, R. & Barto, A. (2018). *Reinforcement Learning* — policy and value function abstractions

## Cognitive Science / Cognitive Architecture

- Anderson, J.R. (2007). *How Can the Human Mind Occur in the Physical Universe?* — ACT-R as multi-mode processing
- Clark, A. (1997). *Being There* — situated cognition, context-driven processing modes

## Philosophy of Science

- Kuhn, T.S. (1962). *The Structure of Scientific Revolutions* — paradigm shifts as scope transitions
- van Fraassen, B. (1980). *The Scientific Image* — perspectivism, partial observability

---

## Closely Related Frameworks — Regime Partitioning and Coarse-Graining

This section collects literature that addresses regime partitioning, coarse-graining
admissibility, and scope-based reduction most directly. Sources drawn from a
systematic literature review (March 2026) against ARW core concerns. Organized
by four structural strands.

### Strand 1 — Markov Chain Reduction (Coarse-graining, Lumpability, Error Bounds)

- Geiger, B.C. (2026). Information-theoretic reduction of Markov chains. *Computer
  Science Review*. DOI: 10.1016/j.cosrev.2025.100802
  — Survey of coarse-graining vs. model-reduction for Markov chains; covers
  lumpability as special case; useful as meta-map of admissibility criteria.

- Hilder, B. & Sharma, U. (2024). Quantitative coarse-graining of Markov chains.
  *SIAM Journal on Mathematical Analysis*. DOI: 10.1137/22M1473996
  — Formalizes effective dynamics for coarse-grained CTMCs; provides sufficient
  conditions and quantitative error bounds without explicit scale separation.
  Most directly relevant to ARW admissibility criterion and ε-calibration.

- Teza, G. et al. (2025). Coarse-graining via lumping: exact calculations and
  fundamental limitations. arXiv: 2512.11974
  — Identifies when lumping preserves entropy production statistics exactly and
  when information loss is unavoidable. Relevant to observable sufficiency and
  the scope-boundary problem (F5).

- Cardelli, L. et al. (2021). Exact maximal reduction of stochastic reaction
  networks by species lumping. *Bioinformatics*. DOI: 10.1093/bioinformatics/btab081
  — Formal equivalence-relation criterion for macro-species without dynamical loss;
  algorithm for maximal lumping. Relevant to BC-class Aggregation and Q-SIG-01.

### Strand 2 — Coherent / Almost-Invariant Sets (Regime as Weakly Mixing Region)

- Froyland, G. & Padberg, K. (2009). Almost-invariant sets and invariant
  manifolds — connecting probabilistic and geometric descriptions of coherent
  structures in flows. *Physica D*. DOI: 10.1016/j.physd.2009.03.002
  — Connects transfer-operator (probabilistic) and geometric (manifold) views
  of regime structure. Relevant to ARW Restriction BC and coherent-set
  interpretation of regime interiors.

- Froyland, G. et al. (2010). Coherent sets for nonautonomous dynamical systems.
  *Physica D*. DOI: 10.1016/j.physd.2010.03.009
  — Extends almost-invariant sets to non-autonomous systems; relevant to
  Forcing BC (S3) and regime tracking under time-dependent BCs.

- Chemnitz, R., Engel, M. & Koltai, P. (2024/2025). Extracting coherent sets in
  aperiodically driven flows from generators of Mather semigroups. *DCDS-B*.
  DOI: 10.3934/dcdsb.2024149
  — Trajectory-free, operator-based extraction of coherent sets robust under
  small stochastic perturbations. Closest existing work to ARW's Δ-stability
  criterion for regime partition robustness.

### Strand 3 — Parameter Space Decompositions (Regime Maps, Morse Graphs)

- Cummins, B. et al. (2018). DSGRN: examining the dynamics of families of
  logical models. *Frontiers in Physiology*. DOI: 10.3389/fphys.2018.00549
  — Finite decomposition of parameter space; each region carries an identical
  state-transition graph (Morse graph as dynamical summary). Structurally
  closest to ARW's BC-space → regime-partition → adjacency-graph pipeline.
  See also: docs/notes/arw_dsgrn_dialogue_plan.md, open_questions.md Q16.

- Flack, J.C. (2017). Coarse-graining as a downward causation mechanism.
  *Philosophical Transactions of the Royal Society A*. DOI: 10.1098/rsta.2016.0338
  — Operational criteria for when coarse-grained variables become stable and
  "fundamental" (slow timescale, robustness, consensus across estimators).
  Relevant to ARW's concept of admissible observable selection.

### Strand 4 — Structural State Partitions from Observations (Computational Mechanics)

- Shalizi, C.R. & Crutchfield, J.P. (2001). Computational mechanics: pattern and
  prediction, structure and simplicity. *Journal of Statistical Physics*.
  DOI: 10.1023/A:1010388907793
  — Defines causal states as equivalence classes for optimal prediction; ε-machine
  as minimal predictive representation. Relevant to Q13 (partition extraction
  without equations of motion) and observation-based regime definition.

- Rupe, A. & Crutchfield, J.P. (2018). Local causal states and discrete coherent
  structures. *Chaos*. DOI: 10.1063/1.5021130
  — Extends causal states to spatiotemporal fields; unsupervised identification
  of coherent structures from observations. Relevant to Q7 (scope-transition
  detection without ground truth).

- Brodu, N. & Crutchfield, J.P. (2022). Discovering causal structure with
  reproducing-kernel Hilbert space ε-machines. *Chaos*. DOI: 10.1063/5.0062829
  — RKHS-based inference of causal structure robust to measurement noise and
  resolution; finite/infinite-state kernel ε-machines from data. Most directly
  relevant to Q12 (empirical ε specification) and Q13.

---

## Active Research Communities (Forschungslandschaft, March 2026)

These communities represent active connection points identified in a landscape
survey of ARW-adjacent research programs.

- **Operator Inference / Scientific ROM** — Oden Institute, UT Austin.
  Data-driven reduced-order models via operator learning; connects to ARW
  partition pipeline and ART instantiation methodology.

- **Koopman + Control** — AI Institute in Dynamic Systems (UW-led NSF);
  Mezić Research Group (UCSB). Koopman/DMD operator methods for
  nonlinear dynamics; relevant to S4 (Dissipation) and S3 (Forcing) signatures.

- **Mori-Zwanzig / Memory-DL** — Pennsylvania State University; Pacific
  Northwest National Laboratory (Panos Stinis). ML-augmented Mori-Zwanzig
  for non-Markovian memory terms; directly relevant to S5 (Conditional
  Expectation) and non-Markovian extension of ARW scope tuple.

- **Applied Category Theory** — ACT 2026 conference; AlgebraicJulia ecosystem.
  Compositional methods for open systems; relevant to Q-TENSOR-01 and
  the monoidal product extension of ARW primitives.

- **Nichtgleichgewicht / RG** — Max Planck Institute for Physics of Complex
  Systems, Dresden. Non-equilibrium statistical physics and renormalization;
  relevant to S4 (Dissipation) and coarse-graining admissibility.

- **Neural/Representation Collapse** — NeurIPS/ICML workshops (HiLD, NeurReps).
  Collapse of representational geometry in deep networks; structural parallel
  to ARW's Π_local collapse in emergence formalism (CASE-20260318-0004).

---

## ARW Formal Foundations (Felder 2026)

- Felder, R. (2026). *When Does a System Have a Well-Defined State? Cover Stability
  as a Necessary Condition for Observable Information*. April 2026 (v1 + v2).
  — Provides the formal necessary condition for when a descriptive scope sustains
  observable information: the cover C_ε must be non-trivial (ε < ε*(O,X)) and
  Δ-stable (sup_x σ_Δ(x) < ε). Introduces perturbation spread σ_Δ(x) as a named
  formal quantity; the Lipschitz bound on σ_Δ (Corollary 1); the descriptive
  crossover concept (F-gradient); and the multi-observable admissible regime as a
  region in ℝᵏ. Empirically confirmed via Kuramoto and conservative pendulum case
  studies. The foundational layer for ARW's ε-sweep and regime-partition machinery.
  See: docs/core/cover_stability_criterion.md, docs/core/observable_information.md,
  docs/glossary/perturbation_spread.md,
  docs/related_fields/related_fields_and_methodological_connections.md §8.
