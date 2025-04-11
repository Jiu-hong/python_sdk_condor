"""CL option type module.

This module provides the CLOption type for handling optional values in the Casper network.
An option can either contain a value (Some) or be empty (None).
"""

from typing import Optional, Union

from .cl_basetype import CLValue
from ..constants import TAG


class CLOption(CLValue):
    """Class representing an optional value in the Casper network.

    An option can either contain a value (Some) or be empty (None).
    This is similar to Rust's Option type or Haskell's Maybe type.
    """

    tag = TAG.CLOption.value

    def __init__(self, *data: Union[CLValue, None]) -> None:
        """Initialize a CL option.

        Args:
            *data: Either:
                - A single CLValue for Some
                - None for None

        Raises:
            TypeError: If the input is not a CLValue or None.
        """
        # Some
        if len(data) == 1:
            if not isinstance(data[0], CLValue):
                raise TypeError(
                    "Input type should be CLValue for CLOption")
            self.flag = 1  # 1 - some, 0 - none
            self.data = data[0]
        # None
        elif len(data) == 2:
            if data[0] is not None:
                raise TypeError(
                    "Input type should be None or CLValue for CLOption")
            self.flag = 0
            self.data = data

    def serialize(self) -> bytes:
        """Serialize this option to bytes.

        The option is serialized as:
        - For None: A single byte 0x00
        - For Some: A single byte 0x01 followed by the serialized value

        Returns:
            Bytes representation of this option.
        """
        # None
        if self.flag == 0:
            return int(0).to_bytes(1, byteorder='little')
        # Some
        else:
            return int(1).to_bytes(1, byteorder='little') + self.data.serialize()
