"""Session contract hash module.

This module provides functionality for handling contract hash sessions in Casper network deployments.
"""

import re
from typing import Dict

from ..constants import JsonName
from ..utils import serialize_string
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionContractHash:
    """Class for managing contract hash sessions.

    This class handles the creation and management of sessions that use contract hashes
    in Casper network deployments.
    """

    def __init__(self, contract_hash: str, entrypoint: str, runtime_args: Dict):
        """Initialize a contract hash session.

        Args:
            contract_hash: The hash of the contract (64-character hex string).
            entrypoint: The entrypoint function name.
            runtime_args: Dictionary of runtime arguments.

        Raises:
            ValueError: If contract_hash is invalid or entrypoint is empty.
        """
        # Check contract_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(contract_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "contract-hash should only contain alphabet and number(64 length)"
            )

        # Check entrypoint
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")

        self.contract_hash = contract_hash
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        """Convert the session to bytes.

        Returns:
            Bytes representation of the session.
        """
        # Tag StoredContractByHashTag = '01'
        stored_contract_by_hash_tag = int(1).to_bytes()

        return (
            stored_contract_by_hash_tag +
            bytes.fromhex(self.contract_hash) +
            serialize_string(self.entrypoint) +
            self.runtime_args.serialize()
        )

    def to_json(self) -> Dict:
        """Convert the session to JSON format.

        Returns:
            Dictionary containing the session in JSON format.
        """
        return {
            JSONNAME.DEPLOY_SESSION: {
                JSONNAME.STOREDCONTRACTBYHASH: {
                    JSONNAME.HASH: self.contract_hash,
                    JSONNAME.ENTRYPOINT: self.entrypoint,
                    JSONNAME.ARGS: self.runtime_args.to_json()
                }
            }
        }
