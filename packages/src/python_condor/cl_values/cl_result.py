from ..cl_values.cl_basetype import CLValue
from ..constants import TAG


class CLResult(CLValue):
    tag = TAG.CLResult.value

    def __init__(self, *data) -> None:
        self.data = data

    def serialize(self):
        # innerOk: CLValue,
        # innerErr: CLValue,
        # value: CLValue,
        # isSuccess: boolean

        # check ok or err
        match self.data[2]:
            case True:
                return int(1).to_bytes(1, byteorder='little') + self.data[0].ok_value.serialize()
            case False:
                return int(0).to_bytes(1, byteorder='little') + self.data[1].err_value.serialize()
            case _:
                # todo
                # it should be result type
                raise ValueError("the third field should be a flag")
