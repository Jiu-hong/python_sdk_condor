import json
from cl_number import CLU256, CLU32, CLBool
from cl_string import CLString
from cl_tuple import CLTuple1, CLTuple2


class NamedArg:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # CLValue

    def to_byte_with_named_arg(self):
        offset = 0
        buffer = b''

        name_bytes = CLString(self.name).serialize()
        buffer = name_bytes

        offset += len(name_bytes)

        value_bytes = bytes.fromhex(self.value.cl_value())

        buffer = buffer + value_bytes

        offset += len(value_bytes)
        return buffer

    def to_json(self):
        my_dict = {}
        print("self.value:", type(self.value))
        my_dict["cl_type"] = self.value.to_json()
        my_dict["bytes"] = self.value.serialize().hex()
        my_dict["parsed"] = self.value.value()

        return self.name, my_dict


a = NamedArg("tuple1", CLTuple1(CLBool(False),))
# tuple1: CLValue.newCLTuple1(CLValue.newCLValueBool(false)),
b = a.to_byte_with_named_arg()
# print("b is:", b.hex())
# print("json_value:", json.dumps(a.to_json()))
# 0400000061726731040000002a00000004
# 0400000061726731040000002a00000004
