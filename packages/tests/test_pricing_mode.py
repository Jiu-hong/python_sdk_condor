import pytest

from python_condor import PricingMode


# ===== PackageNameTarget without version =====

pricing_mode_classic = PricingMode("Classic", 123)


def test_pricing_classic_to_bytes():
    result = pricing_mode_classic.to_bytes().hex()
    assert result == "0400000000000000000001000100000002000900000003000a0000000b000000007b000000000000000101"


def test_pricing_classic_to_json():
    result = pricing_mode_classic.to_json()
    assert result == {'pricing_mode': {'PaymentLimited': {'gas_price_tolerance': 1,
                                                          'payment_amount': 123,
                                                          'standard_payment': True}}}


# === check incorrect pricing mode==
def test_contracthash_regex_pattern_not_match():
    with pytest.raises(ValueError, match="Invalid input: Fixed. Allowed values are: Classic"):
        _ = PricingMode("Fixed", 123)


# === check incorrect payment amount==
def test_contracthash_regex_pattern_not_match():
    with pytest.raises(TypeError, match=r"Invalid type of input: <class 'str'> for payment_amount. Allowed value is int"):
        _ = PricingMode("Classic", "123")
