from python_condor.call_table_serialization import CalltableSerialization
from python_condor.cl_values.cl_number import CLU8
from python_condor.cl_values.cl_string import CLString
from .constants import JsonName

JSONNAME = JsonName()


class InvocableEntityAliasTarget:
    def __init__(self, contract_name: str):
        self.contract_name = contract_name

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, CLU8(1).serialize()).\
            addField(1, CLString(
                self.contract_name).serialize())
        return table.to_bytes()

    def to_json(self):
        result = {}
        result[JSONNAME.BYNAME] = self.contract_name
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
# a = InvocableEntityAliasTarget("apple_contract")
# print(a.to_json())
