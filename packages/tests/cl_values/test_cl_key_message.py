"""Tests for CL (CasperLabs) message key functionality.

This module contains test cases for the CLKey class when handling message keys,
which represent message topics and entities in the Casper network.
The tests cover two types of message keys:
1. Message Topic keys (message-topic)
2. Message Entity keys (message-entity)

For each type, it tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
- Hash validation
- Index validation (for message entities)
"""

import pytest
from python_condor import CLKey

# === Test Data ===

# Valid hash values for testing
VALID_HASH_1 = "2a" * 32  # 64-character hex string
VALID_HASH_2 = "02" * 32  # 64-character hex string
VALID_INDEX = "f"  # Hex index

# Test data for message topic keys
VALID_KEYS = {
    'topic': (
        f"message-topic-entity-contract-{VALID_HASH_1}-{VALID_HASH_1}"
    ),
    'entity': (
        f"message-entity-contract-{VALID_HASH_1}-{VALID_HASH_2}-{VALID_INDEX}"
    ),
}

# Invalid test data for validation
INVALID_KEYS = {
    # Topic key validation
    'topic_single_hash': "message-topic-entity-contract-xxx",  # Missing second hash
    'topic_hash_format': "message-topic-entity-contract-xxx-xxx",  # Invalid hash format
    # Wrong prefix
    'topic_wrong_prefix': f"msg-topic-entity-contract-{VALID_HASH_1}-{VALID_HASH_1}",
    # Non-hex hash
    'topic_non_hex': f"message-topic-entity-contract-{VALID_HASH_1}-{'g'*63}",

    # Entity key validation
    'entity_single_hash': "message-entity-contract-xxx",  # Missing components
    'entity_two_hashes': "message-entity-contract-xxx-xxx",  # Missing index
    'entity_hash_format': "message-entity-contract-xxx-xxx-1",  # Invalid hash format
    # Invalid index
    'entity_index': f"message-entity-contract-{VALID_HASH_1}-{VALID_HASH_2}-?",
    # Wrong prefix
    'entity_wrong_prefix': f"msg-entity-contract-{VALID_HASH_1}-{VALID_HASH_2}-{VALID_INDEX}",
    # Non-hex index
    'entity_non_hex_index': f"message-entity-contract-{VALID_HASH_1}-{VALID_HASH_2}-g",
}

# === Expected Values ===

# Expected values for message topic
TOPIC_EXPECTED = {
    'serialized': f"13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a00",
    'cl_value': f"4300000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a000b",
    'json': "Key",
}

# Expected values for message entity
ENTITY_EXPECTED = {
    'serialized': f"13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f000000",
    'cl_value': f"4700000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f0000000b",
    'json': "Key",
}

# === Message Topic Tests ===


def test_message_topic_serialization():
    """Test serialization of message topic key."""
    message_key = CLKey(VALID_KEYS['topic'])
    result = message_key.serialize().hex()
    assert result == TOPIC_EXPECTED['serialized']


def test_message_topic_value():
    """Test value retrieval of message topic key."""
    message_key = CLKey(VALID_KEYS['topic'])
    result = message_key.value()
    assert result == VALID_KEYS['topic']


def test_message_topic_cl_value():
    """Test CL value representation of message topic key."""
    message_key = CLKey(VALID_KEYS['topic'])
    result = message_key.cl_value()
    assert result == TOPIC_EXPECTED['cl_value']


def test_message_topic_to_json():
    """Test JSON representation of message topic key."""
    message_key = CLKey(VALID_KEYS['topic'])
    result = message_key.to_json()
    assert result == TOPIC_EXPECTED['json']


def test_invalid_topic_hash_count():
    """Test validation of message topic key requiring two hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a topic hash."):
        _ = CLKey(INVALID_KEYS['topic_single_hash'])


def test_invalid_topic_hash_format():
    """Test validation of message topic key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['topic_hash_format'])


def test_invalid_topic_prefix():
    """Test validation of message topic key prefix."""
    with pytest.raises(ValueError, match="invalid prefix"):
        _ = CLKey(INVALID_KEYS['topic_wrong_prefix'])


def test_invalid_topic_non_hex_hash():
    """Test validation of message topic key non-hex hash."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['topic_non_hex'])


# === Message Entity Tests ===

def test_message_entity_serialization():
    """Test serialization of message entity key."""
    message_key = CLKey(VALID_KEYS['entity'])
    result = message_key.serialize().hex()
    assert result == ENTITY_EXPECTED['serialized']


def test_message_entity_value():
    """Test value retrieval of message entity key."""
    message_key = CLKey(VALID_KEYS['entity'])
    result = message_key.value()
    assert result == VALID_KEYS['entity']


def test_message_entity_cl_value():
    """Test CL value representation of message entity key."""
    message_key = CLKey(VALID_KEYS['entity'])
    result = message_key.cl_value()
    assert result == ENTITY_EXPECTED['cl_value']


def test_message_entity_to_json():
    """Test JSON representation of message entity key."""
    message_key = CLKey(VALID_KEYS['entity'])
    result = message_key.to_json()
    assert result == ENTITY_EXPECTED['json']


def test_invalid_entity_single_hash():
    """Test validation of message entity key requiring three components."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(INVALID_KEYS['entity_single_hash'])


def test_invalid_entity_two_hashes():
    """Test validation of message entity key requiring message index."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(INVALID_KEYS['entity_two_hashes'])


def test_invalid_entity_hash_format():
    """Test validation of message entity key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_KEYS['entity_hash_format'])


def test_invalid_entity_index_format():
    """Test validation of message entity key index format."""
    with pytest.raises(ValueError, match="the index should be an hexadecimal number"):
        _ = CLKey(INVALID_KEYS['entity_index'])


def test_invalid_entity_prefix():
    """Test validation of message entity key prefix."""
    with pytest.raises(ValueError, match="invalid prefix"):
        _ = CLKey(INVALID_KEYS['entity_wrong_prefix'])


def test_invalid_entity_non_hex_index():
    """Test validation of message entity key non-hex index."""
    with pytest.raises(ValueError, match="the index should be an hexadecimal number"):
        _ = CLKey(INVALID_KEYS['entity_non_hex_index'])
