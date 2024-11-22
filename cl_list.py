from cl_baseType import CLType
from cl_number import CLU256, CLU32
from cl_string import CLString
from cl_tuple import CLTuple2
from cl_util import deep_value_v2


class CLList(CLType):
    tag = 14

    def __init__(self, data) -> None:
        super().__init__(data)
        if not isinstance(self.data, list):
            raise
        base_type = type(self.data[0])
        # check type if consistent
        for element in self.data[1:]:
            if type(element) != base_type:
                # to do
                # types aren't consistent for the elements
                raise Exception  # CLListError1

    def serialize(self):
        new_data = ""
        if len(self.data) == 0:
            return '00000000'

        for element in self.data:
            new_data += element.serialize()
        list_length = '{:02x}'.format(
            int(len(self.data))).ljust(8, '0')
        return list_length + new_data

    def sorted(self):
        self.data.sort(key=lambda x: x.value())
        return CLList(self.data)

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


# a = CLList([CLU32(13), CLU32(2), CLU32(3)])
# print(a.value())
# a = CLList([CLString("hello"), CLString("world"), CLString("nihao")])
# print(a.value())

# b = CLList([CLList([
#            CLString("hello"), CLString("world"), CLString("nihao")]), CLString("world"), CLString("nihao")])
# print(b.value())

# c = CLList([CLTuple2((CLU32(1), CLString("Hello, World!"))),
#            CLString("world"), CLString("nihao")])
# print(c)
# print(c.value())

# c = CLList([CLU32(1), CLU32(2), CLU32(3)])
# print(c)
# print(c.serialize())
# print(c.value())
# # 0x03000000010000000200000003000000
# # 0300000000010000000200000003000000
# # amount: CLValueBuilder.u256(2500000000)
# # owner: CLValueBuilder.u256(2500000000),
# a = CLList([CLTuple2((CLString("amount"), CLU256("2500000000"))),
#            CLTuple2((CLString("owner"), CLU256("2500000000")))])
# print(a.serialize())
# # expect 0100000006000000616d6f756e74050000000400f9029507
# # actual 0100000006000000616d6f756e74        0400f90295
# # expect 0200000006000000616d6f756e74050000000400f9029507050000006f776e6572050000000400f9029507
# # actual 0200000006000000616d6f756e74        0400f90295  050000006f776e6572        0400f90295
# a = CLList([CLTuple2((CLString("amount"), CLU256("123"))),
#            CLTuple2((CLString("owner"), CLU256("456"))), CLTuple2((CLString("recipient"), CLU256("456")))])
# print(a.serialize())
