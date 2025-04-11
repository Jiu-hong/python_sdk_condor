"""Put transaction RPC module.

This module provides functionality for sending transactions to the Casper network
via the account_put_transaction RPC method.
"""

from typing import Dict, Any

import requests

from ..constants import RpcMethod


RPCMETHOD = RpcMethod()


class PutTransction:
    """Class for handling the account_put_transaction RPC call.

    This class allows sending transactions to the Casper network and
    receiving the response.
    """

    def __init__(self, url: str, transactionV1: Dict[str, Any]) -> None:
        """Initialize a PutTransction instance.

        Args:
            url: The RPC endpoint URL.
            transactionV1: The transaction data to send.
        """
        self.url = url
        self.rpc_payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": RPCMETHOD.ACCOUNT_PUT_TRANSACTION,
            "params": transactionV1
        }

    def run(self) -> Dict[str, Any]:
        """Send the transaction to the network.

        Returns:
            The JSON response from the RPC call.

        Raises:
            requests.exceptions.RequestException: If the RPC call fails.
        """
        response = requests.post(self.url, json=self.rpc_payload)
        if response.status_code == requests.codes.ok:
            return response.json()
