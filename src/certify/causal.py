"""Causal reintroduction diagnostics."""
from __future__ import annotations

import numpy as np


def reintroduction_stat(p_b_given_y1_a0: float, p_b_given_y1: float) -> float:
    """Absolute deviation between conditioned and marginal probabilities."""
    return abs(p_b_given_y1_a0 - p_b_given_y1)


def permutation_p_value(
    obs: float,
    samples_a0: np.ndarray,
    samples_all: np.ndarray,
    *,
    iters: int = 2000,
    seed: int | None = 0,
) -> float:
    """Estimate a permutation-style p-value for the reintroduction statistic."""
    rng = np.random.default_rng(seed)
    n0 = int(len(samples_a0))
    n = int(len(samples_all))
    if n0 == 0 or n == 0 or n0 > n:
        raise ValueError("Invalid sample sizes for permutation test")

    count = 0
    for _ in range(iters):
        idx = rng.choice(n, size=n0, replace=False)
        est = abs(float(samples_all[idx].mean()) - float(samples_all.mean()))
        if est >= obs - 1e-12:
            count += 1
    return (count + 1.0) / (iters + 1.0)
