"""String serialization utilities.

This module provides functions for serializing strings into bytes format
for use in the Casper network.
"""


def serialize_string(data: str) -> bytes:
    """Serialize a string into bytes format.

    This function converts a string into bytes by encoding it as UTF-8 and
    prefixing it with its length as a 4-byte little-endian integer.

    Args:
        data: The string to serialize.

    Returns:
        The serialized string as bytes, prefixed with its length.
    """
    content = bytearray(data, encoding="utf-8")
    bytes_len = int(len(content)).to_bytes(4, byteorder='little')
    return bytes_len + content
