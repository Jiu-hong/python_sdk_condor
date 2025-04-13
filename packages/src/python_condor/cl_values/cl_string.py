"""CL string type module.

This module provides the CLString type for handling string values in the Casper network.
A string is a sequence of UTF-8 encoded characters that can be serialized and converted to JSON.
"""

from typing import Union

from .cl_base_type import CLValue
from ..constants import NoneHolder, TAG


class CLString(CLValue):
    """Class representing a string value in the Casper network.

    A string is a sequence of UTF-8 encoded characters that can be serialized
    and converted to JSON. The string is stored as a UTF-8 encoded byte array
    with a 4-byte length prefix.
    """

    tag = TAG.CLString.value

    def __init__(self, data: Union[str, NoneHolder]) -> None:
        """Initialize a CL string.

        Args:
            data: The string value or NoneHolder.

        Raises:
            TypeError: If the input is not a string or NoneHolder.
        """
        if not isinstance(data, str) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLString. Allowed value is {str}")

        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize this string to bytes.

        The string is serialized as:
        1. A 4-byte little-endian integer representing the length of the string in bytes
        2. The UTF-8 encoded bytes of the string

        Returns:
            Bytes representation of this string.
        """
        content = bytearray(self.data, encoding="utf-8")
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')
        return bytes_len + content

    def value(self) -> Union[str, NoneHolder]:
        """Get the value of this string.

        Returns:
            The string value or NoneHolder.
        """
        return self.data
