from .cl_basetype import CLValue
from ..constants import TAG


class CLOption(CLValue):
    tag = TAG.CLOption.value

    def __init__(self, *data: CLValue | None) -> None:
        # Some
        if len(data) == 1:
            if not isinstance(data[0], CLValue):
                raise TypeError(
                    "Input type should be CLValue for CLOption")
            self.flag = 1  # 1 - some, 0 - none
            self.data = data[0]
        # None
        if len(data) == 2:
            if data[0] is not None:
                raise TypeError(
                    "Input type should be None or CLValue for CLOption")
            self.flag = 0
            self.data = data

    def serialize(self):
        # None
        if self.flag == 0:
            return int(0).to_bytes()
        # Some
        else:
            # remove '0x'
            return int(1).to_bytes()+self.data.serialize()
