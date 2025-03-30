# https://docs.python.org/3/library/stdtypes.html#bytes


from .cl_baseType import CLAtomic, CLValue
from ..exceptions import ExceptionExceedMaxValue

from ..constants import RESULTHOLDER, TAG


class CLNumber(CLValue, CLAtomic):
    def __init__(self, data):
        if not isinstance(data, int) and not isinstance(data, RESULTHOLDER):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLNumber. Allowed value is {int}")
        super().__init__(data)

    def value(self):
        return self.data


class CLBool(CLValue, CLAtomic):
    tag = TAG.CLBool.value

    def __init__(self, data):
        if not isinstance(data, bool) and not isinstance(data, RESULTHOLDER):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLBool. Allowed value is {bool}")
        super().__init__(data)

    def serialize(self):
        return int(self.data).to_bytes(1, byteorder='little')

    def value(self):
        return self.data


# a = CLBool("True")
# print("here:", a.cl_value())
# print(a.serialize().hex())
# print(a.to_json())
# print(a.cl_value())


class CLI32(CLNumber):
    minvalue = -2**31
    maxvalue = 2**31-1
    tag = TAG.CLI32.value

    def serialize(self):
        if CLI32.minvalue <= self.data <= CLI32.maxvalue:
            return (self.data).to_bytes(4, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI32")


# a = CLI32("123")
# print(a.serialize().hex())
# print(a.to_json())
# print(a.cl_value())


class CLI64(CLNumber):
    minvalue = -2**63
    maxvalue = 2**63-1
    tag = TAG.CLI64.value

    def serialize(self):
        if CLI64.minvalue <= self.data <= CLI64.maxvalue:
            return (self.data).to_bytes(8, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI64")


# a = CLI64(2**63-1)
# print(a.serialize())


class CLU8(CLNumber):
    maxvalue = 2**8-1
    tag = TAG.CLU8.value

    def serialize(self):
        if 0 <= self.data <= CLU8.maxvalue:
            return (self.data).to_bytes(1, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU8")

# a = CLU8(2**8-1)
# print(a.serialize())
# print(a)
# print(a.value())


class CLU16(CLNumber):
    maxvalue = 2**16-1

    def serialize(self):
        if 0 <= self.data <= CLU16.maxvalue:
            # return (self.data).to_bytes(2, byteorder='little').hex()
            return (self.data).to_bytes(2, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU16")


class CLU32(CLNumber):
    maxvalue = 2**32-1
    tag = TAG.CLU32.value

    def serialize(self):
        if 0 <= self.data <= CLU32.maxvalue:
            return (self.data).to_bytes(4, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU32")


# x = CLU32(7)
# print("x=>", x)
# print(x.serialize().hex())
# # u32
# x = (1024).to_bytes(4, byteorder='little')
# x.hex()


class CLU64(CLNumber):
    maxvalue = 2**64-1
    tag = TAG.CLU64.value

    def serialize(self):
        if 0 <= self.data <= CLU64.maxvalue:
            return (self.data).to_bytes(8, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU64")


# x = CLU64(1603994401469)
# print(x.to_json())
# print(x.serialize())
# x = CLU64(int(time() * 1000))
# print(x.serialize())
# print(CLU64(int(time() * 1000)).serialize())


# class CLBigNumber(CLNumber):
#     def __init__(self, data):
#         super().__init__(data)

#         hex_string = '{:x}'.format(self.data)
#         # if the length is odd pad a zero in the left
#         if len(hex_string) % 2:
#             self.hex_string = hex_string.zfill(len(hex_string)+1)
#         else:
#             self.hex_string = hex_string

#         self.bytes = ""
#         self.index = int(len(self.hex_string)/2)

#         # bytes length: '{:02x}'.format(integer) => 2 ->'0x02'
#         self.bytes_len_hex = '{:02x}'.format(self.index)

#     def serialize(self):
#         # reverse bytes
#         for _ in range(self.index, 0, -1):
#             self.index = self.index - 1
#             result = self.hex_string[self.index*2:]
#             self.hex_string = self.hex_string[:self.index*2]
#             self.bytes += result
#         return bytes.fromhex(self.bytes_len_hex+self.bytes)

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


class CLU512(CLBigNumber):
    # u512 max value - class attribute
    maxvalue = 2**512-1
    tag = TAG.CLU512.value

    def serialize(self):
        if 0 <= self.data <= CLU512.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU512")


# a = CLU512("1000000000000000000000000")
# print(a.to_json())
# print(a.serialize())
# print(a)
# print("cl_value:", a.cl_value())
# a = CLU512(str(7))
# print(a.serialize())


class CLU256(CLBigNumber):
    # u256 max value - class attribute
    maxvalue = 2**256-1
    tag = TAG.CLU256.value

    def serialize(self):
        if 0 <= self.data <= CLU256.maxvalue:
            return super().serialize()
        else:
            # print("number exceeded the max u512 value")
            raise ExceptionExceedMaxValue(str(self.data), "CLU256")


# b = CLU256("1")
# print("b to_json:", b.to_json())
# print("type:", type(b))
# print(b.serialize().hex())
# b = CLU256(str(2**256-1))
# print(b.serialize().hex())
# a = CLU256("2500000000")
# print("serialize cl_value:", a.cl_value())


class CLU128(CLBigNumber):
    maxvalue = 2**128-1
    tag = TAG.CLU128.value

    def serialize(self):

        if 0 <= self.data <= CLU128.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU128")

# # ite = CLBigNumber('123456789101112131415')
# # print(ite.serialize())

    # def to_json(self):
    #     return "U128"
# a = CLU128(123)
# print(a.to_json())


# a = CLU32(123)
# print("a:", a.serialize().hex())
# # b = CLU128("abcd")
# # print(b.serialize())
# b = CLU128(2**128-1)
# print(b.serialize())
# b = CLU128(str(123456789101112131415))
# print(b.serialize())


# to do
class Unit:
    pass


# todo
class CLByteArray:
    tag = TAG.CLByteArray.value

    def __init__(self, data) -> None:
        self.data = data

    def serialize(self):
        pass


# a = CLU32(RESULTHOLDER())
# b = CLString(RESULTHOLDER())
# print("a:", a.to_json())
# print("b:", b.to_json())
