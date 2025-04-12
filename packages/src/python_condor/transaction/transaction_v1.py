"""
Transaction V1 module for handling Casper version 1 transactions.

This module provides functionality for creating and managing version 1 transactions in the Casper network.
It handles:
- Transaction creation with payload and signers
- Transaction hashing using BLAKE2b
- Transaction signing with multiple signers
- JSON serialization of transactions
"""

from hashlib import blake2b
from typing import List, Tuple, Dict, Any

from ..constants import JsonName, AlgoKind
from ..keys import get_key_pair_from_pem_file, get_signature, KeyAlgorithm
from .transaction_v1_payload import TransactionV1Payload


# Constants for JSON field names
JSONNAME = JsonName()
PREFIX = AlgoKind()


class TransactionV1:
    """
    Represents a version 1 transaction in the Casper network.

    A transaction consists of:
    - A payload containing the transaction details
    - A list of signers with their key paths and algorithms
    - A transaction hash
    - Signatures from all signers

    Attributes:
        payload (TransactionV1Payload): The transaction payload
        signers_keypaths_algo (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
    """

    def __init__(self, payload: TransactionV1Payload, signers_keypaths_algo: List[Tuple[str, KeyAlgorithm]]):
        """
        Initialize a version 1 transaction.

        Args:
            payload (TransactionV1Payload): The transaction payload
            signers_keypaths_algo (List[Tuple[str, KeyAlgorithm]]): List of signers with their key paths and algorithms
        """
        self.payload = payload
        self.signers_keypaths_algo = signers_keypaths_algo

    def byteHash(self) -> str:
        """
        Calculate the BLAKE2b hash of the transaction payload.

        Returns:
            str: The hexadecimal representation of the transaction hash
        """
        payload_bytes = self.payload.to_bytes()
        h = blake2b(digest_size=32)
        h.update(payload_bytes)
        return h.hexdigest()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the transaction to a JSON representation.

        The JSON includes:
        - Transaction hash
        - Transaction payload
        - Approvals (signatures) from all signers

        Returns:
            Dict[str, Any]: The JSON representation of the transaction
        """
        # Calculate transaction hash
        transaction_hash = self.byteHash()

        # Get signatures from all signers
        approval_list = []
        for signer_keypath, algo in self.signers_keypaths_algo:
            # Get key pair from PEM file
            private_key_bytes, public_key_bytes = get_key_pair_from_pem_file(
                signer_keypath, algo)

            # Sign the transaction hash
            signature = get_signature(
                bytes.fromhex(transaction_hash),
                algo,
                private_key_bytes
            ).hex()

            # Create approval entry
            approval = {
                JSONNAME.SIGNER: public_key_bytes.hex(),
                JSONNAME.SIGNATURE: signature
            }
            approval_list.append(approval)

        # Construct the final JSON
        approvals = {JSONNAME.APPROVALS: approval_list}
        hash_data = {JSONNAME.HASH: transaction_hash}
        payload_data = self.payload.to_json()

        return {
            JSONNAME.TRANSACTION: {
                JSONNAME.VERSION1: {
                    **hash_data,
                    **payload_data,
                    **approvals
                }
            }
        }
