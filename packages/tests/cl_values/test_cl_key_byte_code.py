import pytest
from python_condor import CLKey


# ===== CLKey - byte_code =====

clkey_byte_code = CLKey(
    "byte-code-6565656565656565656565656565656565656565656565656565656565656565")


def test_clkey_byte_code_serialize():
    result = clkey_byte_code.serialize().hex()
    assert result == "12016565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_string_value():
    result = clkey_byte_code.value()
    assert result == "byte-code-6565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_cl_value():
    result = clkey_byte_code.cl_value()
    assert result == "22000000120165656565656565656565656565656565656565656565656565656565656565650b"


def test_clkey_byte_code_to_json():
    result = clkey_byte_code.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_byte_code_invalid_inner_value():
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey("byte-code-123")
