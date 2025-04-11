"""Session module bytes module.

This module provides functionality for handling module bytes sessions in Casper network deployments.
"""

from typing import Any, Dict

from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionModuleBytes:
    """Class for managing module bytes sessions.

    This class handles the creation and management of sessions that use module bytes
    in Casper network deployments.
    """

    def __init__(
        self,
        module_bytes: str,
        runtime_args: Dict[str, Any]
    ):
        """Initialize a module bytes session.

        Args:
            module_bytes: The module bytes in hex string format.
            runtime_args: Dictionary of runtime arguments.
        """
        self.module_bytes = bytes.fromhex(module_bytes)
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        """Convert the session to bytes.

        Returns:
            Bytes representation of the session.
        """
        # Tag ModuleBytesTag = '00'
        module_bytes_tag = int(0).to_bytes()

        # Module bytes length
        module_bytes_length = len(
            self.module_bytes).to_bytes(4, byteorder='little')

        return (
            module_bytes_tag +
            module_bytes_length +
            self.module_bytes +
            self.runtime_args.serialize()
        )

    def to_json(self) -> Dict[str, Any]:
        """Convert the session to JSON format.

        Returns:
            Dictionary containing the session in JSON format.
        """
        return {
            JSONNAME.DEPLOY_SESSION: {
                JSONNAME.MODULEBYTES: {
                    JSONNAME.MODULE_BYTES: self.module_bytes.hex(),
                    JSONNAME.ARGS: self.runtime_args.to_json()
                }
            }
        }
