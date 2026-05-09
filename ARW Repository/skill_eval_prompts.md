# ARW Skill Eval — 8 Probe-Szenarien

**Zweck:** Testet die Korrektheit der aktualisierten ARW-Skills (arw-meta-guard,
arw-repo-context, arw-observable-analysis, arw-doc-consistency) nach dem
Context-Map-Update vom 2026-05-10.

**Durchführung:** Jeden Prompt in einer NEUEN Cowork-Session einfügen (frischer Kontext).
Skills müssen installiert sein. Antwort gegen das SOLL prüfen.

**Bewertung:** PASS / PARTIAL / FAIL pro Szenario notieren.

---

## Szenario 1 — F-gradient vs F0 (GUARD-2 fix)

**Testet:** Erkennt der Agent, dass F0 falsch ist wenn A0–A6 alle bestehen?

**Prompt:**

> Please review this ScopeSpec falsification block for correctness:
>
> ```yaml
> falsification:
>   - id: F0
>     description: >
>       Observable var_rel remains within R(π) at all sweep points.
>       Substrate analysis confirms A0–A6 all satisfied throughout X_B.
>       However, at E ≈ ω₀², the gradient |∂var_rel/∂E| is very high,
>       causing σ_Δ(x) ≥ ε_working in a localised region.
>     severity: observable_replacement
>     recommended_action: Replace observable
> ```
>
> Is this correct? If not, what should it be?

**SOLL:**
- Agent identifiziert: ID sollte `F-gradient` sein, nicht `F0`
- Begründung: A0–A6 alle bestehen → kein Substratfehler → nicht F0
- Severity sollte `scope_refinement` sein, nicht `observable_replacement`
- Empfehlung: ε senken, Δ reduzieren, oder stability mask anwenden

**PASS-Kriterium:** Agent nennt F-gradient explizit und korrigiert severity.

---

## Szenario 2 — Ungültige Falsification-ID (GUARD-2)

**Testet:** Erkennt der Agent einen nicht-existenten Falsification-ID?

**Prompt:**

> Check this ScopeSpec falsification entry before I commit it:
>
> ```yaml
> falsification:
>   - id: F5
>     description: No plateau found in N(ε) for any observable.
>     severity: scope_rejection
> ```
>
> Is the `id` field valid?

**SOLL:**
- Agent flaggt `F5` als ungültig
- Benennt das korrekte Enum: {F0, F1, F1_BC, F2, F3, F4, F-gradient}
- Schlägt vor: `F3` wäre hier korrekt (kein Plateau für alle Observables → collective failure)
- Severity `scope_rejection` für F3 ist korrekt — kein Fix nötig dort

**PASS-Kriterium:** Agent nennt das korrekte Enum und schlägt F3 vor.

---

## Szenario 3 — Falsche Severity bei F1 (GUARD-4)

**Testet:** Erkennt der Agent, dass observable_insufficiency ≠ scope_rejection?

**Prompt:**

> Is this ScopeSpec entry correct?
>
> ```yaml
> falsification:
>   - id: F1
>     description: >
>       span(var_rel) < 2·ε_working. Observable has insufficient spread
>       to distinguish regimes at this resolution.
>     severity: scope_rejection
>     recommended_action: Reject scope and restart with different B.
> ```

**SOLL:**
- Agent flaggt severity als falsch
- F1 → `observable_replacement`, nicht `scope_rejection`
- scope_rejection nur bei F1_BC (wenn F1 für ALLE π ∈ Π gilt)
- Erklärt GUARD-4 (observable_insufficiency ≠ scope_rejection)

**PASS-Kriterium:** Agent korrigiert severity zu observable_replacement und erklärt den Unterschied zu F1_BC.

---

## Szenario 4 — Context Map Navigation (Differential Diagnosis)

**Testet:** Nutzt der Agent die context_map Differential-Diagnose korrekt?

**Prompt:**

> I'm analysing an observable O for a new case. Within the admissible domain X_B,
> substrate analysis (A0–A6) passes at every point. But when I compute the stability
> mask, I find σ_Δ(x) ≥ ε_working in a small connected region near the parameter
> value κ = 2.1. The gradient |∂O/∂κ| is very large there.
>
> What is the ARW classification of this situation, and what actions are recommended?

**SOLL:**
- Klassifikation: F-gradient (descriptive crossover) — explizit benannt
- Formal: Z_cover ≠ ∅, aber Z(π) = ∅ (kein Substratfehler)
- Empfohlene Aktionen (in Reihenfolge): stability_mask exclusion → ε erhöhen → Δ-Radius r reduzieren → Observable ersetzen
- Kein scope_rejection, kein F0

**PASS-Kriterium:** F-gradient explizit genannt, scope_refinement als primäre Aktion, F0 klar abgegrenzt.

