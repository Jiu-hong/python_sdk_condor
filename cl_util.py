# v1
from result import Err, Ok
# from cl_baseType import CLType # this causes circular
import cl_baseType


def deep(data):
    if isinstance(data, list | tuple):
        for x in data:
            return deep(x)
    elif isinstance(data, Ok):
        deep(data.ok_value)
    elif isinstance(data, Err):
        deep(data.err_value)
    else:
        return data
# CLTuple2((CLU32(1), CLString("hello")))


def deep_v2(data):
    result = ""
    if isinstance(data, cl_baseType.CLType):
        result = f'{data.__class__.__name__}({deep_v2(data.data)})'
    elif isinstance(data, list | tuple):
        result = [
            f'{x.__class__.__name__}({deep_v2(x.data)})' for x in data]
        # remove single quote for list members
        result = f"[{', '.join(result)}]"

    elif isinstance(data, Ok | Err):
        result = f'{data.__class__.__name__}({deep_v2(data.value)})'
    else:
        if isinstance(data, int | str):
            if isinstance(data, int):
                result = data
            else:
                # quote string
                result = f'"{data}"'
        else:
            # result = f'{data.__class__.__name__}({deep_v2(data.data)})'
            raise  # incorrect types
    return result


def deep_value_v2(self):
    result = ""
    if isinstance(self, int | str):
        result = self
    elif isinstance(self, tuple | list):
        result = [deep_value_v2(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, Ok | Err):
        result = deep_value_v2(self.value)
    else:
        result = deep_value_v2(self.data)
    return result
