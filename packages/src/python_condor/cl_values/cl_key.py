from ..utils import check_bid_addr_format
from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG, Prefix

PREFIX = Prefix()


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):

        if self.data.startswith(PREFIX.ACCOUNT_HASH):
            result = '00' + self.data.removeprefix(PREFIX.ACCOUNT_HASH)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.HASH):
            result = '01'+self.data.removeprefix(PREFIX.HASH)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.UREF):
            temp = self.data.split('-')
            result = '02' + temp[1] + '{:02x}'.format(int(temp[2]))
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.TRANSFER):
            result = '03'+self.data.removeprefix(PREFIX.TRANSFER)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.DEPLOY):
            result = '04'+self.data.removeprefix(PREFIX.DEPLOY)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.ERA):
            era_int = int(self.data.removeprefix(PREFIX.ERA))
            result = bytes.fromhex(
                '05') + era_int.to_bytes(8, byteorder='little')
            return result

        elif self.data.startswith(PREFIX.BALANCE):
            result = '06'+self.data.removeprefix(PREFIX.BALANCE)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.WITHDRAW):
            result = '08'+self.data.removeprefix(PREFIX.WITHDRAW)
            return bytes.fromhex(result)

        elif self.data.startswith(PREFIX.DICTIONARY):
            result = '09'+self.data.removeprefix(PREFIX.DICTIONARY)
            return bytes.fromhex(result)

        # system-contract-registry- tag 10
        elif self.data.startswith(PREFIX.SYSTEM_CONTRACT_REGISTRY):
            result = '0a' + \
                self.data.removeprefix(PREFIX.SYSTEM_CONTRACT_REGISTRY)
            return bytes.fromhex(result)

        # era-summary- tag 11
        elif self.data.startswith(PREFIX.ERA_SUMMARY):
            result = '0b'+self.data.removeprefix(PREFIX.ERA_SUMMARY)
            return bytes.fromhex(result)

        # unbond- tag 12
        elif self.data.startswith(PREFIX.UNBOND):
            result = '0c'+self.data.removeprefix(PREFIX.UNBOND)
            return bytes.fromhex(result)

        # chainspec-registry- 13
        elif self.data.startswith(PREFIX.CHAINSPEC_REGISTRY):
            result = '0d'+self.data.removeprefix(PREFIX.CHAINSPEC_REGISTRY)
            return bytes.fromhex(result)

        # checksum-registry- 14
        elif self.data.startswith(PREFIX.CHECKSUM_REGISTRY):
            result = '0e'+self.data.removeprefix(PREFIX.CHECKSUM_REGISTRY)
            return bytes.fromhex(result)

        # bid-addr- 15
        elif self.data.startswith(PREFIX.BID_ADDR):
            check_bid_addr_format(self.data)
            result = '0f' + self.data.removeprefix(PREFIX.BID_ADDR)
            return bytes.fromhex(result)

        # bid tag 7 "bid-"
        elif self.data.startswith(PREFIX.BID):
            result = '07'+self.data.removeprefix(PREFIX.BID)
            return bytes.fromhex(result)

        # package- 16
        elif self.data.startswith(PREFIX.PACKAGE):
            result = '0g'+self.data.removeprefix(PREFIX.PACKAGE)
            return bytes.fromhex(result)

        # byte-code- 18
        elif self.data.startswith(PREFIX.BYTE_CODE):
            bytescode_hex = self.data.removeprefix(PREFIX.BYTE_CODE)
            if len(bytescode_hex) > 0:
                result = int(1).to_bytes(1) + bytes.fromhex(bytescode_hex)
            else:
                result = int(0).to_bytes(1)
            return bytes.fromhex('0i') + result

        # message- 19 todo
        else:
            raise
