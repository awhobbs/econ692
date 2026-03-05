"""
Main entry point: runs VFI for baseline parameters and generates all figures.

Usage:
    python run.py                    # Sequential (laptop)
    python run.py --parallel         # All 6 VFI runs in parallel (server)
    python run.py --parallel --workers 32  # Specify worker count
"""

import argparse
import os
import sys
import time

import numpy as np

# Ensure local imports work when running from this directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from figures import (
    fig1_indirect_utility,
    fig2_marginal_utility,
    fig3_value_function,
    fig4_investment_policy,
    fig5_insurance_policy,
    fig6_comparative_statics_alpha,
    fig_convergence,
)
from model import K, indirect_utility, regime_boundaries
from vfi import solve_vfi, solve_vfi_parallel

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# --- Shared parameters ---
VFI_KWARGS = dict(n_actions=80, n_refine_starts=10, n_grid=200, n_quad=50)


def verify_static_model(alpha=0.6):
    """Verify indirect_utility matches analytical expressions."""
    print("=" * 60)
    print("VERIFICATION: Static model")
    print("=" * 60)

    y_j = 1.0
    k = K(alpha)
    y_lower, y_upper = regime_boundaries(y_j, alpha)

    tests = [
        ("Pooling (y_i=1.0)", 1.0, k / (1 + alpha) * (1.0 + y_j)),
        ("i-only  (y_i=3.0)", 3.0, k * 3.0),
        ("j-only  (y_i=0.1)", 0.1, (1 - alpha) ** (1 - alpha) * y_j ** (1 - alpha) * 0.1**alpha),
    ]

    all_pass = True
    for name, y_i, expected in tests:
        computed = indirect_utility(np.array([y_i]), y_j, alpha)[0]
        match = np.isclose(computed, expected, rtol=1e-10)
        status = "PASS" if match else "FAIL"
        if not match:
            all_pass = False
        print(f"  {status}: {name}: computed={computed:.8f}, expected={expected:.8f}")

    eps = 1e-8
    v_at_lower_minus = indirect_utility(np.array([y_lower - eps]), y_j, alpha)[0]
    v_at_lower_plus = indirect_utility(np.array([y_lower + eps]), y_j, alpha)[0]
    v_at_upper_minus = indirect_utility(np.array([y_upper - eps]), y_j, alpha)[0]
    v_at_upper_plus = indirect_utility(np.array([y_upper + eps]), y_j, alpha)[0]

    cont_lower = np.isclose(v_at_lower_minus, v_at_lower_plus, rtol=1e-5)
    cont_upper = np.isclose(v_at_upper_minus, v_at_upper_plus, rtol=1e-5)
    print(f"  {'PASS' if cont_lower else 'FAIL'}: Continuity at y_lower={y_lower:.4f}")
    print(f"  {'PASS' if cont_upper else 'FAIL'}: Continuity at y_upper={y_upper:.4f}")

    if not (cont_lower and cont_upper):
        all_pass = False

    print(f"  Overall: {'ALL PASSED' if all_pass else 'SOME FAILED'}")
    print()
    return all_pass


def run_sequential():
    """Run all VFI solves sequentially (for laptops)."""
    w_j_values = [0.5, 1.0, 2.0]
    alpha_values = [0.4, 0.6, 0.8]

    results_by_wj = {}
    results_by_alpha = {}

    print("=" * 60)
    print("VFI: Baseline runs (alpha=0.6)")
    print("=" * 60)
    for w_j in w_j_values:
        print(f"\n--- w_j = {w_j} ---")
        t0 = time.time()
        res = solve_vfi(alpha=0.6, w_j=w_j, **VFI_KWARGS, verbose=True)
        elapsed = time.time() - t0
        print(f"  Time: {elapsed:.1f}s, Converged: {res['converged']}, Iterations: {res['n_iter']}")
        results_by_wj[w_j] = res

    print("\n" + "=" * 60)
    print("VFI: Comparative statics in alpha")
    print("=" * 60)
    for alpha in alpha_values:
        print(f"\n--- alpha = {alpha} ---")
        t0 = time.time()
        res = solve_vfi(alpha=alpha, w_j=1.0, **VFI_KWARGS, verbose=True)
        elapsed = time.time() - t0
        print(f"  Time: {elapsed:.1f}s, Converged: {res['converged']}, Iterations: {res['n_iter']}")
        results_by_alpha[alpha] = res

    return results_by_wj, results_by_alpha


def run_parallel(n_workers=None):
    """Run all 6 VFI solves in parallel (for servers)."""
    w_j_values = [0.5, 1.0, 2.0]
    alpha_values = [0.4, 0.6, 0.8]

    # Build parameter list for all 6 runs
    param_list = []
    # Baseline runs: vary w_j with alpha=0.6
    for w_j in w_j_values:
        param_list.append(dict(alpha=0.6, w_j=w_j, verbose=False, **VFI_KWARGS))
    # Comparative statics: vary alpha with w_j=1.0
    for alpha in alpha_values:
        param_list.append(dict(alpha=alpha, w_j=1.0, verbose=False, **VFI_KWARGS))

    print("=" * 60)
    print(f"VFI: Running all 6 solves in parallel")
    print("=" * 60)
    t0 = time.time()
    all_results = solve_vfi_parallel(param_list, n_workers=n_workers)
    elapsed = time.time() - t0

    for i, res in enumerate(all_results):
        label = f"w_j={param_list[i]['w_j']}, alpha={param_list[i]['alpha']}"
        print(f"  {label}: converged={res['converged']}, iterations={res['n_iter']}")
    print(f"  Total time: {elapsed:.1f}s")

    results_by_wj = {wj: all_results[i] for i, wj in enumerate(w_j_values)}
    results_by_alpha = {a: all_results[3 + i] for i, a in enumerate(alpha_values)}

    return results_by_wj, results_by_alpha


def main():
    parser = argparse.ArgumentParser(description="Dynamic model simulation")
    parser.add_argument("--parallel", action="store_true",
                        help="Run all VFI solves in parallel (use on server)")
    parser.add_argument("--workers", type=int, default=None,
                        help="Number of parallel workers (default: all cores)")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    np.random.seed(42)

    # Step 1: Verify static model
    verify_static_model()

    # Step 2: Static figures
    print("=" * 60)
    print("FIGURES: Static model (Figures 1-2)")
    print("=" * 60)
    fig1_indirect_utility(OUTPUT_DIR)
    fig2_marginal_utility(OUTPUT_DIR)

    # Step 3: VFI runs
    if args.parallel:
        results_by_wj, results_by_alpha = run_parallel(args.workers)
    else:
        results_by_wj, results_by_alpha = run_sequential()

    # Step 4: Dynamic figures
    print("\n" + "=" * 60)
    print("FIGURES: Dynamic model (Figures 3-6)")
    print("=" * 60)
    fig3_value_function(OUTPUT_DIR, results_by_wj)
    fig4_investment_policy(OUTPUT_DIR, results_by_wj)
    fig5_insurance_policy(OUTPUT_DIR, results_by_wj)
    fig6_comparative_statics_alpha(OUTPUT_DIR, results_by_alpha)

    # Convergence plot
    fig_convergence(OUTPUT_DIR, results_by_wj[1.0])

    print("\n" + "=" * 60)
    print(f"All figures saved to {OUTPUT_DIR}/")
    print("=" * 60)


if __name__ == "__main__":
    main()
