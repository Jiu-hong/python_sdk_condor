import pytest
from python_condor import CLKey


# ===== CLKey - withdraw =====

clkey_withdraw = CLKey(
    "withdraw-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_withdraw_serialize():
    result = clkey_withdraw.serialize().hex()
    assert result == "082a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_withdraw_string_value():
    result = clkey_withdraw.value()
    assert result == "withdraw-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_withdraw_cl_value():
    result = clkey_withdraw.cl_value()
    assert result == "21000000082a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b"


def test_clkey_withdraw_to_json():
    result = clkey_withdraw.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_withdraw_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "withdraw-1234")
