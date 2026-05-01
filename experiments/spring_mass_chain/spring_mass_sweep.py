"""
spring_mass_sweep.py
====================
ARW Multi-Scale Observable Case — Vertical Spring-Mass Chain
ScopeSpec v3 implementation.

System:
    N masses connected vertically by springs, hanging from a pivot.
    Pivot undergoes periodic vertical forcing: z_pivot(t) = A * sin(Omega * t)
    All motion is 1D (vertical only).

Observables (three levels):
    pi_micro  : mean spring-extension variance   (relative, internal)
    pi_meso   : center-of-mass variance          (absolute, collective)
    pi_macro  : end-mass variance                (absolute, terminal)

Sweep:
    Active BC domain: (A, Omega/omega_1) — 2D grid
    Conditioned:      N, gamma, m, k, l0

Usage:
    python spring_mass_sweep.py --N 3 --n_A 20 --n_Omega 20 --pilot
    python spring_mass_sweep.py --N 3 --n_A 40 --n_Omega 40
    python spring_mass_sweep.py --N 1 --n_A 30 --n_Omega 30   # baseline P6

Outputs (written to ./results/N{N}/):
    sweep_raw.npz       : full observable arrays over (A, Omega) grid
    sigma_delta.npz     : perturbation spread sigma_Delta per observable
    bcmanifest.json     : all conditioned parameter values
    invariants.json     : placeholder (filled by partition step)
"""

import argparse
import json
import os
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh


# ---------------------------------------------------------------------------
# 1.  PHYSICS
# ---------------------------------------------------------------------------

def equilibrium_positions(N, m, k, g, l0):
    """
    Compute equilibrium positions z_i,eq (downward positive, from pivot).
    Each mass is pulled down by its own weight plus all masses below it.
    z_i,eq = sum_{j=1}^{i} (l0 + m*g*(N-j+1)/k)
    """
    z_eq = np.zeros(N)
    for i in range(N):
        # Extension of spring i+1 at equilibrium:
        # carries weight of masses i+1 .. N
        spring_ext = m * g * (N - i) / k
        if i == 0:
            z_eq[i] = l0 + spring_ext
        else:
            z_eq[i] = z_eq[i-1] + l0 + spring_ext
    return z_eq


def stiffness_matrix(N, k):
    """Tridiagonal stiffness matrix K (N x N)."""
    K = np.zeros((N, N))
    for i in range(N):
        K[i, i] = 2 * k if i < N - 1 else k   # last mass: only spring above
        if i < N - 1:
            K[i, i+1] = -k
            K[i+1, i] = -k
    return K


def normal_modes(N, m, k):
    """
    Compute eigenfrequencies and eigenvectors for uniform chain.
    Returns:
        omega_j : array (N,) — eigenfrequencies in ascending order
        V       : array (N,N) — columns are eigenvectors (mass-normalised)
    """
    M = m * np.eye(N)
    K = stiffness_matrix(N, k)
    # Solve generalised eigenvalue problem K v = omega^2 M v
    omega2, V = eigh(K, M)
    omega2 = np.maximum(omega2, 0.0)   # numerical safety
    return np.sqrt(omega2), V


def equations_of_motion(t, state, N, m, k, gamma, g, l0, A, Omega):
    """
    ODE right-hand side in absolute lab-frame coordinates.

    state = [z_1, ..., z_N, zdot_1, ..., zdot_N]

    Pivot position: z_0(t) = A * sin(Omega * t)
    """
    z    = state[:N]
    zdot = state[N:]
    zddot = np.zeros(N)

    z0 = A * np.sin(Omega * t)   # pivot position

    for i in range(N):
        z_above = z0 if i == 0 else z[i-1]
        z_below = z[i+1] if i < N-1 else None

        # Spring above (connects z_above to z[i])
        ext_above = z[i] - z_above - l0
        F_above   = -k * ext_above          # pulls mass upward

        # Spring below (connects z[i] to z_below)
        F_below = 0.0
        if z_below is not None:
            ext_below = z_below - z[i] - l0
            F_below   = k * ext_below       # pulls mass downward

        zddot[i] = (m * g + F_above + F_below - gamma * zdot[i]) / m

    return np.concatenate([zdot, zddot])


