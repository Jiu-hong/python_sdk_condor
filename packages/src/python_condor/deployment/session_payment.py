"""Session payment module.

This module provides functionality for handling payment sessions in Casper network deployments.
"""

from typing import Any, Dict, Union

from ..cl_values import CLU512
from ..constants import JsonName
from .deploy_name_arg import DeployNamedArg


JSONNAME = JsonName()


class SessionPayment:
    """Class for managing payment sessions.

    This class handles the creation and management of payment sessions
    in Casper network deployments. It provides methods for converting
    payment sessions to bytes and JSON formats.
    """

    def __init__(self, payment_amount: Union[int, str]) -> None:
        """Initialize a payment session.

        Args:
            payment_amount: The amount to be paid, can be an integer or string.

        Raises:
            ValueError: If the payment amount is invalid.
        """
        self.payment_amount = DeployNamedArg(
            {JSONNAME.AMOUNT: CLU512(payment_amount)}
        )

    def to_bytes(self) -> bytes:
        """Convert the payment session to bytes.

        The bytes representation includes:
        - Module bytes tag (0x00)
        - Module bytes length (0)
        - Empty module bytes
        - Serialized payment amount

        Returns:
            Bytes representation of the payment session.
        """
        # Tag ModuleBytesTag = '00'
        module_bytes_tag = int(0).to_bytes()

        # Length is 0
        module_bytes_length = int(0).to_bytes(4, byteorder='little')

        # Module bytes is null
        module_bytes = b''

        return (
            module_bytes_tag +
            module_bytes_length +
            module_bytes +
            self.payment_amount.serialize()
        )

    def to_json(self) -> Dict[str, Any]:
        """Convert the payment session to JSON format.

        The JSON representation includes:
        - Payment section
        - Module bytes section with empty bytes
        - Arguments section with payment amount

        Returns:
            Dictionary containing the payment session in JSON format.
        """
        return {
            JSONNAME.PAYMENT: {
                JSONNAME.MODULEBYTES: {
                    JSONNAME.MODULE_BYTES: "",
                    JSONNAME.ARGS: self.payment_amount.to_json()
                }
            }
        }
