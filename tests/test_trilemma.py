from src.certify.trilemma import Marginals, cannot_simultaneously_optimize, trilemma_envelope


def test_trilemma_envelope_shapes():
    marginals = Marginals(alpha1=0.9, beta1=0.8, alpha0=0.02, beta0=0.03)
    envelope = trilemma_envelope(marginals)
    assert envelope.o1.L == envelope.p1.L
    assert envelope.o1.U == envelope.p1.U
    assert envelope.p0.L <= envelope.p0.U <= 1.0
    assert envelope.p1.L <= envelope.p1.U <= 1.0
    assert envelope.tight is True


def test_trilemma_impossibility_flag():
    marginals = Marginals(alpha1=0.9, beta1=0.8, alpha0=0.02, beta0=0.03)
    assert cannot_simultaneously_optimize(marginals) is True


def test_degenerate_pathology():
    marginals = Marginals(alpha1=1.0, beta1=1.0, alpha0=0.0, beta0=0.0)
    assert cannot_simultaneously_optimize(marginals) is False
