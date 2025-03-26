from hashlib import blake2b
import json
from cryptography.hazmat.primitives.asymmetric import ed25519
from PricingMode import PricingMode
from TransactionEntryPoint import TransactionEntryPoint
from TransactionScheduling import TransactionScheduling
from TransactionTarget import TransactionTarget
from TransactionV1Payload import TransactionV1Payload
from cl_number import CLU8
from cl_string import CLString
from keys import get_pvk_from_pem_file, get_signature_from_pem_file


class TransactionV1:
    def __init__(self, payload: TransactionV1Payload, keypath):
        self.payload = payload
        self.keypath = keypath

    def byteHash(self):
        payload_bytes = self.payload.to_bytes()
        h = blake2b(digest_size=32)
        h.update(payload_bytes)
        return h.hexdigest()

    def to_json(self):
        PREFIX_ED25519 = '01'
        transaction_hash = self.byteHash()
        print("transaction_hash here:", transaction_hash)
        sig = PREFIX_ED25519 + get_signature_from_pem_file(bytes.fromhex(
            transaction_hash), self.keypath).hex()
        private_key = get_pvk_from_pem_file("secret_key.pem")
        ek25519KeyPair = ed25519.Ed25519PrivateKey.from_private_bytes(
            private_key)
        signer_publickey = '01' + ek25519KeyPair.public_key().public_bytes_raw().hex()
        approval = {}
        approval["signer"] = signer_publickey
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
# f = open("wasm", "r")
# module_bytes = f.read()
# target2 = TransactionTarget("session", module_bytes, True)
# target1 = TransactionTarget("stored", "InvocableEntity",
#                             "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")

# entrypoint2 = TransactionEntryPoint("Call")
# entrypoint1 = TransactionEntryPoint("Custom", "test2")

# pricing_mode = PricingMode("Classic", 200000000000)
# # args = {}
# args = {"arg1": CLU8(123), "arg2": CLString("Hello")}

# payload = TransactionV1Payload(args, target1,
#                                entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")
# transaction = TransactionV1(payload, "secret_key.pem")
# # print("transaction.hash:", transaction.byteHash())
# # print("transaction_to_json:", json.dumps(transaction.to_json()))

args = {}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 200000000000)
target1 = TransactionTarget("stored", "Package",
                            "40ad74eb43330f7fb496d6ea49df990e6583f51a01a7204a17a6217dbeb715d7")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")

transaction = TransactionV1(payload, "secret_key.pem")

print("transaction_to_json:", json.dumps(transaction.to_json()))
