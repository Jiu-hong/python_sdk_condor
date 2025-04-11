"""Block global key module.

This module provides functionality for handling block global keys in the Casper network.
Block global keys are used to identify specific block-related information.
"""

from typing import NoReturn, Tuple


# Block key constants
BLOCK_KEY: Tuple[str, str] = (
    "block-time-00000000000000000000000000000000000000000000000000000000000000",
    "block-message-count-00000000000000000000000000000000000000000000000000000000000000"
)

BLOCK_MESSAGE_COUNT: str = "block-message-count-"


def check_block_global_key_format(data: str) -> NoReturn:
    """Check if the block global key format is valid.

    The block global key should be one of:
    - block-time-00000000000000000000000000000000000000000000000000000000000000
    - block-message-count-00000000000000000000000000000000000000000000000000000000000000

    Args:
        data: The block global key string to validate.

    Raises:
        ValueError: If the key format is invalid.
    """
    if data not in BLOCK_KEY:
        raise ValueError(
            "Key not valid. It should be 'block-time-00000000000000000000000000000000000000000000000000000000000000' "
            "or 'block-message-count-00000000000000000000000000000000000000000000000000000000000000'"
        )


def serialize_block_global_key(data: str) -> bytes:
    """Serialize a block global key to bytes.

    The block global key is serialized as:
    1. A single byte indicating the type (0x00 for time, 0x01 for message count)
    2. The remaining bytes from the key

    Args:
        data: The block global key string to serialize.

    Returns:
        Bytes representation of the block global key.
    """
    if data.startswith(BLOCK_MESSAGE_COUNT):
        return bytes.fromhex("01") + bytes.fromhex(data.removeprefix("block-message-count-"))
    return bytes.fromhex("00") + bytes.fromhex(data.removeprefix("block-time-"))
