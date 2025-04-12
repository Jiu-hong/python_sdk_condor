"""Tests for CL (Casper) URef functionality.

This module contains test cases for the CLURef class, which represents unforgeable
references in the Casper network. The tests verify:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation (prefix, length, access rights)
"""

import pytest

from python_condor import CLURef

# Test data
VALID_UREF = "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"
INVALID_PREFIX_UREF = "ref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"
INVALID_LENGTH_UREF = "uref-1234567890-007"
INVALID_ACCESS_RIGHT_UREF = "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-008"

# Expected values
EXPECTED_SERIALIZED = "fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07"
EXPECTED_CL_VALUE = "21000000fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f070c"

# === Valid URef Tests ===


def test_uref_serialization():
    """Test serialization of valid URef."""
    uref = CLURef(VALID_UREF)
    result = uref.serialize().hex()
    assert result == EXPECTED_SERIALIZED


def test_uref_value():
    """Test value retrieval of valid URef."""
    uref = CLURef(VALID_UREF)
    result = uref.value()
    assert result == VALID_UREF


def test_uref_cl_value():
    """Test CL value representation of valid URef."""
    uref = CLURef(VALID_UREF)
    result = uref.cl_value()
    assert result == EXPECTED_CL_VALUE


def test_uref_to_json():
    """Test JSON representation of valid URef."""
    uref = CLURef(VALID_UREF)
    result = uref.to_json()
    assert result == "URef"


# === Invalid URef Tests ===

def test_uref_invalid_prefix():
    """Test validation of URef with incorrect prefix."""
    with pytest.raises(ValueError, match="Input prefix is ref. Expected prefix is 'uref'."):
        _ = CLURef(INVALID_PREFIX_UREF)


def test_uref_invalid_length():
    """Test validation of URef with incorrect length."""
    with pytest.raises(ValueError, match="Input length is 10. Expected length is 64."):
        _ = CLURef(INVALID_LENGTH_UREF)


def test_uref_invalid_access_right():
    """Test validation of URef with incorrect access right."""
    with pytest.raises(ValueError, match="Input access right is 008. Expected access right should be between 000-007."):
        _ = CLURef(INVALID_ACCESS_RIGHT_UREF)
