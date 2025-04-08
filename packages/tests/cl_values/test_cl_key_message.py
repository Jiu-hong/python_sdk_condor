import pytest
from python_condor import CLKey


# ===== CLKey - message_topic =====
clkey_message_topic = CLKey(
    "message-topic-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_message_topic_serialize():
    result = clkey_message_topic.serialize().hex()
    assert result == "13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a00"


def test_clkey_message_topic_string_value():
    result = clkey_message_topic.value()
    assert result == "message-topic-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_message_topic_cl_value():
    result = clkey_message_topic.cl_value()
    assert result == "4300000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a000b"


def test_clkey_message_topic_to_json():
    result = clkey_message_topic.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_message_topic_without_two_hashes():
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address and a topic hash."):
        _ = CLKey(
            "message-topic-entity-contract-xxx")


def test_clkey_message_topic_invalid_hash_value():
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "message-topic-entity-contract-xxx-xxx")


# ===== CLKey - message_entity =====
clkey_message_topic_entity = CLKey(
    "message-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-0202020202020202020202020202020202020202020202020202020202020202-f")


def test_clkey_message_topic_entity_serialize():
    result = clkey_message_topic_entity.serialize().hex()
    assert result == "13022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f000000"


def test_clkey_message_topic_entity_string_value():
    result = clkey_message_topic_entity.value()
    assert result == "message-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-0202020202020202020202020202020202020202020202020202020202020202-f"


def test_clkey_message_topic_entity_cl_value():
    result = clkey_message_topic_entity.cl_value()
    assert result == "4700000013022a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0202020202020202020202020202020202020202020202020202020202020202010f0000000b"


def test_clkey_message_topic_entity_to_json():
    result = clkey_message_topic_entity.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_message_topic_entity_with_one_hashes_no_index():
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(
            "message-entity-contract-xxx")


def test_clkey_message_topic_entity_with_two_hashes_no_index():
    with pytest.raises(ValueError, match="Key not valid. It should have a hash address, a topic hash, and a message index."):
        _ = CLKey(
            "message-entity-contract-xxx-xxx")


def test_clkey_message_topic_entity_with_invalid_hashes():
    with pytest.raises(ValueError, match="hash value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "message-entity-contract-xxx-xxx-1")


def test_clkey_message_topic_entity_with_invalid_index():
    with pytest.raises(ValueError, match="the index should be an hexadecimal number"):
        _ = CLKey(
            "message-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-0202020202020202020202020202020202020202020202020202020202020202-?")
