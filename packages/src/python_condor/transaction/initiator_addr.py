"""
Initiator Address module for handling Casper transaction initiators.

This module provides functionality for managing transaction initiator addresses.
Initiator addresses are used for:
- Identifying the sender of a transaction
- Managing public key-based authentication
- Supporting account hash-based addressing

The module supports:
- Public key validation
- Address serialization
- JSON representation
"""

from typing import Dict, Any

from ..cl_values import CLPublicKey
from ..utils import CalltableSerialization


class InitiatorAddr:
    """
    Represents an initiator address in a Casper transaction.

    An initiator address identifies the sender of a transaction.
    It supports:
    - Public key-based addressing
    - Account hash-based addressing (TODO)
    - Address serialization and JSON representation

    Attributes:
        address (str): The initiator's address in hex format
    """

    def __init__(self, address: str):
        """
        Initialize an initiator address.

        Args:
            address (str): The initiator's address in hex format
        """
        self.address = address

    def to_bytes(self) -> bytes:
        """
        Serialize the initiator address to bytes.

        The serialization includes:
        - Address type (0 for public key)
        - Public key data

        Returns:
            bytes: The serialized initiator address
        """
        table = CalltableSerialization()
        table.add_field(0, int(0).to_bytes()) \
            .add_field(1, CLPublicKey(self.address).serialize())
        return table.to_bytes()

    def serialize(self) -> bytes:
        """
        Serialize the initiator address to a simple byte format.

        The serialization includes:
        - Address type (0 for public key)
        - Public key data

        Returns:
            bytes: The serialized initiator address
        """
        return int(0).to_bytes() + self.address

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the initiator address to a JSON representation.

        The JSON structure follows the format:
        {
            "initiator_addr": {
                "PublicKey": "<address>"
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the initiator address
        """
        return {
            "initiator_addr": {
                "PublicKey": self.address
            }
        }
