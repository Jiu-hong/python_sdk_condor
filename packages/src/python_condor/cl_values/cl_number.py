from .cl_basetype import CLAtomic, CLValue
from ..constants import NoneHolder, TAG
from .exceptions import ExceptionExceedMaxValue


class CLNumber(CLValue, CLAtomic):

    def __init__(self, data):
        if not isinstance(data, int) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLNumber. Allowed value is {int}")
        super().__init__(data)

    def value(self):
        return self.data


class CLBool(CLValue, CLAtomic):
    tag = TAG.CLBool.value

    def __init__(self, data):
        if not isinstance(data, bool) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLBool. Allowed value is {bool}")
        super().__init__(data)

    def serialize(self):
        return int(self.data).to_bytes(1, byteorder='little')

    def value(self):
        return self.data


class CLI32(CLNumber):
    minvalue = -2**31
    maxvalue = 2**31-1
    tag = TAG.CLI32.value

    def __init__(self, data):
        # not check resultholder
        if isinstance(data, int):
            if data > CLI32.maxvalue or data < CLI32.minvalue:
                raise ValueError(
                    f"The inner value for the number should be {CLI32.minvalue} - {CLI32.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if CLI32.minvalue <= self.data <= CLI32.maxvalue:
            return self.data.to_bytes(4, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI32")


class CLI64(CLNumber):
    minvalue = -2**63
    maxvalue = 2**63-1
    tag = TAG.CLI64.value

    def __init__(self, data):
        # not check resultholder
        if isinstance(data, int):
            if data > CLI64.maxvalue or data < CLI64.minvalue:
                raise ValueError(
                    f"The inner value for the number should be {CLI64.minvalue} - {CLI64.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if CLI64.minvalue <= self.data <= CLI64.maxvalue:
            return self.data.to_bytes(8, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI64")


class CLU8(CLNumber):
    maxvalue = 2**8-1
    tag = TAG.CLU8.value

    def __init__(self, data):
        if isinstance(data, int):
            if data > CLU8.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU8.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU8.maxvalue:
            return self.data.to_bytes(1, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU8")


class CLU16(CLNumber):
    maxvalue = 2**16-1

    def __init__(self, data):
        if data > CLU16.maxvalue or data < 0:
            raise ValueError(
                f"The inner value for the number should be 0 - {CLU16.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU16.maxvalue:
            return self.data.to_bytes(2, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU16")


class CLU32(CLNumber):
    maxvalue = 2**32-1
    tag = TAG.CLU32.value

    def __init__(self, data):
        if isinstance(data, int):
            if data > CLU32.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU32.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU32.maxvalue:
            return self.data.to_bytes(4, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU32")


class CLU64(CLNumber):
    maxvalue = 2**64-1
    tag = TAG.CLU64.value

    def __init__(self, data):
        if isinstance(data, int):
            if data > CLU64.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU64.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU64.maxvalue:
            return self.data.to_bytes(8, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU64")


class CLBigNumber(CLNumber):

    def serialize(self):
        hex_string = '{:x}'.format(self.data)
        # if the length is odd pad a zero in the left
        if len(hex_string) % 2:
            hex_string = hex_string.zfill(len(hex_string)+1)

        m_bytes = ""
        index = int(len(hex_string)/2)
        bytes_len_hex = '{:02x}'.format(index)
        # reverse bytes
        for _ in range(index, 0, -1):
            index = index - 1
            result = hex_string[index*2:]
            hex_string = hex_string[:index*2]
            m_bytes += result
        return bytes.fromhex(bytes_len_hex+m_bytes)


class CLU128(CLBigNumber):
    maxvalue = 2**128-1
    tag = TAG.CLU128.value

    def __init__(self, data):
        if isinstance(data, int):
            if data > CLU128.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU128.maxvalue}")
        super().__init__(data)

    def serialize(self):

        if 0 <= self.data <= CLU128.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU128")


class CLU256(CLBigNumber):
    maxvalue = 2**256-1
    tag = TAG.CLU256.value

    def __init__(self, data):
        # not check resultholder
        if isinstance(data, int):
            if data > CLU256.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU256.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU256.maxvalue:
            return super().serialize()
        else:
            # print("number exceeded the max u512 value")
            raise ExceptionExceedMaxValue(str(self.data), "CLU256")


class CLU512(CLBigNumber):
    # u512 max value - class attribute
    maxvalue = 2**512-1
    tag = TAG.CLU512.value

    def __init__(self, data):
        # not check resultholder
        if isinstance(data, int):
            if data > CLU512.maxvalue or data < 0:
                raise ValueError(
                    f"The inner value for the number should be 0 - {CLU512.maxvalue}")
        super().__init__(data)

    def serialize(self):
        if 0 <= self.data <= CLU512.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU512")


class Unit:
    pass


# todo
class CLByteArray:
    tag = TAG.CLByteArray.value

    def __init__(self, data) -> None:
        self.data = data

    def serialize(self):
        pass
