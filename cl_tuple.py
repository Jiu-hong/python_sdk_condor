
from cl_baseType import CLType
from cl_number import *
from cl_string import CLString
from constants import Length


class CLTupleBase(CLType):
    def __init__(self, data) -> None:
        super().__init__(data)
        if not isinstance(self.data, tuple):
            raise

    def serialize(self):
        new_data = b''
        if not isinstance(self.data, tuple):
            raise
        for element in self.data:
            new_data += element.serialize()
        return new_data


class CLTuple1(CLTupleBase):
    tag = TAG.CLTuple1.value

    def __init__(self, *data):
        print("data: ", data)
        if len(data) != Length.CLTuple1.value:
            raise
        super().__init__(data)


# a = CLTuple1(CLBool(True))
# print("a.to_json is:", a.to_json())
# print("a.cl_value is:", a.cl_value())
# expected:
# 01000000001200
# 01000000011200
# 010000000112
# tuple2(bool,string)
# expected:
# 0a000000 010500000048656c6c6f 13000a
# actual
#
class CLTuple2(CLTupleBase):
    tag = TAG.CLTuple2.value

    def __init__(self, data):
        print("data:", data)
        if len(data) != Length.CLTuple2.value:
            raise ("length incorrect for CLTuple2")
        super().__init__(data)


# CLValue.newCLTuple2((CLValue.newCLValueBool(true)), CLValue.newCLString("Hello")))
# expected
# 0a000000010500000048656c6c6f13000a
# actual
# 0a000000010500000048656c6c6f13000a
# tuple2 = CLTuple2((CLBool(True), CLString("Hello")))
# print("tuple2 to_json", tuple2.to_json())
# print("tuple2 cl_value()", tuple2.cl_value())


class CLTuple3(CLTupleBase):
    tag = TAG.CLTuple3.value

    def __init__(self, data):
        if len(data) != Length.CLTuple3.value:
            raise
        super().__init__(data)


# CLValue.newCLTuple3((CLValue.newCLValueBool(true)), CLValue.newCLString("Hello"), CLValue.newCLInt32(10))
# expected
# 0e000000010500000048656c6c6f0a00000014000a01

# a = CLTuple3((CLBool(True), CLString("Hello"), CLI32(10)))
# print(a.to_json())
# print(a.cl_value())
# a = CLTuple2((CLU32(1), CLString("hello")))
# print(a)
# print(a.value())

# a = CLTuple3((CLU32(1), CLString("hello"), CLU64(1)))
# print(a)
# print(a.value())
# a = CLTuple3((CLU32(1), CLString("Hello, World!"), CLBool("true")))
# print(a.serialize())
# print(a)
# print(a.serialize())
# # todo
# a = CLTuple2(())
# print(a.serialize())
# a = CLTuple2(1)
# print(type(a))
# a = CLTuple2((CLU8(3), CLString("Jim")))
# print(a.serialize())
# b = CLTuple2((CLU8(2), CLString("Jack")))
# print(b.serialize())
