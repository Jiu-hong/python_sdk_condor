from python_condor.cl_values.cl_basetype import CLValue
from python_condor.cl_values.cl_number import CLU32
from python_condor.cl_values.cl_string import CLString
from python_condor.constants.base import RESULTHOLDER, TAG
# from .cl_basetype import CLValue
# from ..constants import TAG


# new CLValueOption(null, new CLTypeOption(CLTypeUInt32))


class CLOption(CLValue):
    tag = TAG.CLOption.value

    def __init__(self, data: CLValue | None) -> None:
        print("data is:", data)
        if data is not None and not isinstance(data, CLValue):
            raise TypeError(
                "Input type should be None or CLValue for CLOption")
        super().__init__(data)

    def serialize(self):
        if self.data == None:
            return int(0).to_bytes()
        else:
            # remove '0x'
            return int(1).to_bytes()+self.data.serialize()


# a = CLOption(CLList([CLOption(CLU32(1)), CLOption(
#     CLU32(2)), CLOption(CLU32(3)), CLOption(CLU32(3)), CLOption(CLU32(3))]))
# print(a.value())
# print(a.cl_value())
# c = CLOption(None, CLString(RESULTHOLDER()))
a = CLOption(CLU32(777))
# b = CLOption(CLU32(888))
# print(a.serialize())
# print(b.serialize())
# print(a.serialize() > b.serialize())
# a = CLOption(CLU32(10))
# print(a.value())
# print(a)
# print(a)
# # print(a.serialize())
# b = CLOption(CLString("Hello, World!"))
# print(b)
# c = CLTuple2((CLU32(1), CLString("Hello, World!"), CLBool(
#     'true'), CLTuple2((CLU32(1), CLString("Hello, World!")))))
# d = CLOption(c)
# print(d)
# print(d.serialize())
# # print(b.serialize())

# c = CLOption(CLU64(0))
# a = CLOption(CLTuple2((CLU32(1), CLString("hello"))))
# print('C:', c.cl_value())
# print(c.to_json())
# {
# "Option": {
#     "Tuple3": [
#         "I32",
#         "String",
#         "String"
#     ]
# }
# }
# print("c serial:", c.serialize().hex())
# print(c.serialize())
# # print(c.serialize())
# a = CLOption(CLU32(10))
# print(a)
# print(a.serialize())
# print(a.value())

# expected
# 090000000100000000000000000d05
# actual
# 090000000100000000000000000d
