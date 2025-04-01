from .utils import CalltableSerialization
from .constants import JsonName, RuntimeKind

from .transaction_invocation_target import TransactionInvocationTarget
from .transaction_runtime import TransactionRuntime


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
        result_inner = {}

        result_inner[JSONNAME.STORED] = {
            **self.id.to_json(),
            JSONNAME.RUNTIME: self.runtime
        }
        result[JSONNAME.TARGET] = result_inner

        return result
