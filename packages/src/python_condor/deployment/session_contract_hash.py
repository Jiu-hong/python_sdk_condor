# StoredContractByHash serializes such that the first byte within
# the serialized buffer is 1u8. This is followed by the byte representation
# of the remaining fields.


import re

from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU512
from python_condor.cl_values.cl_string import CLString

from python_condor.constants.cons_jsonname import JsonName
from python_condor.deployment.deploy_name_arg import DeployNamedArg
from python_condor.utils import serialize_string


JSONNAME = JsonName()


class SessionContractHash:
    def __init__(self, contract_hash, entrypoint, runtime_args):
        # check contract_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(contract_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "contract-hash should only contain alphabet and number(64 length)")
        # check entrypoint
        if not isinstance(entrypoint, str):
            raise TypeError("The entrypoint should be of type str.")
        self.contract_hash = contract_hash
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag StoredContractByHashTag = '01'
        StoredContractByHashTag = int(1).to_bytes()

        result = StoredContractByHashTag + bytes.fromhex(self.contract_hash) + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDCONTRACTBYHASH: {
                JSONNAME.HASH: self.contract_hash,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result


# def serialize_payment(amount):
#     ModuleBytesTag = '00'
#     # # modulebytes 0 -> '00000000'
#     result = ModuleBytesTag + \
#         '00000000' + \
#         NamedArg({"amount": CLU512(amount)}).serialize()
#     return result


# def serialize_stored_contract(contract_hash, entrypoint, runtime_args):
#     StoredContractByHashTag = '01'
#     result = StoredContractByHashTag + contract_hash + \
#         CLString(entrypoint).serialize().hex() + \
#         NamedArg(runtime_args).serialize()
#     return result


# def serialize_stored_name(contract_name, entrypoint, runtime_args):
#     StoredContractByNameTag = '02'
#     result = StoredContractByNameTag + serialize_string(contract_name) + \
#         CLString(entrypoint).serialize().hex() + \
#         NamedArg(runtime_args).serialize()
#     return result


# contract_hash = "16def1f26e22235bfb8d58fa1fcea580a9f1eba68706a7d88bee1c659006a01d"
# entrypoint = "store_key"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}

# a = serialize_stored_contract(contract_hash, entrypoint, runtime_args)
# print(a)


# def hash_body(session_hexstring, payment_hexstring):
#     h = blake2b(digest_size=32)
#     session_bytes = bytes.fromhex(session_hexstring)
#     payment_bytes = bytes.fromhex(payment_hexstring)
#     h.update(payment_bytes + session_bytes)
#     return h.hexdigest()


# # session part
# contract_hash = "16def1f26e22235bfb8d58fa1fcea580a9f1eba68706a7d88bee1c659006a01d"
# entrypoint = "store_key"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
# session_hexstring = serialize_stored_contract(
#     contract_hash, entrypoint, runtime_args)
# # payment part
# payment_hexstring = serialize_payment(3000000000)
# # print("body_hash:")
# # print(hash_body(payment_hexstring, session_hexstring))
# # print(hash_body(session_hexstring, payment_hexstring))
# # expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
# #        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
