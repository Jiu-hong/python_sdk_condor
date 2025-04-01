from result import Err, Ok
import python_condor.cl_values.cl_basetype as cl_baseType
from ..constants import RESULTHOLDER


def serialize_string(data):
    content = bytearray(data, encoding="utf-8")
    bytes_len = int(len(content)).to_bytes(4, byteorder='little')
    return bytes_len+content
# def deep_v2(data):
#     result = ""
#     if isinstance(data, cl_baseType.CLValue):
#         result = f'{data.__class__.__name__}({deep_v2(data.data)})'
#     elif isinstance(data, list | tuple):
#         result = [
#             {x.__class__.__name__}({deep_v2(x.data)}) for x in data]
#         # remove single quote for list members
#         result = f"[{', '.join(result)}]"
#     elif isinstance(data, dict):
#         result = "{"+f'{deep_v2(list(data.keys())[0])}: {
#             deep_v2(list(data.values())[0])}' + "}"
#     elif isinstance(data, Ok | Err):
#         result = f'{data.__class__.__name__}({deep_v2(data.value)})'
#     else:
#         if isinstance(data, int | str):
#             if isinstance(data, int):
#                 result = data
#             else:
#                 # quote string
#                 result = f'{data}'
#         elif isinstance(data, RESULTHOLDER):
#             result = f'{data}'
#         else:
#             # result = f'{data.__class__.__name__}({deep_v2(data.data)})'
#             raise  # incorrect types
#     return result


def deep_value_v2(self):
    result = ""
    if isinstance(self, int | str):
        result = self
        if isinstance(self, str):
            result = f'{self}'
    elif isinstance(self, tuple | list):
        # check if CLResult
        if isinstance(self, tuple) and isinstance(self[-1], bool):
            if self[-1] == True:  # OK value
                result = {'Ok': deep_value_v2(self[0])}
            else:  # err value
                result = {'Err': deep_value_v2(self[1])}
            return result
        # check if cloption none
        if isinstance(self, tuple) and self[0] is None:
            return
        result = [deep_value_v2(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, dict):
        result = []
        for key_value in self.items():
            item = {'key': deep_value_v2(
                key_value[0]), 'value': deep_value_v2(key_value[1])}
            result.append(item)
    elif isinstance(self, Ok):
        result = deep_value_v2(self.ok_value)
    elif isinstance(self, Err):
        result = deep_value_v2(self.err_value)
    elif self is None:
        result = None
    else:
        result = deep_value_v2(self.data)
    return result
