from result import Err, Ok

from cl_baseType import CLValue
from cl_list import CLList
from cl_map import CLMap
from cl_number import CLU32, CLU64, CLU8
from cl_option import CLOption
from cl_string import CLString
from cl_tuple import CLTuple2
from constants import RESULTHOLDER, TAG, CLTypeName


class CLResult(CLValue):
    tag = TAG.CLResult.value

    def __init__(self, *data) -> None:
        self.data = data
        print("self.data:", self.data)
        print("type of self.data:", type(self.data))

    def serialize(self):
        # innerOk: CLValue,
        # innerErr: CLValue,
        # value: CLValue,
        # isSuccess: boolean

        match self.flag:
            case True:
                return int(1).to_bytes(4, byteorder='little') + self.data.serialize()
            case False:
                return int(0).to_bytes(4, byteorder='little') + self.data.serialize()
            case _:
                # todo
                # it should be result type
                raise


a = CLResult(Ok(CLOption(CLString(RESULTHOLDER()))), Err(CLString(CLU32(1))))
b = CLResult(Ok(CLOption(CLU32(1))), Err(CLString(RESULTHOLDER())))
c = CLTuple2((a, b))
d = CLList([a, b])

# print(d.to_json())

e = CLMap({CLU8(3): a, CLU8(
    2): a, CLU8(4): a, CLU8(1): a})
# print(e.to_json())
# CONST = CLTypeName()
# result = CLResult(CONST.CLString(CONST.CLOption),
#                   CONST.CLU32, Ok(CLString("hello")))
# * CLType Result<T, E> is represented as a JSON Object with exactly one entry named either "Ok" or
#   "Err" where the Object's value is suitable to represent T or E respectively, e.g.
#   {"name":"entry_point_name","type":{"Result":{"ok":"Bool","err":"U8"}},"value":{"Ok":true}}
#   {"name":"entry_point_name","type":{"Result":{"ok":"Bool","err":"U8"}},"value":{"Err":1}}
# a = CLMap({CLU8(3): CLString("Jim")})

# print(CONST.CLPublicKey)
# print("result to_json():", result.to_json())
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
# a = CLResult(Ok(CLU64(123)), (TAG.CLMap, TAG.CLOption, TAG.CLI32))
# a = CLResult(ok_type, err_type, value, flag)

# print(a.to_json())
# a = CLResult(Err(CLString("Uh oh")))
# print(a)
# print(a.serialize())
# print(a.value())
# a = Ok(1)
# print("a is:", a.value)
