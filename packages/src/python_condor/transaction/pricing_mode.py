"""
Pricing Mode module for handling Casper transaction pricing modes.

This module provides functionality for managing transaction pricing modes.
Pricing modes control:
- Payment amount calculation
- Gas price tolerance
- Standard payment flag

The module supports:
- Classic pricing mode (default)
- Fixed pricing mode (TODO)
- Payment amount validation
- Gas price tolerance configuration
- Standard payment flag management
- Serialization to bytes and JSON
"""

from typing import Dict, Any, Union

from ..constants import JsonName, PricingModeKind
from .payment_limit import PaymentLimited


# Constants for pricing mode configuration
PRICINGMODE = PricingModeKind()
VALID_ALLOWD_PRICINGMODE = (PRICINGMODE.CLASSIC)
JSONNAME = JsonName()


class PricingMode:
    """
    Represents a pricing mode in a Casper transaction.

    A pricing mode determines how the transaction payment is calculated and processed.
    It includes:
    - Pricing mode type (Classic, Fixed)
    - Payment amount
    - Gas price tolerance
    - Standard payment flag

    Attributes:
        pricing_mode (str): The type of pricing mode
        payment_limited (PaymentLimited): The payment limit configuration
    """

    def __init__(self, pricing_mode: str, payment_amount: int, gas_price_tolerance: int = 1, standard_payment: bool = True):
        """
        Initialize a pricing mode.

        Args:
            pricing_mode (str): The type of pricing mode
            payment_amount (int): The payment amount in motes
            gas_price_tolerance (int, optional): The gas price tolerance value. Defaults to 1.
            standard_payment (bool, optional): Whether this is a standard payment. Defaults to True.

        Raises:
            ValueError: If the pricing mode is invalid
            TypeError: If the payment amount is not an integer
        """
        if pricing_mode not in VALID_ALLOWD_PRICINGMODE:
            raise ValueError(
                f"Invalid input: {pricing_mode}. Allowed values are: {VALID_ALLOWD_PRICINGMODE}")
        if not isinstance(payment_amount, int):
            raise TypeError(
                f"Invalid type of input: {type(payment_amount)} for payment_amount. Allowed value is int.")

        self.pricing_mode = pricing_mode
        self.payment_limited = PaymentLimited(
            payment_amount, gas_price_tolerance, standard_payment)

    def to_bytes(self) -> bytes:
        """
        Serialize the pricing mode to bytes.

        The serialization includes:
        - Pricing mode type
        - Payment limit data

        Returns:
            bytes: The serialized pricing mode
        """
        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                return self.payment_limited.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the pricing mode to a JSON representation.

        The JSON structure follows the format:
        {
            "pricing_mode": {
                "PaymentLimited": {
                    "payment_amount": <amount>,
                    "gas_price_tolerance": <tolerance>,
                    "standard_payment": <flag>
                }
            }
        }

        Returns:
            Dict[str, Any]: The JSON representation of the pricing mode
        """
        result = {}
        match self.pricing_mode:
            case PRICINGMODE.CLASSIC:
                result[JSONNAME.PRICING_MODE] = self.payment_limited.to_json()
            case PRICINGMODE.FIXED:
                # Fixed pricing mode implementation is pending
                pass
        return result
