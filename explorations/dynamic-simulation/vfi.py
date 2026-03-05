"""
Value function iteration solver for the dynamic intrahousehold model.

Bellman equation:
    V_i(w_i, w_j) = max_{s_i, q_i} { v_i(w_i - s_i - p*q_i, w_j)
                                       + beta * E[V_i(w_i', w_j')] }
    subject to: s_i >= 0, q_i >= 0, s_i + p*q_i <= w_i
    transition: w_i' = R * s_i + q_i * psi(R)

We fix w_j and solve a 1D problem over w_i.

Strategy: fine grid search for VFI convergence, then a single refinement
pass with Nelder-Mead multi-start to smooth the policy functions.
Supports multiprocessing for both within-iteration and across-run parallelism.
"""

import numpy as np
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from scipy.interpolate import interp1d
from scipy.optimize import minimize

from model import indirect_utility


def gauss_hermite_lognormal(mu, sigma, n_points):
    """Quadrature nodes and weights for lognormal(mu, sigma)."""
    x, w = np.polynomial.hermite.hermgauss(n_points)
    R_nodes = np.exp(mu + np.sqrt(2) * sigma * x)
    weights = w / np.sqrt(np.pi)
    return R_nodes, weights


def make_action_grid(n_actions):
    """Create a grid of (s_frac, q_frac) pairs in [0,1]^2 summing to <= 1."""
    fracs = np.linspace(0, 1, n_actions)
    s_fracs, q_fracs = np.meshgrid(fracs, fracs)
    s_fracs = s_fracs.ravel()
    q_fracs = q_fracs.ravel()
    feasible = s_fracs + q_fracs <= 1.0 + 1e-10
    return s_fracs[feasible], q_fracs[feasible]


def _bellman_rhs_vectorized(w_grid, s_fracs, q_fracs, p, w_j, alpha, beta,
                            R_nodes, R_bar, R_weights, V_interp, w_min, w_max):
    """Evaluate Bellman RHS for all grid points and actions simultaneously.

    Returns (V_new, s_policy, q_policy) arrays of length n_w.
    Fully vectorized: no Python loop over grid points.
    """
    n_w = len(w_grid)
    n_a = len(s_fracs)
    n_r = len(R_nodes)

    # Shape: (n_w, n_a)
    s_vals = w_grid[:, None] * s_fracs[None, :]
    q_vals = w_grid[:, None] * q_fracs[None, :] / p if p > 0 else np.zeros((n_w, n_a))

    y_i = np.maximum(w_grid[:, None] - s_vals - p * q_vals, 1e-10)

    # Current-period utility: (n_w, n_a)
    # indirect_utility expects 1D, so flatten and reshape
    u_now = indirect_utility(y_i.ravel(), w_j, alpha).reshape(n_w, n_a)

    # Next-period wealth: (n_w, n_a, n_r)
    psi_R = np.maximum(0.0, R_bar - R_nodes)  # (n_r,)
    w_prime = s_vals[:, :, None] * R_nodes[None, None, :] + q_vals[:, :, None] * psi_R[None, None, :]
    w_prime = np.clip(w_prime, w_min, w_max)

    # Expected continuation: (n_w, n_a)
    EV = np.sum(V_interp(w_prime.reshape(-1)).reshape(n_w, n_a, n_r) * R_weights[None, None, :], axis=2)

    total = u_now + beta * EV  # (n_w, n_a)

    best_idx = np.argmax(total, axis=1)  # (n_w,)
    V_new = total[np.arange(n_w), best_idx]
    s_policy = s_vals[np.arange(n_w), best_idx]
    q_policy = q_vals[np.arange(n_w), best_idx]

    return V_new, s_policy, q_policy


