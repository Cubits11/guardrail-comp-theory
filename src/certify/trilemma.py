"""Guardrail composition trilemma helpers."""
from __future__ import annotations

from dataclasses import dataclass

from .fh import FHInterval, fh_and_bounds, fh_or_bounds


@dataclass(frozen=True)
class Marginals:
    """Class-conditional guardrail hit rates."""

    alpha1: float
    beta1: float
    alpha0: float
    beta0: float


@dataclass(frozen=True)
class TrilemmaEnvelope:
    """FH intervals for the trilemma objectives."""

    p1: FHInterval
    p0: FHInterval
    o1: FHInterval
    tight: bool


def trilemma_envelope(m: Marginals) -> TrilemmaEnvelope:
    """Return FH intervals for the AND (harmful) and OR (benign) cases."""
    p1 = fh_and_bounds(m.alpha1, m.beta1)
    p0 = fh_or_bounds(m.alpha0, m.beta0)
    return TrilemmaEnvelope(p1=p1, p0=p0, o1=p1, tight=True)


def cannot_simultaneously_optimize(m: Marginals) -> bool:
    """True if FH intervals are non-degenerate, signalling the trilemma."""
    env = trilemma_envelope(m)
    return env.p1.width() > 0.0 or env.p0.width() > 0.0
