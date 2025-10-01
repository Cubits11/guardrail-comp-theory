import numpy as np
import pytest

from src.certify.causal import permutation_p_value, reintroduction_stat


def test_reintroduction_stat_basic():
    assert reintroduction_stat(0.3, 0.25) == pytest.approx(0.05)


def test_permutation_p_value_range():
    rng = np.random.default_rng(0)
    all_samples = rng.binomial(1, 0.3, size=400)
    a0_samples = all_samples[:80]
    obs = abs(a0_samples.mean() - all_samples.mean())
    p_val = permutation_p_value(obs, a0_samples, all_samples, iters=500, seed=0)
    assert 0.0 < p_val <= 1.0
