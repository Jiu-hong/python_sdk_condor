
from ...constants import Prefix

PREFIX = Prefix()


class EntityAddr:
    def __init__(self, data):
        # check todo
        self.data = data

    def serialize(self):
        entity_data = self.data.removeprefix(PREFIX.ENTITY)
        if entity_data.startswith(PREFIX.SYSTEM):
            return int(0).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.SYSTEM))
        elif entity_data.startswith(PREFIX.ACCOUNT):
            return int(1).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.ACCOUNT))
        elif entity_data.startswith(PREFIX.CONTRACT):
            return int(2).to_bytes() + bytes.fromhex(entity_data.removeprefix(PREFIX.CONTRACT))


def check_message_key_format(data):
    if not data.startswith("message-topic-entity-") and not data.startswith("message-entity-"):
        raise ValueError(
            "Key not valid. It should start with 'message-topic-entity-' or 'message-entity-'")


def serialize_message_key(data):
    source = data.removeprefix("message-")
    # message-topic-entity-contract-xxx
    if source.startswith("topic-"):
        source = source.removeprefix("topic-")

        parts = source.split('-')
        if len(parts) != 4:
            raise ValueError(
                "Key not valid. It should have a hash address and a topic hash.")

        hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

        topic_hash = parts[3]

        return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("00")

    else:
        # message-entity-contract-xxx-xxx-x
        parts = source.split('-')
        if len(parts) != 5:
            raise ValueError(
                "Key not valid. It should have a hash address, a topic hash, and a message index.")

        hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

        topic_hash = parts[3]

        if len(parts[4]) == 0:
            raise ValueError(
                "Key not valid. Expected a non-empty message index.'")

        index = int(parts[4], 16).to_bytes(4, byteorder='little')

        return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("01")+index
