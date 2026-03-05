"""
Publication-quality figures for the intrahousehold dynamics paper.

Figure 1: Indirect utility v_i(y_i) for fixed y_j
Figure 2: Marginal utility lambda_i(y_i) — discrete jumps at regime boundaries
Figure 3: Value function V_i(w_i) for different w_j levels
Figure 4: Investment policy s*(w_i) by w_j
Figure 5: Insurance policy q*(w_i) by w_j
Figure 6: Comparative statics in alpha
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from model import K, indirect_utility, marginal_utility, regime_boundaries

# --- Style ---
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 11,
        "axes.labelsize": 13,
        "axes.titlesize": 13,
        "legend.fontsize": 10,
        "figure.figsize": (6, 4),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)

USF_GREEN = "#00543C"
USF_GOLD = "#FDBB30"
COLORS = [USF_GREEN, USF_GOLD, "#1f77b4", "#d62728", "#9467bd"]


def _add_regime_lines(ax, y_j, alpha, ymin=None, ymax=None):
    """Add vertical dashed lines at regime boundaries."""
    y_lower, y_upper = regime_boundaries(y_j, alpha)
    kw = dict(color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.axvline(y_lower, **kw)
    ax.axvline(y_upper, **kw)
    # Labels at top
    ylim = ax.get_ylim()
    y_pos = ylim[1] * 0.95 if ymax is None else ymax * 0.95
    ax.text(y_lower, y_pos, r"$\alpha y_j$", ha="center", fontsize=8, color="gray")
    ax.text(y_upper, y_pos, r"$y_j/\alpha$", ha="center", fontsize=8, color="gray")


def fig1_indirect_utility(output_dir, alpha=0.6, y_j_values=(0.5, 1.0, 2.0)):
    """Figure 1: Indirect utility v_i(y_i) for fixed y_j values."""
    y_i = np.linspace(0.01, 5.0, 1000)

    fig, ax = plt.subplots()
    for idx, y_j in enumerate(y_j_values):
        v = indirect_utility(y_i, y_j, alpha)
        ax.plot(y_i, v, color=COLORS[idx], linewidth=1.5, label=f"$y_j = {y_j}$")

    # Show regime boundaries for middle case
    _add_regime_lines(ax, y_j_values[1], alpha)

    ax.set_xlabel(r"Own income $y_i$")
    ax.set_ylabel(r"Indirect utility $v_i(y_i, y_j)$")
    ax.set_title(rf"Indirect Utility ($\alpha = {alpha}$)")
    ax.legend()
    fig.savefig(os.path.join(output_dir, "fig1_indirect_utility.pdf"))
    plt.close(fig)
    print("  Saved fig1_indirect_utility.pdf")


def fig2_marginal_utility(output_dir, alpha=0.6, y_j=1.0):
    """Figure 2: Marginal utility showing discrete jump at regime boundary."""
    y_i = np.linspace(0.01, 5.0, 1000)
    dv = marginal_utility(y_i, y_j, alpha)

    fig, ax = plt.subplots()
    ax.plot(y_i, dv, color=USF_GREEN, linewidth=1.5)

    _add_regime_lines(ax, y_j, alpha)

    # Annotate the jump
    k = K(alpha)
    ax.axhline(k / (1 + alpha), color="gray", linestyle=":", linewidth=0.6, alpha=0.5)
    ax.axhline(k, color="gray", linestyle=":", linewidth=0.6, alpha=0.5)
    ax.text(4.5, k + 0.01, r"$K$", fontsize=9, color="gray")
    ax.text(4.5, k / (1 + alpha) + 0.01, r"$K/(1+\alpha)$", fontsize=9, color="gray")

    ax.set_xlabel(r"Own income $y_i$")
    ax.set_ylabel(r"Marginal utility $\partial v_i / \partial y_i$")
    ax.set_title(rf"Marginal Utility ($\alpha = {alpha}$, $y_j = {y_j}$)")
    fig.savefig(os.path.join(output_dir, "fig2_marginal_utility.pdf"))
    plt.close(fig)
    print("  Saved fig2_marginal_utility.pdf")


def fig3_value_function(output_dir, results_by_wj):
    """Figure 3: Value function V_i(w_i) for different w_j levels."""
    fig, ax = plt.subplots()
    for idx, (w_j, res) in enumerate(sorted(results_by_wj.items())):
        ax.plot(
            res["w_grid"],
            res["V"],
            color=COLORS[idx],
            linewidth=1.5,
            label=f"$w_j = {w_j}$",
        )

    ax.set_xlabel(r"Own wealth $w_i$")
    ax.set_ylabel(r"Value function $V_i(w_i)$")
    alpha = list(results_by_wj.values())[0]["params"]["alpha"]
    ax.set_title(rf"Value Function ($\alpha = {alpha}$)")
    ax.legend()
    fig.savefig(os.path.join(output_dir, "fig3_value_function.pdf"))
    plt.close(fig)
    print("  Saved fig3_value_function.pdf")


def fig4_investment_policy(output_dir, results_by_wj):
    """Figure 4: Investment policy s*(w_i) for different w_j."""
    fig, ax = plt.subplots()
    for idx, (w_j, res) in enumerate(sorted(results_by_wj.items())):
        ax.plot(
            res["w_grid"],
            res["s_policy"],
            color=COLORS[idx],
            linewidth=1.5,
            label=f"$w_j = {w_j}$",
        )

    ax.set_xlabel(r"Own wealth $w_i$")
    ax.set_ylabel(r"Investment $s^*(w_i)$")
    alpha = list(results_by_wj.values())[0]["params"]["alpha"]
    ax.set_title(rf"Investment Policy ($\alpha = {alpha}$)")
    ax.legend()
    fig.savefig(os.path.join(output_dir, "fig4_investment_policy.pdf"))
    plt.close(fig)
    print("  Saved fig4_investment_policy.pdf")


def fig5_insurance_policy(output_dir, results_by_wj):
    """Figure 5: Insurance policy q*(w_i) for different w_j."""
    fig, ax = plt.subplots()
    for idx, (w_j, res) in enumerate(sorted(results_by_wj.items())):
        ax.plot(
            res["w_grid"],
            res["q_policy"],
            color=COLORS[idx],
            linewidth=1.5,
            label=f"$w_j = {w_j}$",
        )

    ax.set_xlabel(r"Own wealth $w_i$")
    ax.set_ylabel(r"Insurance coverage $q^*(w_i)$")
    alpha = list(results_by_wj.values())[0]["params"]["alpha"]
    ax.set_title(rf"Insurance Policy ($\alpha = {alpha}$)")
    ax.legend()
    fig.savefig(os.path.join(output_dir, "fig5_insurance_policy.pdf"))
    plt.close(fig)
    print("  Saved fig5_insurance_policy.pdf")


def fig6_comparative_statics_alpha(output_dir, results_by_alpha):
    """Figure 6: Comparative statics in alpha (investment and insurance side by side)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    for idx, (alpha, res) in enumerate(sorted(results_by_alpha.items())):
        label = rf"$\alpha = {alpha}$"
        ax1.plot(res["w_grid"], res["s_policy"], color=COLORS[idx], linewidth=1.5, label=label)
        ax2.plot(res["w_grid"], res["q_policy"], color=COLORS[idx], linewidth=1.5, label=label)

    ax1.set_xlabel(r"Own wealth $w_i$")
    ax1.set_ylabel(r"Investment $s^*(w_i)$")
    ax1.set_title("Investment Policy")
    ax1.legend()

    ax2.set_xlabel(r"Own wealth $w_i$")
    ax2.set_ylabel(r"Insurance coverage $q^*(w_i)$")
    ax2.set_title("Insurance Policy")
    ax2.legend()

    fig.suptitle("Comparative Statics in Public Goods Weight", fontsize=14, y=1.02)
    fig.savefig(os.path.join(output_dir, "fig6_comparative_statics.pdf"))
    plt.close(fig)
    print("  Saved fig6_comparative_statics.pdf")


def fig_convergence(output_dir, results):
    """Supplementary: VFI convergence plot."""
    fig, ax = plt.subplots()
    ax.semilogy(results["errors"], color=USF_GREEN, linewidth=1.5)
    ax.axhline(1e-6, color="gray", linestyle="--", linewidth=0.8)
    ax.set_xlabel("Iteration")
    ax.set_ylabel(r"$\|V^{n+1} - V^n\|_\infty$")
    ax.set_title("VFI Convergence")
    fig.savefig(os.path.join(output_dir, "fig_convergence.pdf"))
    plt.close(fig)
    print("  Saved fig_convergence.pdf")
