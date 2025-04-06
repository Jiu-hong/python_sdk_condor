from .base import constant


class Prefix(object):
    @constant
    def ACCOUNT_HASH():
        return "account-hash-"

    @constant
    def HASH():
        return "hash-"

    @constant
    def UREF():
        return "uref-"

    @constant
    def TRANSFER():
        return "transfer-"

    @constant
    def DEPLOY():
        return "deploy-"

    @constant
    def ERA():
        return "era-"

    @constant
    def BALANCE():
        return "balance-"

    @constant
    def WITHDRAW():
        return "withdraw-"

    @constant
    def DICTIONARY():
        return "dictionary-"

    @constant
    def SYSTEM_CONTRACT_REGISTRY():
        return "system-contract-registry-"

    @constant
    def ERA_SUMMARY():
        return "era-summary-"

    @constant
    def UNBOND():
        return "unbond-"

    @constant
    def CHAINSPEC_REGISTRY():
        return "chainspec-registry-"

    @constant
    def CHECKSUM_REGISTRY():
        return "checksum-registry-"

    @constant
    def BID_ADDR():
        return "bid-addr-"

    @constant
    def BID():
        return "bid-"

    @constant
    def PACKAGE():
        return "package-"

    @constant
    def BYTE_CODE():
        return "byte-code-"


class AlgoKind(object):
    @constant
    def ED25519():
        return "01"

    @constant
    def SECP256K1():
        return "02"
