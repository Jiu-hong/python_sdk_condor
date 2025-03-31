# to_bytes to do
from hashlib import blake2b
from .cl_values import CLU16, CLU32
from .constants import JsonName
from .named_arg import NamedArg
from .transaction_entry_point import TransactionEntryPoint
from .transaction_target import TransactionTarget


JSONNAME = JsonName()


class PayloadFields:
    def __init__(self, args: dict, target: TransactionTarget, entry_point: TransactionEntryPoint, scheduleing):

        self.args = args
        self.target = target
        self.entry_point = entry_point
        self.scheduling = scheduleing
        self.dict = {}

    def addField(self, index, bytes):
        self.dict[CLU16(index)] = bytes

    def to_bytes(self):
        buffer = CLU32(len(self.dict)).serialize()
        for key, value in self.dict.items():
            # print("key:", key)
            # print("key serialize:", key.serialize().hex())
            # print("value: ", value.hex())
            buffer = buffer + key.serialize()  # key is CLU16
            buffer = buffer + value
        return buffer

    # def serialize(self):
    #     return self.args.serialize() + self.target.serialize() + self.entry_point.serialize()+self.scheduling.serialize()

    def body_hash(self):
        body_hex = self.serialize()
        h = blake2b(digest_size=32)
        body_bytes = bytes.fromhex(body_hex)
        h.update(body_bytes)
        return h.hexdigest()

    def to_json(self):

        result = {}
        name_args = []

        for name, value in self.args.items():
            name_args.append(NamedArg(name, value).to_json())

        result[JSONNAME.FIELDS] = {
            JSONNAME.ARGS: {JSONNAME.NAMED: name_args}, **self.entry_point.to_json(), **self.scheduling.to_json(), **self.target.to_json()}
        return result


# args = {"arg1": CLU8(123), "arg2": CLString("Hello")}
# target = TransactionTarget("stored", "InvocableEntity",
#                            "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
# entrypoint = TransactionEntryPoint("Custom", "apple")
# scheduleing = TransactionScheduling()
# payloadfields = PayloadFields(args, target, entrypoint, scheduleing)
# print("payloadfields to_json", json.dumps(payloadfields.to_json()))
