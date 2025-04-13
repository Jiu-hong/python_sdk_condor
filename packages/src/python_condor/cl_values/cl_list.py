"""CL list type module.

This module provides the CLList type for handling list values in the Casper network.
A list is a collection of values that can be serialized and converted to JSON.
"""

from typing import List, Any

from .cl_basetype import CLValue
from ..constants import TAG
from ..utils import get_cl_tags


class CLList(CLValue):
    """Class representing a CL list type.

    A list is a collection of values that can be serialized and converted to JSON.
    All elements in the list must be of the same type.
    """

    tag = TAG.CLList.value

    def __init__(self, data: List[Any], inner_type=None) -> None:
        """Initialize a CL list.

        Args:
            data: A list of values to be stored in the CL list.
                All elements must be of the same type.

        Raises:
            TypeError: If the input is not a list or if the elements are not of the same type.
        """
        if not isinstance(data, list):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLList. Allowed value is {list}")

        if (inner_type != None and len(data) != 0) or (inner_type == None and len(data) == 0):

            raise ValueError(
                "it should be a list without specifying type or empty list sepcifying type")
        # check type if consistent
        if len(data) != 0:
            for x in data:
                if not isinstance(x, CLValue):
                    raise TypeError(f"The inner type should be CLValue")

            # base_type = type(data[0])
            base_type = get_cl_tags(data[0])
            for element in data[1:]:
                if get_cl_tags(element) != base_type:
                    raise TypeError(f"types aren't consistent in the elements")
        super().__init__(data)
        self.inner_type = inner_type

    def serialize(self) -> bytes:
        """Serialize this CL list to bytes.

        The list is serialized as:
        1. A 4-byte little-endian integer representing the length of the list
        2. The serialized bytes of each element in the list

        Returns:
            Bytes representation of this CL list.
        """
        new_data = b''
        if len(self.data) == 0:
            return int(0).to_bytes(4, byteorder='little')

        for element in self.data:
            new_data += element.serialize()
        list_length = int(len(self.data)).to_bytes(4, byteorder='little')
        return list_length + new_data

    def sorted(self) -> 'CLList':
        """Sort the list based on the serialized bytes of each element.

        Returns:
            A new CLList containing the sorted elements.
        """
        if len(self.data) > 0:
            self.data.sort(key=lambda x: x.serialize())
            return CLList(self.data)
        else:
            return CLList([], self.inner_type)
