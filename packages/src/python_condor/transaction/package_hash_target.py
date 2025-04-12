"""
Package Hash Target module for handling Casper package hash targets.

This module provides functionality for creating and managing package hash targets in transactions.
Package hash targets are used for:
- Targeting contracts by their package hash
- Supporting versioned package references
- Managing runtime environment configuration

The module supports:
- Package hash validation (64-character hex string)
- Version management
- Runtime configuration
- Serialization to bytes and JSON
"""

import re
from typing import Dict, Any, Optional

from ..constants import JsonName
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization


# Constants for package hash target configuration
JSONNAME = JsonName()


class PackageHashTarget:
    """
    Represents a package hash target in a Casper transaction.

    A package hash target is used to reference a contract by its package hash.
    It supports:
    - Package hash specification (64-character hex string)
    - Optional version number
    - Runtime environment configuration

    Attributes:
        package_hash (str): The hash of the package in hex format
        version (Optional[int]): The version number of the package
        runtime (str): The runtime environment to use
    """

    def __init__(self, runtime: str, package_hash: str, version: Optional[int] = None):
        """
        Initialize a package hash target.

        Args:
            runtime (str): The runtime environment to use
            package_hash (str): The hash of the package in hex format
            version (Optional[int], optional): The version number of the package. Defaults to None.

        Raises:
            ValueError: If the package hash is not a valid 64-character hex string
        """
        # Validate package hash format
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(package_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "package-hash should only contain alphabet and number(64 length)")

        self.package_hash = package_hash
        self.version = version
        self.runtime = runtime

    def to_bytes(self) -> bytes:
        """
        Serialize the package hash target to bytes.

        The serialization includes:
        - Target type (1 for stored)
        - Package hash and version
        - Runtime configuration

        Returns:
            bytes: The serialized package hash target
        """
        # Serialize version information
        version_bytes = b''
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                (self.version).to_bytes(4, byteorder='little')

        # Create inner table for package hash target
        selftable = CalltableSerialization()
        selftable.add_field(0, int(2).to_bytes()) \
            .add_field(1, bytes.fromhex(self.package_hash)) \
            .add_field(2, version_bytes)

        # Create outer table for stored target
        table = CalltableSerialization()
        table.add_field(0, int(1).to_bytes()) \
            .add_field(1, selftable.to_bytes()) \
            .add_field(2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the package hash target to a JSON representation.

        The JSON structure follows the format:
        {
            "target": {
                "Stored": {
                    "id": {
                        "ByPackageHash": {
                            "addr": "<package_hash>",
                            "version": <version_number>
                        }
                    },
                    "runtime": "<runtime>"
                }
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the package hash target
        """
        return {
            JSONNAME.TARGET: {
                JSONNAME.STORED: {
                    JSONNAME.ID: {
                        JSONNAME.BYPACKAGEHASH: {
                            JSONNAME.ADDR: self.package_hash,
                            JSONNAME.VERSION: self.version
                        }
                    },
                    JSONNAME.RUNTIME: self.runtime
                }
            }
        }
