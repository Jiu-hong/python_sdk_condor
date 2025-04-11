"""Deploy module for creating and managing Casper network deployments.

This module provides functionality for creating and managing deployments on the Casper network,
including header management, payment handling, and session configuration.
"""

from hashlib import blake2b
from typing import List, Tuple, Union

from ..constants import JsonName, AlgoKind
from ..keys import KeyAlgorithm, get_key_pair_from_pem_file, get_signature
from .deploy_header import DeployHeader
from .session_contract_hash import SessionContractHash
from .session_contract_name import SessionContractName
from .session_module_bytes import SessionModuleBytes
from .session_package_hash import SessionPackageHash
from .session_package_name import SessionPackageName
from .session_payment import SessionPayment


JSONNAME = JsonName()
PREFIX = AlgoKind()


class Deploy:
    """Class for managing Casper network deployments.

    This class handles the creation and management of deployments on the Casper network,
    including header management, payment handling, and session configuration.
    """

    def __init__(
        self,
        header: DeployHeader,
        payment: SessionPayment,
        session: Union[
            SessionModuleBytes,
            SessionContractHash,
            SessionPackageHash,
            SessionContractName,
            SessionPackageName
        ],
        signers_keypaths_algo: List[Tuple[str, KeyAlgorithm]]
    ):
        """Initialize a new deployment.

        Args:
            header: The deployment header containing metadata.
            payment: The payment configuration for the deployment.
            session: The session configuration (module bytes, contract hash, or package hash).
            signers_keypaths_algo: List of tuples containing signer key paths and algorithms.
        """
        self.header = header
        self.payment = payment
        self.session = session
        self.signers_keypaths_algo = signers_keypaths_algo

    def generate_body_hash(self) -> None:
        """Generate and add the body hash to the deployment header.

        The body hash is calculated using the payment and session bytes.
        """
        h = blake2b(digest_size=32)
        session_bytes = self.session.to_bytes()
        payment_bytes = self.payment.to_bytes()
        h.update(payment_bytes + session_bytes)

        # Update the header with the body hash
        self.header.add_body_hash(h.hexdigest())

    def get_approvals(self, deploy_hash: str) -> dict:
        """Generate approvals for the deployment.

        Args:
            deploy_hash: The hash of the deployment.

        Returns:
            A dictionary containing the approvals for the deployment.
        """
        approval_list = []
        for signer_keypath, algo in self.signers_keypaths_algo:
            private_key_bytes, public_key_bytes = get_key_pair_from_pem_file(
                signer_keypath, algo
            )

            # Add prefix "01" or "02"
            sig = get_signature(
                bytes.fromhex(deploy_hash),
                algo,
                private_key_bytes
            ).hex()

            approval = {
                JSONNAME.SIGNER: public_key_bytes.hex(),
                JSONNAME.SIGNATURE: sig
            }
            approval_list.append(approval)

        return {JSONNAME.APPROVALS: approval_list}

    def to_json(self) -> dict:
        """Convert the deployment to JSON format.

        Returns:
            A dictionary containing the deployment in JSON format.
        """
        # Add body hash to the header
        self.generate_body_hash()

        # Get deploy hash
        deploy_hash = self.header.byteHash()

        # Get approvals
        approvals = self.get_approvals(deploy_hash)

        return {
            JSONNAME.DEPLOY: {
                JSONNAME.HASH: deploy_hash,
                **self.header.to_json(),
                **self.payment.to_json(),
                **self.session.to_json(),
                **approvals
            }
        }
