---
status: note
layer: docs/advanced/
title: "Aggregation Limits of Typological Observables: The Variance Crossover Problem"
created: 2026-05-14
depends_on:
  - docs/glossary/scope.md
  - docs/bc_taxonomy/boundary_condition_classes.md
  - docs/advanced/observable_decomposition.md
  - docs/glossary/observable_range.md
related:
  - kht_arw_analysis_revised.md
  - CASE-20260328-0010
note: >
  This document addresses a structural limitation that applies to any typological
  observable — any observable whose admissible range R(π) is defined by membership
  in a discrete type class. It is not KHT-specific. KHT is used as an illustrative
  example throughout, but the formal argument applies to MBTI, Big Five profiles,
  institutional typologies, and any other system that maps a continuous state space
  onto a discrete partition.
---

# Aggregation Limits of Typological Observables: The Variance Crossover Problem

## 1. The Problem

Typological observables assign states to discrete classes — psychological types,
institutional categories, cultural archetypes. Their utility rests on the assumption
that membership in a class is informative: knowing which class a state belongs to
tells you something meaningful about the state.

This assumption holds under a specific condition that is rarely made explicit:

> **The within-class variance of the relevant outcome variable must be smaller than
> the between-class variance.**

When this condition fails — when within-class variance exceeds between-class variance
at a given aggregation level — the typological observable loses its predictive and
descriptive utility at that level, even if it remains valid at other levels.

This is the **variance crossover problem**: there exists a critical aggregation level
N* at which within-group and between-group variance exchange their relative magnitude,
and the observable transitions from informative to structurally uninformative.

This document formalizes the variance crossover in ARW terms, characterizes the
two distinct failure modes it produces, and derives the conditions under which any
typological observable reaches its aggregation limit.

---

## 2. Formal Setup

### 2.1 Typological Observables

Let O be a typological observable with the following structure:

```
O: X → C

where:
  X = state space of the system
  C = {c₁, c₂, ..., cₖ} = discrete class set (the typology)
```

O assigns each state x ∈ X to a class c ∈ C. The observable has resolution ε:
two states x, y are indistinguishable under O if d(x, y) ≤ ε, i.e. O maps them
to the same class.

The **admissible range** R(O) is the set of states x ∈ X_B for which O produces
reliable class assignments — where the class boundaries are stable under the
admissible perturbations Δ specified in the scope tuple.

### 2.2 Aggregation Level

Let the system be embedded in a population or context structure with aggregation
level A:

```
A = 1:          Individual level — single system instance x ∈ X
A = n (small):  Group level — n system instances {x₁, ..., xₙ}
A = N (large):  Population level — N instances, potentially spanning
                multiple contexts or subpopulations
```

At each aggregation level, the observable O produces a distribution over C rather
than a single class assignment. The question is whether this distribution is
informative.

### 2.3 Within-Group and Between-Group Variance

For any outcome variable Y (the quantity the typological classification is supposed
to predict or describe), define:

```
σ²_W(A) = within-group variance of Y at aggregation level A
           (variance of Y among instances assigned to the same class)

σ²_B(A) = between-group variance of Y at aggregation level A
           (variance of Y between class means)
```

The typological observable O is **informative** at aggregation level A if and only if:

```
σ²_B(A) > σ²_W(A)
```

The **variance crossover point** N* is the aggregation level at which:

```
σ²_B(N*) = σ²_W(N*)
```

Below N*, O is informative. Above N*, the class membership contributes less
structuring variance than the variance within classes — the class mean is no better
a predictor of y_i than the population mean, and the type assignment adds no
explanatory power beyond what the population baseline already provides. This does
not mean O is worthless at all levels above N*: it means the *marginal contribution*
of knowing the type, over and above knowing the population distribution, collapses.
The practical utility of the classification becomes strongly scope-dependent and
cannot be assumed to transfer to new contexts without re-estimation.

---

## 3. Why Crossover Occurs: Two Structural Mechanisms

The variance crossover is not a measurement artifact. It arises from two structural
mechanisms that become active at different aggregation levels.

### 3.1 Mechanism 1: Context Heterogeneity Inflates Within-Group Variance

As the scope of a typological study expands to include more diverse contexts
(different environments, cultural settings, institutional frameworks), the behavior
of instances within the same class becomes more variable — because the class
definition does not capture context-sensitivity.

