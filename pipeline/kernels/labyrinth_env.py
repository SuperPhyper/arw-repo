"""
pipeline/kernels/labyrinth_env.py — Labyrinth Grid Environment

ART instantiation of the context-navigation labyrinth experiment (CASE-20260329-0011).
Implements the Zone A boundary conditions from ScopeSpec.yaml:

    B_Zone_A = (d=5, r=5, c=0.05, m=0, tau=lenient)

    - Planning budget d=5: agent may look ahead up to 5 steps
    - Visibility radius r=5: local observation covers (2r+1)×(2r+1) = 121 cells
    - Action cost c=0.05: low step penalty; exploration is economically viable
    - Memory capacity m=0: no anchor memory (disabled for Phase 1)
    - Error tolerance tau=lenient: wall collisions are non-destructive (agent stays)

State space X:
    x = (grid_position, local_observation, episode_step)
    grid_position  ∈ {0,...,9}²      (10×10 grid)
    local_observation ∈ {0, 0.5, 1}^121  (empty / goal / wall)
    episode_step   ∈ {0,...,T_max}

Actions: UP=0, DOWN=1, LEFT=2, RIGHT=3  (4 cardinal directions)

The environment is generated once per LabyrinthEnv instantiation using a
randomized-DFS perfect maze. All cells are reachable; a single path exists
between any two cells (plus any additionally opened walls).
"""

import numpy as np
from typing import Optional


# ── Action encoding ──────────────────────────────────────────────────────────

ACTION_DELTAS = {
    0: (-1,  0),   # UP    (row decreases)
    1: ( 1,  0),   # DOWN
    2: ( 0, -1),   # LEFT  (col decreases)
    3: ( 0,  1),   # RIGHT
}
N_ACTIONS = 4


# ── Environment ──────────────────────────────────────────────────────────────

