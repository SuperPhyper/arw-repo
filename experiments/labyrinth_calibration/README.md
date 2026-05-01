# Experiment: Scope Calibration — Labyrinth (CASE-20260330-0012)

Scope calibration tool for the labyrinth context-navigation experiment.

## Script

`calibrate_scope.py` — Answers two questions:

- **Q1 (Scope):** Which (GRID_SIZE, T_MAX, exit_zone_width) combination yields
  `P(episode ∈ R(π_goal)) ≥ target_admissibility`? Measured with a GREEDY baseline policy.
- **Q2 (Training):** Given a calibrated scope, how much PPO training is needed
  until `goal_rate` converges to `P(R)`?

## Usage

```bash
python calibrate_scope.py                          # full sweep
python calibrate_scope.py --q1-only               # scope sweep only
python calibrate_scope.py --target 0.80           # different target
python calibrate_scope.py --env corridor          # specific env
python calibrate_scope.py --grid-sizes 25 35 50   # maze size sweep
```

## Related

- `cases/CASE-20260330-0012/` — labyrinth agent case
- `docs/context_navigation/` — three-scope architecture docs
