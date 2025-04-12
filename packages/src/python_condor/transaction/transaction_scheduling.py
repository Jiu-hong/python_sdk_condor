"""
Transaction Scheduling module for handling CasperLabs transaction scheduling.

This module provides functionality for managing how transactions are scheduled in the Casper network.
Currently, it supports:
- Standard scheduling: The default scheduling mode for transactions
"""

from typing import Dict, Any

from ..constants import SchedulingKind, JsonName
from ..utils import CalltableSerialization


# Constants for scheduling configuration
CONST = SchedulingKind()
JSONNAME = JsonName()

# Valid scheduling modes
VALID_ALLOWED_SCHEDULING = (CONST.STANDARD)


class TransactionScheduling:
    """
    Represents transaction scheduling configuration in the Casper network.

    Scheduling determines how a transaction is processed:
    - Standard: The default scheduling mode, where transactions are processed in order

    Attributes:
        schedule_mode (str): The scheduling mode to use
    """

    def __init__(self, schedule_mode: str = CONST.STANDARD):
        """
        Initialize transaction scheduling.

        Args:
            schedule_mode (str, optional): The scheduling mode. Defaults to STANDARD.

        Raises:
            ValueError: If the scheduling mode is invalid
        """
        if schedule_mode not in VALID_ALLOWED_SCHEDULING:
            raise ValueError(
                f"Invalid input: {schedule_mode}. Valid allowed values: {VALID_ALLOWED_SCHEDULING}")
        self.schedule_mode = schedule_mode

    def to_bytes(self) -> bytes:
        """
        Serialize the scheduling configuration to bytes.

        The serialization includes:
        - Scheduling mode as a u32

        Returns:
            bytes: The serialized scheduling configuration
        """
        match self.schedule_mode:
            case CONST.STANDARD:
                table = CalltableSerialization()
                table.add_field(0, int(0).to_bytes())
                return table.to_bytes()

    # def serialize(self):
    #     match self.schedule_mode:
    #         case CONST.STANDARD:
    #             return int(0).to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the scheduling configuration to a JSON representation.

        Returns:
            Dict[str, Any]: The JSON representation of the scheduling configuration
        """
        return {JSONNAME.SCHEDULING: self.schedule_mode}


# scheduling = TransactionScheduling()
# # print("scheduleing is: ", scheduling.to_bytes().hex())
# print("here")
