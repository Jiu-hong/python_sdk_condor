from .cl_values import CLU8, CLString

from .constants import JsonName
from .constants import EntryPointKind
from .call_table_serialization import CalltableSerialization

ENTYPOINT = EntryPointKind()
VALID_ALLOWD_ENTRY_POINTS = (
    ENTYPOINT.CALL, ENTYPOINT.CUSTOM, ENTYPOINT.TRANSFER, ENTYPOINT.ADD_BID, ENTYPOINT.WITHDRAW_BID, ENTYPOINT.DELEGATE, ENTYPOINT.UNDELEGATE, ENTYPOINT.REDELEGATE, ENTYPOINT.ACTIVATE_BID, ENTYPOINT.CHANGEPUBLICKEY)

JSONNAME = JsonName()


class TransactionEntryPoint:
    def __init__(self, entry_point: str, arg: str = None):
        if entry_point not in VALID_ALLOWD_ENTRY_POINTS:
            raise ValueError(
                f"Invalid input: {entry_point}. Allowed values are: {VALID_ALLOWD_ENTRY_POINTS}")
        self.entry_point = entry_point
        self.arg = arg

    def to_bytes(self):
        table = CalltableSerialization()
        match self.entry_point:
            case ENTYPOINT.CALL:
                table.addField(0, CLU8(0).serialize())
            case ENTYPOINT.CUSTOM:
                table.addField(0, CLU8(1).serialize()).addField(
                    1, CLString(self.arg).serialize())
            case ENTYPOINT.TRANSFER:
                table.addField(0, CLU8(2).serialize())
            case ENTYPOINT.ADD_BID:
                table.addField(0, CLU8(3).serialize())
            case ENTYPOINT.WITHDRAW_BID:
                table.addField(0, CLU8(4).serialize())
            case ENTYPOINT.DELEGATE:
                table.addField(0, CLU8(5).serialize())
            case ENTYPOINT.UNDELEGATE:
                table.addField(0, CLU8(6).serialize())
            case ENTYPOINT.REDELEGATE:
                table.addField(0, CLU8(7).serialize())
            case ENTYPOINT.ACTIVATE_BID:
                table.addField(0, CLU8(8).serialize())
            case ENTYPOINT.CHANGEPUBLICKEY:
                table.addField(0, CLU8(9).serialize())

        return table.to_bytes()

    def to_json(self):
        result = {}
        match self.entry_point:
            case ENTYPOINT.CUSTOM:
                result[JSONNAME.ENTRYPOINT] = {self.entry_point: self.arg}
            case _:
                result[JSONNAME.ENTRYPOINT] = self.entry_point

        return result


entrypoint = TransactionEntryPoint("Custom", "apple")
# print("entrypoint: ", entrypoint.to_bytes().hex())
