"""
Transaction V1 Payload module for handling Casper version 1 transaction payloads.

This module provides functionality for creating and managing version 1 transaction payloads in the Casper network.
It handles:
- Payload creation with arguments, target, entry point, and scheduling
- Payload serialization to bytes
- JSON serialization of payloads
- Time and TTL management
- Chain name and pricing mode handling
"""

from datetime import datetime, timezone
from typing import Dict, Any, Union

from ..constants import JsonName
from ..utils import serialize_string, CalltableSerialization
from .entity_alias_target import EntityAliasTarget
from .entity_target import EntityTarget
from .initiator_addr import InitiatorAddr
from .named_arg import NamedArg
from .package_hash_target import PackageHashTarget
from .package_name_target import PackageNameTarget
from .payload_fields import PayloadFields
from .pricing_mode import PricingMode
from .transaction_entry_point import TransactionEntryPoint
from .transaction_scheduling import TransactionScheduling


# Constants for JSON field names
JSONNAME = JsonName()


class TransactionV1Payload:
    """
    Represents a version 1 transaction payload in the Casper network.

    A transaction payload contains:
    - Arguments for the transaction
    - Target (entity, package, etc.)
    - Entry point for execution
    - Scheduling information
    - Initiator address
    - Pricing mode
    - Chain name
    - Time and TTL settings

    Attributes:
        initiatorAddr (str): The address of the transaction initiator
        ttl (int): Time to live in minutes
        pricingMode (PricingMode): The pricing mode for the transaction
        time (datetime): The transaction timestamp
        chainName (str): The name of the target chain
        fields (PayloadFields): The payload fields container
    """

    def __init__(
        self,
        args: Dict[str, Any],
        transactionTarget: Union[EntityTarget, EntityAliasTarget, PackageHashTarget, PackageNameTarget],
        entrypoint: TransactionEntryPoint,
        scheduling: TransactionScheduling,
        initiatorAddr: str,
        pricing_mode: PricingMode,
        chainName: str,
        ttl: int = 30,
        now: datetime = datetime.now(timezone.utc)
    ):
        """
        Initialize a version 1 transaction payload.

        Args:
            args (Dict[str, Any]): The transaction arguments
            transactionTarget (Union[EntityTarget, EntityAliasTarget, PackageHashTarget, PackageNameTarget]): The transaction target
            entrypoint (TransactionEntryPoint): The entry point for execution
            scheduling (TransactionScheduling): The scheduling information
            initiatorAddr (str): The address of the transaction initiator
            pricing_mode (PricingMode): The pricing mode for the transaction
            chainName (str): The name of the target chain
            ttl (int, optional): Time to live in minutes. Defaults to 30.
            now (datetime, optional): The transaction timestamp. Defaults to current UTC time.
        """
        self.initiatorAddr = initiatorAddr
        self.ttl = ttl
        self.pricingMode = pricing_mode
        self.time = now
        self.chainName = chainName
        self.fields = PayloadFields(
            args, transactionTarget, entrypoint, scheduling)

    def to_bytes(self) -> bytes:
        """
        Serialize the payload to bytes.

        The serialization includes:
        1. Runtime arguments with length
        2. Target with length
        3. Entry point with length
        4. Scheduling with length
        5. Initiator address
        6. Timestamp
        7. TTL
        8. Chain name
        9. Pricing mode
        10. Fields

        Returns:
            bytes: The serialized payload
        """
        # Serialize runtime arguments
        runtime_args_buffer = int(0).to_bytes()
        runtime_args_buffer += len(self.fields.args).to_bytes(4,
                                                              byteorder='little')

        for name, value in self.fields.args.items():
            named_arg = NamedArg(name, value)
            arg_bytes = named_arg.to_byte_with_named_arg()
            runtime_args_buffer += arg_bytes

        length_runtime_args = len(
            runtime_args_buffer).to_bytes(4, byteorder='little')
        runtime_args_with_length = length_runtime_args + runtime_args_buffer
        self.fields.addField(0, runtime_args_with_length)

        # Serialize target
        target_bytes = self.fields.target.to_bytes()
        length_target = len(target_bytes).to_bytes(4, byteorder='little')
        target_with_length = length_target + target_bytes
        self.fields.addField(1, target_with_length)

        # Serialize entry point
        entry_point_bytes = self.fields.entry_point.to_bytes()
        length_entry_point = len(entry_point_bytes).to_bytes(
            4, byteorder='little')
        entry_point_with_length = length_entry_point + entry_point_bytes
        self.fields.addField(2, entry_point_with_length)

        # Serialize scheduling
        scheduling_bytes = self.fields.scheduling.to_bytes()
        length_scheduling = len(scheduling_bytes).to_bytes(
            4, byteorder='little')
        scheduling_with_length = length_scheduling + scheduling_bytes
        self.fields.addField(3, scheduling_with_length)

        # Create final serialization table
        table = CalltableSerialization()
        table.add_field(0, InitiatorAddr(self.initiatorAddr).to_bytes()) \
            .add_field(1, int(self.time.timestamp() * 1000).to_bytes(8, byteorder='little')) \
            .add_field(2, (int(self.ttl) * 60000).to_bytes(8, byteorder='little')) \
            .add_field(3, serialize_string(self.chainName)) \
            .add_field(4, self.pricingMode.to_bytes()) \
            .add_field(5, self.fields.to_bytes())

        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the payload to a JSON representation.

        The JSON includes:
        - Initiator address
        - Timestamp
        - TTL
        - Chain name
        - Pricing mode
        - Fields (args, target, entry point, scheduling)

        Returns:
            Dict[str, Any]: The JSON representation of the payload
        """
        return {
            JSONNAME.PAYLOAD: {
                **InitiatorAddr(self.initiatorAddr).to_json(),
                JSONNAME.TIMESTAMP: self.time.replace(tzinfo=None).isoformat(timespec='milliseconds') + "Z",
                JSONNAME.TTL: f"{self.ttl}m",
                JSONNAME.CHAIN_NAME: self.chainName,
                **self.pricingMode.to_json(),
                **self.fields.to_json()
            }
        }


# args = {"arg1": CLU8(123), "arg2": CLString("Hello")}

# transactionTarget = TransactionTarget("stored", "InvocableEntity",
#                                       "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")


# entrypoint = TransactionEntryPoint("Custom", "apple")

# scheduling = TransactionScheduling()
# initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
# pricing_mode = PricingMode("Classic", 20000000000000)

# args = {}
# transactionTarget2 = TransactionTarget("session", '01', False)
# entrypoint2 = TransactionEntryPoint("Call")
# transaction_v1_payload = TransactionV1Payload(args, transactionTarget2,
#                                               entrypoint2, scheduling, initiatorAddr, pricing_mode, "casper-net-1")


# print("transaction_v1_payload to_json:",
#       json.dumps(transaction_v1_payload.to_json()))

# bytes = transaction_v1_payload.to_bytes()
# print("bytes_transaction_v1_payload is: \n", bytes.hex())