class LabyrinthEnv:
    """
    10×10 grid labyrinth with Zone A boundary conditions (Phase 1).

    Observation vector (size = (2r+1)^2 + 3):
        [0 .. (2r+1)^2 - 1]  local grid scan within radius r, row-major
            0.0  = empty cell
            0.5  = goal cell
            1.0  = wall or out-of-bounds
        [-3]  normalised delta_col to goal  (dx in [-1, 1])
        [-2]  normalised delta_row to goal  (dy in [-1, 1])
        [-1]  episode progress = step / T_max   (in [0, 1])
    """

    START = (0, 0)

    def __init__(
        self,
        grid_size: int = 10,
        visibility: int = 5,
        action_cost: float = 0.05,
        goal_reward: float = 1.0,
        t_max: int = 500,
        seed: Optional[int] = None,
        extra_openings: int = 5,
    ):
        self.G = grid_size
        self.r = visibility
        self.c = action_cost
        self.goal_reward = goal_reward
        self.T = t_max
        self.rng = np.random.default_rng(seed)
        self.goal = (grid_size - 1, grid_size - 1)

        # Generate maze (walls array: True = wall, False = open)
        self.walls = self._generate_maze(extra_openings)

        # Observation size: (2r+1)^2 local cells + 3 scalar features
        self.obs_size = (2 * self.r + 1) ** 2 + 3

        # Runtime state
        self.pos = self.START
        self.step_count = 0

    # ── Maze generation ──────────────────────────────────────────────────────

    def _generate_maze(self, extra_openings: int = 5) -> np.ndarray:
        """
        Randomized DFS perfect maze on a grid of odd-indexed cells.
        Works on a 2n-1 × 2n-1 grid where cells are at even indices.
        Adapted to fit exactly into self.G × self.G by treating every cell
        as a node and every wall as a separating edge.
        """
        G = self.G
        rng = self.rng
        walls = np.ones((G, G), dtype=bool)   # start: everything is a wall

        visited = np.zeros((G, G), dtype=bool)

        def neighbours_dfs(r: int, c: int):
            """2-step neighbours for DFS (carve through walls)."""
            ns = []
            for dr, dc in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < G and 0 <= nc < G and not visited[nr, nc]:
                    ns.append((nr, nc, r + dr // 2, c + dc // 2))
            return ns

        # Carve starting from (0,0)
        stack = [(0, 0)]
        visited[0, 0] = True
        walls[0, 0] = False

        while stack:
            row, col = stack[-1]
            ns = neighbours_dfs(row, col)
            if ns:
                idx = rng.integers(len(ns))
                nr, nc, wr, wc = ns[idx]
                visited[nr, nc] = True
                walls[nr, nc] = False
                walls[wr, wc] = False     # carve the wall between cells
                stack.append((nr, nc))
            else:
                stack.pop()

        # Ensure start and goal are open
        walls[self.START] = False
        walls[self.goal]  = False

        # Open a few extra walls to increase path density (Zone A: exploration)
        opened = 0
        attempts = 0
        while opened < extra_openings and attempts < 200:
            wr = int(rng.integers(1, G - 1))
            wc = int(rng.integers(1, G - 1))
            if walls[wr, wc]:
                walls[wr, wc] = False
                opened += 1
            attempts += 1

        return walls

    # ── Episode control ──────────────────────────────────────────────────────

    def reset(self) -> np.ndarray:
        """Reset to start position; return initial observation."""
        self.pos = self.START
        self.step_count = 0
        return self._get_obs()

    def step(self, action: int):
        """
        Execute action.
        Returns (obs, reward, done, info).

        tau=lenient: wall hits leave position unchanged (no penalty beyond -c).
        """
        dr, dc = ACTION_DELTAS[action]
        nr, nc = self.pos[0] + dr, self.pos[1] + dc

        if 0 <= nr < self.G and 0 <= nc < self.G and not self.walls[nr, nc]:
            self.pos = (nr, nc)
        # else: wall hit — position unchanged (lenient error tolerance)

        self.step_count += 1
        reward = -self.c        # action cost always applies

        done = (self.pos == self.goal)
        if done:
            reward += self.goal_reward

        if self.step_count >= self.T:
            done = True

        info = {
            "pos":       self.pos,
            "reached":   done and (self.pos == self.goal),
            "step":      self.step_count,
        }
        return self._get_obs(), reward, done, info

    # ── Observation ──────────────────────────────────────────────────────────

    def _get_obs(self) -> np.ndarray:
        """
        Build observation vector: local grid scan + goal direction + step fraction.
        Cells outside grid bounds are treated as walls (1.0).
        """
        r = self.r
        pr, pc = self.pos
        G = self.G

        # Local grid scan: (2r+1)^2 values, row-major
        local = []
        for dr in range(-r, r + 1):
            for dc in range(-r, r + 1):
                nr, nc = pr + dr, pc + dc
                if 0 <= nr < G and 0 <= nc < G:
                    if (nr, nc) == self.goal:
                        local.append(0.5)    # goal marker
                    elif self.walls[nr, nc]:
                        local.append(1.0)    # wall
                    else:
                        local.append(0.0)    # empty
                else:
                    local.append(1.0)        # out-of-bounds = wall

        # Goal direction (normalised by grid size)
        gr, gc = self.goal
        dx = (gc - pc) / self.G      # positive = goal is to the right
        dy = (gr - pr) / self.G      # positive = goal is below

        # Episode progress
        prog = self.step_count / self.T

        obs = np.array(local + [dx, dy, prog], dtype=np.float32)
        assert len(obs) == self.obs_size, f"obs size mismatch: {len(obs)} != {self.obs_size}"
        return obs

    # ── Utilities ────────────────────────────────────────────────────────────

    def render_ascii(self) -> str:
        """Return ASCII representation of current maze state."""
        lines = []
        for r in range(self.G):
            row = []
            for c in range(self.G):
                if (r, c) == self.pos:
                    row.append("A")
                elif (r, c) == self.goal:
                    row.append("G")
                elif self.walls[r, c]:
                    row.append("█")
                else:
                    row.append("·")
            lines.append(" ".join(row))
        return "\n".join(lines)

    def clone_layout(self, seed: Optional[int] = None) -> "LabyrinthEnv":
        """Return a new env with the same BC parameters but a different maze."""
        return LabyrinthEnv(
            grid_size=self.G,
            visibility=self.r,
            action_cost=self.c,
            goal_reward=self.goal_reward,
            t_max=self.T,
            seed=seed,
        )
