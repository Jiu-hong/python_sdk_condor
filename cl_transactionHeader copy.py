from datetime import datetime, timezone
from hashlib import blake2b
from time import time
from cl_number import CLU32, CLU64, CLU8, CLBool
from cl_option import CLOption
from cl_publickey import CLPublicKey
from cl_string import CLString
from name_arg import NamedArg
from table import CalltableSerialization


class Transaction:
    def __init__(self,  payload, approvals) -> None:
        self.payload = payload
        self.approvals = approvals

    def to_json(self):
        hash = xxx
        approvals = xxx
        result = {"Version1": {
            "hash": hash,
            "payload": self.payload,
            "approvals": approvals
        }}
        return result


class PayloadInitiatorAddr:
    def __init__(self, publicKey) -> None:
        self.publicKey = publicKey

    def to_json(self):
        result = {}
        result["initiator_addr"] = {"PublicKey": self.publicKey}
        return result


class PayloadPricingMode:
    def __init__(self, payment_limited) -> None:
        self.payment_limited = payment_limited

    def to_json(self):
        result = {"pricing_mode": self.payment_limited}
        return result


class PaymentLimited:
    def __init__(self, payment_amount, gas_price_tolerance, standard_payment) -> None:
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def to_json(self):
        result = {}
        # result = {"PaymentLimited": {
        #     "payment_amount": self.payment_amount, "gas_price_tolerace": self.gas_price_tolerance, "standard_payment": self.standard_payment}}
        result["PaymentLimited"] = {
            "payment_amount": self.payment_amount, "gas_price_tolerace": self.gas_price_tolerance, "standard_payment": self.standard_payment}
        return result


class InitiatorAddr:
    def __init__(self, address):
        self.address = address

    def serialize(self):
        return CLU8(0).serialize() + self.address  # public key

    def to_json(self):
        result = {}
        result["initiator_addr"] = {"PublicKey": self.address}
        return result


class PricingMode:
    def __init__(self, pricing_mode, standard_payment=True, payment_amount=None, gas_price_tolerance=1):
        self.pricing_mode = pricing_mode
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def serialize(self):
        match self.pricing_mode:
            case "Classic":
                return CLU8(0).serialize()+CLU64(self.payment_amount).serialize() + CLU8(self.gas_price_tolerance).serialize() + CLBool(self.standard_payment).serialize()
            case "Fixed":
                return CLU8(1).serialize() + CLU64(self.gas_price_tolerance).serialize()

    def to_json(self):
        result = {}
        match self.pricing_mode:
            case "Classic":
                result["pricing_mode"] = {
                    "PaymentLimited": {
                        "payment_amount": self.payment_amount,
                        "gas_price_tolerance": self.gas_price_tolerance,
                        "standard_payment": self.standard_payment
                    }
                }
            case "Fixed":
                result["pricing_mode"] = {
                    "PaymentLimited": {
                        "gas_price_tolerance": self.gas_price_tolerance,
                        "standard_payment": self.standard_payment
                    }
                }
        return result


class TransactionV1Header:
    def __init__(self, chain_name,  body_hash,  pricing_mode, initiator_addr, payment_amount=None, gas_price_tolerance=1,  now=datetime.now(timezone.utc), ttl=30, ):
        self.chain_name = CLString(chain_name)
        # CLU64(int(time() * 1000)).serialize() // ??
        self.time = now
        self.ttl = ttl
        self.body_hash = body_hash
        self.pricing_mode = pricing_mode
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.initiator_addr = initiator_addr

    def serialize(self):
        return self.chain_name.serialize() \
            + CLU64(int(self.time.timestamp() * 1000)).serialize() \
            + CLU64(int(self.ttl) * 60000).serialize() \
            + self.body_hash \
            + PricingMode(self.pricing_mode, self.payment_amount,
                          self.gas_price_tolerance).serialize() \
            + InitiatorAddr(self.initiator_addr).serialize()

    def to_json(self):
        result = {}
        result["payload"] = {
            **InitiatorAddr(self.initiator_addr).to_json(), "timestamp": self.time.replace(
                tzinfo=None).isoformat(timespec='milliseconds')+"Z", "ttl": self.ttl, "chain_name": self.chain_name.value(), **PricingMode(self.pricing_mode, self.payment_amount,
                                                                                                                                           self.gas_price_tolerance).to_json()}
        result["hash"] = self.transaction_hash()
        return result

    def transaction_hash(self):
        header_hex = self.serialize()
        h = blake2b(digest_size=32)
        header_bytes = bytes.fromhex(header_hex)
        h.update(header_bytes)
        return h.hexdigest()


