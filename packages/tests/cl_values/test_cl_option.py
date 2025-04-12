"""Tests for CL (Casper) option functionality.

This module contains test cases for the CLOption class, which represents optional
values in the Casper network. The tests cover four main scenarios:
1. Some value (CLString)
2. NoneHolder for type information only
3. Invalid inputs and type validation

For each success scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
"""

import pytest
from python_condor import CLOption, CLString, NoneHolder, CLU32

# === Test Data ===
TEST_DATA = {
    'string_value': "helloworld",
    'some_option': CLOption(CLString("helloworld")),
    'none_option': CLOption(CLString(NoneHolder())),
}

# === Expected Values ===
SOME_EXPECTED = {
    'serialized': "010a00000068656c6c6f776f726c64",
    'cl_value': "0f000000010a00000068656c6c6f776f726c640d0a",
    'value': "helloworld",
}

NONE_EXPECTED = {
    'serialized': "00",
    'cl_value': "01000000000d0a",
    'value': None,
}


JSON_EXPECTED = {"Option": "String"}

# == = Some Value Tests == =


def test_some_option_serialization():
    """Test serialization of Some(CLString) value."""
    result = TEST_DATA['some_option'].serialize().hex()
    assert result == SOME_EXPECTED['serialized']


def test_some_option_value():
    """Test value retrieval of Some(CLString) value."""
    result = TEST_DATA['some_option'].value()
    assert result == SOME_EXPECTED['value']


def test_some_option_cl_value():
    """Test CL value representation of Some(CLString) value."""
    result = TEST_DATA['some_option'].cl_value()
    assert result == SOME_EXPECTED['cl_value']


def test_some_option_to_json():
    """Test JSON representation of Some(CLString) value."""
    result = TEST_DATA['some_option'].to_json()
    assert result == JSON_EXPECTED


# === None  Tests ===

def test_none_option_serialization():
    """Test serialization of NoneHolder with type information."""
    result = TEST_DATA['none_option'].serialize().hex()
    assert result == NONE_EXPECTED['serialized']


def test_none_option_value():
    """Test value retrieval of NoneHolder with type information."""
    result = TEST_DATA['none_option'].value()
    assert result == NONE_EXPECTED['value']


def test_none_option_cl_value():
    """Test CL value representation of NoneHolder with type information."""
    result = TEST_DATA['none_option'].cl_value()
    assert result == NONE_EXPECTED['cl_value']


def test_none_option_to_json():
    """Test JSON representation of NoneHolder with type information."""
    result = TEST_DATA['none_option'].to_json()
    assert result == JSON_EXPECTED


# === Validation Tests ===
def test_invalid_option_type():
    """Test validation of option type input."""
    with pytest.raises(TypeError, match="Input type should be CLValue for CLOption"):
        _ = CLOption("invalid")
