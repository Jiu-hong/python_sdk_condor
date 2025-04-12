"""Tests for CL (Casper) byte code key functionality.

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

# === Test Data ===

# Valid byte code hash for testing
VALID_BYTECODE_HASH = "6565656565656565656565656565656565656565656565656565656565656565"

# Test data for each byte code type
VALID_KEYS = {
    'v1_wasm': f"byte-code-v1-wasm-{VALID_BYTECODE_HASH}",
    'v2_wasm': f"byte-code-v2-wasm-{VALID_BYTECODE_HASH}",
    'empty': f"byte-code-empty-{VALID_BYTECODE_HASH}",
}

# Invalid test data for validation
INVALID_KEYS = {
    'v1_wasm': "byte-code-v1-wasm-123",  # Invalid hash length
    'v2_wasm': "byte-code-v2-wasm-123",  # Invalid hash length
    'empty': "byte-code-emp-123",  # Invalid format
    # Wrong prefix
    'invalid_prefix': f"bytecode-v1-wasm-{VALID_BYTECODE_HASH}",
    # Invalid version
    'invalid_version': f"byte-code-v3-wasm-{VALID_BYTECODE_HASH}",
    'invalid_hash': "byte-code-v1-wasm-xyz123",  # Non-hex hash
}

# === Expected Values ===

# Expected values for WASM v1
V1_EXPECTED = {
    'serialized': "12016565656565656565656565656565656565656565656565656565656565656565",
    'cl_value': "22000000120165656565656565656565656565656565656565656565656565656565656565650b",
    'json': "Key",
}

# Expected values for WASM v2
V2_EXPECTED = {
    'serialized': "12026565656565656565656565656565656565656565656565656565656565656565",
    'cl_value': "22000000120265656565656565656565656565656565656565656565656565656565656565650b",
    'json': "Key",
}

# Expected values for empty byte code
EMPTY_EXPECTED = {
    'serialized': "1200",
    'cl_value': "0200000012000b",
    'json': "Key",
}

# === WASM v1 Byte Code Tests ===


def test_v1_wasm_serialization():
    """Test serialization of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v1_wasm'])
    result = byte_code_key.serialize().hex()
    assert result == V1_EXPECTED['serialized']


def test_v1_wasm_value():
    """Test value retrieval of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v1_wasm'])
    result = byte_code_key.value()
    assert result == VALID_KEYS['v1_wasm']


def test_v1_wasm_cl_value():
    """Test CL value representation of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v1_wasm'])
    result = byte_code_key.cl_value()
    assert result == V1_EXPECTED['cl_value']


def test_v1_wasm_to_json():
    """Test JSON representation of WASM v1 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v1_wasm'])
    result = byte_code_key.to_json()
    assert result == V1_EXPECTED['json']


def test_invalid_v1_wasm_format():
    """Test validation of WASM v1 byte code key format."""
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey(INVALID_KEYS['v1_wasm'])


# === WASM v2 Byte Code Tests ===

def test_v2_wasm_serialization():
    """Test serialization of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v2_wasm'])
    result = byte_code_key.serialize().hex()
    assert result == V2_EXPECTED['serialized']


def test_v2_wasm_value():
    """Test value retrieval of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v2_wasm'])
    result = byte_code_key.value()
    assert result == VALID_KEYS['v2_wasm']


def test_v2_wasm_cl_value():
    """Test CL value representation of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v2_wasm'])
    result = byte_code_key.cl_value()
    assert result == V2_EXPECTED['cl_value']


def test_v2_wasm_to_json():
    """Test JSON representation of WASM v2 byte code key."""
    byte_code_key = CLKey(VALID_KEYS['v2_wasm'])
    result = byte_code_key.to_json()
    assert result == V2_EXPECTED['json']


def test_invalid_v2_wasm_format():
    """Test validation of WASM v2 byte code key format."""
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey(INVALID_KEYS['v2_wasm'])


# === Empty Byte Code Tests ===

def test_empty_bytecode_serialization():
    """Test serialization of empty byte code key."""
    byte_code_key = CLKey(VALID_KEYS['empty'])
    result = byte_code_key.serialize().hex()
    assert result == EMPTY_EXPECTED['serialized']


def test_empty_bytecode_value():
    """Test value retrieval of empty byte code key."""
    byte_code_key = CLKey(VALID_KEYS['empty'])
    result = byte_code_key.value()
    assert result == VALID_KEYS['empty']


def test_empty_bytecode_cl_value():
    """Test CL value representation of empty byte code key."""
    byte_code_key = CLKey(VALID_KEYS['empty'])
    result = byte_code_key.cl_value()
    assert result == EMPTY_EXPECTED['cl_value']


def test_empty_bytecode_to_json():
    """Test JSON representation of empty byte code key."""
    byte_code_key = CLKey(VALID_KEYS['empty'])
    result = byte_code_key.to_json()
    assert result == EMPTY_EXPECTED['json']


def test_invalid_empty_bytecode_format():
    """Test validation of empty byte code key format."""
    with pytest.raises(ValueError, match="invalid prefix byte-code-xxx"):
        _ = CLKey(INVALID_KEYS['empty'])


# === Additional Validation Tests ===

def test_invalid_prefix():
    """Test validation of byte code key prefix."""
    with pytest.raises(ValueError, match="invalid prefix"):
        _ = CLKey(INVALID_KEYS['invalid_prefix'])


def test_invalid_version():
    """Test validation of byte code key version."""
    with pytest.raises(ValueError, match="invalid prefix byte-code-xxx"):
        _ = CLKey(INVALID_KEYS['invalid_version'])


def test_invalid_hash():
    """Test validation of byte code key hash format."""
    with pytest.raises(ValueError, match="bytescode should be hex string"):
        _ = CLKey(INVALID_KEYS['invalid_hash'])
