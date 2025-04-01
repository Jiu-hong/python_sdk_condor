from .constants import JsonName, RuntimeKind
from .utils import CalltableSerialization

JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionNativeTarget:
    def to_bytes(self):
        table = CalltableSerialization()
        # table.addField(0, CLU8(0).serialize())
        table.addField(0, int(0).to_bytes())
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result[JSONNAME.TARGET] = JSONNAME.NATIVE
        return result