def _objective_neg(x, w, p, w_j, alpha, beta, R_nodes, R_bar, R_weights,
                   V_interp, w_min, w_max):
    """Negative Bellman RHS for minimizer."""
    s_frac, q_frac = x
    if s_frac < 0 or q_frac < 0 or s_frac + q_frac > 1.0 + 1e-10:
        return 1e10
    s = s_frac * w
    q = q_frac * w / p if p > 0 else 0.0
    y_i = w - s - p * q
    if y_i < 1e-10:
        return 1e10
    u_now = indirect_utility(np.array([y_i]), w_j, alpha)[0]
    w_prime = s * R_nodes + q * np.maximum(0.0, R_bar - R_nodes)
    w_prime = np.clip(w_prime, w_min, w_max)
    EV = np.sum(V_interp(w_prime) * R_weights)
    return -(u_now + beta * EV)


def _refine_single_point(args):
    """Refine policy for a single grid point (for multiprocessing)."""
    (i_w, w, s_pol, q_pol, s_prev, q_prev, p, w_j, alpha, beta,
     R_nodes, R_bar, R_weights, w_grid_arr, V_arr, w_min, w_max, n_starts) = args

    V_interp = interp1d(w_grid_arr, V_arr, kind="linear", fill_value="extrapolate")

    if w < 1e-8:
        v = indirect_utility(np.array([w]), w_j, alpha)[0] / (1 - beta)
        return i_w, v, 0.0, 0.0

    s0_frac = s_pol / w if w > 0 else 0.0
    q0_frac = q_pol * p / w if w > 0 and p > 0 else 0.0

    starts = [(s0_frac, q0_frac)]
    # Neighbor policy (already refined)
    if s_prev is not None:
        sf = s_prev / w if w > 0 else 0.0
        qf = q_prev * p / w if w > 0 and p > 0 else 0.0
        starts.append((np.clip(sf, 0, 1), np.clip(qf, 0, max(0, 1 - sf))))
    # Diverse corners
    starts.extend([
        (0.7, 0.0), (0.0, 0.7), (0.4, 0.4),
        (0.9, 0.0), (0.0, 0.9), (0.5, 0.2), (0.2, 0.5),
        (0.6, 0.1), (0.1, 0.6), (0.8, 0.1),
    ])

    best_val = -np.inf
    best_s = s_pol
    best_q = q_pol
    common_args = (w, p, w_j, alpha, beta, R_nodes, R_bar, R_weights,
                   V_interp, w_min, w_max)

    for sf0, qf0 in starts[:n_starts]:
        sf0 = np.clip(sf0, 0.01, 0.98)
        qf0 = np.clip(qf0, 0.0, 0.98 - sf0)
        res = minimize(
            _objective_neg,
            np.array([sf0, qf0]),
            args=common_args,
            method="Nelder-Mead",
            options={"xatol": 1e-8, "fatol": 1e-12, "maxiter": 500, "adaptive": True},
        )
        val = -res.fun
        if val > best_val:
            best_val = val
            sf, qf = res.x
            sf = np.clip(sf, 0, 1)
            qf = np.clip(qf, 0, max(0, 1 - sf))
            best_s = sf * w
            best_q = qf * w / p if p > 0 else 0.0

    return i_w, best_val, best_s, best_q