Example: An "NJ-type" individual in a high-autonomy academic environment shows
systematically different behavioral vectors than an "NJ-type" individual in a
high-constraint bureaucratic environment. Both are correctly typed, but their
behavioral outcomes differ enough to inflate σ²_W to the point where it
approaches or exceeds σ²_B.

The typological observable was designed to describe structure that is
context-independent (the persistent profile). But any behavioral outcome variable
Y has context-dependent components that the observable does not capture. As context
diversity increases with aggregation level, the context-dependent variance component
grows, inflating σ²_W.

### 3.2 Mechanism 2: Population Heterogeneity Compresses Between-Group Variance

As the scope expands to cover more heterogeneous populations, the class frequency
distribution flattens — more types are represented in more equal proportions, and
the class means of Y converge. This compresses σ²_B.

The intuition: in a highly homogeneous group (e.g. a specific professional cohort),
type differences may produce large outcome differences because the group shares
many contextual variables that amplify type-specific effects. In a maximally
heterogeneous population, these amplification effects cancel out, and σ²_B shrinks
toward zero.

### 3.3 The Crossover as a Structural Property, Not a Measurement Failure

Critically, neither mechanism represents a failure of the typological model or of
the measurement instrument. The crossover is a structural consequence of applying
a fixed-resolution observable across varying aggregation levels.

This is analogous to the relationship between microscopic and macroscopic
descriptions in physics: a molecular model is correct at the molecular level but
loses predictive utility for bulk thermodynamic properties — not because the model
is wrong, but because the relevant variables at the bulk level are not individual
molecular states.

---

## 4. ARW Formalization: Two Failure Modes

The variance crossover produces two distinct ARW failure modes, which must be
distinguished because they have different remedies.

### 4.1 Failure Mode A: F1 at the Aggregation Level

**Condition:** The observable O is applied at aggregation level A > N*, where
within-group variance dominates.

**ARW characterization:** This is an **F1 failure** (cover too coarse). The
effective resolution of O at this aggregation level is:

```
ε_effective(A) = ε_individual × f(A)

where f(A) is a monotonically increasing function of aggregation level
under the null hypothesis of uniform context heterogeneity increase.
In populations with hierarchical structure, f(A) may be non-monotone
(see §10.1), and F1 may not apply at all aggregation levels above N*.
```

As A increases, ε_effective grows: states that were distinguishable at the
individual level become indistinguishable under the aggregated class assignment.
The cover becomes trivial — all instances within a class are treated as equivalent
despite having outcome variance that exceeds between-class variance.

**Observable sufficiency condition:** O is sufficient for outcome Y at aggregation
level A only if:

```
ε_effective(A) < d_min(Y)

where d_min(Y) is the minimum distinguishable difference in Y that is practically
significant.
```

When this condition fails, O provides no useful discrimination at level A.

**Remedy:** Reduce aggregation level (return to the individual or small-group scope
where O remains informative), or introduce a finer observable that captures the
context-dependent variance component.

### 4.2 Failure Mode B: Z_shared — Scope Boundary Violation

**Condition:** The scope B is defined at aggregation level A > N* and treated as
a single homogeneous system, when in fact it contains multiple structurally
distinct subsystems.

**ARW characterization:** This is a **Z_shared-type scope transition**. The scope
B at aggregation level A does not correspond to a single attractor basin — it
spans multiple attractor basins (the distinct subpopulations with different type
distributions and BC structures). The substrate assumption A0 (the system has a
well-defined state space X_B) is violated: X_B is not homogeneous.

Example: Treating "all individuals in cultural region X" as a single scope B
violates A0 if that region contains subpopulations with systematically different
type distributions (e.g. professional cohorts, age cohorts, urban/rural splits).
The scope is internally heterogeneous; any observable calibrated to the aggregate
will fail for subpopulations that deviate from the aggregate distribution.

**The key distinction from F1:**
- F1: The scope B is valid, but the observable's resolution is too coarse.
  The system is homogeneous; the observable just cannot resolve it adequately.
- Z_shared: The scope B is invalid — it conflates structurally distinct subsystems.
  No observable calibrated to the aggregate can be expected to be informative
  for individual subsystems.

**Remedy:** Decompose the scope B into subsystem-level scopes B_i where each B_i
corresponds to a structurally homogeneous subpopulation. Apply O within each B_i
separately. The aggregate is then a distribution over subsystem-level results,
not a single class assignment.

