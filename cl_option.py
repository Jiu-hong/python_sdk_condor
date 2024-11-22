from cl_baseType import CLType
from cl_list import CLList
from cl_number import CLU32
from cl_string import CLString
from cl_tuple import CLTuple2
from cl_util import deep_value_v2


class CLOption(CLType):
    tag = 13

    def __init__(self, data) -> None:
        super().__init__(data)
        if not isinstance(self.data, CLType):
            raise

    def serialize(self):
        if self.data == None:
            return '00'
        else:
            # remove '0x'
            return '01'+self.data.serialize()

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


# a = CLOption(CLList([CLTuple2((CLU32(1), CLString("Hello, World!"))),
#                     CLString("world"), CLString("nihao")]))
# print(a.value())
# print(a)
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
# c = CLOption(None)
# print(c)
# # print(c.serialize())
# a = CLOption(CLU32(10))
# print(a)
# print(a.serialize())
# print(a.value())
