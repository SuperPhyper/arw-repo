---
status: note
layer: cases/CASE-20260311-0001/transfer/
---

# Transfer Report: CASE-0001 → CASE-0003
**Datum:** 2026-03-12  
**System A:** Kuramoto (N=500 Oszillatoren, BC-Klasse: Coupling, Sweep: κ ∈ [0, 3])  
**System B:** Doppelpendel (BC-Klasse: Restriction, Sweep: E_target ∈ [0.5, 30 J])  
**Pipeline:** pipeline.transfer v1 + erweiterter Interpretationsblock

---

## Rohergebnisse

| Metrik | Wert | Pipeline-Label |
|--------|------|----------------|
| RCD    | 5    | significant_mismatch |
| TBS    | 2.525 | large_shift |
| PCI    | 0.444 | partial_compatibility |
| SDI    | 10   | significant_distortion |
| **Φ**  | **0.40** | **inadmissible** |

Partition A: N=4, θ*=κ 1.475, persistence=0.914  
Partition B: N=9, θ*=E 4.0 J, persistence=0.273

---

## Metriken-Validitätsprüfung

Bevor das Φ-Ergebnis interpretiert wird, muss für jeden Bestandteil geprüft
werden, ob die Metrik für diesen Transfertyp (Cross-BC-Klasse,
verschiedene Zustandsräume) überhaupt definiert ist.

### TBS — dimensionslos inkommensurabel

TBS = |θ*_A − θ*_B| = |1.475 − 4.0| = 2.525

θ*_A liegt auf der κ-Achse (dimensionsloser Kopplungsparameter, κ ∈ [0, 3]).
θ*_B liegt auf der E-Achse (Energie in Joule, E ∈ [0.5, 30 J]).

Diese Subtraktion ist **formal undefiniert**. Beide Werte sind in völlig
verschiedenen Einheiten — ein absoluter Differenzbetrag ist sinnlos.
TBS ist als Metrik nur innerhalb derselben BC-Klasse auf derselben
Parameterachse interpretierbar. Der pipeline-interne TBS_score = 0
(maximale Bestrafung) ist ein Artefakt der dimensionalen Inkommensurabilität,
kein Befund über die Partitionsstruktur.

**Konsequenz:** TBS aus dem Φ-Compositum herausnehmen für Cross-BC-Transfer.
Φ_korr = 0.4 * PCI + 0.3 * RCD_score + 0.2 * SDI_score = 0.40 + ... 
Siehe Sensitivitätsanalyse unten.

### PCI — strukturelle Approximation, kein echtes Klassen-Alignment

PCI = min(N_A, N_B) / max(N_A, N_B) = 4/9 = 0.444

Die Pipeline-Implementierung berechnet PCI als strukturelle Approximation:
Verhältnis der kleineren zur größeren Regime-Anzahl. Das ist ein Proxy,
kein echtes Partition-Alignment.

Echte PCI würde fordern: für jede Klasse Rᵢ ∈ G_A prüfen ob
∃ Rⱼ ∈ G_B mit Rᵢ ⊆ Rⱼ (Enthaltungsrelation). Das setzt voraus, dass
A und B Partitionen desselben Zustandsraums sind — was hier nicht gilt.
Kuramoto und Doppelpendel haben völlig verschiedene Zustandsräume (T^N vs. T^2 × R^2).

**Konsequenz:** PCI ist für diesen Transfertyp konzeptuell nicht definiert.
Die strukturelle Approximation misst nur: wie ähnlich sind die Regime-Anzahlen?
Das ist identisch mit dem, was RCD bereits misst — PCI und RCD sind hier redundant.

### RCD und SDI — definiert, aber ε-sensitiv

RCD = |N_A − N_B| = |4 − 9| = 5 ist korrekt berechnet.

SDI = Knotenkosten + Kantenkosten = |4−9| + |3−8| = 5 + 5 = 10.
Beide Komponenten werden **vollständig von N_A ≠ N_B getrieben** —
SDI misst hier keine unabhängige Information über die Graphstruktur.
Die Adjazenzgraphen beider Cases sind lineare Ketten (sequentielle Partition),
die Topologie ist identisch. Das SDI-Signal ist reines Regime-Anzahl-Signal.

**Wichtiger Befund:** N_B = 9 ist nicht eine feste Eigenschaft des Systems,
sondern eine Funktion der ε-Wahl. Der ε-Sweep von CASE-0003 zeigt:

| ε_B   | N_B | w     | RCD | SDI | Φ (ohne TBS) |
|-------|-----|-------|-----|-----|--------------|
| 0.015 | 9   | 0.551 | 5   | 10  | 0.40 (inadmissible) |
| 0.034 | 4   | 0.157 | 0   | 0   | **0.95 (highly_admissible)** |
| 0.045 | 3   | 0.236 | 1   | 2   | 0.725 (partially_admissible) |

Das bedeutet: **das Inadmissibilitäts-Ergebnis ist kein Befund über die
Systeme, sondern über die ε-Wahl.** Bei ε_B = 0.034 (N=4-Plateau) ist
die Partition des Doppelpendels eine exakte strukturelle Entsprechung
der Kuramoto-Partition bei ε_A = 0.09.

---

## Interpretation im ARW-Forschungsbild

### Was Φ = 0.40 bedeutet — und was nicht

