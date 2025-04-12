"""
Tests for EntityAliasTarget functionality.

This module contains test cases for the EntityAliasTarget class, which represents
entity alias targets in CasperLabs transactions. The tests verify:
- Entity alias target creation
- Byte serialization
- JSON serialization
"""

from python_condor import EntityAliasTarget


# Test data setup
RUNTIME = "VmCasperV1"
ALIAS_NAME = "apple_contract"


def create_test_entity_alias_target() -> EntityAliasTarget:
    """
    Create a test entity alias target with sample data.

    Returns:
        EntityAliasTarget: A configured test target
    """
    return EntityAliasTarget(RUNTIME, ALIAS_NAME)


# Expected test results
EXPECTED_BYTES = (
    "0300000000000000000001000100000002002800000037000000010200000000000000000001000100000013000000010e0000006170706c655f636f6e7472616374010000000000000000000100000000"
)

EXPECTED_JSON = {
    'target': {
        'Stored': {
            'id': {'ByName': ALIAS_NAME},
            'runtime': RUNTIME
        }
    }
}


def test_entity_alias_target_to_bytes():
    """Test byte serialization of entity alias target."""
    target = create_test_entity_alias_target()
    result = target.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_entity_alias_target_to_json():
    """Test JSON serialization of entity alias target."""
    target = create_test_entity_alias_target()
    result = target.to_json()
    assert result == EXPECTED_JSON
