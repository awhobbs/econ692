"""
Core model definitions for the intrahousehold public goods game.

Implements the indirect utility function v_i(y_i, y_j) from Propositions 2-3
(symmetric case: alpha_i = alpha_j = alpha) and the dynamic transition equations.

Regimes (symmetric case):
    1. Both contribute (pooling):  alpha * y_j <= y_i <= y_j / alpha
    2. Only i contributes:         y_i > y_j / alpha
    3. Only j contributes:         y_i < alpha * y_j
"""

import numpy as np


def K(alpha):
    """Cobb-Douglas constant: K = alpha^alpha * (1-alpha)^(1-alpha)."""
    return alpha**alpha * (1 - alpha) ** (1 - alpha)


def regime_boundaries(y_j, alpha):
    """Return (y_lower, y_upper) boundaries for the pooling regime.

    y_lower = alpha * y_j      (below: only j contributes)
    y_upper = y_j / alpha      (above: only i contributes)
    """
    return alpha * y_j, y_j / alpha


def indirect_utility(y_i, y_j, alpha):
    """Piecewise indirect utility v_i(y_i, y_j) for symmetric alpha.

    From the proofs of Propositions 2 and 3:
        Pooling:           K/(1+alpha) * (y_i + y_j)
        i contributes:     K * y_i
        j contributes:     (1-alpha)^(1-alpha) * y_j^(1-alpha) * y_i^alpha
    """
    y_i = np.asarray(y_i, dtype=float)
    y_j = float(y_j)
    k = K(alpha)
    y_lower, y_upper = regime_boundaries(y_j, alpha)

    v = np.empty_like(y_i)

    # Regime masks
    pooling = (y_i >= y_lower) & (y_i <= y_upper)
    i_only = y_i > y_upper
    j_only = y_i < y_lower

    # Pooling: both contribute
    v[pooling] = k / (1 + alpha) * (y_i[pooling] + y_j)

    # Only i contributes
    v[i_only] = k * y_i[i_only]

    # Only j contributes
    v[j_only] = (1 - alpha) ** (1 - alpha) * y_j ** (1 - alpha) * y_i[j_only] ** alpha

    return v


def marginal_utility(y_i, y_j, alpha):
    """Marginal utility dv_i/dy_i for symmetric alpha.

        Pooling:       K / (1 + alpha)
        i contributes: K
        j contributes: alpha * (1-alpha)^(1-alpha) * y_j^(1-alpha) * y_i^(alpha-1)
    """
    y_i = np.asarray(y_i, dtype=float)
    y_j = float(y_j)
    k = K(alpha)
    y_lower, y_upper = regime_boundaries(y_j, alpha)

    dv = np.empty_like(y_i)

    pooling = (y_i >= y_lower) & (y_i <= y_upper)
    i_only = y_i > y_upper
    j_only = y_i < y_lower

    dv[pooling] = k / (1 + alpha)
    dv[i_only] = k
    dv[j_only] = (
        alpha * (1 - alpha) ** (1 - alpha) * y_j ** (1 - alpha) * y_i[j_only] ** (alpha - 1)
    )

    return dv


def insurance_payout(R, R_bar):
    """Insurance payout: psi(R) = max(0, R_bar - R)."""
    return np.maximum(0.0, R_bar - R)


def next_period_income(s, q, R, R_bar):
    """Next-period wealth: w' = R*s + q*psi(R)."""
    return R * s + q * insurance_payout(R, R_bar)
