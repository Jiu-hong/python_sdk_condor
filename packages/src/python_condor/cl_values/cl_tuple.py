"""CL tuple types module.

This module provides tuple types for the Casper network, including:
- CLTuple1: A tuple with exactly 1 element
- CLTuple2: A tuple with exactly 2 elements
- CLTuple3: A tuple with exactly 3 elements

All tuple elements must be CLValue types.
"""

from typing import Tuple

from result import Err, Ok

from .cl_base_type import CLValue
from ..constants import NoneHolder, TAG, Length


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


class CLTupleBase(CLValue):
    """Base class for all tuple types in the Casper network.

    This class provides common functionality for tuples, including:
    - Type checking for tuple elements
    - Serialization of tuple elements
    """

    def __init__(self, data: Tuple[CLValue, ...]) -> None:
        """Initialize a CL tuple.

        Args:
            data: A tuple of CLValue objects.

        Raises:
            TypeError: If the input is not a tuple or if any element is not a CLValue.
        """
        if not isinstance(data, tuple):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLTuple. Allowed value is {tuple}")
        for x in data:
            if not isinstance(x, CLValue):
                raise TypeError(f"The inner type should be CLValue")

        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize this tuple to bytes.

        The tuple is serialized by concatenating the serialized bytes of each element.

        Returns:
            Bytes representation of this tuple.
        """
        new_data = b''
        if self.actual_value:
            for element in self.data:
                new_data += element.serialize()
        return new_data


class CLTuple1(CLTupleBase):
    """Class representing a tuple with exactly 1 element in the Casper network."""

    tag = TAG.CLTuple1.value

    def __init__(self, *data: Tuple[CLValue, ...]) -> None:
        """Initialize a CL tuple with 1 element.

        Args:
            *data: A tuple containing exactly 1 CLValue.

        Raises:
            ValueError: If the tuple does not have exactly 1 element.
        """
        super().__init__(data)
        if len(data) != Length.CLTuple1.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple1 length is 1.")
        # Actual Value
        if not check_non_holder(data[0]):
            self.actual_value = True
        # place holder
        else:
            self.actual_value = False
            if not check_if_holder_is_inner_of_clvalue(data[0]):
                raise ValueError("NoneHolder should be inner of clvalue")


class CLTuple2(CLTupleBase):
    """Class representing a tuple with exactly 2 elements in the Casper network."""

    tag = TAG.CLTuple2.value

    def __init__(self, data: Tuple[CLValue, CLValue]) -> None:
        """Initialize a CL tuple with 2 elements.

        Args:
            data: A tuple containing exactly 2 CLValues.

        Raises:
            ValueError: If the tuple does not have exactly 2 elements.
        """
        super().__init__(data)
        if len(data) != Length.CLTuple2.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple2 length is 2.")

        # Actual Value
        if not (check_non_holder(data[1]) and check_non_holder(data[0])):
            self.actual_value = True
        # place holder
        else:
            self.actual_value = False
            if not check_if_holder_is_inner_of_clvalue(data[0]):
                raise ValueError("NoneHolder should be inner of clvalue")


class CLTuple3(CLTupleBase):
    """Class representing a tuple with exactly 3 elements in the Casper network."""

    tag = TAG.CLTuple3.value

    def __init__(self, data: Tuple[CLValue, CLValue, CLValue]) -> None:
        """Initialize a CL tuple with 3 elements.

        Args:
            data: A tuple containing exactly 3 CLValues.

        Raises:
            ValueError: If the tuple does not have exactly 3 elements.
        """
        super().__init__(data)
        if len(data) != Length.CLTuple3.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple3 length is 3.")

        # Actual Value
        if not (check_non_holder(data[0]) and check_non_holder(data[1]) and check_non_holder(data[2])):
            self.actual_value = True
        # place holder
        else:
            self.actual_value = False
            if not check_if_holder_is_inner_of_clvalue(data[0]):
                raise ValueError("NoneHolder should be inner of clvalue")
