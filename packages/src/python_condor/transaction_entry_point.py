from .utils import serialize_string
from .call_table_serialization import CalltableSerialization

from .constants import EntryPointKind, JsonName


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
                table.addField(0, int(0).to_bytes())
            case ENTYPOINT.CUSTOM:
                table.addField(0, int(1).to_bytes()).addField(
                    1, serialize_string(self.arg))
            case ENTYPOINT.TRANSFER:
                table.addField(0, int(2).to_bytes())
            case ENTYPOINT.ADD_BID:
                table.addField(0, int(3).to_bytes())
            case ENTYPOINT.WITHDRAW_BID:
                table.addField(0, int(4).to_bytes())
            case ENTYPOINT.DELEGATE:
                table.addField(0, int(5).to_bytes())
            case ENTYPOINT.UNDELEGATE:
                table.addField(0, int(6).to_bytes())
            case ENTYPOINT.REDELEGATE:
                table.addField(0, int(7).to_bytes())
            case ENTYPOINT.ACTIVATE_BID:
                table.addField(0, int(8).to_bytes())
            case ENTYPOINT.CHANGEPUBLICKEY:
                table.addField(0, int(9).to_bytes())

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
