import cl_util


class CLType:
    def __init__(self, data) -> None:
        self.data = data

    def __str__(self):
        return f'{self.__class__.__name__}({cl_util.deep_v2(self.data)})'

    def value(self):
        return cl_util.deep_value_v2(self)

    def cl_type(self):
        return cl_util.deep_type_v2(self)


class CLAtomic():
    pass
