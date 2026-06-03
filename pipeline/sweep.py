"""
pipeline/sweep.py — BC Parameter Sweep Runner

Reads BCManifest.yaml to determine sweep parameters, runs the simulation
kernel for the specified system, and writes raw trajectory/state data to
results/raw/.

Currently implemented kernels:
    kuramoto   — Kuramoto oscillator synchronization
    pendulum   — Multi-link pendulum (stub)
    consensus  — Opinion dynamics ABM (stub)
    meanfield  — Mean-field ODE (stub)
    labyrinth  — Context-navigation agent (stub)

Usage:
    python -m pipeline.sweep --case cases/CASE-... --out results/raw
    python -m pipeline.sweep --case cases/CASE-... --dry-run
"""

import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path

try:
    import yaml
    import numpy as np
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    print("Run: pip install pyyaml numpy --break-system-packages")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent


# ── Simulation Kernels ───────────────────────────────────────────────────────

def run_kuramoto(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    Kuramoto oscillator model.
    S_K: N oscillators, coupling κ, natural frequencies ωᵢ ~ N(0,1).
    Observable: order parameter r(t) = |1/N Σ exp(i θⱼ)|
    Regime partition R_K: Incoherent (r≈0) | Partial | Synchronized (r≈1)
    Analytical K_c = 2/π·g(0) ≈ 2/π for g = N(0,1)  →  K_c ≈ 0.6366
    """
    N        = params.get("N", 500)
    T        = params.get("T", 200)
    dt       = params.get("dt", 0.05)
    kappa    = sweep_point["kappa"]
    seed     = sweep_point.get("seed", 42)

    rng_local = np.random.default_rng(seed)
    omega = rng_local.standard_normal(N)          # natural frequencies
    theta = rng_local.uniform(0, 2*np.pi, N)      # initial phases

    n_steps  = int(T / dt)
    r_series = np.zeros(n_steps)

    for t in range(n_steps):
        # Mean-field coupling
        psi   = np.angle(np.mean(np.exp(1j * theta)))
        r     = np.abs(np.mean(np.exp(1j * theta)))
        dtheta = omega + kappa * r * np.sin(psi - theta)
        theta  = theta + dt * dtheta
        r_series[t] = r

    # Steady-state: last 20% of trajectory
    r_ss = float(np.mean(r_series[int(0.8 * n_steps):]))
    r_std = float(np.std(r_series[int(0.8 * n_steps):]))

    return {
        "kappa":     kappa,
        "r_ss":      r_ss,
        "r_std":     r_std,
        "r_series":  r_series[-100:].tolist(),   # save last 100 steps only
        "N":         N,
        "T":         T,
    }


def run_pendulum(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    Two-link planar pendulum with passive joint coupling.
    S_P = (B_P, Pi_P, Delta_P, epsilon_P)

    State: x = (theta_1, theta_2, dtheta_1, dtheta_2)
    Observables:
        pi_01: lambda_proxy  — finite-time Lyapunov exponent proxy (chaos indicator)
        pi_02: Var_rel       — variance of (theta_1 - theta_2) in steady state

    Regime partition R_P:
        R_P1 Periodic:       lambda_proxy < 0,    Var_rel >= 0.01
        R_P2 Quasi-periodic: lambda_proxy in [-0.05, 0.05], Var_rel moderate
        R_P3 Chaotic:        lambda_proxy > 0.05
        R_P4 Locked:         Var_rel < 0.001  (links move as unit)

    Primary sweep parameter: kappa (joint stiffness)
    """
    try:
        from scipy.integrate import solve_ivp
    except ImportError:
        return {"status": "error", "note": "scipy not installed. Run: pip install scipy --break-system-packages"}

    kappa  = float(sweep_point.get("kappa", 1.0))
    gamma  = float(params.get("gamma", 0.1))    # damping
    A      = float(params.get("A", 0.0))        # driving amplitude (0 = free)
    Omega  = float(params.get("Omega", 0.67))   # driving frequency
    m      = float(params.get("m", 1.0))        # link mass
    L      = float(params.get("L", 1.0))        # link length
    g      = 9.81
    T_end  = float(params.get("T", 80.0))
    T_trans = float(params.get("T_transient", 30.0))
    seed   = int(sweep_point.get("seed", 42))
    n_ic   = int(params.get("n_ic", 3))          # ICs for lambda_proxy averaging

    def pendulum_ode(t, y):
        th1, th2, dth1, dth2 = y
        # Equations of motion (simplified equal-mass, equal-length, small-angle safe)
        # Full nonlinear EOM for two-link pendulum
        delta = th2 - th1

        # Denominator terms
        den = 2*m*L**2 * (2 - np.cos(delta)**2) + 1e-12

        # Driving torque on link 1
        tau_drive = A * np.cos(Omega * t) if A > 0 else 0.0

        ddth1 = (
            2*m*L**2 * (dth2**2 * np.sin(delta) - 2*g/L * np.sin(th1))
            + m*L**2 * (dth1**2 * np.sin(delta) * np.cos(delta) - g/L * np.sin(th2) * np.cos(delta))
            - kappa * (th1 - th2)
            - gamma * dth1
            + tau_drive
        ) / den

        ddth2 = (
            m*L**2 * (-dth1**2 * np.sin(delta) + 2*g/L * (np.sin(th1)*np.cos(delta) - np.sin(th2)))
            + kappa * (th1 - th2)
            - gamma * dth2
        ) / den

        return [dth1, dth2, ddth1, ddth2]

    rng_local = np.random.default_rng(seed)

    # Small ICs: start near equilibrium so low-kappa regimes are accessible
    # IC amplitude scales inversely with kappa: high kappa -> even smaller ICs (near locked)
    ic_amp = min(0.25, max(0.05, 0.3 / (1.0 + kappa)))

    # ── Steady-state trajectory for Var_rel ─────────────────────────────────
    y0_base = rng_local.uniform([-ic_amp, -ic_amp, 0, 0], [ic_amp, ic_amp, 0, 0])
    try:
        sol = solve_ivp(pendulum_ode, [0, T_end], y0_base,
                        method="RK45", max_step=0.02, dense_output=False,
                        rtol=1e-8, atol=1e-10)
        if not sol.success:
            raise RuntimeError(sol.message)
        i_trans = np.searchsorted(sol.t, T_trans)
        th1_ss = sol.y[0, i_trans:]
        th2_ss = sol.y[1, i_trans:]
        var_rel = float(np.var(th1_ss - th2_ss))
    except Exception as e:
        return {"status": "error", "note": str(e), "sweep_point": sweep_point}

    # ── Lambda proxy: finite-time divergence rate ────────────────────────────
    # Use same small ICs for consistency with var_rel measurement
    lambda_proxies = []
    T_lyap = 30.0
    delta_x0_mag = 1e-7
    for i in range(n_ic):
        y0 = rng_local.uniform([-ic_amp, -ic_amp, 0, 0], [ic_amp, ic_amp, 0, 0])
        d0 = rng_local.standard_normal(4)
        d0 = d0 / np.linalg.norm(d0) * delta_x0_mag
        y0_pert = y0 + d0
        try:
            s1 = solve_ivp(pendulum_ode, [0, T_lyap], y0,
                           method="RK45", max_step=0.02, rtol=1e-8, atol=1e-10)
            s2 = solve_ivp(pendulum_ode, [0, T_lyap], y0_pert,
                           method="RK45", max_step=0.02, rtol=1e-8, atol=1e-10)
            if s1.success and s2.success:
                dT = np.linalg.norm(s1.y[:, -1] - s2.y[:, -1])
                lp = (1.0 / T_lyap) * np.log(max(dT, 1e-20) / delta_x0_mag)
                lambda_proxies.append(lp)
        except Exception:
            pass

    lambda_proxy = float(np.mean(lambda_proxies)) if lambda_proxies else 0.0

    # ── Regime labeling ──────────────────────────────────────────────────────
    # Var_rel < 0.0005: links tightly locked (R_P4)
    # lambda_proxy > 0.08: clearly chaotic (R_P3)
    # lambda_proxy < 0.0: negative divergence = periodic/stable (R_P1)
    # otherwise: quasi-periodic / transition (R_P2)
    if var_rel < 0.0005:
        regime_label, regime_id = "Locked", 3
    elif lambda_proxy > 0.08:
        regime_label, regime_id = "Chaotic", 2
    elif lambda_proxy < 0.0:
        regime_label, regime_id = "Periodic", 0
    else:
        regime_label, regime_id = "Quasi_periodic", 1

    return {
        "status":        "ok",
        "kappa":         kappa,
        "gamma":         gamma,
        "lambda_proxy":  round(lambda_proxy, 6),
        "var_rel":       round(var_rel, 6),
        "regime_label":  regime_label,
        "regime_id":     regime_id,
        "n_ic_used":     len(lambda_proxies),
    }


def run_consensus(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """Stub — opinion dynamics ABM."""
    return {"status": "stub", "sweep_point": sweep_point,
            "note": "Implement Deffuant/HK model in pipeline/kernels/consensus.py"}


def run_meanfield(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """Stub — mean-field ODE over opinion density."""
    return {"status": "stub", "sweep_point": sweep_point,
            "note": "Implement mean-field ODE in pipeline/kernels/meanfield.py"}


def run_labyrinth(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    Context-navigation agent — Phase 1 behavioral sweep.

    NOTE: The labyrinth system does not use a BC parameter sweep.
    Use pipeline.sweep_behavioral instead of pipeline.sweep for this system:

        python -m pipeline.sweep_behavioral --case cases/CASE-20260329-0011

    This function is retained for interface compatibility but redirects
    to the behavioral adapter, which performs training + ε-sweep
    over policy embeddings (cosine distance) and mode_dist (L1).
    """
    try:
        from pipeline.sweep_behavioral import run_behavioral_sweep
        import yaml
        from pathlib import Path

        case_id = params.get("case_id", "")
        repo_root = Path(__file__).parent.parent
        case_dir = None

        # Try to locate case directory by id
        for candidate in (repo_root / "cases").iterdir():
            if candidate.is_dir() and (case_id in candidate.name or not case_id):
                if (candidate / "BCManifest.yaml").exists():
                    bcm = yaml.safe_load((candidate / "BCManifest.yaml").read_text())
                    if bcm.get("id", "").endswith("0011"):
                        case_dir = candidate
                        break

        if case_dir is None:
            return {
                "status": "redirect",
                "note": (
                    "Labyrinth uses pipeline.sweep_behavioral (not pipeline.sweep). "
                    "Run: python -m pipeline.sweep_behavioral "
                    "--case cases/CASE-20260329-0011"
                ),
            }

        result = run_behavioral_sweep(
            case_dir=case_dir,
            n_train=params.get("n_training_episodes", 500),
            n_eval=params.get("n_eval_episodes", 100),
            n_seeds=params.get("n_seeds", 3),
            epsilon_greedy=params.get("epsilon_greedy", 0.03),
            eps_cosine=[0.05, 0.08, 0.10, 0.12, 0.15, 0.20],
            eps_l1=[0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25],
            verbose=False,
        )
        return {"status": "ok", "phase1_go_nogo": result.get("phase1_go_nogo"),
                "reproducibility_cosine": result.get("reproducibility_cosine")}

    except Exception as e:
        return {"status": "error", "note": str(e),
                "redirect": "python -m pipeline.sweep_behavioral --case cases/CASE-20260329-0011"}


def run_double_pendulum(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    Classical double pendulum — two rigid links connected by a free
    rotational joint, suspended from a fixed pivot.

    State: x = (θ₁, θ₂, dθ₁, dθ₂)
      θ₁: angle of upper link from vertical
      θ₂: angle of lower link from vertical

    Physical parameters (from params or sweep_point):
      m1, m2:    link masses [kg]
      L1, L2:    link lengths [m]
      gamma:     damping coefficient [1/s] (0 = conservative)
      A, Omega:  external driving amplitude [N·m] and frequency [rad/s]

    Sweep parameters (any of the above, plus):
      E_target:  target total energy — sets IC amplitude

    Observables:
      lambda_proxy:  finite-time Lyapunov exponent proxy (chaos indicator)
      var_rel:       Var(θ₁ - θ₂) in steady state (relative motion)
      E_mean:        mean total energy in steady state

    Regime partition R_DP:
      Periodic:       lambda_proxy < 0
      Quasi-periodic: 0 ≤ lambda_proxy ≤ 0.1
      Chaotic:        lambda_proxy > 0.1
    """
    try:
        from scipy.integrate import solve_ivp
    except ImportError:
        return {"status": "error",
                "note": "scipy not installed. Run: pip install scipy --break-system-packages"}

    # ── Parameters: sweep_point overrides params ─────────────────────────
    def p(name, default):
        return float(sweep_point.get(name, params.get(name, default)))

    m1    = p("m1", 1.0)
    m2    = p("m2", 1.0)
    L1    = p("L1", 1.0)
    L2    = p("L2", 1.0)
    gamma = p("gamma", 0.0)       # 0 = no damping (classical)
    A     = p("A", 0.0)           # 0 = no driving (free)
    Omega = p("Omega", 2.0/3.0)   # driving frequency
    g_acc = 9.81

    T_end   = p("T", 60.0)
    T_trans = p("T_transient", 20.0)
    seed    = int(sweep_point.get("seed", 42))
    n_ic    = int(params.get("n_ic", 5))

    # Energy target for IC generation
    E_target = sweep_point.get("E_target", params.get("E_target", None))

    # ── Equations of motion ──────────────────────────────────────────────
    # Full nonlinear EOM for a planar double pendulum
    # (angles measured from vertical, standard Lagrangian derivation)
    def eom(t, y):
        th1, th2, w1, w2 = y
        delta = th2 - th1
        cos_d = np.cos(delta)
        sin_d = np.sin(delta)

        M = m1 + m2
        den = M * L1 - m2 * L1 * cos_d**2

        # Driving torque on upper link
        tau = A * np.cos(Omega * t) if A > 0 else 0.0

        dw1 = (m2 * L1 * w1**2 * sin_d * cos_d
               + m2 * g_acc * np.sin(th2) * cos_d
               + m2 * L2 * w2**2 * sin_d
               - M * g_acc * np.sin(th1)
               - gamma * w1 + tau) / den

        dw2 = (-m2 * L2 * w2**2 * sin_d * cos_d
               - M * g_acc * np.sin(th2)
               + M * L1 * w1**2 * sin_d
               + M * g_acc * np.sin(th1) * cos_d
               - gamma * w2) / (M * L2 / m2 - L2 * cos_d**2 + 1e-12)

        return [w1, w2, dw1, dw2]

    # ── Total energy ─────────────────────────────────────────────────────
    def total_energy(th1, th2, w1, w2):
        # Kinetic energy
        T_kin = (0.5 * (m1 + m2) * L1**2 * w1**2
                 + 0.5 * m2 * L2**2 * w2**2
                 + m2 * L1 * L2 * w1 * w2 * np.cos(th1 - th2))
        # Potential energy (zero at both links hanging down)
        V = (-(m1 + m2) * g_acc * L1 * np.cos(th1)
             - m2 * g_acc * L2 * np.cos(th2))
        return T_kin + V

    # ── Initial conditions ───────────────────────────────────────────────
    rng_local = np.random.default_rng(seed)

    if E_target is not None:
        E_target = float(E_target)
        # Set IC amplitude to approximately match target energy
        # For small angles: E ≈ (m1+m2)*g*L1*θ₁² + m2*g*L2*θ₂²
        # Scale angle amplitude to hit E_target
        E_ref = (m1 + m2) * g_acc * L1 + m2 * g_acc * L2
        if E_ref > 0:
            amp = min(np.pi * 0.95, np.sqrt(abs(E_target) / E_ref))
        else:
            amp = 0.5
    else:
        amp = 0.5  # default: moderate amplitude

    # ── Steady-state trajectory for Var_rel and E_mean ───────────────────
    y0 = rng_local.uniform([-amp, -amp, 0, 0], [amp, amp, 0, 0])
    try:
        sol = solve_ivp(eom, [0, T_end], y0, method="RK45",
                        max_step=0.02, rtol=1e-8, atol=1e-10)
        if not sol.success:
            raise RuntimeError(sol.message)

        i_trans = np.searchsorted(sol.t, T_trans)
        th1_ss = sol.y[0, i_trans:]
        th2_ss = sol.y[1, i_trans:]
        w1_ss  = sol.y[2, i_trans:]
        w2_ss  = sol.y[3, i_trans:]

        var_rel = float(np.var(th1_ss - th2_ss))
        E_series = total_energy(th1_ss, th2_ss, w1_ss, w2_ss)
        E_mean = float(np.mean(E_series))
        E_std  = float(np.std(E_series))
    except Exception as e:
        return {"status": "error", "note": str(e), "sweep_point": sweep_point}

    # ── Lyapunov proxy ───────────────────────────────────────────────────
    lambda_proxies = []
    T_lyap = 30.0
    delta_x0_mag = 1e-7

    for i in range(n_ic):
        y0_i = rng_local.uniform([-amp, -amp, 0, 0], [amp, amp, 0, 0])
        d0 = rng_local.standard_normal(4)
        d0 = d0 / np.linalg.norm(d0) * delta_x0_mag
        y0_pert = y0_i + d0
        try:
            s1 = solve_ivp(eom, [0, T_lyap], y0_i,
                           method="RK45", max_step=0.02, rtol=1e-8, atol=1e-10)
            s2 = solve_ivp(eom, [0, T_lyap], y0_pert,
                           method="RK45", max_step=0.02, rtol=1e-8, atol=1e-10)
            if s1.success and s2.success:
                dT = np.linalg.norm(s1.y[:, -1] - s2.y[:, -1])
                lp = (1.0 / T_lyap) * np.log(max(dT, 1e-20) / delta_x0_mag)
                lambda_proxies.append(lp)
        except Exception:
            pass

    lambda_proxy = float(np.mean(lambda_proxies)) if lambda_proxies else 0.0

    return {
        "status":        "ok",
        "m1": m1, "m2": m2, "L1": L1, "L2": L2,
        "gamma": gamma, "A": A, "Omega": Omega,
        "E_target":      E_target,
        "E_mean":        round(E_mean, 6),
        "E_std":         round(E_std, 6),
        "lambda_proxy":  round(lambda_proxy, 6),
        "var_rel":       round(var_rel, 6),
        "ic_amplitude":  round(amp, 6),
        "n_ic_used":     len(lambda_proxies),
    }


def run_sir_epidemic(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    ODE-based SIR epidemic model — pure numpy RK4 (no scipy dependency).
    BC class: Aggregation (SIR is a quotient projection of N micro-states to 3 compartments).

    dS/dt = -beta*S*I,  dI/dt = beta*S*I - gamma_r*I,  dR/dt = gamma_r*I

    Primary observable: I_peak = max_t I(t)  (peak infected fraction)
    Secondary: R_final = R(T) ~= R_infinity
    """
    beta    = float(sweep_point.get("beta", 0.1))
    gamma_r = float(params.get("gamma_r", 0.1))
    S0      = float(params.get("S0", 0.99))
    I0      = float(params.get("I0", 0.01))
    R0_ic   = float(params.get("R0", 0.0))
    T       = float(params.get("T", 500.0))
    dt      = float(params.get("dt", 0.1))

    def f(y):
        S, I, R = y
        return np.array([-beta*S*I, beta*S*I - gamma_r*I, gamma_r*I])

    y = np.array([S0, I0, R0_ic])
    n_steps = int(T / dt)
    I_peak = I0
    for _ in range(n_steps):
        k1 = f(y)
        k2 = f(y + 0.5*dt*k1)
        k3 = f(y + 0.5*dt*k2)
        k4 = f(y + dt*k3)
        y  = y + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)
        y  = np.clip(y, 0.0, 1.0)  # numerical safety
        if y[1] > I_peak:
            I_peak = y[1]

    return {
        "status":               "ok",
        "beta":                 beta,
        "gamma_r":              gamma_r,
        "I_peak":               round(float(I_peak), 6),
        "R_final":              round(float(y[2]), 6),
        "beta_star_analytical": round(gamma_r / S0, 6),
    }


def run_pendulum_gamma(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    Multi-link pendulum with gamma (damping) sweep — Dissipation BC case (CASE-0005).
    Pure-numpy RK4 integrator (no scipy dependency).

    State: y = (theta_1, theta_2, dtheta_1, dtheta_2)
    Primary observable: var_rel = Var(theta_1 - theta_2) in steady state [T_trans, T]
    Secondary observable: energy_ss = mean(0.5*(dtheta_1^2 + dtheta_2^2)) in steady state

    BC class: Dissipation
    Sweep parameter: gamma (joint damping coefficient)
    Fixed: kappa (joint stiffness, above Coupling transition from CASE-0002)
    """
    gamma   = float(sweep_point.get("gamma", 0.5))
    kappa   = float(params.get("kappa", 3.25))
    m       = float(params.get("m", 1.0))
    L       = float(params.get("L", 1.0))
    g_grav  = 9.81
    T_end   = float(params.get("T", 500.0))
    T_trans = float(params.get("T_transient", 300.0))
    dt      = float(params.get("dt", 0.02))
    n_ic    = int(params.get("n_ic", 10))
    seed    = int(sweep_point.get("seed", 42))

    def pend_ode(y):
        th1, th2, dth1, dth2 = y
        delta = th2 - th1
        den = 2 * m * L**2 * (2 - np.cos(delta)**2) + 1e-12
        ddth1 = (
            2 * m * L**2 * (dth2**2 * np.sin(delta) - 2 * g_grav / L * np.sin(th1))
            + m * L**2 * (dth1**2 * np.sin(delta) * np.cos(delta)
                          - g_grav / L * np.sin(th2) * np.cos(delta))
            - kappa * (th1 - th2)
            - gamma * dth1
        ) / den
        ddth2 = (
            m * L**2 * (-dth1**2 * np.sin(delta)
                        + 2 * g_grav / L * (np.sin(th1) * np.cos(delta) - np.sin(th2)))
            + kappa * (th1 - th2)
            - gamma * dth2
        ) / den
        return np.array([dth1, dth2, ddth1, ddth2])

    rng_local = np.random.default_rng(seed)
    ic_amp = 0.1

    var_rels    = []
    energy_vals = []
    n_steps     = int(T_end / dt)
    n_trans     = int(T_trans / dt)

    for _ in range(n_ic):
        y = rng_local.uniform(np.array([-ic_amp, -ic_amp, 0.0, 0.0]),
                               np.array([ic_amp,  ic_amp,  0.0, 0.0]))
        th1_ss_list  = []
        th2_ss_list  = []
        dth1_ss_list = []
        dth2_ss_list = []
        try:
            for step in range(n_steps):
                k1 = pend_ode(y)
                k2 = pend_ode(y + 0.5 * dt * k1)
                k3 = pend_ode(y + 0.5 * dt * k2)
                k4 = pend_ode(y + dt * k3)
                y  = y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
                if step >= n_trans:
                    th1_ss_list.append(y[0])
                    th2_ss_list.append(y[1])
                    dth1_ss_list.append(y[2])
                    dth2_ss_list.append(y[3])
        except Exception:
            continue

        if len(th1_ss_list) < 10:
            continue
        th1_ss  = np.array(th1_ss_list)
        th2_ss  = np.array(th2_ss_list)
        dth1_ss = np.array(dth1_ss_list)
        dth2_ss = np.array(dth2_ss_list)
        var_rels.append(float(np.var(th1_ss - th2_ss)))
        energy_vals.append(float(np.mean(0.5 * (dth1_ss**2 + dth2_ss**2))))

    if not var_rels:
        return {"status": "error", "note": "All IC runs failed", "gamma": gamma, "kappa": kappa}

    var_rel   = float(np.mean(var_rels))
    energy_ss = float(np.mean(energy_vals))

    regime_label, regime_id = ("coupling_dominated", 0) if var_rel > 0.05 else ("dissipation_dominated", 1)

    return {
        "status":        "ok",
        "gamma":         gamma,
        "kappa":         kappa,
        "var_rel":       round(var_rel, 6),
        "energy_ss":     round(energy_ss, 6),
        "regime_label":  regime_label,
        "regime_id":     regime_id,
        "n_ic_used":     len(var_rels),
    }


def run_sir_growing(params: dict, sweep_point: dict, rng: np.random.Generator) -> dict:
    """
    ODE-based SIR epidemic model with growing population N(t) = N0*exp(rho*t).
    BC class: Dissipation (population dilution acts as S4 contraction on infected fraction).

    Equations (absolute counts):
        dS/dt = rho*N - beta*S*I/N    (births replenish susceptibles)
        dI/dt = beta*S*I/N - gamma_r*I
        dR/dt = gamma_r*I
        N(t) = S + I + R grows as N0*exp(rho*t)

    Primary observable: g_max_percapita = max_t [(dI/dt) / N(t)]
                      = max_t [i(t) * (beta*s(t) - gamma_r)]
    Secondary (diagnostic): I_peak_frac = max_t [I(t)/N(t)]
    Secondary (DEV-02 fibre-resolved companion): g_ratio = g(t@s=0.5) / g(t@s=0.9)
                      per-capita velocity at a late vs early state landmark; non-collapsing
                      readout across the order axis (population grows, so t-order = <=-order).

    NOTE (camouflage, corrected 2026-06-02 — see transfer_test_dissipation_growth/
    protocol_deviation_log.md DEV-01): g(t) reduces exactly to a function of the closed
    fraction system (s,i): g = i*(beta*s - gamma_r). It carries NO absolute-count signal.
    Camouflage (absorption of rho into an effective gamma_r) is avoided not by "absolute
    counts" but by the rho*(1-s) replenishment term in ds/dt, which makes rho enter the
    closed (s,i) system in two places. g_max is still a scalar collapse; g_ratio is the
    fibre-resolved companion that can detect a break g_max would miss.

    Analytical threshold: rho* = beta*s0 - gamma_r
    """
    rho     = float(sweep_point.get("rho", 0.0))
    beta    = float(params.get("beta", 0.3))
    gamma_r = float(params.get("gamma_r", 0.1))
    N0      = float(params.get("N0", 10000.0))
    I0      = float(params.get("I0", 100.0))
    S0_abs  = float(params.get("S0", N0 - I0))
    T       = float(params.get("T", 300.0))
    dt      = float(params.get("dt", 0.1))

    rng_local = np.random.default_rng(int(sweep_point.get("seed", 42)))

    # IC perturbation range
    ic_range_I = params.get("ic_range_I", [I0 * 0.5, I0 * 1.5])
    n_runs = int(params.get("n_ic", 10))

    g_max_list       = []
    I_peak_frac_list = []
    g_ratio_list     = []

    for _ in range(n_runs):
        I0_run = float(rng_local.uniform(ic_range_I[0], ic_range_I[1]))
        S0_run = N0 - I0_run
        R0_run = 0.0

        # RK4 integration
        y = np.array([S0_run, I0_run, R0_run])
        n_steps = int(T / dt)
        g_max_run    = -np.inf
        I_peak_frac_run = I0_run / N0
        # DEV-02 landmarks: g at first crossing of s=0.9 (early) and s=0.5 (late)
        g_early = None
        g_late  = None

        try:
            for _ in range(n_steps):
                S, I, R = y
                N = S + I + R
                if N <= 0:
                    break
                s = S / N
                i = I / N

                def f(yv):
                    Sv, Iv, Rv = yv
                    Nv = Sv + Iv + Rv
                    if Nv <= 0:
                        return np.zeros(3)
                    return np.array([
                        rho * Nv - beta * Sv * Iv / Nv,
                        beta * Sv * Iv / Nv - gamma_r * Iv,
                        gamma_r * Iv,
                    ])

                k1 = f(y)
                k2 = f(y + 0.5 * dt * k1)
                k3 = f(y + 0.5 * dt * k2)
                k4 = f(y + dt * k3)
                y = y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
                y = np.maximum(y, 0.0)  # numerical safety

                S, I, R = y
                N = S + I + R
                if N <= 0:
                    break

                # Compute g(t) = (dI/dt) / N  =  i * (beta*s - gamma_r)
                s_cur = S / N
                i_cur = I / N
                g_cur = i_cur * (beta * s_cur - gamma_r)

                if g_cur > g_max_run:
                    g_max_run = g_cur
                if i_cur > I_peak_frac_run:
                    I_peak_frac_run = i_cur

                # DEV-02 fibre landmarks (s decreases during an epidemic)
                if g_early is None and s_cur <= 0.9:
                    g_early = g_cur
                if g_late is None and s_cur <= 0.5:
                    g_late = g_cur

        except Exception:
            continue

        if np.isfinite(g_max_run):
            g_max_list.append(g_max_run)
            I_peak_frac_list.append(I_peak_frac_run)
            # g_ratio = late/early per-capita velocity; 0 if late landmark never reached
            if g_early is not None and g_early > 1e-12 and g_late is not None:
                g_ratio_list.append(g_late / g_early)
            else:
                g_ratio_list.append(0.0)

    if not g_max_list:
        return {"status": "error", "note": "All IC runs failed", "rho": rho}

    rho_star = beta * (S0_abs / N0) - gamma_r
    regime_label = "epidemic_sustained" if rho < rho_star else "epidemic_suppressed"
    regime_id    = 0 if rho < rho_star else 1

    return {
        "status":              "ok",
        "rho":                 rho,
        "g_max_percapita":     round(float(np.mean(g_max_list)), 8),
        "I_peak_frac":         round(float(np.mean(I_peak_frac_list)), 6),
        "g_ratio":             round(float(np.mean(g_ratio_list)), 6),
        "rho_star_analytical": round(rho_star, 6),
        "regime_label":        regime_label,
        "regime_id":           regime_id,
        "n_ic_used":           len(g_max_list),
    }


KERNEL_MAP = {
    "kuramoto":        run_kuramoto,
    "pendulum":        run_pendulum,
    "pendulum_gamma":  run_pendulum_gamma,
    "double_pendulum": run_double_pendulum,
    "consensus":       run_consensus,
    "meanfield":       run_meanfield,
    "labyrinth":       run_labyrinth,
    "sir_epidemic":    run_sir_epidemic,
    "sir_growing":     run_sir_growing,
}


# ── Sweep runner ─────────────────────────────────────────────────────────────
# Restored 2026-06-02: sweep.py had lost its __main__ runner, so sweeps could not
# be (re)generated. Output format mirrors a working case
# (cases/CASE-20260315-0007/results/raw/sweep_results.json) exactly:
#   top dict {case_id, system, created_at, n_points, elapsed_s, sweep_design_note, results}
#   each result = kernel output + "_sweep_index" + "_sweep_point" (param + _bc_id + _bc_class)

def _primary_component(manifest: dict) -> dict:
    comps = manifest.get("bc_components", [])
    for c in comps:
        if c.get("primary"):
            return c
    return comps[0] if comps else {}


def _build_sweep_points(component: dict) -> list:
    """Build sweep points from a primary bc_component's perturbation_program.

    Supports explicit `values: [...]` (all current cases) and, as a fallback,
    `range: [min, max]` + `n_points`.
    """
    bc_id    = component.get("id", "bc_01")
    bc_class = component.get("class", "")
    pp = component.get("perturbation_program", {})
    sweeps = pp.get("sweeps", [])
    if not sweeps:
        raise ValueError("No perturbation_program.sweeps in primary bc_component")
    sweep = sweeps[0]
    param = sweep.get("param") or component.get("sweep_param")
    if "values" in sweep and sweep["values"]:
        values = list(sweep["values"])
    elif "range" in sweep:
        lo, hi = sweep["range"]
        n = int(sweep.get("n_points", 26))
        values = list(np.linspace(lo, hi, n))
    else:
        raise ValueError("sweep entry has neither 'values' nor 'range'")
    return [{param: float(v), "_bc_id": bc_id, "_bc_class": bc_class} for v in values]


def run_sweep(case_dir: Path, out_subdir: str = "results/raw", seed: int = 42) -> Path:
    manifest_path = case_dir / "BCManifest.yaml"
    if not manifest_path.exists():
        print(f"ERROR: BCManifest.yaml not found at {manifest_path}")
        sys.exit(1)
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))

    system = manifest.get("system")
    if system not in KERNEL_MAP:
        print(f"ERROR: system '{system}' not in KERNEL_MAP {list(KERNEL_MAP)}")
        sys.exit(1)
    kernel = KERNEL_MAP[system]

    component    = _primary_component(manifest)
    fixed_params = dict(component.get("fixed_params", {}))
    sweep_points = _build_sweep_points(component)

    rng = np.random.default_rng(seed)
    t0 = time.time()
    results = []
    for idx, sp in enumerate(sweep_points):
        r = kernel(fixed_params, sp, rng)
        r["_sweep_index"] = idx
        r["_sweep_point"] = sp
        results.append(r)
    elapsed = round(time.time() - t0, 3)

    out_dict = {
        "case_id":           manifest.get("case_id", case_dir.name),
        "system":            system,
        "created_at":        date.today().isoformat(),
        "n_points":          len(results),
        "elapsed_s":         elapsed,
        "sweep_design_note": f"{component.get('sweep_param', '')}-sweep via "
                             f"perturbation_program ({len(results)} points)",
        "results":           results,
    }
    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "sweep_results.json"
    out_path.write_text(json.dumps(out_dict, indent=2), encoding="utf-8")

    n_ok = sum(1 for r in results if r.get("status") == "ok")
    print(f"  sweep: {system} | {len(results)} points ({n_ok} ok) | {elapsed}s")
    print(f"  -> {out_path}")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Run a BC parameter sweep for a case.")
    ap.add_argument("--case", required=True, help="Path to case directory (contains BCManifest.yaml)")
    ap.add_argument("--out", default="results/raw", help="Output subdir under the case (default results/raw)")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    case_dir = Path(args.case)
    if not case_dir.is_absolute():
        case_dir = (Path.cwd() / case_dir)
    run_sweep(case_dir, args.out, args.seed)


if __name__ == "__main__":
    main()
