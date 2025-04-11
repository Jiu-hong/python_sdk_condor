"""Entry point kind constants module.

This module provides constants for different kinds of entry points
used in the Casper network.
"""

from .base import constant


class EntryPointKind:
    """Class containing entry point kind constants.

    This class provides string names used for different types of entry points
    in the Casper network, such as contract calls, transfers, and staking operations.
    """

    @constant
    def CALL() -> str:
        """Get the call entry point kind."""
        return "Call"

    @constant
    def CUSTOM() -> str:
        """Get the custom entry point kind."""
        return "Custom"

    @constant
    def TRANSFER() -> str:
        """Get the transfer entry point kind."""
        return "Transfer"

    @constant
    def ADD_BID() -> str:
        """Get the add bid entry point kind."""
        return "Add_Bid"

    @constant
    def WITHDRAW_BID() -> str:
        """Get the withdraw bid entry point kind."""
        return "Withdraw_Bid"

    @constant
    def DELEGATE() -> str:
        """Get the delegate entry point kind."""
        return "Delegate"

    @constant
    def UNDELEGATE() -> str:
        """Get the undelegate entry point kind."""
        return "Undelegate"

    @constant
    def REDELEGATE() -> str:
        """Get the redelegate entry point kind."""
        return "Redelegate"

    @constant
    def ACTIVATE_BID() -> str:
        """Get the activate bid entry point kind."""
        return "Activate_Bid"

    @constant
    def CHANGEPUBLICKEY() -> str:
        """Get the change public key entry point kind."""
        return "ChangePublicKey"
