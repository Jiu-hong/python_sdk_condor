from .call_table_serialization import CalltableSerialization
from .cl_values import CLU8
from .constants import JsonName, RuntimeKind

CONST = RuntimeKind()
VALID_ALLOWED_RUNTIME = (CONST.VMCASPERV1)

JSONNAME = JsonName()


class TransactionRuntime:
    def __init__(self, runtime: str = CONST.VMCASPERV1):
        if runtime not in VALID_ALLOWED_RUNTIME:
            raise ValueError(
                f"Invalid input {runtime}. Allowed values are: {VALID_ALLOWED_RUNTIME}")
        self.runtime = runtime

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, CLU8(0).serialize())
        return table.to_bytes()

    def serialize(self):
        return CLU8(0).serialize()

    def to_json(self):
        result = {}
        result[JSONNAME.RUNTIME] = self.runtime
        return result


a = TransactionRuntime()
# print(a.to_bytes().hex())

# expect:
# 010000000000000000000100000000
# 010101000100010100
