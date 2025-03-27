from hashlib import blake2b
import json
from cryptography.hazmat.primitives.asymmetric import ed25519
from PricingMode import PricingMode
from TransactionEntryPoint import TransactionEntryPoint
from TransactionScheduling import TransactionScheduling
from TransactionTarget import TransactionTarget
from TransactionV1Payload import TransactionV1Payload
from cl_list import CLList
from cl_map import CLMap
from cl_number import CLU32, CLU512, CLU64, CLU8
from cl_option import CLOption
from cl_publickey import CLPublicKey
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
# path = "/Users/jh/mywork/contract/accountaccess/contract/target/wasm32-unknown-unknown/release/contract.wasm"
# f = open("wasm", "r")
# f = open(path, "r")
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

# args = {"target": CLPublicKey("01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"), "amount": CLU512(2500000000),
#         "id": CLOption(CLU64(0))}
# args = {"id": CLOption(CLU64(0)), "target": CLPublicKey("01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"), "amount": CLU512(2500000000),
#         }
# args = {"arg1": CLList([CLOption(CLU32(1)), CLOption(
#     CLU32(2)), CLOption(CLU32(3)), CLOption(CLU32(3)), CLOption(CLU32(3))])}
args = {
    "arg1": CLMap({CLU8(3): CLString("Jim"), CLU8(
        2): CLString("Jack"), CLU8(4): CLString("Jane"), CLU8(1): CLString("Jill")})
}
scheduling = TransactionScheduling()
print("scheduling to_bytes()", scheduling.to_bytes().hex())
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"

pricing_mode = PricingMode("Classic", 2500000000)
print("pricing_mode to_bytes():", pricing_mode.to_bytes().hex())

target1 = TransactionTarget("stored", "InvocableEntity",
                            "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")
print("entrypoint1 bytes is:", entrypoint1.to_bytes().hex())

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")
# print("payload bytes is:", payload.to_bytes().hex())

transaction = TransactionV1(payload, "secret_key.pem")
print("transaction_to_json:", json.dumps(transaction.to_json()))
