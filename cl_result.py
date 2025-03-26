from result import Err, Ok

from cl_baseType import CLType
from cl_list import CLList
from cl_number import CLU32, CLU64
from cl_option import CLOption
from cl_string import CLString
from cl_tuple import CLTuple2
from cl_util import deep, deep_v2, deep_value_v2


class CLResult(CLType):
    tag = 16

    def serialize(self):
        match self.data:
            case Ok(value):
                return '01'+value.serialize()
            case Err(value):
                return '00' + value.serialize()
            case _:
                # todo
                # it should be result type
                raise

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag

# a = CLResult(Ok(CLU64(314)))
# print("CLResult:", a.serialize())
# a = CLResult(Err(CLString("Uh oh")))
# print(a.serialize())
# # a = CLResult(CLI32(1))
# # print(a.serialize())


a = CLResult(Ok(CLString("Hello world!")))
# print(a.value())
# print(a)
# print(a.serialize())

b = CLResult(Err(CLOption(CLList([CLTuple2((CLU32(1), CLString("Hello, World!"))),
                                  CLString("world"), CLString("nihao")]))))
print(b)
print(b.value())

# -   E.g. `Ok(314u64)` serializes as `0x013a01000000000000`
# -   E.g. `Err("Uh oh")` serializes as `0x00050000005568206f68`
a = CLResult(Ok(CLU64(314)))
print(a)
print(a.serialize())
print(a.value())

a = CLResult(Err(CLString("Uh oh")))
print(a)
print(a.serialize())
print(a.value())
