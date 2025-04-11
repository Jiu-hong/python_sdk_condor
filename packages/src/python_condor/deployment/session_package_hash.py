"""Session package hash module.

This module provides functionality for handling package hash sessions in Casper network deployments.
"""

import re
from typing import Any, Dict, Optional, Union

from ..constants import JsonName
from ..utils import serialize_string
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionPackageHash:
    """Class for managing package hash sessions.

    This class handles the creation and management of sessions that use package hashes
    in Casper network deployments.
    """

    def __init__(
        self,
        package_hash: str,
        version: Optional[int],
        entrypoint: str,
        runtime_args: Dict[str, Any]
    ):
        """Initialize a package hash session.

        Args:
            package_hash: The hash of the package (64-character hex string).
            version: Optional version number of the package.
            entrypoint: The entrypoint function name.
            runtime_args: Dictionary of runtime arguments.

        Raises:
            ValueError: If package_hash is invalid or entrypoint is empty.
        """
        # Check package_hash
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(package_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "package-hash should only contain alphabet and number(64 length)"
            )

        # Check entrypoint
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")

        self.package_hash = package_hash
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        """Convert the session to bytes.

        Returns:
            Bytes representation of the session.
        """
        # Tag StoredPackageByHashTag = '03'
        stored_package_by_hash_tag = int(3).to_bytes()

        # Version handling
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = (
                int(1).to_bytes() +
                self.version.to_bytes(4, byteorder='little')
            )

        return (
            stored_package_by_hash_tag +
            bytes.fromhex(self.package_hash) +
            version_bytes +
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
                JSONNAME.STOREDVERSIONEDCONTRACTBYHASH: {
                    JSONNAME.HASH: self.package_hash,
                    JSONNAME.VERSION: self.version,
                    JSONNAME.ENTRYPOINT: self.entrypoint,
                    JSONNAME.ARGS: self.runtime_args.to_json()
                }
            }
        }
