"""
Transaction Runtime module for handling CasperLabs runtime environments.

This module provides functionality for managing runtime environments in transactions.
Currently, it supports:
- Casper VM V1: The standard runtime environment for CasperLabs transactions

The module supports:
- Runtime environment validation
- Serialization to bytes and JSON
- Default runtime configuration
"""

from typing import Dict, Any

from ..constants import JsonName, RuntimeKind
from ..utils import CalltableSerialization


# Constants for runtime configuration
CONST = RuntimeKind()
JSONNAME = JsonName()

# Valid runtime environments
VALID_ALLOWED_RUNTIME = (CONST.VMCASPERV1)


class TransactionRuntime:
    """
    Represents a runtime environment in a CasperLabs transaction.

    The runtime environment determines how the transaction code will be executed.
    Currently, only Casper VM V1 is supported.

    Attributes:
        runtime (str): The runtime environment identifier
    """

    def __init__(self, runtime: str = CONST.VMCASPERV1):
        """
        Initialize a runtime environment.

        Args:
            runtime (str, optional): The runtime environment identifier. Defaults to VMCASPERV1.

        Raises:
            ValueError: If the runtime environment is invalid
        """
        if runtime not in VALID_ALLOWED_RUNTIME:
            raise ValueError(
                f"Invalid input {runtime}. Allowed values are: {VALID_ALLOWED_RUNTIME}")
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the runtime environment to bytes.

        The serialization includes:
        - Runtime type as a u32 (0 for VMCASPERV1)

        Returns:
            bytes: The serialized runtime environment
        """
        table = CalltableSerialization()
        table.add_field(0, int(0).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the runtime environment to a JSON representation.

        Returns:
            Dict[str, Any]: The JSON representation of the runtime environment
        """
        return {JSONNAME.RUNTIME: self.runtime}
