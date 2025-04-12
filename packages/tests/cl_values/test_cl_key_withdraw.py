"""Tests for CL (CasperLabs) withdraw key functionality.

This module contains test cases for the CLKey class when handling withdraw keys,
which represent withdraw hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid withdraw key for testing
VALID_WITHDRAW_KEY = "withdraw-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"

# Invalid withdraw key for testing validation
INVALID_WITHDRAW_KEY = "withdraw-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "082a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a",
    "cl_value": "21000000082a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b",
    "json": "Key"
}

# === Valid Withdraw Key Tests ===


def test_withdraw_key_serialization():
    """Test serialization of withdraw key."""
    withdraw_key = CLKey(VALID_WITHDRAW_KEY)
    result = withdraw_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_withdraw_key_value():
    """Test value retrieval of withdraw key."""
    withdraw_key = CLKey(VALID_WITHDRAW_KEY)
    result = withdraw_key.value()
    assert result == VALID_WITHDRAW_KEY


def test_withdraw_key_cl_value():
    """Test CL value representation of withdraw key."""
    withdraw_key = CLKey(VALID_WITHDRAW_KEY)
    result = withdraw_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_withdraw_key_to_json():
    """Test JSON representation of withdraw key."""
    withdraw_key = CLKey(VALID_WITHDRAW_KEY)
    result = withdraw_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Withdraw Key Tests ===
def test_invalid_withdraw_key_format():
    """Test withdraw key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_WITHDRAW_KEY)
