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
    """Stub — context-navigation agent."""
    return {"status": "stub", "sweep_point": sweep_point,
            "note": "Implement labyrinth environment in pipeline/kernels/labyrinth.py"}


KERNEL_MAP = {
    "kuramoto":  run_kuramoto,
    "pendulum":  run_pendulum,
    "consensus": run_consensus,
    "meanfield": run_meanfield,
    "labyrinth": run_labyrinth,
}


# ── Sweep Executor ───────────────────────────────────────────────────────────

def build_sweep_points(bc_components: list) -> list:
    """
    Expand BCManifest sweep specs into a flat list of sweep points.
    Each point is a dict of {param_name: value, ...}.
    Currently handles single-param sweeps; extend for multi-param grids.
    """
    points = []
    for bc in bc_components:
        sweeps = bc.get("perturbation_program", {}).get("sweeps", [])
        for sweep in sweeps:
            param  = sweep.get("param", "")
            values = sweep.get("values", [])
            for v in values:
                points.append({param: v, "_bc_id": bc.get("id", ""), "_bc_class": bc.get("class", "")})
    return points


def run_sweep(case_dir: Path, out_subdir: str, dry_run: bool = False):
    bcm_path    = case_dir / "BCManifest.yaml"
    scope_path  = case_dir / "ScopeSpec.yaml"
    record_path = case_dir / "CaseRecord.yaml"

    for p in [bcm_path, scope_path]:
        if not p.exists():
            print(f"ERROR: {p.name} not found in {case_dir}")
            sys.exit(1)

    bcm    = yaml.safe_load(bcm_path.read_text())
    scope  = yaml.safe_load(scope_path.read_text())
    record = yaml.safe_load(record_path.read_text()) if record_path.exists() else {}

    system = record.get("system", "custom")
    kernel = KERNEL_MAP.get(system)
    if kernel is None:
        print(f"ERROR: No kernel for system '{system}'. Available: {list(KERNEL_MAP.keys())}")
        sys.exit(1)

    sweep_points = build_sweep_points(bcm.get("bc_components", []))
    if not sweep_points:
        print("ERROR: No sweep points found in BCManifest. Check bc_components[*].perturbation_program.sweeps")
        sys.exit(1)

    print(f"\nSweep: {case_dir.name}  |  system={system}  |  {len(sweep_points)} points")
    print("─" * 50)

    if dry_run:
        print("DRY RUN — sweep points:")
        for i, pt in enumerate(sweep_points):
            print(f"  [{i:03d}] {pt}")
        return

    # Simulation parameters from ScopeSpec (use sensible defaults)
    sim_params = scope.get("simulation_parameters", {})

    out_dir = case_dir / out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    rng = np.random.default_rng(0)

    t0 = time.time()
    for i, pt in enumerate(sweep_points):
        print(f"  [{i+1:03d}/{len(sweep_points)}] {pt} ... ", end="", flush=True)
        t_pt = time.time()
        try:
            result = kernel(sim_params, pt, rng)
            result["_sweep_index"] = i
            result["_sweep_point"] = pt
            results.append(result)
            print(f"done ({time.time()-t_pt:.2f}s)")
        except Exception as e:
            print(f"FAILED: {e}")
            results.append({"_sweep_index": i, "_sweep_point": pt, "status": "failed", "error": str(e)})

    elapsed = time.time() - t0
    print(f"\n  Completed {len(sweep_points)} points in {elapsed:.1f}s")

    # Write output
    out_path = out_dir / "sweep_results.json"
    out_meta = {
        "case_id":     record.get("id", case_dir.name),
        "system":      system,
        "created_at":  time.strftime("%Y-%m-%dT%H:%M:%S"),
        "n_points":    len(sweep_points),
        "elapsed_s":   round(elapsed, 2),
        "results":     results,
    }
    out_path.write_text(json.dumps(out_meta, indent=2))
    print(f"  Output: {out_path}")
    print(f"\nNext step: python -m pipeline.extract_partition --case {case_dir} --in {out_subdir}")


def main():
    parser = argparse.ArgumentParser(description="Run BC parameter sweep.")
    parser.add_argument("--case",    required=True)
    parser.add_argument("--out",     default="results/raw")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    case_dir = REPO_ROOT / args.case if not Path(args.case).is_absolute() else Path(args.case)
    if not case_dir.exists():
        print(f"ERROR: Case not found: {case_dir}")
        sys.exit(1)

    run_sweep(case_dir, args.out, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
