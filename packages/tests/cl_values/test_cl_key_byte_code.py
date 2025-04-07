import pytest
from python_condor import CLKey


# ===== CLKey - byte_code_v1_wasm =====

clkey_byte_code_v1_wasm = CLKey(
    "byte-code-v1-wasm-6565656565656565656565656565656565656565656565656565656565656565")


def test_clkey_byte_code_v1_wasm_serialize():
    result = clkey_byte_code_v1_wasm.serialize().hex()
    assert result == "12016565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_v1_wasm_string_value():
    result = clkey_byte_code_v1_wasm.value()
    assert result == "byte-code-v1-wasm-6565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_v1_wasm_cl_value():
    result = clkey_byte_code_v1_wasm.cl_value()
    assert result == "22000000120165656565656565656565656565656565656565656565656565656565656565650b"


def test_clkey_byte_code_v1_wasm_to_json():
    result = clkey_byte_code_v1_wasm.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_byte_code_v1_wasm_invalid_inner_value():
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey("byte-code-v1-wasm-123")


# ===== CLKey - byte_code_v2_wasm =====
clkey_byte_code_v2_wasm = CLKey(
    "byte-code-v2-wasm-6565656565656565656565656565656565656565656565656565656565656565")


def test_clkey_byte_code_v2_wasm_serialize():
    result = clkey_byte_code_v2_wasm.serialize().hex()
    assert result == "12026565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_v2_wasm_string_value():
    result = clkey_byte_code_v2_wasm.value()
    assert result == "byte-code-v2-wasm-6565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_v2_wasm_cl_value():
    result = clkey_byte_code_v2_wasm.cl_value()
    assert result == "22000000120265656565656565656565656565656565656565656565656565656565656565650b"


def test_clkey_byte_code_v2_wasm_to_json():
    result = clkey_byte_code_v2_wasm.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_byte_code_v2_wasm_invalid_inner_value():
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey("byte-code-v2-wasm-123")


# ===== CLKey - byte_code_empty =====
clkey_byte_code_empty = CLKey(
    "byte-code-empty-6565656565656565656565656565656565656565656565656565656565656565")


def test_clkey_byte_code_empty_serialize():
    result = clkey_byte_code_empty.serialize().hex()
    assert result == "1200"


def test_clkey_byte_code_empty_string_value():
    result = clkey_byte_code_empty.value()
    assert result == "byte-code-empty-6565656565656565656565656565656565656565656565656565656565656565"


def test_clkey_byte_code_empty_cl_value():
    result = clkey_byte_code_empty.cl_value()
    assert result == "0200000012000b"


def test_clkey_byte_code_empty_to_json():
    result = clkey_byte_code_empty.to_json()
    assert result == "Key"

# === check invalid inner type


def test_clkey_byte_code_empty_invalid_inner_value():
    with pytest.raises(ValueError, match="invalid byte-code-xxx"):
        _ = CLKey("byte-code-emp-123")
