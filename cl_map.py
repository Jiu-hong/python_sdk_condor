
from cl_baseType import CLMapBase, CLType
import cl_list
from cl_number import CLU8
from cl_string import CLString
from cl_tuple import CLTuple2
from constants import TAG


class CLMap(CLType):
    tag = TAG.CLMap.value

    def __get_list__(self):
        inner_tuple = [CLTuple2(x) for x in self.data.items()]
        return cl_list.CLList(inner_tuple)

    # def __str__(self):
    #     return f'{self.__class__.__name__}({{{str(self.__get_list__())}}})'

    def serialize(self):
        return self.__get_list__().sorted().serialize()

    # def value(self):
    #     return self.__get_list__().value()

    # def cl_value(self):

    #     content = self.serialize()
    #     bytes_len_hex = '{:02x}'.format(
    #         int(len(content) / 2)).ljust(8, '0')
    #     tag = '{:02x}'.format(self.tag)

    #     return bytes_len_hex + content + tag


a = CLMap({CLU8(3): CLString("Jim"), CLU8(
    2): CLString("Jack"), CLU8(4): CLString("Jane"), CLU8(1): CLString("Jill")})
# print(a.serialize())
# print("str=>", a.to_json())
# print("value=>", a.value())
# print("type=>", a.cl_type())
# print("a", a.to_json())
# print("clvalue:", a.cl_value())
print("value:", a.value())
# expected:
# 270000000400000003030000004a696d02040000004a61636b04040000004a616e6501040000004a696c6c11030a
# actual:
# 270000000400000001040000004a696c6c02040000004a61636b03030000004a696d04040000004a616e6511030a
