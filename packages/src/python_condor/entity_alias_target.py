from .utils import CalltableSerialization, serialize_string

from .transaction_runtime import TransactionRuntime
from .constants import JsonName

JSONNAME = JsonName()


# class InvocableEntityAliasTarget:
#     def __init__(self, contract_name: str):
#         self.contract_name = contract_name

#     def to_bytes(self):
#         table = CalltableSerialization()
#         table.addField(0, CLU8(1).serialize()).\
#             addField(1, CLString(
#                 self.contract_name).serialize())
#         return table.to_bytes()

#     def to_json(self):
#         result = {}
#         result[JSONNAME.BYNAME] = self.contract_name
#         return result
class EntityAliasTarget:
    def __init__(self, runtime: str, contract_name: str):
        self.contract_name = contract_name
        self.runtime = runtime

    def to_bytes(self):
        selftable = CalltableSerialization()
        selftable.addField(0, int(1).to_bytes()).\
            addField(1, serialize_string(self.contract_name))
        # return table.to_bytes()
        table = CalltableSerialization()
        table.addField(0, int(1).to_bytes()).addField(
            1, selftable.to_bytes()).addField(
            2, TransactionRuntime(self.runtime).to_bytes())
        return table.to_bytes()

    def to_json(self):
        result = {}
        # result[JSONNAME.BYNAME] = self.contract_name
        result = {}
        result_2 = {}
        result_3 = {}
        result_4 = {}
        result_4[JSONNAME.BYNAME] = self.contract_name
        result_3[JSONNAME.ID] = result_4
        result_3[JSONNAME.RUNTIME] = self.runtime
        result_2[JSONNAME.STORED] = result_3
        result[JSONNAME.TARGET] = result_2
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
