"""
Payload Fields module for handling CasperLabs transaction payload fields.

This module provides functionality for managing transaction payload fields.
Payload fields include:
- Runtime arguments
- Transaction targets
- Entry points
- Scheduling configuration

The module supports:
- Field serialization
- Body hash calculation
- JSON representation
- Named argument handling
"""

from hashlib import blake2b
from typing import Dict, Any, Union, List

from ..constants import JsonName
from .entity_alias_target import EntityAliasTarget
from .entity_target import EntityTarget
from .named_arg import NamedArg
from .package_hash_target import PackageHashTarget
from .package_name_target import PackageNameTarget
from .transaction_scheduling import TransactionScheduling
from .transaction_entry_point import TransactionEntryPoint


# Constants for payload fields configuration
JSONNAME = JsonName()


class PayloadFields:
    """
    Represents the fields of a CasperLabs transaction payload.

    A payload contains all the necessary information for executing a transaction:
    - Runtime arguments for the transaction
    - Target specification (contract, package, etc.)
    - Entry point for execution
    - Scheduling configuration

    Attributes:
        args (Dict[str, Any]): The runtime arguments
        target (Union[EntityTarget, EntityAliasTarget, PackageHashTarget, PackageNameTarget]): The transaction target
        entry_point (TransactionEntryPoint): The entry point for execution
        scheduling (TransactionScheduling): The scheduling configuration
        dict (Dict[int, bytes]): Internal field storage
    """

    def __init__(
        self,
        args: Dict[str, Any],
        target: Union[EntityTarget, EntityAliasTarget, PackageHashTarget, PackageNameTarget],
        entry_point: TransactionEntryPoint,
        scheduling: TransactionScheduling
    ):
        """
        Initialize payload fields.

        Args:
            args (Dict[str, Any]): The runtime arguments
            target (Union[EntityTarget, EntityAliasTarget, PackageHashTarget, PackageNameTarget]): The transaction target
            entry_point (TransactionEntryPoint): The entry point for execution
            scheduling (TransactionScheduling): The scheduling configuration
        """
        self.args = args
        self.target = target
        self.entry_point = entry_point
        self.scheduling = scheduling
        self.dict = {}

    def addField(self, index: int, bytes_data: bytes) -> None:
        """
        Add a field to the payload.

        Args:
            index (int): The field index
            bytes_data (bytes): The field data
        """
        self.dict[index] = bytes_data

    def to_bytes(self) -> bytes:
        """
        Serialize the payload fields to bytes.

        The serialization includes:
        - Field count as u32
        - Field indices and data

        Returns:
            bytes: The serialized payload fields
        """
        buffer = (len(self.dict)).to_bytes(4, byteorder='little')
        for key, value in self.dict.items():
            buffer = buffer + key.to_bytes(2, byteorder='little')
            buffer = buffer + value
        return buffer

    def body_hash(self) -> str:
        """
        Calculate the hash of the payload body.

        The hash is calculated using BLAKE2b-256 on the serialized payload.

        Returns:
            str: The hex-encoded hash of the payload body
        """
        body_hex = self.serialize()
        h = blake2b(digest_size=32)
        body_bytes = bytes.fromhex(body_hex)
        h.update(body_bytes)
        return h.hexdigest()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the payload fields to a JSON representation.

        The JSON structure includes:
        - Runtime arguments as named arguments
        - Entry point configuration
        - Scheduling configuration
        - Target specification

        Returns:
            Dict[str, Any]: The JSON representation of the payload fields
        """
        # Convert runtime arguments to named arguments
        name_args: List[Dict[str, Any]] = []
        for name, value in self.args.items():
            name_args.append(NamedArg(name, value).to_json())

        # Combine all fields into a single JSON structure
        return {
            JSONNAME.FIELDS: {
                JSONNAME.ARGS: {JSONNAME.NAMED: name_args},
                **self.entry_point.to_json(),
                **self.scheduling.to_json(),
                **self.target.to_json()
            }
        }
