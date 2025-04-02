from datetime import datetime, timezone
from hashlib import blake2b
from time import time

from python_condor.cl_values.cl_number import CLU64
from python_condor.cl_values.cl_publickey import CLPublicKey
from python_condor.cl_values.cl_string import CLString
from python_condor.deploy_header import DeployHeader
from python_condor.session_package_hash import SessionPackageHash, SessionPayment


class Deploy:
    def __init__(self, header: DeployHeader, payment: SessionPayment, session: SessionPackageHash, approvals):

        self.header = header
        self.payment = payment
        self.session = session
        self.approvals = approvals

    def generate_body_hash(self):
        # def hash_body(session_hexstring, payment_hexstring):
        h = blake2b(digest_size=32)
        session_bytes = bytes.fromhex(self.session.to_bytes())
        payment_bytes = bytes.fromhex(self.payment.to_bytes())
        h.update(payment_bytes + session_bytes)
        self.header.add_body_hash(h.hexdigest())

    def to_json(self):
        self.generate_body_hash()  # add body hash to the header
        deploy_hash = self.header.byteHash()
        result = {}
        result["deploy"] = {
            "hash": deploy_hash,
            "header": self.header.to_json(),
            "payment": self.payment.to_json(),
            "session": self.session.to_json(),
            "approvals": self.approvals.to_json()
        }


account = "0203c1e1349b0a5b34246bce27a68de90d842ace31221a363007e483301977611dfa"
timestamp = "123"
ttl = 30
gas_price = 3
body_hash = "889135da6f70c3e5832a43b358a4b634df9056d4f55c9486cc92249d2c3e386d"
dependencies = "00"
chain_name = "casper-test"
header = DeployHeader(
    account, timestamp, ttl, gas_price, dependencies, chain_name)

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
payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [])
