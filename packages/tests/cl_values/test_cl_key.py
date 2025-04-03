import pytest

from python_condor import CLKey


# ===== CLKey =====

clkey = CLKey(
    "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")


def test_clkey_serialize():
    result = clkey.serialize().hex()
    assert result == "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"


def test_clkey_string_value():
    result = clkey.value()
    assert result == "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"


def test_clkey_cl_value():
    result = clkey.cl_value()
    assert result == "21000000000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f200b"


def test_clkey_to_json():
    result = clkey.to_json()
    assert result == "Key"
