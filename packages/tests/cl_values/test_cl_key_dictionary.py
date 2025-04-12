"""Tests for CL (Casper) dictionary key functionality.

This module contains test cases for the CLKey class when handling dictionary keys,
which represent dictionary hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid dictionary key for testing
VALID_DICTIONARY_KEY = "dictionary-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"

# Invalid dictionary key for testing validation
INVALID_DICTIONARY_KEY = "dictionary-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "092a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a",
    "cl_value": "21000000092a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b",
    "json": "Key"
}

# === Valid Dictionary Key Tests ===


def test_dictionary_key_serialization():
    """Test serialization of dictionary key."""
    dictionary_key = CLKey(VALID_DICTIONARY_KEY)
    result = dictionary_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_dictionary_key_value():
    """Test value retrieval of dictionary key."""
    dictionary_key = CLKey(VALID_DICTIONARY_KEY)
    result = dictionary_key.value()
    assert result == VALID_DICTIONARY_KEY


def test_dictionary_key_cl_value():
    """Test CL value representation of dictionary key."""
    dictionary_key = CLKey(VALID_DICTIONARY_KEY)
    result = dictionary_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_dictionary_key_to_json():
    """Test JSON representation of dictionary key."""
    dictionary_key = CLKey(VALID_DICTIONARY_KEY)
    result = dictionary_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Dictionary Key Tests ===
def test_invalid_dictionary_key_format():
    """Test dictionary key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_DICTIONARY_KEY)
