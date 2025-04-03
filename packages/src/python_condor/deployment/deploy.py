from hashlib import blake2b

from ..constants import JsonName, AlgoKind
from .deploy_header import DeployHeader
from .session_contract_hash import SessionContractHash
from .session_contract_name import SessionContractName
from .session_module_bytes import SessionModuleBytes
from .session_package_hash import SessionPackageHash
from .session_package_name import SessionPackageName
from .session_payment import SessionPayment
from ..keys import get_key_pair_from_pem_file, get_signature, KeyAlgorithm

JSONNAME = JsonName()
PREFIX = AlgoKind()


class Deploy:
    def __init__(self, header: DeployHeader, payment: SessionPayment, session: SessionModuleBytes | SessionContractHash | SessionPackageHash | SessionContractName | SessionPackageName, signers_keypaths_algo: list[(str, KeyAlgorithm)]):
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
