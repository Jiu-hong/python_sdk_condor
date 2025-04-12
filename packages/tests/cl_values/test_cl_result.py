"""Tests for CL (Casper) result functionality.

This module contains test cases for the CLResult class, which represents Result
types in the Casper network. The tests cover three main scenarios:
1. Ok variant with a complex value (Option<Tuple2<String, U64>>)
2. Err variant with a simple value (U32)
3. Invalid inputs and type validation

For each success scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
"""

from result import Err, Ok
import pytest

from python_condor import (
    CLBool,
    CLOption,
    CLResult,
    CLString,
    CLTuple2,
    CLU32,
    CLU64,
    NoneHolder,
)

# === Test Data for Ok Variant ===
OK_TEST_DATA = {
    'inner_string': "hello",
    'inner_u64': 123,
    'inner_tuple': CLTuple2((CLString("hello"), CLU64(123))),
    'inner_option': CLOption(CLTuple2((CLString("hello"), CLU64(123)))),
    'err_type': CLU32(NoneHolder()),
}

VALID_OK_RESULT = CLResult(
    Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
    Err(OK_TEST_DATA['err_type']),
    True
)

# === Test Data for Err Variant ===
ERR_TEST_DATA = {
    'err_value': 10,
    'ok_type': CLBool(NoneHolder()),
}

VALID_ERR_RESULT = CLResult(
    Ok(ERR_TEST_DATA['ok_type']),
    Err(CLU32(ERR_TEST_DATA['err_value'])),
    False
)

# === Expected Values for Ok Variant ===
OK_EXPECTED = {
    'serialized': "01010500000068656c6c6f7b00000000000000",
    'cl_value': "1300000001010500000068656c6c6f7b00000000000000100d130a0504",
    'value': {'Ok': ('hello', 123)},
    'json': {'Result': {'err': 'U32', 'ok': {
        'Option': {'Tuple2': ['String', 'U64']}}}}
}

# === Expected Values for Err Variant ===
ERR_EXPECTED = {
    'serialized': "000a000000",
    'cl_value': "05000000000a000000100004",
    'value': {'Err': 10},
    'json': {'Result': {'err': 'U32', 'ok': 'Bool'}}
}

# === Ok Variant Tests ===


def test_ok_result_serialization():
    """Test serialization of Ok variant."""
    result = VALID_OK_RESULT.serialize().hex()
    assert result == OK_EXPECTED['serialized']


def test_ok_result_value():
    """Test value retrieval of Ok variant."""
    result = VALID_OK_RESULT.value()
    assert result == OK_EXPECTED['value']


def test_ok_result_cl_value():
    """Test CL value representation of Ok variant."""
    result = VALID_OK_RESULT.cl_value()
    assert result == OK_EXPECTED['cl_value']


def test_ok_result_to_json():
    """Test JSON representation of Ok variant."""
    result = VALID_OK_RESULT.to_json()
    assert result == OK_EXPECTED['json']


# === Err Variant Tests ===

def test_err_result_serialization():
    """Test serialization of Err variant."""
    result = VALID_ERR_RESULT.serialize().hex()
    assert result == ERR_EXPECTED['serialized']


def test_err_result_value():
    """Test value retrieval of Err variant."""
    result = VALID_ERR_RESULT.value()
    assert result == ERR_EXPECTED['value']


def test_err_result_cl_value():
    """Test CL value representation of Err variant."""
    result = VALID_ERR_RESULT.cl_value()
    assert result == ERR_EXPECTED['cl_value']


def test_err_result_to_json():
    """Test JSON representation of Err variant."""
    result = VALID_ERR_RESULT.to_json()
    assert result == ERR_EXPECTED['json']


# === Validation Tests ===

def test_invalid_ok_type():
    """Test validation of Ok type input."""
    with pytest.raises(ValueError, match=r"ok value should be Ok\(clvalue\)"):
        _ = CLResult(Ok("invalid"), Err(CLU32(NoneHolder())), True)


def test_invalid_err_type():
    """Test validation of Err type input."""
    with pytest.raises(ValueError, match=r"err value should be Err\(clvalue\)"):
        _ = CLResult(Ok(CLBool(NoneHolder())), Err((NoneHolder())), False)


def test_invalid_result_type():
    """Test validation of Result type input."""
    with pytest.raises(ValueError, match=r"Ok value should be Ok\(...\)"):
        _ = CLResult("not_a_result", "not_a_result", True)
