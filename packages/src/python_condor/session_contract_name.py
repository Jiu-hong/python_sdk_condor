# StoredContractByHash serializes such that the first byte within
# the serialized buffer is 1u8. This is followed by the byte representation
# of the remaining fields.


from hashlib import blake2b

from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU512
from python_condor.cl_values.cl_string import CLString
from python_condor.deploy_name_arg import NamedArg
from python_condor.utils import serialize_string


def serialize_payment(amount):
    ModuleBytesTag = '00'
    # # modulebytes 0 -> '00000000'
    result = ModuleBytesTag + \
        '00000000' + \
        NamedArg({"amount": CLU512(amount)}).serialize()
    return result


def serialize_stored_name(contract_name, entrypoint, runtime_args):
    StoredContractByNameTag = '02'
    result = StoredContractByNameTag + serialize_string(contract_name).hex() + \
        CLString(entrypoint).serialize().hex() + \
        NamedArg(runtime_args).serialize()
    return result


def hash_body(session_hexstring, payment_hexstring):
    h = blake2b(digest_size=32)
    session_bytes = bytes.fromhex(session_hexstring)
    payment_bytes = bytes.fromhex(payment_hexstring)
    h.update(payment_bytes + session_bytes)
    return h.hexdigest()


# session part
contract_name = "apple_contract"
entrypoint = "apple"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
runtime_args = {}
session_hexstring = serialize_stored_name(
    contract_name, entrypoint, runtime_args)
# payment part
payment_hexstring = serialize_payment(2500000000)
print("body_hash:")
# print(hash_body(payment_hexstring, session_hexstring))
print(hash_body(session_hexstring, payment_hexstring))
# expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
#        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
