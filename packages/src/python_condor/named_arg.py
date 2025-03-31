from .cl_values import CLString


class NamedArg:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # CLValue

    def to_byte_with_named_arg(self):
        name_bytes = CLString(self.name).serialize()
        value_bytes = bytes.fromhex(self.value.cl_value())

        return name_bytes + value_bytes

    def to_json(self):
        my_dict = {}
        my_dict["cl_type"] = self.value.to_json()
        my_dict["bytes"] = self.value.serialize().hex()
        my_dict["parsed"] = self.value.value()

        return self.name, my_dict


# a = NamedArg("tuple1", CLTuple1(CLBool(False),))
# # tuple1: CLValue.newCLTuple1(CLValue.newCLValueBool(false)),
# b = a.to_byte_with_named_arg()

# c = NamedArg("arg2", CLResult(
#     Ok(CLString("ABC")), Err(CLU32(RESULTHOLDER())), True))
# d = c.to_byte_with_named_arg()
# print("d is:", d.hex())
# print("b is:", b.hex())
# print("json_value:", json.dumps(a.to_json()))
# 0400000061726731040000002a00000004
# 0400000061726731040000002a00000004
