import json
from ByPackageHashInvocationTarget import ByPackageHashInvocationTarget
from ByPackageNameInvocationTarget import ByPackageNameInvocationTarget
from InvocableEntityAliasTarget import InvocableEntityAliasTarget
from InvocableEntityTarget import InvocableEntityTarget
from cl_number import CLU32, CLU8
from cl_option import CLOption
from cl_string import CLString
from constants.cons_jsonname import JsonName
from constants.const_Invocation import InvocationKind
from table import CalltableSerialization

CONST = InvocationKind()
VALID_ALLOWED_INVOCATION = (
    CONST.INVOCABLEENTITY, CONST.INVOCABLEENTITYALIAS, CONST.PACKAGE, CONST.PACKAGEALIAS)

JSONNAME = JsonName()


class TransactionInvocationTarget:
    def __init__(self, invocation_kind: str, *args: str):
        if invocation_kind not in VALID_ALLOWED_INVOCATION:
            raise ValueError(
                f"Invalid input: {invocation_kind}. Allowed values are: {VALID_ALLOWED_INVOCATION}")
        self.invocation_kind = invocation_kind
        self.args = args

    def to_bytes(self):
        match self.invocation_kind:
            case CONST.INVOCABLEENTITY:
                table = CalltableSerialization()
                table.addField(0, CLU8(0).serialize()).\
                    addField(1, bytes.fromhex(self.args[0]))
                return table.to_bytes()

            case CONST.INVOCABLEENTITYALIAS:
                table = CalltableSerialization()
                table.addField(0, CLU8(1).serialize()).\
                    addField(1, CLString(
                        *self.args).serialize())
                return table.to_bytes()

            case CONST.PACKAGE:
                return ByPackageHashInvocationTarget(
                    *self.args).to_bytes()

            case CONST.PACKAGEALIAS:
                return ByPackageNameInvocationTarget(
                    *self.args).to_bytes()

    def to_json(self):
        target = {}
        result = {}
        match self.invocation_kind:
            case CONST.INVOCABLEENTITY:
                target = InvocableEntityTarget(
                    *self.args).to_json()

            case CONST.INVOCABLEENTITYALIAS:
                target = InvocableEntityAliasTarget(
                    *self.args).to_json()

            case CONST.PACKAGE:
                target = ByPackageHashInvocationTarget(
                    *self.args).to_json()

            case CONST.PACKAGEALIAS:
                target = ByPackageNameInvocationTarget(
                    *self.args).to_json()

        # result["Stored"] = {
        #     "id": target,
        #     "runtime": "VmCasperV1"
        # }
        result[JSONNAME.ID] = target
        return result


# stored
        # "target": {
        #     "Stored": {
        #         "id": {
        #             "ByName": "apple_contract"
        #         },
        #         "runtime": "VmCasperV1"
        #     }
        # }

target = TransactionInvocationTarget(
    "InvocableEntity", "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# a = target.to_bytes()
# # print("a is ", a.hex())
# b = target.to_json()
# print("b is: ", json.dumps(b))


# ByHash
# f3469257d7c361b80def54eda2a7ca794e9280229287bd9c997e1980485648d8
