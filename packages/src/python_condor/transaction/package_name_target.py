"""
Package Name Target module for handling Casper package name targets.

This module provides functionality for creating and managing package name targets in transactions.
Package name targets are used for:
- Targeting contracts by their package name
- Supporting versioned package references
- Managing runtime environment configuration

The module supports:
- Package name validation
- Version management
- Runtime configuration
- Serialization to bytes and JSON
"""

from typing import Dict, Any, Optional

from ..constants import JsonName
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization, serialize_string


# Constants for package name target configuration
JSONNAME = JsonName()


class PackageNameTarget:
    """
    Represents a package name target in a Casper transaction.

    A package name target is used to reference a contract by its package name.
    It supports:
    - Package name specification
    - Optional version number
    - Runtime environment configuration

    Attributes:
        package_name (str): The name of the package
        version (Optional[int]): The version number of the package
        runtime (str): The runtime environment to use
    """

    def __init__(self, runtime: str, name: str, version: Optional[int] = None):
        """
        Initialize a package name target.

        Args:
            runtime (str): The runtime environment to use
            name (str): The name of the package
            version (Optional[int], optional): The version number of the package. Defaults to None.
        """
        self.package_name = name
        self.version = version
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the package name target to bytes.

        The serialization includes:
        - Target type (1 for stored)
        - Package name and version
        - Runtime configuration

        Returns:
            bytes: The serialized package name target
        """
        # Serialize version information
        version_bytes = b''
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                (self.version).to_bytes(4, byteorder='little')

        # Create inner table for package name target
        selftable = CalltableSerialization()
        selftable.add_field(0, int(3).to_bytes()) \
            .add_field(1, serialize_string(self.package_name)) \
            .add_field(2, version_bytes)

        # Create outer table for stored target
        table = CalltableSerialization()
        table.add_field(0, int(1).to_bytes()) \
            .add_field(1, selftable.to_bytes()) \
            .add_field(2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the package name target to a JSON representation.

        The JSON structure follows the format:
        {
            "target": {
                "Stored": {
                    "id": {
                        "ByPackageName": {
                            "name": "<package_name>",
                            "version": <version_number>
                        }
                    },
                    "runtime": "<runtime>"
                }
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the package name target
        """
        return {
            JSONNAME.TARGET: {
                JSONNAME.STORED: {
                    JSONNAME.ID: {
                        JSONNAME.BYPACKAGENAME: {
                            JSONNAME.NAME: self.package_name,
                            JSONNAME.VERSION: self.version
                        }
                    },
                    JSONNAME.RUNTIME: self.runtime
                }
            }
        }
