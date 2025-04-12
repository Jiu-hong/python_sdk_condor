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
    CLMap,
    CLOption,
    CLString,
    CLU32,
    CLU8, NoneHolder
)

# Test data for CLMap

MAP_DATA = {
    CLU8(3): CLOption(CLString("Jim")),
    CLU8(2): CLOption(CLString("Jack")),
    CLU8(4): CLOption(CLString("Jane")),
    CLU8(1): CLOption(CLString("Jill")),
}


VALID_MAP = CLMap(MAP_DATA)
EMPTY_MAP = CLMap({}, CLOption(None, CLU32(NoneHolder())))

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

# Expected values for regular map
REGULAR_EXPECTED = {
    'serialized': EXPECTED_SERIALIZED,
    'cl_value': EXPECTED_CL_VALUE,
    'value': EXPECTED_VALUE,
    'json': EXPECTED_JSON,
}

# Expected values for empty map
EMPTY_EXPECTED = {
    'serialized': "00000000",
    'cl_value': "0400000000000000110d04",
    'value': [],
    'json': {'Map': {'Option': 'U32'}},
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


# === Empty map Tests ===

def test_empty_map_serialization():
    """Test serialization of empty map value."""
    result = EMPTY_MAP.serialize().hex()
    assert result == EMPTY_EXPECTED['serialized']


def test_empty_map_value():
    """Test value retrieval of empty map value."""
    result = EMPTY_MAP.value()
    assert result == EMPTY_EXPECTED['value']


def test_empty_map_cl_value():
    """Test CL value representation of empty map value."""
    result = EMPTY_MAP.cl_value()
    assert result == EMPTY_EXPECTED['cl_value']


def test_empty_map_to_json():
    """Test JSON representation of empty map value."""
    result = EMPTY_MAP.to_json()
    assert result == EMPTY_EXPECTED['json']

#


def test_invalid_map_type():
    """Test validation of map type input."""
    with pytest.raises(TypeError, match="inner type should be map"):
        _ = CLMap(CLString("helloworld"))


def test_inconsistent_map_key_types():
    """Test validation of map key type consistency."""
    with pytest.raises(TypeError, match="key types aren't consistent in the elements"):
        _ = CLMap({
            CLU32(1): CLOption(CLString("hello")),
            CLU8(2): CLOption(CLString("123"))
        })


def test_inconsistent_map_value_types():
    """Test validation of map value type consistency."""
    with pytest.raises(TypeError, match="value types aren't consistent in the elements"):
        _ = CLMap({
            CLU8(1): CLOption(CLString("hello")),
            CLU8(2): CLOption(CLU32(123))
        })


def test_non_clvalue_map_key_value_types():
    """Test validation of map value type clvalue."""
    with pytest.raises(TypeError, match="The inner key and value should be CLValue"):
        _ = CLMap({
            CLU8(1): None,
            CLU8(2): CLOption(CLU32(123))
        })
