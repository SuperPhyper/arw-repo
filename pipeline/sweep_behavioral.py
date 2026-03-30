"""
pipeline/sweep_behavioral.py — Behavioral Sweep Adapter for Labyrinth Phase 1

Bridges the context-navigation agent experiment to the ARW partition pipeline.

STRUCTURAL DIFFERENCE FROM PHYSICS CASES:
    Physics cases (Kuramoto, pendulum, Stuart-Landau) sweep a BC parameter κ
    and measure a scalar observable at each sweep point. The ε-sweep then
    finds regime boundaries in the κ-axis.

    Phase 1 (labyrinth) has NO BC parameter sweep — all Zone A constraints
    are fixed. The "sweep" here is:
        1. Train the agent for N_training_episodes (learning phase)
        2. Collect N_eval_episodes of trajectory data (extraction phase)
        3. Sweep ε (cosine distance threshold) over policy_embedding centroids
           to find the cluster count N(ε)

    The output EpsilonSweep_behavioral.json follows the same schema as
    EpsilonSweep.json but uses ε (not κ) as the sweep axis and N_clusters
    (not a physical observable) as the partition signal.

Output files (written to results/partition/):
    behavioral_data.json         — per-episode trajectory summary
    EpsilonSweep_behavioral.json — N_clusters vs ε (cosine & L1)
    agent_weights.npz            — trained agent weights (for Phase 2 reuse)

Usage:
    python -m pipeline.sweep_behavioral --case cases/CASE-20260329-0011
    python -m pipeline.sweep_behavioral --case cases/CASE-20260329-0011 \\
        --train-episodes 1000 --eval-episodes 200 --seeds 5

Phase 1 go/no-go:
    EpsilonSweep_behavioral shows a stable plateau with N=1 over at least
    3 consecutive ε steps, in >= 80% of random seeds (delta_03).
    Falsification: no plateau (continuous manifold) → scope_rejection F3.
"""

import argparse
import json
import math
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import numpy as np
    import yaml
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    print("Run: pip install numpy pyyaml --break-system-packages")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent

from pipeline.kernels.labyrinth_env   import LabyrinthEnv
from pipeline.kernels.labyrinth_agent import ModeLibraryAgent


# ── Training ─────────────────────────────────────────────────────────────────

def run_episode(
    env: LabyrinthEnv,
    agent: ModeLibraryAgent,
    epsilon_greedy: float,
    rng: np.random.Generator,
    train: bool = True,
) -> dict:
    """
    Run one episode.  Returns per-episode summary dict.
    If train=True, calls agent.update() at episode end.
    """
    obs = env.reset()
    trajectory = []
    mode_seq   = []
    emb_seq    = []
    sal_seq    = []
    total_rew  = 0.0

    while True:
        # Single forward pass — collect all values needed for action and backprop
        emb, mode_weights, active_mode, mixed_probs, salience, all_logits = agent.forward(obs)

        if rng.random() < epsilon_greedy:
            action_idx = int(rng.integers(0, 4))
        else:
            action_idx = int(np.argmax(mixed_probs))

        obs_next, reward, done, info = env.step(action_idx)

        trajectory.append((obs, action_idx, reward, emb.copy(), mode_weights.copy(), [lg.copy() for lg in all_logits]))
        mode_seq.append(active_mode)
        emb_seq.append(emb.copy())
        sal_seq.append(salience)
        total_rew += reward
        obs = obs_next

        if done:
            break

    if train:
        agent.update(trajectory)

    mode_dist  = agent.get_mode_dist(mode_seq)
    emb_centroid = agent.get_embedding_centroid(emb_seq)
    # Entropy of mode_dist (scalar observable for L1 ε-sweep)
    md_clipped = np.clip(mode_dist, 1e-12, 1.0)
    entropy    = float(-np.sum(md_clipped * np.log(md_clipped)))

    return {
        "total_reward":      round(float(total_rew), 4),
        "episode_length":    len(trajectory),
        "reached_goal":      info.get("reached", False),
        "mode_dist":         mode_dist.tolist(),
        "mode_entropy":      round(entropy, 6),
        "dominant_mode":     int(np.argmax(mode_dist)),
        "salience_mean":     round(float(np.mean(sal_seq)), 6),
        "embedding_centroid": emb_centroid.tolist(),
    }


