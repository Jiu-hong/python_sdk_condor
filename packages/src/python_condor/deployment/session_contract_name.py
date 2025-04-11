"""Session contract name module.

This module provides functionality for handling contract name sessions in Casper network deployments.
"""

from typing import Any, Dict

from ..constants import JsonName
from ..utils import serialize_string
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionContractName:
    """Class for managing contract name sessions.

    This class handles the creation and management of sessions that use contract names
    in Casper network deployments.
    """

    def __init__(
        self,
        contract_name: str,
        entrypoint: str,
        runtime_args: Dict[str, Any]
    ):
        """Initialize a contract name session.

        Args:
            contract_name: The name of the contract.
            entrypoint: The entrypoint function name.
            runtime_args: Dictionary of runtime arguments.

        Raises:
            ValueError: If contract_name or entrypoint is empty.
        """
        if contract_name == "":
            raise ValueError("The contract name shouldn't be empty.")
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")

        self.contract_name = contract_name
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        """Convert the session to bytes.

        Returns:
            Bytes representation of the session.
        """
        # Tag StoredContractByNameTag = '02'
        stored_contract_by_name_tag = int(2).to_bytes()

        return (
            stored_contract_by_name_tag +
            serialize_string(self.contract_name) +
            serialize_string(self.entrypoint) +
            self.runtime_args.serialize()
        )

    def to_json(self) -> Dict[str, Any]:
        """Convert the session to JSON format.

        Returns:
            Dictionary containing the session in JSON format.
        """
        return {
            JSONNAME.DEPLOY_SESSION: {
                JSONNAME.STOREDCONTRACTBYNAME: {
                    JSONNAME.NAME: self.contract_name,
                    JSONNAME.ENTRYPOINT: self.entrypoint,
                    JSONNAME.ARGS: self.runtime_args.to_json()
                }
            }
        }
