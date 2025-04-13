"""CL option type module.

This module provides the CLOption type for handling optional values in the Casper network.
An option can either contain a value (Some) or be empty (None).
"""

from typing import Union

from result import Err, Ok


from .cl_basetype import CLValue
from ..constants import TAG, NoneHolder


def check_non_holder(data) -> bool:

    if isinstance(data, int | str) or data is None:
        return False
    else:
        if isinstance(data, NoneHolder):
            return True
        else:
            if isinstance(data, tuple | list):
                for x in data:
                    return check_non_holder(x)
            elif isinstance(data, dict):
                for k, v in data.items():
                    for x in (k, v):
                        return check_non_holder(x)
            elif isinstance(data, Ok):
                return check_non_holder(data.ok_value)
            elif isinstance(data, Err):
                return check_non_holder(data.err_value)
            else:
                return check_non_holder(data.data)


class CLOption(CLValue):
    """Class representing an optional value in the Casper network.

    An option can either contain a value (Some) or be empty (None).
    This is similar to Rust's Option type or Haskell's Maybe type.
    """

    tag = TAG.CLOption.value

    def __init__(self, data: Union[CLValue, NoneHolder]) -> None:
        """Initialize a CL option.

        Args:
            *data: Either:
                - A single CLValue for Some
                - None for None

        Raises:
            TypeError: If the input is not a CLValue or None.
        """
        # Some
        if not check_non_holder(data):
            # if len(data) == 1:
            if not isinstance(data, CLValue):
                raise TypeError(
                    "Input type should be CLValue for CLOption")
            self.flag = 1  # 1 - some, 0 - none
            # # check if there is any NoneHolder() in some value
            # if check_non_holder(data) == True:
            #     raise TypeError("Some type shouldn't included NoneHolder")
        # None
        else:
            # if data[0] is not None and not check_non_holder(data[1]):
            #     raise TypeError(
            #         "Input type should be None with NoneHolder or CLValue for CLOption")
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
