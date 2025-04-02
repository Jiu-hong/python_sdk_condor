from .cl_basetype import CLValue
from ..constants import TAG, Length


class CLTupleBase(CLValue):
    def __init__(self, data: tuple) -> None:
        if not isinstance(data, tuple):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLTuple. Allowed value is {tuple}")
        for x in data:
            if not isinstance(x, CLValue):
                raise TypeError(f"The inner type should be CLValue")

        super().__init__(data)

    def serialize(self):
        new_data = b''
        for element in self.data:
            new_data += element.serialize()
        return new_data


class CLTuple1(CLTupleBase):
    tag = TAG.CLTuple1.value

    def __init__(self, *data: tuple):
        super().__init__(data)
        if len(data) != Length.CLTuple1.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple1 length is 1.")


class CLTuple2(CLTupleBase):
    tag = TAG.CLTuple2.value

    def __init__(self, data: tuple):
        super().__init__(data)
        if len(data) != Length.CLTuple2.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple2 length is 2.")


class CLTuple3(CLTupleBase):
    tag = TAG.CLTuple3.value

    def __init__(self, data: tuple):
        super().__init__(data)
        if len(data) != Length.CLTuple3.value:
            raise ValueError(
                f"Input tuple length is {len(data)}. Allowed CLTuple3 length is 3.")
