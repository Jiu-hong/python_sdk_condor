from ..constants import JsonName, RuntimeKind
from ..utils import CalltableSerialization

JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionNativeTarget:
    def to_bytes(self):
        table = CalltableSerialization()
        table.add_field(0, int(0).to_bytes())
        return table.to_bytes()

    def to_json(self):
        result = {}
        result[JSONNAME.TARGET] = JSONNAME.NATIVE
        return result
