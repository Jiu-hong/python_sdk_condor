"""Bid address tag constants module.

This module provides constants for bid address tags used in the Casper network.
"""

from .base import constant


class BidAddrTag:
    """Class containing bid address tag constants.

    This class provides string tags used for different types of bid addresses
    in the Casper network.
    """

    @constant
    def UnifiedTag() -> str:
        """Get the unified tag."""
        return "00"

    @constant
    def ValidatorTag() -> str:
        """Get the validator tag."""
        return "01"

    @constant
    def DelegatedAccountTag() -> str:
        """Get the delegated account tag."""
        return "02"

    @constant
    def DelegatedPurseTag() -> str:
        """Get the delegated purse tag."""
        return "03"

    @constant
    def CreditTag() -> str:
        """Get the credit tag."""
        return "04"

    @constant
    def ReservedDelegationAccountTag() -> str:
        """Get the reserved delegation account tag."""
        return "05"

    @constant
    def ReservedDelegationPurseTag() -> str:
        """Get the reserved delegation purse tag."""
        return "06"

    @constant
    def UnbondAccountTag() -> str:
        """Get the unbond account tag."""
        return "07"

    @constant
    def UnbondPurseTag() -> str:
        """Get the unbond purse tag."""
        return "08"
