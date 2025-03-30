from .base import constant


class EntryPointKind(object):
    @constant
    def CALL():
        return "Call"

    @constant
    def CUSTOM():
        return "Custom"

    @constant
    def TRANSFER():
        return "Transfer"

    @constant
    def ADD_BID():
        return "Add_Bid"

    @constant
    def WITHDRAW_BID():
        return "Withdraw_Bid"

    @constant
    def DELEGATE():
        return "Delegate"

    @constant
    def UNDELEGATE():
        return "Undelegate"

    @constant
    def REDELEGATE():
        return "Redelegate"

    @constant
    def ACTIVATE_BID():
        return "Activate_Bid"

    @constant
    def CHANGEPUBLICKEY():
        return "ChangePublicKey"
