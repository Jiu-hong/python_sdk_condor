"""
Transaction Session Target module for handling CasperLabs session targets.

This module provides functionality for creating and managing session targets in transactions.
Session targets are used for:
- Deploying new contracts
- Upgrading existing contracts
- Executing session code

The module supports:
- Module bytecode handling
- Install/upgrade flag management
- Runtime configuration
- Serialization to bytes and JSON
"""

from typing import Dict, Any

from ..constants import JsonName, RuntimeKind
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization


# Constants for session target configuration
JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionSessionTarget:
    """
    Represents a session target in a CasperLabs transaction.

    A session target is used for deploying or upgrading contracts, or executing session code.
    It contains the module bytecode and configuration for how it should be executed.

    Attributes:
        module_bytes (bytes): The compiled module bytecode
        is_install_upgrade (bool): Whether this is an install/upgrade operation
        runtime (str): The runtime environment to use
    """

    def __init__(self, runtime: str, module_bytes: str, is_install_upgrade: bool = False):
        """
        Initialize a session target.

        Args:
            runtime (str): The runtime environment to use
            module_bytes (str): The module bytecode in hex format
            is_install_upgrade (bool, optional): Whether this is an install/upgrade operation. Defaults to False.
        """
        self.module_bytes = bytes.fromhex(module_bytes)
        self.is_install_upgrade = is_install_upgrade
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the session target to bytes.

        The serialization includes:
        - Target type (2 for session)
        - Install/upgrade flag
        - Runtime configuration
        - Module bytecode length and data

        Returns:
            bytes: The serialized session target
        """
        module_bytes_length = len(
            self.module_bytes).to_bytes(4, byteorder='little')
        table = CalltableSerialization()
        table.add_field(0, int(2).to_bytes()) \
            .add_field(1, self.is_install_upgrade.to_bytes()) \
            .add_field(2, TransactionRuntime(self.runtime).to_bytes()) \
            .add_field(3, module_bytes_length + self.module_bytes)
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the session target to a JSON representation.

        Returns:
            Dict[str, Any]: The JSON representation of the session target
        """
        return {
            JSONNAME.TARGET: {
                JSONNAME.TRANSACTION_SESSION: {
                    JSONNAME.IS_INSTALL_UPGRADE: self.is_install_upgrade,
                    JSONNAME.MODULE_BYTES: self.module_bytes.hex(),
                    JSONNAME.RUNTIME: self.runtime
                }
            }
        }
