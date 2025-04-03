from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):
        # match self.data:
        # account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20
        if self.data.startswith("account-hash-"):
            result = '00' + self.data.removeprefix('account-hash-')
            return bytes.fromhex(result)
        # hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20
        elif self.data.startswith("hash-"):
            result = '01'+self.data.removeprefix('hash-')
            return bytes.fromhex(result)
        # uref-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20-005
        elif self.data.startswith("uref-"):
            temp = self.data.split('-')
            result = '02' + temp[1] + '{:02x}'.format(int(temp[2]))
            return bytes.fromhex(result)
        else:
            raise


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
