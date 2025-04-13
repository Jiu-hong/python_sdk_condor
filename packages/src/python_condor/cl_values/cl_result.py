"""CL result type module.

This module provides the CLResult type for handling result values in the Casper network.
A result can be either a success (Ok) or a failure (Err) with associated values.
"""

from typing import Tuple

from result import Err, Ok

from .cl_base_type import CLValue
from ..constants import TAG, NoneHolder


def check_non_holder(data) -> bool:

    if isinstance(data, int) or isinstance(data, str):
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


ALLOWED_TYPES = (
    TAG.CLBool.value,
    TAG.CLI32.value,
    TAG.CLI64.value,
    TAG.CLU8.value,
    TAG.CLU32.value,
    TAG.CLU64.value,
    TAG.CLU128.value,
    TAG.CLU256.value,
    TAG.CLU512.value,
    TAG.CLString.value,
    TAG.CLKey.value,
    TAG.CLPublicKey.value,
    TAG.CLURef.value
)


def check_if_holder_is_inner_of_clvalue(data, parent_tag=None):
    if isinstance(data, NoneHolder):
        if parent_tag in ALLOWED_TYPES:
            return True
        else:
            return False

    elif isinstance(data, CLValue):
        parent_tag = data.tag
        return check_if_holder_is_inner_of_clvalue(data.data, parent_tag)
    elif isinstance(data, int | str):
        return False
    elif isinstance(data, list | tuple):
        for x in data:
            if hasattr(x, "tag"):
                parent_tag = x.tag
            else:
                parent_tag = None
            return check_if_holder_is_inner_of_clvalue(x, parent_tag)
    elif isinstance(data, dict):
        for k, v in data.items():
            for x in (k, v):
                if hasattr(x, "tag"):
                    parent_tag = x.tag
                else:
                    parent_tag = None
                return check_if_holder_is_inner_of_clvalue(x, parent_tag)
    elif isinstance(data, Ok):
        if hasattr(data, "tag"):
            parent_tag = data.tag
        else:
            parent_tag = None
        return check_if_holder_is_inner_of_clvalue(data.ok_value, parent_tag)
    elif isinstance(data, Err):
        if hasattr(data, "tag"):
            parent_tag = data.tag
        else:
            parent_tag = None
        return check_if_holder_is_inner_of_clvalue(data.err_value, parent_tag)


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
        # data[0]:ok value
        # data[1]:err value
        # data[2]: true or false

        # Actual Value
        if not (check_non_holder(data[1]) and check_non_holder(data[0])):
            if len(data) < 3:
                raise ValueError(
                    "the data should contain ok value, err value and bool flag")

            if not isinstance(data[2], bool):
                raise TypeError("the third field should be bool flag")

            # check ok value:
            if data[2] == True:
                # ok value.
                if not isinstance(data[0], Ok):
                    raise ValueError("Ok value should be Ok(...)")
                if not isinstance(data[0].ok_value, CLValue):

                    raise ValueError("ok value should be Ok(clvalue)")
                # data[0] shouldn't be non_holder. err value data[1] should be non_holder
                if not check_non_holder(data[1]) or check_non_holder(data[0]):
                    raise ValueError("ok value construct incorrect")
                if not check_if_holder_is_inner_of_clvalue(data[1]):
                    raise ValueError(
                        "NoneHolder should be inner of clvalue for Err value")
            else:
                # err value
                if not isinstance(data[1], Err):
                    raise ValueError("Err value should be Err(...)")
                if not isinstance(data[1].err_value, CLValue):
                    raise ValueError("err value should be Err(clvalue)")
                # err value
                if not check_non_holder(data[0]) or check_non_holder(data[1]):
                    raise ValueError("error value construct incorrect")
                if not check_if_holder_is_inner_of_clvalue(data[0]):
                    raise ValueError(
                        "NoneHolder should be inner of clvalue for Okay value")
        # place holder
        else:
            if not check_if_holder_is_inner_of_clvalue(data[0]) or not check_if_holder_is_inner_of_clvalue(data[1]):
                raise ValueError("NoneHolder should be inner of clvalue")

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
