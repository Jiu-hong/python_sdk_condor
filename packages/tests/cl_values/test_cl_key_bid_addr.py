import pytest
from python_condor import CLKey


# ===== CLKey bid_addr 03=====

# bid-addr tag: 03
clkey_bid_addr_03 = CLKey(
    "bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c")


def test_clkey_bid_addr_03_serialize():
    result = clkey_bid_addr_03.serialize().hex()
    assert result == "0f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"


def test_clkey_bid_addr_03_string_value():
    result = clkey_bid_addr_03.value()
    assert result == "bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"


def test_clkey_bid_addr_03_cl_value():
    result = clkey_bid_addr_03.cl_value()
    assert result == "420000000f03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c0b"


def test_clkey_bid_addr_03_to_json():
    result = clkey_bid_addr_03.to_json()
    assert result == "Key"


# ===== CLKey bid_addr 00=====

# bid-addr tag: 00
clkey_bid_addr_00 = CLKey(
    "bid-addr-00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1")


def test_clkey_bid_addr_00_serialize():
    result = clkey_bid_addr_00.serialize().hex()
    assert result == "0f00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"


def test_clkey_bid_addr_00_string_value():
    result = clkey_bid_addr_00.value()
    assert result == "bid-addr-00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"


def test_clkey_bid_addr_00_cl_value():
    result = clkey_bid_addr_00.cl_value()
    assert result == "220000000f00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a10b"


def test_clkey_bid_addr_00_to_json():
    result = clkey_bid_addr_00.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_bid_addr_invalid_inner_value():
    with pytest.raises(ValueError, match="not valid bid-addr prefix"):
        _ = CLKey(
            "bid-addr-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1")
