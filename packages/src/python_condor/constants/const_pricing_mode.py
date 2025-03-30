from .base import constant


class PricingModeKind(object):
    @constant
    def CLASSIC():
        return "Classic"

    @constant
    def FIXED():
        return "Fixed"
