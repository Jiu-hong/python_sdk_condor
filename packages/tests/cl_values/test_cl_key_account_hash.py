"""Tests for CL (Casper) account hash key functionality.

This module contains test cases for the CLKey class when handling account hash keys,
which represent account hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid account hash key for testing
VALID_ACCOUNT_HASH_KEY = "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"

# Invalid account hash key for testing validation
INVALID_ACCOUNT_HASH_KEY = "account-hash-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20",
    "cl_value": "21000000000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f200b",
    "json": "Key"
}

# === Valid Account Hash Key Tests ===


def test_account_hash_key_serialization():
    """Test serialization of account hash key."""
    account_hash_key = CLKey(VALID_ACCOUNT_HASH_KEY)
    result = account_hash_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_account_hash_key_value():
    """Test value retrieval of account hash key."""
    account_hash_key = CLKey(VALID_ACCOUNT_HASH_KEY)
    result = account_hash_key.value()
    assert result == VALID_ACCOUNT_HASH_KEY


def test_account_hash_key_cl_value():
    """Test CL value representation of account hash key."""
    account_hash_key = CLKey(VALID_ACCOUNT_HASH_KEY)
    result = account_hash_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_account_hash_key_to_json():
    """Test JSON representation of account hash key."""
    account_hash_key = CLKey(VALID_ACCOUNT_HASH_KEY)
    result = account_hash_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Account Hash Key Tests ===
def test_invalid_account_hash_key_format():
    """Test account hash key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_ACCOUNT_HASH_KEY)