# ---------------------------------------------------------------------------
# 2.  OBSERVABLE COMPUTATION
# ---------------------------------------------------------------------------

def compute_observables(t_obs, z_traj, N, m, l0, z0_traj):
    """
    Compute all three observables from a stationary trajectory window.

    Parameters
    ----------
    t_obs   : 1D array — time points in the observation window
    z_traj  : (N, len(t_obs)) — absolute positions of masses
    N       : int
    m       : float — mass (equal for all)
    l0      : float — rest length
    z0_traj : 1D array — pivot position z_0(t) over observation window

    Returns
    -------
    pi_micro : float — mean spring-extension variance
    pi_meso  : float — COM variance
    pi_macro : float — end-mass variance
    """
    # Spring extensions d_i(t) = z_i - z_{i-1} - l0
    # z_{i-1} for i=1 is the pivot z0
    d = np.zeros_like(z_traj)
    d[0] = z_traj[0] - z0_traj - l0
    for i in range(1, N):
        d[i] = z_traj[i] - z_traj[i-1] - l0

    pi_micro = float(np.mean(np.var(d, axis=1)))   # mean over springs

    z_COM = np.mean(z_traj, axis=0)                # equal masses
    pi_meso = float(np.var(z_COM))

    pi_macro = float(np.var(z_traj[-1]))           # end mass

    return pi_micro, pi_meso, pi_macro


# ---------------------------------------------------------------------------
# 3.  SINGLE SIMULATION
# ---------------------------------------------------------------------------

def run_single(N, m, k, gamma, g, l0, A, Omega,
               T_transient, T_obs, n_obs_points,
               delta_z=0.0, delta_zdot=0.0, seed=0):
    """
    Simulate the chain and return observable values.

    delta_z, delta_zdot : uniform perturbation amplitude for Δ-sampling.
    seed                : random seed for perturbation direction.
    """
    z_eq = equilibrium_positions(N, m, k, g, l0)

    rng = np.random.default_rng(seed)
    dz    = rng.uniform(-delta_z,    delta_z,    N) if delta_z    > 0 else np.zeros(N)
    dzdot = rng.uniform(-delta_zdot, delta_zdot, N) if delta_zdot > 0 else np.zeros(N)

    x0 = np.concatenate([z_eq + dz, dzdot])

    T_total = T_transient + T_obs
    t_span  = (0.0, T_total)

    # Dense output only in observation window
    t_eval_obs = np.linspace(T_transient, T_total, n_obs_points)

    sol = solve_ivp(
        equations_of_motion,
        t_span,
        x0,
        method='RK45',
        t_eval=t_eval_obs,
        args=(N, m, k, gamma, g, l0, A, Omega),
        rtol=1e-8, atol=1e-10,
        dense_output=False,
    )

    if not sol.success:
        return None, None, None

    z_traj  = sol.y[:N]                                    # (N, n_obs_points)
    z0_traj = A * np.sin(Omega * sol.t)                    # pivot

    pi_micro, pi_meso, pi_macro = compute_observables(
        sol.t, z_traj, N, m, l0, z0_traj
    )
    return pi_micro, pi_meso, pi_macro


# ---------------------------------------------------------------------------
# 4.  PERTURBATION SPREAD  sigma_Delta
# ---------------------------------------------------------------------------

def compute_sigma_delta(N, m, k, gamma, g, l0, A, Omega,
                        T_transient, T_obs, n_obs_points,
                        delta_r, n_delta_samples):
    """
    Empirically estimate sigma_Delta for all three observables at (A, Omega).

    sigma_Delta(pi, b) = max_{delta in Delta} |pi(b, delta) - pi(b, 0)|
    """
    pi0 = run_single(N, m, k, gamma, g, l0, A, Omega,
                     T_transient, T_obs, n_obs_points,
                     delta_z=0.0, delta_zdot=0.0, seed=0)

    if pi0[0] is None:
        return np.nan, np.nan, np.nan

    spreads = np.zeros((n_delta_samples, 3))
    for s in range(n_delta_samples):
        pi_s = run_single(N, m, k, gamma, g, l0, A, Omega,
                          T_transient, T_obs, n_obs_points,
                          delta_z=delta_r, delta_zdot=delta_r, seed=s+1)
        if pi_s[0] is None:
            spreads[s] = np.nan
        else:
            spreads[s] = [abs(pi_s[j] - pi0[j]) for j in range(3)]

    sigma = np.nanmax(spreads, axis=0)
    return float(sigma[0]), float(sigma[1]), float(sigma[2])


