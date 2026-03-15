---
status: note
layer: docs/art_instantiations/
---

# ART Instantiations

Concrete ART scope examples: each file specifies a complete
S = (B, Π, Δ, ε) for a real system, following the scope template.

---

## Contents

### Templates and Examples

| Document | Domain |
|---|---|
| [art_scope_template.md](art_scope_template.md) | Blank ART scope template — use this to create new instantiations |
| [art_geopolitical_scope_example.md](art_geopolitical_scope_example.md) | Geopolitical instantiation: Persian Gulf system |
| [arw_littman_bc_analysis.md](arw_littman_bc_analysis.md) | BC extraction: Littman-Metcalf laser (optical engineering) |

### Domain Onboarding Guides

These documents translate ARW vocabulary into the language of specific
research communities, providing a vocabulary table, what ARW adds, where
the tension lies, and a direct case entry point.

| Document | Audience | Primary BC entry point |
|---|---|---|
| [arw_for_synergetics.md](arw_for_synergetics.md) | Synergetics / self-organization (Haken) | CASE-0004 Stuart-Landau |
| [arw_for_game_theory.md](arw_for_game_theory.md) | Game theory / mechanism design | CASE-0002 Multi-Pendel |
| [arw_for_ecology.md](arw_for_ecology.md) | Ecology / population dynamics / resilience | CASE-0007 SIR |
| [arw_for_neuroscience.md](arw_for_neuroscience.md) | Computational / systems neuroscience | CASE-0009 Stoch. Kuramoto |
| [arw_for_social_science.md](arw_for_social_science.md) | Sociology / institutional theory | CASE-0007 + SOC1 |
| [arw_for_statistical_physics.md](arw_for_statistical_physics.md) | Statistical physics / condensed matter | CASE-0004 Stuart-Landau |
| [arw_for_ml.md](arw_for_ml.md) | ML / representation learning / deep learning | CASE-0009 + operator catalog |

---

## How to Add an Instantiation

1. Copy `art_scope_template.md` to a new file.
2. Fill in all four scope components (B, Π, Δ, ε) with concrete values.
3. Derive the expected regime partition and specify falsification conditions.

For operator-level justification, use `docs/cases/CASE_TEMPLATE_signature_first.md`.

For physical and agent system scopes, see also the experiment files
in [experiments/](../../experiments/) which contain full ART instantiations
embedded in their experimental designs.