class TransactionTarget:
    #     "Stored", "ByPackageHash", "e48c5b9631c3a2063e61826d6e52181ea5d6fe35566bf994134caa26fce16586")
    def __init__(self, target_kind, *kw):
        self.target_kind = target_kind
        self.kw = kw

    def serialize(self):
        match self.target_kind:
            case "native":
                return CLU8(0).serialize()
            case "stored":
                return CLU8(1).serialize() + TransactionInvocationTarget(self.kw).serialize() + TransactionRuntime().serialize()
            case "session":
                return CLU8(2).serialize() + TransactionSessionTarget(self.kw).serialize() + TransactionRuntime().serialize()

    def to_json(self):
        result = {}
        # print("self.target_kind:", self.target_kind)
        match self.target_kind:
            case "native":
                result["target"] = "Native"
            case "stored":
                result["target"] = {
                    **TransactionInvocationTarget(self.kw).to_json()}
            case "session":
                result["target"] = {"Session": {
                    **TransactionSessionTarget(self.kw).to_json()}}

        return result


class TransactionEntryPoint:
    def __init__(self, entry_point, content=None):
        self.entry_point = entry_point
        self.content = content

    def serialize(self):
        match self.entry_point:
            case "Custom":
                return CLU8(0).serialize() + CLString(self.content).serialize()
            case "Transfer":
                return CLU8(1).serialize()
            case "Add_Bid":
                return CLU8(2).serialize()
            case "Withdraw_Bid":
                return CLU8(3).serialize()
            case "Delegate":
                return CLU8(4).serialize()
            case "Undelegate":
                return CLU8(5).serialize()
            case "Redelegate":
                return CLU8(6).serialize()
            case "Activate_Bid":
                return CLU8(7).serialize()
            case "ChangePublicKey":
                return CLU8(8).serialize()
            case "Call":
                return CLU8(9).serialize()

    def to_json(self):
        result = {}
        match self.entry_point:
            case "Custom":
                result["entry_point"] = {self.entry_point: self.content}
            case _:
                result["entry_point"] = self.entry_point

        return result


class TransactionScheduling:
    def __init__(self, schedule_mode="Standard"):
        self.schedule_mode = schedule_mode

    def to_bytes(self):
        # if (this.standard) {
        #   const calltableSerialization = new CalltableSerialization();
        #   calltableSerialization.addField(0, Uint8Array.of(0));
        #   return calltableSerialization.toBytes();
        # } else if (this.futureEra) {
        #   return this.futureEra.toBytes();
        # } else if (this.futureTimestamp) {
        #   return this.futureTimestamp.toBytes();
        # }
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


class TransactionV1Body:
    def __init__(self, target: TransactionTarget, entry_point: TransactionEntryPoint, scheduleing: TransactionScheduling, args: NamedArg):
        self.args = args
        self.target = target
        self.entry_point = entry_point
        self.scheduling = scheduleing

    def serialize(self):
        return self.args.serialize() + self.target.serialize() + self.entry_point.serialize()+self.scheduling.serialize()

    def body_hash(self):
        body_hex = self.serialize()
        h = blake2b(digest_size=32)
        body_bytes = bytes.fromhex(body_hex)
        h.update(body_bytes)
        return h.hexdigest()

    def to_json(self):
        result = {}
        result["fields"] = {
            **self.args.to_json(), **self.entry_point.to_json(), **self.scheduling.to_json(), **self.target.to_json()}
        return result


