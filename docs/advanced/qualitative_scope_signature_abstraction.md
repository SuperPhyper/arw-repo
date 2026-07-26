---
status: hypothesis
layer: docs/advanced/
last_updated: 2026-07-11
depends_on:
  - docs/glossary/scope.md
  - docs/advanced/observable_decomposition.md
  - docs/advanced/operator_signature_catalog.md
  - docs/advanced/cross_domain_signature_matrix.md
  - docs/bc_taxonomy/boundary_condition_classes.md
related:
  - docs/advanced/bc_signature_extraction_observables.md
  - docs/notes/cross_scope_causal_construction.md
open_questions:
  - Q-QSC-01: Does a qualitatively-assigned BC signature survive contact with a
    formal pipeline case built for the same system (toy model, actual sweep)?
  - Q-QSC-02: Does qualitative signature-equivalence between two adaptations
    predict successful engineering transfer (adapting one via the other's
    specific mechanism actually works), or only surface resemblance?
---

# Qualitative Scope-Signature Abstraction (QSA)

## 0. Motivation

Every extraction procedure currently in the repo — top-down
(`bc_extraction_method.md`) or bottom-up (`bc_signature_extraction_observables.md`)
— assumes a system that can be swept: a model with parameters, or a dataset
with sweep points. This is the ART pipeline's native evidentiary form.

A large class of candidate ARW instances has no such data and never will:
historical technologies, craft adaptations, institutional designs — solutions
that are documented in prose, artifacts, and practice, not in sweep files.
This is precisely the territory the CDS manifesto names as the actual
bottleneck ("storage is not our bottleneck; recognition is"): the world
already has descriptions of these adaptations. What is missing is a way to
read a *structural* signature off them well enough to compare across domains
without first forcing them through a quantitative model they may never get.

This document defines a **qualitative** counterpart to the two existing
extraction directions — same target (a BC signature over the S1–S5 operator
catalogue), no sweep data required as input.

**This is explicitly a lower evidentiary tier than either existing extraction
method.** It is a hypothesis-generation tool, not a validation tool. See §4.

---

## 1. The Abstraction Problem

Given:
- A prose/structural description of a mechanism (a technology, a facilitation
  design, an institutional rule) — no equations, no sweep data
- The existing operator-signature catalogue (S1–S5) and BC taxonomy
  (Restriction, Coupling, Aggregation, Symmetry Breaking, Dissipation, Forcing)

Produce:
- An abstracted scope tuple Ŝ = (B̂, Π̂, Δ̂, ε̂) — a structural stand-in for the
  real S = (B, Π, Δ, ε), populated by reading the mechanism's description
  rather than measuring a system
- A BC-signature string (e.g. R·D, R·A) assigned via the same
  operation→operator-signature table used in bottom-up extraction

The components are re-read for this qualitative setting as follows:

| Component | Quantitative reading | Qualitative (QSA) reading |
|---|---|---|
| B̂ | Admissible state subspace | The condition class the mechanism is built to handle (e.g. "intermittent high-intensity input", "steady low-gradient flow") |
| Π̂ | Observable / projection | The structural feature the description foregrounds as load-bearing (what the mechanism *does*, stated as an operation) |
| Δ̂ | Admissible perturbations | The variability the design is documented to remain stable under (season, flood magnitude, material substitution) |
| ε̂ | Resolution threshold | Not a numeric distance — a **matching criterion**: two mechanisms are Ŝ-indistinguishable iff their BC-signature strings are identical, independent of surface material/vocabulary |

ε̂ is the load-bearing difference from the quantitative case: there is no
d_Π to threshold. Equivalence is defined directly on the BC-signature
string. This is a real weakening (see §4) — flagged explicitly, not treated
as a stand-in that "amounts to the same thing."

---

## 2. Procedure

```
1. Read the mechanism's core operation in plain language
   ("delay a pulse and release it slowly", "convert a gradient into flow",
   "pool at each stage before passing on")
2. Map the operation to an operator signature via the existing
   Base Operation → Operator Signature → BC Class table
   (docs/advanced/observable_decomposition.md §1, cross_domain_signature_matrix.md)
3. Compose the BC-signature string in the same notation as bottom-up
   extraction (e.g. R³·A·D)
4. Record B̂/Π̂/Δ̂ per §1 as free-text scope fields (not numeric)
5. Compare signature strings across mechanisms:
   - identical string → candidate same-adaptation-class (flag for §4 caveat)
   - structurally distinct string despite domain/surface similarity →
     genuine negative finding (same domain label, different structure)
```

