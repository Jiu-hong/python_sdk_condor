"""Tests for CL (CasperLabs) tuple functionality.

This module contains test cases for the CLTuple classes, which represent fixed-length
tuples of CL values in the Casper network. The tests cover three tuple types:
1. CLTuple1 - Single-element tuple
2. CLTuple2 - Two-element tuple
3. CLTuple3 - Three-element tuple

For each type, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Length validation
- Type validation
"""

import pytest

from python_condor import (
    CLBool,
    CLOption,
    CLString,
    CLTuple1,
    CLTuple2,
    CLTuple3,
    CLU32,
    NoneHolder,
)

# Test data for CLTuple1
TUPLE1_STRING = "helloworld"
VALID_TUPLE1 = CLTuple1(CLString(TUPLE1_STRING))

# Test data for CLTuple2
TUPLE2_STRING = "helloworld"
TUPLE2_BOOL = True
VALID_TUPLE2 = CLTuple2((CLString(TUPLE2_STRING), CLBool(TUPLE2_BOOL)))

# Test data for CLTuple3
TUPLE3_U32 = 1
TUPLE3_OPTION_STRING = CLOption(None, CLString(NoneHolder()))
TUPLE3_OPTION_BOOL = CLOption(CLBool(True))
VALID_TUPLE3 = CLTuple3(
    (CLU32(TUPLE3_U32), TUPLE3_OPTION_STRING, TUPLE3_OPTION_BOOL))

# === CLTuple1 Tests ===


def test_tuple1_serialization():
    """Test serialization of single-element tuple."""
    result = VALID_TUPLE1.serialize().hex()
    assert result == "0a00000068656c6c6f776f726c64"


def test_tuple1_value():
    """Test value retrieval of single-element tuple."""
    result = VALID_TUPLE1.value()
    assert result == (TUPLE1_STRING,)


def test_tuple1_cl_value():
    """Test CL value representation of single-element tuple."""
    result = VALID_TUPLE1.cl_value()
    assert result == "0e0000000a00000068656c6c6f776f726c64120a"


def test_tuple1_to_json():
    """Test JSON representation of single-element tuple."""
    result = VALID_TUPLE1.to_json()
    assert result == {'Tuple1': ['String']}


def test_tuple1_invalid_length():
    """Test validation of single-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple1 length is 1."):
        _ = CLTuple1(CLString(TUPLE1_STRING), CLBool(True))


# === CLTuple2 Tests ===

def test_tuple2_serialization():
    """Test serialization of two-element tuple."""
    result = VALID_TUPLE2.serialize().hex()
    assert result == "0a00000068656c6c6f776f726c6401"


def test_tuple2_value():
    """Test value retrieval of two-element tuple."""
    result = VALID_TUPLE2.value()
    assert result == (TUPLE2_STRING, TUPLE2_BOOL)


def test_tuple2_cl_value():
    """Test CL value representation of two-element tuple."""
    result = VALID_TUPLE2.cl_value()
    assert result == "0f0000000a00000068656c6c6f776f726c6401130a00"


def test_tuple2_to_json():
    """Test JSON representation of two-element tuple."""
    result = VALID_TUPLE2.to_json()
    assert result == {'Tuple2': ['String', 'Bool']}


def test_tuple2_invalid_length():
    """Test validation of two-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple2 length is 2."):
        _ = CLTuple2((CLString(TUPLE2_STRING),))


# === CLTuple3 Tests ===

def test_tuple3_serialization():
    """Test serialization of three-element tuple."""
    result = VALID_TUPLE3.serialize().hex()
    assert result == "01000000000101"


def test_tuple3_value():
    """Test value retrieval of three-element tuple."""
    result = VALID_TUPLE3.value()
    assert result == (TUPLE3_U32, None, True)


def test_tuple3_cl_value():
    """Test CL value representation of three-element tuple."""
    result = VALID_TUPLE3.cl_value()
    assert result == "070000000100000000010114040d0a0d00"


def test_tuple3_to_json():
    """Test JSON representation of three-element tuple."""
    result = VALID_TUPLE3.to_json()
    assert result == {'Tuple3': [
        'U32', {'Option': 'String'}, {'Option': 'Bool'}]}


def test_tuple3_invalid_length():
    """Test validation of three-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("helloworld"),))
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("helloworld"), CLU32(1)))


def test_tuple3_invalid_type():
    """Test validation of three-element tuple inner types."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple3((1, 2, 3))