def _refine_policies(w_grid, V, s_policy, q_policy, p, w_j, alpha, beta,
                     R_nodes, R_bar, R_weights, n_refine_starts, n_workers, verbose):
    """Single-pass policy refinement using Nelder-Mead multi-start.

    Processes grid points sequentially to allow neighbor-seeding,
    but can optionally use multiprocessing for batches.
    """
    n_w = len(w_grid)
    w_min, w_max = w_grid[0], w_grid[-1]

    V_refined = np.empty(n_w)
    s_refined = np.empty(n_w)
    q_refined = np.empty(n_w)

    if n_workers > 1:
        # Parallel refinement (loses sequential neighbor-seeding but much faster)
        args_list = []
        for i_w in range(n_w):
            s_prev = s_policy[i_w - 1] if i_w > 0 else None
            q_prev = q_policy[i_w - 1] if i_w > 0 else None
            args_list.append((
                i_w, w_grid[i_w], s_policy[i_w], q_policy[i_w],
                s_prev, q_prev,
                p, w_j, alpha, beta, R_nodes, R_bar, R_weights,
                w_grid, V, w_min, w_max, n_refine_starts
            ))

        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            results = list(executor.map(_refine_single_point, args_list))

        for i_w, v, s, q in results:
            V_refined[i_w] = v
            s_refined[i_w] = s
            q_refined[i_w] = q
    else:
        # Sequential (allows neighbor-seeding for smoother results)
        V_interp = interp1d(w_grid, V, kind="linear", fill_value="extrapolate")
        for i_w, w in enumerate(w_grid):
            if w < 1e-8:
                V_refined[i_w] = indirect_utility(np.array([w]), w_j, alpha)[0] / (1 - beta)
                s_refined[i_w] = 0.0
                q_refined[i_w] = 0.0
                continue

            s0_frac = s_policy[i_w] / w if w > 0 else 0.0
            q0_frac = q_policy[i_w] * p / w if w > 0 and p > 0 else 0.0

            starts = [(s0_frac, q0_frac)]
            # Neighbors (already refined)
            for di in [-1, -2]:
                ni = i_w + di
                if 0 <= ni < n_w:
                    sf = s_refined[ni] / w if w > 0 else 0.0
                    qf = q_refined[ni] * p / w if w > 0 and p > 0 else 0.0
                    starts.append((np.clip(sf, 0, 1), np.clip(qf, 0, max(0, 1 - sf))))
            # Forward neighbor (grid policy)
            if i_w + 1 < n_w:
                sf = s_policy[i_w + 1] / w if w > 0 else 0.0
                qf = q_policy[i_w + 1] * p / w if w > 0 and p > 0 else 0.0
                starts.append((np.clip(sf, 0, 1), np.clip(qf, 0, max(0, 1 - sf))))
            starts.extend([
                (0.7, 0.0), (0.0, 0.7), (0.4, 0.4),
                (0.9, 0.0), (0.0, 0.9), (0.5, 0.2), (0.2, 0.5),
                (0.6, 0.1), (0.1, 0.6), (0.8, 0.1),
            ])

            best_val = -np.inf
            best_s = s_policy[i_w]
            best_q = q_policy[i_w]
            common_args = (w, p, w_j, alpha, beta, R_nodes, R_bar, R_weights,
                           V_interp, w_grid[0], w_grid[-1])

            for sf0, qf0 in starts[:n_refine_starts]:
                sf0 = np.clip(sf0, 0.01, 0.98)
                qf0 = np.clip(qf0, 0.0, 0.98 - sf0)
                res = minimize(
                    _objective_neg,
                    np.array([sf0, qf0]),
                    args=common_args,
                    method="Nelder-Mead",
                    options={"xatol": 1e-8, "fatol": 1e-12, "maxiter": 500, "adaptive": True},
                )
                val = -res.fun
                if val > best_val:
                    best_val = val
                    sf, qf = res.x
                    sf = np.clip(sf, 0, 1)
                    qf = np.clip(qf, 0, max(0, 1 - sf))
                    best_s = sf * w
                    best_q = qf * w / p if p > 0 else 0.0

            V_refined[i_w] = best_val
            s_refined[i_w] = best_s
            q_refined[i_w] = best_q

    if verbose:
        improvement = np.max(np.abs(V_refined - V))
        print(f"  Refinement: max |V_refined - V_grid| = {improvement:.2e}")

    return V_refined, s_refined, q_refined


