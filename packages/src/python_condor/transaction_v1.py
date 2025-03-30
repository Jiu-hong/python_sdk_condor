from hashlib import blake2b
import json
from cryptography.hazmat.primitives.asymmetric import ed25519
from result import Err, Ok
from .cl_values import CLURef, CLMap, CLList, CLU32, CLU512, CLU64, CLU8, CLBool, CLOption, CLString, CLResult, CLTuple1, CLTuple2, CLTuple3, CLPublicKey


from .keys import KeyAlgorithm, get_key_pair_from_pem_file, get_signature

from .pricing_mode import PricingMode
from .transaction_entry_point import TransactionEntryPoint
from .transaction_scheduling import TransactionScheduling
from .transaction_target import TransactionTarget
from .transaction_v1_payload import TransactionV1Payload

from .constants import RESULTHOLDER, JsonName, AlgoKind


JSONNAME = JsonName()
PREFIX = AlgoKind()


class TransactionV1:
    def __init__(self, payload: TransactionV1Payload, signers_keypaths_algo: list[(str, KeyAlgorithm)]):
        self.payload = payload
        self.signers_keypaths_algo = signers_keypaths_algo

    def byteHash(self):
        payload_bytes = self.payload.to_bytes()
        h = blake2b(digest_size=32)
        h.update(payload_bytes)
        return h.hexdigest()

    def to_json(self):
        # get hash
        transaction_hash = self.byteHash()
        # get signature
        approval_list = []
        for (signer_keypath, algo) in self.signers_keypaths_algo:
            (PrivateKeyBytes, PublicKeyBytes) = get_key_pair_from_pem_file(
                signer_keypath, algo)
            # add prefix "01" or "02"
            if algo == KeyAlgorithm.ED25519:
                sig = PREFIX.ED25519 + get_signature(bytes.fromhex(
                    transaction_hash),  algo, PrivateKeyBytes).hex()
            else:
                sig = PREFIX.SECP256K1 + get_signature(bytes.fromhex(
                    transaction_hash),  algo, PrivateKeyBytes).hex()
            approval = {}
            approval[JSONNAME.SIGNER] = PublicKeyBytes.hex()
            approval[JSONNAME.SIGNATURE] = sig
            approval_list.append(approval)
        approvals = {JSONNAME.APPROVALS: approval_list}
        # hash
        hash = {JSONNAME.HASH: transaction_hash}
        # payload
        payload = self.payload.to_json()

        result = {JSONNAME.TRANSACTION: {
            JSONNAME.VERSION1: {**hash, **payload, **approvals}}}
        return result


# key_pair = get_key_pair_from_pem_file("secret_key.pem", 1)
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
# # f = open(path, "r")
# print("hello world==")
# module_bytes = f.read()
# print("type of module_bytes:", type(module_bytes))
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
arg2 = CLResult(
    Ok(CLString("ABC")), Err(CLU32(RESULTHOLDER())), True)
a1 = CLResult(Ok(CLOption(CLTuple2((CLString("hello"), CLU512(123))))),
              Err(CLString(RESULTHOLDER())), True)
a2 = CLResult(Ok(CLOption(CLTuple2((CLString(RESULTHOLDER()), CLU512(123))))),
              Err(CLString("error Hello")), False)
a3 = CLResult(Ok(CLOption(CLTuple2((CLString("world"), CLU512(123))))),
              Err(CLString(RESULTHOLDER())), True)

c = CLList([a1, a2, a3])
args = {
    # "arg1": CLMap({CLU8(3): CLString("Jim"), CLU8(
    #     2): CLString("Jack"), CLU8(4): CLString("Jane"), CLU8(1): CLString("Jill")}),
    "arg2": c
}


scheduling = TransactionScheduling()
print("scheduling to_bytes()", scheduling.to_bytes().hex())
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
# initiatorAddr = "0203b3eb6ae40e21a9436b956aa8a3af5b7336340cfc6ec035db7aec6a4ff1cda22f"
pricing_mode = PricingMode("Classic", 2500000000)
print("pricing_mode to_bytes():", pricing_mode.to_bytes().hex())

target1 = TransactionTarget("VmCasperV1", "stored", "InvocableEntity",
                            "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")
print("entrypoint1 bytes is:", entrypoint1.to_bytes().hex())

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")
# print("payload bytes is:", payload.to_bytes().hex())

# transaction = TransactionV1(
#     payload, [("secret_key.pem", KeyAlgorithm.ED25519)])
# # transaction = TransactionV1(
# #     payload, [("secret_key2.pem", KeyAlgorithm.SECP256K1)])
# print("transaction_to_json:", json.dumps(transaction.to_json()))

# expected:
# 0600000000000000000001003600000002003e00000003004600000004005a00000005008500000049010000020000000000000000000100010000002200000000017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f55d486fd09501000040771b000000000010000000696e746567726174696f6e2d746573740400000000000000000001000100000002000900000003000a0000000b0000000000d0ed902e00000001010400000000001c0000000001000000
# 0400000061726732080000000103000000414243100a04
# 01005f000000030000000000000000000100010000000200360000004500000001020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee601000000000000000000010000000002001e000000020000000000000000000100010000000a0000000105000000746573743203000f000000010000000000000000000100000000
# # actual:
# 0600000000000000000001003600000002003e00000003004600000004005a00000005008500000049010000020000000000000000000100010000002200000000017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f55d486fd09501000040771b000000000010000000696e746567726174696f6e2d746573740400000000000000000001000100000002000900000003000a0000000b0000000000f902950000000001010400000000001c0000000001000000
# 0400000061726732080000000103000000414243100a04
# 01005f000000030000000000000000000100010000000200360000004500000001020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee601000000000000000000010000000002001e000000020000000000000000000100010000000a0000000105000000746573743203000f000000010000000000000000000100000000

args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")))}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 200000000000)
target1 = TransactionTarget("VmCasperV1", "stored", "InvocableEntityAlias",
                            "accesscontract")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")

# transaction = TransactionV1(payload, "secret_key.pem")

# print("transaction_to_json1:", json.dumps(transaction.to_json()))
