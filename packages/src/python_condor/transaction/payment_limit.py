"""
Payment Limit module for handling CasperLabs transaction payment limits.

This module provides functionality for managing payment limits in transactions.
Payment limits control:
- Maximum payment amount
- Gas price tolerance
- Standard payment flag

The module supports:
- Payment amount validation
- Gas price tolerance configuration
- Standard payment flag management
- Serialization to bytes and JSON
"""

from typing import Dict, Any

from ..constants import JsonName
from ..utils import CalltableSerialization


# Constants for payment limit configuration
JSONNAME = JsonName()


class PaymentLimited:
    """
    Represents a payment limit in a CasperLabs transaction.

    A payment limit controls how much a transaction can spend and under what conditions.
    It includes:
    - Maximum payment amount
    - Gas price tolerance
    - Standard payment flag

    Attributes:
        payment_amount (int): The maximum payment amount in motes
        gas_price_tolerance (int): The gas price tolerance value
        standard_payment (bool): Whether this is a standard payment
    """

    def __init__(self, payment_amount: int, gas_price_tolerance: int, standard_payment: bool) -> None:
        """
        Initialize a payment limit.

        Args:
            payment_amount (int): The maximum payment amount in motes
            gas_price_tolerance (int): The gas price tolerance value
            standard_payment (bool): Whether this is a standard payment
        """
        self.payment_amount = payment_amount
        self.gas_price_tolerance = gas_price_tolerance
        self.standard_payment = standard_payment

    def to_bytes(self) -> bytes:
        """
        Serialize the payment limit to bytes.

        The serialization includes:
        - Payment type (0 for limited)
        - Payment amount as u64
        - Gas price tolerance as u32
        - Standard payment flag as u32

        Returns:
            bytes: The serialized payment limit
        """
        table = CalltableSerialization()
        table.add_field(0, int(0).to_bytes()) \
            .add_field(1, self.payment_amount.to_bytes(8, byteorder='little')) \
            .add_field(2, self.gas_price_tolerance.to_bytes()) \
            .add_field(3, int(self.standard_payment).to_bytes())
        return table.to_bytes()

    def to_json(self) -> Dict[str, Any]:
        """
        Convert the payment limit to a JSON representation.

        Returns:
            Dict[str, Any]: The JSON representation of the payment limit
        """
        return {
            JSONNAME.PAYMENTLIMITED: {
                JSONNAME.PAYMENT_AMOUNT: self.payment_amount,
                JSONNAME.GAS_PRICE_TOLERACE: self.gas_price_tolerance,
                JSONNAME.STANDARD_PAYMENT: self.standard_payment
            }
        }
