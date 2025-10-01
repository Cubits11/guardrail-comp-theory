"""Synthetic experiment demonstrating guardrail composition helpers."""
from __future__ import annotations

import numpy as np

from src.certify.fh import fh_and_bounds, fh_or_bounds
from src.certify.pac import bernstein_halfwidth, domain_adapt_inflation
from src.certify.trilemma import Marginals, cannot_simultaneously_optimize, trilemma_envelope


def simulate(
    *,
    n1: int = 2000,
    n0: int = 2000,
    tpr_a: float = 0.85,
    tpr_b: float = 0.75,
    fpr_a: float = 0.03,
    fpr_b: float = 0.04,
    seed: int = 7,
) -> tuple[float, float, float, float, float, float, int, int]:
    """Simulate class-conditional rail outputs."""
    rng = np.random.default_rng(seed)
    a_y1 = rng.binomial(1, tpr_a, size=n1)
    b_y1 = rng.binomial(1, tpr_b, size=n1)
    a_y0 = rng.binomial(1, fpr_a, size=n0)
    b_y0 = rng.binomial(1, fpr_b, size=n0)

    alpha1 = float(a_y1.mean())
    beta1 = float(b_y1.mean())
    alpha0 = float(a_y0.mean())
    beta0 = float(b_y0.mean())

    p1_hat = float((a_y1 & b_y1).mean())
    p0_hat = float((a_y0 | b_y0).mean())
    return alpha1, beta1, alpha0, beta0, p1_hat, p0_hat, n1, n0


def main() -> None:
    alpha1, beta1, alpha0, beta0, p1_hat, p0_hat, n1, n0 = simulate()
    marginals = Marginals(alpha1=alpha1, beta1=beta1, alpha0=alpha0, beta0=beta0)
    envelope = trilemma_envelope(marginals)

    p1_interval = fh_and_bounds(alpha1, beta1)
    p0_interval = fh_or_bounds(alpha0, beta0)
    halfwidth = bernstein_halfwidth(n1, p1_interval, delta=0.05)
    inflation = domain_adapt_inflation(0.3)

    print("=== Synthetic Guardrail Report ===")
    print(
        "Empirical marginals (alpha1, beta1, alpha0, beta0) = "
        f"({alpha1:.3f}, {beta1:.3f}, {alpha0:.3f}, {beta0:.3f})"
    )
    print(f"Empirical joints: p1_hat={p1_hat:.3f}, p0_hat={p0_hat:.3f}")
    print(
        f"FH AND on Y=1: [{p1_interval.L:.3f}, {p1_interval.U:.3f}] width={p1_interval.width():.3f}"
    )
    print(
        f"FH OR on Y=0: [{p0_interval.L:.3f}, {p0_interval.U:.3f}] width={p0_interval.width():.3f}"
    )
    print(f"PAC half-width for p1 (delta=0.05): {halfwidth:.3f}")
    print(f"Domain adaptation inflation (hΔh=0.3): {inflation:.3f}")
    print(f"Trilemma impossibility flag: {cannot_simultaneously_optimize(marginals)}")
    print(f"Envelope tightness indicator: {envelope.tight}")


if __name__ == "__main__":
    main()
