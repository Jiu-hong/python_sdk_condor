from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG, Prefix, ClKeyTAG
from ..utils import check_bid_addr_format

PREFIX = Prefix()


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):

        if self.data.startswith(PREFIX.ACCOUNT_HASH):
            tag = int(ClKeyTAG.ACCOUNT_HASH.value).to_bytes()
            result = self.data.removeprefix(PREFIX.ACCOUNT_HASH)
            # tag = int(self.tag).to_bytes(1, byteorder='little')
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.HASH):
            tag = int(ClKeyTAG.HASH.value).to_bytes()
            result = self.data.removeprefix(PREFIX.HASH)
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.UREF):
            tag = int(ClKeyTAG.UREF.value).to_bytes()
            temp = self.data.split('-')
            result = temp[1] + '{:02x}'.format(int(temp[2]))
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.TRANSFER):
            tag = int(ClKeyTAG.TRANSFER.value).to_bytes()
            result = self.data.removeprefix(PREFIX.TRANSFER)
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.DEPLOY):
            tag = int(ClKeyTAG.DEPLOY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.DEPLOY)
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.ERA):
            tag = int(ClKeyTAG.ERA.value).to_bytes()
            era_int = int(self.data.removeprefix(PREFIX.ERA))
            result = era_int.to_bytes(8, byteorder='little')
            return tag + result

        elif self.data.startswith(PREFIX.BALANCE):
            tag = int(ClKeyTAG.BALANCE.value).to_bytes()
            result = self.data.removeprefix(PREFIX.BALANCE)
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.WITHDRAW):
            tag = int(ClKeyTAG.WITHDRAW.value).to_bytes()
            result = self.data.removeprefix(PREFIX.WITHDRAW)
            return tag + bytes.fromhex(result)

        elif self.data.startswith(PREFIX.DICTIONARY):
            tag = int(ClKeyTAG.DICTIONARY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.DICTIONARY)
            return tag + bytes.fromhex(result)

        # system-contract-registry- tag 10
        elif self.data.startswith(PREFIX.SYSTEM_CONTRACT_REGISTRY):
            tag = int(ClKeyTAG.SYSTEM_CONTRACT_REGISTRY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.SYSTEM_CONTRACT_REGISTRY)
            return tag + bytes.fromhex(result)

        # era-summary- tag 11
        elif self.data.startswith(PREFIX.ERA_SUMMARY):
            tag = int(ClKeyTAG.ERA_SUMMARY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.ERA_SUMMARY)
            return tag + bytes.fromhex(result)

        # unbond- tag 12
        elif self.data.startswith(PREFIX.UNBOND):
            tag = int(ClKeyTAG.UNBOND.value).to_bytes()
            result = self.data.removeprefix(PREFIX.UNBOND)
            return tag + bytes.fromhex(result)

        # chainspec-registry- 13
        elif self.data.startswith(PREFIX.CHAINSPEC_REGISTRY):
            tag = int(ClKeyTAG.CHAINSPEC_REGISTRY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.CHAINSPEC_REGISTRY)
            return tag + bytes.fromhex(result)

        # checksum-registry- 14
        elif self.data.startswith(PREFIX.CHECKSUM_REGISTRY):
            tag = int(ClKeyTAG.CHECKSUM_REGISTRY.value).to_bytes()
            result = self.data.removeprefix(PREFIX.CHECKSUM_REGISTRY)
            return tag + bytes.fromhex(result)

        # bid-addr- 15
        elif self.data.startswith(PREFIX.BID_ADDR):
            tag = int(ClKeyTAG.BID_ADDR.value).to_bytes()
            check_bid_addr_format(self.data)
            result = self.data.removeprefix(PREFIX.BID_ADDR)
            return tag + bytes.fromhex(result)

        # bid tag 7 "bid-"
        elif self.data.startswith(PREFIX.BID):
            tag = int(ClKeyTAG.BID.value).to_bytes()
            result = self.data.removeprefix(PREFIX.BID)
            return tag + bytes.fromhex(result)

        # package- 16
        elif self.data.startswith(PREFIX.PACKAGE):
            tag = int(ClKeyTAG.PACKAGE.value).to_bytes()
            result = self.data.removeprefix(PREFIX.PACKAGE)
            return tag + bytes.fromhex(result)

        # byte-code- 18
        elif self.data.startswith(PREFIX.BYTE_CODE):
            tag = int(ClKeyTAG.BYTE_CODE.value).to_bytes()
            bytescode_hex = self.data.removeprefix(PREFIX.BYTE_CODE)
            if len(bytescode_hex) > 0:
                result = int(1).to_bytes(1) + bytes.fromhex(bytescode_hex)
            else:
                result = int(0).to_bytes(1)
            return tag + result

        # message- 19 todo
        else:
            raise
