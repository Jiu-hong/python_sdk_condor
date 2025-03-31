
from .constants import JsonName

JSONNAME = JsonName()


class InvocableEntityTarget:
    def __init__(self, contract_hash: str):
        self.contract_hash = contract_hash

    def to_bytes(self):
        pass

    def to_json(self):
        result = {}
        result[JSONNAME.BYHASH] = self.contract_hash
        return result


# By contract hash
# f3469257d7c361b80def54eda2a7ca794e9280229287bd9c997e1980485648d8
        # "target": {
        #     "Stored": {
        #         "id": {
        #             "ByHash": "7af6303b6e7d8f0fc0b5e9510034d9c818b30c7db43b2ef6e5f595357270451e"
        #         },
        #         "runtime": "VmCasperV1"
        #     }
        # }
# a = InvocableEntityTarget(
#     "7af6303b6e7d8f0fc0b5e9510034d9c818b30c7db43b2ef6e5f595357270451e")
# print(a.to_json())
