"""Tests for CL (CasperLabs) package key functionality.

This module contains test cases for the CLKey class when handling package keys,
which represent package hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid package key for testing
VALID_PACKAGE_KEY = "package-6464646464646464646464646464646464646464646464646464646464646464"

# Invalid package key for testing validation
INVALID_PACKAGE_KEY = "package-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "106464646464646464646464646464646464646464646464646464646464646464",
    "cl_value": "210000001064646464646464646464646464646464646464646464646464646464646464640b",
    "json": "Key"
}

# === Valid Package Key Tests ===


def test_package_key_serialization():
    """Test serialization of package key."""
    package_key = CLKey(VALID_PACKAGE_KEY)
    result = package_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_package_key_value():
    """Test value retrieval of package key."""
    package_key = CLKey(VALID_PACKAGE_KEY)
    result = package_key.value()
    assert result == VALID_PACKAGE_KEY


def test_package_key_cl_value():
    """Test CL value representation of package key."""
    package_key = CLKey(VALID_PACKAGE_KEY)
    result = package_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_package_key_to_json():
    """Test JSON representation of package key."""
    package_key = CLKey(VALID_PACKAGE_KEY)
    result = package_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Package Key Tests ===
def test_invalid_package_key_format():
    """Test package key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_PACKAGE_KEY)
