
from .entity_addr import EntityAddr
from ...utils import check_clkey_hash_format


# "message-topic-entity-contract-xxx-xxx"
# message-entity-contract-xxx-xxx-f


def check_message_key_format(data):
    if not data.startswith("message-topic-entity-") and not data.startswith("message-entity-"):
        raise ValueError(
            "Key not valid. It should start with 'message-topic-entity-' or 'message-entity-'")

    if data.startswith("message-topic-"):
        source = data.removeprefix("message-topic-")
        parts = source.split('-')

        if len(parts) != 4:
            raise ValueError(
                "Key not valid. It should have a hash address and a topic hash.")
    else:
        source = data.removeprefix("message-")
        parts = source.split('-')

        if len(parts) != 5:
            raise ValueError(
                "Key not valid. It should have a hash address, a topic hash, and a message index.")

        try:
            _ = int(parts[4], 16)  # check index format
        except:
            raise ValueError("the index should be an hexadecimal number")

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"
    _ = EntityAddr(hash_addr)  # check entity_addr format
    check_clkey_hash_format(parts[3])


def serialize_message_key(data):
    source = data.removeprefix("message-")
    # message-topic-entity-contract-xxx
    if source.startswith("topic-"):
        source = source.removeprefix("topic-")

        parts = source.split('-')
        # if len(parts) != 4:
        #     raise ValueError(
        #         "Key not valid. It should have a hash address and a topic hash.")

        hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

        topic_hash = parts[3]

        return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("00")

    else:
        # message-entity-contract-xxx-xxx-x
        parts = source.split('-')
        # if len(parts) != 5:
        #     raise ValueError(
        #         "Key not valid. It should have a hash address, a topic hash, and a message index.")

        hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

        topic_hash = parts[3]

        if len(parts[4]) == 0:
            raise ValueError(
                "Key not valid. Expected a non-empty message index.'")

        index = int(parts[4], 16).to_bytes(4, byteorder='little')

        return EntityAddr(hash_addr).serialize() + bytes.fromhex(topic_hash) + bytes.fromhex("01")+index
