import pytest
from python_condor import CLKey


# ===== CLKey - balance =====

clkey_balance = CLKey(
    "balance-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_balance_serialize():
    result = clkey_balance.serialize().hex()
    assert result == "062a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_balance_string_value():
    result = clkey_balance.value()
    assert result == "balance-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_balance_cl_value():
    result = clkey_balance.cl_value()
    assert result == "21000000062a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b"


def test_clkey_balance_to_json():
    result = clkey_balance.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_balance_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "balance-1234")
