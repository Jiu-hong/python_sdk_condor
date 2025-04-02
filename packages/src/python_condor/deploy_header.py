from datetime import datetime, timezone
from hashlib import blake2b
from python_condor.constants import JsonName
from python_condor.cl_values.cl_number import CLU64
from python_condor.cl_values.cl_publickey import CLPublicKey
from python_condor.cl_values.cl_string import CLString
from python_condor.utils import serialize_string

JSONNAME = JsonName()


class DeployHeader:
    def __init__(self, account, chain_name, now=datetime.now(timezone.utc), ttl=30, gas_price=1):
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


account = "0203c1e1349b0a5b34246bce27a68de90d842ace31221a363007e483301977611dfa"
timestamp = "123"
ttl = 30
gas_price = 3
body_hash = "889135da6f70c3e5832a43b358a4b634df9056d4f55c9486cc92249d2c3e386d"
dependencies = "00"
chain_name = "casper-test"
# a = DeployHeader(account, timestamp, ttl, gas_price,
#                  body_hash, dependencies, chain_name)
# print("hash=>")
# print(a.byteHash())
