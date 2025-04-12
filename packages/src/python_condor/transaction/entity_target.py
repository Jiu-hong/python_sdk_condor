"""
Entity Target module for handling Casper entity targets.

This module provides functionality for creating and managing entity targets in transactions.
Entity targets are used for:
- Targeting contracts by their hash
- Managing runtime environment configuration
- Supporting stored contract references

The module supports:
- Contract hash validation (64-character hex string)
- Runtime configuration
- Serialization to bytes and JSON
"""

import re
from typing import Dict, Any

from ..constants import JsonName
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization


# Constants for entity target configuration
JSONNAME = JsonName()


class EntityTarget:
    """
    Represents an entity target in a Casper transaction.

    An entity target is used to reference a contract by its hash.
    It supports:
    - Contract hash specification (64-character hex string)
    - Runtime environment configuration
    - Stored contract references

    Attributes:
        contract_hash (str): The hash of the contract in hex format
        runtime (str): The runtime environment to use
    """

    def __init__(self, runtime: str, contract_hash: str):
        """
        Initialize an entity target.

        Args:
            runtime (str): The runtime environment to use
            contract_hash (str): The hash of the contract in hex format

        Raises:
            ValueError: If the contract hash is not a valid 64-character hex string
        """
        # Validate contract hash format
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(contract_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "contract-hash should only contain alphabet and number(64 length)")

        self.contract_hash = contract_hash
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the entity target to bytes.

        The serialization includes:
        - Target type (1 for stored)
        - Contract hash
        - Runtime configuration

        Returns:
            bytes: The serialized entity target
        """
        # Create inner table for entity target
        selftable = CalltableSerialization()
        selftable.add_field(0, int(0).to_bytes()) \
            .add_field(1, bytes.fromhex(self.contract_hash))

        # Create outer table for stored target
        table = CalltableSerialization()
        table.add_field(0, int(1).to_bytes()) \
            .add_field(1, selftable.to_bytes()) \
            .add_field(2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the entity target to a JSON representation.

        The JSON structure follows the format:
        {
            "target": {
                "Stored": {
                    "id": {
                        "ByHash": "<contract_hash>"
                    },
                    "runtime": "<runtime>"
                }
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the entity target
        """
        return {
            JSONNAME.TARGET: {
                JSONNAME.STORED: {
                    JSONNAME.ID: {
                        JSONNAME.BYHASH: self.contract_hash
                    },
                    JSONNAME.RUNTIME: self.runtime
                }
            }
        }
