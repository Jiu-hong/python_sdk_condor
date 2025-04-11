"""CL type name constants module.

This module provides constants for CL (CasperLabs) type names used in the Casper network.
"""

from .base import constant


class CLTypeName:
    """Class containing CL type name constants.

    This class provides string names used for different types of CL values
    in the Casper network.
    """

    @constant
    def CLBool() -> str:
        """Get the CL boolean type name."""
        return "Bool"

    @constant
    def CLI32() -> str:
        """Get the CL 32-bit integer type name."""
        return "I32"

    @constant
    def CLI64() -> str:
        """Get the CL 64-bit integer type name."""
        return "I64"

    @constant
    def CLU8() -> str:
        """Get the CL 8-bit unsigned integer type name."""
        return "U8"

    @constant
    def CLU32() -> str:
        """Get the CL 32-bit unsigned integer type name."""
        return "U32"

    @constant
    def CLU64() -> str:
        """Get the CL 64-bit unsigned integer type name."""
        return "U64"

    @constant
    def CLU128() -> str:
        """Get the CL 128-bit unsigned integer type name."""
        return "U128"

    @constant
    def CLU256() -> str:
        """Get the CL 256-bit unsigned integer type name."""
        return "U256"

    @constant
    def CLU512() -> str:
        """Get the CL 512-bit unsigned integer type name."""
        return "U512"

    @constant
    def CLUnit() -> str:
        """Get the CL unit type name."""
        return "Unit"

    @constant
    def CLString() -> str:
        """Get the CL string type name."""
        return "String"

    @constant
    def CLKey() -> str:
        """Get the CL key type name."""
        return "Key"

    @constant
    def CLURef() -> str:
        """Get the CL URef type name."""
        return "URef"

    @constant
    def CLOption() -> str:
        """Get the CL option type name."""
        return "Option"

    @constant
    def CLList() -> str:
        """Get the CL list type name."""
        return "List"

    @constant
    def CLByteArray() -> str:
        """Get the CL byte array type name."""
        return "ByteArray"

    @constant
    def CLResult() -> str:
        """Get the CL result type name."""
        return "Result"

    @constant
    def CLMap() -> str:
        """Get the CL map type name."""
        return "Map"

    @constant
    def CLTuple1() -> str:
        """Get the CL 1-tuple type name."""
        return "Tuple1"

    @constant
    def CLTuple2() -> str:
        """Get the CL 2-tuple type name."""
        return "Tuple2"

    @constant
    def CLTuple3() -> str:
        """Get the CL 3-tuple type name."""
        return "Tuple3"

    @constant
    def Any() -> str:
        """Get the CL any type name."""
        return "Any"

    @constant
    def CLPublicKey() -> str:
        """Get the CL public key type name."""
        return "PublicKey"
