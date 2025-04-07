import pytest
from python_condor import CLKey


# ===== CLKey - unbond =====

clkey_unbond = CLKey(
    "unbond-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_unbond_serialize():
    result = clkey_unbond.serialize().hex()
    assert result == "0c2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_unbond_string_value():
    result = clkey_unbond.value()
    assert result == "unbond-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_unbond_cl_value():
    result = clkey_unbond.cl_value()
    assert result == "210000000c2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b"


def test_clkey_unbond_to_json():
    result = clkey_unbond.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_unbond_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey("unbond-1234")
