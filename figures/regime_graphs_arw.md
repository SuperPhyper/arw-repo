
# Regime Graphs in ARW

## Purpose

This document introduces **regime graphs** as a useful extension for interpreting
regime partitions within the ARW framework.

While the standard ARW operator extracts **behavioral partitions**, regime graphs
describe the **adjacency and transition structure** between these regimes.

This helps connect ARW with ideas from dynamical systems and bifurcation analysis
without introducing explicit time dynamics.

---

# From Partitions to Regime Graphs

The ARW operator currently produces:

A(S) = R_S

Where:

R_S = set of behavioral regimes (equivalence classes)

However, regimes are rarely isolated. In many systems there exist **admissible
perturbations** that allow transitions between regimes.

This produces a **regime adjacency structure**.

---

# Definition

Given:

S = (B, Π, Δ, ε)

Let:

R_S = {R₁, R₂, ..., Rₙ}

Define a regime graph:

G_S = (R_S , E)

Where edges exist when admissible perturbations allow transitions between regimes.

Edge condition:

An edge between Rᵢ and Rⱼ exists if

∃ x ∈ Rᵢ and δ ∈ Δ such that

δ(x) ∈ Rⱼ

---

# Interpretation

Nodes:
behavioral regimes

Edges:
possible regime transitions under admissible perturbations

This produces a **structural map of behavioral transitions** within the scope.

Importantly this does not require:

- time dynamics
- differential equations
- explicit trajectories

It only uses **reachability under admissible perturbations**.

---

# Relation to Stability Regions

Regimes correspond to **stability regions** under ε-resolution.

Edges represent **transition boundaries** where perturbations move the system
outside one stability region into another.

Thus the regime graph captures:

regime stability + transition possibilities.

---

# Example: ECDL Laser Modes

Consider a laser system with two regimes:

R₁ = multi-mode operation  
R₂ = single-mode operation

Possible structures:

Case A – hysteretic transition

multi-mode ⇄ single-mode

Case B – gradual transition

multi-mode → intermediate → single-mode

Both systems share the same partition but differ in their regime graphs.

---

# Why Regime Graphs Matter

Two systems may share the same regime partition but have different
transition structures.

Partition comparison alone therefore cannot fully describe structural similarity.

Regime graphs allow ARW to distinguish:

- compatible regime partitions
- compatible transition topology
- structural distortion across scopes

---

# Relation to Bifurcation Analysis

In dynamical systems, bifurcation diagrams describe how regimes appear
or disappear as parameters change.

Regime graphs provide a **scope-generalized analogue**:

they describe the connectivity of behavioral regimes induced by boundary conditions.

This allows ARW to relate to concepts from:

- bifurcation theory
- phase transitions
- engineering stability analysis
- complex systems

without requiring explicit dynamical equations.

---

# Summary

Adding regime graphs to ARW provides:

- structural information about regime connectivity
- a bridge to dynamical-systems intuition
- a clearer description of transition topology

The extended interpretation becomes:

A*(S) = (R_S , G_S)

Where:

R_S = regime partition  
G_S = regime adjacency graph

This extension remains compatible with the existing ARW formalism.
