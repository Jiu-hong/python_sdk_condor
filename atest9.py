class CLTypeTag:
    CLBool = {"id": 0, "name": "Bool"}
    CLI32 = {"id": 1, "name": "I32"}
    CLI64 = {"id": 2, "name": "I64"}
    CLU8 = {"id": 3, "name": "U8"}
    CLU32 = {"id": 4, "name": "U32"}
    CLU64 = {"id": 5, "name": "U64"}
    CLU128 = {"id": 6, "name": "U128"}
    CLU256 = {"id": 7, "name": "U256"}
    CLU512 = {"id": 8, "name": "U512"}
    CLUnit = {"id": 9, "name": "Unit"}
    CLString = {"id": 10, "name": "String"}
    CLKey = {"id": 11, "name": "Key"}
    CLURef = {"id": 12, "name": "URef"}
    CLOption = {"id": 13, "name": "Option"}
    CLList = {"id": 14, "name": "List"}
    CLByteArray = {"id": 15, "name": "ByteArray"}
    CLResult = {"id": 16, "name": "Result"}
    CLMap = {"id": 17, "name": "Map"}
    CLTuple1 = {"id": 18, "name": "Tuple1"}
    CLTuple2 = {"id": 19, "name": "Tuple2"}
    CLTuple3 = {"id": 20, "name": "Tuple3"}
    CLAny = {"id": 21, "name": "Any"}
    CLPublicKey = {"id": 22, "name": "PublicKey"}


a = CLTypeTag.CLPublicKey
print("a is:", a["id"], a["name"])
