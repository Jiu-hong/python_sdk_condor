"""
Tests for EntityTarget functionality.

This module contains test cases for the EntityTarget class, which represents
entity targets in CasperLabs transactions. The tests verify:
- Entity target creation with contract hash
- Byte serialization
- JSON serialization
- Input validation for contract hash format
"""

import pytest

from python_condor import EntityTarget


# Test data setup
RUNTIME = "VmCasperV1"
CONTRACT_HASH = "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6"


def create_test_entity_target() -> EntityTarget:
    """
    Create a test entity target with sample data.

    Returns:
        EntityTarget: A configured test target
    """
    return EntityTarget(RUNTIME, CONTRACT_HASH)


# Expected test results
EXPECTED_BYTES = "030000000000000000000100010000000200360000004500000001020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6010000000000000000000100000000"

EXPECTED_JSON = {
    'target': {
        'Stored': {
            'id': {
                'ByHash': CONTRACT_HASH
            },
            'runtime': RUNTIME
        }
    }
}


def test_entity_target_to_bytes():
    """
    Test byte serialization of an entity target.

    Verifies that the target correctly serializes to the expected byte format.
    """
    target = create_test_entity_target()
    result = target.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_entity_target_to_json():
    """
    Test JSON serialization of an entity target.

    Verifies that the target correctly serializes to the expected JSON structure.
    """
    target = create_test_entity_target()
    result = target.to_json()
    assert result == EXPECTED_JSON


def test_entity_target_invalid_hash():
    """
    Test validation of contract hash format.

    Verifies that the target raises a ValueError when given an invalid contract hash.
    """
    with pytest.raises(ValueError, match=r"contract-hash should only contain alphabet and number\(64 length\)"):
        _ = EntityTarget(RUNTIME, "123-0")
