"""Tests for CLKey class handling block global keys in the Casper network.

This module tests two types of block global keys:
1. Block Time Key: Represents a global block time key with a specific format
2. Block Message Count Key: Represents a global block message count key

For each key type, the following aspects are tested:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Invalid key format validation

The tests ensure that block global keys are properly formatted, serialized,
and that invalid formats are rejected with appropriate error messages.
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid block global keys
BLOCK_TIME_KEY = "block-time-00000000000000000000000000000000000000000000000000000000000000"
BLOCK_MESSAGE_COUNT_KEY = "block-message-count-00000000000000000000000000000000000000000000000000000000000000"

# Invalid block global keys for testing validation
INVALID_BLOCK_TIME_KEY = "block-time1-00000000000000000000000000000000000000000000000000000000000000"
INVALID_BLOCK_MESSAGE_KEY = "block-message1-count-00000000000000000000000000000000000000000000000000000000000000"

# Expected values for assertions
BLOCK_TIME_EXPECTED = {
    "serialized": "150000000000000000000000000000000000000000000000000000000000000000",
    "cl_value": "210000001500000000000000000000000000000000000000000000000000000000000000000b",
    "json": "Key"
}

BLOCK_MESSAGE_COUNT_EXPECTED = {
    "serialized": "150100000000000000000000000000000000000000000000000000000000000000",
    "cl_value": "210000001501000000000000000000000000000000000000000000000000000000000000000b",
    "json": "Key"
}

# Test instances
clkey_block_time = CLKey(BLOCK_TIME_KEY)
clkey_block_message_count = CLKey(BLOCK_MESSAGE_COUNT_KEY)

# === Block Time Key Tests ===


def test_block_time_key_serialization():
    """Test serialization of a block time key."""
    result = clkey_block_time.serialize().hex()
    assert result == BLOCK_TIME_EXPECTED["serialized"]


def test_block_time_key_string_value():
    """Test string value retrieval of a block time key."""
    result = clkey_block_time.value()
    assert result == BLOCK_TIME_KEY


def test_block_time_key_cl_value():
    """Test CL value representation of a block time key."""
    result = clkey_block_time.cl_value()
    assert result == BLOCK_TIME_EXPECTED["cl_value"]


def test_block_time_key_to_json():
    """Test JSON representation of a block time key."""
    result = clkey_block_time.to_json()
    assert result == BLOCK_TIME_EXPECTED["json"]


def test_block_time_key_invalid_prefix():
    """Test rejection of invalid block time key format."""
    error_msg = (
        "Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' "
        "or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'"
    )
    with pytest.raises(ValueError, match=error_msg):
        CLKey(INVALID_BLOCK_TIME_KEY)

# === Block Message Count Key Tests ===


def test_block_message_count_key_serialization():
    """Test serialization of a block message count key."""
    result = clkey_block_message_count.serialize().hex()
    assert result == BLOCK_MESSAGE_COUNT_EXPECTED["serialized"]


def test_block_message_count_key_string_value():
    """Test string value retrieval of a block message count key."""
    result = clkey_block_message_count.value()
    assert result == BLOCK_MESSAGE_COUNT_KEY


def test_block_message_count_key_cl_value():
    """Test CL value representation of a block message count key."""
    result = clkey_block_message_count.cl_value()
    assert result == BLOCK_MESSAGE_COUNT_EXPECTED["cl_value"]


def test_block_message_count_key_to_json():
    """Test JSON representation of a block message count key."""
    result = clkey_block_message_count.to_json()
    assert result == BLOCK_MESSAGE_COUNT_EXPECTED["json"]


def test_block_message_count_key_invalid_prefix():
    """Test rejection of invalid block message count key format."""
    error_msg = (
        "Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' "
        "or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'"
    )
    with pytest.raises(ValueError, match=error_msg):
        CLKey(INVALID_BLOCK_MESSAGE_KEY)
