from .cl_values import CLU64, CLU8, CLBool
from .constants import JsonName, PricingModeKind
from .payment_limit import PaymentLimited


PRICINGMODE = PricingModeKind()
JSONNAME = JsonName()


class PricingMode:
    def __init__(self, pricing_mode, payment_amount, gas_price_tolerance=1, standard_payment=True, ):
        self.pricing_mode = pricing_mode
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def to_bytes(self):

        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                return PaymentLimited(self.payment_amount,
                                      self.gas_price_tolerance, self.standard_payment).to_bytes()

    def serialize(self):
        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                return CLU8(0).serialize()+CLU64(self.payment_amount).serialize() + CLU8(self.gas_price_tolerance).serialize() + CLBool(self.standard_payment).serialize()
            case PRICINGMODE.FIXED:
                return CLU8(1).serialize() + CLU64(self.gas_price_tolerance).serialize()

    def to_json(self):
        result = {}
        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                result[JSONNAME.PRICING_MODE] = PaymentLimited(self.payment_amount,
                                                               self.gas_price_tolerance, self.standard_payment).to_json()

            case PRICINGMODE.FIXED:
                # result["pricing_mode"] = {
                #     "PaymentLimited": {
                #         "gas_price_tolerance": self.gas_price_tolerance,
                #         "standard_payment": self.standard_payment
                #     }
                # }
                # todo
                pass
        return result


pricing_mode = PricingMode("Classic", 123)
a = pricing_mode.to_bytes()
# print("a is:", a.hex())
