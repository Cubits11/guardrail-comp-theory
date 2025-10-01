from src.certify.lipschitz import LipschitzRails, adversarial_fh_tax


def test_tax_increases_with_eps_and_L():
    base = 0.8
    rails = LipschitzRails(L_A=0.5, L_B=0.7)
    t1 = adversarial_fh_tax(base, 0.0, rails)
    t2 = adversarial_fh_tax(base, 0.1, rails)
    t3 = adversarial_fh_tax(base, 0.2, rails)
    assert t1 == base
    assert t2 > t1
    assert t3 > t2
    assert 0.0 <= t3 <= 1.0
