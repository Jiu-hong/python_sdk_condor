"""CL result type module.

This module provides the CLResult type for handling result values in the Casper network.
A result can be either a success (Ok) or a failure (Err) with associated values.
"""

from typing import Any, Tuple

from ..cl_values.cl_basetype import CLValue
from ..constants import TAG


class CLResult(CLValue):
    """Class representing a CL result type.

    A result type can be either a success (Ok) or a failure (Err) with associated values.
    This is similar to Rust's Result type or Haskell's Either type.
    """

    tag = TAG.CLResult.value

    def __init__(self, *data: Tuple[CLValue, CLValue, bool]) -> None:
        """Initialize a CL result.

        Args:
            *data: A tuple containing:
                - ok_value: The value to use if the result is successful
                - err_value: The value to use if the result is an error
                - is_success: Boolean flag indicating success or failure

        Raises:
            ValueError: If the data tuple is not properly formatted.
        """
        self.data = data

    def serialize(self) -> bytes:
        """Serialize this CL result to bytes.

        The serialization format is:
        - 1 byte flag (1 for success, 0 for failure)
        - Serialized value (either ok_value or err_value)

        Returns:
            Bytes representation of this CL result.

        Raises:
            ValueError: If the success flag is not a boolean.
        """
        # innerOk: CLValue,
        # innerErr: CLValue,
        # value: CLValue,
        # isSuccess: boolean

        # check ok or err
        match self.data[2]:
            case True:
                return int(1).to_bytes(1, byteorder='little') + self.data[0].ok_value.serialize()
            case False:
                return int(0).to_bytes(1, byteorder='little') + self.data[1].err_value.serialize()
            case _:
                raise ValueError(
                    "The third field should be a boolean flag indicating success or failure")
