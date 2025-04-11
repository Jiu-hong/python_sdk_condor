"""CL tuple types module.

This module provides tuple types for the Casper network, including:
- CLTuple1: A tuple with exactly 1 element
- CLTuple2: A tuple with exactly 2 elements
- CLTuple3: A tuple with exactly 3 elements

All tuple elements must be CLValue types.
"""

from typing import Tuple

from .cl_basetype import CLValue
from ..constants import TAG, Length


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
