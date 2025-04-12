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

# Test data for account named keys
VALID_ACCOUNT_NAMED_KEY = (
    "named-key-entity-account-"
    "928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3c-"
    "dde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"
)
INVALID_HASH_KEY = "named-key-entity-account-xx-xx"
SINGLE_HASH_KEY = "named-key-entity-account-xx"
TRIPLE_HASH_KEY = "named-key-entity-account-xx-xx-xx"
INVALID_ENTITY_KEY = "named-key-something-account-xx-xx"

# Test data for contract named keys
VALID_CONTRACT_NAMED_KEY = (
    "named-key-entity-contract-"
    "2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-"
    "2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b"
)

# === Account Named Key Tests ===


def test_account_named_key_serialization():
    """Test serialization of account named key."""
    named_key = CLKey(VALID_ACCOUNT_NAMED_KEY)
    result = named_key.serialize().hex()
    assert result == "1401928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3cdde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"


def test_account_named_key_value():
    """Test value retrieval of account named key."""
    named_key = CLKey(VALID_ACCOUNT_NAMED_KEY)
    result = named_key.value()
    assert result == VALID_ACCOUNT_NAMED_KEY


def test_account_named_key_cl_value():
    """Test CL value representation of account named key."""
    named_key = CLKey(VALID_ACCOUNT_NAMED_KEY)
    result = named_key.cl_value()
    assert result == "420000001401928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3cdde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec70b"


def test_account_named_key_to_json():
    """Test JSON representation of account named key."""
    named_key = CLKey(VALID_ACCOUNT_NAMED_KEY)
    result = named_key.to_json()
    assert result == "Key"


def test_invalid_hash_format():
    """Test validation of named key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_HASH_KEY)


def test_invalid_single_hash():
    """Test validation of named key requiring two hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(SINGLE_HASH_KEY)


def test_invalid_triple_hash():
    """Test validation of named key having too many hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a namedkey hash."):
        _ = CLKey(TRIPLE_HASH_KEY)


def test_invalid_entity_type():
    """Test validation of named key entity type."""
    with pytest.raises(ValueError, match="data should start with 'entity-"):
        _ = CLKey(INVALID_ENTITY_KEY)


# === Contract Named Key Tests ===

def test_contract_named_key_serialization():
    """Test serialization of contract named key."""
    named_key = CLKey(VALID_CONTRACT_NAMED_KEY)
    result = named_key.serialize().hex()
    assert result == "14022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b"


def test_contract_named_key_value():
    """Test value retrieval of contract named key."""
    named_key = CLKey(VALID_CONTRACT_NAMED_KEY)
    result = named_key.value()
    assert result == VALID_CONTRACT_NAMED_KEY


def test_contract_named_key_cl_value():
    """Test CL value representation of contract named key."""
    named_key = CLKey(VALID_CONTRACT_NAMED_KEY)
    result = named_key.cl_value()
    assert result == "4200000014022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b0b"


def test_contract_named_key_to_json():
    """Test JSON representation of contract named key."""
    named_key = CLKey(VALID_CONTRACT_NAMED_KEY)
    result = named_key.to_json()
    assert result == "Key"
