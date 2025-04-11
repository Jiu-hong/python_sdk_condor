"""Message key module.

This module provides functionality for handling message keys in the Casper network.
Message keys are used to identify specific messages in the network.
"""

from typing import NoReturn

from .entity_addr import EntityAddr
from ...utils import check_clkey_hash_format


# "message-topic-entity-contract-xxx-xxx"
# message-entity-contract-xxx-xxx-f


def check_message_key_format(data: str) -> NoReturn:
    """Check if the message key format is valid.

    The message key should be in one of these formats:
    1. message-topic-entity-<entity_addr>-<topic_hash>
    2. message-entity-<entity_addr>-<topic_hash>-<message_index>

    Args:
        data: The message key string to validate.

    Raises:
        ValueError: If the key format is invalid:
            - Wrong prefix
            - Wrong number of parts
            - Invalid entity address
            - Invalid topic hash
            - Invalid message index (for format 2)
    """
    if not data.startswith("message-topic-entity-") and not data.startswith("message-entity-"):
        raise ValueError(
            "Key not valid. It should start with 'message-topic-entity-' or 'message-entity-'")

    if data.startswith("message-topic-"):
        source = data.removeprefix("message-topic-")
        parts = source.split('-')

        if len(parts) != 4:
            raise ValueError(
                "Key not valid. It should have a hash address and a topic hash.")
    else:
        source = data.removeprefix("message-")
        parts = source.split('-')

        if len(parts) != 5:
            raise ValueError(
                "Key not valid. It should have a hash address, a topic hash, and a message index.")

        try:
            _ = int(parts[4], 16)  # check index format
        except ValueError:
            raise ValueError("the index should be an hexadecimal number")

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
    _ = EntityAddr(hash_addr)  # check entity_addr format
    check_clkey_hash_format(parts[3])


def serialize_message_key(data: str) -> bytes:
    """Serialize a message key to bytes.

    The message key is serialized differently based on its type:
    1. For topic messages:
       - Serialized entity address
       - Topic hash bytes
       - Single byte 0x00
    2. For regular messages:
       - Serialized entity address
       - Topic hash bytes
       - Single byte 0x01
       - 4-byte little-endian message index

    Args:
        data: The message key string to serialize.

    Returns:
        Bytes representation of the message key.

    Raises:
        ValueError: If the message index is empty.
    """
    source = data.removeprefix("message-")

    if source.startswith("topic-"):
        source = source.removeprefix("topic-")
        parts = source.split('-')
        hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
        topic_hash = parts[3]
        return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("00")

    # Regular message format
    parts = source.split('-')
    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
    topic_hash = parts[3]

    if len(parts[4]) == 0:
        raise ValueError("Key not valid. Expected a non-empty message index.")

    index = int(parts[4], 16).to_bytes(4, byteorder='little')
    return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("01") + index