def solve_vfi(
    alpha=0.6,
    beta=0.95,
    p=None,
    R_bar=1.0,
    E_R=1.05,
    sigma_R=0.2,
    w_j=1.0,
    w_grid=None,
    n_grid=200,
    n_quad=50,
    n_actions=80,
    n_refine_starts=10,
    n_workers=1,
    tol=1e-6,
    max_iter=500,
    verbose=True,
):
    """Solve the dynamic problem by value function iteration.

    Two phases:
    1. Vectorized grid search VFI until convergence (fast)
    2. Single refinement pass with Nelder-Mead multi-start (smooth policies)

    Parameters
    ----------
    alpha, beta, p, R_bar, E_R, sigma_R, w_j : model parameters
    w_grid : array or None
        Wealth grid.
    n_grid : int
        Number of grid points.
    n_quad : int
        Quadrature points for return distribution.
    n_actions : int
        Grid density for action search.
    n_refine_starts : int
        Number of Nelder-Mead starting points per grid point.
    n_workers : int
        Number of parallel workers for refinement (1 = sequential with neighbor-seeding).
    tol : float
        Convergence tolerance (sup norm).
    max_iter : int
        Maximum VFI iterations.
    verbose : bool
        Print progress.
    """
    if w_grid is None:
        w_grid = np.linspace(0.01, 10.0, n_grid)
    n_w = len(w_grid)

    # Lognormal return distribution
    mu_ln = np.log(E_R) - 0.5 * sigma_R**2
    R_nodes, R_weights = gauss_hermite_lognormal(mu_ln, sigma_R, n_quad)

    # Actuarially fair premium
    if p is None:
        p = np.sum(R_weights * np.maximum(0.0, R_bar - R_nodes))
    if verbose:
        print(f"Insurance premium p = {p:.6f}")

    # Action grid
    s_fracs, q_fracs = make_action_grid(n_actions)
    if verbose:
        print(f"Action grid: {len(s_fracs)} feasible pairs (n_actions={n_actions})")

    # Initialize value function
    V = indirect_utility(w_grid, w_j, alpha) / (1 - beta)
    errors = []
    w_min, w_max = w_grid[0], w_grid[-1]

    # === Phase 1: Vectorized grid search VFI ===
    if verbose:
        print("Phase 1: Vectorized grid search VFI")

    s_policy = np.zeros(n_w)
    q_policy = np.zeros(n_w)

    for iteration in range(max_iter):
        V_interp = interp1d(w_grid, V, kind="linear", fill_value="extrapolate")

        V_new, s_policy, q_policy = _bellman_rhs_vectorized(
            w_grid, s_fracs, q_fracs, p, w_j, alpha, beta,
            R_nodes, R_bar, R_weights, V_interp, w_min, w_max
        )

        err = np.max(np.abs(V_new - V))
        errors.append(err)
        if verbose and (iteration % 20 == 0 or err < tol):
            print(f"  Iteration {iteration:4d}: ||V_new - V|| = {err:.2e}")

        V[:] = V_new
        if err < tol:
            if verbose:
                print(f"  Converged in {iteration + 1} iterations.")
            break
    else:
        if verbose:
            print(f"  WARNING: Did not converge after {max_iter} iterations (err={err:.2e}).")

    converged = err < tol
    n_iter = min(iteration + 1, max_iter)

    # === Phase 2: Refine policies ===
    if verbose:
        print(f"Phase 2: Nelder-Mead policy refinement ({n_refine_starts} starts, {n_workers} workers)")

    V_ref, s_ref, q_ref = _refine_policies(
        w_grid, V, s_policy, q_policy, p, w_j, alpha, beta,
        R_nodes, R_bar, R_weights, n_refine_starts, n_workers, verbose
    )

    return {
        "w_grid": w_grid.copy(),
        "V": V_ref,
        "s_policy": s_ref,
        "q_policy": q_ref,
        "converged": converged,
        "n_iter": n_iter,
        "errors": errors,
        "params": {
            "alpha": alpha, "beta": beta, "p": p,
            "R_bar": R_bar, "E_R": E_R, "sigma_R": sigma_R, "w_j": w_j,
        },
    }


def solve_vfi_parallel(param_list, n_workers=None, verbose=True):
    """Run multiple VFI solves in parallel (across different parameter sets).

    Parameters
    ----------
    param_list : list of dict
        Each dict is passed as kwargs to solve_vfi.
    n_workers : int or None
        Number of parallel processes. None = all available cores.

    Returns
    -------
    list of dict (same order as param_list)
    """
    import os
    if n_workers is None:
        n_workers = min(len(param_list), os.cpu_count() or 1)
    if verbose:
        print(f"Running {len(param_list)} VFI solves on {n_workers} workers")

    def _run_one(kwargs):
        return solve_vfi(**kwargs)

    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        results = list(executor.map(_run_one, param_list))

    return results
