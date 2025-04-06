from .cl_basetype import CLValue
from ..cl_values import CLList, CLTuple2
from ..constants import TAG


class CLMap(CLValue):
    tag = TAG.CLMap.value

    def __get_list__(self):
        inner_tuple = [CLTuple2(x) for x in self.data.items()]
        return CLList(inner_tuple)

    # def __str__(self):
    #     return f'{self.__class__.__name__}({{{str(self.__get_list__())}}})'

    def serialize(self):
        return self.__get_list__().sorted().serialize()
