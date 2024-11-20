from cl_baseType import CLType
from cl_util import deep_v2


class CLString(CLType):
    tag = 10

    def serialize(self):
        content = bytearray(self.data, encoding="utf-8").hex()
        # bytes length: '0x{:02x}'.format(integer) => 2 ->'0x02'
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        return bytes_len_hex+content

    def value(self):
        return self.data

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


a = CLString("{'name':'Outlaw's Gambit #520', 'asset': 'https://bafybeife3ljy62bcxi4zjmc5thuba7je3jqpkyhymuhrbyqwebj3jg3dnu.ipfs.w3s.link'}")
# cspr.live
# 7b0000007b226e616d65223a224f75746c617727732047616d6269742023353230222c226173736574223a2268747470733a2f2f626166796265696665336c6a79363262637869347a6a6d63357468756261376a65336a71706b7968796d7568726279717765626a336a6733646e752e697066732e7733732e6c696e6b227d
# 7d0000007b276e616d65273a274f75746c617727732047616d6269742023353230272c20276173736574273a202768747470733a2f2f626166796265696665336c6a79363262637869347a6a6d63357468756261376a65336a71706b7968796d7568726279717765626a336a6733646e752e697066732e7733732e6c696e6b277d
# 7d0000007b226e616d65223a224f75746c617727732047616d6269742023353230222c20226173736574223a202268747470733a2f2f626166796265696665336c6a79363262637869347a6a6d63357468756261376a65336a71706b7968796d7568726279717765626a336a6733646e752e697066732e7733732e6c696e6b227d
print(a)
a = CLString("my_public_key")
print(a.serialize())

a = CLString("Hello, World!")
print(a.serialize())
# print(a.serialize())
# print("value=>", a.value())
# 0d0000006d795f7075626c69635f6b6579
# 0d0000006d795f7075626c69635f6b6579
# 0d00000000
a = CLString("pclphXwfYmCmdITj8hnh")
print(a.serialize())
