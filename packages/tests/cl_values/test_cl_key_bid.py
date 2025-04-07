import pytest
from python_condor import CLKey


# ===== CLKey - bid =====

clkey_bid = CLKey(
    "bid-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1")


def test_clkey_bid_serialize():
    result = clkey_bid.serialize().hex()
    assert result == "07306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"


def test_clkey_bid_string_value():
    result = clkey_bid.value()
    assert result == "bid-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"


def test_clkey_bid_cl_value():
    result = clkey_bid.cl_value()
    assert result == "2100000007306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a10b"


def test_clkey_bid_to_json():
    result = clkey_bid.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_bid_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "bid-1234")
