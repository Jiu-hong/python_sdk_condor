"""Target kind constants module.

This module provides constants for different kinds of targets used in the Casper network.
"""

from .base import constant


class TargetKind:
    """Class containing target kind constants.

    This class provides string names used for different types of targets
    in the Casper network, such as native, stored, and session targets.
    """

    @constant
    def NATIVE() -> str:
        """Get the native target kind."""
        return "native"

    @constant
    def STORED() -> str:
        """Get the stored target kind."""
        return "stored"

    @constant
    def SESSION() -> str:
        """Get the session target kind."""
        return "session"
