from cl_number import CLU8
from cl_string import CLString
from table import CalltableSerialization


class TransactionEntryPoint:
    def __init__(self, entry_point, content=None):
        self.entry_point = entry_point
        self.content = content

    def to_bytes(self):
        table = CalltableSerialization()
        match self.entry_point:
            case "Call":
                table.addField(0, CLU8(0).serialize())
            case "Custom":
                table.addField(0, CLU8(1).serialize()).addField(
                    1, CLString(self.content).serialize())
            case "Transfer":
                table.addField(0, CLU8(1).serialize())
            case "Add_Bid":
                table.addField(0, CLU8(2).serialize())
            case "Withdraw_Bid":
                table.addField(0, CLU8(3).serialize())
            case "Delegate":
                table.addField(0, CLU8(4).serialize())
            case "Undelegate":
                table.addField(0, CLU8(5).serialize())
            case "Redelegate":
                table.addField(0, CLU8(6).serialize())
            case "Activate_Bid":
                table.addField(0, CLU8(7).serialize())
            case "ChangePublicKey":
                table.addField(0, CLU8(8).serialize())

        return table.to_bytes()

    def to_json(self):
        result = {}
        match self.entry_point:
            case "Custom":
                result["entry_point"] = {self.entry_point: self.content}
            case _:
                result["entry_point"] = self.entry_point

        return result


entrypoint = TransactionEntryPoint("Custom", "apple")
# print("entrypoint: ", entrypoint.to_bytes().hex())
