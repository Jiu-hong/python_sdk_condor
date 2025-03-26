from hashlib import blake2b
import json

from PricingMode import PricingMode
from TransactionEntryPoint import TransactionEntryPoint
from TransactionScheduling import TransactionScheduling
from TransactionTarget import TransactionTarget
from TransactionV1Payload import TransactionV1Payload
from cl_number import CLU8
from cl_string import CLString
from keys import get_signature_from_pem_file


class TransactionV1:
    def __init__(self, payload: TransactionV1Payload, signer):
        self.payload = payload
        self.signer = signer

    def byteHash(self):
        payload_bytes = self.payload.to_bytes()
        h = blake2b(digest_size=32)
        h.update(payload_bytes)
        return h.hexdigest()

    def to_json(self):
        Prefix_ed25519 = '01'
        transaction_hash = self.byteHash()
        sig = Prefix_ed25519 + get_signature_from_pem_file(bytes.fromhex(
            transaction_hash), "secret_key.pem").hex()
        approval = {}
        approval["signer"] = self.signer
        approval["signature"] = sig
        approvals = {"approvals": [approval]}
        hash = {"hash": transaction_hash}
        payload = self.payload.to_json()

        result = {"transaction": {
            "Version1": {**hash, **payload, **approvals}}}
        return result


# print("sig is:", '01'+sig.hex())

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
target1 = TransactionTarget("stored", "InvocableEntity",
                            "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")

entrypoint2 = TransactionEntryPoint("Call")
entrypoint1 = TransactionEntryPoint("Custom", "test2")
scheduling = TransactionScheduling()
pricing_mode = PricingMode("Classic", 200000000000)
args = {}
initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")
transaction = TransactionV1(payload, initiatorAddr)
# print("transaction.hash:", transaction.byteHash())
# print("transaction_to_json:", json.dumps(transaction.to_json()))

args = {}
transactionTarget2 = TransactionTarget("session", module_bytes, True)
entrypoint2 = TransactionEntryPoint("Call")
transaction_v1_payload = TransactionV1Payload(args, transactionTarget2,
                                              entrypoint2, scheduling, initiatorAddr, pricing_mode, "integration-test")
transaction = TransactionV1(transaction_v1_payload, initiatorAddr)
print("transaction_to_json:", json.dumps(transaction.to_json()))
