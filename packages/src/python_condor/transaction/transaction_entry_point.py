"""
Transaction Entry Point module for handling Casper transaction entry points.

This module provides functionality for creating and managing transaction entry points in the Casper network.
It supports various types of entry points:
- Call: For calling contracts
- Custom: For custom entry points with arguments
- Transfer: For transfer operations
- Add/Withdraw/Activate Bid: For bid operations
- Delegate/Undelegate/Redelegate: For delegation operations
- Change Public Key: For key changes
"""

from typing import Dict, Any, Optional

from ..constants import EntryPointKind, JsonName
from ..utils import CalltableSerialization, serialize_string


# Constants for entry point configuration
ENTRYPOINT = EntryPointKind()
JSONNAME = JsonName()

# Valid entry point types
VALID_ALLOWED_ENTRY_POINTS = (
    ENTRYPOINT.CALL,
    ENTRYPOINT.CUSTOM,
    ENTRYPOINT.TRANSFER,
    ENTRYPOINT.ADD_BID,
    ENTRYPOINT.WITHDRAW_BID,
    ENTRYPOINT.DELEGATE,
    ENTRYPOINT.UNDELEGATE,
    ENTRYPOINT.REDELEGATE,
    ENTRYPOINT.ACTIVATE_BID,
    ENTRYPOINT.CHANGEPUBLICKEY
)


class TransactionEntryPoint:
    """
    Represents a transaction entry point in the Casper network.

    An entry point defines where and how a transaction will be executed:
    - The type of operation (call, transfer, bid, etc.)
    - Any additional arguments needed (for custom entry points)

    Attributes:
        entry_point (str): The type of entry point
        arg (Optional[str]): Additional argument for custom entry points
    """

    def __init__(self, entry_point: str, arg: Optional[str] = None):
        """
        Initialize a transaction entry point.

        Args:
            entry_point (str): The type of entry point
            arg (Optional[str], optional): Additional argument for custom entry points. Defaults to None.

        Raises:
            ValueError: If the entry point type is invalid or if a custom entry point is missing its argument
        """
        if entry_point not in VALID_ALLOWED_ENTRY_POINTS:
            raise ValueError(
                f"Invalid input: {entry_point}. Allowed values are: {VALID_ALLOWED_ENTRY_POINTS}")
        if entry_point == ENTRYPOINT.CUSTOM and arg is None:
            raise ValueError("Entrypoint name cannot be empty for Custom.")

        self.entry_point = entry_point
        self.arg = arg

    def to_bytes(self) -> bytes:
        """
        Serialize the entry point to bytes.

        The serialization includes:
        - Entry point type as a u32
        - Additional argument for custom entry points

        Returns:
            bytes: The serialized entry point
        """
        table = CalltableSerialization()

        match self.entry_point:
            case ENTRYPOINT.CALL:
                table.add_field(0, int(0).to_bytes())
            case ENTRYPOINT.CUSTOM:
                table.add_field(0, int(1).to_bytes()) \
                    .add_field(1, serialize_string(self.arg))
            case ENTRYPOINT.TRANSFER:
                table.add_field(0, int(2).to_bytes())
            case ENTRYPOINT.ADD_BID:
                table.add_field(0, int(3).to_bytes())
            case ENTRYPOINT.WITHDRAW_BID:
                table.add_field(0, int(4).to_bytes())
            case ENTRYPOINT.DELEGATE:
                table.add_field(0, int(5).to_bytes())
            case ENTRYPOINT.UNDELEGATE:
                table.add_field(0, int(6).to_bytes())
            case ENTRYPOINT.REDELEGATE:
                table.add_field(0, int(7).to_bytes())
            case ENTRYPOINT.ACTIVATE_BID:
                table.add_field(0, int(8).to_bytes())
            case ENTRYPOINT.CHANGEPUBLICKEY:
                table.add_field(0, int(9).to_bytes())

        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the entry point to a JSON representation.

        The JSON format depends on the entry point type:
        - For custom entry points: {"entry_point": {"Custom": "arg"}}
        - For other types: {"entry_point": "type"}

        Returns:
            Dict[str, Any]: The JSON representation of the entry point
        """
        match self.entry_point:
            case ENTRYPOINT.CUSTOM:
                return {JSONNAME.ENTRYPOINT: {self.entry_point: self.arg}}
            case _:
                return {JSONNAME.ENTRYPOINT: self.entry_point}
