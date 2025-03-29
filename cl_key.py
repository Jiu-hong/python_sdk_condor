
from cl_baseType import CLAtomic, CLValue
from constants.base import TAG


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):
        # match self.data:
        # account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20
        if self.data.startswith("account-hash-"):
            return '00' + self.data.removeprefix('account-hash-')
        # hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20
        elif self.data.startswith("hash-"):
            return '01'+self.data.removeprefix('hash-')
        # uref-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20-005
        elif self.data.startswith("uref-"):
            temp = self.data.split('-')
            return '02' + temp[1] + '{:02x}'.format(int(temp[2]))
        else:
            raise

    def value(self):
        return self.serialize()

    def cl_value(self):

        content = self.serialize()
        bytes_len_hex = '{:02x}'.format(
            int(len(content) / 2)).ljust(8, '0')
        tag = '{:02x}'.format(self.tag)

        return bytes_len_hex + content + tag


a = CLKey(
    "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20")
# print(a.serialize())
# print(a)

b = CLKey('hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20')
# print(b.serialize())
# print(b)

c = CLKey('uref-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20-005')
# print(c.to_json())
# print(c.serialize())
# print(c)
# print(a)
# print(a.value())
# {
#     "cl_type": "Key",
#     "bytes": "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20",
#     "parsed": {
#         "Account": "account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"
#     }
# }

# {
#     "cl_type": "Key",
#     "bytes": "010102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20",
#     "parsed": {
#         "Hash": "hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"
#     }
# }

#         "cl_type": "Key",
# "bytes": "020102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2000",
# "parsed": {
#     "URef": "uref-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20-000"
# }

# {
#     "cl_type": "Key",
#     "bytes": "020102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f2005",
#     "parsed": {
#         "URef": "uref-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20-005"
#     }
# }
