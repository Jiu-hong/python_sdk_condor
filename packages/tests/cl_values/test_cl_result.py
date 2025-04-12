"""Tests for CL (CasperLabs) result functionality.

This module contains test cases for the CLResult class, which represents Result
types in the Casper network. The tests cover two scenarios:
1. Ok variant with a complex value (Option<Tuple2<String, U64>>)
2. Err variant with a simple value (U32)

For each scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
"""

from result import Err, Ok

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

# Test data for Ok variant
OK_INNER_STRING = "hello"
OK_INNER_U64 = 123
OK_INNER_TUPLE = CLTuple2((CLString(OK_INNER_STRING), CLU64(OK_INNER_U64)))
OK_INNER_OPTION = CLOption(OK_INNER_TUPLE)
OK_ERR_TYPE = CLU32(NoneHolder())
VALID_OK_RESULT = CLResult(Ok(OK_INNER_OPTION), Err(OK_ERR_TYPE), True)

# Test data for Err variant
ERR_VALUE = 10
ERR_OK_TYPE = CLBool(NoneHolder())
VALID_ERR_RESULT = CLResult(Ok(ERR_OK_TYPE), Err(CLU32(ERR_VALUE)), False)

# Expected values for assertions
EXPECTED_OK_SERIALIZED = "01010500000068656c6c6f7b00000000000000"
EXPECTED_OK_CL_VALUE = "1300000001010500000068656c6c6f7b00000000000000100d130a0504"
EXPECTED_OK_VALUE = {'Ok': ('hello', 123)}
EXPECTED_OK_JSON = {'Result': {'err': 'U32', 'ok': {
    'Option': {'Tuple2': ['String', 'U64']}}}}

EXPECTED_ERR_SERIALIZED = "000a000000"
EXPECTED_ERR_CL_VALUE = "05000000000a000000100004"
EXPECTED_ERR_VALUE = {'Err': 10}
EXPECTED_ERR_JSON = {'Result': {'err': 'U32', 'ok': 'Bool'}}

# === Ok Variant Tests ===


def test_ok_result_serialization():
    """Test serialization of Ok variant."""
    result = VALID_OK_RESULT.serialize().hex()
    assert result == EXPECTED_OK_SERIALIZED


def test_ok_result_value():
    """Test value retrieval of Ok variant."""
    result = VALID_OK_RESULT.value()
    assert result == EXPECTED_OK_VALUE


def test_ok_result_cl_value():
    """Test CL value representation of Ok variant."""
    result = VALID_OK_RESULT.cl_value()
    assert result == EXPECTED_OK_CL_VALUE


def test_ok_result_to_json():
    """Test JSON representation of Ok variant."""
    result = VALID_OK_RESULT.to_json()
    assert result == EXPECTED_OK_JSON


# === Err Variant Tests ===

def test_err_result_serialization():
    """Test serialization of Err variant."""
    result = VALID_ERR_RESULT.serialize().hex()
    assert result == EXPECTED_ERR_SERIALIZED


def test_err_result_value():
    """Test value retrieval of Err variant."""
    result = VALID_ERR_RESULT.value()
    assert result == EXPECTED_ERR_VALUE


def test_err_result_cl_value():
    """Test CL value representation of Err variant."""
    result = VALID_ERR_RESULT.cl_value()
    assert result == EXPECTED_ERR_CL_VALUE


def test_err_result_to_json():
    """Test JSON representation of Err variant."""
    result = VALID_ERR_RESULT.to_json()
    assert result == EXPECTED_ERR_JSON
