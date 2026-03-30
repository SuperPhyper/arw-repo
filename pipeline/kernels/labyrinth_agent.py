"""
pipeline/kernels/labyrinth_agent.py — Mode-Library Agent (Phase 1 Minimal)

Implements the minimal agent architecture for CASE-20260329-0011 (Phase 1).
Architecture maps directly to the ARW role table in
docs/context_navigation/context_navigation_scope_spec.md §4:

    Perception layer        → embedding layer (obs → context_embedding)
    Mode library M          → k independent linear policy heads
    Mode gating / selection → softmax gate over context_embedding
    Salience estimator      → Var_m(mode_fitness) per step
    Anchor memory           → DISABLED (m=0 for Phase 1)
    Sleep / consolidation   → DISABLED for Phase 1 (baseline ablation)

Phase 1 scientific question:
    Do the k=4 mode policies converge to a SINGLE cluster in embedding space
    (N=1, as predicted under uniform Zone A BC), or do they split into
    spurious sub-clusters (continuous manifold → falsification)?

Training algorithm: REINFORCE with running baseline.
    - Gradient flows through: embedding layer → gate → active mode head.
    - One gradient step per episode (Monte Carlo returns).
    - Numerically stable: tanh activations, gradient clipping.

Observables produced per episode (Π_B from ScopeSpec.yaml):
    mode_dist          → empirical distribution over active modes
    policy_embedding   → mean context_embedding over episode steps
    salience_mean      → mean Var_m(mode_fitness) over episode steps
    active_mode_seq    → per-step mode activation sequence
"""

import numpy as np
from typing import Optional


