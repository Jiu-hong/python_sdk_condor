from cl_number import CLU32, CLU8
from cl_option import CLOption
from call_table_serialization import CalltableSerialization


class InvocableEntityAliasTarget:
    def __init__(self, contract_name: str):
        self.contract_name = contract_name

    def to_bytes(self):
        pass

    def to_json(self):
        result = {}
        result["ByName"] = self.contract_name
        return result


# By contract name
# c77cea12d795be628541d8d548ebcd2df6127bdb0ccaebb9809b252c611c005c
        # "target": {
        #     "Stored": {
        #         "id": {
        #             "ByName": "apple_contract"
        #         },
        #         "runtime": "VmCasperV1"
        #     }
        # }
a = InvocableEntityAliasTarget("apple_contract")
# print(a.to_json())
