from ...utils import check_clkey_hash_format
from ...constants import Prefix

PREFIX = Prefix()


class EntityAddr:
    def __init__(self, data):
        # entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a
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

    def serialize(self):
        entity_data = self.data.removeprefix(PREFIX.ENTITY)
        if entity_data.startswith(PREFIX.SYSTEM):
            return int(0).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.SYSTEM))
        elif entity_data.startswith(PREFIX.ACCOUNT):
            return int(1).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.ACCOUNT))
        elif entity_data.startswith(PREFIX.CONTRACT):
            return int(2).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.CONTRACT))
