# StoredContractByHash serializes such that the first byte within
# the serialized buffer is 1u8. This is followed by the byte representation
# of the remaining fields.


from hashlib import blake2b

from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU512
from python_condor.cl_values.cl_string import CLString
from python_condor.deploy_name_arg import NamedArg
from python_condor.utils import serialize_string


class SessionPackageHash:
    def __init__(self, package_hash_hex, version, entrypoint, runtime_args: NamedArg):
        self.package_hash_hex = package_hash_hex
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = runtime_args

    def to_bytes(self):
        StoredPackageByNameTag = '03'

        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                self.version.to_bytes(4, byteorder='little')
        result = StoredPackageByNameTag + self.package_hash_hex + \
            version_bytes.hex() + \
            CLString(self.entrypoint).serialize().hex() + \
            NamedArg(self.runtime_args).serialize()
        return result

    def to_json(self):
        result = {"session": {
            "StoredVersionedContractByHash": {
                "hash": self.package_hash_hex,
                "version": self.version,
                "entry_point": self.entrypoint,
                "args": self.runtime_args.to_json()
            }
        }}
        return result


class SessionPayment:
    def __init__(self, payment_amount):
        self.payment_amount = payment_amount

    def to_bytes(self):
        ModuleBytesTag = '00'
        # # modulebytes 0 -> '00000000'
        result = ModuleBytesTag + \
            '00000000' + \
            NamedArg({"amount": CLU512(self.payment_amount)}).serialize()
        return result

    def to_json(self):
        result = {"payment": {
            "ModuleBytes": {
                "module_bytes": "",
                "args": NamedArg({"amount": CLU512(self.payment_amount)}).to_json()
            }
        }}
        return result


def hash_body(session_hexstring, payment_hexstring):
    h = blake2b(digest_size=32)
    session_bytes = bytes.fromhex(session_hexstring)
    payment_bytes = bytes.fromhex(payment_hexstring)
    h.update(payment_bytes + session_bytes)
    return h.hexdigest()


# session part
package_hash_hex = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
entrypoint = "apple"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
runtime_args = {}
session_packagehash = SessionPackageHash(
    package_hash_hex, None, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()
# session_hexstring = serialize_package_hash(
#     package_hash_hex, None, entrypoint, runtime_args)
# payment part
payment_hexstring = SessionPayment(2500000000).to_bytes()
print("body_hash:")
# print(hash_body(payment_hexstring, session_hexstring))
print(hash_body(session_hexstring, payment_hexstring))
# expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
#        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
