from result import Err, Ok
import python_condor.cl_values.cl_baseType as cl_baseType


def deep_v2(data):
    result = ""
    if isinstance(data, cl_baseType.CLValue):
        result = f'{data.__class__.__name__}({deep_v2(data.data)})'
    elif isinstance(data, list | tuple):
        result = [
            f'{x.__class__.__name__}({deep_v2(x.data)})' for x in data]
        # remove single quote for list members
        result = f"[{', '.join(result)}]"
    elif isinstance(data, dict):
        result = "{"+f'{deep_v2(list(data.keys())[0])}: {
            deep_v2(list(data.values())[0])}' + "}"
    elif isinstance(data, Ok | Err):
        result = f'{data.__class__.__name__}({deep_v2(data.value)})'
    else:
        if isinstance(data, int | str):
            if isinstance(data, int):
                result = data
            else:
                # quote string
                result = f'"{data}"'
        elif isinstance(data, cl_baseType.RESULTHOLDER):
            result = f'"{data}"'
        else:
            # result = f'{data.__class__.__name__}({deep_v2(data.data)})'
            raise  # incorrect types
    return result


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
        result = [deep_value_v2(x) for x in self]
        if isinstance(self, tuple):
            result = tuple(result)
    elif isinstance(self, dict):
        result = []
        for key_value in self.items():
            item = {'key': deep_value_v2(
                key_value[0]), 'value': deep_value_v2(key_value[1])}
            result.append(item)
    elif isinstance(self, Ok | Err):
        result = deep_value_v2(self.value)
    else:
        result = deep_value_v2(self.data)
    return result
