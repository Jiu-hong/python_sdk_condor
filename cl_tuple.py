
from cl_number import *
from cl_string import CLString


class CLTupleBase(CLType):

    def serialize(self):
        new_data = ""
        if not isinstance(self.data, tuple):
            raise
        for element in self.data:
            new_data += element.serialize()
        return new_data

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


class CLTuple1(CLTupleBase):
    LENGTH = 1
    tag = 18

    def __init__(self, data):
        if len(data) != CLTuple1.LENGTH:
            raise
        super().__init__(data)


class CLTuple2(CLTupleBase):
    LENGTH = 2
    tag = 19

    def __init__(self, data):
        if len(data) != CLTuple2.LENGTH:
            raise
        super().__init__(data)


class CLTuple3(CLTupleBase):
    LENGTH = 3
    tag = 20

    def __init__(self, data):
        if len(data) != CLTuple3.LENGTH:
            raise
        super().__init__(data)


a = CLTuple3((CLString("Hello, World!"), CLBool(
    'true'), CLTuple2((CLU32(1), CLString("Hello, World!")))))
print(a)
print(a.value())
a = CLTuple2((CLU32(1), CLString("hello")))
print(a)
print(a.value())

a = CLTuple3((CLU32(1), CLString("hello"), CLU64(1)))
print(a)
print(a.value())
a = CLTuple3((CLU32(1), CLString("Hello, World!"), CLBool("true")))
print(a.serialize())
print(a)
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
