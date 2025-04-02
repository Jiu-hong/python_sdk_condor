import re
from python_condor.cl_values.cl_number import CLU512

from python_condor.constants.cons_jsonname import JsonName
from python_condor.deployment.deploy_name_arg import DeployNamedArg
from python_condor.utils import serialize_string

JSONNAME = JsonName()


class SessionPackageHash:
    def __init__(self, package_hash, version, entrypoint, runtime_args):
        # check package_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(package_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "package-hash should only contain alphabet and number(64 length)")
        # check entrypoint
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")
        self.package_hash = package_hash
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag
        StoredPackageByHashTag = int(3).to_bytes()

        # version
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                self.version.to_bytes(4, byteorder='little')

        result = StoredPackageByHashTag + bytes.fromhex(self.package_hash) + \
            version_bytes + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDVERSIONEDCONTRACTBYHASH: {
                JSONNAME.HASH: self.package_hash,
                JSONNAME.VERSION: self.version,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result


# def hash_body(session_hexstring, payment_hexstring):
#     h = blake2b(digest_size=32)
#     session_bytes = bytes.fromhex(session_hexstring)
#     payment_bytes = bytes.fromhex(payment_hexstring)
#     h.update(payment_bytes + session_bytes)
#     return h.hexdigest()

# session part
package_hash = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
entrypoint = "apple"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
runtime_args = {}
session_packagehash = SessionPackageHash(
    package_hash, None, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()
# session_hexstring = serialize_package_hash(
#     package_hash, None, entrypoint, runtime_args)
# payment part
# payment_hexstring = SessionPayment(2500000000).to_bytes()
# print("body_hash:")
# print(hash_body(payment_hexstring, session_hexstring))
# print(hash_body(session_hexstring, payment_hexstring))
# expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
#        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
