from hashlib import blake2b

from ..constants import JsonName, AlgoKind
from ..keys import get_key_pair_from_pem_file, get_signature, KeyAlgorithm
from .transaction_v1_payload import TransactionV1Payload
from ..keys.ecc_secp256k1 import get_signature as get_signature_secp256k1, get_key_pair_from_pem_file as get_key_pair_from_pem_file_secp256k1
from ..keys.ecc_ed25519 import get_signature as get_signature_ed25519, get_key_pair_from_pem_file as get_key_pair_from_pem_file_ed25519


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
        transaction_hash_here = transaction_hash
        for (signer_keypath, algo) in self.signers_keypaths_algo:

            # add prefix "01" or "02"
            if algo == KeyAlgorithm.ED25519:
                (PrivateKeyBytes, PublicKeyBytes) = get_key_pair_from_pem_file_ed25519(
                    signer_keypath)
                print("transaction_hash_here in ED25519:", transaction_hash_here)
                sig = PREFIX.ED25519 + get_signature_ed25519(bytes.fromhex(
                    transaction_hash_here),  algo, PrivateKeyBytes).hex()
            else:
                (PrivateKeyBytes, PublicKeyBytes) = get_key_pair_from_pem_file_secp256k1(
                    signer_keypath)

                print("transaction_hash_here in SECP256K1:",
                      transaction_hash_here)
                sig = PREFIX.SECP256K1 + get_signature_secp256k1(bytes.fromhex(
                    transaction_hash_here), PrivateKeyBytes).hex()
            approval = {}
            approval[JSONNAME.SIGNER] = "02"+PublicKeyBytes.hex()
            approval[JSONNAME.SIGNATURE] = sig
            approval_list.append(approval)
        approvals = {JSONNAME.APPROVALS: approval_list}
        # hash
        hash = {JSONNAME.HASH: transaction_hash_here}
        # payload
        payload = self.payload.to_json()

        result = {JSONNAME.TRANSACTION: {
            JSONNAME.VERSION1: {**hash, **payload, **approvals}}}
        return result
