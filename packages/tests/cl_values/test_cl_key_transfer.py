"""Tests for CL (Casper) transfer key functionality.

This module contains test cases for the CLKey class when handling transfer keys,
which represent transfer hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid transfer key for testing
VALID_TRANSFER_KEY = "transfer-199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad"

# Invalid transfer key for testing validation
INVALID_TRANSFER_KEY = "transfer-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "03199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad",
    "cl_value": "2100000003199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad0b",
    "json": "Key"
}

# === Valid Transfer Key Tests ===


def test_transfer_key_serialization():
    """Test serialization of transfer key."""
    transfer_key = CLKey(VALID_TRANSFER_KEY)
    result = transfer_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_transfer_key_value():
    """Test value retrieval of transfer key."""
    transfer_key = CLKey(VALID_TRANSFER_KEY)
    result = transfer_key.value()
    assert result == VALID_TRANSFER_KEY


def test_transfer_key_cl_value():
    """Test CL value representation of transfer key."""
    transfer_key = CLKey(VALID_TRANSFER_KEY)
    result = transfer_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_transfer_key_to_json():
    """Test JSON representation of transfer key."""
    transfer_key = CLKey(VALID_TRANSFER_KEY)
    result = transfer_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Transfer Key Tests ===
def test_invalid_transfer_key_format():
    """Test transfer key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_TRANSFER_KEY)
