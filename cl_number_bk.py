# https://docs.python.org/3/library/stdtypes.html#bytes

from cl_baseType import CLType


x = 1024
x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
# print(x)
(1024).to_bytes(2, byteorder='little')

# u8
x = (7).to_bytes(1, byteorder='little')
x.hex()


class ExceptionExceedMaxValue(Exception):
    def __init__(self, data, num_type, message=" isn't in the range of "):
        self.data = data
        self.message = message
        self.num_type = num_type
        super().__init__(self.data + self.message + self.num_type)


class ExceptionCLNumber(Exception):
    def __init__(self, data, message="should be decimal or string(decimal)"):
        self.data = data
        self.message = message
        super().__init__(self.data + " => "+self.message)


class CLNumber(CLType):
    def __init__(self, data):

        # is data isn't int or string, return None
        if not isinstance(data, str) and not isinstance(data, int):
            raise ExceptionCLNumber(data)

        # data is string but not correct decimal
        if isinstance(data, str):
            if not data.isdecimal():
                raise ExceptionCLNumber(data)
            else:
                data = int(data)
        self.data = data


class CLU8(CLNumber):
    maxvalue = 2**8

    def new(self):
        if 0 <= self.data <= CLU8.maxvalue:
            return (self.data).to_bytes(1, byteorder='little').hex()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU8")


# a = CLU8(2**9)
# print(a.new())


class CLU32(CLNumber):
    maxvalue = 2**32

    def new(self):
        if 0 <= self.data <= CLU32.maxvalue:
            return (self.data).to_bytes(4, byteorder='little').hex()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU32")


x = CLU32(7)
print(x.new())
# u32
x = (1024).to_bytes(4, byteorder='little')
x.hex()
# output '00040000'


class CLU64(CLNumber):
    maxvalue = 2**64

    def new(self):
        if 0 <= self.data <= CLU64.maxvalue:
            return (self.data).to_bytes(8, byteorder='little').hex()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU64")


# x = CLU64(2*63)
# print(x.new())
# # u512
# x = 123456789101112131415
# expect
# 0x0957ff1ada959f4eb106

# input '6b14e9f95da1aff57'


# exception when input number isn't decimal or string(decimal)


class CLBigNumber(CLNumber):
    def __init__(self, data):
        super().__init__(data)

        hex_string = '{:x}'.format(self.data)
        # if the length is odd pad a zero in the left
        if len(hex_string) % 2:
            self.hex_string = hex_string.zfill(len(hex_string)+1)
        else:
            self.hex_string = hex_string

        self.bytes = ""
        self.index = int(len(self.hex_string)/2)

        # bytes length: '0x{:02x}'.format(integer) => 2 ->'0x02'
        self.bytes_len_hex = '{:02x}'.format(self.index)

    def new(self):
        # reverse bytes
        for _ in range(self.index, 0, -1):
            self.index = self.index - 1
            result = self.hex_string[self.index*2:]
            self.hex_string = self.hex_string[:self.index*2]
            self.bytes += result
        return self.bytes_len_hex+self.bytes


class CLU512(CLBigNumber):
    # u512 max value - class attribute
    maxvalue = 2**512

    def new(self):

        if 0 <= self.data <= CLU512.maxvalue:
            return super().new()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU512")


# a = CLU512(str(2**513))
# print(a.new())
# a = CLU512(str(7))
# print(a.new())


class CLU256(CLBigNumber):
    # u256 max value - class attribute
    maxvalue = 2**256

    def new(self):
        if 0 <= self.data <= CLU256.maxvalue:
            return super().new()
        else:
            # print("number exceeded the max u512 value")
            raise ExceptionExceedMaxValue(str(self.data), "CLU256")


b = CLU256("10")
print(b.new())
# b = CLU256(str(2**256+1))
# print(b.new())


class CLU128(CLBigNumber):
    maxvalue = 2**128

    def new(self):

        if 0 <= self.data <= CLU128.maxvalue:
            return super().new()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU128")


# ite = CLBigNumber('123456789101112131415')
# print(ite.new())

# b = CLU128("abcd")
# print(b.new())
# b = CLU128(2**128)
# print(b.new())
# b = CLU128(str(123456789101112131415))
# print(b.new())
# 0b1101011000101001110100111111001010111011010000110101111111101010111
# 0b1101011000101001110100111111001010111011010000110101111111101011000
# 0b1101011000101001110100111111001010111011010000110101111111101010111
# original:
# 0b1101011000101001110100111111001010111011010000110101111111101010111
# expect:
# 0x0957ff1ada959f4eb106
# Define a hexadecimal string
# hex_string = "0957ff1ada959f4eb106"
# # Convert the hexadecimal string to an integer using the base 16
# hex_integer = int(hex_string, 16)
# binary_string = bin(hex_integer)
# # 0b1001010101111111111100011010110110101001010110011111010011101011000100000110
# struct.pack('>h', 1023)

# a = 123456789101112131415
# binary_string = bin(hex_integer)
# binary_string
# '0b1001010101111111111100011010110110101001010110011111010011101011000100000110'
# "{0:0>4X}".format(int("0000010010001101", 2))
# '048D'
# "{0:0>4X}".format(int(
#     "0b1001010101111111111100011010110110101001010110011111010011101011000100000110", 2))
# '957FF1ADA959F4EB106'
