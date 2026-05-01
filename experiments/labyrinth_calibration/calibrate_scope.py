"""
calibrate_scope.py — Scope calibration for the labyrinth experiment.

Answers two questions:

  Q1 (Scope): Which (GRID_SIZE, T_MAX, exit_zone_width) combination yields
              P(episode ∈ R(π_goal)) ≥ target_admissibility?
              → Measured with a GREEDY baseline policy (minimal directional
                competence — not random, not trained).
              → This is a property of the environment, not the agent.
              → Maze size is the third sweep dimension: larger mazes lower
                P(R) for weak policies, coupling admissibility to policy
                quality (see F-06).

  Q2 (Training): Given a calibrated scope, how much training is needed
                 until goal_rate converges to P(R)?
                 → Measured by running PPO and tracking goal_rate/P(R) ratio.
                 → solve_ratio = goal_rate / P(R) → 1.0 means training
                   fully exploits the admissible episodes.

Usage:
    python calibrate_scope.py                    # full sweep
    python calibrate_scope.py --q1-only          # scope sweep only
    python calibrate_scope.py --target 0.80      # different target
    python calibrate_scope.py --env corridor     # specific env
    python calibrate_scope.py --grid-sizes 25 35 50  # maze size sweep
"""

import argparse
import importlib
import json
import sys
import time
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict

# ── Config ────────────────────────────────────────────────────────────────────

GRID_SIZES      = [25, 35, 50]              # maze sizes to sweep
T_MAX_VALUES    = [60, 90, 120, 180, 240, 360]
EXIT_COL_STARTS = [24, 23, 22, 21, 20, 19, 18, 16]   # narrowing → widening zone
N_EPISODES_Q1   = 500    # episodes per combo — greedy baseline
N_EPISODES_Q2   = 2000   # episodes per training checkpoint
TARGET_DEFAULT  = 0.80
TRAIN_STEPS_Q2  = [50_000, 100_000, 200_000, 400_000]