def train_agent(
    env: LabyrinthEnv,
    agent: ModeLibraryAgent,
    n_episodes: int,
    epsilon_greedy: float,
    rng: np.random.Generator,
    verbose: bool = True,
) -> list:
    """Train agent for n_episodes; return training log."""
    log = []
    t0  = time.time()
    interval = max(1, n_episodes // 10)

    for ep in range(n_episodes):
        result = run_episode(env, agent, epsilon_greedy, rng, train=True)
        log.append(result)

        if verbose and (ep + 1) % interval == 0:
            recent = log[-interval:]
            avg_rew  = np.mean([r["total_reward"] for r in recent])
            avg_goal = np.mean([float(r["reached_goal"]) for r in recent])
            print(f"  [train {ep+1:4d}/{n_episodes}]  "
                  f"avg_reward={avg_rew:+.3f}  goal_rate={avg_goal:.2f}  "
                  f"baseline={agent.baseline:.3f}  "
                  f"({time.time()-t0:.1f}s)")

    return log


def evaluate_agent(
    env: LabyrinthEnv,
    agent: ModeLibraryAgent,
    n_episodes: int,
    epsilon_greedy: float,
    rng: np.random.Generator,
) -> list:
    """Evaluate agent (no weight updates); return eval log."""
    return [
        run_episode(env, agent, epsilon_greedy, rng, train=False)
        for _ in range(n_episodes)
    ]


# ── Epsilon sweep on behavioral data ─────────────────────────────────────────

def cosine_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine distance in [0, 2]."""
    na = np.linalg.norm(a)
    nb = np.linalg.norm(b)
    if na < 1e-12 or nb < 1e-12:
        return 0.0
    return float(1.0 - np.dot(a, b) / (na * nb))


def count_clusters_cosine(embeddings: np.ndarray, eps: float) -> int:
    """
    Count connected components in the graph where edge (i,j) exists iff
    cosine_distance(emb_i, emb_j) < eps.
    Uses union-find (path compression).
    """
    n = len(embeddings)
    if n == 0:
        return 0

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path compression
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for i in range(n):
        for j in range(i + 1, n):
            if cosine_distance(embeddings[i], embeddings[j]) < eps:
                union(i, j)

    return len(set(find(i) for i in range(n)))


def count_clusters_l1(mode_dists: np.ndarray, eps: float) -> int:
    """
    Count connected components using L1 distance on mode_dist vectors.
    Edge (i,j) iff L1(mode_dist_i, mode_dist_j) < eps.
    """
    n = len(mode_dists)
    if n == 0:
        return 0

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    for i in range(n):
        for j in range(i + 1, n):
            if np.sum(np.abs(mode_dists[i] - mode_dists[j])) < eps:
                union(i, j)

    return len(set(find(i) for i in range(n)))


def epsilon_sweep_behavioral(
    eval_log: list,
    eps_cosine: list,
    eps_l1: list,
) -> dict:
    """
    Sweep ε over policy_embedding (cosine) and mode_dist (L1).
    Returns sweep results and plateau analysis.
    """
    embeddings = np.array([ep["embedding_centroid"] for ep in eval_log], dtype=np.float32)
    mode_dists = np.array([ep["mode_dist"]          for ep in eval_log], dtype=np.float32)

    # ── Cosine ε-sweep ───────────────────────────────────────────────────────
    cosine_results = []
    for eps in eps_cosine:
        n_clust = count_clusters_cosine(embeddings, eps)
        cosine_results.append({
            "epsilon":    round(eps, 4),
            "N_clusters": n_clust,
            "metric":     "cosine",
        })

    # ── L1 ε-sweep ───────────────────────────────────────────────────────────
    l1_results = []
    for eps in eps_l1:
        n_clust = count_clusters_l1(mode_dists, eps)
        l1_results.append({
            "epsilon":    round(eps, 4),
            "N_clusters": n_clust,
            "metric":     "l1_mode_dist",
        })

    # ── Plateau detection ────────────────────────────────────────────────────
    def find_plateaus(results: list) -> list:
        plateaus, current = [], None
        for r in results:
            if current is None or r["N_clusters"] != current["N"]:
                if current:
                    plateaus.append(current)
                current = {
                    "N": r["N_clusters"],
                    "eps_start": r["epsilon"],
                    "eps_end":   r["epsilon"],
                    "width":     1,
                }
            else:
                current["eps_end"] = r["epsilon"]
                current["width"]  += 1
        if current:
            plateaus.append(current)
        return plateaus

    cosine_plateaus = find_plateaus(cosine_results)
    l1_plateaus     = find_plateaus(l1_results)

    # ── Go/no-go for Phase 1 ─────────────────────────────────────────────────
    # Criterion: stable N=1 plateau of width >= 3 in cosine sweep
    n1_cosine = [p for p in cosine_plateaus if p["N"] == 1 and p["width"] >= 3]
    gng_cosine = "go"  if n1_cosine else "pending"

    n1_l1 = [p for p in l1_plateaus if p["N"] == 1 and p["width"] >= 3]
    gng_l1 = "go" if n1_l1 else "pending"

    return {
        "cosine": {
            "sweep":    cosine_results,
            "plateaus": cosine_plateaus,
            "go_nogo":  gng_cosine,
        },
        "l1_mode_dist": {
            "sweep":    l1_results,
            "plateaus": l1_plateaus,
            "go_nogo":  gng_l1,
        },
    }


# ── Main runner ───────────────────────────────────────────────────────────────

def run_behavioral_sweep(
    case_dir: Path,
    n_train: int,
    n_eval: int,
    n_seeds: int,
    epsilon_greedy: float,
    eps_cosine: list,
    eps_l1: list,
    verbose: bool = True,
) -> dict:
    """
    Full Phase 1 behavioral sweep over n_seeds random seeds.
    Corresponds to delta_03 (seed robustness) from ScopeSpec.yaml.
    """
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"

    scope  = yaml.safe_load(scope_path.read_text())  if scope_path.exists()  else {}
    record = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}

    print(f"\n{'='*60}")
    print(f"Behavioral sweep: {record.get('id', case_dir.name)}")
    print(f"  n_train={n_train}  n_eval={n_eval}  n_seeds={n_seeds}")
    print(f"  epsilon_greedy={epsilon_greedy}")
    print(f"  eps_cosine: {eps_cosine}")
    print(f"  eps_l1:     {eps_l1}")
    print(f"{'='*60}\n")

    out_dir = case_dir / "results" / "partition"
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_dir = case_dir / "results" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    all_seed_results = []

    for seed_idx in range(n_seeds):
        rng  = np.random.default_rng(seed_idx + 1)
        env  = LabyrinthEnv(grid_size=10, visibility=5, action_cost=0.05,
                            goal_reward=1.0, t_max=500, seed=int(rng.integers(10000)))
        obs_size = env.obs_size
        agent = ModeLibraryAgent(obs_size=obs_size, k=4, d_embed=32,
                                 n_actions=4, lr=0.01, seed=seed_idx)

        print(f"── Seed {seed_idx + 1}/{n_seeds}  (obs_size={obs_size}) ──")

        # Training phase
        train_log = train_agent(env, agent, n_train, epsilon_greedy, rng, verbose=verbose)

        # Save weights for seed 0 (reference)
        if seed_idx == 0:
            agent.save(str(raw_dir / "agent_weights_seed0.npz"))

        # Evaluation phase (new maze layout, same BC)
        eval_env = env.clone_layout(seed=int(rng.integers(10000)))
        eval_log = evaluate_agent(eval_env, agent, n_eval, epsilon_greedy=0.0, rng=rng)

        # Per-seed epsilon sweep
        eps_result = epsilon_sweep_behavioral(eval_log, eps_cosine, eps_l1)

        # Summary stats
        goal_rates = [float(ep["reached_goal"]) for ep in eval_log]
        avg_goal   = float(np.mean(goal_rates))
        avg_entropy= float(np.mean([ep["mode_entropy"] for ep in eval_log]))
        avg_sal    = float(np.mean([ep["salience_mean"] for ep in eval_log]))

        seed_summary = {
            "seed_idx":         seed_idx,
            "n_train":          n_train,
            "n_eval":           n_eval,
            "goal_rate":        round(avg_goal, 4),
            "mean_mode_entropy":round(avg_entropy, 6),
            "mean_salience":    round(avg_sal, 6),
            "final_baseline":   round(float(agent.baseline), 4),
            "epsilon_sweep":    eps_result,
            "eval_log":         eval_log,        # full per-episode data
            "train_returns":    [round(ep["total_reward"], 3) for ep in train_log],
        }
        all_seed_results.append(seed_summary)

        cosine_gng = eps_result["cosine"]["go_nogo"]
        l1_gng     = eps_result["l1_mode_dist"]["go_nogo"]
        print(f"  goal_rate={avg_goal:.2f}  "
              f"entropy={avg_entropy:.3f}  salience={avg_sal:.4f}")
        print(f"  go_nogo: cosine={cosine_gng}  l1={l1_gng}")
        cosine_plateaus = eps_result["cosine"]["plateaus"]
        if cosine_plateaus:
            best = max(cosine_plateaus, key=lambda p: p["width"])
            print(f"  best cosine plateau: N={best['N']}  "
                  f"ε∈[{best['eps_start']},{best['eps_end']}]  width={best['width']}")
        print()

    # ── Aggregate across seeds ───────────────────────────────────────────────
    go_cosine = sum(1 for s in all_seed_results
                    if s["epsilon_sweep"]["cosine"]["go_nogo"] == "go")
    go_l1     = sum(1 for s in all_seed_results
                    if s["epsilon_sweep"]["l1_mode_dist"]["go_nogo"] == "go")
    reproducibility_cosine = go_cosine / n_seeds
    reproducibility_l1     = go_l1     / n_seeds

    # Phase 1 go_nogo: >= 80% of seeds show N=1 plateau
    phase1_gng = "go" if reproducibility_cosine >= 0.8 else "pending"

    aggregate = {
        "case_id":                 record.get("id", case_dir.name),
        "phase":                   "1",
        "n_seeds":                 n_seeds,
        "n_train":                 n_train,
        "n_eval":                  n_eval,
        "reproducibility_cosine":  round(reproducibility_cosine, 3),
        "reproducibility_l1":      round(reproducibility_l1, 3),
        "phase1_go_nogo":          phase1_gng,
        "go_nogo_criterion":       "reproducibility_cosine >= 0.80",
        "seed_results":            all_seed_results,
    }

    # ── Write outputs ────────────────────────────────────────────────────────
    # 1. Full behavioral data
    behavioral_path = raw_dir / "behavioral_data.json"
    behavioral_path.write_text(json.dumps(aggregate, indent=2))
    print(f"Behavioral data → {behavioral_path}")

    # 2. Epsilon sweep summary (compatible structure for inspection)
    # Use seed 0 as representative sweep for EpsilonSweep_behavioral.json
    seed0 = all_seed_results[0]
    eps_summary = {
        "case_id":       record.get("id", case_dir.name),
        "sweep_type":    "behavioral_epsilon",
        "phase":         "1",
        "note": (
            "Labyrinth Phase 1 behavioral ε-sweep. Sweep axis = ε (cosine distance "
            "threshold), not a BC parameter. N_clusters = connected components in "
            "episode embedding space under cosine distance < ε. Representative seed=0."
        ),
        "cosine_sweep":   seed0["epsilon_sweep"]["cosine"]["sweep"],
        "l1_sweep":       seed0["epsilon_sweep"]["l1_mode_dist"]["sweep"],
        "cosine_plateaus":seed0["epsilon_sweep"]["cosine"]["plateaus"],
        "l1_plateaus":    seed0["epsilon_sweep"]["l1_mode_dist"]["plateaus"],
        "reproducibility_cosine": aggregate["reproducibility_cosine"],
        "phase1_go_nogo": phase1_gng,
        "created_at":    time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    eps_path = out_dir / "EpsilonSweep_behavioral.json"
    eps_path.write_text(json.dumps(eps_summary, indent=2))
    print(f"Epsilon sweep  → {eps_path}")

    # 3. Print Phase 1 verdict
    print(f"\n{'='*60}")
    print(f"PHASE 1 VERDICT: {phase1_gng.upper()}")
    print(f"  cosine go/nogo: {go_cosine}/{n_seeds} seeds passed  "
          f"(reproducibility={reproducibility_cosine:.0%})")
    print(f"  l1     go/nogo: {go_l1}/{n_seeds} seeds passed  "
          f"(reproducibility={reproducibility_l1:.0%})")
    if phase1_gng == "go":
        print("  → Discrete partition emerged. Phase 2 (zone switching) may proceed.")
    else:
        print("  → N=1 plateau not reproducible. Check F3 (continuous manifold) or "
              "extend training (increase --train-episodes).")
    print(f"{'='*60}\n")

    return aggregate


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Behavioral sweep for labyrinth Phase 1 (CASE-20260329-0011)."
    )
    parser.add_argument("--case",            required=True,
                        help="Path to case directory, e.g. cases/CASE-20260329-0011")
    parser.add_argument("--train-episodes",  type=int,   default=500,
                        help="Number of training episodes per seed (default 500)")
    parser.add_argument("--eval-episodes",   type=int,   default=100,
                        help="Number of evaluation episodes per seed (default 100)")
    parser.add_argument("--seeds",           type=int,   default=3,
                        help="Number of random seeds for delta_03 robustness (default 3)")
    parser.add_argument("--epsilon-greedy",  type=float, default=0.03,
                        help="Epsilon-greedy exploration probability (default 0.03)")
    parser.add_argument("--quiet",           action="store_true",
                        help="Suppress per-episode training output")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case directory not found: {case_dir}")
        sys.exit(1)

    # ε values from ScopeSpec.yaml stability_window_plan
    eps_cosine = [0.05, 0.08, 0.10, 0.12, 0.15, 0.20]
    eps_l1     = [0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25]

    run_behavioral_sweep(
        case_dir       = case_dir,
        n_train        = args.train_episodes,
        n_eval         = args.eval_episodes,
        n_seeds        = args.seeds,
        epsilon_greedy = args.epsilon_greedy,
        eps_cosine     = eps_cosine,
        eps_l1         = eps_l1,
        verbose        = not args.quiet,
    )


if __name__ == "__main__":
    main()
