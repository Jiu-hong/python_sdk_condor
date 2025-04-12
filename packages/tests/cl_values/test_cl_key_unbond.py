"""Tests for CL (Casper) unbond key functionality.

This module contains test cases for the CLKey class when handling unbond keys,
which represent unbonding hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid unbond key for testing
VALID_UNBOND_KEY = "unbond-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"

# Invalid unbond key for testing validation
INVALID_UNBOND_KEY = "unbond-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "0c2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a",
    "cl_value": "210000000c2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b",
    "json": "Key"
}

# === Valid Unbond Key Tests ===


def test_unbond_key_serialization():
    """Test serialization of unbond key."""
    unbond_key = CLKey(VALID_UNBOND_KEY)
    result = unbond_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_unbond_key_value():
    """Test value retrieval of unbond key."""
    unbond_key = CLKey(VALID_UNBOND_KEY)
    result = unbond_key.value()
    assert result == VALID_UNBOND_KEY


def test_unbond_key_cl_value():
    """Test CL value representation of unbond key."""
    unbond_key = CLKey(VALID_UNBOND_KEY)
    result = unbond_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_unbond_key_to_json():
    """Test JSON representation of unbond key."""
    unbond_key = CLKey(VALID_UNBOND_KEY)
    result = unbond_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Unbond Key Tests ===
def test_invalid_unbond_key_format():
    """Test unbond key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_UNBOND_KEY)
