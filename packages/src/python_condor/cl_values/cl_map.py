"""CL map type module.

This module provides the CLMap type for handling map values in the Casper network.
A map is a collection of key-value pairs that can be serialized and converted to JSON.
"""

from typing import Dict, Any

from .cl_basetype import CLValue
from ..cl_values import CLList, CLTuple2
from ..constants import TAG


class CLMap(CLValue):
    """Class representing a CL map type.

    A map is a collection of key-value pairs that can be serialized and converted to JSON.
    The map is internally represented as a list of tuples, where each tuple contains a key-value pair.
    """

    tag = TAG.CLMap.value

    def __get_list__(self) -> CLList:
        """Convert the map to a list of tuples.

        Returns:
            A CLList containing CLTuple2 objects representing the key-value pairs.
        """
        inner_tuple = [CLTuple2(x) for x in self.data.items()]
        return CLList(inner_tuple)

    # def __str__(self):
    #     return f'{self.__class__.__name__}({{{str(self.__get_list__())}}})'

    def serialize(self) -> bytes:
        """Serialize this CL map to bytes.

        The map is first converted to a sorted list of tuples, then serialized.

        Returns:
            Bytes representation of this CL map.
        """
        return self.__get_list__().sorted().serialize()
