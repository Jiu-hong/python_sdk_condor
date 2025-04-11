"""Algorithm kind prefix constants module.

This module provides constants for algorithm kind prefixes used in the Casper network.
"""

from .base import constant


class AlgoKind:
    """Class containing algorithm kind prefix constants.

    This class provides string prefixes used for different types of algorithms
    in the Casper network.
    """

    @constant
    def ED25519() -> str:
        """Get the ED25519 algorithm prefix."""
        return "01"

    @constant
    def SECP256K1() -> str:
        """Get the SECP256K1 algorithm prefix."""
        return "02"
