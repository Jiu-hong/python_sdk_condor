"""
Tests for PricingMode functionality.

This module contains test cases for the PricingMode class, which represents
pricing configuration in Casper transactions. The tests verify:
- Pricing mode creation with Classic configuration
- Byte serialization
- JSON serialization
- Input validation for pricing mode types
- Input validation for payment amount types
"""

import pytest

from python_condor import PricingMode


# Test data setup
PRICING_MODE = "Classic"
PAYMENT_AMOUNT = 123


def create_test_pricing_mode() -> PricingMode:
    """
    Create a test pricing mode with sample data.

    Returns:
        PricingMode: A configured test pricing mode
    """
    return PricingMode(PRICING_MODE, PAYMENT_AMOUNT)


# Expected test results
EXPECTED_BYTES = "0400000000000000000001000100000002000900000003000a0000000b000000007b000000000000000101"

EXPECTED_JSON = {
    'pricing_mode': {
        'PaymentLimited': {
            'gas_price_tolerance': 1,
            'payment_amount': PAYMENT_AMOUNT,
            'standard_payment': True
        }
    }
}


def test_pricing_mode_to_bytes():
    """
    Test byte serialization of a pricing mode.

    Verifies that the pricing mode correctly serializes to the expected byte format.
    """
    pricing_mode = create_test_pricing_mode()
    result = pricing_mode.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_pricing_mode_to_json():
    """
    Test JSON serialization of a pricing mode.

    Verifies that the pricing mode correctly serializes to the expected JSON structure.
    """
    pricing_mode = create_test_pricing_mode()
    result = pricing_mode.to_json()
    assert result == EXPECTED_JSON


def test_pricing_mode_invalid_type():
    """
    Test validation of pricing mode type.

    Verifies that the pricing mode raises a ValueError when given an invalid type.
    """
    with pytest.raises(ValueError, match="Invalid input: Fixed. Allowed values are: Classic"):
        _ = PricingMode("Fixed", PAYMENT_AMOUNT)


def test_pricing_mode_invalid_payment_amount():
    """
    Test validation of payment amount type.

    Verifies that the pricing mode raises a TypeError when given an invalid payment amount type.
    """
    with pytest.raises(TypeError, match=r"Invalid type of input: <class 'str'> for payment_amount. Allowed value is int"):
        _ = PricingMode(PRICING_MODE, "123")
