"""Tests for CL (CasperLabs) option functionality.

This module contains test cases for the CLOption class, which represents optional
values in the Casper network. The tests cover three scenarios:
1. Some value (CLString)
2. None value with type information
3. NoneHolder for type information only

For each scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
"""

from python_condor import CLOption, CLString, NoneHolder

# Test data for CLOption
TEST_STRING = "helloworld"
VALID_SOME_OPTION = CLOption(CLString(TEST_STRING))
VALID_NONE_OPTION = CLOption(None, CLString(NoneHolder()))
VALID_HOLDER_OPTION = CLOption(CLString(NoneHolder()))

# Expected values for assertions
EXPECTED_SOME_SERIALIZED = "010a00000068656c6c6f776f726c64"
EXPECTED_SOME_CL_VALUE = "0f000000010a00000068656c6c6f776f726c640d0a"
EXPECTED_NONE_SERIALIZED = "00"
EXPECTED_NONE_CL_VALUE = "01000000000d0a"
EXPECTED_JSON = {"Option": "String"}

# === Some Value Tests ===


def test_some_option_serialization():
    """Test serialization of Some(CLString) value."""
    result = VALID_SOME_OPTION.serialize().hex()
    assert result == EXPECTED_SOME_SERIALIZED


def test_some_option_value():
    """Test value retrieval of Some(CLString) value."""
    result = VALID_SOME_OPTION.value()
    assert result == TEST_STRING


def test_some_option_cl_value():
    """Test CL value representation of Some(CLString) value."""
    result = VALID_SOME_OPTION.cl_value()
    assert result == EXPECTED_SOME_CL_VALUE


def test_some_option_to_json():
    """Test JSON representation of Some(CLString) value."""
    result = VALID_SOME_OPTION.to_json()
    assert result == EXPECTED_JSON


# === None Value Tests ===

def test_none_option_serialization():
    """Test serialization of None value with type information."""
    result = VALID_NONE_OPTION.serialize().hex()
    assert result == EXPECTED_NONE_SERIALIZED


def test_none_option_value():
    """Test value retrieval of None value with type information."""
    result = VALID_NONE_OPTION.value()
    assert result is None


def test_none_option_cl_value():
    """Test CL value representation of None value with type information."""
    result = VALID_NONE_OPTION.cl_value()
    assert result == EXPECTED_NONE_CL_VALUE


def test_none_option_to_json():
    """Test JSON representation of None value with type information."""
    result = VALID_NONE_OPTION.to_json()
    assert result == EXPECTED_JSON


# === NoneHolder Tests ===

def test_holder_option_to_json():
    """Test JSON representation of NoneHolder value."""
    result = VALID_HOLDER_OPTION.to_json()
    assert result == EXPECTED_JSON
