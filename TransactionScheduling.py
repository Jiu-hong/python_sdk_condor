from cl_number import CLU8
from table import CalltableSerialization


class TransactionScheduling:
    def __init__(self, schedule_mode="Standard"):
        self.schedule_mode = schedule_mode

    def to_bytes(self):
        match self.schedule_mode:
            case "Standard":
                table = CalltableSerialization()
                table.addField(0, int(0).to_bytes())
                return table.to_bytes()

    def serialize(self):
        match self.schedule_mode:
            case "Standard":
                return CLU8(0).serialize()

    def to_json(self):
        result = {}
        result["scheduling"] = self.schedule_mode
        return result


scheduling = TransactionScheduling()
# print("scheduleing is: ", scheduling.to_bytes().hex())