Step 5's negative case is not a failure of the method — it is often the more
useful output. Two things sharing a domain label ("historical water
technology") are not assumed to share a structure; QSA is a filter against
that assumption, not a device for confirming it.

---

## 3. Worked Example — Passive Water Management Across History

Source material: Kaffeehaus session 2026-07-11 (water management concepts
surveyed across regions/eras, discussed toward an adaptive-synergetic house
design; see `docs/notes/research_journal.md` for the session pointer once
logged).

| Mechanism | Core operation (plain language) | Operator signature | BC signature Ŝ_BC |
|---|---|---|---|
| Qanat / karez / falaj / foggara / puquios | Constant-gradient tunnel; continuous gravity-driven flow, no storage | S1 (channel restricts path) ∘ S4 (gradient dissipated into flow along the length) | R·D |
| Petra/Nabataean check-dams; Mulden-Rigolen (modern retention) | Pulse input (flash flood / rain) buffered, released at a bounded rate | S1 (storage capacity bound) ∘ S4 (throttled release) | R·D |
| Agricultural terracing (Andean, Ifugao, Konso) | Stepped basins; each stage pools before overflow to the next | S1 (bench restricts path) ∘ S5 (each stage aggregates before passing on) | R·A |
| Tank-cascade networks (Sri Lanka wewa) | Networked basins, not strictly serial — overflow of one can feed back into system-level balancing | as terracing, plus S2 (basins cross-coupled, not chained) | R·A·C |
| Fog/dew harvesting (Garoé tree, fog nets) | Passive phase change (vapor → liquid) at a temperature/wind-driven threshold | S3 (external gradient drives the transition; not a stored/throttled flow at all) | F (Forcing-dominated; no R·D buffering structure present) |

**Reading the result:** four of five mechanisms collapse onto R·D or its
immediate extension (R·A, R·A·C) — a "buffer-then-release" structure,
regardless of whether the material is rock-cut channel, gravel rigole, or
earthen bench. Fog harvesting does not belong to this cluster at all; it
has no storage/throttle structure, only a threshold-triggered phase change.
This is the kind of result QSA is meant to surface: the domain label
("old water technique") is not doing the classifying — the signature is,
and it disagrees with the label in one case out of five.

---

## 4. Evidentiary Status and the Label-Matching Trap

**QSA output is not equivalent to a pipeline-extracted Σ.** It carries no
persistence measure p : 2^BC → ℝ≥0 (`bc_signature_persistence_and_dominance.md`
§6) because there is no sweep to compute dominance over. A shared BC-signature
string under QSA is weaker evidence of shared generator structure than a
matched Σ from `bc_signature_extraction_observables.md`.

This matters because of the exact failure mode
`cross_scope_causal_construction.md` describes for causal claims:
**label matching is not generator matching.** QSA replaces one coarse label
("both are ancient water technologies") with a finer one ("both have BC
signature R·D") — which is progress, but it is still a label, arrived at by
qualitative reading rather than by generator-level derivation. Two mechanisms
with the same QSA signature are not thereby shown to share a generator; they
are shown to share a *description* of their generator, at whatever
granularity a plain-language reading supports. Treat a QSA match as grounds
to prioritize a system for formal (bottom-up or top-down) extraction — not as
a substitute for it.

---

## 5. Relation to Existing Extraction Methods

```
Top-down (equations available):        bc_extraction_method.md
Bottom-up (sweep data, no equations):  bc_signature_extraction_observables.md
Qualitative (prose only, no data):     this document (QSA)
```

QSA is strictly the weakest of the three and should be the first one
abandoned in favor of either of the others the moment quantitative data
becomes available for a given mechanism (see Q-QSC-01).

---

## Open Questions

- **Q-QSC-01**: Does a QSA-assigned BC signature survive contact with a formal
  pipeline case built for the same system? Candidate test: build a minimal
  toy model of gravity-driven channel flow (qanat structure) and check
  whether bottom-up extraction from its sweep data returns R·D, as QSA
  predicted here without data.
- **Q-QSC-02**: Does QSA signature-equivalence between two mechanisms predict
  successful engineering transfer — i.e., does adapting one mechanism using
  specific design features "borrowed" from another with the same signature
  actually work in practice — or does it only track surface resemblance?
  Candidate test: the German-context transfer discussion in the source
  Kaffeehaus session (qanat-derived passive cooling vs. Mulden-Rigolen
  retention, both R·D) as a first informal case.

---

## Maintenance History

- **2026-07-11**: Created. First draft of the qualitative extraction method,
  worked example from the water-management Kaffeehaus session, and the
  label-matching caveat cross-linked to `cross_scope_causal_construction.md`.
