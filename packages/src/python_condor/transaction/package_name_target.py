from ..constants import JsonName
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization, serialize_string

JSONNAME = JsonName()


class PackageNameTarget:
    def __init__(self, runtime: str, name: str, version: int = None):
        self.package_name = name  # string
        self.version = version
        self.runtime = runtime

    def to_bytes(self):
        selftable = CalltableSerialization()

        version_bytes = b''
        if self.version is None:
            version_bytes = int(0).to_bytes()
        else:
            version_bytes = int(1).to_bytes() + \
                (self.version).to_bytes(4, byteorder='little')
        selftable.addField(0, int(3).to_bytes()).addField(
            1, serialize_string(self.package_name)).addField(2, version_bytes)

        table = CalltableSerialization()
        table.addField(0, int(1).to_bytes()).addField(
            1, selftable.to_bytes()).addField(
            2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self):
        result = {}
        result_2 = {}
        result_3 = {}
        result_4 = {}
        result_4[JSONNAME.BYPACKAGENAME] = {
            JSONNAME.NAME: self.package_name, JSONNAME.VERSION: self.version}
        result_3[JSONNAME.ID] = result_4
        result_3[JSONNAME.RUNTIME] = self.runtime
        result_2[JSONNAME.STORED] = result_3
        result[JSONNAME.TARGET] = result_2
        return result

        # explore 7be243df8aca5c9e4986dfc53e3295e63ecb356707269cc87346061c8b750040
        # "target": {
        #     "Stored": {
        #         "id": {
        #             "ByPackageName": {
        #                 "name": "my_hash",
        #                 "version": null
        #             }
        #         },
        #         "runtime": "VmCasperV1"
        #     }
        # }

        # a = ByPackageNameInvocationTarget("my_hash")
        # print(a.to_json())
