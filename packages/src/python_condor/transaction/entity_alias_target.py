"""
Entity Alias Target module for handling CasperLabs entity alias targets.

This module provides functionality for creating and managing entity alias targets in transactions.
Entity alias targets are used for:
- Targeting contracts by their name
- Managing runtime environment configuration
- Supporting stored contract references

The module supports:
- Contract name validation
- Runtime configuration
- Serialization to bytes and JSON
"""

from typing import Dict, Any

from ..constants import JsonName
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization, serialize_string


# Constants for entity alias target configuration
JSONNAME = JsonName()


class EntityAliasTarget:
    """
    Represents an entity alias target in a CasperLabs transaction.

    An entity alias target is used to reference a contract by its name.
    It supports:
    - Contract name specification
    - Runtime environment configuration
    - Stored contract references

    Attributes:
        contract_name (str): The name of the contract
        runtime (str): The runtime environment to use
    """

    def __init__(self, runtime: str, contract_name: str):
        """
        Initialize an entity alias target.

        Args:
            runtime (str): The runtime environment to use
            contract_name (str): The name of the contract
        """
        self.contract_name = contract_name
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the entity alias target to bytes.

        The serialization includes:
        - Target type (1 for stored)
        - Contract name
        - Runtime configuration

        Returns:
            bytes: The serialized entity alias target
        """
        # Create inner table for entity alias target
        selftable = CalltableSerialization()
        selftable.add_field(0, int(1).to_bytes()) \
            .add_field(1, serialize_string(self.contract_name))

        # Create outer table for stored target
        table = CalltableSerialization()
        table.add_field(0, int(1).to_bytes()) \
            .add_field(1, selftable.to_bytes()) \
            .add_field(2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the entity alias target to a JSON representation.

        The JSON structure follows the format:
        {
            "target": {
                "Stored": {
                    "id": {
                        "ByName": "<contract_name>"
                    },
                    "runtime": "<runtime>"
                }
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the entity alias target
        """
        return {
            JSONNAME.TARGET: {
                JSONNAME.STORED: {
                    JSONNAME.ID: {
                        JSONNAME.BYNAME: self.contract_name
                    },
                    JSONNAME.RUNTIME: self.runtime
                }
            }
        }