---

## Szenario 5 — Case Lookup (neue Cases)

**Testet:** Kennt der Agent CASE-20260430-0013 (nach Update neu in §2)?

**Prompt:**

> What BC class does CASE-20260430-0013 use, what is the sweep setup,
> and what makes it scientifically notable?

**SOLL:**
- BC-Klasse: FORCING + RESTRICTION
- Sweep: 2D (A = forcing amplitude, Ω = forcing frequency)
- Konditionierter Parameter: N (Kettenlänge, 1–5)
- Observables: π_micro (spring extension variance), π_meso (COM variance), π_macro (end-mass variance)
- Notabel: erster Multi-Scale-Observable-Case im Repo
- Status: open / pending

**PASS-Kriterium:** BC-Klasse korrekt, multi-scale observable genannt.

---

## Szenario 6 — Dokumentstatus (updated pending items)

**Testet:** Weiß der Agent, dass perturbation_spread.md bereits existiert?

**Prompt:**

> I want to write a document about perturbation spread σ_Δ(x) for the ARW repo.
> Does something like this already exist? If so, where, and what does it cover?

**SOLL:**
- Agent sagt: Ja, existiert bereits
- Pfad: `docs/glossary/perturbation_spread.md`
- Erstellt: 2026-04-29, status: definition
- Inhalt: σ_Δ(x) = sup_{δ∈Δ} |O(x+δ)−O(x)|, pointwise stability, Lipschitz bound (Felder 2026 Def 4)
- Agent rät: extend, nicht neu erstellen

**PASS-Kriterium:** Korrekte Pfadangabe, kein "zu erstellen" Hinweis.

---

## Szenario 7 — Notation-Verständnis (Context Map)

**Testet:** Kann der Agent die komprimierte Context-Map-Notation korrekt interpretieren?

**Prompt:**

> I found this entry in the ARW context map:
>
> ```
> Z_cover: zone∈cover | {x:σ_Δ(x)≥ε}∩R(π) | ε-dependent | →F-gradient | ¬Z(π)
> ```
>
> Without looking at any other documentation: what does this entry tell me about
> Z_cover, and what action should I take if I detect it in my analysis?

**SOLL:**
- Z_cover ist eine Zone innerhalb R(π) (kein Substratfehler)
- Bedingung: σ_Δ(x) ≥ ε, d.h. ε-abhängig (kein Substratproblem)
- Trigger: → F-gradient (nicht F0, nicht scope_rejection)
- ¬Z(π): explizit abgegrenzt von Substratversagen
- Aktion: scope_refinement (ε anpassen, Δ reduzieren, stability mask)

**PASS-Kriterium:** Agent leitet aus der Notation allein die richtige Aktion ab, ohne Verweis auf andere Docs nötig.

---

## Szenario 8 — Differentialdiagnose F0 vs F-gradient

**Testet:** Unterscheidet der Agent korrekt, wenn BEIDE Bedingungen vorliegen?

**Prompt:**

> In my case, at parameter value κ = 1.5:
> - σ_Δ(x) = 0.42, which exceeds ε_working = 0.09
> - Substrate analysis finds that assumption A2 (stationarity of measure) fails at this point
>
> Should I classify this as F0 or F-gradient? What action follows?

**SOLL:**
- Klassifikation: F0 (Substratfehler hat Vorrang)
- Begründung: A2 verletzt → observable außerhalb R(π) → Z(π) ≠ ∅
- F-gradient scheidet aus: F-gradient setzt A0–A6 alle bestehend voraus
- Aktion: observable_replacement (nicht scope_refinement)
- Hinweis: hohe σ_Δ allein reicht nicht für F-gradient wenn Substrat versagt

**PASS-Kriterium:** F0 gewählt, Begründung via A2-Verletzung, observable_replacement als Aktion.

---

## Auswertungsraster

| # | Szenario | PASS | PARTIAL | FAIL | Notiz |
|---|---|---|---|---|---|
| 1 | F-gradient vs F0 | | | | |
| 2 | Ungültige ID (F5) | | | | |
| 3 | F1 severity (GUARD-4) | | | | |
| 4 | Context Map Navigation | | | | |
| 5 | Case Lookup (0013) | | | | |
| 6 | Dokumentstatus | | | | |
| 7 | Notation-Verständnis | | | | |
| 8 | Differential F0/F-gradient | | | | |
| | **Gesamt** | /8 | /8 | /8 | |

**Wertung:**
- 7–8 PASS: Skills und Context Map funktionieren wie erwartet
- 5–6 PASS: Leichte Lücken, gezielte Nachbesserung nötig
- <5 PASS: Strukturelles Problem — Skill-Trigger oder Notation überarbeiten

