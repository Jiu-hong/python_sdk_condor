from .entity_addr import EntityAddr
from ...utils import check_clkey_hash_format


def check_named_key_format(data):
    source = data.removeprefix("named-key-")

    parts = source.split('-')
    if len(parts) != 4:
        raise ValueError(
            "Key not valid. It should have a hash address and a namedkey hash.")

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

    _ = EntityAddr(hash_addr)  # check entity_addr format

    check_clkey_hash_format(parts[3])  # check namedkey hash


def serialize_named_key(data):
    source = data.removeprefix("named-key-")

    parts = source.split('-')

    hash_addr = f"{parts[0]}-{parts[1]}-{parts[2]}"

    named_key_hash = parts[3]

    return EntityAddr(hash_addr).serialize() + bytes.fromhex(named_key_hash)
