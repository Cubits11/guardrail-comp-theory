"""PAC-style guardrail confidence helpers."""
from __future__ import annotations

from math import log, sqrt

from .fh import FHInterval, fh_variance_envelope


def bernstein_halfwidth(n: int, interval: FHInterval, delta: float) -> float:
    """Conservative Bernstein-style half-width using FH variance envelopes."""
    if n <= 1:
        return 1.0
    v = fh_variance_envelope(interval)
    a = sqrt(max(0.0, 2.0 * v * log(2.0 / delta) / n))
    b = (7.0 / 3.0) * log(2.0 / delta) / max(1.0, n - 1.0)
    return min(1.0, a + b)


def domain_adapt_inflation(h_delta_h: float) -> float:
    """Return the Ben-David style domain adaptation inflation term."""
    return max(0.0, min(1.0, 0.5 * h_delta_h))
