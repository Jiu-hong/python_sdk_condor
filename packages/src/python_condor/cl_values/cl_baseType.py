from .cl_util import deep_v2, deep_value_v2
from ..constants import TAG
from ..constants import CLTypeName

CONST = CLTypeName()


class CLValue(object):
    def __init__(self, data) -> None:
        self.data = data

    def __str__(self):
        return f'{self.__class__.__name__}({deep_v2(self.data)})'

    def value(self):
        return deep_value_v2(self)

    def cl_value(self):
        content = self.serialize()
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')

        def get_cl_tags(self):
            tag = int(self.tag).to_bytes(1, byteorder='little')
            if hasattr(self.data, 'tag'):
                return tag + get_cl_tags(self.data)
            elif isinstance(self.data, tuple):
                # if clresult type
                if isinstance(self.data[-1], bool):
                    # get both ok and err tag
                    return tag + get_cl_tags(self.data[0].value) + get_cl_tags(self.data[1].value)
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

        tag = get_cl_tags(self)
        return (bytes_len + content + tag).hex()

    def to_json(self):

        def get_deep_json(self):
            json_type = CONST.__getattribute__(self.__class__.__name__)

            if hasattr(self.data, 'tag'):
                return {json_type: get_deep_json(self.data)}
            elif isinstance(self.data, tuple):
                # result type
                if self.tag == TAG.CLResult.value:
                    return {json_type: {'ok': get_deep_json(self.data[0].value), 'err': get_deep_json(self.data[1].value)}}
                return {json_type: [get_deep_json(x) for x in self.data]}
            elif isinstance(self.data, list):
                return {json_type: get_deep_json(self.data[0])}
            elif isinstance(self.data, dict):
                tuple_value = list(self.data.items())[0]  # tuple
                return {json_type: {'key': get_deep_json(tuple_value[0]), 'value': get_deep_json(tuple_value[1])}}
            else:
                return json_type

        return get_deep_json(self)


class CLAtomic:
    pass
