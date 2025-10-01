from src.certify.fh import FHInterval
from src.certify.pac import bernstein_halfwidth, domain_adapt_inflation


def test_bernstein_monotone_with_n():
    interval = FHInterval(0.3, 0.8)
    h_small = bernstein_halfwidth(50, interval, 0.05)
    h_large = bernstein_halfwidth(500, interval, 0.05)
    assert 0.0 <= h_large <= h_small <= 1.0
    assert h_large < h_small


def test_domain_adapt_inflation_bounds():
    assert domain_adapt_inflation(0.0) == 0.0
    assert domain_adapt_inflation(2.0) == 1.0
    assert domain_adapt_inflation(1.0) == 0.5
