"""Era key module.

This module provides functionality for handling era keys in the Casper network.
Era keys are used to identify specific eras in the network's history.
"""

from typing import NoReturn

from ...constants import Prefix


PREFIX = Prefix()


def check_era_key_format(data: str) -> NoReturn:
    """Check if the era key format is valid.

    The era key should be in the format:
    era-<decimal_integer>

    Args:
        data: The era key string to validate.

    Raises:
        ValueError: If the key format is invalid:
            - Not a decimal integer
    """
    try:
        int(data.removeprefix(PREFIX.ERA))
    except ValueError:
        raise ValueError("era value should be decimal int")


def serialize_era_key(data: str) -> bytes:
    """Serialize an era key to bytes.

    The era key is serialized as:
    - 8-byte little-endian integer

    Args:
        data: The era key string to serialize.

    Returns:
        Bytes representation of the era key.
    """
    era_int = int(data.removeprefix(PREFIX.ERA))
    return era_int.to_bytes(8, byteorder='little')
