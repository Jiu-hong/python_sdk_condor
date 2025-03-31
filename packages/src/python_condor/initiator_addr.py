from .call_table_serialization import CalltableSerialization
from .cl_values import CLPublicKey, CLU8


class InitiatorAddr:
    def __init__(self, address: str):
        self.address = address

    def to_bytes(self):
        # account hash to do
        table = CalltableSerialization()
        table.addField(0, CLU8(0).serialize()).addField(
            1, CLPublicKey(self.address).serialize())
        return table.to_bytes()

    def serialize(self):
        return CLU8(0).serialize() + self.address  # public key

    def to_json(self):
        result = {}
        result["initiator_addr"] = {"PublicKey": self.address}
        return result


# initiator_addr = InitiatorAddr(
#     "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61")
# a = initiator_addr.to_bytes()
# print("a is:", a.hex())
