import re
from python_condor.transaction_runtime import TransactionRuntime
from .call_table_serialization import CalltableSerialization
from .cl_values import CLU32, CLU8, CLOption
from .constants import JsonName


JSONNAME = JsonName()


class PackageHashTarget:
    def __init__(self, runtime: str, package_hash: str, version: int = None):
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(package_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "package-hash should only contain alphabet and number(64 length)")
        self.package_hash = package_hash  # hex string
        self.version = version
        self.runtime = runtime

    def to_bytes(self):
        selftable = CalltableSerialization()

        version_bytes = b''
        if self.version is None:
            version_bytes = bytes.fromhex("00")
        else:
            version_bytes = CLOption(CLU32(self.version)).serialize()
        selftable.addField(0, CLU8(2).serialize()).addField(
            1, bytes.fromhex(self.package_hash)).addField(2, version_bytes)
        # return selftable.to_bytes()
        table = CalltableSerialization()
        table.addField(0, int(1).to_bytes()).addField(
            1, selftable.to_bytes()).addField(
            2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self):
        # result = {}
        # result[JSONNAME.BYPACKAGEHASH] = {
        #     JSONNAME.ADDR: self.package_hash, JSONNAME.VERSION: self.version}
        # return result
        result = {}
        result_2 = {}
        result_3 = {}
        result_4 = {}
        result_4[JSONNAME.BYPACKAGEHASH] = {
            JSONNAME.ADDR: self.package_hash, JSONNAME.VERSION: self.version}
        result_3[JSONNAME.ID] = result_4
        result_3[JSONNAME.RUNTIME] = self.runtime
        result_2[JSONNAME.STORED] = result_3
        result[JSONNAME.TARGET] = result_2
        return result

# By package hash
# 7ac469fbaaace9fadb60f0ca43389842ca137698de7b417cead5a213a355ed30
        # "target": {
        #     "Stored": {
        #         "id": {
        #             "ByPackageHash": {
        #                 "addr": "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56",
        #                 "version": null
        #             }
        #         },
        #         "runtime": "VmCasperV1"
        #     }
        # }


# a = ByPackageHashInvocationTarget(
#     "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# # print(a.to_json())
