"""Tests for CL (CasperLabs) map functionality.

This module contains test cases for the CLMap class, which represents key-value
mappings in the Casper network. The tests verify:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Type validation
- Key-value pair consistency
"""

import pytest

from python_condor import (
    CLList,
    CLMap,
    CLOption,
    CLString,
    CLU32,
    CLU8,
)

# Test data for CLMap
MAP_DATA = {
    CLU8(3): CLOption(CLString("Jim")),
    CLU8(2): CLOption(CLString("Jack")),
    CLU8(4): CLOption(CLString("Jane")),
    CLU8(1): CLOption(CLString("Jill")),
}
VALID_MAP = CLMap(MAP_DATA)

# Expected values for assertions
EXPECTED_SERIALIZED = "040000000101040000004a696c6c0201040000004a61636b0301030000004a696d0401040000004a616e65"
EXPECTED_CL_VALUE = "2b000000040000000101040000004a696c6c0201040000004a61636b0301030000004a696d0401040000004a616e6511030d0a"
EXPECTED_VALUE = [
    {"key": 3, "value": "Jim"},
    {"key": 2, "value": "Jack"},
    {"key": 4, "value": "Jane"},
    {"key": 1, "value": "Jill"},
]
EXPECTED_JSON = {
    "Map": {
        "key": "U8",
        "value": {
            "Option": "String"
        }
    }
}


def test_map_serialization():
    """Test serialization of map value."""
    result = VALID_MAP.serialize().hex()
    assert result == EXPECTED_SERIALIZED


def test_map_value():
    """Test value retrieval of map value."""
    result = VALID_MAP.value()
    assert result == EXPECTED_VALUE


def test_map_cl_value():
    """Test CL value representation of map value."""
    result = VALID_MAP.cl_value()
    assert result == EXPECTED_CL_VALUE


def test_map_to_json():
    """Test JSON representation of map value."""
    result = VALID_MAP.to_json()
    assert result == EXPECTED_JSON


def test_invalid_list_type():
    """Test validation of list type input."""
    with pytest.raises(TypeError, match="Invalid type of input: <class 'python_condor.cl_values.cl_string.CLString'> for CLList. Allowed value is <class 'list'>"):
        _ = CLList(CLString("helloworld"))


def test_inconsistent_list_elements():
    """Test validation of list element type consistency."""
    with pytest.raises(TypeError, match="types aren't consistent in the elements"):
        _ = CLList([CLString("helloworld"), CLU32(123)])
