from .cl_basetype import CLValue
from ..constants import TAG


class CLList(CLValue):
    tag = TAG.CLList.value

    def __init__(self, data: list) -> None:
        if not isinstance(data, list):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLList. Allowed value is {list}")
        base_type = type(data[0])
        # check type if consistent
        for element in data[1:]:
            if type(element) != base_type:

                raise TypeError(f"types aren't consistent in the elements")
        super().__init__(data)

    def serialize(self):
        new_data = b''
        if len(self.data) == 0:
            return int(0).to_bytes(4, byteorder='little')

        for element in self.data:
            new_data += element.serialize()
        list_length = int(len(self.data)).to_bytes(4, byteorder='little')
        return list_length + new_data

    def sorted(self):
        self.data.sort(key=lambda x: x.serialize())
        return CLList(self.data)


# CLValueParser.toBytesWithType(CLValue.newCLList(CLTypeUInt32, [
#     CLValue.newCLUInt32(1),
#     CLValue.newCLUInt32(2),
#     CLValue.newCLUInt32(3),
#     CLValue.newCLUInt32(3),
#     CLValue.newCLUInt32(3)
# ]))
# expected
# 180000000500000001000000020000000300000003000000030000000e04
# a = CLList([CLOption(CLU64(1)), CLOption(
#     CLU64(2)), CLOption(CLU64(3)), CLOption(CLU64(3)), CLOption(CLU64(3))])
# print("a.to_json():", a.to_json())
# print("a.cl_value():", a.cl_value())

# expected
# 31000000050000000101000000000000000102000000000000000103000000000000000103000000000000000103000000000000000e0d05
# 31000000050000000101000000000000000102000000000000000103000000000000000103000000000000000103000000000000000e0d05
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
