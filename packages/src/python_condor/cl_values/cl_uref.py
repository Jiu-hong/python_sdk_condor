from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG


class CLURef(CLValue, CLAtomic):
    tag = TAG.CLURef.value

    def __init__(self, data):
        # self.data = data
        temp = data.split('-')
        if temp[0] != 'uref':
            # prefix should be uref
            raise ValueError(
                f"Input prefix is {temp[0]}. Expected prefix is 'uref'.")
        if len(temp[1]) != 64:
            # length is incorrect
            raise ValueError(
                f"Input length is {len(temp[1])}. Expected length is 64.")
        if int(temp[2]) > 7 or int(temp[2]) < 0:
            # access right should be 0-7
            raise ValueError(
                f"Input access right is {temp[2]}. Expected access right should be between 000-007.")
        super().__init__(data)

    def serialize(self):
        temp = self.data.split('-')
        return bytes.fromhex(temp[1]) + int(temp[2]).to_bytes(1, "little")
