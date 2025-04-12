"""Tests for CL (Casper) tuple functionality.

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

# === Test Data ===

# CLTuple1 test data
TUPLE1_DATA = {
    'string_value': "helloworld",
    'valid_tuple': CLTuple1(CLString("helloworld")),
}

# CLTuple2 test data
TUPLE2_DATA = {
    'string_value': "helloworld",
    'bool_value': True,
    'valid_tuple': CLTuple2((CLString("helloworld"), CLBool(True))),
}

# CLTuple3 test data
TUPLE3_DATA = {
    'u32_value': 1,
    'option_string': CLOption(None, CLString(NoneHolder())),
    'option_bool': CLOption(CLBool(True)),
    'valid_tuple': CLTuple3((
        CLU32(1),
        CLOption(None, CLString(NoneHolder())),
        CLOption(CLBool(True))
    )),
}

# === Expected Values ===

# CLTuple1 expected values
TUPLE1_EXPECTED = {
    'serialized': "0a00000068656c6c6f776f726c64",
    'cl_value': "0e0000000a00000068656c6c6f776f726c64120a",
    'value': ("helloworld",),
    'json': {'Tuple1': ['String']},
}

# CLTuple2 expected values
TUPLE2_EXPECTED = {
    'serialized': "0a00000068656c6c6f776f726c6401",
    'cl_value': "0f0000000a00000068656c6c6f776f726c6401130a00",
    'value': ("helloworld", True),
    'json': {'Tuple2': ['String', 'Bool']},
}

# CLTuple3 expected values
TUPLE3_EXPECTED = {
    'serialized': "01000000000101",
    'cl_value': "070000000100000000010114040d0a0d00",
    'value': (1, None, True),
    'json': {'Tuple3': ['U32', {'Option': 'String'}, {'Option': 'Bool'}]},
}

# === CLTuple1 Tests ===


def test_tuple1_serialization():
    """Test serialization of single-element tuple."""
    result = TUPLE1_DATA['valid_tuple'].serialize().hex()
    assert result == TUPLE1_EXPECTED['serialized']


def test_tuple1_value():
    """Test value retrieval of single-element tuple."""
    result = TUPLE1_DATA['valid_tuple'].value()
    assert result == TUPLE1_EXPECTED['value']


def test_tuple1_cl_value():
    """Test CL value representation of single-element tuple."""
    result = TUPLE1_DATA['valid_tuple'].cl_value()
    assert result == TUPLE1_EXPECTED['cl_value']


def test_tuple1_to_json():
    """Test JSON representation of single-element tuple."""
    result = TUPLE1_DATA['valid_tuple'].to_json()
    assert result == TUPLE1_EXPECTED['json']


def test_tuple1_invalid_length():
    """Test validation of single-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple1 length is 1."):
        _ = CLTuple1(CLString("test"), CLBool(True))


def test_tuple1_invalid_type():
    """Test validation of single-element tuple inner type."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple1("not_a_cl_value")


# === CLTuple2 Tests ===

def test_tuple2_serialization():
    """Test serialization of two-element tuple."""
    result = TUPLE2_DATA['valid_tuple'].serialize().hex()
    assert result == TUPLE2_EXPECTED['serialized']


def test_tuple2_value():
    """Test value retrieval of two-element tuple."""
    result = TUPLE2_DATA['valid_tuple'].value()
    assert result == TUPLE2_EXPECTED['value']


def test_tuple2_cl_value():
    """Test CL value representation of two-element tuple."""
    result = TUPLE2_DATA['valid_tuple'].cl_value()
    assert result == TUPLE2_EXPECTED['cl_value']


def test_tuple2_to_json():
    """Test JSON representation of two-element tuple."""
    result = TUPLE2_DATA['valid_tuple'].to_json()
    assert result == TUPLE2_EXPECTED['json']


def test_tuple2_invalid_length():
    """Test validation of two-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple2 length is 2."):
        _ = CLTuple2((CLString("test"),))


def test_tuple2_invalid_type():
    """Test validation of two-element tuple inner types."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple2(("not_cl_value", True))


# === CLTuple3 Tests ===

def test_tuple3_serialization():
    """Test serialization of three-element tuple."""
    result = TUPLE3_DATA['valid_tuple'].serialize().hex()
    assert result == TUPLE3_EXPECTED['serialized']


def test_tuple3_value():
    """Test value retrieval of three-element tuple."""
    result = TUPLE3_DATA['valid_tuple'].value()
    assert result == TUPLE3_EXPECTED['value']


def test_tuple3_cl_value():
    """Test CL value representation of three-element tuple."""
    result = TUPLE3_DATA['valid_tuple'].cl_value()
    assert result == TUPLE3_EXPECTED['cl_value']


def test_tuple3_to_json():
    """Test JSON representation of three-element tuple."""
    result = TUPLE3_DATA['valid_tuple'].to_json()
    assert result == TUPLE3_EXPECTED['json']


def test_tuple3_invalid_length():
    """Test validation of three-element tuple length."""
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("test"),))
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("test"), CLU32(1)))


def test_tuple3_invalid_type():
    """Test validation of three-element tuple inner types."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple3((1, 2, 3))


def test_tuple3_mixed_invalid_types():
    """Test validation of three-element tuple with mixed invalid types."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple3((CLString("test"), 2, CLBool(True)))
