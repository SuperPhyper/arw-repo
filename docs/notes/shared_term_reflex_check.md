---
status: note
layer: docs/notes/
depends_on:
  - docs/glossary/scope.md
  - docs/notes/scope_component_conflict_typology.md
  - docs/notes/cross_scope_causal_construction.md
---

# Shared-Term Reflex Check: Flagging Concept Drift Before a Discussion Starts

> **Status note.** Exploratory. Originated in a Kaffeehaus session (2026-07-04),
> as a deliberately lightweight front-end to the conflict typology and the
> cross-scope causal-construction note. This file recaps enough of both to be
> usable on its own; it is not a substitute for either.

## 1. Purpose

The conflict typology classifies a controversy *after* it has broken out. The
level-shift detector (in the causal-construction note) flags a scope jump
*inside* an argument already under way. Both are diagnostic, not preventive.

This note is the step before both: a **two-question reflex**, applied the
moment a term is reused by a second party or reapplied to a new case, meant to
catch drift before it produces an unproductive discussion — not to classify or
resolve anything. It is intentionally coarser and faster than the instruments
it defers to.

## 2. The reflex check (the tool itself)

The moment a term already in use is picked up by another party, or applied to
a new instance, ask exactly two questions:

1. **Same B?** — is the same set of states/cases being referenced, or has the
   selection silently shifted (e.g. one case vs. a population, this system vs.
   an aggregate of systems)?
2. **Same Π?** — is the term computed/derived from the same set of variables,
   or have new or different variables entered (e.g. a new codetermining factor
   now feeds the same-named observable)?

If either answer is **no** or **unclear**, that is the flag — regardless of
what kind of conflict it eventually turns out to be. The purpose of flagging is
not classification; it is a pause: *"we are using the same word, probably not
for the same object — resolve that before continuing."*

**Design constraint, deliberate**: this check is coarser and more lossy than
the four-marker level-shift detector (§3 below). That is intentional. A live
reflex needs to be fast enough to interrupt a conversation before it escalates;
the four-marker detector is precise but retrospective — suited to analyzing a
transcript, not to interrupting one in progress. False positives here are an
acceptable cost; missed drift is not.

## 3. Recap: what to do once the flag fires

This section restates only what is needed to route the flag correctly, without
requiring the other two files to be open.

**From the scope-component conflict typology** (full file:
`scope_component_conflict_typology.md`): once drift is confirmed, classify
which scope-tuple component was actually varied —

| Type | Varied component | Resolution behavior |
|---|---|---|
| ε-conflict | Resolution threshold | Dissolves once aggregation groups are made explicit |
| Δ-conflict | Admissible perturbations | Survives disambiguation — genuine normative dispute |
| Π-conflict | Admissible projections/observables | Not resolvable by measurement; argue projective richness |
| B-conflict | Boundary/state selection | Deepest, least empirically decidable |
| Π-monopolization | (not a tuple component) | One party denies the competing Π's legitimacy rather than disputing it; antidote is naming each Π's B, usage range, and limitation instead of replacing one with the other |

**From the cross-scope causal-construction note** (full file:
`cross_scope_causal_construction.md`): if, in addition to the term itself, a
**causal claim** is being carried across the flagged boundary (not just a
descriptive label), two further things apply —

- Generator identity is undecidable in general from the label alone (same
  principle as Q-REL-05's expected negative resolution) — do not expect the
  flag, or anything else, to *prove* the generators differ.
- A legitimate cross-scope causal claim needs three independently-supported
  parts: (1) a counterfactual mechanism claim at the source scope, (2)
  instance-level signature evidence fixed before inspecting the instance, (3)
  the bridge claim itself, with "undecidable" as a legitimate third outcome —
  not just satisfied/not satisfied.

## 4. Escalation path

```
term reused / reapplied
        │
        ▼
  reflex check (§2): same B? same Π?
        │
   no / unclear ──────────────► flag raised
        │                            │
       yes                           ▼
        │                 is a causal claim being made
        ▼                 across the flagged boundary?
  proceed, no flag           │                    │
                             no                   yes
                             │                    │
                             ▼                    ▼
                  classify via typology   causal-construction note:
                  (§3 table above)        level-shift detector +
                                          three-part construction
```

## 5. Limitations

- This is a heuristic, not a proof procedure. It catches candidates for drift;
  it does not confirm drift, and cannot — see the undecidability point in §3.
- It presupposes the parties are willing to pause and check; it does not help
  in a Π-monopolization situation where one party denies the other a position
  to check from in the first place (see typology, §7) — that needs the
  reconciliation rule, not this reflex.
- Untested as a real-time practice; no instance yet of this check being applied
  live rather than reconstructed after a discussion.

## 6. Open questions

- Can "same B / same Π" be answered quickly enough in live conversation to be
  useful, or does even this reduced form require the kind of reflection that
  only happens after the fact — i.e. is a genuinely preventive version of this
  tool achievable at all, or only a fast-retrospective one?
- Should the two questions be asked separately (B first, then Π) or combined,
  given that a B-shift often silently drags a Π-shift with it (a different
  case selection frequently comes with different available variables)?
- Is there a minimal, non-accusatory phrasing for raising the flag in a live
  discussion that does not itself read as a Π-monopolization move ("you're not
  even talking about the same thing") against the other party?
