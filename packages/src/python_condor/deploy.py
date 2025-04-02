from hashlib import blake2b
import json

from python_condor.constants import JsonName, AlgoKind
from python_condor.cl_values.cl_number import CLU256
from python_condor.cl_values.cl_string import CLString
from python_condor.deploy_header import DeployHeader

from python_condor.keys.ecc_types import KeyAlgorithm
from python_condor.session_package_hash import SessionPackageHash, SessionPayment
from python_condor.keys import get_key_pair_from_pem_file, get_signature, KeyAlgorithm

JSONNAME = JsonName()
PREFIX = AlgoKind()


class Deploy:
    def __init__(self, header: DeployHeader, payment: SessionPayment, session: SessionPackageHash, signers_keypaths_algo: list[(str, KeyAlgorithm)]):
        self.header = header
        self.payment = payment
        self.session = session
        self.signers_keypaths_algo = signers_keypaths_algo

    def generate_body_hash(self):
        h = blake2b(digest_size=32)
        session_bytes = self.session.to_bytes()
        payment_bytes = self.payment.to_bytes()
        h.update(payment_bytes + session_bytes)

        # update to header
        self.header.add_body_hash(h.hexdigest())

    def get_approvals(self, deploy_hash):
        approval_list = []
        for (signer_keypath, algo) in self.signers_keypaths_algo:
            (PrivateKeyBytes, PublicKeyBytes) = get_key_pair_from_pem_file(
                signer_keypath, algo)
            # add prefix "01" or "02"
            if algo == KeyAlgorithm.ED25519:
                sig = PREFIX.ED25519 + get_signature(bytes.fromhex(
                    deploy_hash),  algo, PrivateKeyBytes).hex()
            else:
                sig = PREFIX.SECP256K1 + get_signature(bytes.fromhex(
                    deploy_hash),  algo, PrivateKeyBytes).hex()
            approval = {}
            approval[JSONNAME.SIGNER] = PublicKeyBytes.hex()
            approval[JSONNAME.SIGNATURE] = sig
            approval_list.append(approval)
        approvals = {JSONNAME.APPROVALS: approval_list}
        return approvals

    def to_json(self):
        # add body hash to the header
        self.generate_body_hash()
        # get deploy hash
        deploy_hash = self.header.byteHash()
        # get_approvals
        approvals = self.get_approvals(deploy_hash)

        result = {JSONNAME.DEPLOY: {
            JSONNAME.HASH: deploy_hash,
            **self.header.to_json(),
            **self.payment.to_json(),
            **self.session.to_json(),
            **approvals
        }}
        return result


account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
timestamp = "123"
ttl = 30
gas_price = 1
# body_hash = "889135da6f70c3e5832a43b358a4b634df9056d4f55c9486cc92249d2c3e386d"
dependencies = "00"
chain_name = "integration-test"
header = DeployHeader(
    account, chain_name)

package_hash_hex = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
entrypoint = "apple"
runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
# runtime_args = {}
session_packagehash = SessionPackageHash(
    package_hash_hex, None, entrypoint, runtime_args)
session_hexstring = session_packagehash.to_bytes()

payment = SessionPayment(2500000000)
deploy = Deploy(header, payment, session_packagehash, [
                ("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])

a = deploy.to_json()
print("a:", json.dumps(a))
