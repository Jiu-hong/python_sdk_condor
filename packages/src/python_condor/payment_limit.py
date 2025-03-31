from .call_table_serialization import CalltableSerialization
from .cl_values import CLBool, CLU8, CLU64
from .constants import JsonName

JSONNAME = JsonName()


class PaymentLimited:
    def __init__(self, payment_amount, gas_price_tolerance, standard_payment) -> None:
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def to_bytes(self):
        table = CalltableSerialization()
        table.addField(0, CLU8(0).serialize()).addField(
            1, CLU64(self.payment_amount).serialize()).addField(
            2, CLU8(self.gas_price_tolerance).serialize()).addField(
            3, CLBool(self.standard_payment).serialize())
        return table.to_bytes()

    def to_json(self):
        result = {}

        result[JSONNAME.PAYMENTLIMITED] = {
            JSONNAME.PAYMENT_AMOUNT: self.payment_amount,
            JSONNAME.GAS_PRICE_TOLERACE: self.gas_price_tolerance,
            JSONNAME.STANDARD_PAYMENT: self.standard_payment
        }
        return result


# payment_limit = PaymentLimited(123, 1, True)
# a = payment_limit.to_bytes()
# print("a is:", a.hex())