# ---------------------------------------------------------------------------
# 5.  PILOT SWEEP  (gradient estimation)
# ---------------------------------------------------------------------------

def pilot_sweep(N, m, k, gamma, g, l0,
                A_fixed, Omega_ratio_grid,
                T_transient, T_obs, n_obs_points, omega_1):
    """
    Run a sparse 1D sweep over Omega/omega_1 at fixed A.
    Returns gradient estimate G_micro_max for grid density calculation.
    """
    print(f"  Pilot sweep: {len(Omega_ratio_grid)} points along Omega/omega_1 axis")
    pi_micro_vals = []
    for r in Omega_ratio_grid:
        Omega = r * omega_1
        pm, _, _ = run_single(N, m, k, gamma, g, l0, A_fixed, Omega,
                               T_transient, T_obs, n_obs_points)
        pi_micro_vals.append(pm if pm is not None else np.nan)

    pi_micro_vals = np.array(pi_micro_vals)
    dpi = np.abs(np.diff(pi_micro_vals))
    dr  = np.diff(Omega_ratio_grid)
    G   = dpi / dr
    G_max = float(np.nanmax(G))
    print(f"  G_micro_max = {G_max:.4f}  (pi_micro / (Omega/omega_1))")
    return G_max, pi_micro_vals


# ---------------------------------------------------------------------------
# 6.  MAIN SWEEP
# ---------------------------------------------------------------------------