ENV_REGISTRY = {
    'open':     'env_open.OpenEnv',
    'halfwall': 'env_halfwall.HalfWallEnv',
    'costpath': 'env_costpath.CostPathEnv',
    'corridor': 'env_corridor.CorridorEnv',
    'combined': 'env_combined.CombinedEnv',
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _load_env_class(name: str):
    mod_name, cls_name = ENV_REGISTRY[name].rsplit('.', 1)
    import importlib
    mod = importlib.import_module(mod_name)
    return getattr(mod, cls_name)


def _set_exit_curriculum(col_start: int):
    """
    Override EXIT_CURRICULUM in env_base so all envs use a fixed exit zone
    [col_start, 24] for this calibration run.
    """
    import env_base
    cols = list(range(col_start, env_base.GRID_SIZE))
    # Single stage — no curriculum progression during calibration
    env_base.EXIT_CURRICULUM = [(None, cols)]
    env_base.EXIT_ZONE_COLS  = cols


def _set_t_max(t_max: int):
    """Override T_MAX in env_base and all loaded env modules."""
    import env_base, env_open, env_halfwall, env_costpath, env_corridor, env_combined
    for mod in [env_base, env_open, env_halfwall, env_costpath,
                env_corridor, env_combined]:
        mod.T_MAX = t_max


def _set_grid_size(grid_size: int):
    """
    Patch env_base constants for the current grid size.

    IMPORTANT: env modules (env_open, etc.) must NOT yet be imported when
    this is called, because they run module-level connectivity checks at
    import time using GRID_SIZE. The correct usage pattern is:

        _set_grid_size(25)
        from env_open import OpenEnv   # imports AFTER patch

    For multi-grid sweeps, use the --grid-size CLI argument and run
    calibrate_scope.py once per grid size (separate Python sessions).
    The q1_scope_sweep() function handles this via subprocess when
    multiple grid sizes are requested.
    """
    import env_base
    env_base.GRID_SIZE     = grid_size
    env_base.EXIT          = (grid_size - 1, grid_size - 1)
    env_base.D_MAX         = float((grid_size - 1) * 2)
    env_base.SPAWN_MAX_COL = max(1, grid_size // 3)

    exit_start = grid_size * 2 // 3
    full_zone  = list(range(exit_start, grid_size))
    env_base.EXIT_ZONE_COLS = full_zone

    col_a = max(exit_start, grid_size - max(3, grid_size // 10))
    col_b = max(exit_start, grid_size - max(6, grid_size // 5))
    env_base.EXIT_CURRICULUM = [
        (500,  list(range(col_a, grid_size))),
        (2000, list(range(col_b, grid_size))),
        (None, full_zone),
    ]


def _run_greedy_episodes(EnvCls, n_episodes: int, seed: int = 0) -> Dict:
    """
    Run N episodes with a greedy-toward-exit policy (always moves toward
    exit row/col, with random tie-breaking and 20% exploration noise).

    This estimates P(episode ∈ R(π_goal)) for a minimally competent agent —
    not a random walk (too pessimistic) and not a trained policy (too
    optimistic). The greedy policy approximates what a policy with perfect
    d_nav signal but no wall-avoidance learning would achieve.
    """
    rng = np.random.default_rng(seed)
    env = EnvCls(seed=seed)

    reached = 0
    ep_lengths = []
    d_exit_at_start = []

    for _ in range(n_episodes):
        obs = env.reset()
        d_start = env._dist_to_exit()
        done = False
        steps = 0
        while not done:
            r, c = env.pos
            er, ec = env._exit
            # Greedy: prefer action that reduces Manhattan distance
            # 20% random noise to avoid permanent wall-blocking
            if rng.random() < 0.20:
                action = int(rng.integers(4))
            else:
                dr = er - r; dc = ec - c
                candidates = []
                if dr > 0: candidates.append(1)   # DOWN
                if dr < 0: candidates.append(0)   # UP
                if dc > 0: candidates.append(3)   # RIGHT
                if dc < 0: candidates.append(2)   # LEFT
                action = int(rng.choice(candidates)) if candidates else int(rng.integers(4))
            obs, _, done, info = env.step(action)
            steps += 1
        if info['reached_goal']:
            reached += 1
        ep_lengths.append(steps)
        d_exit_at_start.append(d_start)

    p_r = reached / n_episodes
    return {
        'p_admissible':   round(p_r, 4),
        'mean_ep_length': round(float(np.mean(ep_lengths)), 1),
        'mean_d_start':   round(float(np.mean(d_exit_at_start)), 2),
        'n_episodes':     n_episodes,
    }


# ── Q1: Scope sweep ───────────────────────────────────────────────────────────

def q1_scope_sweep(env_names: List[str], target: float,
                   grid_sizes: List[int] = None,
                   verbose: bool = True) -> Dict:
    """
    Sweep GRID_SIZE × T_MAX × exit_zone_width.

    For each grid size, dispatches a subprocess so env modules are
    imported fresh with the correct GRID_SIZE (module-level connectivity
    checks require a clean import). Results are merged across grid sizes.
    """
    import subprocess, tempfile, os
    if grid_sizes is None:
        grid_sizes = GRID_SIZES

    all_results   = {}
    recommendations = {}

    for grid in grid_sizes:
        if verbose:
            print(f'\n=== Q1 grid={grid} — dispatching subprocess ===')

        # Build subprocess command for this grid size
        script = (
            f"import sys; sys.path.insert(0,'{sys.path[0]}')\n"
            f"from calibrate_scope import (\n"
            f"    _set_grid_size, _set_t_max, _set_exit_curriculum,\n"
            f"    _run_greedy_episodes, _load_env_class,\n"
            f"    T_MAX_VALUES, N_EPISODES_Q1\n"
            f")\n"
            f"import json\n"
            f"_set_grid_size({grid})\n"
            f"env_names = {env_names!r}\n"
            f"target    = {target}\n"
            f"results   = {{}}\n"
            f"exit_start = {grid} * 2 // 3\n"
            f"col_starts = sorted(set([\n"
            f"    {grid}-1,\n"
            f"    max(exit_start, {grid}-3),\n"
            f"    max(exit_start, {grid}-5),\n"
            f"    max(exit_start, {grid}-8),\n"
            f"    exit_start,\n"
            f"]), reverse=True)\n"
            f"for env_name in env_names:\n"
            f"    EnvCls = _load_env_class(env_name)\n"
            f"    results[env_name] = {{}}\n"
            f"    for t_max in T_MAX_VALUES:\n"
            f"        _set_t_max(t_max)\n"
            f"        results[env_name][t_max] = {{}}\n"
            f"        for col in col_starts:\n"
            f"            _set_exit_curriculum(col)\n"
            f"            m = _run_greedy_episodes(EnvCls, N_EPISODES_Q1)\n"
            f"            results[env_name][t_max][col] = m\n"
            f"print(json.dumps(results))\n"
        )

        proc = subprocess.run(
            [sys.executable, '-c', script],
            capture_output=True, text=True
        )
        if proc.returncode != 0:
            print(f'  [ERROR] grid={grid}: {proc.stderr[-400:]}')
            continue

        try:
            grid_results = json.loads(proc.stdout.strip().split('\n')[-1])
        except Exception as e:
            print(f'  [ERROR] parsing results grid={grid}: {e}')
            continue

        all_results[grid] = grid_results

        # Print results and find recommendations
        if verbose:
            print(f'{"env":12s}  {"T_MAX":>6}  {"cols":>10}  {"P(R)":>6}  '
                  f'{"mean_d":>7}  {"steps":>8}')
            print('─' * 58)

        for env_name in env_names:
            if env_name not in grid_results:
                continue
            env_r = grid_results[env_name]
            exit_start = grid * 2 // 3

            for t_max_str, t_results in sorted(env_r.items(),
                                                key=lambda x: int(x[0])):
                t_max = int(t_max_str)
                for col_str, m in sorted(t_results.items(),
                                          key=lambda x: -int(x[0])):
                    col = int(col_str)
                    admits = m['p_admissible'] >= target
                    mark = '✓' if admits else ' '
                    if verbose:
                        print(f'{env_name:12s}  {t_max:>6}  '
                              f'{col:>4}–{grid-1:<4}  '
                              f'{m["p_admissible"]:>6.3f}{mark}  '
                              f'{m["mean_d_start"]:>7.1f}  '
                              f'{m["mean_ep_length"]:>8.1f}')

                    # First (smallest scope) that meets target
                    key = env_name
                    if admits and key not in recommendations:
                        recommendations[key] = (grid, t_max, col,
                                                m['p_admissible'])
            if verbose:
                print()

    if verbose:
        print('\n=== Recommendations ===')
        for env_name in env_names:
            rec = recommendations.get(env_name)
            if rec:
                g, t, c, p = rec
                print(f'  {env_name:12s}: grid={g}  T_MAX={t}  '
                      f'cols {c}–{g-1}  P(R)={p:.3f}')
            else:
                print(f'  {env_name:12s}: no admissible scope found')

    return {'sweep': all_results, 'recommendations': recommendations,
            'target': target, 'n_episodes': N_EPISODES_Q1,
            'grid_sizes': grid_sizes}


# ── Q2: Training convergence ──────────────────────────────────────────────────

def q2_training_convergence(env_name: str, t_max: int, col_start: int,
                             target_p_r: float, verbose: bool = True) -> Dict:
    """
    Given a calibrated scope (T_MAX, col_start), measure how training
    steps affect P(solve | R, policy).

    Trains a PPO agent for increasing step budgets and measures:
      - goal_rate_observed    (what the trained policy achieves)
      - p_admissible          (P(R) under random policy — constant)
      - solve_ratio           = goal_rate_observed / p_admissible
                               → 1.0 means training fully exploits R(π_goal)
    """
    try:
        from stable_baselines3 import PPO
        from stable_baselines3.common.monitor import Monitor
        from policy import LabyrinthGymEnv, make_ppo_model
        from s_online import SOnline
        from s_sleep import sleep_phase
        from env_base import SALIENCY_TYPES
    except ImportError as e:
        print(f'[Q2] Import error: {e} — skipping training convergence')
        return {}

    _set_t_max(t_max)
    _set_exit_curriculum(col_start)
    EnvCls = _load_env_class(env_name)

    # Baseline: random policy admissibility
    p_r = _run_greedy_episodes(EnvCls, N_EPISODES_Q1)['p_admissible']

    if verbose:
        print(f'\n=== Q2 Training convergence: {env_name} '
              f'(T_MAX={t_max}, cols {col_start}–24, P(R)={p_r:.3f}) ===')
        print(f'{"steps":>10}  {"goal_rate":>10}  {"P(R)":>6}  '
              f'{"solve_ratio":>12}  {"gap":>8}')
        print('─' * 55)

    arch = {t: [] for t in SALIENCY_TYPES}
    model = None
    results = []

    cumulative_steps = 0
    for step_budget in TRAIN_STEPS_Q2:
        additional = step_budget - cumulative_steps
        if additional <= 0:
            continue

        gym_env = LabyrinthGymEnv(EnvCls, archetype_library=arch, seed=42)
        mon_env = Monitor(gym_env)

        if model is None:
            model = make_ppo_model(mon_env, seed=42)
        else:
            model.set_env(mon_env)

        model.learn(total_timesteps=additional, reset_num_timesteps=False)
        cumulative_steps = step_budget

        # Evaluate: 200 episodes with trained policy
        eval_env = EnvCls(seed=99)
        reached_eval = 0
        for _ in range(200):
            obs = eval_env.reset()
            done = False
            while not done:
                action, _ = model.predict(obs, deterministic=True)
                obs, _, done, info = eval_env.step(int(action))
            if info['reached_goal']:
                reached_eval += 1

        goal_rate = reached_eval / 200
        solve_ratio = goal_rate / p_r if p_r > 0 else float('nan')
        gap = p_r - goal_rate

        row = {
            'steps':        cumulative_steps,
            'goal_rate':    round(goal_rate, 4),
            'p_admissible': round(p_r, 4),
            'solve_ratio':  round(solve_ratio, 4),
            'gap':          round(gap, 4),
        }
        results.append(row)

        if verbose:
            converged = '✓ converged' if solve_ratio >= 0.90 else ''
            print(f'{cumulative_steps:>10,}  {goal_rate:>10.3f}  '
                  f'{p_r:>6.3f}  {solve_ratio:>12.3f}  {gap:>8.3f}  '
                  f'{converged}')

    return {
        'env': env_name, 't_max': t_max, 'col_start': col_start,
        'p_admissible': p_r, 'training_curve': results,
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target',     type=float, default=TARGET_DEFAULT)
    parser.add_argument('--env',        type=str,   default='all')
    parser.add_argument('--q1-only',    action='store_true')
    parser.add_argument('--grid-sizes', type=int,   nargs='+',
                        default=GRID_SIZES,
                        help='Maze sizes to sweep (default: 25 35 50)')
    parser.add_argument('--out',        type=str,   default='results/calibration')
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    env_names = list(ENV_REGISTRY.keys()) if args.env == 'all' else [args.env]

    print(f'Scope calibration — target P(R) = {args.target}')
    print(f'Envs: {env_names}')
    print(f'Grid sizes: {args.grid_sizes}')
    print(f'Q1: {N_EPISODES_Q1} episodes/combo × '
          f'{len(T_MAX_VALUES)} T_MAX × exit zones × {len(args.grid_sizes)} grid sizes')

    t0 = time.time()

    # Q1 — scope sweep (now includes grid size)
    q1 = q1_scope_sweep(env_names, args.target, grid_sizes=args.grid_sizes)
    with open(out_dir / 'q1_scope_sweep.json', 'w') as f:
        json.dump(q1, f, indent=2)
    print(f'\nQ1 saved → {out_dir}/q1_scope_sweep.json')

    if not args.q1_only:
        q2_results = []
        for env_name in env_names:
            rec = q1['recommendations'].get(env_name)
            if rec is None:
                print(f'\n[Q2] Skipping {env_name} — no admissible scope found')
                continue
            grid, t_max, col_start, _ = rec
            _set_grid_size(grid)
            result = q2_training_convergence(env_name, t_max, col_start,
                                             args.target)
            if result:
                q2_results.append(result)

        with open(out_dir / 'q2_training_convergence.json', 'w') as f:
            json.dump(q2_results, f, indent=2)
        print(f'\nQ2 saved → {out_dir}/q2_training_convergence.json')

    # Summary
    print(f'\n{"="*60}')
    print('CALIBRATION SUMMARY')
    print(f'{"="*60}')
    print(f'{"env":12s}  {"grid":>6}  {"T_MAX":>6}  {"exit_cols":>12}  {"P(R)":>6}')
    print('─' * 48)
    for env_name, rec in q1['recommendations'].items():
        if rec:
            g, t, c, p = rec
            print(f'{env_name:12s}  {g:>6}  {t:>6}  '
                  f'{c:>4}–{g-1:<4}   {p:>6.3f}')
        else:
            print(f'{env_name:12s}  {"—":>6}  {"no admissible scope":>20}')
    print(f'\nTotal time: {time.time()-t0:.0f}s')


if __name__ == '__main__':
    main()
