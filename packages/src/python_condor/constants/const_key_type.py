from .base import constant
from enum import Enum


class ClKeyTAG(Enum):
    ACCOUNT_HASH = 0
    HASH = 1
    UREF = 2
    TRANSFER = 3
    DEPLOY = 4
    ERA = 5
    BALANCE = 6
    BID = 7
    WITHDRAW = 8
    DICTIONARY = 9
    SYSTEM_ENTITY_REGISTRY = 10
    ERA_SUMMARY = 11
    UNBOND = 12
    CHAINSPEC_REGISTRY = 13
    CHECKSUM_REGISTRY = 14
    BID_ADDR = 15
    PACKAGE = 16
    BYTE_CODE = 18


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
    def SYSTEM_ENTITY_REGISTRY():
        return "system-entity-registry-"

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

    @constant
    def V1_WASM():
        return "v1-wasm-"

    @constant
    def V2_WASM():
        return "v2-wasm-"

    @constant
    def EMPTY():
        return "empty-"
# const V1_WASM_PREFIX: &str = "v1-wasm-";
# const V2_WASM_PREFIX: &str = "v2-wasm-";
# const EMPTY_PREFIX: &str = "empty-";
