# Transfer Report: CASE-0003 → CASE-0001
**Datum:** 2026-03-12  
**System A:** Doppelpendel (BC-Klasse: Restriction, Sweep: E_target ∈ [0.5, 30 J], N=9, ε=0.015)  
**System B:** Kuramoto (BC-Klasse: Coupling, Sweep: κ ∈ [0, 3], N=4, ε=0.09)  
**Transfertyp:** Cross-BC-class (Restriction ↔ Coupling)  
**Pipeline:** pipeline.transfer v1

Vollständige inhaltliche Analyse: `cases/CASE-20260311-0001/transfer/kuramoto_vs_pendulum/TransferReport_extended.md`

---

## Metriken

| Metrik | Wert | Interpretation |
|---|---|---|
| RCD    | 5    | significant_mismatch |
| TBS    | 0.217 (norm) / 2.525 (raw) | moderate_shift |
| PCI    | 0.444 | partial_compatibility |
| SDI    | 10   | significant_distortion |
| **Φ**  | **0.40** | **inadmissible** |

Partition A: N=9, θ*=E 4.0 J, persistence=0.273  
Partition B: N=4, θ*=κ 1.475, persistence=0.914

---

## ε-Sensitivität

Φ=0.40 reflektiert ε-Mismatch (N_A=9 vs. N_B=4), keine intrinsische BC-Inkompatibilität.

| ε_A   | N_A | ε_B  | N_B | RCD | Φ | Label |
|-------|-----|------|-----|-----|---|-------|
| 0.015 | 9   | 0.09 | 4   | 5   | 0.40 | current |
| 0.034 | 4   | 0.09 | 4   | 0   | ~0.95 | matched_resolution |
| 0.045 | 3   | 0.09 | 4   | 1   | ~0.73 | near_match |

---

## TBS-Normierung

TBS_raw = |4.0 − 1.475| = 2.525 — inkommensurabel (J vs. dimensionslos).  
TBS_norm = |4.0/29.5 − 1.475/3.0| = |0.136 − 0.492| = **0.356** (moderate_shift).

Interpretation: Der Doppelpendel-Übergang liegt bei 13.7% des Sweep-Bereichs,
der Kuramoto-Übergang bei 49.2%. Der Restriction-BC erzeugt frühere Übergänge
relativ zum erkundeten BC-Raum.

---

## Strukturbefund

Bei ε-Alignment (beide N=4): Coupling- und Restriction-BCs induzieren strukturell
äquivalente sequentielle Partitionen. Kandidat für Transfersatz:

> *Coupling- und Restriction-BCs mit monotonen Observablen erzeugen strukturell
> äquivalente sequentielle Partitionen wenn ε so gewählt wird, dass N_A = N_B.*

---

## Nächste Schritte

- Sweep-Verdichtung um E_target ∈ [2, 8 J] für bessere θ*-Lokalisierung
- Transfer-Lauf mit ε_A = 0.034 (N=4-Plateau) als matched-resolution Referenzpunkt
- Persistence CASE-0003 (0.273): 12 Sweep-Punkte zu wenig; dichterer Sweep empfohlen
