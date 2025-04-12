"""Tests for CL (Casper) URef key functionality.

This module contains test cases for the CLKey class when handling URef (Unforgeable Reference) keys,
which represent unique references in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation (length and suffix)
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid URef key for testing
VALID_UREF_KEY = "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"

# Invalid URef keys for testing validation
INVALID_LENGTH_UREF_KEY = "uref-1234-002"
INVALID_SUFFIX_UREF_KEY = "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f"

# === Expected Values ===
EXPECTED = {
    "serialized": "02fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07",
    "cl_value": "2200000002fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f070b",
    "json": "Key"
}

# === Valid URef Key Tests ===


def test_uref_key_serialization():
    """Test serialization of URef key."""
    uref_key = CLKey(VALID_UREF_KEY)
    result = uref_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_uref_key_value():
    """Test value retrieval of URef key."""
    uref_key = CLKey(VALID_UREF_KEY)
    result = uref_key.value()
    assert result == VALID_UREF_KEY


def test_uref_key_cl_value():
    """Test CL value representation of URef key."""
    uref_key = CLKey(VALID_UREF_KEY)
    result = uref_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_uref_key_to_json():
    """Test JSON representation of URef key."""
    uref_key = CLKey(VALID_UREF_KEY)
    result = uref_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid URef Key Tests ===
def test_invalid_uref_key_length():
    """Test URef key length validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_LENGTH_UREF_KEY)


def test_invalid_uref_key_suffix():
    """Test URef key suffix validation."""
    error_msg = "uref should end with '000 - 007'"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_SUFFIX_UREF_KEY)
