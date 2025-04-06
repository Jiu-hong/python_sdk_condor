import re

from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG
from hashlib import blake2b

algo = {
    b'\x01': "ed25519",
    b'\x02': "secp256k1"
}


class CLPublicKey(CLValue, CLAtomic):
    tag = TAG.CLPublicKey.value

    def __init__(self, data):
        regx = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(data)
        if not isinstance(result, re.Match):
            raise ValueError(
                "publickey should be 01xxx(64 length) or 02xxx(66 length)")
        super().__init__(data)

    def serialize(self) -> bytes:
        return bytes.fromhex(self.data)

    def get_account_hash(self):
        public_key_bytes = bytes.fromhex(self.data)

        as_bytes = \
            bytes(algo[public_key_bytes[0:1]], "utf-8") + \
            bytearray(1) + \
            public_key_bytes[1:]

        h = blake2b(digest_size=32)
        h.update(as_bytes)
        return h.hexdigest()
