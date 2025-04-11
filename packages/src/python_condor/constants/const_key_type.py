"""Key type constants module.

This module provides constants for key types and prefixes used in the Casper network.
"""

from enum import Enum

from .base import constant


class ClKeyTAG(Enum):
    """Enumeration of key type tags.

    This enum defines the numeric tags used to identify different types of keys
    in the Casper network.
    """

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
    ADDRESSABLE_ENTITY = 17
    BYTE_CODE = 18
    MESSAGE = 19
    NAMED_KEY = 20
    BLOCK_GLOBAL = 21
    BALANCE_HOLD = 22
    ENTRY_POINT = 23


class Prefix:
    """Class containing key prefix constants.

    This class provides string prefixes used for different types of keys
    in the Casper network.
    """

    @constant
    def ACCOUNT_HASH() -> str:
        """Get the account hash prefix."""
        return "account-hash-"

    @constant
    def HASH() -> str:
        """Get the hash prefix."""
        return "hash-"

    @constant
    def UREF() -> str:
        """Get the URef prefix."""
        return "uref-"

    @constant
    def TRANSFER() -> str:
        """Get the transfer prefix."""
        return "transfer-"

    @constant
    def DEPLOY() -> str:
        """Get the deploy prefix."""
        return "deploy-"

    @constant
    def ERA() -> str:
        """Get the era prefix."""
        return "era-"

    @constant
    def BALANCE() -> str:
        """Get the balance prefix."""
        return "balance-"

    @constant
    def WITHDRAW() -> str:
        """Get the withdraw prefix."""
        return "withdraw-"

    @constant
    def DICTIONARY() -> str:
        """Get the dictionary prefix."""
        return "dictionary-"

    @constant
    def SYSTEM_ENTITY_REGISTRY() -> str:
        """Get the system entity registry prefix."""
        return "system-entity-registry-"

    @constant
    def ERA_SUMMARY() -> str:
        """Get the era summary prefix."""
        return "era-summary-"

    @constant
    def UNBOND() -> str:
        """Get the unbond prefix."""
        return "unbond-"

    @constant
    def CHAINSPEC_REGISTRY() -> str:
        """Get the chainspec registry prefix."""
        return "chainspec-registry-"

    @constant
    def CHECKSUM_REGISTRY() -> str:
        """Get the checksum registry prefix."""
        return "checksum-registry-"

    @constant
    def BID_ADDR() -> str:
        """Get the bid address prefix."""
        return "bid-addr-"

    @constant
    def BID() -> str:
        """Get the bid prefix."""
        return "bid-"

    @constant
    def PACKAGE() -> str:
        """Get the package prefix."""
        return "package-"

    @constant
    def BYTE_CODE() -> str:
        """Get the byte code prefix."""
        return "byte-code-"

    @constant
    def MESSAGE() -> str:
        """Get the message prefix."""
        return "message-"

    @constant
    def NAMED_KEY() -> str:
        """Get the named key prefix."""
        return "named-key-"

    @constant
    def BLOCK_GLOBAL() -> str:
        """Get the block global prefix."""
        return "block-"

    @constant
    def V1_WASM() -> str:
        """Get the V1 WASM prefix."""
        return "v1-wasm-"

    @constant
    def V2_WASM() -> str:
        """Get the V2 WASM prefix."""
        return "v2-wasm-"

    @constant
    def EMPTY() -> str:
        """Get the empty prefix."""
        return "empty-"

    @constant
    def ENTITY() -> str:
        """Get the entity prefix."""
        return "entity-"

    @constant
    def SYSTEM() -> str:
        """Get the system prefix."""
        return "system-"

    @constant
    def ACCOUNT() -> str:
        """Get the account prefix."""
        return "account-"

    @constant
    def CONTRACT() -> str:
        """Get the contract prefix."""
        return "contract-"

    @constant
    def ENTRY_POINT() -> str:
        """Get the entry point prefix."""
        return "entry-point-"
