import re
from datetime import datetime, timezone
from hashlib import blake2b

from ..cl_values import CLPublicKey
from ..constants import JsonName
from ..utils import serialize_string

JSONNAME = JsonName()


class DeployHeader:
    def __init__(self, account, chain_name, now=datetime.now(timezone.utc), ttl=30, gas_price=1):
        # check account pattern
        regx = "(01[0-9a-zA-Z]{64})|(02[0-9a-zA-Z]{66})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(account)
        if not isinstance(result, re.Match):
            raise ValueError(
                "account should be 01xxx(64 length) or 02xxx(66 length)")
         # check chain-name
        if chain_name == "":
            raise ValueError("The chain_name shouldn't be empty.")
        # check time
        if not isinstance(now, datetime):
            raise TypeError("time should be type datetime.datetime")
        # check ttl
        if not isinstance(ttl, int):
            raise TypeError("ttl should be type int")
        # check gas_price
        if not isinstance(gas_price, int):
            raise TypeError("gas_price should be type int")
        self.account = account
        self.chain_name = chain_name
        self.time = now
        self.ttl = ttl
        self.gas_price = gas_price

    def add_body_hash(self, body_hash):
        self.body_hash = body_hash

    def to_bytes(self) -> bytes:
        s_account = CLPublicKey(self.account).serialize()
        s_time_now = int(self.time.timestamp() *
                         1000).to_bytes(8, byteorder='little')
        # example 2024-11-17T23:22:15.313Z
        # s_time_now = CLU64(int(datetime.fromisoformat(
        #     '2025-04-02T02:13:08.720Z').timestamp() * 1000)).serialize()
        # ttl is mins -> switch to milliseconds
        s_ttl = (int(self.ttl) * 60000).to_bytes(8, byteorder='little')
        s_gas_price = self.gas_price.to_bytes(8, byteorder='little')
        s_body_hash = bytes.fromhex(self.body_hash)
        s_dependencies = bytes.fromhex("00000000")
        s_chain_name = serialize_string(self.chain_name)
        result = s_account + s_time_now + s_ttl + s_gas_price + \
            s_body_hash+s_dependencies + s_chain_name
        return result

    def byteHash(self) -> str:
        header_bytes = self.to_bytes()
        h = blake2b(digest_size=32)
        h.update(header_bytes)
        return h.hexdigest()

    def to_json(self) -> dict:
        result = {JSONNAME.HEADER: {
            JSONNAME.ACCOUNT: self.account,
            JSONNAME.TIMESTAMP: self.time.replace(
                tzinfo=None).isoformat(timespec=JSONNAME.MILLISECONDS)+"Z",
            JSONNAME.TTL: str(self.ttl)+'m',
            JSONNAME.GAS_PRICE: self.gas_price,
            JSONNAME.BODY_HASH: self.body_hash,
            JSONNAME.DEPENDENCIES: [],
            JSONNAME.CHAIN_NAME: self.chain_name
        }}
        return result
