from ..constants import SchedulingKind, JsonName
from ..utils import CalltableSerialization


CONST = SchedulingKind()
VALID_ALLOWED_SCHEDULING = (CONST.STANDARD)

JSONNAME = JsonName()


class TransactionScheduling:
    def __init__(self, schedule_mode: str = CONST.STANDARD):
        if schedule_mode not in VALID_ALLOWED_SCHEDULING:
            raise ValueError(
                f"Invalid input: {schedule_mode}. Valid allowed values: {VALID_ALLOWED_SCHEDULING}")
        self.schedule_mode = schedule_mode

    def to_bytes(self):
        match self.schedule_mode:
            case CONST.STANDARD:
                table = CalltableSerialization()
                table.addField(0, int(0).to_bytes())
                return table.to_bytes()

    # def serialize(self):
    #     match self.schedule_mode:
    #         case CONST.STANDARD:
    #             return int(0).to_bytes()

    def to_json(self):
        result = {}
        result[JSONNAME.SCHEDULING] = self.schedule_mode
        return result


# scheduling = TransactionScheduling()
# # print("scheduleing is: ", scheduling.to_bytes().hex())
# print("here")
