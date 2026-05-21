---
status: hypothesis
layer: docs/notes/
title: "KHT — Pre-Scopal Biological Substrate: Hypotheses and Empirical Questions"
part_of: kht_unified_architecture
depends_on:
  - kht_architecture_layer1.md
  - kht_architecture_layer2.md
created: 2026-05-14
note: >
  This document is deliberately hypothetical. The KHT architecture is designed
  to generate empirically tractable questions, not to assert neurobiological facts.
  All claims below are hypothesis-grade — they identify what would have to be true
  for the architectural commitments of Layer 1 to hold, and what empirical findings
  would confirm or disconfirm them. The nativism/interactionism question regarding
  operator differentiation is explicitly left open.
---

# KHT — Pre-Scopal Biological Substrate: Hypotheses and Empirical Questions

## 1. Framing

The KHT Layer 1 architecture makes a structural commitment: operators (Ni, Si, Ne, Se)
are **independent transformation axes**, orthogonal to the modulator dimensions (T/F,
I/E, J/P). Operators are not reducible to modulator combinations; they process
categorically distinct modes of information through mechanisms that are in principle
separable from the modulator systems that act on their outputs.

This is an architectural claim, not a neurobiological one. But it has neurobiological
*implications* — it entails specific conditions about the biological substrate that
would need to hold for the architecture to be instantiated in a real cognitive system.

This document makes those conditions explicit as hypotheses, and identifies the
empirical questions they generate. The nativism/interactionism question — whether
operator differentiation is genetically programmed or shaped by early experience —
is left deliberately open. The model is designed to make that question tractable,
not to answer it.

---

## 2. The Core Structural Commitment and What It Requires

The independence claim for operators requires that it be **physically possible** to
disturb one operator without disturbing the others. This is a strong condition:
two systems are genuinely independent only if their substrates are at least partially
dissociable — anatomically, developmentally, or functionally.

This generates the following necessary conditions:

### A Note on Candidate Substrates and the Reverse Inference Problem

Before listing candidate substrates, a methodological caveat is necessary.
Neuroimaging research identifies where activation occurs during a cognitive task —
it does not directly establish what a region *does* as its primary function.
Inferring that a region is the substrate of a specific cognitive operation from
its activation during a task associated with that operation is a *reverse inference*:
a logically valid but probabilistically uncertain move. A region active during
"familiarity judgment" tasks may be involved in many processes, familiarity being
one of them.

This caveat applies to all candidate substrates listed below. They are
**entry points for empirical questions**, not confirmations of the KHT operator
taxonomy. Their confidence levels reflect the robustness of the underlying
dissociation evidence, not the strength of the KHT-specific mapping claim.

**Confidence level key:**

| Level | Meaning |
|---|---|
| High | Dissociation is robust and well-replicated; functional characterization is consistent across studies |
| Medium | Dissociation is supported by multiple studies but functional interpretation is contested or not specific to the KHT-relevant operation |
| Low–medium | Activation evidence exists but double dissociations are sparse or the mapping is indirect |

---

### H1 — Anatomical Dissociability of Operator Substrates

> Each operator (Ni, Si, Ne, Se) corresponds to a cortical network or network
> configuration that is at least partially anatomically separable from the others.
> Selective disruption of one operator's substrate (through lesion, developmental
> variation, or pharmacological intervention) should produce selective impairment
> of that operator's transformation without equivalent impairment of the others.

**Biological candidate substrates:**

| Operator | Candidate network | Basis for candidacy | Confidence |
|---|---|---|---|
| **Ni** | Medial PFC / posterior cingulate / hippocampal-entorhinal complex | Contextual recollection, future projection, abstract predictive modeling. Hippocampus supports relational binding and episodic simulation; mPFC supports self-referential and anticipatory processing. | Medium — well-supported for projection/recollection; mapping to Ni specifically is indirect |
| **Si** | Perirhinal cortex / parahippocampal gyrus | Item-level familiarity and recognition memory. Perirhinal lesions selectively impair familiarity (the sense that a stimulus was previously encountered) while leaving recollection relatively intact — a well-replicated double dissociation. Si as discrete referencing — "so war es zuvor", comparison against stored state — maps onto familiarity-based matching rather than contextual recollection. | Medium–high — familiarity dissociation is among the most robust in memory research; reverse inference caveat still applies |
| **Ne** | Posterior parietal / lateral temporal / anterior temporal cortex | Categorical recognition, pattern identification, analogical mapping. Lateral temporal and anterior temporal regions support semantic categorization and conceptual similarity. Ne as identifying topology — placing an instance into a class, recognizing a pattern as an instance of a type — maps onto categorical and similarity-based processing. | Low–medium — categorization networks are less cleanly dissociated than MTL memory systems; anterior temporal involvement in semantic processing is robust but not Ne-specific |
| **Se** | Sensorimotor cortex / superior colliculus / anterior insula | Real-time stimulus gradient detection, saliency mapping, action-readiness data. Insula supports interoceptive and interceptive awareness of dynamic bodily/environmental states; superior colliculus drives rapid spatial orienting. | Medium — somatosensory and motor systems are anatomically well-defined; the Se-specific functional claim (gradient detection, not just sensory processing) is less directly testable |