---

## 5. The Crossover Point N* as a Scope Parameter

The crossover point N* is not a universal constant — it is a property of the
specific typological observable O, the outcome variable Y, and the context
structure of the population. It must be treated as a **scope parameter** that
belongs in the scope tuple:

```
S = (B, Π, Δ, ε)

Extended to include aggregation constraint:
B must specify: aggregation level A < N*(O, Y, context_structure)
```

This means: any scope claiming to apply a typological observable O must
explicitly state the maximum aggregation level at which O remains informative
for the intended outcome variable Y. Claims about O's validity that do not
specify this bound are underspecified.

### 5.1 Estimating N*

N* cannot be determined analytically from the typological model alone — it
depends on empirical variance structure of the population. However, it can be
bounded:

**Lower bound on N*:** The smallest group size at which σ²_W approaches σ²_B.
This can be estimated from pilot studies comparing type-outcome relationships
across samples of varying size and heterogeneity.

**Upper bound on N*:** If the typological observable is theoretically grounded
in individual-level mechanisms (as in KHT: persistent profiles arising from
individual biological BCs), then N* is bounded above by the point at which
the theoretical individual-level mechanism no longer drives outcomes — i.e.
where contextual factors dominate.

### 5.2 N* is Observable-Specific

Different observables O have different crossover points:

| Observable type | Expected N* behavior |
|---|---|
| Fine-grained individual (O1: behavioral vectors) | Low N* — highly context-sensitive, crossover occurs early |
| Categorical type label (O3: modulator cluster) | Medium N* — less context-sensitive than behavioral vectors |
| Aggregate trait score (O2: OCEAN profile) | Higher N* — statistical averaging already smooths context effects |
| Group-level faction type (O4) | N* is defined at the group level; individual crossover does not apply |

This ordering has a direct implication: the more fine-grained the observable,
the earlier the variance crossover, and the more tightly constrained the
maximum admissible aggregation level.

---

## 6. The Ecological Fallacy as a Special Case

The classical **ecological fallacy** — inferring individual properties from
group-level statistics — is a special case of the variance crossover problem
at its most extreme: applying a group-level observable to individual prediction
when A >> N*.

In ARW terms, the ecological fallacy is an **out-of-scope application** of a
group-level observable to individual states. The observable O_group has been
calibrated at aggregation level A_group; applying it to individual states at
level A = 1 violates the B-constraint of the scope within which O_group is valid.

The variance crossover framework generalizes this: the ecological fallacy is
not the only failure mode. The symmetric failure — applying an individual-level
observable to group-level prediction (the **atomistic fallacy**) — is equally
a scope violation, occurring when A < N*_group where the group-level BC structure
is not yet visible in the individual-level variance.

Both directions of scope violation are characterizable within ARW as B-constraint
violations at the wrong aggregation level.

---

## 7. Implications for Study Design

Any empirical study using typological observables should specify:

**Required scope parameters:**

1. **Target aggregation level A:** individual, dyad, small group, organization,
   population. This determines which observables are admissible.

2. **Estimated N* for the intended observable and outcome variable:** either
   from prior literature or as an explicit hypothesis to be tested.

3. **Context heterogeneity control:** the scope B should specify the context
   structure — if multiple contexts are included, they should be treated as
   separate subsystem scopes B_i rather than a single aggregated scope.

4. **Cross-level inference restrictions:** results valid at level A should not
   be extended to inferences at level A' ≠ A without explicit re-scoping
   and re-calibration of N*.

**Design recommendation:** For any typological model, the first empirical study
should not ask "does the typology predict Y in this population?" but rather
"at what aggregation level does the typology's predictive utility for Y peak,
and at what level does it cross over into uninformativeness?" This characterizes
the scope structure before substantive hypotheses are tested.

---

## 8. Application to KHT: Scope Validity Across Levels

KHT is used here as an illustrative example. The variance crossover analysis
yields the following scope structure for KHT observables:

| Aggregation level | KHT observable status | Primary failure risk |
|---|---|---|
| Individual (A=1) | O1, O3 fully admissible within B_Layer2 | F-gradient near regime boundaries |
| Dyad / small group (A=2–12) | O1, O3 admissible; O4 (faction type) becomes relevant | Coupling structure must be specified in B |
| Organization / cohort (A=13–~200) | O4 admissible; O1, O3 require within-cohort subsystem decomposition | F1 risk for O1 if context heterogeneity is high |
| Cultural region (A >> 200) | All individual observables approach variance crossover | Z_shared risk: cultural region is not a homogeneous scope |
| Cross-cultural comparison | Between-culture B-structure must be explicitly specified | Ecological fallacy risk if individual-level conclusions are drawn |

