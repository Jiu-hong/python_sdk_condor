from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG, Prefix, ClKeyTAG
from ..utils import check_clkey_bid_addr_format, check_clkey_hash_format, check_purse_format

PREFIX = Prefix()


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def __init__(self, data):
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
            try:
                int(data.removeprefix(PREFIX.ERA))
            except:
                raise ValueError("era value should be int")

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
            rest_hex = data.removeprefix(PREFIX.BYTE_CODE)
            if rest_hex.startswith(PREFIX.V1_WASM):
                bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
            elif rest_hex.startswith(PREFIX.V2_WASM):
                bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
            elif rest_hex.startswith(PREFIX.EMPTY):
                bytescode_hex = ""
            else:
                raise ValueError("invalid byte-code-xxx")
            try:
                bytes.fromhex(bytescode_hex)
            except:
                raise ValueError("bytescode should be hex string")
        # message- 19 todo
        else:
            raise ValueError("invalid prefix")

        super().__init__(data)

    def serialize(self):

        if self.data.startswith(PREFIX.ACCOUNT_HASH):
            tag = int(ClKeyTAG.ACCOUNT_HASH.value).to_bytes()
            value = self.data.removeprefix(PREFIX.ACCOUNT_HASH)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.HASH):
            tag = int(ClKeyTAG.HASH.value).to_bytes()
            value = self.data.removeprefix(PREFIX.HASH)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.UREF):
            tag = int(ClKeyTAG.UREF.value).to_bytes()
            temp = self.data.split('-')
            value = temp[1] + '{:02x}'.format(int(temp[2]))
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.TRANSFER):
            tag = int(ClKeyTAG.TRANSFER.value).to_bytes()
            value = self.data.removeprefix(PREFIX.TRANSFER)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.DEPLOY):
            tag = int(ClKeyTAG.DEPLOY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.DEPLOY)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.BALANCE):
            tag = int(ClKeyTAG.BALANCE.value).to_bytes()
            value = self.data.removeprefix(PREFIX.BALANCE)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.WITHDRAW):
            tag = int(ClKeyTAG.WITHDRAW.value).to_bytes()
            value = self.data.removeprefix(PREFIX.WITHDRAW)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.DICTIONARY):
            tag = int(ClKeyTAG.DICTIONARY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.DICTIONARY)
            return tag + bytes.fromhex(value)

        # system-entity-registry- tag 10
        elif self.data.startswith(PREFIX.SYSTEM_ENTITY_REGISTRY):
            tag = int(ClKeyTAG.SYSTEM_ENTITY_REGISTRY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.SYSTEM_ENTITY_REGISTRY)
            return tag + bytes.fromhex(value)

        # era-summary- tag 11
        elif self.data.startswith(PREFIX.ERA_SUMMARY):
            tag = int(ClKeyTAG.ERA_SUMMARY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.ERA_SUMMARY)
            return tag + bytes.fromhex(value)

        elif self.data.startswith(PREFIX.ERA):
            tag = int(ClKeyTAG.ERA.value).to_bytes()
            era_int = int(self.data.removeprefix(PREFIX.ERA))
            value = era_int.to_bytes(8, byteorder='little')
            return tag + value
        # unbond- tag 12
        elif self.data.startswith(PREFIX.UNBOND):
            tag = int(ClKeyTAG.UNBOND.value).to_bytes()
            value = self.data.removeprefix(PREFIX.UNBOND)
            return tag + bytes.fromhex(value)

        # chainspec-registry- 13
        elif self.data.startswith(PREFIX.CHAINSPEC_REGISTRY):
            tag = int(ClKeyTAG.CHAINSPEC_REGISTRY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.CHAINSPEC_REGISTRY)
            return tag + bytes.fromhex(value)

        # checksum-registry- 14
        elif self.data.startswith(PREFIX.CHECKSUM_REGISTRY):
            tag = int(ClKeyTAG.CHECKSUM_REGISTRY.value).to_bytes()
            value = self.data.removeprefix(PREFIX.CHECKSUM_REGISTRY)
            return tag + bytes.fromhex(value)

        # bid-addr- 15
        elif self.data.startswith(PREFIX.BID_ADDR):
            tag = int(ClKeyTAG.BID_ADDR.value).to_bytes()
            value = self.data.removeprefix(PREFIX.BID_ADDR)
            return tag + bytes.fromhex(value)

        # bid tag 7 "bid-"
        elif self.data.startswith(PREFIX.BID):
            tag = int(ClKeyTAG.BID.value).to_bytes()
            value = self.data.removeprefix(PREFIX.BID)
            return tag + bytes.fromhex(value)

        # package- 16
        elif self.data.startswith(PREFIX.PACKAGE):
            tag = int(ClKeyTAG.PACKAGE.value).to_bytes()
            value = self.data.removeprefix(PREFIX.PACKAGE)
            return tag + bytes.fromhex(value)

        # byte-code- 18

        elif self.data.startswith(PREFIX.BYTE_CODE):
            tag = int(ClKeyTAG.BYTE_CODE.value).to_bytes()
            rest_hex = self.data.removeprefix(PREFIX.BYTE_CODE)
            if rest_hex.startswith(PREFIX.V1_WASM):
                bytescode_hex = rest_hex.removeprefix(PREFIX.V1_WASM)
                value = int(1).to_bytes() + bytes.fromhex(bytescode_hex)
            elif rest_hex.startswith(PREFIX.V2_WASM):
                bytescode_hex = rest_hex.removeprefix(PREFIX.V2_WASM)
                value = int(2).to_bytes() + bytes.fromhex(bytescode_hex)
            else:
                value = int(0).to_bytes()
            return tag + value

        # message- 19 todo
        else:
            raise ValueError("invalid prefix")
