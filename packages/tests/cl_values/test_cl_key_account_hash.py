import pytest
from python_condor import CLKey


# ===== CLKey - account_hash =====

clkey_account_hash = CLKey(
    "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")


def test_clkey_serialize():
    result = clkey_account_hash.serialize().hex()
    assert result == "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"


def test_clkey_string_value():
    result = clkey_account_hash.value()
    assert result == "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"


def test_clkey_cl_value():
    result = clkey_account_hash.cl_value()
    assert result == "21000000000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f200b"


def test_clkey_to_json():
    result = clkey_account_hash.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_account_hash_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "account-hash-1234")
