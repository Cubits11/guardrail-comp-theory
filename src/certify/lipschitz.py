"""Helpers for Lipschitz adversarial taxes."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LipschitzRails:
    """Lipschitz moduli for two rails."""

    L_A: float
    L_B: float


def adversarial_fh_tax(min_ceiling: float, eps_wasserstein: float, rails: LipschitzRails) -> float:
    """Add the Lipschitz tax to an FH ceiling, clamped to $[0,1]$."""
    taxed = min_ceiling + eps_wasserstein * (rails.L_A + rails.L_B)
    return max(0.0, min(1.0, taxed))
