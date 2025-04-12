"""CL number types module.

This module provides various number types for the Casper network, including:
- Signed integers (I32, I64)
- Unsigned integers (U8, U16, U32, U64, U128, U256, U512)
- Boolean values
- Big numbers for large integer values
"""

from typing import Union, Optional

from .cl_basetype import CLValue
from ..constants import NoneHolder, TAG
from .exceptions import ExceptionExceedMaxValue


class CLBool(CLValue):
    """Class representing a boolean value in the Casper network."""

    tag = TAG.CLBool.value

    def __init__(self, data: Union[bool, NoneHolder]) -> None:
        """Initialize a CL boolean.

        Args:
            data: The boolean value or NoneHolder.

        Raises:
            TypeError: If the input is not a boolean or NoneHolder.
        """
        if not isinstance(data, bool) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLBool. Allowed value is {bool}")
        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize this boolean to bytes.

        Returns:
            A single byte: 0x01 for True, 0x00 for False.
        """
        return int(self.data).to_bytes(1, byteorder='little')

    def value(self) -> Union[bool, NoneHolder]:
        """Get the value of this boolean.

        Returns:
            The boolean value or NoneHolder.
        """
        return self.data


class CLNumber(CLValue):
    """Base class for all number types in the Casper network."""

    def __init__(self, data: Union[int, NoneHolder]) -> None:
        """Initialize a CL number.

        Args:
            data: The number value or NoneHolder.

        Raises:
            TypeError: If the input is not an integer or NoneHolder.
        """
        if not isinstance(data, int) and not isinstance(data, NoneHolder):
            raise TypeError(
                f"Invalid type of input: {type(data)} for CLNumber. Allowed value is {int}")
        if isinstance(data, int):
            if data > self.maxvalue:
                raise ValueError(
                    f"Value {data} exceeds maximum {self.maxvalue} for {self.__class__.__name__}")
            if data < self.minvalue:
                raise ValueError(
                    f"Value {data} below minimum {self.minvalue} for {self.__class__.__name__}")
        super().__init__(data)

    def value(self) -> Union[int, NoneHolder]:
        """Get the value of this number.

        Returns:
            The number value or NoneHolder.
        """
        return self.data


class CLI32(CLNumber):
    """Class representing a 32-bit signed integer in the Casper network."""

    minvalue = -2**31
    maxvalue = 2**31-1
    tag = TAG.CLI32.value

    def serialize(self) -> bytes:
        """Serialize this I32 to bytes.

        Returns:
            4 bytes in little-endian order.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if CLI32.minvalue <= self.data <= CLI32.maxvalue:
            return self.data.to_bytes(4, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI32")


class CLI64(CLNumber):
    """Class representing a 64-bit signed integer in the Casper network."""

    minvalue = -2**63
    maxvalue = 2**63-1
    tag = TAG.CLI64.value

    def serialize(self) -> bytes:
        """Serialize this I64 to bytes.

        Returns:
            8 bytes in little-endian order.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if CLI64.minvalue <= self.data <= CLI64.maxvalue:
            return self.data.to_bytes(8, byteorder='little', signed=True)
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLI64")


class CLU8(CLNumber):
    """Class representing an 8-bit unsigned integer in the Casper network."""

    maxvalue = 2**8-1
    minvalue = 0
    tag = TAG.CLU8.value

    def serialize(self) -> bytes:
        """Serialize this U8 to bytes.

        Returns:
            A single byte.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU8.maxvalue:
            return self.data.to_bytes(1, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU8")


class CLU32(CLNumber):
    """Class representing a 32-bit unsigned integer in the Casper network."""

    maxvalue = 2**32-1
    minvalue = 0
    tag = TAG.CLU32.value

    def serialize(self) -> bytes:
        """Serialize this U32 to bytes.

        Returns:
            4 bytes in little-endian order.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU32.maxvalue:
            return self.data.to_bytes(4, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU32")


class CLU64(CLNumber):
    """Class representing a 64-bit unsigned integer in the Casper network."""

    maxvalue = 2**64-1
    minvalue = 0
    tag = TAG.CLU64.value

    def serialize(self) -> bytes:
        """Serialize this U64 to bytes.

        Returns:
            8 bytes in little-endian order.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU64.maxvalue:
            return self.data.to_bytes(8, byteorder='little')
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU64")


class CLBigNumber(CLNumber):
    """Base class for big number types in the Casper network."""

    def serialize(self) -> bytes:
        """Serialize this big number to bytes.

        The number is serialized as:
        1. A single byte representing the length of the number in bytes
        2. The number bytes in little-endian order

        Returns:
            Bytes representation of this big number.
        """
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
    """Class representing a 128-bit unsigned integer in the Casper network."""

    maxvalue = 2**128-1
    minvalue = 0
    tag = TAG.CLU128.value

    def serialize(self) -> bytes:
        """Serialize this U128 to bytes.

        Returns:
            Bytes representation of this U128.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU128.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU128")


class CLU256(CLBigNumber):
    """Class representing a 256-bit unsigned integer in the Casper network."""

    maxvalue = 2**256-1
    minvalue = 0
    tag = TAG.CLU256.value

    def serialize(self) -> bytes:
        """Serialize this U256 to bytes.

        Returns:
            Bytes representation of this U256.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU256.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU256")


class CLU512(CLBigNumber):
    """Class representing a 512-bit unsigned integer in the Casper network."""

    maxvalue = 2**512-1
    minvalue = 0
    tag = TAG.CLU512.value

    def serialize(self) -> bytes:
        """Serialize this U512 to bytes.

        Returns:
            Bytes representation of this U512.

        Raises:
            ExceptionExceedMaxValue: If the value is outside the valid range.
        """
        if 0 <= self.data <= CLU512.maxvalue:
            return super().serialize()
        else:
            raise ExceptionExceedMaxValue(str(self.data), "CLU512")


class Unit:
    """Class representing a unit type in the Casper network."""
    pass


class CLByteArray:
    """Class representing a byte array in the Casper network."""

    tag = TAG.CLByteArray.value

    def __init__(self, data: bytes) -> None:
        """Initialize a CL byte array.

        Args:
            data: The byte array data.
        """
        self.data = data

    def serialize(self) -> bytes:
        """Serialize this byte array to bytes.

        Returns:
            The byte array data.
        """
        return self.data
