"""Tests for CL (CasperLabs) entry point key functionality.

This module contains test cases for the CLKey class when handling entry point keys,
which represent contract entry points in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
- Version validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid entry point key for testing
VALID_ENTRYPOINT_KEY = (
    "entry-point-v1-entity-contract-"
    "53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-"
    "3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481"
)

# Invalid entry point keys for testing validation
INVALID_LENGTH_KEY = (
    "entry-point-v1-entity-contract-"
    "3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481"
)
INVALID_VERSION_KEY = (
    "entry-point-v2-entity-contract-"
    "53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-"
    "3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481"
)

# === Expected Values ===
EXPECTED = {
    "serialized": "17000253c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481",
    "cl_value": "4300000017000253c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d54383964810b",
    "json": "Key"
}

# === Valid Entry Point Key Tests ===


def test_entrypoint_key_serialization():
    """Test serialization of entry point key."""
    entrypoint_key = CLKey(VALID_ENTRYPOINT_KEY)
    result = entrypoint_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_entrypoint_key_value():
    """Test value retrieval of entry point key."""
    entrypoint_key = CLKey(VALID_ENTRYPOINT_KEY)
    result = entrypoint_key.value()
    assert result == VALID_ENTRYPOINT_KEY


def test_entrypoint_key_cl_value():
    """Test CL value representation of entry point key."""
    entrypoint_key = CLKey(VALID_ENTRYPOINT_KEY)
    result = entrypoint_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_entrypoint_key_to_json():
    """Test JSON representation of entry point key."""
    entrypoint_key = CLKey(VALID_ENTRYPOINT_KEY)
    result = entrypoint_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Entry Point Key Tests ===
def test_invalid_entrypoint_key_length():
    """Test entry point key length validation."""
    error_msg = "Key not valid. It should have vm version, a hash address and a entrypoint hash."
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_LENGTH_KEY)


def test_invalid_entrypoint_key_version():
    """Test entry point key version validation."""
    error_msg = "vm version should be v1"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_VERSION_KEY)