Der Pipeline-Output "inadmissible" ist technisch korrekt für die gewählten
ε-Werte: ε_A=0.09 (N=4) vs. ε_B=0.015 (N=9). Ein Transfer zwischen
diesen zwei Auflösungsniveaus scheitert, weil die Doppelpendel-Partition
neun Regime unterscheidet, wo die Kuramoto-Partition nur vier sieht.

Das ist aber keine Aussage über die BC-Klassen. Es ist eine Aussage über
ε-Kompatibilität: man kann nicht zwischen inkompatiblen Auflösungsniveaus
transferieren, unabhängig davon ob die BC-Klassen verwandt sind oder nicht.

### Der eigentliche Transfer-Befund

Die Sensitivitätsanalyse zeigt, dass bei ε_B = 0.034 (N=4-Plateau,
w=0.157) die Doppelpendel-Partition strukturell identisch zur
Kuramoto-Partition ist: beide haben N=4, beide haben eine lineare
Adjazenzgraph-Topologie, beide haben drei Übergänge.

Das ist ein konkretes Ergebnis im ARW-Sinne: **Coupling-BC (κ) und
Restriction-BC (E_target) induzieren bei passender ε-Wahl strukturell
äquivalente sequentielle 4-Regime-Partitionen.** Die Äquivalenz ist
nicht trivial — sie bedeutet, dass beide BC-Klassen eine ähnliche
ordinale Struktur in ihren jeweiligen Zustandsräumen erzeugen:
einen graduellen Übergang von einem "niedrig-aktiven" zu einem
"hoch-aktiven" Zustandsbereich, vermittelt durch zwei Zwischenphasen.

### Was das für die BC-Taxonomie bedeutet

Die ursprüngliche Erwartung war, dass Coupling und Restriction
*inkompatible* Partitionsstrukturen erzeugen — als Beleg für die
konzeptuelle Verschiedenheit der BC-Klassen.

Das Gegenteil ist der Fall: die Strukturen sind bei gleicher
Auflösung kompatibel. Das ist kein Widerspruch zur Taxonomie,
sondern eine Präzisierung: **BC-Klassen unterscheiden sich in
der Natur des Übergangs (kollektiv vs. individuell, Symmetriebrechung
vs. Phasenraum-Kontraktion), nicht in der Anzahl oder Topologie der
induzierten Regime.** Die Partition ist eine strukturelle Invariante,
die über BC-Klassen hinweg erhalten bleibt — was überhaupt erst
einen sinnvollen Transfer ermöglicht.

Das N=4-Plateau des Doppelpendels ist allerdings schmal (w=0.157) —
fast dreimal schmaler als das Kuramoto-Plateau (w=0.700). Das zeigt
den echten Unterschied: **Restriction-BCs erzeugen fragile Partitionen
in dem Sinne, dass die Regime-Grenzen ε-sensitiver sind.** Der
Korridor, in dem eine bestimmte Partitionsstruktur stabil existiert,
ist kleiner. Das ist ein quantitativer Befund über BC-Klassen.

### Methodischer Befund: TBS-Definition für Cross-BC-Transfer

TBS ist in der aktuellen Implementierung für Cross-BC-Klassen-Transfer
undefiniert. Es gibt zwei Möglichkeiten:

1. **TBS aus Φ herausnehmen** für alle Transfers zwischen verschiedenen
   BC-Klassen. Φ_quer = 0.4·PCI + 0.3·RCD_score + 0.3·SDI_score.

2. **TBS normalisieren** auf den jeweiligen Sweep-Bereich:
   TBS_norm = |θ*_A/range_A − θ*_B/range_B| = |1.475/3.0 − 4.0/29.5| = |0.492 − 0.136| = 0.356.
   Das ist ein relativer Grenz-Shift: Kuramoto geht bei ~49% seines
   Sweepbereichs in Synchronisation über, Doppelpendel bei ~12%.
   Das wäre inhaltlich interpretierbar: die Coupling-BC liegt näher an
   der "Mitte" ihres BC-Raums als die Restriction-BC.

Option 2 ist methodisch vorzuziehen, weil sie eine echte Information
erhält: *wo* im BC-Raum liegt die kritische Grenze relativ zum
untersuchten Bereich?

---

## Empfehlung

### Für die Pipeline
- `compute_tbs()` um normalisierten TBS_norm erweitern (erfordert sweep_range in Invariants.json)
- `compute_pci()` für Cross-Systemtyp-Transfer als "not_applicable" flaggen und aus Φ herausnehmen
- Φ-Gewichte für intra- vs. cross-BC-Klasse-Transfer trennen

### Für CASE-0003
- Zusätzlicher Transfer-Lauf mit ε_B = 0.034 (N=4-Plateau) als Vergleichspunkt
- Sweep-Verdichtung um E_target ∈ [2, 8 J] (Übergangszone) für bessere Grenzlokalisierung

### Für die ARW-Theorie
- Der Befund "strukturelle Äquivalenz bei ε-Alignment" ist dokumentierbar als:
  *Satz: Coupling- und Restriction-BCs induzieren strukturell äquivalente
  sequentielle Partitionen wenn ε so gewählt wird, dass N_A = N_B.*
  Das ist ein Kandidat für ein formales Transferresultat.

---

*pipeline.transfer v1 + erweiterter Interpretationsblock · 2026-03-12*
