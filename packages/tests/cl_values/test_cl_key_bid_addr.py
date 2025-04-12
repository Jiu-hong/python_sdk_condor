"""Tests for CL (CasperLabs) bid address key functionality.

This module contains test cases for the CLKey class when handling bid address keys,
which represent bid addresses in the Casper network. It tests two variants:
- Type 03: Public key bid address
- Type 00: Account hash bid address

For each variant, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid bid address keys for testing
VALID_BID_ADDR_03 = "bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"
VALID_BID_ADDR_00 = "bid-addr-00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"

# Invalid bid address key for testing validation
INVALID_BID_ADDR = "bid-addr-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"

# === Expected Values ===
EXPECTED = {
    "03": {
        "serialized": "0f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c",
        "cl_value": "420000000f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c0b",
        "json": "Key"
    },
    "00": {
        "serialized": "0f00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1",
        "cl_value": "220000000f00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a10b",
        "json": "Key"
    }
}

# === Type 03 Bid Address Key Tests ===


def test_bid_addr_03_serialization():
    """Test serialization of type 03 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_03)
    result = bid_addr.serialize().hex()
    assert result == EXPECTED["03"]["serialized"]


def test_bid_addr_03_value():
    """Test value retrieval of type 03 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_03)
    result = bid_addr.value()
    assert result == VALID_BID_ADDR_03


def test_bid_addr_03_cl_value():
    """Test CL value representation of type 03 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_03)
    result = bid_addr.cl_value()
    assert result == EXPECTED["03"]["cl_value"]


def test_bid_addr_03_to_json():
    """Test JSON representation of type 03 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_03)
    result = bid_addr.to_json()
    assert result == EXPECTED["03"]["json"]


# === Type 00 Bid Address Key Tests ===
def test_bid_addr_00_serialization():
    """Test serialization of type 00 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_00)
    result = bid_addr.serialize().hex()
    assert result == EXPECTED["00"]["serialized"]


def test_bid_addr_00_value():
    """Test value retrieval of type 00 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_00)
    result = bid_addr.value()
    assert result == VALID_BID_ADDR_00


def test_bid_addr_00_cl_value():
    """Test CL value representation of type 00 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_00)
    result = bid_addr.cl_value()
    assert result == EXPECTED["00"]["cl_value"]


def test_bid_addr_00_to_json():
    """Test JSON representation of type 00 bid address key."""
    bid_addr = CLKey(VALID_BID_ADDR_00)
    result = bid_addr.to_json()
    assert result == EXPECTED["00"]["json"]


# === Invalid Bid Address Key Tests ===
def test_invalid_bid_addr_format():
    """Test bid address key format validation."""
    error_msg = "not valid bid-addr prefix"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_BID_ADDR)
