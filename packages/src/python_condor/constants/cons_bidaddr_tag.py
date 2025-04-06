# from enum import Enum
# export enum BidAddrTag {
#   UnifiedTag = 0,
#   ValidatorTag,
#   DelegatedAccountTag,
#   DelegatedPurseTag,
#   CreditTag,
#   ReservedDelegationAccountTag,
#   ReservedDelegationPurseTag,
#   UnbondAccountTag,
#   UnbondPurseTag
# }
from .base import constant


class BidAddrTag(object):
    @constant
    def UnifiedTag():
        return "00"

    @constant
    def ValidatorTag():
        return "01"

    @constant
    def DelegatedAccountTag():
        return "02"

    @constant
    def DelegatedPurseTag():
        return "03"

    @constant
    def CreditTag():
        return "04"

    @constant
    def ReservedDelegationAccountTag():
        return "05"

    @constant
    def ReservedDelegationPurseTag():
        return "06"

    @constant
    def UnbondAccountTag():
        return "07"

    @constant
    def UnbondPurseTag():
        return "08"
