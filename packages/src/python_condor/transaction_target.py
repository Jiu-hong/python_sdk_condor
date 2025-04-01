from python_condor.transaction_native_target import TransactionNativeTarget
from .call_table_serialization import CalltableSerialization
from .cl_values import CLU8
from .constants import JsonName, TargetKind
from .transaction_session_target import TransactionSessionTarget
from .transaction_stored_target import TransactionStoredTarget


CONST = TargetKind()
VALID_TARGETS = (CONST.NATIVE, CONST.STORED, CONST.SESSION)
JSONNAME = JsonName()


class TransactionTarget:
    def __init__(self, runtime: str, target_kind: str, *args):
        if target_kind not in VALID_TARGETS:
            raise ValueError(
                f"Invalid input: {target_kind}. Allowed values are: {VALID_TARGETS}")
        self.target_kind = target_kind
        self.args = args
        self.runtime = runtime

    def to_bytes(self):
        match self.target_kind:
            case CONST.NATIVE:
                # table = CalltableSerialization()
                # # table.addField(0, CLU8(0).serialize())
                # table.addField(0, int(0).to_bytes())
                # return table.to_bytes()
                return TransactionNativeTarget().to_bytes()
            case CONST.STORED:
                return TransactionStoredTarget(self.runtime, *self.args).to_bytes()
            case CONST.SESSION:
                return TransactionSessionTarget(self.runtime, *self.args).to_bytes()

    def to_json(self):
        result = {}
        match self.target_kind:
            case CONST.NATIVE:
                result[JSONNAME.TARGET] = JSONNAME.NATIVE
            case CONST.STORED:
                result[JSONNAME.TARGET] = TransactionStoredTarget(
                    self.runtime, *self.args).to_json()
            case CONST.SESSION:
                result[JSONNAME.TARGET] = TransactionSessionTarget(
                    self.runtime, *self.args).to_json()

        return result


# target = TransactionTarget("stored", "InvocableEntity",
#                            "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# # print("target is:", target.to_bytes().hex())

# f = open("wasm", "r")
# module_bytes = f.read()
# target2 = TransactionTarget("session", module_bytes, True)
# print("target2 is:", target2.to_bytes().hex())

# print("target json is:", target.to_json())
# target = TransactionTarget("helo", "InvocableEntity",
#                            "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# target
