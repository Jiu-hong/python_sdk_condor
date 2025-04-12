"""CL public key module.

This module provides the CLPublicKey type for handling public keys in the Casper network.
It supports both ED25519 and SECP256K1 public key formats.
"""

import re
from hashlib import blake2b
from typing import Dict

from .cl_basetype import CLValue
from ..constants import TAG


# Algorithm type mapping
ALGO_MAP: Dict[bytes, str] = {
    b'\x01': "ed25519",
    b'\x02': "secp256k1"
}


class CLPublicKey(CLValue):
    """Class representing a CL public key.

    This class handles public keys in the Casper network, supporting both
    ED25519 and SECP256K1 formats. It provides methods for serialization
    and account hash generation.
    """

    tag = TAG.CLPublicKey.value

    def __init__(self, data: str) -> None:
        """Initialize a CL public key.

        Args:
            data: The public key in hexadecimal string format.
                For ED25519: 01 followed by 64 hex characters
                For SECP256K1: 02 followed by 66 hex characters

        Raises:
            ValueError: If the public key format is invalid.
        """
        regx = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(data)
        if not isinstance(result, re.Match):
            raise ValueError(
                "Public key should be 01xxx(64 length) or 02xxx(66 length)")
        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize this public key to bytes.

        Returns:
            Bytes representation of this public key.
        """
        return bytes.fromhex(self.data)

    def get_account_hash(self) -> str:
        """Generate the account hash for this public key.

        The account hash is generated by:
        1. Converting the public key to bytes
        2. Prepend the algorithm name
        3. Add a null byte separator
        4. Hash using BLAKE2b

        Returns:
            Hexadecimal string representation of the account hash.
        """
        public_key_bytes = bytes.fromhex(self.data)

        as_bytes = (
            bytes(ALGO_MAP[public_key_bytes[0:1]], "utf-8") +
            bytearray(1) +
            public_key_bytes[1:]
        )

        h = blake2b(digest_size=32)
        h.update(as_bytes)
        return h.hexdigest()
