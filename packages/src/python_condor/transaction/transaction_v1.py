from hashlib import blake2b

from ..constants import JsonName, AlgoKind
from ..keys import get_key_pair_from_pem_file, get_signature, KeyAlgorithm
from .transaction_v1_payload import TransactionV1Payload


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
