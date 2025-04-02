from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU512
from python_condor.cl_values.cl_string import CLString
# from python_condor.deploy_name_arg import NamedArg
from python_condor.constants.cons_jsonname import JsonName
from python_condor.deployment.deploy_name_arg import DeployNamedArg
from python_condor.utils import serialize_string

JSONNAME = JsonName()


class SessionPackageName:
    def __init__(self, package_name, version, entrypoint, runtime_args):
        self.package_name = package_name
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        # tag
        StoredPackageByNameTag = int(4).to_bytes()

        # version
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                self.version.to_bytes(4, byteorder='little')

        result = StoredPackageByNameTag + serialize_string(self.package_name) + \
            version_bytes + \
            serialize_string(self.entrypoint) + \
            self.runtime_args.serialize()

        return result

    def to_json(self):
        result = {JSONNAME.SESSION: {
            JSONNAME.STOREDVERSIONEDCONTRACTBYNAME: {
                JSONNAME.NAME: self.package_name,
                JSONNAME.VERSION: self.version,
                JSONNAME.ENTRYPOINT: self.entrypoint,
                JSONNAME.ARGS: self.runtime_args.to_json()
            }
        }}
        return result


# session part
package_name = "my_hash"
entrypoint = "apple"
# runtime_args = {"name": CLString("my_public_key"), "value": CLKey(
#     "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")}
# runtime_args = {}
# session_hexstring = serialize_package_name(
#     package_name, None, entrypoint, runtime_args)
# # payment part
# payment_hexstring = serialize_payment(2500000000)
# print("body_hash:")
# print(hash_body(payment_hexstring, session_hexstring))
# print(hash_body(session_hexstring, payment_hexstring))
# expect 557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
#        557c9c0149aeb4fc886e0f9d361ef23103a12c86dd04a81845d178d09d872e67
