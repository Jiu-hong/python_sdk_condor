"""Pricing mode constants module.

This module provides constants for different kinds of pricing modes
used in the Casper network.
"""

from .base import constant


class PricingModeKind:
    """Class containing pricing mode constants.

    This class provides string names used for different pricing modes
    in the Casper network, such as classic and fixed pricing.
    """

    @constant
    def CLASSIC() -> str:
        """Get the classic pricing mode."""
        return "Classic"

    @constant
    def FIXED() -> str:
        """Get the fixed pricing mode."""
        return "Fixed"
