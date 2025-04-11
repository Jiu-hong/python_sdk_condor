"""Scheduling kind constants module.

This module provides constants for different kinds of scheduling used in the Casper network.
"""

from .base import constant


class SchedulingKind:
    """Class containing scheduling kind constants.

    This class provides string names used for different types of scheduling
    in the Casper network, such as standard scheduling.
    """

    @constant
    def STANDARD() -> str:
        """Get the standard scheduling kind."""
        return "Standard"
