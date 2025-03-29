import json
from cl_number import CLU32, CLU8
from cl_option import CLOption
from cl_string import CLString
from table import CalltableSerialization


class ByPackageNameInvocationTarget:

    def __init__(self, name: str, version: int = None):
        self.name = name  # string
        self.version = version

    def to_bytes(self):
        table = CalltableSerialization()

        version_bytes = b''
        if self.version is None:
            version_bytes = CLOption(None).serialize()
        else:
            version_bytes = CLOption(CLU32(self.version)).serialize()
        table.addField(0, CLU8(3).serialize()).addField(
            1, CLString(self.name).serialize()).addField(2, version_bytes)
        return table.to_bytes()

    def to_json(self):
        result = {}
        result["ByPackageName"] = {"name": self.name, "version": self.version}
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


a = ByPackageNameInvocationTarget("my_hash")
# print(a.to_json())