**Key implication:** The statement "KHT types can describe cultural regions" is
technically not false — a type *distribution* can be estimated for any population.
But this distribution loses individual predictive utility above N*, and cultural-
region-level type assignments carry the same epistemic status as population-genetic
ancestry assignments: informative for statistical descriptions of group-level
differences, uninformative for individual-level predictions within the group.

The within-group variance of individual cognitive profiles within any cultural
region will, under realistic population structures, substantially exceed the
between-group variance between cultural regions — just as within-ethnic genetic
variance substantially exceeds between-ethnic genetic variance for almost all
genetic traits except those under strong directional selection.

---

## 9. Summary

The variance crossover problem is a structural feature of all typological
observables, not a defect of any particular typological model. It states:

1. Every typological observable has a **crossover point N*** beyond which
   within-group variance exceeds between-group variance, rendering the
   observable structurally uninformative at that aggregation level.

2. The crossover produces two distinct ARW failure modes: **F1** (cover too
   coarse, observable still technically valid but uninformative) and
   **Z_shared** (scope B is heterogeneous, substrate assumption A0 violated).

3. The crossover point N* is a **scope parameter** that must be specified
   explicitly in any scope claiming to apply a typological observable.

4. The **ecological fallacy** and its symmetric counterpart (the atomistic
   fallacy) are special cases of cross-level scope violations in the ARW framework.

5. Typological models with strong individual-level theoretical grounding
   (such as KHT) are most informative at the individual and small-group level,
   and should not be extended to population-level predictions without explicit
   re-scoping and empirical N*-estimation.

6. The **Aggregation Stability Measure (ASM)** (§10) provides a concrete path
   from qualitative criterion to quantitative instrument: the Variance Ratio
   Profile V(A) = σ²_B(A) / σ²_W(A) tracks observable informativeness across
   aggregation levels; N* is the zero-crossing; and the full ASM tuple
   {N*_median, N*_CI, N*_IQR, V_slope, N*_adjusted} converts the variance
   crossover into a reportable scope parameter. The ASM is structurally
   equivalent to tracking ICC across aggregation levels, making it computable
   with standard multilevel modeling infrastructure.

The ARW framework provides the formal vocabulary to make these limitations
explicit and testable — converting a vague intuition about "aggregation problems"
into a precise scope parameter that belongs in every empirical study design.

---

## 10. Toward an Aggregation Stability Measure (ASM)

The preceding sections establish a qualitative framework. This section sketches
the transition to a quantitative instrument — an **Aggregation Stability Measure
(ASM)** that converts the variance crossover from a philosophical criterion into
a computable property of any typological observable applied to any population.

This section is a formal research agenda, not a completed method. It identifies
the required components, their estimation strategy, and the open problems that
remain before ASM can be applied as a standard study design tool.

---

### 10.1 The Variance Ratio Profile

The core object of the ASM is the **Variance Ratio Profile** V(A): the ratio of
between-group to within-group variance as a function of aggregation level A.

```
V(A) = σ²_B(A) / σ²_W(A)

Interpretation:
  V(A) > 1:  Observable O is informative at aggregation level A
  V(A) = 1:  Crossover point — N* = A
  V(A) < 1:  Observable O is uninformative at aggregation level A
```

**Construction of V(A):**

Given a dataset of N individual observations {(xᵢ, yᵢ)} where xᵢ ∈ X is a
system state and yᵢ ∈ ℝ is the outcome variable of interest:

1. Apply the typological observable O to assign each xᵢ to a class c ∈ C
2. At each aggregation level A ∈ {1, n₁, n₂, ..., N}:
   a. Partition the dataset into groups of size A by random sampling or
      natural grouping (e.g. teams, cohorts, geographic units)
   b. Compute within-group variance: σ²_W(A) = E[Var(y | O(x) = c, group of size A)]
   c. Compute between-group variance: σ²_B(A) = Var(E[y | O(x) = c])
   d. Record V(A) = σ²_B(A) / σ²_W(A)
