"""Invocation kind constants module.

This module provides constants for different kinds of invocations
used in the Casper network.
"""

from .base import constant


class InvocationKind:
    """Class containing invocation kind constants.

    This class provides string names used for different types of invocations
    in the Casper network, such as invocable entities and packages.
    """

    @constant
    def INVOCABLEENTITY() -> str:
        """Get the invocable entity kind."""
        return "InvocableEntity"

    @constant
    def INVOCABLEENTITYALIAS() -> str:
        """Get the invocable entity alias kind."""
        return "InvocableEntityAlias"

    @constant
    def PACKAGE() -> str:
        """Get the package kind."""
        return "Package"

    @constant
    def PACKAGEALIAS() -> str:
        """Get the package alias kind."""
        return "PackageAlias"
