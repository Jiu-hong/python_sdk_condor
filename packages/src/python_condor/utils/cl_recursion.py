"""CL value recursion utilities.

This module provides functions for recursively processing CL values in the Casper network,
including extracting tags, converting to JSON format, and handling nested data structures.
"""

from typing import Any, Dict, List,  Tuple, Union

from result import Err, Ok


from ..constants import CLTypeName, TAG, NoneHolder


CONST = CLTypeName()


def get_cl_tags(self) -> bytes:
    """Recursively extract CL tags from a value.

    This function traverses the data structure and extracts CL tags from each element,
    handling various types including tuples, lists, dictionaries, and special cases
    like CLOption and CLResult.

    Args:
        self: The CL value object to process.

    Returns:
        The concatenated bytes of all CL tags in the structure.
    """
    tag = int(self.tag).to_bytes(1, byteorder='little')
    if hasattr(self.data, 'tag'):
        return tag + get_cl_tags(self.data)
    elif isinstance(self.data, tuple):
        # if cloption None type
        if self.data[0] is None:
            # self.data[1] is option(null)'s tag
            return tag + get_cl_tags(self.data[1])

        # if clresult type
        # if isinstance(self.data[-1], bool):
        if self.tag == TAG.CLResult.value:
            # get both ok and err tag
            return tag + get_cl_tags(self.data[0].ok_value) + get_cl_tags(self.data[1].err_value)
        # get all the tuple elements' tag
        return tag + b''.join([get_cl_tags(x) for x in self.data])
    elif isinstance(self.data, list):
        # get all the list elements' tag
        if len(self.data) > 0:
            return tag + get_cl_tags(self.data[0])
        else:
            return tag + get_cl_tags(self.inner_type)
    elif isinstance(self.data, dict):
        if len(self.data) > 0:
            # get first element in dict
            tuple_value = list(self.data.items())[0]  # tuple
            return tag + b''.join([get_cl_tags(x) for x in tuple_value])
        else:
            return tag + b''.join([get_cl_tags(x) for k, v in self.inner_type.items() for x in (k, v)])

    else:
        return tag


def get_deep_json(self) -> Dict[str, Any]:
    """Recursively convert a CL value to its JSON representation.

    This function traverses the data structure and converts each element to its
    corresponding JSON format, handling various types including tuples, lists,
    dictionaries, and special cases like CLOption and CLResult.

    Args:
        self: The CL value object to convert.

    Returns:
        A dictionary representing the JSON structure of the CL value.
    """
    json_type = CONST.__getattribute__(self.__class__.__name__)

    if hasattr(self.data, 'tag'):
        return {json_type: get_deep_json(self.data)}
    elif isinstance(self.data, tuple):
        if self.tag == TAG.CLOption.value and self.data[0] is None:
            return {json_type: get_deep_json(self.data[1])}
        # result type
        if self.tag == TAG.CLResult.value:
            return {json_type: {'ok': get_deep_json(self.data[0].ok_value),
                                'err': get_deep_json(self.data[1].err_value)}}
        return {json_type: [get_deep_json(x) for x in self.data]}
    elif isinstance(self.data, list):
        if len(self.data) > 0:
            return {json_type: get_deep_json(self.data[0])}
        else:
            return {json_type: get_deep_json(self.inner_type)}

    elif isinstance(self.data, dict):
        if len(self.data) > 0:
            tuple_value = list(self.data.items())[0]  # tuple
            return {json_type: {'key': get_deep_json(tuple_value[0]),
                                'value': get_deep_json(tuple_value[1])}}
        else:
            return {json_type: {'key': get_deep_json(list(self.inner_type.keys())[0]),
                                'value': get_deep_json(list(self.inner_type.values())[0])}}

    else:
        return json_type


def get_deep_value(self) -> Union[None, int, str, List[Dict[str, Any]], Tuple[Any, ...], Dict[str, Any]]:
    """Recursively extract the deep value from a CL value.

    This function traverses the data structure and extracts the actual values,
    handling various types including tuples, lists, dictionaries, and special
    cases like CLOption and CLResult.

    Args:
        self: The CL value object to process.

    Returns:
        The extracted value in its appropriate Python type.
    """
    result = ""
    if isinstance(self, (int, str)):
        result = self
        if isinstance(self, str):
            result = f'{self}'
    elif isinstance(self, (tuple, list)):
        # check if CLResult
        if isinstance(self, tuple) and isinstance(self[-1], bool):
            if self[-1]:  # OK value
                result = {'Ok': get_deep_value(self[0])}
            else:  # err value
                result = {'Err': get_deep_value(self[1])}
            return result
        # check if cloption none
        if isinstance(self, tuple) and self[0] is None:
            return None
        result = [get_deep_value(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, dict):
        result = []
        for key_value in self.items():
            item = {'key': get_deep_value(key_value[0]),
                    'value': get_deep_value(key_value[1])}
            result.append(item)
    elif isinstance(self, Ok):
        result = get_deep_value(self.ok_value)
    elif isinstance(self, Err):
        result = get_deep_value(self.err_value)
    elif self is None or isinstance(self, NoneHolder):
        result = None
    else:
        result = get_deep_value(self.data)
    return result


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

    # elif isinstance(data, CLValue):
    elif hasattr(data, 'tag'):
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
