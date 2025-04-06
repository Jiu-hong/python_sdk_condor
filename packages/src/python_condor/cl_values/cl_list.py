from .cl_basetype import CLValue
from ..constants import TAG


class CLList(CLValue):
    tag = TAG.CLList.value

    def __init__(self, data: list) -> None:
        if not isinstance(data, list):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLList. Allowed value is {list}")
        base_type = type(data[0])
        # check type if consistent
        for element in data[1:]:
            if type(element) != base_type:
                raise TypeError(f"types aren't consistent in the elements")
        super().__init__(data)

    def serialize(self):
        new_data = b''
        if len(self.data) == 0:
            return int(0).to_bytes(4, byteorder='little')

        for element in self.data:
            new_data += element.serialize()
        list_length = int(len(self.data)).to_bytes(4, byteorder='little')
        return list_length + new_data

    def sorted(self):
        self.data.sort(key=lambda x: x.serialize())
        return CLList(self.data)
