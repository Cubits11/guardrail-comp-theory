"""Fréchet--Hoeffding interval helpers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FHInterval:
    """Closed interval [L, U] for Bernoulli probabilities."""

    L: float
    U: float

    def width(self) -> float:
        """Return the width of the interval, clamped at zero."""
        return max(0.0, self.U - self.L)

    def clamp(self) -> "FHInterval":
        """Clamp both endpoints to [0, 1] and ensure ordering."""
        L = max(0.0, min(1.0, self.L))
        U = max(0.0, min(1.0, self.U))
        if L > U:
            L, U = U, L
        return FHInterval(L, U)


def fh_and_bounds(alpha: float, beta: float) -> FHInterval:
    """FH bounds for the AND of two Bernoulli rails."""
    return FHInterval(max(0.0, alpha + beta - 1.0), min(alpha, beta)).clamp()


def fh_or_bounds(alpha: float, beta: float) -> FHInterval:
    """FH bounds for the OR of two Bernoulli rails."""
    return FHInterval(max(alpha, beta), min(1.0, alpha + beta)).clamp()


def fh_variance_envelope(interval: FHInterval) -> float:
    """Return the maximum Bernoulli variance within the interval."""
    L, U = interval.L, interval.U
    if L <= 0.5 <= U:
        return 0.25
    return max(L * (1 - L), U * (1 - U))
