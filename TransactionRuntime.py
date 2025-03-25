from cl_number import CLU8
from table import CalltableSerialization


class TransactionRuntime:
    def __init__(self, runtime="VmCasperV1"):
        self.runtime = runtime

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, CLU8(0).serialize())
        return table.to_bytes()

    def serialize(self):
        return CLU8(0).serialize()

    def to_json(self):
        result = {}
        result["runtime"] = self.runtime
        return result
