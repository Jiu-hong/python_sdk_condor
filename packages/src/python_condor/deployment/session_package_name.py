"""Session package name module.

This module provides functionality for handling package name sessions in Casper network deployments.
"""

from typing import Any, Dict, Optional

from ..constants import JsonName
from ..utils import serialize_string
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionPackageName:
    """Class for managing package name sessions.

    This class handles the creation and management of sessions that use package names
    in Casper network deployments. It provides methods for converting sessions to
    bytes and JSON formats, supporting both versioned and unversioned packages.
    """

    def __init__(
        self,
        package_name: str,
        version: Optional[int],
        entrypoint: str,
        runtime_args: Dict[str, Any]
    ) -> None:
        """Initialize a package name session.

        Args:
            package_name: The name of the package.
            version: Optional version number of the package. If None, the latest version is used.
            entrypoint: The entrypoint function name to be called.
            runtime_args: Dictionary of runtime arguments to be passed to the entrypoint.

        Raises:
            ValueError: If package_name or entrypoint is empty.
        """
        if package_name == "":
            raise ValueError("The package name shouldn't be empty.")
        if entrypoint == "":
            raise ValueError("The entrypoint shouldn't be empty.")

        self.package_name = package_name
        self.version = version
        self.entrypoint = entrypoint
        self.runtime_args = DeployNamedArg(runtime_args)

    def to_bytes(self) -> bytes:
        """Convert the session to bytes.

        The bytes representation includes:
        - StoredPackageByName tag (0x04)
        - Serialized package name
        - Version bytes (0 for no version, 1 + version number for versioned)
        - Serialized entrypoint name
        - Serialized runtime arguments

        Returns:
            Bytes representation of the session.
        """
        # Tag StoredPackageByNameTag = '04'
        stored_package_by_name_tag = int(4).to_bytes()

        # Version handling
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = (
                int(1).to_bytes() +
                self.version.to_bytes(4, byteorder='little')
            )

        return (
            stored_package_by_name_tag +
            serialize_string(self.package_name) +
            version_bytes +
            serialize_string(self.entrypoint) +
            self.runtime_args.serialize()
        )

    def to_json(self) -> Dict[str, Any]:
        """Convert the session to JSON format.

        The JSON representation includes:
        - Session section
        - StoredVersionedContractByName section with:
          - Package name
          - Version (if specified)
          - Entrypoint name
          - Runtime arguments

        Returns:
            Dictionary containing the session in JSON format.
        """
        return {
            JSONNAME.DEPLOY_SESSION: {
                JSONNAME.STOREDVERSIONEDCONTRACTBYNAME: {
                    JSONNAME.NAME: self.package_name,
                    JSONNAME.VERSION: self.version,
                    JSONNAME.ENTRYPOINT: self.entrypoint,
                    JSONNAME.ARGS: self.runtime_args.to_json()
                }
            }
        }
