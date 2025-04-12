"""Tests for CL (CasperLabs) list functionality.

This module contains test cases for the CLList class, which represents lists of
CL values in the Casper network. The tests cover four scenarios:
1. Regular list with consistent types (Option<String>)
2. Empty list
3. List with single element
4. Invalid list inputs

For each valid scenario, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Type validation
"""

import pytest
from python_condor import (
    CLBool,
    CLList,
    CLOption,
    CLString,
    CLU32,
    NoneHolder,
)

# === Test Data ===

# Test data for CLList
TEST_DATA = {
    'strings': ["hello", "world"],
    'numbers': [1, 2, 3],
    'single': ["test"],
}

# Test instances
TEST_INSTANCES = {
    'regular': CLList([
        CLOption(CLString("hello")),
        CLOption(CLString("world")),
    ]),
    'empty': CLList([], CLOption(None, CLString(NoneHolder()))),
    'single': CLList([CLOption(CLString("test"))]),
    'numbers': CLList([CLU32(1), CLU32(2), CLU32(3)]),
}

# === Expected Values ===

# Expected values for regular list
REGULAR_EXPECTED = {
    'serialized': "02000000010500000068656c6c6f0105000000776f726c64",
    'cl_value': "1800000002000000010500000068656c6c6f0105000000776f726c640e0d0a",
    'value': ['hello', 'world'],
    'json': {'List': {'Option': 'String'}},
}

# Expected values for empty list
EMPTY_EXPECTED = {
    'serialized': "00000000",
    'cl_value': "04000000000000000e0d0a",
    'value': [],
    'json': {'List': {'Option': 'String'}},
}

# Expected values for single element list
SINGLE_EXPECTED = {
    'serialized': "01000000010400000074657374",
    'cl_value': "0d000000010000000104000000746573740e0d0a",
    'value': ['test'],
    'json': {'List': {'Option': 'String'}},
}

# === Regular List Tests ===


def test_regular_list_serialization():
    """Test serialization of regular list value."""
    result = TEST_INSTANCES['regular'].serialize().hex()
    assert result == REGULAR_EXPECTED['serialized']


def test_regular_list_value():
    """Test value retrieval of regular list value."""
    result = TEST_INSTANCES['regular'].value()
    assert result == REGULAR_EXPECTED['value']


def test_regular_list_cl_value():
    """Test CL value representation of regular list value."""
    result = TEST_INSTANCES['regular'].cl_value()
    assert result == REGULAR_EXPECTED['cl_value']


def test_regular_list_to_json():
    """Test JSON representation of regular list value."""
    result = TEST_INSTANCES['regular'].to_json()
    assert result == REGULAR_EXPECTED['json']


# === Empty List Tests ===

def test_empty_list_serialization():
    """Test serialization of empty list value."""
    result = TEST_INSTANCES['empty'].serialize().hex()
    assert result == EMPTY_EXPECTED['serialized']


def test_empty_list_value():
    """Test value retrieval of empty list value."""
    result = TEST_INSTANCES['empty'].value()
    assert result == EMPTY_EXPECTED['value']


def test_empty_list_cl_value():
    """Test CL value representation of empty list value."""
    result = TEST_INSTANCES['empty'].cl_value()
    assert result == EMPTY_EXPECTED['cl_value']


def test_empty_list_to_json():
    """Test JSON representation of empty list value."""
    result = TEST_INSTANCES['empty'].to_json()
    assert result == EMPTY_EXPECTED['json']


# === Single Element List Tests ===

def test_single_element_list_serialization():
    """Test serialization of single element list value."""
    result = TEST_INSTANCES['single'].serialize().hex()
    assert result == SINGLE_EXPECTED['serialized']


def test_single_element_list_value():
    """Test value retrieval of single element list value."""
    result = TEST_INSTANCES['single'].value()
    assert result == SINGLE_EXPECTED['value']


def test_single_element_list_cl_value():
    """Test CL value representation of single element list value."""
    result = TEST_INSTANCES['single'].cl_value()
    assert result == SINGLE_EXPECTED['cl_value']


def test_single_element_list_to_json():
    """Test JSON representation of single element list value."""
    result = TEST_INSTANCES['single'].to_json()
    assert result == SINGLE_EXPECTED['json']


# === Validation Tests ===

def test_invalid_list_type():
    """Test validation of list type input."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'python_condor.cl_values.cl_string.CLString'> for CLList. Allowed value is <class 'list'>"):
        _ = CLList(CLString("helloworld"))


def test_inconsistent_list_elements():
    """Test validation of list element type consistency."""
    with pytest.raises(TypeError, match="types aren't consistent in the elements"):
        _ = CLList([CLString("helloworld"), CLU32(123)])


def test_invalid_list_element_type():
    """Test validation of list element types."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLList(["not_a_cl_value", "another_string"])


def test_mixed_invalid_types():
    """Test validation of mixed invalid types in list."""
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLList([CLString("test"), 123, True])
