"""Tests for CL (CasperLabs) byte code key functionality.

This module contains test cases for the CLKey class when handling byte code keys,
which represent different versions of WASM byte code in the Casper network.
The tests cover three types of byte code keys:
1. WASM v1 byte code
2. WASM v2 byte code
3. Empty byte code

For each type, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# Test data for byte code keys
VALID_BYTECODE_HASH = "6565656565656565656565656565656565656565656565656565656565656565"
VALID_V1_WASM_KEY = f"byte-code-v1-wasm-{VALID_BYTECODE_HASH}"
VALID_V2_WASM_KEY = f"byte-code-v2-wasm-{VALID_BYTECODE_HASH}"
VALID_EMPTY_KEY = f"byte-code-empty-{VALID_BYTECODE_HASH}"

INVALID_V1_WASM_KEY = "byte-code-v1-wasm-123"
INVALID_V2_WASM_KEY = "byte-code-v2-wasm-123"
INVALID_EMPTY_KEY = "byte-code-emp-123"

# === WASM v1 Byte Code Tests ===


def test_v1_wasm_serialization():
    """Test serialization of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_V1_WASM_KEY)
    result = byte_code_key.serialize().hex()
    assert result == "12016565656565656565656565656565656565656565656565656565656565656565"


def test_v1_wasm_value():
    """Test value retrieval of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_V1_WASM_KEY)
    result = byte_code_key.value()
    assert result == VALID_V1_WASM_KEY


def test_v1_wasm_cl_value():
    """Test CL value representation of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_V1_WASM_KEY)
    result = byte_code_key.cl_value()
    assert result == "22000000120165656565656565656565656565656565656565656565656565656565656565650b"


def test_v1_wasm_to_json():
    """Test JSON representation of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_V1_WASM_KEY)
    result = byte_code_key.to_json()
    assert result == "Key"


def test_invalid_v1_wasm_format():
    """Test validation of WASM v1 byte code key format."""
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey(INVALID_V1_WASM_KEY)


# === WASM v2 Byte Code Tests ===

def test_v2_wasm_serialization():
    """Test serialization of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_V2_WASM_KEY)
    result = byte_code_key.serialize().hex()
    assert result == "12026565656565656565656565656565656565656565656565656565656565656565"


def test_v2_wasm_value():
    """Test value retrieval of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_V2_WASM_KEY)
    result = byte_code_key.value()
    assert result == VALID_V2_WASM_KEY


def test_v2_wasm_cl_value():
    """Test CL value representation of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_V2_WASM_KEY)
    result = byte_code_key.cl_value()
    assert result == "22000000120265656565656565656565656565656565656565656565656565656565656565650b"


def test_v2_wasm_to_json():
    """Test JSON representation of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_V2_WASM_KEY)
    result = byte_code_key.to_json()
    assert result == "Key"


def test_invalid_v2_wasm_format():
    """Test validation of WASM v2 byte code key format."""
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey(INVALID_V2_WASM_KEY)


# === Empty Byte Code Tests ===

def test_empty_bytecode_serialization():
    """Test serialization of empty byte code key."""
    byte_code_key = CLKey(VALID_EMPTY_KEY)
    result = byte_code_key.serialize().hex()
    assert result == "1200"


def test_empty_bytecode_value():
    """Test value retrieval of empty byte code key."""
    byte_code_key = CLKey(VALID_EMPTY_KEY)
    result = byte_code_key.value()
    assert result == VALID_EMPTY_KEY


def test_empty_bytecode_cl_value():
    """Test CL value representation of empty byte code key."""
    byte_code_key = CLKey(VALID_EMPTY_KEY)
    result = byte_code_key.cl_value()
    assert result == "0200000012000b"


def test_empty_bytecode_to_json():
    """Test JSON representation of empty byte code key."""
    byte_code_key = CLKey(VALID_EMPTY_KEY)
    result = byte_code_key.to_json()
    assert result == "Key"


def test_invalid_empty_bytecode_format():
    """Test validation of empty byte code key format."""
    with pytest.raises(ValueError, match="invalid byte-code-xxx"):
        _ = CLKey(INVALID_EMPTY_KEY)
