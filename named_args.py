from cl_number import CLU32
from cl_string import CLString


class NamedArg:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # CLValue

    def to_byte_with_named_arg(self):

        offset = 0
        buffer = b''

        name_bytes = CLString(self.name).serialize()
        print("name_bytes is:", name_bytes.hex())
        buffer = name_bytes
        print("buffer here is:", buffer.hex())

        offset += len(name_bytes)

        value_bytes = bytes.fromhex(self.value.cl_value())

        buffer = buffer + value_bytes

        offset += len(value_bytes)
        print("offset is,", offset)
        return buffer


a = NamedArg("arg1", CLU32(42))
b = a.to_byte_with_named_arg()
print("b is:", b.hex())
# 0400000061726731040000002a00000004
# 0400000061726731040000002a00000004
