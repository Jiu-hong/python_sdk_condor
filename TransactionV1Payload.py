from datetime import datetime, timezone
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
    def __init__(self, args: list, transactionTarget, entrypoint, scheduling, initiatorAddr,  pricing_mode, chainName, ttl=30, now=datetime.now(timezone.utc)):
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
        print("self.fields.args.items() is: ", self.fields.args.items())
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

        length_schedulingBytes = CLU32(
            len(schedulingBytes)).serialize()
        schedulingWithLength = length_schedulingBytes + schedulingBytes

        self.fields.addField(3, schedulingWithLength)

        #
        table = CalltableSerialization()
        # table.addField(0, InitiatorAddr(
        #     self.initiatorAddr).to_bytes()).\
        #     addField(1, CLU64(int(self.time.timestamp() * 1000)).serialize()). \
        #     addField(2, CLU64(int(self.ttl) * 60000).serialize()). \
        #     addField(3, CLString(self.chainName).serialize()). \
        #     addField(4, self.pricingMode.to_bytes()). \
        #     addField(5, self.fields.to_bytes())
        table.addField(0, InitiatorAddr(
            self.initiatorAddr).to_bytes()).\
            addField(1, CLU64(int(1742777353.133 * 1000)).serialize()). \
            addField(2, CLU64(int(self.ttl) * 60000).serialize()). \
            addField(3, CLString(self.chainName).serialize()). \
            addField(4, self.pricingMode.to_bytes()). \
            addField(5, self.fields.to_bytes())
        return table.to_bytes()


args = {"arg1": CLU8(123), "arg2": CLString("Hello")}
transactionTarget = TransactionTarget("stored", "InvocableEntity",
                                      "cc7a90c16cbecf53a09a8d7f76ccd2ed167da89e04d4edcca0eda2301de87b56")
entrypoint = TransactionEntryPoint("Custom", "apple")
scheduling = TransactionScheduling()
initiatorAddr = "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"
pricing_mode = PricingMode("Classic", 123)

transaction_v1_payload = TransactionV1Payload(args, transactionTarget,
                                              entrypoint, scheduling, initiatorAddr, pricing_mode, "casper-integration")
bytes = transaction_v1_payload.to_bytes()
print("bytes_transaction_v1_payload is: \n", bytes.hex())
