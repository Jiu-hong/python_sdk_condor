from constants.base import constant


class AlgoKind(object):
    @constant
    def ED25519():
        return "01"

    @constant
    def SECP256K1():
        return "02"