3. Plot V(A) as a function of A to obtain the Variance Ratio Profile

**Expected shape of V(A):**

Monotonically decreasing V(A) — starting above 1 at small A, crossing 1 at N*,
and approaching 0 asymptotically — is the **null hypothesis** for a simple
typological observable in a population with uniformly increasing context
heterogeneity. It is not a structural guarantee.

In practice, V(A) may deviate from this baseline shape. Each deviation pattern
carries its own interpretation:

- **Monotone decreasing, single crossing at N***: null hypothesis holds —
  context heterogeneity increases smoothly with aggregation; N* is well-defined
- **Non-monotone V(A)**: the observable has multiple informative ranges at
  different scales, indicating multi-level structure in the population. N* may
  be multiply-defined or ill-defined as a single crossover point. This is not
  a failure of the observable but a structural property of the system that
  the single-N* model cannot capture.
- **V(A) never crosses 1**: the observable is informative at all tested
  aggregation levels (N* > max tested A — the observable is more robust than
  the null hypothesis predicts)
- **V(A) < 1 for all A**: the observable is uninformative at every tested
  level (the typology does not capture the relevant outcome variance at any
  scale — or the outcome variable Y is poorly matched to the typology)

The non-monotone case deserves special attention: real populations often have
hierarchical structure (individuals within teams, teams within organizations,
organizations within sectors) where each level introduces its own BC structure.
V(A) may rise again at institutional or cultural aggregation levels if between-
institution variance is larger than within-institution variance for the outcome
of interest. The null hypothesis of monotone decrease applies only when
population structure is flat — a simplifying assumption that should be tested,
not assumed.

---

### 10.2 Crossover Point Estimation

N* is estimated as the zero-crossing of V(A) - 1. Since V(A) is computed from
finite samples, it requires both a point estimate and a confidence interval.

**Point estimate:**

```
N*_hat = argmin_A |V(A) - 1|

or, if V(A) is smooth enough for interpolation:
N*_hat = A where linear interpolation of V(A) crosses 1
```

**Bootstrap confidence interval:**

Resample the dataset B times with replacement. For each resample b:
- Compute V_b(A) for the same aggregation levels
- Estimate N*_b from V_b(A)

The bootstrap distribution {N*_b} gives the confidence interval:

```
CI_α(N*) = [quantile(N*_b, α/2), quantile(N*_b, 1 - α/2)]
```

**Sensitivity to outcome variable Y:**

N* depends on which outcome variable Y is used. For a typological observable
to be robustly informative, N* should be consistent across a set of theoretically
relevant outcome variables {Y₁, ..., Yₖ}:

```
N*_median = median({N*_Y₁, ..., N*_Yₖ})
N*_IQR    = IQR({N*_Y₁, ..., N*_Yₖ})
```

Small N*_IQR relative to N*_median indicates robustness: the crossover point
is stable across different outcome variables. Large N*_IQR indicates that the
observable's informative range depends heavily on which outcome is of interest —
the scope must be specified jointly for O and Y.

---

### 10.3 Context Heterogeneity Adjustment

The same typological observable applied to two populations of equal size may
have different N* values if the populations differ in context heterogeneity.
A population of academically trained adults in a single institution has lower
context heterogeneity than a general population sample; N* will be higher in
the former.

**Context heterogeneity index H:**

Let H be a measure of context heterogeneity in the population — for example,
the variance of a relevant context variable Z (institutional type, socioeconomic
stratum, geographic region) across the sample:

```
H = Var(Z)  or a normalized version H ∈ [0, 1]
```

**Adjusted crossover point:**

Empirically, if a baseline N*_baseline is known from a reference population with
known heterogeneity H_baseline, the adjusted estimate for a new population with
heterogeneity H_new is approximately:

```
N*_adjusted ≈ N*_baseline × (H_baseline / H_new)
```

This follows from the structural mechanism in §3.1: higher context heterogeneity
inflates σ²_W proportionally, shifting the crossover to smaller A.

This adjustment is approximate and requires calibration. It is offered as a
heuristic for study design, not as a precise formula.

---

### 10.4 The Full ASM

Combining the above components, the Aggregation Stability Measure for a
typological observable O applied to population P with outcome variable set
{Y₁, ..., Yₖ} is the tuple:

