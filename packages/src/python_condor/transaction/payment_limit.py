from ..constants import JsonName
from ..utils import CalltableSerialization


JSONNAME = JsonName()


class PaymentLimited:
    def __init__(self, payment_amount, gas_price_tolerance, standard_payment) -> None:
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def to_bytes(self):
        table = CalltableSerialization()

        table.add_field(0, int(0).to_bytes()).add_field(
            1, self.payment_amount.to_bytes(8, byteorder='little')).add_field(
            2, self.gas_price_tolerance.to_bytes()).add_field(
            3, int(self.standard_payment).to_bytes())
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
