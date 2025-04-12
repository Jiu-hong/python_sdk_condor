"""Tests for CL (Casper) balance key functionality.

This module contains test cases for the CLKey class when handling balance keys,
which represent account balance hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid balance key for testing
VALID_BALANCE_KEY = "balance-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"

# Invalid balance key for testing validation
INVALID_BALANCE_KEY = "balance-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "062a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a",
    "cl_value": "21000000062a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b",
    "json": "Key"
}

# === Valid Balance Key Tests ===


def test_balance_key_serialization():
    """Test serialization of balance key."""
    balance_key = CLKey(VALID_BALANCE_KEY)
    result = balance_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_balance_key_value():
    """Test value retrieval of balance key."""
    balance_key = CLKey(VALID_BALANCE_KEY)
    result = balance_key.value()
    assert result == VALID_BALANCE_KEY


def test_balance_key_cl_value():
    """Test CL value representation of balance key."""
    balance_key = CLKey(VALID_BALANCE_KEY)
    result = balance_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_balance_key_to_json():
    """Test JSON representation of balance key."""
    balance_key = CLKey(VALID_BALANCE_KEY)
    result = balance_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Balance Key Tests ===
def test_invalid_balance_key_format():
    """Test balance key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_BALANCE_KEY)