```
ASM(O, P, {Yᵢ}) = {
  V(A):         Variance Ratio Profile (the full curve)
  N*_median:    Median crossover point across outcome variables
  N*_CI:        Bootstrap confidence interval for N*_median
  N*_IQR:       Interquartile range of N* across outcome variables
                (robustness indicator)
  V_slope:      Slope of V(A) at A = N*
                (how rapidly the observable loses informativeness
                near the crossover — shallow slope = gradual collapse,
                steep slope = sharp collapse)
  N*_adjusted:  Context-heterogeneity-adjusted crossover point
                for the specific population P
}
```

**Interpretation guide:**

| ASM profile | Interpretation | Recommendation |
|---|---|---|
| High N*_median, small N*_IQR, shallow V_slope | Robust observable — informative over a wide range of aggregation levels and outcome variables | Safe to apply up to N*_adjusted |
| High N*_median, large N*_IQR | Outcome-dependent robustness — informative for some Y but not others | Specify Y jointly with O in scope |
| Low N*_median, steep V_slope | Fragile observable — collapses rapidly above individual level | Restrict to individual or small-group scope; do not aggregate |
| V(A) < 1 for all A | Non-informative observable for this population and outcome set | Revise typology or outcome variable selection |
| Non-monotone V(A) | Multi-scale structure — observable may be informative at individual and institutional levels but not intermediate | Decompose into multiple scopes at different A levels |

---

### 10.5 ASM as a Scope Design Tool

The ASM converts the abstract variance crossover criterion into a concrete study
design recommendation. Before applying any typological observable, a researcher
should:

1. **Run a pilot ASM** on a representative subsample to estimate V(A) and N*
2. **Set the scope B** to restrict aggregation level A < N*_adjusted
3. **Specify the outcome variable set {Yᵢ}** that defines the intended
   informative range of the observable
4. **Report N*_median and N*_IQR** as part of the scope specification,
   alongside B, Π, Δ, and ε

This makes the admissibility of the typological observable explicit and
reproducible — and it converts the question "does this typology work?" into
the more precise question "for which outcome variables, at which aggregation
levels, and with what robustness does this typology remain informative?"

---

### 10.6 Open Problems

The ASM as sketched above has several open problems that require further
development before it can be applied as a standard method:

| ID | Problem | Character |
|---|---|---|
| ASM-1 | The context heterogeneity adjustment (§10.3) is a heuristic. A formal derivation of the N* ∝ 1/H relationship from the variance decomposition structure would strengthen the adjustment. | Theoretical |
| ASM-2 | The bootstrap CI assumes that the dataset is large enough for reliable variance estimation at each aggregation level. For small N, both σ²_W and σ²_B are noisy estimates. Small-sample correction methods are needed. | Statistical |
| ASM-3 | The outcome variable set {Yᵢ} must be specified by the researcher. There is no principled way to choose {Yᵢ} from first principles — the ASM measures stability conditional on this choice. | Conceptual |
| ASM-4 | Non-monotone V(A) profiles require decomposition into multiple informative ranges. The algorithm for detecting and characterizing multi-scale structure in V(A) is not specified. | Algorithmic |
| ASM-5 | The ASM assumes that class boundaries are fixed as A changes. In practice, optimal class boundaries may shift with aggregation level (hierarchical clustering). A version of ASM for adaptive partitions would be more general but substantially harder to compute. | Theoretical / Algorithmic |
| ASM-6 | Relationship to existing variance decomposition methods (ANOVA, ICC, multilevel modeling): the ASM is structurally similar to the intraclass correlation coefficient (ICC) used in multilevel modeling. A formal mapping between ASM and ICC would allow existing multilevel modeling infrastructure to be reused for ASM computation. | Statistical |

**Note on ASM-6:** The intraclass correlation coefficient ICC = σ²_B / (σ²_B + σ²_W)
is a monotone function of V(A) = σ²_B / σ²_W. The variance crossover condition
V(A) = 1 corresponds to ICC = 0.5. The Variance Ratio Profile V(A) is therefore
equivalent to tracking ICC across aggregation levels — which means the ASM can
be computed using standard multilevel modeling packages (lme4, brms, etc.)
without new software infrastructure. N* is the aggregation level at which ICC
drops below 0.5.

This connection to ICC substantially lowers the barrier to empirical implementation
and situates the ASM within an established statistical tradition, while the
ARW framing provides the formal scope-theoretic interpretation that ICC alone
lacks.