class TransactionSessionTarget:
    def __init__(self, module_bytes, is_install_upgrade=False):
        self.module_bytes = module_bytes
        self.is_install_upgrade = is_install_upgrade

    def serialize(self):
        if self.is_install_upgrade:
            return CLU8(1).serialize() + self.module_bytes
        else:
            return CLU8(0).serialize() + self.module_bytes

    def to_json(self):
        result = {}
        result["Session"] = {"is_install_upgrade": self.is_install_upgrade,
                             "module_bytes": self.module_bytes, "runtime": "VmCasperV1"}
        return result


class TransactionInvocationTarget:
    #      "ByPackageHash", "e48c5b9631c3a2063e61826d6e52181ea5d6fe35566bf994134caa26fce16586")
    def __init__(self, invocation_target):
        self.invocation_target = invocation_target
        # print("self.invocation_target: ", self.invocation_target)

    def serialize(self):
        match self.invocation_target[0]:
            case "InvocableEntity":
                return CLU8(0).serialize() + self.invocation_target[1]
            case "InvocableEntityAlias":
                return CLU8(1).serialize() + CLString(self.invocation_target[1]).serialize()
            case "Package":
                # todo +version
                #                 const versionBytes = this.version
                #   ? CLValue.newCLOption(
                #       CLValue.newCLUInt32(BigNumber.from(this.version))
                #     ).bytes()
                #   : new CLValueOption(null, new CLTypeOption(CLTypeUInt32)).bytes();
                version = CLOption(CLU32(10))
                return CLU8(2).serialize() + self.invocation_target[1] + version.serialize()
            case "PackageAlias":
                return CLU8(3).serialize() + CLString(self.invocation_target[1]).serialize()

    def to_json(self):
        result = {}
        result["Stored"] = {"runtime": "VmCasperV1",
                            "id": {"ByPackageHash": {"addr": self.invocation_target[1]}}}
        return result


class TransactionRuntime:
    def __init__(self, runtime="VmCasperV1"):
        self.runtime = runtime

    def serialize(self):
        return CLU8(0).serialize()

    def to_json(self):
        result = {}
        result["runtime"] = self.runtime
        return result


transaction_target = TransactionTarget(
    "stored", "Package", "e48c5b9631c3a2063e61826d6e52181ea5d6fe35566bf994134caa26fce16586")
print("hello world=====")
# print(transaction_target.to_json())
# print(transaction_target.serialize())
# a = TransactionV1Body()
transaction_entry_point = TransactionEntryPoint("Custom", "apple")
# print("transaction_entry_point_to_json", transaction_entry_point.to_json())
# print("transaction_entry_point_serialize", transaction_entry_point.serialize())

name_args = NamedArg({"amount": CLU8(2), "owner": CLU8(
    1), 'recipient': CLString("set_all")})
# print("name_args.to_json()", name_args.to_json())
# print("name_args.serialize()", name_args.serialize())
a = TransactionV1Body(transaction_target,
                      transaction_entry_point, TransactionScheduling(), name_args)
# print("a.to_json()", a.to_json())
# print("a.serialize()", a.serialize())
hash = a.body_hash()
# print("hash is:", hash)
header = TransactionV1Header(
    "integration-test", "c6b803ae07f3f4541520b75c12b519afd3949f439d60b114f4f68bea5ee66776", "Classic", "01d23f9a9f240b4bb6f2aaa4253c7c8f34b2be848f104a83d3d6b9b2f276be28fa", 123)
# print("header.to_json()", header.to_json())
# print("header.transaction_hash()", header.transaction_hash())
f = open("wasm", "r")
wasm_bytes = f.read()
session = TransactionSessionTarget(wasm_bytes, True)
serialize = session.serialize()
# print("serialize:", serialize)
json = session.to_json()
# print("json:", json)
