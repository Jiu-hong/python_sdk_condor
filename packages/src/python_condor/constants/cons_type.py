from .base import constant


class CLTypeName(object):
    @constant
    def CLBool():
        return "Bool"

    @constant
    def CLI32():
        return "I32"

    @constant
    def CLI64():
        return "I64"

    @constant
    def CLU8():
        return "U8"

    @constant
    def CLU32():
        return "U32"

    @constant
    def CLU64():
        return "U64"

    @constant
    def CLU128():
        return "U128"

    @constant
    def CLU256():
        return "U256"

    @constant
    def CLU512():
        return "U512"

    @constant
    def CLUnit():
        return "Unit"

    @constant
    def CLString():
        return "String"

    @constant
    def CLKey():
        return "Key"

    @constant
    def CLURef():
        return "URef"

    @constant
    def CLOption():
        return "Option"

    @constant
    def CLList():
        return "List"

    @constant
    def CLByteArray():
        return "ByteArray"

    @constant
    def CLResult():
        return "Result"

    @constant
    def CLMap():
        return "Map"

    @constant
    def CLTuple1():
        return "Tuple1"

    @constant
    def CLTuple2():
        return "Tuple2"

    @constant
    def CLTuple3():
        return "Tuple3"

    @constant
    def Any():
        return "Any"

    @constant
    def CLPublicKey():
        return "PublicKey"


CONST = CLTypeName()
print(CONST.CLPublicKey)
