import json
from cl_number import CLU256, CLU32
from cl_string import CLString


class NamedArg:
    def __init__(self, name, value):
        self.name = name
        self.value = value  # CLValue

    def to_byte_with_named_arg(self):
        offset = 0
        buffer = b''

        name_bytes = CLString(self.name).serialize()
        # print("name_bytes is:", name_bytes.hex())
        buffer = name_bytes
        # print("buffer here is:", buffer.hex())

        offset += len(name_bytes)

        value_bytes = bytes.fromhex(self.value.cl_value())

        buffer = buffer + value_bytes

        offset += len(value_bytes)
        # print("offset is,", offset)
        return buffer

    def to_json(self):
        my_dict = {}
        my_dict["cl_type"] = self.value.cl_type()
        my_dict["bytes"] = self.value.serialize().hex()
        my_dict["parsed"] = self.value.value()

        return self.name, my_dict  # tuple tuple[1] is dict

        # "args": {
        #     "Named": [
        #         [
        #             "recipient",
        #             {
        #                 "cl_type": "Key",
        #                 "bytes": "00df4005315c83abef1275550632fc282a4aa6e80c8a64af23ca9a5c1d21256ee6",
        #                 "parsed": "account-hash-df4005315c83abef1275550632fc282a4aa6e80c8a64af23ca9a5c1d21256ee6"
        #             }
        #         ],
        #         [
        #             "amount",
        #             {
        #                 "cl_type": "U256",
        #                 "bytes": "010a",
        #                 "parsed": "10"
        #             }
        #         ]
        #     ]
        # },


a = NamedArg("arg1", CLU256(10))
b = a.to_byte_with_named_arg()
# print("b is:", b.hex())
# print("json_value:", json.dumps(a.to_json()))
# 0400000061726731040000002a00000004
# 0400000061726731040000002a00000004
