import pytest

from src.certify.fh import FHInterval, fh_and_bounds, fh_or_bounds, fh_variance_envelope


def test_fh_and_bounds_basic():
    interval = fh_and_bounds(0.9, 0.8)
    assert interval.L == pytest.approx(0.7)
    assert interval.U == pytest.approx(0.8)


def test_fh_or_bounds_basic():
    interval = fh_or_bounds(0.02, 0.03)
    assert interval.L == pytest.approx(0.03)
    assert interval.U == pytest.approx(0.05)


def test_variance_envelope_straddle():
    interval = FHInterval(0.4, 0.6)
    assert fh_variance_envelope(interval) == pytest.approx(0.25)


def test_variance_envelope_endpoint():
    interval = FHInterval(0.2, 0.2)
    assert fh_variance_envelope(interval) == pytest.approx(0.16)
