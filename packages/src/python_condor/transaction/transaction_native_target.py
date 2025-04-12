"""
Transaction Native Target module for handling Casper native targets.

This module provides functionality for creating and managing native targets in transactions.
Native targets are used for:
- System-level operations
- Built-in contract calls
- Native functionality execution

The module supports:
- Target type identification
- Serialization to bytes and JSON
"""

from typing import Dict, Any

from ..constants import JsonName, RuntimeKind
from ..utils import CalltableSerialization


# Constants for native target configuration
JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionNativeTarget:
    """
    Represents a native target in a Casper transaction.

    A native target is used for system-level operations and built-in contract calls.
    It does not require additional configuration as it represents the default target type.

    This class is used when:
    - Calling system contracts
    - Executing native functionality
    - Performing built-in operations
    """

    def to_bytes(self) -> bytes:
        """
        Serialize the native target to bytes.

        The serialization includes:
        - Target type as a u32 (0 for native)

        Returns:
            bytes: The serialized native target
        """
        table = CalltableSerialization()
        table.add_field(0, int(0).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the native target to a JSON representation.

        Returns:
            Dict[str, Any]: The JSON representation of the native target
        """
        return {JSONNAME.TARGET: JSONNAME.NATIVE}
