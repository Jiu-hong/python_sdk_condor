from ..utils import check_bid_addr_format
from .cl_basetype import CLAtomic, CLValue
from ..constants import TAG


class CLKey(CLValue, CLAtomic):
    tag = TAG.CLKey.value

    def serialize(self):

        if self.data.startswith("account-hash-"):
            result = '00' + self.data.removeprefix('account-hash-')
            return bytes.fromhex(result)

        elif self.data.startswith("hash-"):
            result = '01'+self.data.removeprefix('hash-')
            return bytes.fromhex(result)

        elif self.data.startswith("uref-"):
            temp = self.data.split('-')
            result = '02' + temp[1] + '{:02x}'.format(int(temp[2]))
            return bytes.fromhex(result)

        elif self.data.startswith("transfer-"):
            result = '03'+self.data.removeprefix('transfer-')
            return bytes.fromhex(result)

        elif self.data.startswith("deploy-"):
            result = '04'+self.data.removeprefix('deploy-')
            return bytes.fromhex(result)

        elif self.data.startswith("era-"):
            era_int = int(self.data.removeprefix('era-'))
            result = bytes.fromhex(
                '05') + era_int.to_bytes(8, byteorder='little')
            return result

        elif self.data.startswith("balance-"):
            result = '06'+self.data.removeprefix('balance-')
            return bytes.fromhex(result)

        elif self.data.startswith("withdraw-"):
            result = '08'+self.data.removeprefix('withdraw-')
            return bytes.fromhex(result)

        elif self.data.startswith("dictionary-"):
            result = '09'+self.data.removeprefix('dictionary-')
            return bytes.fromhex(result)

        # system-contract-registry- tag 10
        elif self.data.startswith("system-contract-registry-"):
            result = '0a'+self.data.removeprefix('system-contract-registry-')
            return bytes.fromhex(result)

        # era-summary- tag 11
        elif self.data.startswith("era-summary-"):
            result = '0b'+self.data.removeprefix('era-summary-')
            return bytes.fromhex(result)

        # unbond- tag 12
        elif self.data.startswith("unbond-"):
            result = '0c'+self.data.removeprefix('unbond-')
            return bytes.fromhex(result)

        # chainspec-registry- 13
        elif self.data.startswith("chainspec-registry-"):
            result = '0d'+self.data.removeprefix('chainspec-registry-')
            return bytes.fromhex(result)

        # checksum-registry- 14
        elif self.data.startswith("checksum-registry-"):
            result = '0e'+self.data.removeprefix('checksum-registry-')
            return bytes.fromhex(result)

        # bid-addr- 15
        elif self.data.startswith("bid-addr-"):
            check_bid_addr_format(self.data)
            result = '0f' + self.data.removeprefix("bid-addr-")
            return bytes.fromhex(result)

        # bid tag 7 "bid-"
        elif self.data.startswith("bid-"):
            result = '07'+self.data.removeprefix('bid-')
            return bytes.fromhex(result)

        # package- 16
        elif self.data.startswith("package-"):
            result = '0g'+self.data.removeprefix('package-')
            return bytes.fromhex(result)

        # byte-code- 18
        elif self.data.startswith("byte-code-"):
            bytescode_hex = self.data.removeprefix("byte-code-")
            if len(bytescode_hex) > 0:
                result = int(1).to_bytes(1) + bytes.fromhex(bytescode_hex)
            else:
                result = int(0).to_bytes(1)
            return bytes.fromhex('0i') + result

        # message- 19 todo
        else:
            raise