def run_sweep(N, m, k, gamma, g, l0,
              A_grid, Omega_ratio_grid, omega_1,
              T_transient, T_obs, n_obs_points,
              delta_r, n_delta_samples,
              output_dir):

    nA = len(A_grid)
    nO = len(Omega_ratio_grid)

    pi_micro  = np.full((nA, nO), np.nan)
    pi_meso   = np.full((nA, nO), np.nan)
    pi_macro  = np.full((nA, nO), np.nan)
    sig_micro = np.full((nA, nO), np.nan)
    sig_meso  = np.full((nA, nO), np.nan)
    sig_macro = np.full((nA, nO), np.nan)

    total = nA * nO
    done  = 0
    t0    = time.time()

    print(f"\n  Main sweep: {nA} x {nO} = {total} grid points")
    print(f"  sigma_Delta: {n_delta_samples} samples per point, delta_r={delta_r}")

    for i, A in enumerate(A_grid):
        for j, r in enumerate(Omega_ratio_grid):
            Omega = r * omega_1

            # Nominal observables
            pm, ps, pk = run_single(
                N, m, k, gamma, g, l0, A, Omega,
                T_transient, T_obs, n_obs_points
            )

            if pm is not None:
                pi_micro[i, j] = pm
                pi_meso[i, j]  = ps
                pi_macro[i, j] = pk

            # Perturbation spread
            sm, ss, sk = compute_sigma_delta(
                N, m, k, gamma, g, l0, A, Omega,
                T_transient, T_obs, n_obs_points,
                delta_r, n_delta_samples
            )
            sig_micro[i, j] = sm
            sig_meso[i, j]  = ss
            sig_macro[i, j] = sk

            done += 1
            if done % max(1, total // 20) == 0:
                elapsed = time.time() - t0
                eta = elapsed / done * (total - done)
                print(f"  {done}/{total}  elapsed={elapsed:.0f}s  ETA={eta:.0f}s")

    # Save
    os.makedirs(output_dir, exist_ok=True)
    np.savez(
        os.path.join(output_dir, "sweep_raw.npz"),
        A_grid=A_grid,
        Omega_ratio_grid=Omega_ratio_grid,
        omega_1=omega_1,
        pi_micro=pi_micro,
        pi_meso=pi_meso,
        pi_macro=pi_macro,
    )
    np.savez(
        os.path.join(output_dir, "sigma_delta.npz"),
        A_grid=A_grid,
        Omega_ratio_grid=Omega_ratio_grid,
        sig_micro=sig_micro,
        sig_meso=sig_meso,
        sig_macro=sig_macro,
        delta_r=delta_r,
        n_delta_samples=n_delta_samples,
    )
    print(f"\n  Saved: {output_dir}/sweep_raw.npz")
    print(f"  Saved: {output_dir}/sigma_delta.npz")

    return pi_micro, pi_meso, pi_macro, sig_micro, sig_meso, sig_macro


# ---------------------------------------------------------------------------
# 7.  BCMANIFEST
# ---------------------------------------------------------------------------

def write_bcmanifest(output_dir, N, m, k, gamma, g, l0,
                     A_grid, Omega_ratio_grid, omega_1,
                     T_transient, T_obs, n_obs_points,
                     delta_r, n_delta_samples):
    manifest = {
        "case_id": f"CASE-20260430-XXXX",
        "system": "vertical_spring_mass_chain",
        "conditioned_parameters": {
            "N": N,
            "m": m,
            "k": k,
            "gamma": gamma,
            "g": g,
            "l0": l0,
        },
        "sweep_parameters": {
            "A": {
                "min": float(A_grid[0]),
                "max": float(A_grid[-1]),
                "n_points": len(A_grid),
                "unit": "m"
            },
            "Omega_ratio": {
                "description": "Omega / omega_1",
                "min": float(Omega_ratio_grid[0]),
                "max": float(Omega_ratio_grid[-1]),
                "n_points": len(Omega_ratio_grid),
            }
        },
        "omega_1": float(omega_1),
        "simulation": {
            "T_transient": T_transient,
            "T_obs": T_obs,
            "n_obs_points": n_obs_points,
            "integrator": "RK45",
            "rtol": 1e-8,
            "atol": 1e-10,
        },
        "delta_class": {
            "delta_r": delta_r,
            "n_delta_samples": n_delta_samples,
            "type": "uniform_all_masses",
        },
        "observables": {
            "pi_micro": "mean spring-extension variance  (1/N) * sum_i Var_t[d_i(t)]",
            "pi_meso":  "COM variance                    Var_t[mean_i z_i(t)]",
            "pi_macro": "end-mass variance               Var_t[z_N(t)]",
        }
    }
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "bcmanifest.json")
    with open(path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"  Saved: {path}")


# ---------------------------------------------------------------------------
# 8.  SIMPLE SUMMARY STATS
# ---------------------------------------------------------------------------

def print_summary(pi_micro, pi_meso, pi_macro):
    for name, arr in [("pi_micro", pi_micro),
                      ("pi_meso",  pi_meso),
                      ("pi_macro", pi_macro)]:
        valid = arr[~np.isnan(arr)]
        if len(valid) == 0:
            print(f"  {name}: all NaN")
        else:
            print(f"  {name}:  min={valid.min():.4e}  "
                  f"max={valid.max():.4e}  "
                  f"span={valid.max()-valid.min():.4e}")


