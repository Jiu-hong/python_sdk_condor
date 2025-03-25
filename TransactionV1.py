from hashlib import blake2b

from PricingMode import PricingMode
from TransactionEntryPoint import TransactionEntryPoint
from TransactionScheduling import TransactionScheduling
from TransactionTarget import TransactionTarget
from TransactionV1Payload import TransactionV1Payload
from cl_number import CLU8
from cl_string import CLString


class TransactionV1:
    def __init__(self, payload: TransactionV1Payload):
        self.payload = payload

    def byteHash(self):
        payload_bytes = self.payload.to_bytes()
        h = blake2b(digest_size=32)
        h.update(payload_bytes)
        return h.hexdigest()


# args = {"arg1": CLU8(123), "arg2": CLString("Hello")}
# transactionTarget = TransactionTarget("stored", "InvocableEntity",
#                                       "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# entrypoint = TransactionEntryPoint("Custom", "apple")
# scheduling = TransactionScheduling()
# initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
# pricing_mode = PricingMode("Classic", 123)

# payload = TransactionV1Payload(args, transactionTarget,
#                                entrypoint, scheduling, initiatorAddr, pricing_mode, "casper-integration")
# transaction = TransactionV1(payload)
# print("transaction.hash:", transaction.byteHash())

#
f = open("wasm", "r")
module_bytes = f.read()
target2 = TransactionTarget("session", module_bytes, True)
entrypoint = TransactionEntryPoint("Call")
scheduling = TransactionScheduling()
pricing_mode = PricingMode("Classic", 2500000000, 2)
args = {}
initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
payload = TransactionV1Payload(args, target2,
                               entrypoint, scheduling, initiatorAddr, pricing_mode, "integration-test")
transaction = TransactionV1(payload)
print("transaction.hash:", transaction.byteHash())
