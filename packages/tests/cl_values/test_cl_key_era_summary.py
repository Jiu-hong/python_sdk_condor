"""Tests for CL (CasperLabs) era summary key functionality.

This module contains test cases for the CLKey class when handling era summary keys,
which represent era summary hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid era summary key for testing
VALID_ERA_SUMMARY_KEY = "era-summary-0000000000000000000000000000000000000000000000000000000000000000"

# Invalid era summary key for testing validation
INVALID_ERA_SUMMARY_KEY = "era-summary-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "0b0000000000000000000000000000000000000000000000000000000000000000",
    "cl_value": "210000000b00000000000000000000000000000000000000000000000000000000000000000b",
    "json": "Key"
}

# === Valid Era Summary Key Tests ===


def test_era_summary_key_serialization():
    """Test serialization of era summary key."""
    era_summary_key = CLKey(VALID_ERA_SUMMARY_KEY)
    result = era_summary_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_era_summary_key_value():
    """Test value retrieval of era summary key."""
    era_summary_key = CLKey(VALID_ERA_SUMMARY_KEY)
    result = era_summary_key.value()
    assert result == VALID_ERA_SUMMARY_KEY


def test_era_summary_key_cl_value():
    """Test CL value representation of era summary key."""
    era_summary_key = CLKey(VALID_ERA_SUMMARY_KEY)
    result = era_summary_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_era_summary_key_to_json():
    """Test JSON representation of era summary key."""
    era_summary_key = CLKey(VALID_ERA_SUMMARY_KEY)
    result = era_summary_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Era Summary Key Tests ===
def test_invalid_era_summary_key_format():
    """Test era summary key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_ERA_SUMMARY_KEY)
