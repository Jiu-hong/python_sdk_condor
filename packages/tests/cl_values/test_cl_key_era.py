"""Tests for CL (CasperLabs) era key functionality.

This module contains test cases for the CLKey class when handling era keys,
which represent specific eras in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid era key for testing
VALID_ERA_KEY = "era-42"

# Invalid era key for testing validation
INVALID_ERA_KEY = "era-h12"

# === Expected Values ===
EXPECTED = {
    "serialized": "052a00000000000000",
    "cl_value": "09000000052a000000000000000b",
    "json": "Key"
}

# === Valid Era Key Tests ===


def test_era_key_serialization():
    """Test serialization of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_era_key_value():
    """Test value retrieval of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.value()
    assert result == VALID_ERA_KEY


def test_era_key_cl_value():
    """Test CL value representation of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_era_key_to_json():
    """Test JSON representation of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Era Key Tests ===
def test_invalid_era_key_format():
    """Test era key format validation."""
    error_msg = "era value should be decimal int"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_ERA_KEY)
