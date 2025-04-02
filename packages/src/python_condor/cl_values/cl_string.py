from .cl_basetype import CLAtomic, CLValue
from ..constants import NoneHolder, TAG


class CLString(CLValue, CLAtomic):
    tag = TAG.CLString.value

    def __init__(self, data: str) -> None:
        if not isinstance(data, str) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLString. Allowed value is {str}")

        super().__init__(data)

    def serialize(self) -> bytes:
        content = bytearray(self.data, encoding="utf-8")
        bytes_len = int(len(content)).to_bytes(4, byteorder='little')
        return bytes_len+content

    def value(self):
        return self.data