**Operator assignment note — Si vs. Ne:**
The original assignment placed familiarity-based comparison under Si and
categorical recognition under Ne. This is consistent with the KHT operator
definitions: Si generates *discrete state representations* for comparison
("this is the same/different from before"), while Ne generates *topological
identifications* ("this is an instance of class X"). The neuroscientific
literature supports this distinction: familiarity-based recognition (Si-analog)
involves perirhinal matching against stored item representations, while
categorical recognition (Ne-analog) involves lateral/anterior temporal
similarity-based classification. These are empirically dissociable processes
operating on partially distinct substrates.

**What this hypothesis requires empirically:**
Double dissociations between operator pairs in neuropsychological or developmental
populations. Priority pairs for empirical investigation:

- Ni vs. Se: abstract projection impairment without real-time gradient impairment,
  and vice versa (broadly consistent with known anterior-posterior gradients)
- Si vs. Ne: familiarity impairment without categorical recognition impairment,
  and vice versa (partially supported by perirhinal vs. anterior temporal
  dissociation literature, but not tested in KHT-specific task designs)

The mapping onto KHT-specific operator boundaries has not been directly tested
in any existing study.

---

### H2 — Global Reach of Modulator Substrates

> The modulator systems (T/F, I/E, J/P) operate on neural substrates that have
> global reach across the operator networks. They modulate the *processing mode*
> of operator networks without being constitutive of any single operator's
> transformation.

**Biological candidate substrates:**

| Modulator | Candidate system | Basis for candidacy | Confidence |
|---|---|---|---|
| **T/F** | Dorsolateral PFC (T-pole: structural consistency evaluation) vs. ventromedial PFC + anterior insula (F-pole: contextual / relational / affective evaluation) | Well-documented functional dissociation between rule-based and value/affect-based evaluation in prefrontal cortex. Both systems project broadly across cortical networks. | Medium — dissociation is robust; interpretation as T/F-analog is plausible but contested; DLPFC and VMPFC are involved in many processes beyond evaluation |
| **I/E** | Default Mode Network (I-pole: internal orientation, self-referential processing) vs. Task-Positive Network / dorsal attention network (E-pole: external orientation, environmental engagement) | One of the most replicated large-scale network dissociations. DMN is consistently associated with internally directed cognition; TPN with externally directed attention. The anticorrelation is robust across many task conditions. However, recent evidence shows DMN subcomponents activate during externally demanding tasks (e.g. task switches between domains), complicating a simple internal/external mapping. | Medium–high for the gross dissociation; medium for the specific I/E interpretation — the "task-negative" characterization of DMN is an oversimplification |
| **J/P** | Dorsolateral PFC / basal ganglia goal-directed circuits (J-pole: convergent closure, action selection) vs. anterior cingulate cortex / orbitofrontal cortex (P-pole: conflict monitoring, exploratory evaluation, open updating) | Consistent with the cognitive control vs. exploration-exploitation literature. The basal ganglia-PFC circuit supports action selection and goal maintenance (J-analog); ACC and OFC support conflict detection and flexible updating (P-analog). | Medium — functional roles are broadly consistent; reverse inference is particularly problematic here as ACC and DLPFC are among the most multiply-recruited regions in all of cognitive neuroscience |

**Modulator-specific caveats:**

- **T/F**: The DLPFC/VMPFC dissociation is well-established as a broad distinction
  between structural-logical and affective-contextual evaluation. However, both
  regions are involved in working memory, decision-making, and social cognition,
  making the T/F-specific mapping an interpretive choice rather than a direct read.

