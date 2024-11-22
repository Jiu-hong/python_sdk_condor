from cl_baseType import CLAtomic, CLType
from cl_util import deep_v2


class CLURef(CLType, CLAtomic):
    tag = 12

    def serialize(self):
        temp = self.data.split('-')
        if temp[0] != 'uref':
            raise  # prefix should be uref

        if len(temp[1]) != 64:
            raise  # length is incorrect
        if int(temp[2]) < 7 or int(temp[2]) < 0:
            raise  # access right should be 0-7
        return temp[1]+'0' + str(int(temp[2]))

    def value(self):
        return self.serialize()

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


# {
#     "cl_type": "URef",
#     "bytes": "fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07",
#     "parsed": "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"
# }
a = CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")
print(a.serialize())
print(a)
