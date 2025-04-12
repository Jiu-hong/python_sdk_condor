"""Tests for CL (Casper) string functionality.

This module contains test cases for the CLString class, which represents string
values in the Casper network. The tests cover three scenarios:
1. Regular string values
2. Empty string values
3. NoneHolder for type information

For each scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Type validation
"""

import pytest
from python_condor import NoneHolder, CLString

# === Test Data ===

# Test data for CLString
TEST_DATA = {
    'regular': "helloworld",
    'empty': "",
    'unicode': "Hello 世界",  # Unicode string
    'special': "!@#$%^&*()",  # Special characters
}

# Test instances
TEST_INSTANCES = {
    'regular': CLString("helloworld"),
    'empty': CLString(""),
    'unicode': CLString("Hello 世界"),
    'special': CLString("!@#$%^&*()"),
    'holder': CLString(NoneHolder()),
}

# === Expected Values ===

# Expected values for regular string
REGULAR_EXPECTED = {
    'serialized': "0a00000068656c6c6f776f726c64",
    'cl_value': "0e0000000a00000068656c6c6f776f726c640a",
    'value': "helloworld",
    'json': "String",
}

# Expected values for empty string
EMPTY_EXPECTED = {
    'serialized': "00000000",
    'cl_value': "04000000000000000a",
    'value': "",
    'json': "String",
}

# === Regular String Tests ===


def test_regular_string_serialization():
    """Test serialization of regular string value."""
    result = TEST_INSTANCES['regular'].serialize().hex()
    assert result == REGULAR_EXPECTED['serialized']


def test_regular_string_value():
    """Test value retrieval of regular string value."""
    result = TEST_INSTANCES['regular'].value()
    assert result == REGULAR_EXPECTED['value']


def test_regular_string_cl_value():
    """Test CL value representation of regular string value."""
    result = TEST_INSTANCES['regular'].cl_value()
    assert result == REGULAR_EXPECTED['cl_value']


def test_regular_string_to_json():
    """Test JSON representation of regular string value."""
    result = TEST_INSTANCES['regular'].to_json()
    assert result == REGULAR_EXPECTED['json']


# === Empty String Tests ===

def test_empty_string_serialization():
    """Test serialization of empty string value."""
    result = TEST_INSTANCES['empty'].serialize().hex()
    assert result == EMPTY_EXPECTED['serialized']


def test_empty_string_value():
    """Test value retrieval of empty string value."""
    result = TEST_INSTANCES['empty'].value()
    assert result == EMPTY_EXPECTED['value']


def test_empty_string_cl_value():
    """Test CL value representation of empty string value."""
    result = TEST_INSTANCES['empty'].cl_value()
    assert result == EMPTY_EXPECTED['cl_value']


def test_empty_string_to_json():
    """Test JSON representation of empty string value."""
    result = TEST_INSTANCES['empty'].to_json()
    assert result == EMPTY_EXPECTED['json']


# === Unicode String Tests ===

def test_unicode_string_value():
    """Test value retrieval of Unicode string value."""
    result = TEST_INSTANCES['unicode'].value()
    assert result == TEST_DATA['unicode']


def test_special_chars_value():
    """Test value retrieval of string with special characters."""
    result = TEST_INSTANCES['special'].value()
    assert result == TEST_DATA['special']


# === NoneHolder Tests ===

def test_holder_to_json():
    """Test JSON representation of NoneHolder value."""
    result = TEST_INSTANCES['holder'].to_json()
    assert result == REGULAR_EXPECTED['json']


# === Validation Tests ===

def test_invalid_string_type():
    """Test validation of string type input."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'int'> for CLString"):
        _ = CLString(123)


def test_invalid_bytes_type():
    """Test validation of bytes type input."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'bytes'> for CLString"):
        _ = CLString(b"hello")


def test_invalid_none_type():
    """Test validation of None type input."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'NoneType'> for CLString"):
        _ = CLString(None)
