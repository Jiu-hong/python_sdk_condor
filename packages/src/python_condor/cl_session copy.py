# StoredContractByHash serializes such that the first byte within
# the serialized buffer is 1u8. This is followed by the byte representation
# of the remaining fields.


from hashlib import blake2b

from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU512
from python_condor.cl_values.cl_string import CLString
from python_condor.deploy_name_arg import NamedArg


# amount should be decimal motes


# class ExecutableDeployItems:
#     pass


# class ModuleBytes(ExecutableDeployItems):
#     def __init__(self, modulebytes_hex, runtime_args) -> None:
#         self.modulebytes_hex = modulebytes_hex
#         self.runtime_args = runtime_args

#     def serialize(self):
#         executable_deploy_tag = "00"
#         modulebytes_hex = self.modulebytes_hex
#         name_args = NamedArg(self.runtime_args).__serialize__()
#         return executable_deploy_tag + modulebytes_hex + name_args


# class StoredContractByHash(ExecutableDeployItems):
#     def __init__(self, contract_hash_hex, entrypoint, runtime_args) -> None:
#         self.contract_hash_hex = contract_hash_hex
#         self.entrypoint = entrypoint
#         self.runtime_args = runtime_args

#     def serialize(self):
#         executable_deploy_tag = "01"
#         entrypoint = CLString(entrypoint).serialize()
#         name_args = NamedArg(self.runtime_args).__serialize__()
#         result = executable_deploy_tag + self.contract_hash_hex + \
#             entrypoint + name_args
#         return result


# class DeployBody:
#     def __init__(self, name_arg, payment, session):
#         self.name_arg = name_arg
#         self.payment = payment
#         self.session = session
#         if isinstance(self.name_args, NamedArg):
#             raise
#         if isinstance(self.payment, payment):
#             raise
#         if isinstance(self.session, session):
#             raise

#     def hash_body(self):
#         h = blake2b(digest_size=32)
#         payment_bytes = self.serialize(self.payment)
#         session_bytes = self.serialize(self.session)
#         h.update(payment_bytes + session_bytes)
#         return h.hexdigest()


def serialize_payment(amount):
    ModuleBytesTag = '00'
    # # modulebytes 0 -> '00000000'
    result = ModuleBytesTag + \
        '00000000' + \
        NamedArg({"amount": CLU512(amount)}).serialize()
    return result


def serialize_session(contract_hash_hex, entrypoint, runtime_args):
    StoredContractByHashTag = '01'
    result = StoredContractByHashTag + contract_hash_hex + \
        CLString(entrypoint).serialize().hex() + \
        NamedArg(runtime_args).serialize()
    return result


contract_hash_hex = "16def1f26e22235bfb8d58fa1fcea580a9f1eba68706a7d88bee1c659006a01d"
entrypoint = "store_key"
runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
    "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}

a = serialize_session(contract_hash_hex, entrypoint, runtime_args)
print(a)
# expect 0132cdc13a3ba05784f9ed45f07a81a0fd015cafbdff8246759903bb8f7f564d8d0d0000007472616e736665725f66726f6d01000000050000006f776e65720300000002c80107
# actual 0132cdc13a3ba05784f9ed45f07a81a0fd015cafbdff8246759903bb8f7f564d8d0d0000007472616e736665725f66726f6d01000000050000006f776e65720300000002c80107
#   const c = DeployUtil.ExecutableDeployItem.newStoredContractByHash(
#     decodeBase16("32cdc13a3ba05784f9ed45f07a81a0fd015cafbdff8246759903bb8f7f564d8d"),
#     "transfer_from",
#     RuntimeArgs.fromMap({
#       owner: CLValueBuilder.u256(456),
#     })
#   )


def hash_body(session_hexstring, payment_hexstring):
    h = blake2b(digest_size=32)
    session_bytes = bytes.fromhex(session_hexstring)
    payment_bytes = bytes.fromhex(payment_hexstring)
    h.update(payment_bytes + session_bytes)
    return h.hexdigest()


# session part
contract_hash_hex = "16def1f26e22235bfb8d58fa1fcea580a9f1eba68706a7d88bee1c659006a01d"
entrypoint = "store_key"
runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
    "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
session_hexstring = serialize_session(
    contract_hash_hex, entrypoint, runtime_args)
# payment part
payment_hexstring = serialize_payment(3000000000)
print("body_hash:")
# print(hash_body(payment_hexstring, session_hexstring))
print(hash_body(session_hexstring, payment_hexstring))
# expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
#        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
