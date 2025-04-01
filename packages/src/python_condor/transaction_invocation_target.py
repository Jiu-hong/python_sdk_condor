from .package_hash_target import PackageHashTarget
from .package_name_target import PackageNameTarget
from .cl_values import CLU8, CLString
from .entity_alias_target import EntityAliasTarget
from .entity_target import EntityTarget


from .constants import JsonName, InvocationKind

from .call_table_serialization import CalltableSerialization

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
                # table = CalltableSerialization()
                # table.addField(0, CLU8(0).serialize()).\
                #     addField(1, bytes.fromhex(self.args[0]))
                # return table.to_bytes()
                return EntityTarget(
                    *self.args).to_bytes()

            case CONST.INVOCABLEENTITYALIAS:
                # table = CalltableSerialization()
                # table.addField(0, CLU8(1).serialize()).\
                #     addField(1, CLString(
                #         *self.args).serialize())
                # return table.to_bytes()
                return EntityAliasTarget(
                    *self.args).to_bytes()

            case CONST.PACKAGE:
                return PackageHashTarget(
                    *self.args).to_bytes()

            case CONST.PACKAGEALIAS:
                return PackageNameTarget(
                    *self.args).to_bytes()

    def to_json(self):
        target = {}
        result = {}
        match self.invocation_kind:
            case CONST.INVOCABLEENTITY:
                target = EntityTarget(
                    *self.args).to_json()

            case CONST.INVOCABLEENTITYALIAS:
                target = EntityAliasTarget(
                    *self.args).to_json()

            case CONST.PACKAGE:
                target = PackageHashTarget(
                    *self.args).to_json()

            case CONST.PACKAGEALIAS:
                target = PackageNameTarget(
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

# target = TransactionInvocationTarget(
#     "InvocableEntity", "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# # a = target.to_bytes()
# # print("a is ", a.hex())
# b = target.to_json()
# print("b is: ", json.dumps(b))


# ByHash
# f3469257d7c361b80def54eda2a7ca794e9280229287bd9c997e1980485648d8
