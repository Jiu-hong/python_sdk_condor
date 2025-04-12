"""Tests for CL (CasperLabs) system entity registry key functionality.

This module contains test cases for the CLKey class when handling system entity registry keys,
which represent system entity registry hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid system entity registry key for testing
VALID_SYSTEM_ENTITY_REGISTRY_KEY = "system-entity-registry-0000000000000000000000000000000000000000000000000000000000000000"

# Invalid system entity registry key for testing validation
INVALID_SYSTEM_ENTITY_REGISTRY_KEY = "system-entity-registry-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "0a0000000000000000000000000000000000000000000000000000000000000000",
    "cl_value": "210000000a00000000000000000000000000000000000000000000000000000000000000000b",
    "json": "Key"
}

# === Valid System Entity Registry Key Tests ===


def test_system_entity_registry_key_serialization():
    """Test serialization of system entity registry key."""
    system_entity_registry_key = CLKey(VALID_SYSTEM_ENTITY_REGISTRY_KEY)
    result = system_entity_registry_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_system_entity_registry_key_value():
    """Test value retrieval of system entity registry key."""
    system_entity_registry_key = CLKey(VALID_SYSTEM_ENTITY_REGISTRY_KEY)
    result = system_entity_registry_key.value()
    assert result == VALID_SYSTEM_ENTITY_REGISTRY_KEY


def test_system_entity_registry_key_cl_value():
    """Test CL value representation of system entity registry key."""
    system_entity_registry_key = CLKey(VALID_SYSTEM_ENTITY_REGISTRY_KEY)
    result = system_entity_registry_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_system_entity_registry_key_to_json():
    """Test JSON representation of system entity registry key."""
    system_entity_registry_key = CLKey(VALID_SYSTEM_ENTITY_REGISTRY_KEY)
    result = system_entity_registry_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid System Entity Registry Key Tests ===
def test_invalid_system_entity_registry_key_format():
    """Test system entity registry key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_SYSTEM_ENTITY_REGISTRY_KEY)
