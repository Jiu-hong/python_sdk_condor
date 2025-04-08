from .entity_addr import EntityAddr
from ...constants import Prefix
from ...utils import check_clkey_hash_format

PREFIX = Prefix()
# entry-point-v1-entity-contract-53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481
VM_VERSION = ("v1")


def check_entry_point_key_format(data):
    source = data.removeprefix(PREFIX.ENTRY_POINT)
    parts = source.split('-')
    if len(parts) != 5:
        raise ValueError(
            "Key not valid. It should have vm version, a hash address and a entrypoint hash.")

    if parts[0] not in VM_VERSION:
        raise ValueError("vm version should be v1")

    hash_addr = f"{parts[1]}-{parts[2]}-{parts[3]}"

    _ = EntityAddr(hash_addr)  # check entity_addr format

    check_clkey_hash_format(parts[4])  # check entrypoint hash


def serialize_entry_point_key(data):
    source = data.removeprefix(PREFIX.ENTRY_POINT)

    parts = source.split('-')

    version = int(0).to_bytes()

    hash_addr = f"{parts[1]}-{parts[2]}-{parts[3]}"

    named_key_hash = parts[4]

    return version + EntityAddr(hash_addr).serialize() + bytes.fromhex(named_key_hash)
