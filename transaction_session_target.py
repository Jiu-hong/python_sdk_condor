from transaction_runtime import TransactionRuntime
from cl_number import CLU32, CLU8, CLBool

from constants.cons_jsonname import JsonName
from constants.const_runtime import RuntimeKind
from call_table_serialization import CalltableSerialization

JSONNAME = JsonName()

RUNTIME = RuntimeKind()


class TransactionSessionTarget:
    def __init__(self, module_bytes: str, is_install_upgrade: bool = False):

        self.module_bytes = bytes.fromhex(module_bytes)
        self.is_install_upgrade = is_install_upgrade

    def to_bytes(self):

        module_bytes_length = CLU32(len(self.module_bytes)).serialize()
        table = CalltableSerialization()
        table.addField(0, int(2).to_bytes()).addField(
            1, CLBool(self.is_install_upgrade).serialize()).addField(
            2, TransactionRuntime().to_bytes()).addField(
            3, module_bytes_length+self.module_bytes)
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result[JSONNAME.SESSION] = {JSONNAME.IS_INSTALL_UPGRADE: self.is_install_upgrade,
                                    JSONNAME.MODULEBYTES: self.module_bytes.hex(), JSONNAME.RUNTIME: RUNTIME.VMCASPERV1}
        return result


f = open("wasm", "r")
module_bytes = f.read()
a = TransactionSessionTarget(module_bytes).to_bytes()
