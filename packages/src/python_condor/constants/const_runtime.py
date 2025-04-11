"""Runtime kind constants module.

This module provides constants for different kinds of runtime environments
used in the Casper network.
"""

from .base import constant


class RuntimeKind:
    """Class containing runtime kind constants.

    This class provides string names used for different runtime environments
    in the Casper network, such as the Casper V1 virtual machine.
    """

    @constant
    def VMCASPERV1() -> str:
        """Get the Casper V1 virtual machine runtime kind."""
        return "VmCasperV1"
