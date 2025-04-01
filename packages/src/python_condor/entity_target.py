
import re
from .utils import CalltableSerialization
from .transaction_runtime import TransactionRuntime
from .constants import JsonName

JSONNAME = JsonName()


class EntityTarget:
    def __init__(self, runtime: str, contract_hash: str):
        regx = "([0-9a-z]{64})"
        pattern = re.compile(regx)
        result = pattern.fullmatch(contract_hash)
        if not isinstance(result, re.Match):
            raise ValueError(
                "contract-hash should only contain alphabet and number(64 length)")
        self.contract_hash = contract_hash
        self.runtime = runtime

    def to_bytes(self):
        selftable = CalltableSerialization()
        selftable.addField(0, int(0).to_bytes()).\
            addField(1, bytes.fromhex(self.contract_hash))

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
        result_4[JSONNAME.BYHASH] = self.contract_hash
        result_3[JSONNAME.ID] = result_4
        result_3[JSONNAME.RUNTIME] = self.runtime
        result_2[JSONNAME.STORED] = result_3
        result[JSONNAME.TARGET] = result_2
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
# a = EntityTarget(
#     "7af6303b6e7d8f0fc0b5e9510034d9c818b30c7db43b2ef6e5f595357270451e")
# print(a.to_json())
