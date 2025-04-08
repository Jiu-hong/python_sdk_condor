import pytest
from python_condor import CLKey


# ===== CLKey - BlockGlobal block-time-=====
clkey_block_time = CLKey(
    "block-time-00000000000000000000000000000000000000000000000000000000000000")


def test_clkey_block_time_serialize():
    result = clkey_block_time.serialize().hex()
    assert result == "150000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_block_time_string_value():
    result = clkey_block_time.value()
    assert result == "block-time-00000000000000000000000000000000000000000000000000000000000000"


def test_clkey_block_time_cl_value():
    result = clkey_block_time.cl_value()
    assert result == "210000001500000000000000000000000000000000000000000000000000000000000000000b"


def test_clkey_block_time_to_json():
    result = clkey_block_time.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_block_time_invalid_prefix():
    with pytest.raises(ValueError, match="Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'"):
        _ = CLKey(
            "block-time1-00000000000000000000000000000000000000000000000000000000000000")


# === check invalid inner type
def test_clkey_block_message_invalid_prefix():
    with pytest.raises(ValueError, match="Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'"):
        _ = CLKey(
            "block-message1-count-00000000000000000000000000000000000000000000000000000000000000")


# ===== CLKey - BlockGlobal block-message-count-=====
clkey_block_message_count = CLKey(
    "block-message-count-00000000000000000000000000000000000000000000000000000000000000")


def test_clkey_block_message_count_serialize():
    result = clkey_block_message_count.serialize().hex()
    assert result == "150100000000000000000000000000000000000000000000000000000000000000"


def test_clkey_block_message_count_string_value():
    result = clkey_block_message_count.value()
    assert result == "block-message-count-00000000000000000000000000000000000000000000000000000000000000"


def test_clkey_block_message_count_cl_value():
    result = clkey_block_message_count.cl_value()
    assert result == "210000001501000000000000000000000000000000000000000000000000000000000000000b"


def test_clkey_block_message_count_to_json():
    result = clkey_block_message_count.to_json()
    assert result == "Key"
