
from .transaction_invocation_target import TransactionInvocationTarget
from .transaction_runtime import TransactionRuntime


from .constants import JsonName, RuntimeKind
from .call_table_serialization import CalltableSerialization


JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionStoredTarget:
    def __init__(self, runtime, *id):
        self.runtime = runtime
        self.id = TransactionInvocationTarget(*id)

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, int(1).to_bytes()).addField(
            1, self.id.to_bytes()).addField(
            2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result[JSONNAME.STORED] = {
            **self.id.to_json(),
            JSONNAME.RUNTIME: self.runtime
        }
        return result