# ---------------------------------------------------------------------------
# 9.  CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="ARW spring-mass chain sweep")
    p.add_argument("--N",          type=int,   default=3,    help="Number of masses (1-5)")
    p.add_argument("--m",          type=float, default=1.0,  help="Mass of each link [kg]")
    p.add_argument("--k",          type=float, default=1.0,  help="Spring constant [N/m]")
    p.add_argument("--gamma",      type=float, default=0.05, help="Damping coefficient")
    p.add_argument("--g",          type=float, default=9.81, help="Gravitational acceleration")
    p.add_argument("--l0",         type=float, default=1.0,  help="Spring rest length [m]")
    p.add_argument("--A_min",      type=float, default=0.01, help="Min forcing amplitude [m]")
    p.add_argument("--A_max",      type=float, default=0.5,  help="Max forcing amplitude [m]")
    p.add_argument("--n_A",        type=int,   default=20,   help="Grid points along A axis")
    p.add_argument("--Or_min",     type=float, default=0.2,  help="Min Omega/omega_1")
    p.add_argument("--Or_max",     type=float, default=3.0,  help="Max Omega/omega_1")
    p.add_argument("--n_Omega",    type=int,   default=20,   help="Grid points along Omega axis")
    p.add_argument("--T_trans",    type=float, default=100.0,help="Transient time [s]")
    p.add_argument("--T_obs",      type=float, default=100.0,help="Observation window [s]")
    p.add_argument("--n_obs",      type=int,   default=2000, help="Time points in obs window")
    p.add_argument("--delta_r",    type=float, default=0.01, help="Perturbation radius for sigma_Delta")
    p.add_argument("--n_delta",    type=int,   default=8,    help="Number of Delta samples per point")
    p.add_argument("--pilot",      action="store_true",      help="Run pilot sweep only (grid density estimation)")
    p.add_argument("--outdir",     type=str,   default="results", help="Output directory base")
    return p.parse_args()


def main():
    args = parse_args()
    N = args.N

    print(f"\n=== ARW Spring-Mass Chain Sweep ===")
    print(f"  N={N}  m={args.m}  k={args.k}  gamma={args.gamma}  g={args.g}  l0={args.l0}")

    # Normal modes
    omega_j, V = normal_modes(N, args.m, args.k)
    omega_1    = omega_j[0]
    print(f"\n  Eigenfrequencies omega_j (N={N}): {np.round(omega_j, 4)}")
    print(f"  omega_1 = {omega_1:.4f}")
    print(f"  Resonance bands Omega/omega_1 = {np.round(omega_j / omega_1, 3)}")

    output_dir = os.path.join(args.outdir, f"N{N}")

    # ---- PILOT ----
    if args.pilot:
        print("\n--- Pilot sweep (gradient estimation) ---")
        Or_pilot = np.linspace(args.Or_min, args.Or_max, 20)
        A_pilot  = (args.A_min + args.A_max) / 2.0
        G_max, _ = pilot_sweep(
            N, args.m, args.k, args.gamma, args.g, args.l0,
            A_pilot, Or_pilot,
            args.T_trans, args.T_obs, args.n_obs, omega_1
        )
        # Recommended grid density
        epsilon_micro_estimate = 0.005  # rough estimate; refine after pilot
        delta_b_min = epsilon_micro_estimate / G_max if G_max > 0 else 0.1
        print(f"\n  Recommended Omega/omega_1 grid spacing <= {delta_b_min:.4f}")
        print(f"  At current n_Omega={args.n_Omega}: "
              f"spacing = {(args.Or_max - args.Or_min) / args.n_Omega:.4f}")
        print("  Adjust --n_Omega accordingly before main sweep.")
        return

    # ---- MAIN SWEEP ----
    A_grid     = np.linspace(args.A_min, args.A_max, args.n_A)
    Or_grid    = np.linspace(args.Or_min, args.Or_max, args.n_Omega)

    write_bcmanifest(
        output_dir, N, args.m, args.k, args.gamma, args.g, args.l0,
        A_grid, Or_grid, omega_1,
        args.T_trans, args.T_obs, args.n_obs,
        args.delta_r, args.n_delta
    )

    pi_micro, pi_meso, pi_macro, \
    sig_micro, sig_meso, sig_macro = run_sweep(
        N, args.m, args.k, args.gamma, args.g, args.l0,
        A_grid, Or_grid, omega_1,
        args.T_trans, args.T_obs, args.n_obs,
        args.delta_r, args.n_delta,
        output_dir
    )

    print("\n--- Observable summary ---")
    print_summary(pi_micro, pi_meso, pi_macro)

    print("\n--- sigma_Delta summary ---")
    print_summary(sig_micro, sig_meso, sig_macro)

    print(f"\nDone. Results in: {output_dir}/")
    print("Next step: run epsilon_sweep.py on sweep_raw.npz to find N* per observable.")


if __name__ == "__main__":
    main()
