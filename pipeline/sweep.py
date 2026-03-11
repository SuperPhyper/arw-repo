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
    """Stub — multi-link pendulum. Implement with scipy.integrate.solve_ivp."""
    return {"status": "stub", "sweep_point": sweep_point,
            "note": "Implement pendulum ODE in pipeline/kernels/pendulum.py"}


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
