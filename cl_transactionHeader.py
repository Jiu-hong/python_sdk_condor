from datetime import datetime, timezone
from hashlib import blake2b
from time import time
from cl_number import CLU32, CLU64, CLU8, CLBool
from cl_option import CLOption
from cl_publickey import CLPublicKey
from cl_string import CLString
from name_arg import NamedArg
from table import CalltableSerialization


# to_bytes to do
class TransactionV1Header:
    def __init__(self, chain_name,  body_hash,  pricing_mode, initiator_addr, payment_amount=None, gas_price_tolerance=1,  now=datetime.now(timezone.utc), ttl=30, ):
        self.chain_name = CLString(chain_name)
        # CLU64(int(time() * 1000)).serialize() // ??
        self.time = now
        self.ttl = ttl
        self.body_hash = body_hash
        self.pricing_mode = pricing_mode
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.initiator_addr = initiator_addr

    def serialize(self):
        return self.chain_name.serialize() \
            + CLU64(int(self.time.timestamp() * 1000)).serialize() \
            + CLU64(int(self.ttl) * 60000).serialize() \
            + self.body_hash \
            + PricingMode(self.pricing_mode, self.payment_amount,
                          self.gas_price_tolerance).serialize() \
            + InitiatorAddr(self.initiator_addr).serialize()

    def to_json(self):
        result = {}
        result["payload"] = {
            **InitiatorAddr(self.initiator_addr).to_json(), "timestamp": self.time.replace(
                tzinfo=None).isoformat(timespec='milliseconds')+"Z", "ttl": self.ttl, "chain_name": self.chain_name.value(), **PricingMode(self.pricing_mode, self.payment_amount,
                                                                                                                                           self.gas_price_tolerance).to_json()}
        result["hash"] = self.transaction_hash()
        return result

    def transaction_hash(self):
        header_hex = self.serialize()
        h = blake2b(digest_size=32)
        header_bytes = bytes.fromhex(header_hex)
        h.update(header_bytes)
        return h.hexdigest()


a = TransactionScheduling()
print(a.to_bytes())
