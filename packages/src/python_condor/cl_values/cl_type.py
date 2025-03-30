from enum import Enum, unique


@unique
class CLTypeTag(Enum):
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
    CLTuple21 = 18
    CLTuple22 = 19
    CLTuple23 = 20
    CLAny = 21
    CLPublicKey = 22


@unique
class CLKeyTag(Enum):
    # Key::Account serializes as 0, Key::Hash as 1, Key::URef as 2.
    Account = 0,
    Hash = 1,
    URef = 2,
    Transfer = 3,
    DeployInfo = 4,
    EraInfo = 5,
    Balance = 6,
    Bid = 7,
    Withdraw = 8,
    Dictionary = 9,
    SystemContractRegistry = 10,
    EraSummary = 11,
    Unbond = 12,
    ChainspecRegistry = 13,
    ChecksumRegistry = 14,

# pub enum KeyTag {
#     Account = 0,
#     Hash = 1,
#     URef = 2,
#     Transfer = 3,
#     DeployInfo = 4,
#     EraInfo = 5,
#     Balance = 6,
#     Bid = 7,
#     Withdraw = 8,
#     Dictionary = 9,
#     SystemContractRegistry = 10,
#     EraSummary = 11,
#     Unbond = 12,
#     ChainspecRegistry = 13,
#     ChecksumRegistry = 14,
# }
