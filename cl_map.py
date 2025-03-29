
from cl_baseType import CLValue
import cl_list
from cl_number import CLU8
from cl_string import CLString
from cl_tuple import CLTuple2
from constants.base import TAG


class CLMap(CLValue):
    tag = TAG.CLMap.value

    def __get_list__(self):
        inner_tuple = [CLTuple2(x) for x in self.data.items()]
        return cl_list.CLList(inner_tuple)

    # def __str__(self):
    #     return f'{self.__class__.__name__}({{{str(self.__get_list__())}}})'

    def serialize(self):
        return self.__get_list__().sorted().serialize()


a = CLMap({CLU8(3): CLString("Jim"), CLU8(
    2): CLString("Jack"), CLU8(4): CLString("Jane"), CLU8(1): CLString("Jill")})
# print(a.serialize())
# print("str=>", a.to_json())
# print("value=>", a.value())
# print("type=>", a.cl_type())
# print("a", a.to_json())
# print("clvalue:", a.cl_value())
# print("value:", a.value())
