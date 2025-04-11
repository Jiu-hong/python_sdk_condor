"""Byte code key module.

This module provides functionality for handling byte code keys in the Casper network.
Byte code keys are used to identify different types of byte code (WASM v1, v2, or empty).
"""

from typing import NoReturn

from ...constants import Prefix


PREFIX = Prefix()


def check_byte_code_key_format(data: str) -> NoReturn:
    """Check if the byte code key format is valid.

    The byte code key should be in one of these formats:
    1. byte-code-v1-wasm-<hex_string>
    2. byte-code-v2-wasm-<hex_string>
    3. byte-code-empty

    Args:
        data: The byte code key string to validate.

    Raises:
        ValueError: If the key format is invalid:
            - Wrong prefix
            - Invalid version
            - Invalid hex string
    """
    rest_hex = data.removeprefix(PREFIX.BYTE_CODE)
    if rest_hex.startswith(PREFIX.V1_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
    elif rest_hex.startswith(PREFIX.V2_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
    elif rest_hex.startswith(PREFIX.EMPTY):
        bytescode_hex = ""
    else:
        raise ValueError("invalid byte-code-xxx")

    try:
        bytes.fromhex(bytescode_hex)
    except ValueError:
        raise ValueError("bytescode should be hex string")


def serialize_bytes_code_key(data: str) -> bytes:
    """Serialize a byte code key to bytes.

    The byte code key is serialized as:
    1. A single byte indicating the version:
       - 0x00 for empty
       - 0x01 for v1-wasm
       - 0x02 for v2-wasm
    2. The byte code bytes (if not empty)

    Args:
        data: The byte code key string to serialize.

    Returns:
        Bytes representation of the byte code key.
    """
    rest_hex = data.removeprefix(PREFIX.BYTE_CODE)
    if rest_hex.startswith(PREFIX.V1_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
        value = int(1).to_bytes(1, byteorder='little') + \
            bytes.fromhex(bytescode_hex)
    elif rest_hex.startswith(PREFIX.V2_WASM):
        bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
        value = int(2).to_bytes(1, byteorder='little') + \
            bytes.fromhex(bytescode_hex)
    else:
        value = int(0).to_bytes(1, byteorder='little')
    return value
