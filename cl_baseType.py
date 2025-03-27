from result import Err, Ok
import cl_util
from constants import CLTypeName


class CLType(object):
    def __init__(self, data) -> None:
        self.data = data

    def __str__(self):
        return f'{self.__class__.__name__}({cl_util.deep_v2(self.data)})'

    def value(self):
        return cl_util.deep_value_v2(self)

    def cl_type(self):
        return cl_util.deep_type_v2(self)

    def cl_value(self):
        content = self.serialize()
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')

        def get_cl_tags(self):
            tag = int(self.tag).to_bytes(1, byteorder='little')
            if hasattr(self.data, 'tag'):
                return tag + get_cl_tags(self.data)
            elif isinstance(self.data, tuple):
                return tag + b''.join([get_cl_tags(x) for x in self.data])
            elif isinstance(self.data, list):
                return tag + get_cl_tags(self.data[0])
            elif isinstance(self.data, dict):
                # first element in dict
                tuple_value = list(self.data.items())[0]  # tuple
                return tag + b''.join([get_cl_tags(x) for x in tuple_value])
            else:
                return tag

        tag = get_cl_tags(self)
        return (bytes_len + content + tag).hex()

    def to_json(self):
        CONST = CLTypeName()

        def get_deep_json(self):
            json_type = CONST.__getattribute__(self.__class__.__name__)
            if hasattr(self.data, 'tag'):
                return {json_type: get_deep_json(self.data)}
            elif isinstance(self.data, tuple):
                return {json_type: [get_deep_json(x) for x in self.data]}
            elif isinstance(self.data, list):
                return {json_type: get_deep_json(self.data[0])}
            elif isinstance(self.data, dict):
                tuple_value = list(self.data.items())[0]  # tuple
                return {json_type: {'key': get_deep_json(tuple_value[0]), 'value': get_deep_json(tuple_value[1])}}
            # elif isinstance(self.data, Ok | Err):
            #     # return {json_type: {'key': get_deep_json(tuple_value[0]), 'value': get_deep_json(tuple_value[1])}}
            #     pass
            else:
                return json_type

        return get_deep_json(self)

    # elif isinstance(data, tuple):
    #     result = [deep_type_v2(x) for x in data]
    #     result = '[' + ', '.join(result) + ']'
    # elif isinstance(data, list):
    #     # print("data[0]", data[0])
    #     result = deep_type_v2(data[0])
    # elif isinstance(data, dict):
    #     result = "{"+f'"key": {deep_type_v2(list(data.keys())[0])}, "value": {
    #         deep_type_v2(list(data.values())[0])}' + "}"
    #     # result = f"[{', '.join(result)}]"
    # elif isinstance(data, Ok | Err):
    #     result = f'{{"{data.__class__.__name__}":{deep_type_v2(data.value)}}}'


class CLAtomic:
    pass
