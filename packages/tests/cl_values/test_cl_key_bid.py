"""Tests for CL (Casper) bid key functionality.

This module contains test cases for the CLKey class when handling bid keys,
which represent bid hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid bid key for testing
VALID_BID_KEY = "bid-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"

# Invalid bid key for testing validation
INVALID_BID_KEY = "bid-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "07306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1",
    "cl_value": "2100000007306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a10b",
    "json": "Key"
}

# === Valid Bid Key Tests ===


def test_bid_key_serialization():
    """Test serialization of bid key."""
    bid_key = CLKey(VALID_BID_KEY)
    result = bid_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_bid_key_value():
    """Test value retrieval of bid key."""
    bid_key = CLKey(VALID_BID_KEY)
    result = bid_key.value()
    assert result == VALID_BID_KEY


def test_bid_key_cl_value():
    """Test CL value representation of bid key."""
    bid_key = CLKey(VALID_BID_KEY)
    result = bid_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_bid_key_to_json():
    """Test JSON representation of bid key."""
    bid_key = CLKey(VALID_BID_KEY)
    result = bid_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Bid Key Tests ===
def test_invalid_bid_key_format():
    """Test bid key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_BID_KEY)
