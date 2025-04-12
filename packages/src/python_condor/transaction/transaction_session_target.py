from ..constants import JsonName, RuntimeKind
from .transaction_runtime import TransactionRuntime
from ..utils import CalltableSerialization


JSONNAME = JsonName()

RUNTIME = RuntimeKind()


class TransactionSessionTarget:
    def __init__(self, runtime: str, module_bytes: str, is_install_upgrade: bool = False):

        self.module_bytes = bytes.fromhex(module_bytes)
        self.is_install_upgrade = is_install_upgrade
        self.runtime = runtime

    def to_bytes(self):
        module_bytes_length = len(
            self.module_bytes).to_bytes(4, byteorder='little')
        table = CalltableSerialization()
        table.add_field(0, int(2).to_bytes()).add_field(
            1, self.is_install_upgrade.to_bytes()).add_field(
            2, TransactionRuntime(self.runtime).to_bytes()).add_field(
            3, module_bytes_length+self.module_bytes)
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result_inner = {}
        result_inner[JSONNAME.TRANSACTION_SESSION] = {JSONNAME.IS_INSTALL_UPGRADE: self.is_install_upgrade,
                                                      JSONNAME.MODULE_BYTES: self.module_bytes.hex(), JSONNAME.RUNTIME: self.runtime}
        result[JSONNAME.TARGET] = result_inner
        return result


# f = open("wasm", "r")
# module_bytes = f.read()
# a = TransactionSessionTarget(module_bytes).to_bytes()
