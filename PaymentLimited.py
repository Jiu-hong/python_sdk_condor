from cl_number import CLU64, CLU8, CLBool
from table import CalltableSerialization


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
        result["PaymentLimited"] = {
            "payment_amount": self.payment_amount, "gas_price_tolerace": self.gas_price_tolerance, "standard_payment": self.standard_payment}
        return result


payment_limit = PaymentLimited(123, 1, True)
a = payment_limit.to_bytes()
# print("a is:", a.hex())
