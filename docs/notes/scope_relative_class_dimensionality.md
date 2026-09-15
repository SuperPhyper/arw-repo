---
status: note
layer: docs/notes/
created: 2026-09-16
depends_on:
  - docs/glossary/scope.md
  - docs/glossary/regime_partition.md
  - docs/glossary/partition.md
  - docs/core/cover_stability_criterion.md
  - docs/core/arw_scope_reduction_partition_criterion.md
  - docs/glossary/perturbation_spread.md
  - docs/notes/general_regime_construction.md
related:
  - docs/notes/scope_fibration.md
  - docs/notes/description_atlas_programme.md
  - docs/notes/total_description_space.md
  - docs/glossary/coarse_graining.md
  - docs/advanced/epsilon_and_scope_resolution.md
---

# Scope-Relative Class Dimensionality

**Level: ARW.** All statements in this note are domain-neutral. The social and
organisational instantiations previously carried in this note have been moved to
`compromise_as_scope_minimization.md` (Part II).

This note merges two earlier drafts ("Scope-Relative Dimensionality, Relations, and
Non-Atomic Description" and "Scope-Relative Class Dimensionality — Formal
Clarifications"). Only the `cdim` notation is retained; the earlier `d_f` / `d_eff`
notation is dropped to avoid two names for one object.

---

## 1. Purpose

The note proposes a notion of descriptive dimensionality that requires neither a
metric state space, nor continuous coordinates, nor an ontologically fundamental set
of atomic elements. Its intended use is scope analysis in domains where conventional
mathematical dimensionality is unavailable or premature.

The note does **not** claim an extension of the scope tuple. §2 states precisely what
its relation to the canonical tuple is, and which part of that relation is open.

---

## 2. Relation to the canonical scope tuple (and to R_S)

In the canonical tuple

$$
S = (B, \Pi, \Delta, \varepsilon)
$$

no component names classes directly. The **regime partition** $R_S$ is *induced*: the
$\varepsilon$-cover on the observable range, via path-connected components (Čech-cover
construction, `docs/glossary/scope.md`). Throughout this note, the word **partition**
is reserved for $R_S$. The objects introduced below are called *class structures* and
*covers*, never partitions.

This note works with a second object: the class structure $\mathcal{C}_S(D)$ that a
description $D$ explicitly employs. Two readings must be kept apart.

**(a) Induced reading.** $\mathcal{C}_S(D)$ *is* the cover $C_\varepsilon$ produced
from $(B, \Pi, \Delta, \varepsilon)$. Then

$$
\operatorname{cdim}_S(D) = |C_\varepsilon| = N,
$$

and this note introduces no new object — only vocabulary for counting and comparing
what the construction already yields.

**(b) Declared reading.** $\mathcal{C}_S(D)$ is a declared component of the
description, not reconstructible from $(B, \Pi, \Delta, \varepsilon)$ alone. The
relational and non-metric applications below use this reading.

**Open question (unregistered — see §13).** Is reading (b) admissible in ARW at all,
or must every declared class structure be exhibited as induced by some
$(B, \Pi, \Delta, \varepsilon)$? Until this is decided, the note stays at
`status: note` and makes no tuple claim. Where a statement below holds only under
reading (b), it is marked **[declared]**.

---

## 3. Class dimensionality

Let a description $D$ under a scope $S$ employ the class structure

$$
\mathcal{C}_S(D) = \{C_1, \ldots, C_n\}.
$$

Define its **scope-relative class dimensionality**

$$
\operatorname{cdim}_S(D) := |\mathcal{C}_S(D)|.
$$

This must be distinguished from vector-space dimension, manifold dimension,
topological dimension, Hausdorff dimension, and the number of physical degrees of
freedom. $\operatorname{cdim}_S(D) = n$ does not imply that the described object
occupies an $n$-dimensional state space. It states only that $D$, under $S$,
distinguishes $n$ classes.

Class dimensionality is therefore a property of a description under a scope, not an
intrinsic property assigned to the object independently of description. Two scopes may
satisfy

$$
\operatorname{cdim}_{S_1}(D) \neq \operatorname{cdim}_{S_2}(D)
$$

without contradiction: they preserve different distinctions.

**Caveat on cardinality.** $\operatorname{cdim}$ counts classes and is blind to
relational structure among them. Two descriptions with equal $\operatorname{cdim}$ may
differ substantially. §9 states the consequence: $\operatorname{cdim}$ is a *reported
scalar*, not a comparison order.

---

## 4. Typed classes and additive composition

Naive addition $|\mathcal{C}_A| + |\mathcal{C}_B|$ presupposes that the two class
structures are disjoint. This need not hold when both descriptions use identical
labels. For relational descriptions, treat classes as **typed**:

$$
\widetilde{\mathcal{C}}_A = \mathcal{C}_A \times \{A\},
\qquad
\widetilde{\mathcal{C}}_B = \mathcal{C}_B \times \{B\},
\qquad
\widetilde{\mathcal{C}}_R = \mathcal{C}_R \times \{R\}.
$$

The complete class structure is the disjoint union

$$
\mathcal{C}_{A,R,B}
= \widetilde{\mathcal{C}}_A \sqcup \widetilde{\mathcal{C}}_B \sqcup \widetilde{\mathcal{C}}_R,
$$

and therefore

$$
\operatorname{cdim}(A,R,B)
= \operatorname{cdim}(A) + \operatorname{cdim}(B) + \operatorname{cdim}(R).
$$

Additivity is not inherited from set union; it follows from the explicit typing.

---

## 5. Minimal relational dimensionality

An explicit relational description requires at least one relational class,
$\mathcal{C}_R \neq \varnothing$, hence $\operatorname{cdim}(R) \geq 1$ and

$$
\operatorname{cdim}(A,R,B) \geq \operatorname{cdim}(A) + \operatorname{cdim}(B) + 1.
$$

The additional class dimension is **not** a new physical degree of freedom. A relation
may be fully derivable from properties of its relata and still constitute a class of
the description:

$$
\text{derivability} \neq \text{descriptive identity}.
$$

This is the same distinction that appears elsewhere in the repo as *observable BC
structure $\neq$ system BC structure*: what a description separates is not fixed by
what the system determines.

---

## 6. Stability and level

A relation contributes to the class structure, $R \in \mathcal{C}_R$. Stability
concerns whether the relational classification is preserved under an admitted
perturbation family $\Delta$:

$$
R(A,B) \xrightarrow{\ \Delta\ } R(A',B').
$$

The earlier drafts asserted flatly that stability adds no dimension. That is only half
correct, and as stated it contradicts §11 (where stable relations *become* classes).
The level-indexed form:

- At the level at which stability is **tested**, it adds no class. It is a predicate
  about a classification already present, not an element of $\mathcal{C}$.
- At any level that **reifies** it — a description that distinguishes stable from
  unstable relations — stability is a class like any other, by the §5 principle. Two
  classes, `stable-R` and `unstable-R`, appear in $\mathcal{C}$.

Stated without the level index the two readings collide. The recursive architecture of
§11 depends on the second reading and is strengthened, not weakened, by making it
explicit.

---

## 7. Resolution: three multiplicities, one of them generalised here

$\varepsilon$ carries three distinct multiplicities. They must not be conflated
(`docs/notes/general_regime_construction.md` §2.2; Q-EPS-01/03).

1. **Across observables.** $\varepsilon_i$, one per $\pi_i \in \Pi$. A single numeric
   $\varepsilon$ across observables with different units is **ill-formed** without a
   declared normalisation. *Unaffected by this note; still required.*
2. **Across the domain.** $\varepsilon_i(x)$ (e.g. reading-dependent accuracy). Needs a
   declared symmetrisation; $\min(\varepsilon(x), \varepsilon(y))$ is the conservative
   default. *Unaffected by this note; still required.*
3. **Across resolution.** The family $\{S_\varepsilon\}$, $I_\varepsilon$,
   $\eta = -\log(\varepsilon/\varepsilon_0)$ — the refinement axis of the fibration.

**This note generalises (3) only.** Let resolution belong to an ordered set

$$
\varepsilon \in E,
\qquad
\varepsilon_1 \preceq_E \varepsilon_2
\ \ \text{iff}\ \
\varepsilon_1 \ \text{distinguishes at least everything}\ \varepsilon_2 \ \text{does}.
$$

Numerical tolerance is the special case $E \subseteq \mathbb{R}$ with the usual order.
The essential structure is refinability, not numerical magnitude. This is what makes
$\varepsilon$ usable where no metric on the descriptive space is available.

Nothing here settles (1) or (2). A non-metric scope with $|\Pi| > 1$ still owes a
declared composition rule (§8) and a declared normalisation.

---

## 8. Tolerance structure and the effective classification

Write $T_{\Delta,\varepsilon}$ for the declared tolerance structure:
$C_i \, T_{\Delta,\varepsilon} \, C_j$ means the distinction between $C_i$ and $C_j$ is
not stably resolved under the declared perturbation and resolution conditions.

A tolerance relation may be reflexive and symmetric but **not** transitive. Then
$\mathcal{C}/T$ is not an ordinary quotient, and the effective classification must be
produced by an explicitly declared operation

$$
\mathcal{C}_{\mathrm{eff}} = \mathfrak{C}\!\left(\mathcal{C}_S(D), T_{\Delta,\varepsilon}\right).
$$

**The choice of $\mathfrak{C}$ is part of the scope and must not be hidden.** Three
constraints on that choice, which the earlier draft listed as free options:

- The repo already names the two principal rules: **Rule A** (joint graph) and
  **Rule B** (common refinement). Use those names. They differ as soon as the base is
  not a 1D path, and Rule B classes need not be connected — Rule B therefore requires
  a stated reason.
- **Connected components of a tolerance graph re-introduce the sorites collapse** that
  the cover construction was adopted to avoid: a chain of pairwise-tolerant classes
  collapses everything on the chain. This is not an option on a par with the others.
  The all-pairs form $G_\varepsilon(O)$ in `docs/core/cover_stability_criterion.md`
  carries the sorites justification; a consecutive-neighbour form does not.
- Doc↔code caveat: `pipeline/epsilon_multi_observable.py` implements the
  common-refinement rule (Rule B), not the joint-graph rule (Rule A), and sweeps only
  the diagonal $\varepsilon_1 = \varepsilon_2$. Do not cite it as a joint
  $(\varepsilon_1, \varepsilon_2)$ construction.

---

## 9. Effective class dimensionality

$$
\operatorname{cdim}^{\mathrm{eff}}_S(D)
= \left| \mathfrak{C}\!\left(\mathcal{C}_S(D), T_{\Delta,\varepsilon}\right) \right|,
\qquad
\operatorname{cdim}^{\mathrm{eff}}_S(D) \leq \operatorname{cdim}_S(D)
$$

in ordinary cases. The difference measures how much of the formally available
distinction structure collapses at the selected scope. The formal description need not
change; what changes is which of its distinctions remain effective.

**Ordering, not counting.** Because $\operatorname{cdim}$ is blind to relational
structure (§3), comparisons between descriptions should be made with respect to the
refinement order $\preceq_E$ and the induced refinement relation on class structures,
with $\operatorname{cdim}$ reported alongside as a scalar summary. Two class structures
may be incomparable under refinement while having equal $\operatorname{cdim}$; treating
the count as the comparison order silently linearises an order that is only partial.
This has a direct consequence for optimisation over scopes
(`compromise_as_scope_minimization.md` §I.3).

---

## 10. Local elementarity without global atoms

At resolution $\varepsilon$, a class $C_i^\varepsilon$ is **elementary relative to that
description** if the scope makes no further distinction within it. This does not imply
indivisibility: at $\varepsilon' \prec_E \varepsilon$ one may obtain

$$
C_i^\varepsilon \longrightarrow \{C_{i1}^{\varepsilon'}, C_{i2}^{\varepsilon'}, \ldots\}.
$$

Hence

$$
\text{scope-elementary} \neq \text{ontologically atomic}.
$$

**Assumption (A-REF), stated as an assumption, not a possibility.** $E$ has no minimal
element, and for every $\varepsilon \in E$ there is $\varepsilon' \prec_E \varepsilon$
whose class structure *strictly* refines $\mathcal{C}_\varepsilon$.

Under (A-REF), every concrete description may have finite class dimensionality while no
finite bound exists across refinements:

$$
\forall S: \operatorname{cdim}_S(D) < \infty,
\qquad
\sup_S \operatorname{cdim}_S(D) = \infty.
$$

Call this **unbounded class dimensionality**, not "infinite dimensionality":

$$
\text{unbounded class dimensionality} \neq \text{infinite-dimensional state space}.
$$

(A-REF) is a declared property of a description family, not a claim about the world.
Descriptions for which it fails are perfectly admissible; they simply bottom out.

---

## 11. Compression through stable relational structure

Suppose $\operatorname{cdim}(D_0) = N$ is large. If stable relations among these classes
permit them to be represented by higher-order classes,

$$
(C_i, C_j, C_k, R) \longmapsto C'_a,
$$

a higher-level description may satisfy
$\operatorname{cdim}^{\mathrm{eff}}(D_1) \ll \operatorname{cdim}^{\mathrm{eff}}(D_0)$:

$$
\text{fine classes} \rightarrow \text{stable relations} \rightarrow \text{higher-order classes} \rightarrow \text{effective dimensional reduction}.
$$

The higher-order description requires no fundamentally atomic lower level. It requires
only that the lower-level distinctions relevant to its own classification be
sufficiently stable under $\Delta$. This is the level at which stability is *reified*
in the sense of §6.

Iterating in both directions:

$$
\cdots \rightarrow D_{-2} \rightarrow D_{-1} \rightarrow D_0 \rightarrow D_1 \rightarrow D_2 \rightarrow \cdots
$$

with downward movement = refinement and upward movement = relational compression. No
privileged bottom level is required.

**Relation to existing repo constructions — do not re-derive.** The downward direction
is the $\varepsilon$-axis of the scope fibration ($\eta = -\log(\varepsilon/\varepsilon_0)$).
The upward direction is a form of **scope reduction**, which already has an owner in
`docs/core/`. This note contributes the class-counting vocabulary and the level-indexed
stability statement (§6); it should link to those definitions rather than restate them.

---

## 12. Stability without a metric: $\chi$ rather than $\sigma_\Delta$

The canonical perturbation spread

$$
\sigma_\Delta(x) = \sup_{\delta \in \Delta} \left| O(x+\delta) - O(x) \right|
$$

presupposes a metric on the descriptive space. The non-metric formulation used here
asks only whether the **class label is preserved** under $\delta \in \Delta$. That
predicate is the assignment-instability indicator $\chi$, not $\sigma_\Delta$.

Consequence worth recording: in the non-metric setting $\chi$ is the *primitive* and
$\sigma_\Delta$ is merely its metric proxy — the reverse of the operative situation in
the repo, where $\sigma_\Delta$ is computed and $\chi$ is computed nowhere (Q_NEW_26).
Non-metric scopes may therefore be a setting in which $\chi$ has to be faced directly.

**Bias direction (inherited, unchanged).** $\Delta$ is a modelling commitment, not an
instrument property, and no specification supplies it. Under-declaring $\Delta$ shrinks
$\sigma_\Delta$, hence yields *more* stability verdicts: under-declaration is
**anti-conservative**. The clean form is a declared family
$\Delta_{\min} \subseteq \cdots \subseteq \Delta_{\max}$ with verdict stability
required across it.

---

## 13. Relation to existing repo material

Collision check run against HEAD `e9c20fa` (2026-08-07): `cdim`, "class
dimensionality" and "descriptive dimension" return **zero hits** across `docs/`,
`pipeline/` and `schemas/`. The concept is new; no document is superseded.

- The **cover construction and the sorites argument** are owned by
  [cover_stability_criterion.md](../core/cover_stability_criterion.md) and
  [scope.md](../glossary/scope.md). §8 here only adds the requirement that the
  effective-classification operation $\mathfrak{C}$ be declared, and the warning that
  connected components are not a neutral choice of $\mathfrak{C}$.
- The **ε-family, Rule A/Rule B, and the commensurability requirement** are owned by
  [general_regime_construction.md](general_regime_construction.md) §2.2–2.4 and
  registered as Q-EPS-01/02/03. §7 here generalises the *resolution-family*
  multiplicity only (numeric $\varepsilon$ → ordered $(E, \preceq_E)$) and explicitly
  leaves the other two untouched.
- **"Partition"** is owned by [regime_partition.md](../glossary/regime_partition.md)
  and [partition.md](../glossary/partition.md) and refers to $R_S$. This note never
  uses the word for its own objects.
- **Compression / reduction upward** is owned by
  [arw_scope_reduction_partition_criterion.md](../core/arw_scope_reduction_partition_criterion.md)
  and, in the glossary, by [coarse_graining.md](../glossary/coarse_graining.md). §11
  contributes only the level-indexed stability statement (§6), not a new reduction
  mechanism.
- The **refinement ladder** of §10–11 is the ε-axis of
  [scope_fibration.md](scope_fibration.md) /
  [total_description_space.md](total_description_space.md). Not re-derived here.
- **$\chi$ vs $\sigma_\Delta$** (§12): $\chi_{\Delta,\varepsilon}$ is monograph Part VII
  Def 6a and its implementation gap is Q_NEW_26. §12 adds the observation that in a
  non-metric scope $\chi$ is the primitive and $\sigma_\Delta$ has no defined proxy
  role at all — which makes the non-metric case a place where Q_NEW_26 cannot be
  deferred.

---

## 14. Open questions (Q-CDIM, registered here)

*Collision check against HEAD `e9c20fa`: no `Q-CDIM` ID exists anywhere in `docs/`.
Prefix allocated here; mirror these into `docs/notes/open_questions.md` in the same
session.*

**Q-CDIM-01 — Is a declared class structure admissible in ARW?**
Is $\mathcal{C}_S(D)$ under reading (b) of §2 admissible, or must every class structure
be exhibited as induced by some $(B, \Pi, \Delta, \varepsilon)$? *Why it matters:*
blocks promotion of this note above `note`, and decides whether the non-metric
applications are ARW statements or only ART-level modelling conveniences.

**Q-CDIM-02 — Relation of $\mathcal{C}_{\mathrm{eff}}$ to $R_S$.**
Under reading (a), is $\mathcal{C}_{\mathrm{eff}} = R_S$, or does $\mathfrak{C}$ admit
constructions that are not covers? *Bears on:* Q-EPS-02 (composition rule).

**Q-CDIM-03 — Does the non-metric setting force $\chi$?**
If class-label preservation rather than a metric spread is the operative criterion, is
$\sigma_\Delta$ available at all, or must $\chi_{\Delta,\varepsilon}$ be constructed
directly? *Bears on:* Q_NEW_26.

**Q-CDIM-04 — Is $I_\varepsilon$ defined on a non-numeric $E$?**
Under $\preceq_E$ with $E$ only partially ordered, is the ε-plateau
$I_\varepsilon = [\varepsilon_{\min}, \varepsilon_{\max}]$ still well-defined, or does it
become an interval in a partial order — and then possibly non-convex? *Bears on:*
Q-EPS-01.

---

## 15. Summary

- **Dimension is local:** $\operatorname{cdim}_S$ counts the classes a description
  distinguishes under $S$; it is a reported scalar, not a comparison order.
- **Elementarity is local:** $\varepsilon$ determines what is not further
  distinguished; scope-elementary $\neq$ ontologically atomic.
- **Stability is level-indexed:** no class at the level where it is tested; a class at
  any level that reifies it.
- **Compression is recursive:** stable relations may become classes of higher
  descriptions — this is scope reduction, not a new mechanism.

$$
\textbf{Finite local description does not require finite global describability.}
$$

$$
\textbf{Local elementarity does not require global atomicity.}
$$
