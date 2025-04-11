"""Named key module.

This module provides functionality for handling named keys in the Casper network.
A named key is used to identify a specific named key in a contract.
"""

from typing import NoReturn

from .entity_addr import EntityAddr
from ...constants import Prefix
from ...utils import check_clkey_hash_format


PREFIX = Prefix()


def check_named_key_format(data: str) -> NoReturn:
    """Check if the named key format is valid.

    The named key should be in the format:
    named-key-<entity_addr>-<namedkey_hash>

    Args:
        data: The named key string to validate.

    Raises:
        ValueError: If the key format is invalid:
            - Wrong number of parts
            - Invalid entity address
            - Invalid namedkey hash
    """
    source = data.removeprefix(PREFIX.NAMED_KEY)
    parts = source.split('-')
    if len(parts) != 4:
        raise ValueError(
            "Key not valid. It should have a hash address and a namedkey hash.")

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
    _ = EntityAddr(hash_addr)  # check entity_addr format
    check_clkey_hash_format(parts[3])  # check namedkey hash


def serialize_named_key(data: str) -> bytes:
    """Serialize a named key to bytes.

    The named key is serialized as:
    1. The serialized entity address
    2. The namedkey hash bytes

    Args:
        data: The named key string to serialize.

    Returns:
        Bytes representation of the named key.
    """
    source = data.removeprefix(PREFIX.NAMED_KEY)
    parts = source.split('-')

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
    named_key_hash = parts[3]

    return EntityAddr(hash_addr).serialize() + bytes.fromhex(named_key_hash)
