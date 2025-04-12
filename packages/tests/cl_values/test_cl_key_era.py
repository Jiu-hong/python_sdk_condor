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

# Test data
VALID_ERA_KEY = "era-42"
INVALID_ERA_KEY = "era-h12"


# ===== CLKey - era =====
clkey_era = CLKey(
    "era-42")


def test_era_key_serialization():
    """Test serialization of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.serialize().hex()
    assert result == "052a00000000000000"


def test_era_key_value():
    """Test value retrieval of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.value()
    assert result == VALID_ERA_KEY


def test_era_key_cl_value():
    """Test CL value representation of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.cl_value()
    assert result == "09000000052a000000000000000b"


def test_era_key_to_json():
    """Test JSON representation of era key."""
    era_key = CLKey(VALID_ERA_KEY)
    result = era_key.to_json()
    assert result == "Key"


# === check invalid inner type
def test_invalid_era_key_format():
    """Test era key format validation."""
    with pytest.raises(ValueError, match="era value should be decimal int"):
        _ = CLKey(INVALID_ERA_KEY)
