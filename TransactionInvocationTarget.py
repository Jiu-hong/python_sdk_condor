import json
from ByPackageHashInvocationTarget import ByPackageHashInvocationTarget
from ByPackageNameInvocationTarget import ByPackageNameInvocationTarget
from InvocableEntityAliasTarget import InvocableEntityAliasTarget
from InvocableEntityTarget import InvocableEntityTarget
from cl_number import CLU32, CLU8
from cl_option import CLOption
from cl_string import CLString
from table import CalltableSerialization


class TransactionInvocationTarget:
    #      "ByPackageHash", "e48c5b9631c3a2063e61826d6e52181ea5d6fe35566bf994134caa26fce16586")
    def __init__(self, *invocation_target):
        self.invocation_target = invocation_target
        print("invocation_target is:", invocation_target)

    def to_bytes(self):
        match self.invocation_target[0]:
            case "InvocableEntity":
                table = CalltableSerialization()
                table.addField(0, CLU8(0).serialize()).\
                    addField(1, bytes.fromhex(self.invocation_target[1]))
                return table.to_bytes()

            case "InvocableEntityAlias":
                table = CalltableSerialization()
                table.addField(0, CLU8(1).serialize()).\
                    addField(1, CLString(
                        self.invocation_target[1]).serialize())
                return table.to_bytes()

            case "Package":
                return ByPackageHashInvocationTarget(
                    self.invocation_target[1], self.invocation_target[2]).to_bytes()

            case "PackageAlias":
                return ByPackageNameInvocationTarget(
                    self.invocation_target[1], self.invocation_target[2]).to_bytes()

# ok
    def to_json(self):
        target = {}
        result = {}
        match self.invocation_target[0]:
            case "InvocableEntity":
                target = InvocableEntityTarget(
                    self.invocation_target[1]).to_json()

            case "InvocableEntityAlias":
                target = InvocableEntityAliasTarget(
                    self.invocation_target[1]).to_json()

            case "Package":
                target = ByPackageHashInvocationTarget(
                    self.invocation_target[1], self.invocation_target[2]).to_json()

            case "PackageAlias":
                target = ByPackageNameInvocationTarget(
                    self.invocation_target[1], self.invocation_target[2]).to_json()

        result["Stored"] = {
            "id": target,
            "runtime": "VmCasperV1"
        }
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
a = target.to_bytes()
print("a is ", a.hex())
b = target.to_json()
print("b is: ", json.dumps(b))


# ByHash
# f3469257d7c361b80def54eda2a7ca794e9280229287bd9c997e1980485648d8
