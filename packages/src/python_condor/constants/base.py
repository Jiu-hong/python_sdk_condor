from enum import Enum


class RESULTHOLDER():
    pass


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
