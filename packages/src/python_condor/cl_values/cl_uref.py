"""CL URef type module.

This module provides the CLURef type for handling URef values in the Casper network.
A URef is a unique reference to a value stored in the global state.
"""

from .cl_basetype import CLValue
from ..constants import NoneHolder, TAG


class CLURef(CLValue):
    """Class representing a URef value in the Casper network.

    A URef is a unique reference to a value stored in the global state.
    It consists of:
    - A prefix 'uref'
    - A 32-byte (64 hex characters) address
    - An access rights byte (0-7)
    """

    tag = TAG.CLURef.value

    def __init__(self, data: str) -> None:
        """Initialize a CL URef.

        Args:
            data: The URef string in the format 'uref-<address>-<access_rights>'.

        Raises:
            ValueError: If the URef format is invalid:
                - Prefix is not 'uref'
                - Address length is not 64 hex characters
                - Access rights are not between 0 and 7
        """
        if not isinstance(data, str) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLURef. Allowed value is {str}")
        if isinstance(data, str):
            temp = data.split('-')
            if temp[0] != 'uref':
                # prefix should be uref
                raise ValueError(
                    f"Input prefix is {temp[0]}. Expected prefix is 'uref'.")
            if len(temp[1]) != 64:
                # length is incorrect
                raise ValueError(
                    f"Input length is {len(temp[1])}. Expected length is 64.")
            if int(temp[2]) > 7 or int(temp[2]) < 0:
                # access right should be 0-7
                raise ValueError(
                    f"Input access right is {temp[2]}. Expected access right should be between 000-007.")
        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize this URef to bytes.

        The URef is serialized as:
        1. The 32-byte address
        2. A single byte representing the access rights

        Returns:
            Bytes representation of this URef.
        """
        temp = self.data.split('-')
        return bytes.fromhex(temp[1]) + int(temp[2]).to_bytes(1, "little")
