from .call_table_serialization import CalltableSerialization
from .constants import JsonName, RuntimeKind

from .transaction_invocation_target import TransactionInvocationTarget
from .transaction_runtime import TransactionRuntime


JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionNativeTarget:
    # def __init__(self, runtime, *id):
    #     self.runtime = runtime
    #     self.id = TransactionInvocationTarget(*id)

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
