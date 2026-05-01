# Experiment: Vertical Spring-Mass Chain (CASE-20260430-0013)

Multi-scale observable sweep for the vertical spring-mass chain.
Implements ScopeSpec v3 (`cases/CASE-20260430-0013/ScopeSpec_signature_first.md`).

## Scripts

| Script | Purpose |
|---|---|
| `spring_mass_sweep.py` | Simulates N-mass chain over 2D grid (A, Ω/ω₁); writes `sweep_raw.npz`, `sigma_delta.npz`, `bcmanifest.json` |
| `spring_mass_cover.py` | Cover analysis on sweep output; applies adjacency-preserving cover pipeline (Felder 2026) to all three observable levels |

## Usage

```bash
# Pilot run (N=3, 20×20 grid)
python spring_mass_sweep.py --N 3 --n_A 20 --n_Omega 20 --pilot

# Full run
python spring_mass_sweep.py --N 3 --n_A 40 --n_Omega 40

# Cover analysis (after sweep)
python spring_mass_cover.py --N 3
```

## Observables

- `pi_micro`: spring-extension variance (relative, internal)
- `pi_meso`: center-of-mass variance (absolute, collective)
- `pi_macro`: end-mass variance (absolute, terminal)
