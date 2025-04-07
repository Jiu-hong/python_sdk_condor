from result import Err, Ok
from ..constants import CLTypeName, TAG

CONST = CLTypeName()


def get_cl_tags(self):
    tag = int(self.tag).to_bytes(1, byteorder='little')
    if hasattr(self.data, 'tag'):
        return tag + get_cl_tags(self.data)
    elif isinstance(self.data, tuple):
        # if cloption None type
        if self.data[0] is None:
            # self.data[1] is option(null)'s tag
            return tag + get_cl_tags(self.data[1])

        # if clresult type
        if isinstance(self.data[-1], bool):
            # get both ok and err tag
            return tag + get_cl_tags(self.data[0].ok_value) + get_cl_tags(self.data[1].err_value)
        # get all the tuple elements' tag
        return tag + b''.join([get_cl_tags(x) for x in self.data])
    elif isinstance(self.data, list):
        # get all the list elements' tag
        return tag + get_cl_tags(self.data[0])
    elif isinstance(self.data, dict):
        # get first element in dict
        tuple_value = list(self.data.items())[0]  # tuple
        return tag + b''.join([get_cl_tags(x) for x in tuple_value])
    else:
        return tag


def get_deep_json(self):
    json_type = CONST.__getattribute__(self.__class__.__name__)

    if hasattr(self.data, 'tag'):
        return {json_type: get_deep_json(self.data)}
    elif isinstance(self.data, tuple):
        if self.tag == TAG.CLOption.value and self.data[0] is None:
            return {json_type: get_deep_json(self.data[1])}
        # result type
        if self.tag == TAG.CLResult.value:
            return {json_type: {'ok': get_deep_json(self.data[0].ok_value), 'err': get_deep_json(self.data[1].err_value)}}
        return {json_type: [get_deep_json(x) for x in self.data]}
    elif isinstance(self.data, list):
        return {json_type: get_deep_json(self.data[0])}
    elif isinstance(self.data, dict):
        tuple_value = list(self.data.items())[0]  # tuple
        return {json_type: {'key': get_deep_json(tuple_value[0]), 'value': get_deep_json(tuple_value[1])}}
    else:
        return json_type


def get_deep_value(self):
    result = ""
    if isinstance(self, int | str):
        result = self
        if isinstance(self, str):
            result = f'{self}'
    elif isinstance(self, tuple | list):
        # check if CLResult
        if isinstance(self, tuple) and isinstance(self[-1], bool):
            if self[-1] == True:  # OK value
                result = {'Ok': get_deep_value(self[0])}
            else:  # err value
                result = {'Err': get_deep_value(self[1])}
            return result
        # check if cloption none
        if isinstance(self, tuple) and self[0] is None:
            return
        result = [get_deep_value(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, dict):
        result = []
        for key_value in self.items():
            item = {'key': get_deep_value(
                key_value[0]), 'value': get_deep_value(key_value[1])}
            result.append(item)
    elif isinstance(self, Ok):
        result = get_deep_value(self.ok_value)
    elif isinstance(self, Err):
        result = get_deep_value(self.err_value)
    elif self is None:
        result = None
    else:
        result = get_deep_value(self.data)
    return result
