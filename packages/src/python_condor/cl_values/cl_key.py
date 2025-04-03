from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):
        # account-hash
        if self.data.startswith("account-hash-"):
            result = '00' + self.data.removeprefix('account-hash-')
            return bytes.fromhex(result)
        # hash
        elif self.data.startswith("hash-"):
            result = '01'+self.data.removeprefix('hash-')
            return bytes.fromhex(result)
        # uref
        elif self.data.startswith("uref-"):
            temp = self.data.split('-')
            result = '02' + temp[1] + '{:02x}'.format(int(temp[2]))
            return bytes.fromhex(result)
        else:
            raise
