"""
CLMap module for handling Casper map values.

This module provides functionality for working with Casper map values, including:
- Creating and manipulating CLMap instances
- Serializing maps to bytes
- Converting maps to JSON representation
- Validating map types and values
- Sorting map entries
"""
from .cl_basetype import CLValue
from ..cl_values import CLList, CLTuple2
from ..constants import TAG
from ..utils import get_cl_tags


class CLMap(CLValue):
    """Class representing a CL map type.

    A map is a collection of key-value pairs that can be serialized and converted to JSON.
    The map is internally represented as a list of tuples, where each tuple contains a key-value pair.
    """

    tag = TAG.CLMap.value

    def __init__(self, data, inner_type=None):
        if not isinstance(data, dict):
            raise TypeError("inner type should be map")

        if not isinstance(data, dict):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLMap. Allowed value is {dict}")
        if (inner_type != None and len(data) != 0) or (inner_type == None and len(data) == 0):
            raise ValueError(
                "it should be a dict without specifying type or empty dict sepcifying type")
        # check type if consistent
        if len(data) == 0:
            if not isinstance(inner_type, dict):
                raise ValueError("the type for clmap should be dict")
            for key, value in inner_type.items():
                if not isinstance(key, CLValue) or not isinstance(value, CLValue):
                    raise TypeError(
                        f"The inner key and value should be CLValue")
        else:
            for key, value in data.items():
                if not isinstance(key, CLValue) or not isinstance(value, CLValue):
                    raise TypeError(
                        f"The inner key and value should be CLValue")

            keys = list(data.keys())
            values = list(data.values())
            # check if key type consistent
            base_key_type = get_cl_tags(keys[0])
            for key in keys[1:]:
                if get_cl_tags(key) != base_key_type:
                    raise TypeError(
                        f"key types aren't consistent in the elements")
            # check if value type consistent
            base_value_type = get_cl_tags(values[0])
            for value in values[1:]:
                if get_cl_tags(value) != base_value_type:
                    raise TypeError(
                        f"value types aren't consistent in the elements")
        super().__init__(data)
        self.inner_type = inner_type

    def __get_list__(self) -> CLList:
        """Convert the map to a list of tuples.

        Returns:
            A CLList containing CLTuple2 objects representing the key-value pairs.
        """
        if len(self.data) != 0:
            inner_tuple = [CLTuple2(x) for x in self.data.items()]
            return CLList(inner_tuple)
        else:
            # empty dict
            return CLList([], self.inner_type)

    def serialize(self) -> bytes:
        """Serialize this CL map to bytes.

        The map is first converted to a sorted list of tuples, then serialized.

        Returns:
            Bytes representation of this CL map.
        """
        return self.__get_list__().sorted().serialize()
