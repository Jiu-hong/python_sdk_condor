"""Tests for CL (CasperLabs) named key functionality.

This module contains test cases for the CLKey class when handling named keys,
which represent named references to accounts and contracts in the Casper network.
The tests cover two types of named keys:
1. Account named keys (entity-account)
2. Contract named keys (entity-contract)

For each type, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
- Hash validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===

# Valid hash values for testing
VALID_HASH_1 = "928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3c"
VALID_HASH_2 = "dde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"
VALID_HASH_3 = "2a" * 32  # Contract hash 1
VALID_HASH_4 = "2b" * 32  # Contract hash 2

# Test data for valid named keys
VALID_KEYS = {
    'account': (
        f"named-key-entity-account-{VALID_HASH_1}-{VALID_HASH_2}"
    ),
    'contract': (
        f"named-key-entity-contract-{VALID_HASH_3}-{VALID_HASH_4}"
    ),
}

# Invalid test data for validation
INVALID_KEYS = {
    # Format validation
    'invalid_hash': "named-key-entity-account-xx-xx",  # Invalid hash format
    'single_hash': "named-key-entity-account-xx",  # Missing second hash
    'triple_hash': "named-key-entity-account-xx-xx-xx",  # Too many hashes
    'invalid_entity': "named-key-something-account-xx-xx",  # Invalid entity type
    # Wrong prefix
    'wrong_prefix': f"key-entity-account-{VALID_HASH_1}-{VALID_HASH_2}",
    # Non-hex hash
    'non_hex_hash': f"named-key-entity-account-{VALID_HASH_1}-{'g'*63}",
    # Hash too short
    'short_hash': f"named-key-entity-account-{VALID_HASH_1[:62]}-{VALID_HASH_2}",
}

# === Expected Values ===

# Expected values for account named key
ACCOUNT_EXPECTED = {
    'serialized': f"1401{VALID_HASH_1}{VALID_HASH_2}",
    'cl_value': f"420000001401{VALID_HASH_1}{VALID_HASH_2}0b",
    'json': "Key",
}

# Expected values for contract named key
CONTRACT_EXPECTED = {
    'serialized': f"1402{VALID_HASH_3}{VALID_HASH_4}",
    'cl_value': f"420000001402{VALID_HASH_3}{VALID_HASH_4}0b",
    'json': "Key",
}

# === Account Named Key Tests ===


def test_account_named_key_serialization():
    """Test serialization of account named key."""
    named_key = CLKey(VALID_KEYS['account'])
    result = named_key.serialize().hex()
    assert result == ACCOUNT_EXPECTED['serialized']


def test_account_named_key_value():
    """Test value retrieval of account named key."""
    named_key = CLKey(VALID_KEYS['account'])
    result = named_key.value()
    assert result == VALID_KEYS['account']


def test_account_named_key_cl_value():
    """Test CL value representation of account named key."""
    named_key = CLKey(VALID_KEYS['account'])
    result = named_key.cl_value()
    assert result == ACCOUNT_EXPECTED['cl_value']


def test_account_named_key_to_json():
    """Test JSON representation of account named key."""
    named_key = CLKey(VALID_KEYS['account'])
    result = named_key.to_json()
    assert result == ACCOUNT_EXPECTED['json']


def test_invalid_hash_format():
    """Test validation of named key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['invalid_hash'])


def test_invalid_single_hash():
    """Test validation of named key requiring two hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(INVALID_KEYS['single_hash'])


def test_invalid_triple_hash():
    """Test validation of named key having too many hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(INVALID_KEYS['triple_hash'])


def test_invalid_entity_type():
    """Test validation of named key entity type."""
    with pytest.raises(ValueError, match="data should start with 'entity-"):
        _ = CLKey(INVALID_KEYS['invalid_entity'])


def test_invalid_prefix():
    """Test validation of named key prefix."""
    with pytest.raises(ValueError, match="invalid prefix"):
        _ = CLKey(INVALID_KEYS['wrong_prefix'])


def test_invalid_non_hex_hash():
    """Test validation of named key non-hex hash."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['non_hex_hash'])


def test_invalid_short_hash():
    """Test validation of named key hash length."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['short_hash'])


# === Contract Named Key Tests ===

def test_contract_named_key_serialization():
    """Test serialization of contract named key."""
    named_key = CLKey(VALID_KEYS['contract'])
    result = named_key.serialize().hex()
    assert result == CONTRACT_EXPECTED['serialized']


def test_contract_named_key_value():
    """Test value retrieval of contract named key."""
    named_key = CLKey(VALID_KEYS['contract'])
    result = named_key.value()
    assert result == VALID_KEYS['contract']


def test_contract_named_key_cl_value():
    """Test CL value representation of contract named key."""
    named_key = CLKey(VALID_KEYS['contract'])
    result = named_key.cl_value()
    assert result == CONTRACT_EXPECTED['cl_value']


def test_contract_named_key_to_json():
    """Test JSON representation of contract named key."""
    named_key = CLKey(VALID_KEYS['contract'])
    result = named_key.to_json()
    assert result == CONTRACT_EXPECTED['json']
