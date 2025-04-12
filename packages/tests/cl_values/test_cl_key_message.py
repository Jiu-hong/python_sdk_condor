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

# Test data for message topic keys
VALID_MESSAGE_TOPIC_KEY = (
    "message-topic-entity-contract-"
    "2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-"
    "2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"
)
INVALID_TOPIC_SINGLE_HASH = "message-topic-entity-contract-xxx"
INVALID_TOPIC_HASH_FORMAT = "message-topic-entity-contract-xxx-xxx"

# Test data for message entity keys
VALID_MESSAGE_ENTITY_KEY = (
    "message-entity-contract-"
    "2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-"
    "0202020202020202020202020202020202020202020202020202020202020202-f"
)
INVALID_ENTITY_SINGLE_HASH = "message-entity-contract-xxx"
INVALID_ENTITY_TWO_HASHES = "message-entity-contract-xxx-xxx"
INVALID_ENTITY_HASH_FORMAT = "message-entity-contract-xxx-xxx-1"
INVALID_ENTITY_INDEX = (
    "message-entity-contract-"
    "2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-"
    "0202020202020202020202020202020202020202020202020202020202020202-?"
)

# === Message Topic Tests ===


def test_message_topic_serialization():
    """Test serialization of message topic key."""
    message_key = CLKey(VALID_MESSAGE_TOPIC_KEY)
    result = message_key.serialize().hex()
    assert result == "13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a00"


def test_message_topic_value():
    """Test value retrieval of message topic key."""
    message_key = CLKey(VALID_MESSAGE_TOPIC_KEY)
    result = message_key.value()
    assert result == VALID_MESSAGE_TOPIC_KEY


def test_message_topic_cl_value():
    """Test CL value representation of message topic key."""
    message_key = CLKey(VALID_MESSAGE_TOPIC_KEY)
    result = message_key.cl_value()
    assert result == "4300000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a000b"


def test_message_topic_to_json():
    """Test JSON representation of message topic key."""
    message_key = CLKey(VALID_MESSAGE_TOPIC_KEY)
    result = message_key.to_json()
    assert result == "Key"


def test_invalid_topic_hash_count():
    """Test validation of message topic key requiring two hashes."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a topic hash."):
        _ = CLKey(INVALID_TOPIC_SINGLE_HASH)


def test_invalid_topic_hash_format():
    """Test validation of message topic key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_TOPIC_HASH_FORMAT)


# === Message Entity Tests ===

def test_message_entity_serialization():
    """Test serialization of message entity key."""
    message_key = CLKey(VALID_MESSAGE_ENTITY_KEY)
    result = message_key.serialize().hex()
    assert result == "13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f000000"


def test_message_entity_value():
    """Test value retrieval of message entity key."""
    message_key = CLKey(VALID_MESSAGE_ENTITY_KEY)
    result = message_key.value()
    assert result == VALID_MESSAGE_ENTITY_KEY


def test_message_entity_cl_value():
    """Test CL value representation of message entity key."""
    message_key = CLKey(VALID_MESSAGE_ENTITY_KEY)
    result = message_key.cl_value()
    assert result == "4700000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f0000000b"


def test_message_entity_to_json():
    """Test JSON representation of message entity key."""
    message_key = CLKey(VALID_MESSAGE_ENTITY_KEY)
    result = message_key.to_json()
    assert result == "Key"


def test_invalid_entity_single_hash():
    """Test validation of message entity key requiring three components."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(INVALID_ENTITY_SINGLE_HASH)


def test_invalid_entity_two_hashes():
    """Test validation of message entity key requiring message index."""
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(INVALID_ENTITY_TWO_HASHES)


def test_invalid_entity_hash_format():
    """Test validation of message entity key hash format."""
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(INVALID_ENTITY_HASH_FORMAT)


def test_invalid_entity_index_format():
    """Test validation of message entity key index format."""
    with pytest.raises(ValueError, match="the index should be an hexadecimal number"):
        _ = CLKey(INVALID_ENTITY_INDEX)
