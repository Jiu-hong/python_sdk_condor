from datetime import datetime, timezone
import json
from InitiatorAddr import InitiatorAddr
from PayloadFields import PayloadFields
from PricingMode import PricingMode
from TransactionEntryPoint import TransactionEntryPoint
from TransactionScheduling import TransactionScheduling
from TransactionTarget import TransactionTarget
from cl_number import CLU32, CLU64, CLU8
from cl_string import CLString

from named_args import NamedArg
from table import CalltableSerialization


class TransactionV1Payload:
    def __init__(self, args: list, transactionTarget, entrypoint, scheduling, initiatorAddr,  pricing_mode: PricingMode, chainName, ttl=30, now=datetime.now(timezone.utc)):
        print("args in TransactionV1Payload:", args)
        self.initiatorAddr = initiatorAddr
        self.ttl = ttl
        self.pricingMode = pricing_mode
        self.time = now
        self.chainName = chainName
        self.fields = PayloadFields(
            args, transactionTarget, entrypoint, scheduling)

    def to_bytes(self):
        # runtime_arg
        offset = 0
        runtimeArgsBuffer = CLU8(0).serialize()
        offset += 1
        runtimeArgsBuffer = runtimeArgsBuffer + \
            CLU32(len(self.fields.args)).serialize()

        offset += 4
        # print("self.fields.args.items() is: ", self.fields.args.items())
        for name, value in self.fields.args.items():
            named_arg = NamedArg(name, value)

            arg_bytes = named_arg.to_byte_with_named_arg()

            runtimeArgsBuffer = runtimeArgsBuffer + arg_bytes

            offset += len(arg_bytes)

        lenth_runtimeArgsBuffer = CLU32(
            len(runtimeArgsBuffer)).serialize()

        runtimeArgsWithLength = lenth_runtimeArgsBuffer + runtimeArgsBuffer

        self.fields.addField(0, runtimeArgsWithLength)

        # target
        targetBytes = self.fields.target.to_bytes()
        # print("targetBytes is:", targetBytes.hex())

        length_targetBytes = CLU32(
            len(targetBytes)).serialize()

        targetWithLength = length_targetBytes + targetBytes

        self.fields.addField(1, targetWithLength)

        # entryPointBytes
        entryPointBytes = self.fields.entry_point.to_bytes()
        length_entryPointBytes = CLU32(
            len(entryPointBytes)).serialize()

        entryPointWithLength = length_entryPointBytes + entryPointBytes

        self.fields.addField(2, entryPointWithLength)

        # schedulingBytes
        schedulingBytes = self.fields.scheduling.to_bytes()
        # print("schedulingBytes is:", schedulingBytes.hex())

        length_schedulingBytes = CLU32(
            len(schedulingBytes)).serialize()
        schedulingWithLength = length_schedulingBytes + schedulingBytes

        self.fields.addField(3, schedulingWithLength)

        #
        table = CalltableSerialization()
        table.addField(0, InitiatorAddr(
            self.initiatorAddr).to_bytes()).\
            addField(1, CLU64(int(self.time.timestamp() * 1000)).serialize()). \
            addField(2, CLU64(int(self.ttl) * 60000).serialize()). \
            addField(3, CLString(self.chainName).serialize()). \
            addField(4, self.pricingMode.to_bytes()). \
            addField(5, self.fields.to_bytes())
        # table.addField(0, InitiatorAddr(
        #     self.initiatorAddr).to_bytes()).\
        #     addField(1, CLU64(int(datetime.fromisoformat('2025-03-26T03:11:48.829Z').timestamp() * 1000)).serialize()). \
        #     addField(2, CLU64(int(self.ttl) * 60000).serialize()). \
        #     addField(3, CLString(self.chainName).serialize()). \
        #     addField(4, self.pricingMode.to_bytes()). \
        #     addField(5, self.fields.to_bytes())
        fields = self.fields.to_bytes()
        # print("fields are:", fields.hex())
        u = self.pricingMode.to_bytes()
        print("pricingMode is:", u.hex())
        t = CLU64(int(datetime.fromisoformat(
            '2025-03-26T03:11:48.829Z').timestamp() * 1000)).serialize()
        print("time is:", t.hex())
        return table.to_bytes()

    def to_json(self):
        result = {}
        initiator_addr = InitiatorAddr(
            self.initiatorAddr).to_json()
        timestamp = {"timestamp": self.time.replace(
            tzinfo=None).isoformat(timespec='milliseconds')+"Z"}
        ttl = {"ttl": str(self.ttl)+'m'}
        chain_name = {"chain_name": self.chainName}
        pricing_mode = self.pricingMode.to_json()
        fields = self.fields.to_json()
        result["payload"] = {
            **initiator_addr, **timestamp, **ttl, **chain_name, **pricing_mode, **fields
        }
        return result


# args = {"arg1": CLU8(123), "arg2": CLString("Hello")}

# transactionTarget = TransactionTarget("stored", "InvocableEntity",
#                                       "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")


# entrypoint = TransactionEntryPoint("Custom", "apple")

# scheduling = TransactionScheduling()
# initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
# pricing_mode = PricingMode("Classic", 20000000000000)

# args = {}
# transactionTarget2 = TransactionTarget("session", '01', False)
# entrypoint2 = TransactionEntryPoint("Call")
# transaction_v1_payload = TransactionV1Payload(args, transactionTarget2,
#                                               entrypoint2, scheduling, initiatorAddr, pricing_mode, "casper-net-1")


# print("transaction_v1_payload to_json:",
#       json.dumps(transaction_v1_payload.to_json()))

# bytes = transaction_v1_payload.to_bytes()
# print("bytes_transaction_v1_payload is: \n", bytes.hex())


# actual
# 0600000000000000000001003600000002003e000000030046000000040056000000050081000000f600000002000000000000000000010001000000220000000001bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c615d486fd09501000040771b00000000000c0000006361737065722d6e65742d310400000000000000000001000100000002000900000003000a0000000b000000000040e59c30120000010104000000000005000000000000000001003600000004000000000000000000010001000000020002000000030011000000160000000200010000000000000000000100000000010000000102000f00000001000000000000000000010000000003000f000000010000000000000000000100000000

# expected target bytes:
# 030000000000000000000100010000000200360000004500000001020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6010000000000000000000100000000
# 020000000000000000000100010000002100000000b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6
