from result import Err, Ok


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
