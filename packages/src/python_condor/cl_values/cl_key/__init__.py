"""CL Key module.

This module provides functionality for handling CL keys in the Casper network.
CL keys are used to identify various types of data in the network, such as accounts,
hashes, URefs, transfers, deploys, balances, and more.
"""

from typing import NoReturn

from .block_global_key import check_block_global_key_format, serialize_block_global_key
from .byte_code_key import check_byte_code_key_format, serialize_bytes_code_key
from .entry_point_key import check_entry_point_key_format, serialize_entry_point_key
from .era_key import check_era_key_format, serialize_era_key
from .message_key import check_message_key_format, serialize_message_key
from .named_key import check_named_key_format, serialize_named_key

from ..cl_basetype import CLAtomic, CLValue
from ...constants import TAG, Prefix, ClKeyTAG
from ...utils import check_clkey_bid_addr_format, check_clkey_hash_format, check_purse_format

PREFIX = Prefix()


class CLKey(CLValue, CLAtomic):
    """Class for handling CL keys in the Casper network.

    CL keys can be of various types, each with its own format and validation rules.
    Supported key types include:
    - Account hash
    - Hash
    - URef
    - Transfer
    - Deploy
    - Balance
    - Withdraw
    - Dictionary
    - System entity registry
    - Era summary
    - Era
    - Unbond
    - Chainspec registry
    - Checksum registry
    - Bid address
    - Package
    - Byte code
    - Message
    - Named key
    - Block global
    - Entry point
    """

    tag = TAG.CLKey.value

    def __init__(self, data: str) -> NoReturn:
        """Initialize a CLKey instance.

        Args:
            data: The key string to validate.

        Raises:
            ValueError: If the key format is invalid for any of the supported types.
        """
        if data.startswith(PREFIX.ACCOUNT_HASH):
            hash_value = data.removeprefix(PREFIX.ACCOUNT_HASH)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.HASH):
            hash_value = data.removeprefix(PREFIX.HASH)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.UREF):
            check_purse_format(data)

        elif data.startswith(PREFIX.TRANSFER):
            hash_value = data.removeprefix(PREFIX.TRANSFER)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.DEPLOY):
            hash_value = data.removeprefix(PREFIX.DEPLOY)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.BALANCE):
            hash_value = data.removeprefix(PREFIX.BALANCE)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.WITHDRAW):
            hash_value = data.removeprefix(PREFIX.WITHDRAW)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.DICTIONARY):
            hash_value = data.removeprefix(PREFIX.DICTIONARY)
            check_clkey_hash_format(hash_value)

        # system-entity-registry- tag 10
        elif data.startswith(PREFIX.SYSTEM_ENTITY_REGISTRY):
            hash_value = data.removeprefix(PREFIX.SYSTEM_ENTITY_REGISTRY)
            check_clkey_hash_format(hash_value)

        # era-summary- tag 11
        elif data.startswith(PREFIX.ERA_SUMMARY):
            hash_value = data.removeprefix(PREFIX.ERA_SUMMARY)
            check_clkey_hash_format(hash_value)

        elif data.startswith(PREFIX.ERA):
            check_era_key_format(data)

        # unbond- tag 12
        elif data.startswith(PREFIX.UNBOND):
            hash_value = data.removeprefix(PREFIX.UNBOND)
            check_clkey_hash_format(hash_value)

        # chainspec-registry- 13
        elif data.startswith(PREFIX.CHAINSPEC_REGISTRY):
            hash_value = data.removeprefix(PREFIX.CHAINSPEC_REGISTRY)
            check_clkey_hash_format(hash_value)

        # checksum-registry- 14
        elif data.startswith(PREFIX.CHECKSUM_REGISTRY):
            hash_value = data.removeprefix(PREFIX.CHECKSUM_REGISTRY)
            check_clkey_hash_format(hash_value)

            # bid-addr- 15
        elif data.startswith(PREFIX.BID_ADDR):
            check_clkey_bid_addr_format(data)

        elif data.startswith(PREFIX.BID):
            hash_value = data.removeprefix(PREFIX.BID)
            check_clkey_hash_format(hash_value)

        # package- 16
        elif data.startswith(PREFIX.PACKAGE):
            hash_value = data.removeprefix(PREFIX.PACKAGE)
            check_clkey_hash_format(hash_value)

        # byte-code- 18
        elif data.startswith(PREFIX.BYTE_CODE):
            check_byte_code_key_format(data)

        # message- 19
        elif data.startswith(PREFIX.MESSAGE):
            check_message_key_format(data)

        # named-key- 20
        elif data.startswith(PREFIX.NAMED_KEY):
            check_named_key_format(data)
            #
        elif data.startswith(PREFIX.BLOCK_GLOBAL):
            check_block_global_key_format(data)

        # entrypoint- 23
        elif data.startswith(PREFIX.ENTRY_POINT):
            check_entry_point_key_format(data)
        else:
            raise ValueError("invalid prefix")

        super().__init__(data)

    def serialize(self) -> bytes:
        """Serialize the CL key to bytes.

        Each key type is serialized with:
        1. A tag byte indicating the key type
        2. The key-specific serialized data

        Returns:
            Bytes representation of the CL key.
        """
        # account_hash tag 0
        if self.data.startswith(PREFIX.ACCOUNT_HASH):
            tag = int(ClKeyTAG.ACCOUNT_HASH.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.ACCOUNT_HASH)
            return tag + bytes.fromhex(value)

        # hash tag 1
        elif self.data.startswith(PREFIX.HASH):
            tag = int(ClKeyTAG.HASH.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.HASH)
            return tag + bytes.fromhex(value)

        # uref tag 2
        elif self.data.startswith(PREFIX.UREF):
            tag = int(ClKeyTAG.UREF.value).to_bytes(1, byteorder='little')
            temp = self.data.split('-')
            value = temp[1] + '{:02x}'.format(int(temp[2]))
            return tag + bytes.fromhex(value)

        # transfer tag 3
        elif self.data.startswith(PREFIX.TRANSFER):
            tag = int(ClKeyTAG.TRANSFER.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.TRANSFER)
            return tag + bytes.fromhex(value)

        # deploy tag 4
        elif self.data.startswith(PREFIX.DEPLOY):
            tag = int(ClKeyTAG.DEPLOY.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.DEPLOY)
            return tag + bytes.fromhex(value)

        # balance tag 6
        elif self.data.startswith(PREFIX.BALANCE):
            tag = int(ClKeyTAG.BALANCE.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.BALANCE)
            return tag + bytes.fromhex(value)

        # withdraw tag 8
        elif self.data.startswith(PREFIX.WITHDRAW):
            tag = int(ClKeyTAG.WITHDRAW.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.WITHDRAW)
            return tag + bytes.fromhex(value)

        # dictionary tag 9
        elif self.data.startswith(PREFIX.DICTIONARY):
            tag = int(ClKeyTAG.DICTIONARY.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.DICTIONARY)
            return tag + bytes.fromhex(value)

        # system-entity-registry- tag 10
        elif self.data.startswith(PREFIX.SYSTEM_ENTITY_REGISTRY):
            tag = int(ClKeyTAG.SYSTEM_ENTITY_REGISTRY.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.SYSTEM_ENTITY_REGISTRY)
            return tag + bytes.fromhex(value)

        # era-summary- tag 11
        elif self.data.startswith(PREFIX.ERA_SUMMARY):
            tag = int(ClKeyTAG.ERA_SUMMARY.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.ERA_SUMMARY)
            return tag + bytes.fromhex(value)

        # ERA tag 5
        elif self.data.startswith(PREFIX.ERA):
            tag = int(ClKeyTAG.ERA.value).to_bytes(1, byteorder='little')
            value = serialize_era_key(self.data)
            return tag + value

        # unbond- tag 12
        elif self.data.startswith(PREFIX.UNBOND):
            tag = int(ClKeyTAG.UNBOND.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.UNBOND)
            return tag + bytes.fromhex(value)

        # chainspec-registry- 13
        elif self.data.startswith(PREFIX.CHAINSPEC_REGISTRY):
            tag = int(ClKeyTAG.CHAINSPEC_REGISTRY.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.CHAINSPEC_REGISTRY)
            return tag + bytes.fromhex(value)

        # checksum-registry- 14
        elif self.data.startswith(PREFIX.CHECKSUM_REGISTRY):
            tag = int(ClKeyTAG.CHECKSUM_REGISTRY.value).to_bytes(
                1, byteorder='little')
            value = self.data.removeprefix(PREFIX.CHECKSUM_REGISTRY)
            return tag + bytes.fromhex(value)

        # bid-addr- 15
        elif self.data.startswith(PREFIX.BID_ADDR):
            tag = int(ClKeyTAG.BID_ADDR.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.BID_ADDR)
            return tag + bytes.fromhex(value)

        # bid- 17
        elif self.data.startswith(PREFIX.BID):
            tag = int(ClKeyTAG.BID.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.BID)
            return tag + bytes.fromhex(value)

        # package- 16
        elif self.data.startswith(PREFIX.PACKAGE):
            tag = int(ClKeyTAG.PACKAGE.value).to_bytes(1, byteorder='little')
            value = self.data.removeprefix(PREFIX.PACKAGE)
            return tag + bytes.fromhex(value)

        # byte-code- 18
        elif self.data.startswith(PREFIX.BYTE_CODE):
            tag = int(ClKeyTAG.BYTE_CODE.value).to_bytes(1, byteorder='little')
            value = serialize_bytes_code_key(self.data)
            return tag + value

         # message- 19
        elif self.data.startswith(PREFIX.MESSAGE):
            tag = int(ClKeyTAG.MESSAGE.value).to_bytes(1, byteorder='little')
            value = serialize_message_key(self.data)
            return tag + value
        # named-key- 20
        elif self.data.startswith(PREFIX.NAMED_KEY):
            tag = int(ClKeyTAG.NAMED_KEY.value).to_bytes(1, byteorder='little')
            value = serialize_named_key(self.data)
            return tag + value
        # block- 21
        elif self.data.startswith(PREFIX.BLOCK_GLOBAL):
            tag = int(ClKeyTAG.BLOCK_GLOBAL.value).to_bytes(
                1, byteorder='little')
            value = serialize_block_global_key(self.data)
            return tag + value

        # entrypoint- 23
        elif self.data.startswith(PREFIX.ENTRY_POINT):
            tag = int(ClKeyTAG.ENTRY_POINT.value).to_bytes(
                1, byteorder='little')
            value = serialize_entry_point_key(self.data)
            return tag + value
        else:
            raise ValueError("invalid prefix")
