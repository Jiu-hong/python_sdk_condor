import re

from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG


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
