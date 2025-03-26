from TransactionRuntime import TransactionRuntime
from cl_number import CLU32, CLU8, CLBool

from table import CalltableSerialization


class TransactionSessionTarget:
    def __init__(self, module_bytes, is_install_upgrade=False):

        self.module_bytes = bytes.fromhex(module_bytes)
        self.is_install_upgrade = is_install_upgrade

    def to_bytes(self):
        # print("self:", self.module_bytes, self.is_install_upgrade)
        module_bytes_length = CLU32(len(self.module_bytes)).serialize()
        print("module_bytes_length is:", module_bytes_length)
        table = CalltableSerialization()
        table.addField(0, int(2).to_bytes()).addField(
            1, CLBool(self.is_install_upgrade).serialize()).addField(
            2, TransactionRuntime().to_bytes()).addField(
            3, module_bytes_length+self.module_bytes)
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result["Session"] = {"is_install_upgrade": self.is_install_upgrade,
                             "module_bytes": self.module_bytes.hex(), "runtime": "VmCasperV1"}
        return result


f = open("wasm", "r")
module_bytes = f.read()
a = TransactionSessionTarget(module_bytes).to_bytes()
