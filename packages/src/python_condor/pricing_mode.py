from .constants import JsonName, PricingModeKind
from .payment_limit import PaymentLimited


PRICINGMODE = PricingModeKind()
VALID_ALLOWD_PRICINGMODE = (
    PRICINGMODE.CLASSIC)

JSONNAME = JsonName()


class PricingMode:
    def __init__(self, pricing_mode, payment_amount, gas_price_tolerance=1, standard_payment=True):
        if pricing_mode not in VALID_ALLOWD_PRICINGMODE:
            raise ValueError(
                f"Invalid input: {pricing_mode}. Allowed values are: {VALID_ALLOWD_PRICINGMODE}")
        if not isinstance(payment_amount, int):
            raise TypeError(
                f"Invalid type of input: {type(payment_amount)} for payment_amount. Allowed value is int.")
        self.pricing_mode = pricing_mode
        self.payment_limited = PaymentLimited(payment_amount,
                                              gas_price_tolerance, standard_payment)

    def to_bytes(self):

        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                return self.payment_limited.to_bytes()

    # def serialize(self):
    #     match self.pricing_mode:
    #         case PRICINGMODE.CLASSIC:
    #             return CLU8(0).serialize()+CLU64(self.payment_amount).serialize() + CLU8(self.gas_price_tolerance).serialize() + CLBool(self.standard_payment).serialize()
    #         case PRICINGMODE.FIXED:
    #             return CLU8(1).serialize() + CLU64(self.gas_price_tolerance).serialize()

    def to_json(self):
        result = {}
        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                result[JSONNAME.PRICING_MODE] = self.payment_limited.to_json()

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
