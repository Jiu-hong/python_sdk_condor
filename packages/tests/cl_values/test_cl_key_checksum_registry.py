"""Tests for CL (CasperLabs) checksum registry key functionality.

This module contains test cases for the CLKey class when handling checksum registry keys,
which represent checksum registry hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid checksum registry key for testing
VALID_CHECKSUM_REGISTRY_KEY = "checksum-registry-0000000000000000000000000000000000000000000000000000000000000000"

# Invalid checksum registry key for testing validation
INVALID_CHECKSUM_REGISTRY_KEY = "checksum-registry-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "0e0000000000000000000000000000000000000000000000000000000000000000",
    "cl_value": "210000000e00000000000000000000000000000000000000000000000000000000000000000b",
    "json": "Key"
}

# === Valid Checksum Registry Key Tests ===


def test_checksum_registry_key_serialization():
    """Test serialization of checksum registry key."""
    checksum_registry_key = CLKey(VALID_CHECKSUM_REGISTRY_KEY)
    result = checksum_registry_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_checksum_registry_key_value():
    """Test value retrieval of checksum registry key."""
    checksum_registry_key = CLKey(VALID_CHECKSUM_REGISTRY_KEY)
    result = checksum_registry_key.value()
    assert result == VALID_CHECKSUM_REGISTRY_KEY


def test_checksum_registry_key_cl_value():
    """Test CL value representation of checksum registry key."""
    checksum_registry_key = CLKey(VALID_CHECKSUM_REGISTRY_KEY)
    result = checksum_registry_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_checksum_registry_key_to_json():
    """Test JSON representation of checksum registry key."""
    checksum_registry_key = CLKey(VALID_CHECKSUM_REGISTRY_KEY)
    result = checksum_registry_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Checksum Registry Key Tests ===
def test_invalid_checksum_registry_key_format():
    """Test checksum registry key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_CHECKSUM_REGISTRY_KEY)
