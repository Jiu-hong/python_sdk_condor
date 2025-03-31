from .call_table_serialization import CalltableSerialization
from .cl_values import CLU32, CLU8, CLOption
from .constants import JsonName


JSONNAME = JsonName()


class ByPackageHashInvocationTarget:
    def __init__(self, package_hash: str, version: int = None):
        self.package_hash = package_hash  # hex string
        self.version = version

    def to_bytes(self):
        table = CalltableSerialization()

        version_bytes = b''
        if self.version is None:
            version_bytes = bytes.fromhex("00")
        else:
            version_bytes = CLOption(CLU32(self.version)).serialize()
        table.addField(0, CLU8(2).serialize()).addField(
            1, bytes.fromhex(self.package_hash)).addField(2, version_bytes)
        return table.to_bytes()

    def to_json(self):
        result = {}
        result[JSONNAME.BYPACKAGEHASH] = {
            JSONNAME.ADDR: self.package_hash, JSONNAME.VERSION: self.version}
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
