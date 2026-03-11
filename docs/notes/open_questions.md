---
status: working-definition
---

# Open Questions

Active unresolved questions in the ARW/ART research program.
Entries are drawn from limitations documents, experiment falsification sections,
and theoretical gaps identified during development.

---

## Formalization

**Q1 — Quantification of admissibility**
Admissibility is currently defined structurally (partition stability under Δ).
Can it be quantified as a continuous measure — an "admissibility degree" —
rather than a binary condition?
Candidates: mutual information between suppressed variables and observables;
Lyapunov exponent under perturbations; PCI as a proxy.

**Q2 — ε as a function of state**
The current formalism treats ε as uniform across X_B.
But near regime boundaries, finer resolution may be needed to resolve
the partition, while bulk states require less.
Should ε be state-dependent? What is the consistent formulation?

**Q3 — Multiple ε for multiple observables**
When Π = {π₁, π₂, ...}, each observable may have a natural resolution scale.
What is the joint admissibility condition?
Is ε a vector, a matrix, or a function on the product space?

**Q4 — Formal relationship between ARW and topological data analysis**
Regime partitions have a topological structure (adjacency, boundary topology).
Is there a formal correspondence between ARW partition types and persistence
homology or sheaf-theoretic descriptions of data structure?

---

## Empirical

**Q5 — Do BC classes generate partition types universally?**
The BC taxonomy predicts that coupling BC generates sequential partitions
across Kuramoto, pendulum, and opinion dynamics.
This is the central empirical hypothesis. Is it borne out?
Under what conditions does it fail? (Network topology variation is the
expected failure mode for coupling — does it generalize?)

**Q6 — What is the scaling exponent for TBS(N)?**
The transition boundary shift is predicted to scale as TBS(N) ~ N^{-α}.
What is α for different BC classes?
Is it universal within a BC class, or system-dependent?

**Q7 — Can scope transitions be detected without ground truth?**
In the labyrinth, scope transitions are detected via salience spikes
and mode switches. But in new domains (without designed zone boundaries),
how would a scope transition be detected from behavioral data alone?
Is there an unsupervised admissibility-loss signal?

**Q8 — Does the mode ecology stabilize, or does it keep growing?**
After sufficient training episodes, does the agent converge to a fixed
number of modes, or does the mode count keep growing?
If it stabilizes, what determines the equilibrium count?

---

## Conceptual

**Q9 — Scope transitions vs. phase transitions: precise relationship**
The framework claims these can coincide but are conceptually distinct.
Are there systematic conditions under which they do coincide?
Is every phase transition a scope transition? Is every scope transition
associated with a phase transition in some dual system?

**Q10 — Is emergence in ARW ontological or epistemic?**
ARW defines emergence as a descriptive event (scope reorganization),
not an ontological claim. But the reorganization is forced by dynamics —
the system itself changes in a way that makes the old description inadmissible.
Where exactly is the boundary between "the description changes" and
"something new comes into existence"? This question is left open deliberately.

**Q11 — BC classes as a complete taxonomy**
The current taxonomy has six classes. Is this complete?
Are there important BC types in social, biological, or cognitive systems
that are not captured by restriction, coupling, symmetry breaking,
dissipation, forcing, or aggregation?

---

## Methodological

**Q12 — How to specify ε empirically**
In the experiment files, ε is set as a hyperparameter (0.05 rad, 0.1 cosine distance).
Is there a principled procedure for deriving ε from data,
consistent with the consistency condition max_{δ ∈ Δ}|Π(x+δ) - Π(x)| < ε?

**Q13 — Partition extraction without known equations of motion**
In the pendulum and Kuramoto, partition extraction can use analytical results.
In the labyrinth and social systems, equations of motion are not available.
What is the general pipeline for partition extraction from trajectory data?

**Q14 — Scope template reuse across domains**
Can an ART scope specification from one domain (e.g., Kuramoto coupling BC)
be transferred to a structurally similar domain (e.g., opinion dynamics coupling BC)
without re-derivation? What is the formal condition for scope template reuse?
