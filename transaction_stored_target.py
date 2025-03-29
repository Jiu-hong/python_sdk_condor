
from transaction_invocation_target import TransactionInvocationTarget
from transaction_runtime import TransactionRuntime
from cl_number import CLU32, CLU8, CLBool

from constants.cons_jsonname import JsonName
from constants.const_runtime import RuntimeKind
from call_table_serialization import CalltableSerialization


JSONNAME = JsonName()
RUNTIME = RuntimeKind()


class TransactionStoredTarget:
    def __init__(self, *id):
        self.id = TransactionInvocationTarget(*id)

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, int(1).to_bytes()).addField(
            1, self.id.to_bytes()).addField(
            2, TransactionRuntime().to_bytes())
        return table.to_bytes()

# ok
    def to_json(self):
        result = {}
        result[JSONNAME.STORED] = {
            **self.id.to_json(),
            JSONNAME.RUNTIME: RUNTIME.VMCASPERV1
        }
        return result
