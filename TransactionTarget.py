
from TransactionInvocationTarget import TransactionInvocationTarget
from TransactionRuntime import TransactionRuntime
from TransactionSessionTarget import TransactionSessionTarget
from cl_number import CLU8
from table import CalltableSerialization


class TransactionTarget:
    def __init__(self, target_kind, *kw):
        self.target_kind = target_kind
        self.kw = kw

    def to_bytes(self):
        match self.target_kind:
            case "native":
                table = CalltableSerialization()
                table.addField(0, CLU8(0).serialize())
                return table.to_bytes()
            case "stored":
                return TransactionInvocationTarget(*self.kw).to_bytes()
            case "session":
                return TransactionSessionTarget(*self.kw).to_bytes()

    def serialize(self):

        match self.target_kind:
            case "native":
                return CLU8(0).serialize()
            case "stored":
                return CLU8(1).serialize() + TransactionInvocationTarget(*self.kw).serialize() + TransactionRuntime().serialize()
            case "session":
                return CLU8(2).serialize() + TransactionSessionTarget(*self.kw).serialize() + TransactionRuntime().serialize()

# ok
    def to_json(self):
        result = {}
        match self.target_kind:
            case "native":
                result["target"] = "Native"
            case "stored":
                result["target"] = TransactionInvocationTarget(
                    *self.kw).to_json()
            case "session":
                result["target"] = TransactionSessionTarget(*self.kw).to_json()

        return result


target = TransactionTarget("stored", "InvocableEntity",
                           "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
print("target is:", target.to_bytes().hex())

f = open("wasm", "r")
module_bytes = f.read()
target2 = TransactionTarget("session", module_bytes, True)
print("target2 is:", target2.to_bytes().hex())

print("target json is:", target.to_json())