class ModeLibraryAgent:
    """
    Mode-library agent with k learnable policies and a softmax gating network.

    Parameters
    ----------
    obs_size : int
        Dimension of the observation vector from LabyrinthEnv.
    k : int
        Number of behavioral modes. Default 4 (matching ScopeSpec predicted regimes).
    d_embed : int
        Context embedding dimension. Default 32.
    n_actions : int
        Number of discrete actions. Default 4 (UP/DOWN/LEFT/RIGHT).
    lr : float
        REINFORCE learning rate.
    gamma : float
        Return discount factor.
    seed : int | None
        Random seed for weight initialization and epsilon-greedy.
    """

    def __init__(
        self,
        obs_size: int,
        k: int = 4,
        d_embed: int = 32,
        n_actions: int = 4,
        lr: float = 0.01,
        gamma: float = 0.99,
        seed: Optional[int] = None,
    ):
        self.k = k
        self.d = d_embed
        self.n_actions = n_actions
        self.lr = lr
        self.gamma = gamma
        rng = np.random.default_rng(seed)
        scale = 0.05

        # Embedding layer: obs → context_embedding ∈ ℝ^d
        # ARW role: observable projection π: X → D_π
        self.W_emb = rng.normal(0, scale, (d_embed, obs_size)).astype(np.float32)
        self.b_emb = np.zeros(d_embed, dtype=np.float32)

        # Gating network: context_embedding → mode_weights ∈ Δ^k
        # ARW role: admissibility check — selects dominant regime
        self.W_gate = rng.normal(0, scale, (k, d_embed)).astype(np.float32)
        self.b_gate = np.zeros(k, dtype=np.float32)

        # k mode policy heads: context_embedding → action_logits ∈ ℝ^n_actions
        # ARW role: regime representatives (candidate behavioral strategies)
        self.W_modes = [
            rng.normal(0, scale, (n_actions, d_embed)).astype(np.float32)
            for _ in range(k)
        ]
        self.b_modes = [np.zeros(n_actions, dtype=np.float32) for _ in range(k)]

        # Baseline for REINFORCE variance reduction
        self.baseline = 0.0
        self.baseline_alpha = 0.02    # EMA coefficient

    # ── Core forward pass ────────────────────────────────────────────────────

    def _softmax(self, x: np.ndarray) -> np.ndarray:
        x = x - np.max(x)
        e = np.exp(np.clip(x, -50, 50))
        return e / (e.sum() + 1e-12)

    def forward(self, obs: np.ndarray):
        """
        Compute context embedding, mode weights, mixed action distribution,
        and salience.

        Returns
        -------
        emb          : ndarray (d,)   — context embedding
        mode_weights : ndarray (k,)   — softmax gate output
        active_mode  : int            — argmax(mode_weights)
        mixed_probs  : ndarray (n,)   — mixed action distribution
        salience     : float          — Var_m(mode_fitness * mode_weight)
        all_logits   : list[ndarray]  — per-mode action logits (for backprop)
        """
        # Embedding
        emb = np.tanh(self.W_emb @ obs + self.b_emb)       # (d,)

        # Gate
        gate_logits  = self.W_gate @ emb + self.b_gate       # (k,)
        mode_weights = self._softmax(gate_logits)             # (k,)
        active_mode  = int(np.argmax(mode_weights))

        # Mode policy heads
        all_logits = [self.W_modes[i] @ emb + self.b_modes[i] for i in range(self.k)]
        all_probs  = [self._softmax(lg) for lg in all_logits]

        # Mixed policy: weighted sum of mode action distributions
        mixed_probs = sum(mode_weights[i] * all_probs[i] for i in range(self.k))
        mixed_probs = mixed_probs / (mixed_probs.sum() + 1e-12)

        # Salience: Var over mode-weighted peak-action probabilities
        # S(c) = Var_m(mode_weight_i * max_a p_i(a))
        # High salience → modes compete strongly → scope boundary proximity
        mode_fitness = np.array([
            mode_weights[i] * float(np.max(all_probs[i]))
            for i in range(self.k)
        ])
        salience = float(np.var(mode_fitness))

        return emb, mode_weights, active_mode, mixed_probs, salience, all_logits

    def select_action(
        self,
        obs: np.ndarray,
        epsilon_greedy: float = 0.03,
        rng: Optional[np.random.Generator] = None,
    ):
        """
        Select action using mixed policy + epsilon-greedy exploration.

        Returns (action, emb, mode_weights, active_mode, salience)
        """
        emb, mode_weights, active_mode, mixed_probs, salience, _ = self.forward(obs)

        if rng is not None and rng.random() < epsilon_greedy:
            action = int(rng.integers(0, self.n_actions))
        else:
            action = int(np.argmax(mixed_probs))

        return action, emb, mode_weights, active_mode, salience

    # ── REINFORCE update ─────────────────────────────────────────────────────

    def update(self, trajectory: list, rng: Optional[np.random.Generator] = None):
        """
        Update all weights using REINFORCE with running baseline.

        trajectory : list of (obs, action, reward, emb, mode_weights, all_logits)
            — one entry per environment step.

        Gradient derivation:
            π(a|s) = Σ_i w_i(s) · p_i(a|s)        mixed policy
            ∇_θ log π(a|s) = Σ_i [p_i(a) / π(a)] · ∇_θ (w_i · p_i)
            Applied via one-sample REINFORCE: loss = -log π(a) · advantage
        """
        if not trajectory:
            return

        # Compute discounted returns G_t
        G = 0.0
        returns = []
        for _, _, rew, *_ in reversed(trajectory):
            G = rew + self.gamma * G
            returns.insert(0, G)

        # Update baseline (EMA)
        episode_return = returns[0]
        self.baseline += self.baseline_alpha * (episode_return - self.baseline)

        clip = 1.0   # gradient clipping magnitude

        for t, (obs, action, _, emb, mode_weights, all_logits) in enumerate(trajectory):
            advantage = returns[t] - self.baseline

            # Recompute mixed probs from stored values
            all_probs = [self._softmax(lg) for lg in all_logits]
            mixed_p   = sum(mode_weights[i] * all_probs[i] for i in range(self.k))
            pi_a      = float(mixed_p[action]) + 1e-12

            # ── Mode policy head gradients ───────────────────────────────
            for i in range(self.k):
                # ∂log_π/∂logits_i via chain rule:
                # ∂log_π/∂p_i[a'] = mode_weights[i] / π(a)  (for a' = action)
                # ∂log_π/∂logits_i = (mode_weights[i]/π(a)) * ∂p_i/∂logits_i
                #                   = (mode_weights[i]/π(a)) * (δ_{a,a'} - p_i[a'])
                scale_i = float(mode_weights[i]) / pi_a
                d_softmax_i = -all_probs[i].copy()
                d_softmax_i[action] += 1.0          # δ_{a, action}
                d_logits_i = scale_i * d_softmax_i  # (n_actions,)

                grad_W = np.outer(d_logits_i, emb) * advantage
                grad_b = d_logits_i * advantage
                np.clip(grad_W, -clip, clip, out=grad_W)
                np.clip(grad_b, -clip, clip, out=grad_b)
                self.W_modes[i] += self.lr * grad_W
                self.b_modes[i] += self.lr * grad_b

            # ── Gate gradients ───────────────────────────────────────────
            # ∂log_π/∂w_i = p_i(action) / π(action)
            # ∂log_π/∂gate_logits via softmax Jacobian:
            # δ = ∂log_π/∂w  = [p_i(a)/π(a) for i in 1..k]
            # ∂w/∂gate_logits = diag(w) - w·w^T  (softmax Jacobian)
            d_w = np.array([all_probs[i][action] / pi_a for i in range(self.k)])
            w   = mode_weights
            jac = np.diag(w) - np.outer(w, w)   # (k, k)
            d_gate_logits = jac @ d_w            # (k,)
            d_gate_logits *= advantage

            grad_Wg = np.outer(d_gate_logits, emb)
            np.clip(grad_Wg, -clip, clip, out=grad_Wg)
            np.clip(d_gate_logits, -clip, clip, out=d_gate_logits)
            self.W_gate += self.lr * grad_Wg
            self.b_gate += self.lr * d_gate_logits

            # ── Embedding gradients ──────────────────────────────────────
            # Sum contributions from all mode heads + gate, through tanh
            d_emb = np.zeros(self.d, dtype=np.float32)
            for i in range(self.k):
                d_logits_i = (float(mode_weights[i]) / pi_a) * (
                    -all_probs[i] + (np.arange(self.n_actions) == action).astype(float)
                ) * advantage
                d_emb += self.W_modes[i].T @ d_logits_i

            d_emb += self.W_gate.T @ (d_gate_logits)
            d_tanh = (1.0 - emb ** 2) * d_emb    # tanh derivative
            np.clip(d_tanh, -clip, clip, out=d_tanh)

            self.W_emb += self.lr * 0.3 * np.outer(d_tanh, obs)
            self.b_emb += self.lr * 0.3 * d_tanh

    # ── Observable extraction (Π_B) ──────────────────────────────────────────

    def get_mode_dist(self, mode_seq: list) -> np.ndarray:
        """
        Compute mode_dist from a sequence of active mode indices.
        Returns empirical distribution over k modes (sums to 1).
        Implements the primary observable π_01 from ScopeSpec.yaml.
        """
        counts = np.zeros(self.k, dtype=np.float32)
        for m in mode_seq:
            counts[m] += 1
        total = counts.sum()
        return counts / total if total > 0 else counts

    def get_embedding_centroid(self, emb_seq: list) -> np.ndarray:
        """
        Mean context_embedding over an episode.
        Implements the secondary observable π_02 (policy_embedding centroid).
        """
        if not emb_seq:
            return np.zeros(self.d, dtype=np.float32)
        return np.mean(np.stack(emb_seq), axis=0)

    def save(self, path: str):
        """Save weight arrays to .npz file."""
        np.savez(
            path,
            W_emb=self.W_emb, b_emb=self.b_emb,
            W_gate=self.W_gate, b_gate=self.b_gate,
            **{f"W_mode_{i}": self.W_modes[i] for i in range(self.k)},
            **{f"b_mode_{i}": self.b_modes[i] for i in range(self.k)},
        )

    def load(self, path: str):
        """Load weight arrays from .npz file."""
        d = np.load(path)
        self.W_emb  = d["W_emb"];  self.b_emb  = d["b_emb"]
        self.W_gate = d["W_gate"]; self.b_gate = d["b_gate"]
        self.W_modes = [d[f"W_mode_{i}"] for i in range(self.k)]
        self.b_modes = [d[f"b_mode_{i}"] for i in range(self.k)]
