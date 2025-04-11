"""Entity address module.

This module provides functionality for handling entity addresses in the Casper network.
Entity addresses are used to identify different types of entities (system, account, contract).
"""

from typing import NoReturn

from ...utils import check_clkey_hash_format
from ...constants import Prefix


PREFIX = Prefix()


class EntityAddr:
    """Class for handling entity addresses in the Casper network.

    An entity address represents a specific entity in the network and can be one of:
    - System entity (entity-system-<hash>)
    - Account entity (entity-account-<hash>)
    - Contract entity (entity-contract-<hash>)
    """

    def __init__(self, data: str) -> NoReturn:
        """Initialize an EntityAddr instance.

        Args:
            data: The entity address string in the format:
                  entity-{system|account|contract}-<hash>

        Raises:
            ValueError: If the address format is invalid:
                - Wrong prefix
                - Invalid entity type
                - Invalid hash format
        """
        if not data.startswith(PREFIX.ENTITY):
            raise ValueError("data should start with 'entity-'")

        entity_data = data.removeprefix(PREFIX.ENTITY)

        if entity_data.startswith(PREFIX.SYSTEM):
            hash_value = entity_data.removeprefix(PREFIX.SYSTEM)
            check_clkey_hash_format(hash_value)
        elif entity_data.startswith(PREFIX.ACCOUNT):
            hash_value = entity_data.removeprefix(PREFIX.ACCOUNT)
            check_clkey_hash_format(hash_value)
        elif entity_data.startswith(PREFIX.CONTRACT):
            hash_value = entity_data.removeprefix(PREFIX.CONTRACT)
            check_clkey_hash_format(hash_value)
        else:
            raise ValueError(
                "data should start with 'entity-system-', 'entity-account' or 'entity-contract'")

        self.data = data

    def serialize(self) -> bytes:
        """Serialize the entity address to bytes.

        The serialization format is:
        1. A single byte indicating the entity type:
           - 0x00 for system
           - 0x01 for account
           - 0x02 for contract
        2. The hash bytes

        Returns:
            Bytes representation of the entity address.
        """
        entity_data = self.data.removeprefix(PREFIX.ENTITY)
        if entity_data.startswith(PREFIX.SYSTEM):
            return int(0).to_bytes(1, byteorder='little') + bytes.fromhex(
                entity_data.removeprefix(PREFIX.SYSTEM))
        elif entity_data.startswith(PREFIX.ACCOUNT):
            return int(1).to_bytes(1, byteorder='little') + bytes.fromhex(
                entity_data.removeprefix(PREFIX.ACCOUNT))
        elif entity_data.startswith(PREFIX.CONTRACT):
            return int(2).to_bytes(1, byteorder='little') + bytes.fromhex(
                entity_data.removeprefix(PREFIX.CONTRACT))