- **I/E**: The DMN "task-negative" label is now known to be an oversimplification.
  DMN subnetworks activate during between-domain task switches and complex
  internally-generated tasks. The I/E mapping is most secure at the level of
  *resting-state orientation* (what the system does absent specific demands), less
  secure at the level of *moment-to-moment modulation* during active cognition.

- **J/P**: This is the least empirically anchored modulator mapping. The
  convergence/divergence distinction is supported by computational models of
  exploration-exploitation, but a clean neural double dissociation for J/P-analog
  processes is not as well established as the MTL memory dissociation or the
  DMN/TPN anticorrelation.

**What this hypothesis requires empirically:**
Each modulator system should show evidence of operating across operator-substrate
boundaries — the same modulator variation (e.g. DMN vs. TPN dominance) should be
observable regardless of which operator transformation is currently running.
This is the KHT-specific test that no existing study has performed: modulator
state should be orthogonally manipulable with respect to operator activation.

---

### H3 — Operator Agnosticism with Respect to Modulator State

> The activation of an operator substrate does not require or entail a specific
> modulator state. An operator can run under any modulator cluster. Formally:
> the probability of operator O being active is independent of the current
> modulator cluster M.

This is the sharpest independence claim. It says: you can do Ni-type processing
(abstract projection) whether you are in a T-evaluating or F-evaluating mode,
whether you are internally or externally oriented, whether you are converging or
diverging. The modulator colors the output; it does not gate the operation.

**What this hypothesis requires empirically:**
Tasks designed to isolate a specific operator transformation (e.g. a task requiring
abstract projection — Ni-analog) should be executable under experimentally
manipulated modulator states (e.g. induced internal vs. external attentional
orientation). Performance quality may differ across modulator states (the modulator
affects how well the operator output is processed), but the transformation itself
should not be blocked by any modulator configuration.

**Where this is most likely to fail:**
Extreme modulator states may effectively gate operator access — e.g. very high
external orientation (strong E-pole) may suppress internally-anchored projection
(Ni-I combination) below functional threshold. This would not violate the
architecture if it is understood as a *threshold effect* rather than a *structural
dependency*: the operator substrate is accessible in principle but below activation
threshold under extreme modulator conditions.

---

### H4 — Developmental Sequence: Operator Differentiation Precedes Modulator Coupling

> Operator substrates differentiate from one another earlier in development than
> the modulator systems achieve their full coupling reach. The sequence is:
>
>   Phase 1: Operator substrates develop functional specialization
>            (cortical arealization, sensory-motor differentiation)
>   Phase 2: Modulator systems mature and establish global coupling
>            to operator substrates (PFC maturation, large-scale network integration)
>   Phase 3: Biological BCs (Layer 2 Restriction + Dissipation) consolidate
>            the persistent profile within the now-structured operator × modulator space

**Basis for this hypothesis:**
Cortical arealization and primary sensory/motor differentiation are known to
precede prefrontal maturation developmentally. The DMN reaches mature functional
connectivity relatively late (adolescence). This is consistent with operators
becoming functionally distinct before modulators achieve their full global coupling
reach.

**What this hypothesis requires empirically:**
In early developmental stages (infancy / early childhood), operator-specific
behavioral signatures (e.g. preference for concrete vs. abstract information
processing) should be observable before modulator-specific signatures (e.g.
systematic T vs. F evaluative style) stabilize. The developmental trajectory
of operator differentiation and modulator stabilization should be temporally
dissociable.

---

### H5 — Biological BCs Break the Layer 1 Symmetry

> The symmetric operator–modulator space of Layer 1 is not the operating state
> of any actual human cognitive system — it is the formal null model. Biological
> boundary conditions (Layer 2) break this symmetry in two phases:
>
>   Restriction (Phase 1): genetic connectivity biases make certain
>     operator × modulator combinations more consolidatable than others
>   Dissipation (Phase 2): Hebbian learning within the Restriction-filtered
>     space converges on a dominant attractor (the persistent profile)

This hypothesis is agnostic about the nativism/interactionism question:

- **Nativist version:** Restriction is primarily genetic — the accessible profile
  subspace X_B is largely determined by heritable connectivity patterns before
  experience acts. Experience (Phase 2 Dissipation) selects within X_B but does
  not shape X_B itself.

- **Interactionist version:** Restriction is partially shaped by very early
  experience — the accessible profile subspace X_B is itself modifiable by
  prenatal environment, perinatal conditions, or early postnatal experience,
  before systematic Hebbian learning begins.

- **Strong nativist version:** Both X_B and the dominant attractor within X_B are
  largely genetically determined. Experience fine-tunes activation weights but does
  not determine the profile identity.

