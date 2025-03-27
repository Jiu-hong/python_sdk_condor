from result import Err, Ok

from cl_baseType import CLType
from cl_list import CLList
from cl_number import CLU32, CLU64
from cl_option import CLOption
from cl_string import CLString
from cl_tuple import CLTuple2
from cl_util import deep, deep_v2, deep_value_v2
from constants import TAG, CLTypeName


class CLResult(CLType):
    tag = TAG.CLResult.value

    def __init__(self, *datalist):
        print("data: ", datalist)
        self.ok_type = datalist[0]
        self.err_type = datalist[1]
        self.data = datalist[2]

    def serialize(self):
        # innerOk: CLType,
        # innerErr: CLType,
        # value: CLValue,
        # isSuccess: boolean

        match self.data:
            case Ok(value):
                return int(1).to_bytes(4, byteorder='little') + value.serialize()
            case Err(value):
                return int(0).to_bytes(4, byteorder='little') + value.serialize()
            case _:
                # todo
                # it should be result type
                raise

    def to_json(self):
        CONST = CLTypeName()

        def get_deep_json(self):
            json_type = CONST.__getattribute__(self.__class__.__name__)
            if hasattr(self.data, 'tag'):
                return {json_type: get_deep_json(self.data)}
            elif isinstance(self.data, tuple):
                return {json_type: [get_deep_json(x) for x in self.data]}
            elif isinstance(self.data, list):
                return {json_type: get_deep_json(self.data[0])}
            elif isinstance(self.data, dict):
                tuple_value = list(self.data.items())[0]  # tuple
                return {json_type: {'key': get_deep_json(tuple_value[0]), 'value': get_deep_json(tuple_value[1])}}
            elif isinstance(self.data, Ok | Err):
                return {json_type: {'ok': self.ok_type, 'err': self.err_type}}
                pass
            else:
                return json_type

        return get_deep_json(self)

        # def cl_value(self):

        #     content = self.serialize()
        #     bytes_len_hex = '{:02x}'.format(
        #         int(len(content) / 2)).ljust(8, '0')
        #     tag = '{:02x}'.format(self.tag)

        #     return bytes_len_hex + content + tag

        # innerOk: CLType,
        # innerErr: CLType,
        # value: CLValue,
        # isSuccess: boolean
        # a = CLResult(Ok(CLU64(314)), Err())


CONST = CLTypeName()
result = CLResult(CONST.CLString(CONST.CLOption),
                  CONST.CLU32, Ok(CLString("hello")))

print(CONST.CLPublicKey)
print("result to_json():", result.to_json())
# print(a.to_json())
# print(a.cl_value())
# print(a.value())
# print("CLResult:", a.serialize())
# a = CLResult(Err(CLString("Uh oh")))
# print(a.serialize())
# # a = CLResult(CLI32(1))
# # print(a.serialize())


# a = CLResult(Ok(CLString("Hello world!")))
# print(a.value())
# print(a)
# print(a.serialize())

# b = CLResult(Err(CLOption(CLList([CLTuple2((CLU32(1), CLString("Hello, World!"))),
#                                   CLString("world"), CLString("nihao")]))))
# print(b)
# print(b.value())

# -   E.g. `Ok(314u64)` serializes as `0x013a01000000000000`
# -   E.g. `Err("Uh oh")` serializes as `0x00050000005568206f68`
# a = CLResult(Ok(CLU64(314)))
# print(a)
# print(a.serialize())
# print(a.value())

# a = CLResult(Err(CLString("Uh oh")))
# print(a)
# print(a.serialize())
# print(a.value())
