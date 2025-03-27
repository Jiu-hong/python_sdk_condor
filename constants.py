from enum import Enum


class TAG(Enum):
    CLBool = 0
    CLI32 = 1
    CLI64 = 2
    CLU8 = 3
    CLU32 = 4
    CLU64 = 5
    CLU128 = 6
    CLU256 = 7
    CLU512 = 8
    CLUnit = 9
    CLString = 10
    CLKey = 11
    CLURef = 12
    CLOption = 13
    CLList = 14
    CLByteArray = 15
    CLResult = 16
    CLMap = 17
    CLTuple1 = 18
    CLTuple2 = 19
    CLTuple3 = 20
    CLAny = 21
    CLPublicKey = 22


class Length(Enum):
    CLTuple1 = 1
    CLTuple2 = 2
    CLTuple3 = 3


# print("TAG.CLI64: ", TAG.CLI64.value, TAG.CLI64.name)


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


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


# CONST = CLTypeName()

# print(CONST.PublicKey)
