from datetime import datetime
from hashlib import blake2b
from time import time
from cl_number import CLU64
from cl_publickey import CLPublicKey
from cl_string import CLString


class Deploy:
    def __init__(self, hash, header, payment, session, approvals) -> None:
        self.hash = hash
        self.header = header
        self.payment = payment
        self.session = session
        self.approvals = approvals


class DeployHeader:
    def __init__(self, account, timestamp, ttl, gas_price, body_hash, dependencies, chain_name) -> None:
        self.account = account
        self.timestamp = timestamp
        self.ttl = ttl
        self.gas_price = gas_price
        self.body_hash = body_hash
        self.dependencies = dependencies
        self.chain_name = chain_name

    def serialize(self):
        s_account = CLPublicKey(self.account).serialize()
        s_time_now = CLU64(int(time() * 1000)).serialize()
        # example 2024-11-17T23:22:15.313Z
        # s_time_now = CLU64(int(datetime.fromisoformat(
        #     '2024-11-17T23:22:15.313Z').timestamp() * 1000)).serialize()
        # ttl is mins -> switch to milliseconds
        s_ttl = CLU64(int(self.ttl) * 60000).serialize()
        s_gas_price = CLU64(self.gas_price).serialize()
        s_body_hash = self.body_hash
        # Body hash is a hash over the contents of the deploy body, which includes the payment, session, and approval fields. Its serialization is the byte representation of the hash itself.
        s_dependencies = "00000000"
        s_chain_name = CLString(self.chain_name).serialize()
        return (s_account, s_time_now, s_ttl, s_gas_price, s_body_hash, s_dependencies, s_chain_name)

    def byteHash(self):
        header_bytes = self.serialize()
        h = blake2b(digest_size=32)
        s_account = bytes.fromhex(header_bytes[0])
        s_time_now = bytes.fromhex(header_bytes[1])
        s_ttl = bytes.fromhex(header_bytes[2])  # ok
        s_gas_price = bytes.fromhex(header_bytes[3])
        s_body_hash = bytes.fromhex(header_bytes[4])

        s_dependencies = bytes.fromhex(header_bytes[5])

        s_chain_name = bytes.fromhex(header_bytes[6])

        h.update(s_account + s_time_now + s_ttl + s_gas_price +
                 s_body_hash + s_dependencies + s_chain_name)
        return h.hexdigest()


account = "010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf52f5045ad6c9838d2f"
timestamp = "123"
ttl = 30
gas_price = 1
body_hash = "557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67"
dependencies = "00"
chain_name = "casper-test"
a = DeployHeader(account, timestamp, ttl, gas_price,
                 body_hash, dependencies, chain_name)
print("hash=>")
print(a.byteHash())
