"""Tests for CL (CasperLabs) hash key functionality.

This module contains test cases for the CLKey class when handling hash keys,
which represent generic hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid hash key for testing
VALID_HASH_KEY = "hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"

# Invalid hash key for testing validation
INVALID_HASH_KEY = "hash-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "010102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20",
    "cl_value": "21000000010102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f200b",
    "json": "Key"
}

# === Valid Hash Key Tests ===


def test_hash_key_serialization():
    """Test serialization of hash key."""
    hash_key = CLKey(VALID_HASH_KEY)
    result = hash_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_hash_key_value():
    """Test value retrieval of hash key."""
    hash_key = CLKey(VALID_HASH_KEY)
    result = hash_key.value()
    assert result == VALID_HASH_KEY


def test_hash_key_cl_value():
    """Test CL value representation of hash key."""
    hash_key = CLKey(VALID_HASH_KEY)
    result = hash_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_hash_key_to_json():
    """Test JSON representation of hash key."""
    hash_key = CLKey(VALID_HASH_KEY)
    result = hash_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Hash Key Tests ===
def test_invalid_hash_key_format():
    """Test hash key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_HASH_KEY)