The KHT architecture does not commit to any of these versions. H5 as stated is
compatible with all three. The versions differ in their empirical predictions about
heritability of profile identity, cross-cultural profile distribution, and the
effects of early environmental manipulation.

---

## 3. The Nativism / Interactionism Question

The most epistemically productive question the architecture generates is also the
one it deliberately leaves open:

> **To what degree is the persistent profile (Layer 2) determined by genetic
> factors vs. shaped by early developmental experience?**

This is not a binary question. The architecture suggests a specific *structure*
for the nativism/interactionism debate:

```
Genetic factors → primarily affect Restriction (which profiles are possible)
Early experience → primarily affects Dissipation (which profile is instantiated
                   within the possible set)
Later experience → primarily affects activation weighting within the profile
                   (which cells of the Ego-block are most active)
```

If this structure is correct, then:
- Heritability studies should show higher heritability for **profile identity**
  (which Ego-block) than for **activation weighting** (relative priority within
  the block)
- Cross-cultural studies should show consistent profile identity distributions
  (if Restriction is primarily genetic) or environmentally modulated distributions
  (if Restriction is partly experiential)
- Early intervention studies should be able to shift activation weighting but
  not profile identity (if identity is Restriction-determined) — or both
  (if Dissipation is highly experience-dependent)

These are falsifiable predictions that do not require committing to nativism or
interactionism in advance.

---

## 4. Empirically Interesting Questions Generated

The following questions are generated by the hypotheses above. They are ordered
by epistemic tractability — from most to least immediately testable given current
neuroscientific methodology.

| ID | Question | Relevant hypothesis | Tractability |
|---|---|---|---|
| EQ-1 | Do double dissociations exist between operator pairs (e.g. Ni-impairment without Se-impairment and vice versa) in neuropsychological populations? | H1 | High — retrospective analysis of existing neuropsychological literature |
| EQ-2 | Is DMN vs. TPN dominance (I/E analog) observable across operator-specific task conditions (abstract vs. concrete processing tasks)? | H2, H3 | High — tractable with standard fMRI paradigms |
| EQ-3 | Can operator-specific tasks (abstract projection, concrete comparison, pattern generation, gradient detection) be performed under experimentally manipulated modulator states without qualitative disruption? | H3 | Medium — requires careful task design to isolate operator transformations |
| EQ-4 | Does the developmental trajectory show operator-specific behavioral signatures earlier than modulator-specific evaluative style? | H4 | Medium — requires longitudinal developmental study design |
| EQ-5 | Is profile identity (Ego-block) more heritable than activation weighting within the profile? | H5 | Medium — requires twin/adoption studies with fine-grained cognitive profiling |
| EQ-6 | Do early environmental manipulations (pre/perinatal conditions, early enrichment/deprivation) shift activation weighting, profile identity, or both? | H5 | Low-medium — ethical constraints limit experimental manipulation; natural experiments (e.g. adverse early environments) are a possible avenue |
| EQ-7 | Is the four-operator taxonomy neurobiologically exhaustive — are there cognitive transformations that do not reduce to Ni, Si, Ne, or Se? | H1 | Low — requires comprehensive neurocognitive taxonomy effort |
| EQ-8 | What is the functional form of the coupling function g(xⱼ) between modulator oscillators (§3.5.1 of Layer 1)? | H2 | Low — requires continuous measurement of modulator state dynamics, currently not methodologically standard |

---

## 5. What the Architecture Does Not Claim

To prevent over-reading, the following are explicitly *not* claims of the KHT
pre-scopal substrate model:

- **Not a claim about specific cortical areas.** The candidate substrates in §2
  are illustrative hypotheses, not anatomical assertions. The architecture is
  compatible with multiple substrate mappings as long as the dissociability
  and global-reach conditions hold.

- **Not a claim about operator universality across species.** The four-operator
  taxonomy is proposed for human cognition. Whether analogous structures exist
  in other species is an open evolutionary question that the architecture does
  not address.

- **Not a claim that profiles are fixed for life.** The Layer 2 distinction between
  profile identity (stable) and activation weighting (modifiable) explicitly
  allows for developmental change in weighting throughout life. Profile identity
  is claimed to be stable in the adult adaptation phase; it is not claimed to be
  immutable under all conditions.

- **Not a commitment to nativism.** The architecture is designed to make the
  nativism/interactionism question tractable, not to answer it in advance.
