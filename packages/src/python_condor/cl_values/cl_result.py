from result import Err, Ok

from ..cl_values.cl_baseType import CLValue

from ..constants import RESULTHOLDER, TAG


class CLResult(CLValue):
    tag = TAG.CLResult.value

    def __init__(self, *data) -> None:
        self.data = data

    def serialize(self):
        # innerOk: CLValue,
        # innerErr: CLValue,
        # value: CLValue,
        # isSuccess: boolean

        # check ok or err
        match self.data[2]:
            case True:
                return int(1).to_bytes(1, byteorder='little') + self.data[0].value.serialize()
            case False:
                return int(0).to_bytes(1, byteorder='little') + self.data[1].value.serialize()
            case _:
                # todo
                # it should be result type
                raise


# a1 = CLResult(Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
#               Err(CLString("1")), True)
# print("a1 value()", a1.to_json())
# a2 = CLResult(Ok(CLOption(CLTuple2((CLString(RESULTHOLDER()), CLU64(123))))),
#               Err(CLString(CLString("error Hello"))), False)
# a3 = CLResult(Ok(CLOption(CLTuple2((CLString("world"), CLU64(123))))),
#               Err(CLString(CLString(RESULTHOLDER()))), True)
# l = CLList()
# c = CLList([a1, a2, a3])
# resultcorrectvalue, _ := clvalue.NewCLResult(cltype.String, cltype.UInt32, *clvalue.NewCLString("ABC"), true)
# resulterrvalue, _ := clvalue.NewCLResult(cltype.Bool, cltype.UInt32, *clvalue.NewCLUInt32(10), false)
# resultcorrectvalue = CLResult(
#     Ok(CLString("ABC")), Err(CLU32(RESULTHOLDER())), True)
# resulterrvalue = CLResult(
#     Ok(CLBool(RESULTHOLDER())), Err(CLU32(10)), False)
# print("resultcorrectvalue to_json()", resultcorrectvalue.to_json())
# expected
# "cl_type": {
#     "Result": {
#         "ok": "String",
#         "err": "U32"
#     }
# }
# actual
# {'Result': {'ok': 'String', 'err': 'U32'}}
# print("resultcorrectvalue value()", resultcorrectvalue.value())
# expected
# # {
#     "Ok": "ABC"
# }
# actual {'Ok': 'ABC'}
# print("resultcorrectvalue serialize()", resultcorrectvalue.serialize().hex())
# expected:
#         0103000000414243
# actual: 0100000003000000414243
# print("resultcorrectvalue cl_value()", resultcorrectvalue.cl_value())

# print("resulterrvalue to_json()", resulterrvalue.to_json())
# print("resulterrvalue value()", resulterrvalue.value())
# print("resulterrvalue serialize()", resulterrvalue.serialize().hex())
# expected 000a000000
# actual   000000000a000000
# c = CLTuple2((a, b))
# print("c.to_json()", c.to_json())
# print("a.to_json()", c.to_json())
# print("a.value", c.value())


# print(d.to_json())

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
